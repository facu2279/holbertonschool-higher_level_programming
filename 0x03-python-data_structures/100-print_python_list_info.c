#include <Python.h>
/**
* print_python_list_info - print information about lists in python
 * @p: list
*/
void print_python_list_info(PyObject *p)
{
    int tope, i;
    PyObject *lista; 
    
    tope = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", tope);
	printf("[*] Allocated = %d\n", tope);

    for (i = 0; i <= tope - 1; i++)
    {
        lista = PyList_GetItem((p), (i));
        printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(lista)->tp_name);
    }
}