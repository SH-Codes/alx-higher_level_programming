#include <stdio.h>
#include <Python.h>

/**
 * Print information about Python bytes object.
 *
 * @param p Python Object
 */
void print_python_bytes(PyObject *p) 
{
	printf("[.] bytes object info\n");
	
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	long int size = PyBytes_Size(p);
	char *string = PyBytes_AsString(p);
	
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	
	long int limit = (size >= 10) ? 10 : size + 1;
	printf("  first %ld bytes:", limit);
	
	for (long int i = 0; i < limit; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}

/**
 * Print information about Python list and its elements.
 *
 * @param p Python Object assumed to be a list
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	
	long int size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;
	
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	
	for (long int i = 0; i < size; i++)
	{
		PyObject *obj = PyList_GetItem(p, i);
		
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		
		if (PyBytes_Check(obj))
		{
			print_python_bytes(obj);
		}
	}
}
