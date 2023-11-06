#include "lists.h"

int counter(listint_t **head);

/**
 * is_palindrome - function checks if a singly linked list is a palindrome
 * @head: singly linked list
 * Return: 0 if not palindrome, 1 otherwise.
 */

int is_palindrome(listint_t **head)
{
	int count, i = 0, j;
	listint_t *next, *prev;

	if (!head)
		return (1);

	count = counter(head);
	if (count == 0)
		return (1);

	while (*head)
	{
		next = prev = *head;
		for (j = 0; j < i; j++)
			next = next->next;
		for (j = 0; j < (count - (i + 1)); j++)
			prev = prev->next;

		if (next->n == prev->n)
			i++;
		else
			return (0);
	}
	return (1);
}

/**
 * counter - function checks the size of a linked list
 * @head: singly linked list
 * Return: the size of the list.
 */

int counter(listint_t **head)
{
	int count = 0;

	while (*head != NULL)
	{
		*head = (*head)->next;
		count++;
	}
	return (count);
}
