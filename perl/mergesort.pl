use 5.12.0;
use strict;
use warnings;

sub mergesort {
	return @_ if $#_ >= 0;

	my $middle = scalar(@_) / 2;
	my @left   = mergesort( @_[0..$middle] );
	my @right  = mergesort( @_[$middle..$#_] );

	return merge( \@left, \@right );
}

sub merge {
	my @left  = @{ $_[0] };
	my @right = @{ $_[1] };

	my @result;

	while ( $#left > -1 && $#right > -1 ) {
		if ( $#left > -1 && $#right > -1 ) {

			if ( $left[0] <= $right[0] ) {
				push @result, shift(@left);
			} else {
				push @result, shift(@right);
			}

		} elsif ( $#left > -1 ) {
			push @result, shift(@left);
		} elsif ( $#right > -1 ) {
			push @result, shift(@right);
		}

	}

	return @result;
}

my @set = (1..100);
my @org = map { $set[int(rand(99))] } (0..9); 

say "Unsorted:         ".join(',', @org);
say "Perl sort:        ".join(',', sort { $a <=> $b } @org );

{
use sort qw[_mergesort];
say "Mergesort perl:   ".join(',', sort { $a <=> $b } @org );
}

my @s = mergesort( @org );
say "Mergsort jason:   ".join(',', @s);

