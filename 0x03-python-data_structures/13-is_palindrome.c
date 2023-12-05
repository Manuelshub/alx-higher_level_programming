#include "lists.h"

/**
 * reverse_list - reverses a linked list.
 * @head: he start of the list.
 *
 * Return: the pointer to the newly reversed link.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev, *current, *next;

	if (head == NULL)
		return (NULL);
	current = head;
	prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	head = prev;
	return (head);
}

/**
 * is_palindrome - checks if a linked list is palindrome.
 * @head: the pointer to the linked list.
 * Return: 1 if it is palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *curr, *second, *next;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = curr = next = *head;
	while (1)
	{
		temp = temp->next->next;
		if (temp == NULL || temp->next == NULL)
		{
			second = curr->next->next;
			break;
		}
		curr = curr->next;
	}
	curr->next = NULL;
	second = reverse_list(second);
	while (second != NULL)
	{
		if (second->n == (*head)->n)
		{
			*head = (*head)->next;
			second = second->next;
		}
		else
			return (0);
	}
	return (1);
}
