''' A simple file-reading util for the Environment. (Built-in) '''

class Environment:
    LibInfo = {
        "name": "Info",
        "credits": [],
        "version": 1.0,
        "description": "Get Information from libaries! (Built-in)",
        "helpinfo": "info [LIBARY]"
    }
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]
    def RunFromEnv(function):
        try:
            system.lprint(system.Output.Format.RED + "Raw:  " + str(libs[function[0]].Environment.LibInfo))
            info = libs[function[0]].Environment.LibInfo
            print("Name:     "+str(info["name"]))
            system.lprint(system.Output.Format.RESET + "Devs:     "+str(info["credits"]))
            print("Version:  "+str(info["version"]))
            system.lprint(system.Output.Format.RESET + "Desc:     "+str(info["description"]))
            print("Help:     "+str(info["helpinfo"]))
        except Exception as Error:
            system.Output.warn("Could not generate info - "+str(Error))
            pass
        except IndexError:
            system.Output.warn("Could Not Read File (No Args)")