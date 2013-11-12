#!/usr/bin/env perl

use 5.12.1;
use Mouse;

for ( my @seq = (1,2); $seq[2] = $seq[0] + $seq[1] <= 4_000_000; shift @seq ) {
    say $seq[2] 
}
