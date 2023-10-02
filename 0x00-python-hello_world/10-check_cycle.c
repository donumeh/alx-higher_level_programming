#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the linked list
 *
 * Return: returns 0 if there's no cycle or 1 if there's a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
