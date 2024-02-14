#include "Python.h"

void print_python_list_info(PyObject *p)
{
	int check_list;
	Py_ssize_t len_p, i;
	PyObject *item;
	const char *item_type;

	check_list = PyList_Check(p);
	if (!check_list)
		return;
	len_p = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len_p);
	printf("[*] Allocated = %ld\n", len_p);

	for (i = 0; i < len_p; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, item_type);
	}
}
