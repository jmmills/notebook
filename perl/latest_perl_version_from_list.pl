use 5.12.0;
use version;
say [ map { $_->[0] } grep {  $_->[1] % 2 != 1 } map { [ "$_", sprintf("%.3f", $_->numify) * 1000 ] } sort { $b <=> $a } map { eval { version->parse($_) }; } <> ]->[0];
