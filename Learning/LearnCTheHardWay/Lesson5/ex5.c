#include <stdio.h>

/* This is a comment.
function returns an int
takes two arguments:
argc, an int, is the number of arguments
*argv, a pointer to the stored character array containing the arguments
*/
int main( int argc, char *argv[] )
{
    int distance = 100;

    // this is also a comment
    printf("You are %d miles away.\n", distance);

    return 0; // Return value of the function
}