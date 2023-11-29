#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list.
 * @head: the head of the list.
 * @number: the number to be inserted.
 * Return: the address of the new_node of NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);			
	new_node->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	temp = *head;
	prev = NULL;
	while (temp != NULL && new_node->n > temp->n)
	{
		prev = temp;
		temp = temp->next;
	}
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = temp;
	}
	return (new_node);
}
