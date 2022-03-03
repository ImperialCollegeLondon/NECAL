# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_interface2050')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_interface2050')
    _interface2050 = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_interface2050', [dirname(__file__)])
        except ImportError:
            import _interface2050
            return _interface2050
        try:
            _mod = imp.load_module('_interface2050', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _interface2050 = swig_import_helper()
    del swig_import_helper
else:
    import _interface2050
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def create_range(range, size):
    return _interface2050.create_range(range, size)
create_range = _interface2050.create_range

def destroy_range(range):
    return _interface2050.destroy_range(range)
destroy_range = _interface2050.destroy_range

def get_cell(range, index):
    return _interface2050.get_cell(range, index)
get_cell = _interface2050.get_cell

def set_cell(range, index, number):
    return _interface2050.set_cell(range, index, number)
set_cell = _interface2050.set_cell

def output_a():
    return _interface2050.output_a()
output_a = _interface2050.output_a

def output_b():
    return _interface2050.output_b()
output_b = _interface2050.output_b

def output_lever_names():
    return _interface2050.output_lever_names()
output_lever_names = _interface2050.output_lever_names

def input_lever_ambition():
    return _interface2050.input_lever_ambition()
input_lever_ambition = _interface2050.input_lever_ambition

def set_input_lever_ambition(newValue):
    return _interface2050.set_input_lever_ambition(newValue)
set_input_lever_ambition = _interface2050.set_input_lever_ambition

def input_lever_start():
    return _interface2050.input_lever_start()
input_lever_start = _interface2050.input_lever_start

def set_input_lever_start(newValue):
    return _interface2050.set_input_lever_start(newValue)
set_input_lever_start = _interface2050.set_input_lever_start

def input_lever_end():
    return _interface2050.input_lever_end()
input_lever_end = _interface2050.input_lever_end

def set_input_lever_end(newValue):
    return _interface2050.set_input_lever_end(newValue)
set_input_lever_end = _interface2050.set_input_lever_end

def reset():
    return _interface2050.reset()
reset = _interface2050.reset
ExcelEmpty = _interface2050.ExcelEmpty
ExcelNumber = _interface2050.ExcelNumber
ExcelString = _interface2050.ExcelString
ExcelBoolean = _interface2050.ExcelBoolean
ExcelError = _interface2050.ExcelError
ExcelRange = _interface2050.ExcelRange
class excel_value(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, excel_value, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, excel_value, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _interface2050.excel_value_type_set
    __swig_getmethods__["type"] = _interface2050.excel_value_type_get
    if _newclass:
        type = _swig_property(_interface2050.excel_value_type_get, _interface2050.excel_value_type_set)
    __swig_setmethods__["number"] = _interface2050.excel_value_number_set
    __swig_getmethods__["number"] = _interface2050.excel_value_number_get
    if _newclass:
        number = _swig_property(_interface2050.excel_value_number_get, _interface2050.excel_value_number_set)
    __swig_setmethods__["string"] = _interface2050.excel_value_string_set
    __swig_getmethods__["string"] = _interface2050.excel_value_string_get
    if _newclass:
        string = _swig_property(_interface2050.excel_value_string_get, _interface2050.excel_value_string_set)
    __swig_setmethods__["array"] = _interface2050.excel_value_array_set
    __swig_getmethods__["array"] = _interface2050.excel_value_array_get
    if _newclass:
        array = _swig_property(_interface2050.excel_value_array_get, _interface2050.excel_value_array_set)
    __swig_setmethods__["rows"] = _interface2050.excel_value_rows_set
    __swig_getmethods__["rows"] = _interface2050.excel_value_rows_get
    if _newclass:
        rows = _swig_property(_interface2050.excel_value_rows_get, _interface2050.excel_value_rows_set)
    __swig_setmethods__["columns"] = _interface2050.excel_value_columns_set
    __swig_getmethods__["columns"] = _interface2050.excel_value_columns_get
    if _newclass:
        columns = _swig_property(_interface2050.excel_value_columns_get, _interface2050.excel_value_columns_set)

    def __init__(self):
        this = _interface2050.new_excel_value()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _interface2050.delete_excel_value
    __del__ = lambda self: None
excel_value_swigregister = _interface2050.excel_value_swigregister
excel_value_swigregister(excel_value)

# This file is compatible with both classic and new-style classes.


