/*
 * =====================================================================================
 *
 *       Filename:  1.c
 *
 *    Description:  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *    Find the sum of all the multiples of 3 or 5 below 1000.
 *
 *        Version:  1.0
 *        Created:  11/16/2013 19:47:16
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jason M. Mills (jmm), jason@yarp.me
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>

int main(void) {

	int sum = 0;

	for(int i = 0; i < 1000; i++) {
		int n3 = i % 3;
		int n5 = i % 5;

		if ( !n3 || !n5 ) {
			sum++;
		}
	}


	printf("Sum: %i\n", sum);
}
