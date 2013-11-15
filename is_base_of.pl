#!/usr/bin/env perl

sub is_base_of {
    my ($number, $base) = @_;
    return ( log($number) / log($base) ) =~ /\D+/;
}