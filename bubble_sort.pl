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

sub bubble_sort_2 {
	for (my $a = 0; $a < $#_; $a++) {
		for (my $b = 0; $b < $#_ ; $b++) {
			if ($_[$b] < $_[$a]) {
				@_[$a, $b] = @_[$b, $a]
			}
			
		}
	}
}

my @list = map {
	int(rand(1000));
} (1..int(rand(25)));

warn Dumper(\@list);
warn "---";
warn Dumper([bubble_sort(@list)]);

bubble_sort_2(@list);

warn "---";
warn Dumper([bubble_sort(@list)]);
