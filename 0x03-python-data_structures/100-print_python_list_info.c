#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function to print basic info about python list
 * @p: Python object
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;

	/**
	 * Py_SIZE: a function used to access the size of an object
	 * PyList_Check: funtion return true if the PyObject is a list Object.
	 * PyListObject: a subtype of PyObject represent a Python list object.
	 * Py_TYPE: a function that return ->ob_type of an Object
	 * PyList_GetItem(PyObject *list, Py_ssize_t index):
	 * *****function to return the object in the postion index
	 * *****@list: Python list Object
	 * *****@index: index (postion) on an item in the list Object.
	 */

	size = Py_SIZE(p);
	if (PyList_Check(p))
	{
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", alloc);

		for (i = 0; i < size; i++)
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
