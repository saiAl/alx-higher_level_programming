#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *prev;

	if (!list)
		return (NULL);

	current = list;
	prev = current;
	while (current->next != NULL)
	{
		current = current->next;
		if (current->n == prev->n)
			return (1);
	}
	return (0);
}
