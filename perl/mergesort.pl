use 5.12.0;
use strict;
use warnings;
use Benchmark;

sub mergesort {
	return @_ if $#_ == 0;

	my $mid = int @_ / 2;

	my @left = mergesort( @_[0..$mid - 1] );
	my @right = mergesort( @_[$mid..$#_] );

	return merge(\@left, \@right);
}

sub merge {
	my @left = @{ shift(@_) };
	my @right = @{ shift(@_) };

	my @return;
	while( @left && @right ) {
		if ( $left[0] <= $right[0] ) {
			push @return, shift(@left);
		} else {
			push @return, shift(@right);
		}
	}

	push @return, @left if @left > 0;
	push @return, @right if @right > 0;

	return @return;
}

my @set = (1..100);
my @org = map { $set[int(rand(99))] } ( 0 .. (1 + int(rand(20))) ); 

say "Unsorted:         ".join(',', @org);
say "Perl sort:        ".join(',', sort { $a <=> $b } @org );

{
use sort qw[_mergesort];
say "Mergesort perl:   ".join(',', sort { $a <=> $b } @org );
}

my @s = mergesort( @org );
say "Mergesort jason:  ".join(',', @s);

exit if defined($ENV{NO_BENCH});

my $iter = 1_000_000;

timethese( $iter, {
	'perl native sort' => sub { sort { $a <=> $b } @org },
	'jason merge sort' => sub { mergesort( @org ); }
});

{
	use sort '_mergesort';
	timethese( $iter, {
		'perl native mergesort' => sub { sort { $a <=> $b } @org }
	});
}
