#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all elements of a listint_t list
 * @h: Pointer to the head of the list
 * Return: Number of nodes
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a listint_t list
 * @head: Pointer to a pointer to the head of the list
 * @n: Integer to be included in the new node
 * Return: Address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list
 * @head: Pointer to the head of the list
 * Return: void
 */
void free_listint(listint_t *head);

/**
 * insert_node - Inserts a node in a sorted listint_t list
 * @head: Pointer to a pointer to the head of the list
 * @number: Integer to be included in the new node
 * Return: Address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
