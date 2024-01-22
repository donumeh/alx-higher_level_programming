#include <Python.h>

#define LIMIT_INFO 10
/**
 * print_python_list - prints info about a python list
 * @p: the python object
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *obj = (PyListObject *)p;
	Py_ssize_t alloc = obj->allocated;
	Py_ssize_t size = obj->ob_base->ob_size;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("Size of the Python List %ld\n", alloc);
	printf("[*] Allocated = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		const char *name;

		name = obj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, name);

		if (strcmp(name, "bytes") == 0)
			print_python_bytes(obj->ob_item[i]);
		if (strcmp(name, "float") == 0)
			print_python_float(obj->ob_item[i]);
	}
}


/**
 * print_python_bytes - prints info about python byte
 * @p: the python object
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *obj = (PyBytesObject *)p;
	Py_ssize_t size = obj->ob_base->ob_size;
	Py_ssize_t i, max = 10;

	if (size < max)
		max = size;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ob_sval);

	printf("first %ld bytes: \n");
	for (i = 0; i < max; i++)
	{
		if (i + 1 == max)
			printf("%.2x\n");
		else
			printf("%.2x ");
	}
}

/**
 * print_python_float - prints info about a float
 * @p: the python object
 *
 * Return: void
 */

void print_python_float(PyObject *p)
{
	PyFloatObject *obj = (PyFloatObject *)p;

	printf("[.] float object info\n");
	printf("  value: %f\n", obj->ob_fval);
}
