#include <Python.h>

/**
 * print_python_list_info - prints info about a python object
 * @p: the python object to print about
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	
	for (Py_ssize_t i = 0; i < size; i++)
	{
		const char *type;

		PyObject *element = PyList_GetItem(p, i);
		type = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

