Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 16 2013, 23:39:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 

>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__loader__', '__name__', '__package__', '__plen', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
>>> sys.platform
'darwin'
>>> from os import chdir
>>> chdir
<built-in function chdir>
>>> import imp
>>> help(imp)
Help on module imp:

NAME
    imp

MODULE REFERENCE
    http://docs.python.org/3.3/library/imp
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides the components needed to build your own __import__
    function.  Undocumented functions are obsolete.
    
    In most cases it is preferred you consider using the importlib module's
    functionality over this module.

CLASSES
    builtins.object
        NullImporter
    
    class NullImporter(builtins.object)
     |  Null import object.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, path)
     |  
     |  find_module(self, fullname)
     |      Always returns None.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    acquire_lock(...)
        acquire_lock() -> None
        Acquires the interpreter's import lock for the current thread.
        This lock should be used by import hooks to ensure thread-safety
        when importing modules.
        On platforms without threads, this function does nothing.
    
    find_module(name, path=None)
        **DEPRECATED**
        
        Search for a module.
        
        If path is omitted or None, search for a built-in, frozen or special
        module and continue search in sys.path. The module name cannot
        contain '.'; to search for a submodule of a package, pass the
        submodule name and the package's __path__.
    
    get_frozen_object(...)
    
    get_magic()
        Return the magic number for .pyc or .pyo files.
    
    get_suffixes()
    
    get_tag()
        Return the magic tag for .pyc or .pyo files.
    
    init_builtin(...)
    
    init_frozen(...)
    
    is_builtin(...)
    
    is_frozen(...)
    
    is_frozen_package(...)
    
    load_compiled(name, pathname, file=None)
    
    load_dynamic(...)
    
    load_module(name, file, filename, details)
        **DEPRECATED**
        
        Load a module, given information returned by find_module().
        
        The module name must include the full package name, if any.
    
    load_package(name, path)
    
    load_source(name, pathname, file=None)
    
    lock_held(...)
        lock_held() -> boolean
        Return True if the import lock is currently held, else False.
        On platforms without threads, return False.
    
    release_lock(...)
        release_lock() -> None
        Release the interpreter's import lock.
        On platforms without threads, this function does nothing.
    
    reload(module)
        Reload the module and return it.
        
        The module must have been successfully imported before.

DATA
    C_BUILTIN = 6
    C_EXTENSION = 3
    IMP_HOOK = 9
    PKG_DIRECTORY = 5
    PY_CODERESOURCE = 8
    PY_COMPILED = 2
    PY_FROZEN = 7
    PY_RESOURCE = 4
    PY_SOURCE = 1
    SEARCH_ERROR = 0

FILE
    /Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/imp.py


>>> imp.reload(os)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    imp.reload(os)
NameError: name 'os' is not defined
>>> imp.reload(sys)
<module 'sys' (built-in)>
>>> import modtest2
 I am being imported from another module
>>> imp.reload(modtest2)
 I am being imported from another module
<module 'modtest2' from './modtest2.py'>
>>> import modtest
>>> help(modtest)
Help on module modtest:

NAME
    modtest

FUNCTIONS
    square(x)

AUTHOR
    jason

FILE
    /Users/jason/notebook/python/cbtnuggets/modtest.py


>>> modtest.square(10)
100
>>> sys.path
['', '/Users/jason/notebook/python/cbtnuggets', '/Library/Frameworks/Python.framework/Versions/3.3/bin', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages/distribute-0.6.49-py3.3.egg', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python33.zip', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages', '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages/setuptools-0.6c11-py3.3.egg-info']
>>> ================================ RESTART ================================
>>> 
