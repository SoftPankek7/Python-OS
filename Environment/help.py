''' A simple file-reading util for the Environment. (Built-in) '''

class Environment:
    LibInfo = {
        "name": "Help",
        "credits": [],
        "version": 1.0,
        "description": "Gets Help Information from libaries! (Built-in)",
        "helpinfo": "help [LIBARY]"
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):
        try:
            system.lprint(system.Output.Format.RED+"Help for "+system.Output.Format.YELLOW+str(function[0])+"\n")
            print(str(libs[function[0]].Environment.LibInfo["helpinfo"]))
        except Exception as Error:
            system.Output.warn("Could not generate help - "+str(Error))
            pass
        except IndexError:
            system.Output.warn("Could Not Read File (No Args)")