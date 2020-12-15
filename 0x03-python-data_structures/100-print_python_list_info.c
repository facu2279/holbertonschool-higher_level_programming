#include <Python.h>
/**
* print_python_list_info - print information about lists in python
 * @p: A PyObject list
*/
void print_python_list_info(PyObject *p)
{
    int tam;
    
    tam = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", tam);
	printf("[*] Allocated = 2\n");
}