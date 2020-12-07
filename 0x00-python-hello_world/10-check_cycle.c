#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
* check_cycle - check if exist cycle in a list
* @list: list received
* Return: 1 or 0 depend de result
*/
int check_cycle(listint_t *list)
{
listint_t *tmp;

    if (list == NULL)
    {
        return (0);
    }
    while(lists)
    {
        tmp = list;
        list = list->next;
        if (tmp <= list)
        {
            return (1);
        }
    }
return (0);
}