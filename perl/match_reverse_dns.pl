#!/usr/bin/perl 

$|++;
use 5.14.0;
use warnings;
use Net::DNS::Async;
use Net::DNS::Resolver;

my $c = Net::DNS::Async->new(QueueSize => 256, Retries => 3);

foreach(@ARGV) {
	my $input_name = $_;
	$c->add( sub {
		my $n = $input_name;
		my $a = shift;
		my $ptr = ($a->answer)[0]
			or return say "$n has no record";
		
		return say "$n isn't a ptr"
			unless ref($ptr) eq 'Net::DNS::RR::PTR';

		my $ptrdname = $ptr->ptrdname;

		$c->add( sub {
			my @answer = shift->answer;
			my @results = grep {
				ref($_) eq 'Net::DNS::RR::A' &&
				$_->address eq $input_name
			} @answer;

			say sprintf("%s => %s, %s",
				$input_name,
				$ptrdname,
				scalar(@results)? $results[0]->address : '!'
			);
		}, $ptrdname );

	}, $input_name);
}

$c->await;
