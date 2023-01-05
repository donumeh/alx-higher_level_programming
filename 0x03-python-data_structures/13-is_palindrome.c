#include <stdio.h>
#include <stddef.h>
#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: the head of the linked list
 *
 * Return: 0 if it is not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	unsigned int count = 0;
	int *array;
	unsigned int i = 0, r_value = 1;

	h = *head;
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	h = *head;

	array = malloc(sizeof(int) * count);
	if (array == NULL)
	{
		printf("Malloc Error\n");
		return (0);
	}

	while (h != NULL)
	{
		array[i] = h->n;
		h = h->next;
		i++;
	}

	h = *head;
	while (h != NULL)
	{
		int n, x; 

		n = h->n;
		x = array[i];

		if (n != x)
		{	
			printf("%d %d\n", x, n);
			r_value = 0;
			break;
		}
		i--;
		h = h->next;
	}
	free(array);
	return (r_value);
}
