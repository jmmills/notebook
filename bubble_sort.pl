use strict;
use warnings;
use Data::Dumper;

sub bubble_sort {
	my @a = @_;
	for my $i (0 .. $#a ) {
		for my $j ( $i + 1 .. $#a ) {
			$a[$j] < $a[$i] and @a[$i, $j] = @a[$j, $i]
		}
	}
	return @a;
}

my @list = map {
	int(rand(1000));
} (1..int(rand(25)));

warn Dumper(\@list);
warn "---";

warn Dumper([bubble_sort(@list)]);

