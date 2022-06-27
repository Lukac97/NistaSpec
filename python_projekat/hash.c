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
	char key[] = "this is the key";

    for (int i = 0; i < strlen(password); i++) {
        if(password[i] == '\0')
            hash_password[i] = password[i];
        else
            hash_password[i] = password[i] ^ (key[i] % (strlen(key) - 1));
    }

	return Py_BuildValue("s#", hash_password, strlen(password));
};

static PyObject* check_password(PyObject* self, PyObject* args)
{
    char* hash_password;
	char* real_password;
	char* new_hash_password;
	new_hash_password = strdup(real_password);
	char key[] = "this is the key";

	if (!PyArg_ParseTuple(args, "ss", &hash_password, &real_password)) {
      return NULL;
    }

    for (int i = 0; i < strlen(real_password); i++) {
        if(real_password[i] == '\0')
            new_hash_password[i] = real_password[i];
        else
            new_hash_password[i] = real_password[i] ^ (key[i] % (strlen(key) - 1));
    }

    if (strncmp(hash_password, new_hash_password, strlen(real_password)) == 0 )
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