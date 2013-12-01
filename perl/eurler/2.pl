#!/usr/bin/env perl

use 5.12.1;

my $sum = 2;

for ( my @seq = (1,2); ($seq[2] = $seq[0] + $seq[1]) <= 4_000_000; shift(@seq) ) {
    say $seq[2];
    $sum += !($seq[2] % 2)? $seq[2] : 0;
}

say "Sum: $sum";