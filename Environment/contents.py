''' A simple file-reading util for the Environment. (Built-in) '''

class Environment:
    LibInfo = {
        "name": "Contents",
        "credits": [],
        "version": 1.0,
        "reqVersion": 1.3,
        "description": "A simple file-reading util for the Environment. (Built-in)",
        "helpinfo": "contents [PATH]\n[PATH] is the place to put your target file to read."
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):
        try:
            print(system.Output.Format.RESET + function[0] + system.Output.Format.LIB_RESET)
            print("-"*len(function[0])+"\n")
            try:
                with open(function[0]) as file:
                    length = file.readlines()
                    for i in range(len(length)):
                        print(system.Output.Format.RESET + str(i+1),system.Output.Format.LIB_RESET + str(length[i]),end="")
                print()
            except Exception as Error:
                system.Output.warn("Could Not Read File - "+str(Error))
        except IndexError:
            system.Output.warn("Could Not Read File (No Args)")