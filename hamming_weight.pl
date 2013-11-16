use 5.14.0;

sub count_bits {
	my $num = shift or return 0;
	state $bits = [ map { 1 << $_ } (0..15) ];
	return scalar grep { ($num & $_) } @{ $bits };
}

my @random_set_of_int = map { int(rand(6535)) } (0..1000+rand(1000));

my $sum = 0;

$sum += count_bits($_) foreach(@random_set_of_int);

say $sum;
