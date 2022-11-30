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
	prev = NULL;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;

	if (*head == NULL)
	{
		*head = temp;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->n >= number)
			{
				temp->next = current;
				if (prev)
				{
					prev->next = temp;
				}
				else
					*head = temp;
				return (*head)
			}
			prev = current;
			current = current->next;
			return (*head);
		}

		current->next = temp;
	}

	return (*head);
}
