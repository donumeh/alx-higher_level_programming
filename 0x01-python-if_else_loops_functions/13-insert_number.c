#include "lists.h"

int count_node(listint_t *);
listint_t *node_at_center(listint_t *, int);
void fix_node(listint_t *, listint_t *, int, int, listint_t *);

/**
 * fix_node - fix in the node to the pos
 * @node_mid: the middle of the linked list
 * @head: the head of the linked list
 * @mid_pos: the pos of middle node
 * @call: yes or no validation
 * @new: the new node to insert
 *
 * Return: void
 */

void fix_node(listint_t *node_mid, listint_t *head, int mid_pos,
		int call, listint_t *new)
{
	listint_t *prev;

	if (call == 0)
	{
		int i = 0;

		while (i < mid_pos)
		{
			if (head->n > new->n)
			{
				new->next = head;
				prev->next = new;
				return;
			}
			prev = head;
			head = head->next;
			i++;
		}
	}
	else
	{
		while (node_mid->next != NULL)
		{
			if (node_mid->n > new->n)
			{
				new->next = node_mid;
				prev->next = new;
				return;
			}
			prev = node_mid;
			node_mid = node_mid->next;
		}
		node_mid->next = new;
	}
}


/**
 * node_at_center - prints the node at the center
 * @head: the head of the linked list
 * @mid_node: position of the node at middle
 *
 * Return: the address to the node at the center
 */

listint_t *node_at_center(listint_t *head, int mid_node)
{
	int i = 0;

	while (i < mid_node)
	{
		head = head->next;
		i++;
	}

	return (head);
}




/**
 * count_node - counts the number of node in a linked list
 * @head: the head of the node
 *
 * Return: the number of node found
 */

int count_node(listint_t *head)
{
	int i = 0;

	while (head != NULL)
	{
		i++;
		head = head->next;
	}
	return (i);
}



/**
 * insert_node - inserts a node in a sorted list
 * @head: the head of the linked list
 * @number: the value to insert
 *
 * Return: the address of the new node of NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL;
	listint_t *node_mid = NULL;
	int num_of_nodes = 0, div_node = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}

	num_of_nodes = count_node(current); /* counts the nodes */
	div_node = num_of_nodes / 2; /* divide the node to find middle */
	node_mid = node_at_center(current, div_node); /* node at mid */

	if (node_mid->n > new->n)
	{
		fix_node(node_mid, current, div_node, 0, new);
		/* check the node_mid to the end of node */
	}
	else
	{
		fix_node(node_mid, current, div_node, 1, new);
		/* check the pos 0 to the node_mid */
	}

	return (*head);
}
