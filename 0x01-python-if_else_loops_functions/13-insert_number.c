#include "lists.h"
#include <stdio.h>


/**
 * insert_node - insert node
 * @head: linked list
 * @number: number to add to the list
 * Return: new node, NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr, *prev;

	new = (listint_t *)malloc(sizeof(listint_t *));
	if (!new)
		return (NULL);

	new->n = number;

	if (!head)
		*head = new;
	else
	{
		ptr = *head;
		prev = ptr;

		while (ptr)
		{
			ptr = ptr->next;
			if (ptr->n < number)
				prev = ptr;
			else
				break;
		}
		new->next = ptr;
		prev->next = new;

	}
	return (new);
}
