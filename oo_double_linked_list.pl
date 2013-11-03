package List;
use Mouse;

has 'first' => (is => 'rw', isa => 'Node');
has 'last' => (is => 'rw', isa => 'Node');

sub new_node {
	my $self = shift;
	my $node = Node->new(list => $self, @_);

	unless ($self->first) {
		$self->first($node);
		$self->last($node); 
	}

	return $node;
}

sub add_node_to_end {
	my $self = shift;
	my $node = shift;
	
	$self->last->insert_after($node);
}

sub add_node_to_start {
	my $self = shift;
	my $node = shift;

	$self->first->insert_before($node);
}

sub names {
	my $self = shift;
	my $dsc  = shift; # True is descending

	return map { $_->name } ($dsc ? $self->last->recurse_desc : $self->first->recurse_asc);
}

1;

package Node;
use Mouse;

has 'list' => (is => 'rw', isa => 'List');
has 'name' => (is => 'rw', isa => 'Str');
has 'next' => (is => 'rw', isa => 'Node');
has 'last' => (is => 'rw', isa => 'Node');

sub is_last {
	my $self = shift;
	return $self->list->last eq $self;
}

sub is_first {
	my $self = shift;
	return $self->list->first eq $self;
}

sub is_linked {
	my $self = shift;
	return ref($self->next) eq 'Node' || $self->($self->last) eq 'Node';
}

sub insert_after {
	my $self = shift;
	my $node = shift;
	my $old  = $self->next;

	$node->last($self);
	$node->next($old) if $old;

	$self->next($node);
	$self->list->last($node) unless $node->next;
}

sub insert_before {
	my $self = shift;
	my $node = shift;
	my $old  = $self->last;

	$node->last($old) if $old;
	$node->next($self);

	$self->last($node);
	$self->list->first($node) unless $node->last;
}

sub recurse_asc {
	my $self = shift;
	return $self->next ? ($self, $self->next->recurse_asc) : ($self);
}

sub recurse_desc {
	my $self = shift;
	return $self->last ? ($self, $self->last->recurse_desc) : ($self);
}


1;

package main;

use Data::Dumper;
use Test::More;

my $list = new_ok 'List';

my $first_node;
ok $first_node = $list->new_node(name => 'first');

ok $list->add_node_to_end( $list->new_node(name => $_) ) for('a'..'z');

ok $list->first->name eq 'first', 'first is first';

ok $list->last->name eq 'z', 'last is z' or diag sprintf("last name is '%s'", $list->last->name);

ok !$list->first->last, 'first does not have something before it';

ok !$list->last->next, 'last does not have something after it';

my @asc = ('first', 'a'..'z');
my @dsc = ('a'..'z','first');

is @asc, $list->names, 'list is linked correctly ascending';
is @dsc, $list->names(1), 'list is linked correctly descending';

done_testing();

1;
