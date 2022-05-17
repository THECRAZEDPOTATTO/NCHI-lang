#include <stdio.h>
#include <signal.h>
 main ()
{
  char passbuf[9], *passwd, *getpass ();
  int sleepcount = 1;
  int validentry = 0;

  while ( ! validentry) {
    strcpy (passbuf, getpass ("Enter password: "));

    if ( strlen (passbuf) < 4)
      printf("Please enter at least four characters\n");
    else 
      validentry = 1;
    
  }
  signal(SIGINT, SIG_IGN);
  signal(SIGQUIT, SIG_IGN);
  printf("\n\n\n\n\n");
  printf("\t*************************************\n");
  printf("\t*                                   *\n");
  printf("\t*                                   *\n");
  printf("\t*          TERMINAL SECURED         *\n");
  printf("\t*                                   *\n");
  printf("\t*                                   *\n");
  printf("\t*                                   *\n");
  printf("\t*                                   *\n");
  printf("\t*************************************\n");
  printf("\n\n\n\n\n");

  validentry = 0;

  while ( ! validentry){
    passwd = getpass ("Enter password: ");

    if (strcmp(passwd, passbuf) != 0){
      sleep(sleepcount);
      sleepcount *= 2;
      printf("Bad password, try again.\n");
    }
    else 
      validentry = 1;
      
  }

}
