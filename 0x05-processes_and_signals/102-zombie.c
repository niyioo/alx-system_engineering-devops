#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Function to create an infinite loop
 *
 * Description: This function creates an infinite loop that sleeps for 1 second
 * in each iteration, effectively putting the process to sleep indefinitely.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program
 *
 * Description: This function is the entry point of the program. It creates 5
 * child processes, and for each child process, it displays a message indicating
 * that a zombie process is created along with the PID of the zombie process.
 * The program then enters an infinite loop using the infinite_while function.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int i = 0;
	pid_t zombie_pid;

	while (i < 5)
	{
		zombie_pid = fork();
		if (!zombie_pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)zombie_pid);
		i++;
	}
	if (zombie_pid != 0)
	{
		infinite_while();
	}
	return (0);
}
