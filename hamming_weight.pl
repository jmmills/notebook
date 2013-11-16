use 5.14.0;
use Benchmark qw(:all);

sub count_bits {
	my $num = shift or return 0;
	state $bits = [ map { 1 << $_ } (0..15) ];
	return scalar grep { ($num & $_) } @{ $bits };
}

sub hamming_weight {
	my $i = shift or return 0;
	my $c   = 0;

	while($i) {
		$c++ if $i & 1;
		$i >>= 1;
	}

	return $c;
}

sub popcount_4 {
	my ($i,$c) = (shift);

	for($c=0; $i; $c++) {
		$i &= ($i - 1) 
	}

	return $c;
}

my @random_set_of_int = map { int(rand(6535)) } (0..1000+rand(1000));

my $sum = 0;
$sum += count_bits($_) foreach(@random_set_of_int);
say "Old way: $sum";

$sum = 0;
$sum += hamming_weight($_) foreach(@random_set_of_int);
say "New way: $sum";

$sum = 0;
$sum += popcount_4($_) foreach(@random_set_of_int);
say "Popcount way: $sum";


timethese( 5000, {
	'old' => sub {
		my $sum = 0;
		$sum += count_bits($_) foreach(@random_set_of_int);
	},
	'reg' => sub {
		my $sum = 0;
		$sum += hamming_weight($_) foreach(@random_set_of_int);
	},
	'pop' => sub {
		my $sum = 0;
		$sum += popcount_4($_) foreach(@random_set_of_int);
	}
});


