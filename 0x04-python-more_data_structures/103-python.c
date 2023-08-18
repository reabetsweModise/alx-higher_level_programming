#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes -this fuction  Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject* p)
{
	char *mystring;
	long int Size, j, Limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Size = ((PyVarObject*)(p))->ob_size;
	mystring = ((PyBytesObject*)p)->ob_sval;

	printf("  size: %ld\n", Size);
	printf("  trying string: %s\n", mystring);

	if (Size >= 10)
		Limit = 10;
	else
		Limit = Size + 1;

	printf("  first %ld bytes:", Limit);

	for (j = 0; j < Limit; j++)
		if (mystring[j] >= 0)
			printf(" %02x", string[j]);
		else
			printf(" %02x", 256 + string[j]);

	printf("\n");
}

/**
 * print_python_list -this Fucntion Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject* p)
{
	long int size, i;
	PyListObject* list;
	PyObject* obj;

	size = ((PyVarObject*)(p))->ob_size;
	list = (PyListObject*)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject*)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}

