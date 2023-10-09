#include "lists.h"

listint_t *init_new_list(listint_t **);
listint_t *reverse_linked_list(listint_t **head);

/**
 * reverse_linked_list - reverses a linked list
 * @head: the head of a linked list
 *
 * Return: the reversed linked list
 */

listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *prev, *next;

	if (head == NULL || *head == NULL)
		return (NULL);

	prev = next = NULL;

	while ((*head)->next != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	(*head)->next = prev;
	return (*head);
}



/**
 * init_new_list - initializes the old list into a new list
 * @head: the head
 *
 * Return: the init linked list
 */

listint_t *init_new_list(listint_t **head)
{
	listint_t *tmp = *head, *new_head = NULL;

	while (tmp != NULL)
	{
		add_nodeint_end(&new_head, tmp->n);
		tmp = tmp->next;
	}

	return (reverse_linked_list(&new_head));
}


/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list
 *
 * Return: 0 if not a palindrome, 1 if otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *new_head, *tmp, *tmp1;

	if (head == NULL || *head == NULL)
		return (1);

	new_head = init_new_list(head);

	tmp = *head;
	tmp1 = new_head;
	while (tmp != NULL && tmp1 != NULL)
	{
		if (tmp->n != tmp1->n)
		{
			free_listint(new_head);
			return (0);
		}
		tmp = tmp->next;
		tmp1 = tmp1->next;
	}
	free_listint(new_head);

	return (1);
}
