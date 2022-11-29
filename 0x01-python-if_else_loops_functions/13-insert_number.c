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

	current = *head;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if (current == NULL)
	{
		current = temp;
		return (*head);
	}
	else
	{
		while (current != NULL)
		{
			if (current->n >= number)
			{
				temp->next = current;
				prev->next = temp;
				return (*head);
			}
			prev = current;
			current = current->next;
		}
	}


	return (NULL);
}
