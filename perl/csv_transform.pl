#!/usr/bin/env perl

use 5.12.0;
use warnings;
use Text::CSV_XS;

my $fn = $ARGV[0]
	or die "Usage: $0 <filename>\n";

my $csv = Text::CSV_XS->new({ binary => 1 });

open my $fh, "<:encoding(utf8)", $fn
	or die "Error with file '$fn': $!";

while ( my $row = $csv->getline($fh) ) {
	my @new = @{$row};

# transform code here

	$csv->print( *STDOUT, \@new );
}
