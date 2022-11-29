#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the head of the linked list
 * @number: the value to be passed
 * Return: head of the linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *temp;
	listint_t *prev;
	listint_t *h;
	
	h = *head;
	current = *head;

	while (current != NULL)
	{
		if (current->n >= number)
		{
			temp = malloc(sizeof(listint_t));
			if (temp == NULL)
			{
				return (NULL);
			}
			temp->n = number;
			temp->next = current;
			prev->next = temp;
			return (h);
		}
		prev = current;
		current = current->next;
	}
	return (NULL);
}
