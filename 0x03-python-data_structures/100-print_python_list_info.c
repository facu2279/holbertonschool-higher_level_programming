#include <Python.h>
/**
* print_python_list_info - print information about lists in python
 * @p: list
*/
void print_python_list_info(PyObject *p)
{
    int tope, i = 0, cant = 0;
    /*
    *char *tipo;
    */
    PyObject *lista; 
    
    tope = Py_SIZE(p);
    cant = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", tope, cant);
    for (; i <= tope - 1; i++)
    {
        lista = PyList_GetItem((p), (i));
        printf("Element %d: %s\n", i, Py_TYPE(lista)->tp_name);
        /**
        * tipo = (Py_TYPE(lista)->tp_name);
		*
        *printf("llego");
        */    
    }
}