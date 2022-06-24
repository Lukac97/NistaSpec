#include <Python.h>
typedef int bool;
#define TRUE 1
#define FALSE 0

static PyObject* hash_password(PyObject* self, PyObject* args)
{
	const char* password;
    if (!PyArg_ParseTuple(args, "s", &password)) {
      return NULL;
    }

	char* hash_password;
	hash_password = strdup(password);
	char key[] = "KEYFORPW";
	int i;

    hash_password[strlen(password)] = '\0';

    for (i = 0; i < strlen(password); i++) {
        hash_password[i] = 'A' + ( hash_password[i] - 'A' + key[i % strlen(key)] - 'A') % 26;
    }
   
	return Py_BuildValue("s", hash_password);
};

static PyObject* check_password(PyObject* self, PyObject* args)
{
    char* hash_password;
	char* real_password;
	int i;
	char key[] = "KEYFORPW";

	if (!PyArg_ParseTuple(args, "ss", &hash_password, &real_password)) {
      return NULL;
    }

    for(i = 0; i < strlen(hash_password); i++) {
        hash_password[i] = 'A' + ( hash_password[i] - key[i % strlen(key)] + 26) % 26;
    }

    if (strcmp(hash_password, real_password) == 0 )
    {
        return Py_BuildValue("i", TRUE);
    }
    else
    {
        return Py_BuildValue("i", FALSE);
    }


};

static PyMethodDef hash_functions[] = {
   {"hash_password", (PyCFunction)hash_password, METH_VARARGS, "hash"},
   {"check_password", (PyCFunction)check_password, METH_VARARGS, "check"},
   {NULL}
};

static PyModuleDef hash_module = {
    PyModuleDef_HEAD_INIT,
    "hash_module",
    "Hash password module",
    0,
    hash_functions
};

void PyInit_hash_module(void) {
   PyModule_Create(&hash_module);
}