#include <stdio.h>

int main( int argc, char *argv[] )
{
	puts("Hello world.");

	//  -- Extra Credit -- 
	// 1) Open the ex1 file in your text editor and change or delete random parts.
	// Try running it and see what happens.

	// 2) Print out 5 more lines of text or something more complex than hello world.
	puts("more");
	puts("complex");
	puts("than");
	puts("hello");
	puts("world");

	/* 3) Run man 3 puts and read about this function and many others.
	int fputc( int c, FILE *stream )
		writes the character c, cast to an unsigned char, to stream
	int fputs( const char *s, FILE *stream )
		writes string s to stream, without its terminating null byte
	int putc( int c, FILE *stream )
		equivilent to fputc, except it can be implemented as a macro which
		evaluates stream more than once
	int putchar( int c )
		equivilent to putc( c, stdout )
	int puts( const char *s )
		writes string s and a trailing newline to stdout
	*/


	return 0;
}