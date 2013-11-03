package BSTree;
use Mouse;

has 'value' => (is => 'rw', isa => 'Str');
has 'left' => (is => 'rw', isa => 'BSTree');
has 'right' => (is => 'rw', isa => 'BSTree');
has 'parent'=> (is => 'rw', isa => 'BSTree');

sub add_left {
	my $self = shift;
	return $self->left( BSTree->new( parent => $self, value => shift ) );
}

sub add_right {
	my $self = shift;
	return $self->right( BSTree->new( parent => $self, value => shift ) );
}

sub add_sibling {
	my $self = shift;
	return defined($self->parent->left) && $self->parent->left == $self? $self->parent->add_right(@_) : $self->parent->add_left(@_);
}

sub search { 
	my $self = shift;
	my $value = shift;

	my @return;
	return grep { defined($_) } (
		$self->value eq $value? $self : undef,
		$self->left? $self->left->search($value) : undef,
		$self->right? $self->right->search($value) : undef
	);
}

1;

package main;
use Data::Dumper;
use Test::More;

my $tree = new_ok 'BSTree' => [value => 'd'];

$tree->add_left( 'd' )->add_right('e')->add_sibling('x')->parent->right->add_left('e')->add_sibling('x')->add_right('e');

diag Dumper( [
	map { $_->value } $tree->search('e') 
] );
done_testing;
