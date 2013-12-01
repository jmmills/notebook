package BSTree;
use 5.12.0;
use Mouse;

has 'value' => (is => 'ro', isa => 'Str');
has 'left' => (is => 'ro', isa => 'BSTree', writer => '_set_left');
has 'right' => (is => 'ro', isa => 'BSTree', writer => '_set_right');
has 'parent'=> (is => 'ro', isa => 'BSTree');

sub add_left {
	my $self = shift;
	return $self->_set_left( BSTree->new( parent => $self, value => shift ) );
}

sub add_right {
	my $self = shift;
	return $self->_set_right( BSTree->new( parent => $self, value => shift ) );
}

sub add_sibling {
	my $self = shift;
	return undef if defined($self->parent->left) && defined($self->parent->right);
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
