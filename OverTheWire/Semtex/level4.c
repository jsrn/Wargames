#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <stdio.h>
#include <sys/syscall.h>
#include <sys/reg.h>

#define TARGET "/semtex/semtex4"
#define NEW_UID 0

int main() {
  int status = 0;
	int entering = 1;
	long cur_eax;
	int pid = fork();
	if ( !pid ) {
		ptrace( PTRACE_TRACEME, 0, 0, 0 );
		execlp( TARGET, TARGET, 0 );
	} else {
		wait( &status );

		while ( 1 ) {
			// Notified on every syscall
			ptrace( PTRACE_SYSCALL, pid, 0, 0 );
			wait( &status );

			// Exit if the child has terminated
			if ( WIFEXITED( status ) ) break;

			// read the child's registers
			cur_eax = ptrace(PTRACE_PEEKUSER,
                         pid, 4*ORIG_EAX,
                         NULL);

			if ( cur_eax == SYS_geteuid32 ) {
				if(entering == 1){
               		entering = 0;
       			} else {
					printf("Exiting geteuid32, ready to rock\n");
               		entering = 1;
               		long retval = ptrace(PTRACE_PEEKUSER,
                         				pid, 4 * EAX,
                         				NULL);
                         printf("Old return value: %ld\n",retval);
               		ptrace(PTRACE_POKEUSER, pid, 4 * EAX, 6005L);
               		long newret = ptrace(PTRACE_PEEKUSER,
                       					pid, 4 * EAX,
                         				NULL);
               		printf("New return value: %ld\n",newret);
				}
			}
		}
	}
	return 0;
}
