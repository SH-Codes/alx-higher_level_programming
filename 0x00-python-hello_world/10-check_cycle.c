#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list.
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
