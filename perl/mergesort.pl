use 5.12.0;
use warnings;
use Test::More;

sub mergesort {
	return @_ if $#_ >= 1;

	my $middle = scalar(@_) / 2;
	my @left   = mergesort( @_[0..$middle] );
	my @right  = mergesort( @_[$middle..$#_] );

	return merge( \@left, \@right );
}

sub merge {
	my @left  = @{ $_[0] };
	my @right = @{ $_[0] };

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

my @n = (9..0);

say join(',', @n);

my @s = mergesort( @n );
say join(',', @s);

{
	use sort '_mergesort'
	say join(',', sort(@n));
}
