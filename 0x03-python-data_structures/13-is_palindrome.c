#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: head of listint_t
 * @n: int to add in listint_t list
 * Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}

/**
 * is_palindrome - identify if a single linked list is palindrome
 * @head: head of listint_t
 * Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed_list = NULL;
	listint_t *original_list = *head;

	if (original_list == NULL || original_list->next == NULL)
		return (1);

    	/* Create a reversed copy of the original list */
	while (original_list != NULL)
	{
		add_nodeint(&reversed_list, original_list->n);
		original_list = original_list->next;
	}

	/* Compare the original list with the reversed list */
	while (*head != NULL)
	{
		if ((*head)->n != reversed_list->n)
		{
			free_listint(reversed_list);
			return (0);
		}

		*head = (*head)->next;
		reversed_list = reversed_list->next;
	}

	/* Free the reversed list */
	free_listint(reversed_list);
	return (1);
}
