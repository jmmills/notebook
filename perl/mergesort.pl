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

	while ( scalar(@left) && scalar(@right) ) {
		if ( scalar(@left) && scalar(@right) ) {

			if ( $left[0] <= $right[0] ) {
				push @result, shift(@left);
			} else {
				push @result, shift(@right);
			}

		} elsif ( scalar(@left) ) {
			push @result, shift(@left);
		} elsif ( scalar(@right) ) {
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
say "Mergesort jason:  ".join(',', @s);

