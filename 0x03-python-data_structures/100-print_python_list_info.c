#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about py lists
 * @p: pointer to an obj
 */

void print_python_list_info(PyObject *p)
{
	int i, sizeobj;
	PyObjject *p2;

	sizeobj = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", sizeobj);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sizeobj; i++)
	{
		p2 = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(p2)->tp_name);
	}
}
