#include <stdio.h>
#include "lists.h"

int count_node(listint_t **);
void reverse_linked_list(listint_t **);


/**
 * compare_linked_list - compares a linked list
 * @head1: the first head to test
 * @head2: the second head to test
 *
 * Return: 0 if not same, 1 if same
 */

int compare_linked_list(listint_t **head1, listint_t **head2)
{
	listint_t *tmp1, *tmp2;

	tmp1 = *head1;
	tmp2 = *head2;
	while (tmp1 && tmp2)
	{
		if (tmp1->n != tmp2->n)
		{
			return (0);
		}

		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}

	return (1);
}



/**
 * reverse_linked_list - reverses a linked list
 * @head: the head to the lists to reverse
 *
 * Return: void
 */

void reverse_linked_list(listint_t **head)
{
	listint_t *current, *prev, *next;

	prev = next = NULL;

	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}





/**
 * count_node - counts the number of node in a linked list
 * @head: the head of a node to count
 *
 * Return: number of nodes in a linked list
 */

int count_node(listint_t **head)
{
	int i = 0;
	listint_t *tmp = *head;

	while (tmp != NULL)
	{
		i++;
		tmp = tmp->next;
	}

	return (i);
}


/**
 * is_palindrome - checks if a sequence of node is a palindrome
 * @head: the head of a linked list
 *
 * Return: 0 if not a palindrome, 1 if otherwise
 */


int is_palindrome(listint_t **head)
{
	int nodes, mid_node, i, is_palin_check;
	listint_t *tmp, *second_part, *first_part;

	is_palin_check = 0;
	tmp = *head;
	first_part = *head;
	nodes = count_node(&tmp);
	mid_node = nodes / 2;

	i = 0;
	while (i < mid_node - 1)
	{
		tmp = tmp->next;
		i++;
	}

	second_part = tmp->next;
	tmp->next = NULL;

	reverse_linked_list(&second_part);

	is_palin_check = compare_linked_list(&first_part, &second_part);

	reverse_linked_list(&second_part);

	while (first_part->next != NULL)
		first_part = first_part->next;

	first_part->next = second_part;

	return (is_palin_check);
}
