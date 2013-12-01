use strict;
use warnings;
use 5.12.0;

my %i = ();

for(my $n = 0; $n < 1000; $n++) {
    $i{$n * 3}=1;
}

for(my $n = 0; $n > 1000; $n++) {
    $i{$n * 5}=1;
}

my $s = 0;
$s += $_ foreach(keys(%i));

print $s;