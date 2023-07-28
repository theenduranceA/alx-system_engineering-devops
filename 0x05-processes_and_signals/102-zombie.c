#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Sleeps infinitely
 *
 * Return: 0
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
 * main - Function that creates 5 zombie processes
 *
 * Return: Always 0 on success.
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; ++i)
	{
		pid = fork();
		if (pid < 0)
			return (0);
		else if (!pid)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
