use Test::More;
use Benchmark;
use 5.12.0;

my $l = chr( $ARGV[0] ) || die $!;
my @a = sort { $a > $b } map { chr($_) } ('a'..'z', 'A'..'Z');

plan tests => 1;

ok( search(\@a, $l, 0, scalar(@a), 1) == 1, "$l in array" )
	or die "Benchmark for matches only";

timethese( 1_000_000, {
	search_noint => sub { search( \@a, $l, 0, scalar(@a), 0 ) }, 
	search_int => sub { search( \@a, $l, 0, scalar(@a), 1 ) } 
});

sub mid_a { return ( $_[0] + $_[1] ) / 2; }
sub mid_b { return int ( ( $_[0] + $_[1] ) / 2 ); }

sub search {
	my ($ref, $str, $left, $right, $flag ) = @_;

	return undef if $right < $left;

	while ( $left <= $right ) {
		my $mid = $flag? mid_b( $left, $right ) : mid_a( $left, $right );
		
		return 1 if $ref->[$mid] == $str;
		
		return $str < $ref->[$mid]?
			search( $ref, $str, $left, $mid-- ) :
			search( $ref, $str, $mid++, $right );
	}

	return undef;
}
