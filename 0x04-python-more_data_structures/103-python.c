#include <Python.h>

/**
 * print_python_list - print a python list info
 * @p: the python object
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t allocated = list->allocated;
	Py_ssize_t index;
	Py_ssize_t size = list->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (index = 0; index < size; index++)
	{
		printf("Element [%ld]: %s\n", index,
				list->ob_item[index]->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: the PyObject
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte = (PyBytesObject *)p;
	Py_ssize_t index;
	Py_ssize_t maxPrint = 10;
	Py_ssize_t size = byte->ob_base.ob_size;

	printf("[.] bytes object info\n");
	if (size == 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: ");
	for (index = 0; index < size; index++)
	{
		printf("%c", byte->ob_sval[index]);
	}

	if (size < maxPrint)
	{
		maxPrint = size + 1;
	}
	printf("\n  first %ld bytes: ", maxPrint);
	for (index = 0; index < maxPrint; index++)
	{
		char c = byte->ob_sval[index];

		if (c < 0)
			c = 256 + c;
		if (index + 1 == maxPrint)
			printf("%02x\n", c);
		else
			printf("%02x ", c);
	}

}
