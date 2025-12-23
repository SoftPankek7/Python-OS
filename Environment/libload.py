try:
    import importlib
except ModuleNotFoundError:
    print("[ CRITICAL ] :  importlib NEEDS TO BE INSTALLED.")
    exit(2)

def load_libs():
    imported_modules = {}
    try:
        with open("libs.el", 'rt') as f:
            module_names = f.readlines()
        for module_name in module_names:
            module_name = module_name.strip()
            if not module_name:
                continue
            try:
                if module_name[0][0] == ";" or module_name[0][0] == "-" or module_name[0][0] == "":
                    pass
                else:
                    module = importlib.import_module(module_name)
                    imported_modules[module_name] = module
            except ImportError as e:
                print(f"[ ERROR ] : Failed to import {str(module_name)} - {str(e)}")
    except FileNotFoundError:
        print("LIBLOAD PANIC!!! LIBS.EL NOT FOUND!")
        exit(1)
    except Exception as Error:
        print(f"Internal Critical Error! ({str(Error)})")
        exit(1)
    return imported_modules

def get_libs():
    imported_modules = {}
    try:
        with open("libs.el", 'rt') as f:
            module_names = f.readlines()
        for module_name in module_names:
            module_name = module_name.strip()
            if module_name[0][0] == ";" or module_name[0][0] == "-" or module_name[0][0] == "":
                pass
            else:
                if not module_name:
                    continue
                imported_modules[module_name] = True
    except FileNotFoundError:
        print("LIBLOAD PANIC!!! LIBS.EL NOT FOUND!")
        exit(1)
    except Exception as Error:
        print(f"Libload GET Error! ({str(Error)})")
    return imported_modules

def add_lib(name):
    try:
        with open("libs.el", 'at') as f:
            f.write(name)
        return True
    except FileNotFoundError:
        print("LIBLOAD PANIC!!! LIBS.EL NOT FOUND!")
        exit(1)
        return False
    except Exception as Error:
        print(f"Internal Critical Error! ({str(Error)})")
        exit(1)
        return False

def get_info(name):
    libs = load_libs()
    return libs[name].Environment.LibInfo