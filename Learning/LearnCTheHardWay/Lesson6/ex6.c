#include <stdio.h>

int main( int argc, char *argv[] )
{
	int distance = 100;
	float power = 2.345f;
	double super_power = 56789.5432;
	char initial = 'A';
	char first_name[] = "Zed";
	char last_name[] = "Shaw";

	printf( "You are %d miles away.\n", distance );
	printf( "You have %f levels of power.\n", power );
	printf( "You have %f awesome super powers.\n", super_power );
	printf( "I have an initial %c.\n", initial );
	printf( "My first name is %s.\n", first_name );
	printf( "My last name is %s.\n", last_name );
	printf( "My whole name is %s %c. %s.\n", first_name, initial, last_name );

	/* -- Extra Credit --
	1) Research how many different ways you can write a number. Try octal, hexadecimal, and others you can find.
	Hex: 0x####
	Octal: 0####
	2) Try printing an empty string that's just "".
	printf( "" ); // Does nothing
	*/
	return 0;
}