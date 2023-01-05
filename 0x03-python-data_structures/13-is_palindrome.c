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
	int i = 0;

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
	i = 0;
	while (h != NULL)
	{
		if (h->n != array[i])
			return (0);
		i++;
		h = h->next;
	}

	return (1);

}
