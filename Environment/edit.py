class Environment:
    LibInfo = {
        "name": "edit",
        "credits": [],
        "version": 1.0,
        "description": "A VERY simple text editor (Built-in)",
        "helpinfo": "Append to files!"
    }
    
    import libload as lib
    global libs, system
    libs = lib.load_libs()
    system = libs["system"]

    def RunFromEnv(func):
        if len(func) == 1:
            with open(func[0], "at") as file:
                try:
                    print(system.Output.Format.RESET + str(func[0]) + system.Output.Format.LIB_RESET)
                    print("-"*len(str(func[0]))+"\n")
                    try:
                        with open(func[0]) as file:
                            length = file.readlines()
                            for i in range(len(length)):
                                print(system.Output.Format.RESET + str(i+1),system.Output.Format.LIB_RESET + str(length[i]),end="")
                        print()
                    except Exception as Error:
                        system.Output.warn("Could Not Read File - "+str(Error))
                except IndexError:
                    system.Output.warn("Could Not Read File (No Args)")

                while True:
                    insert = input(">")
                    if str(insert.lower()) == ":quit":
                        break
                    else:
                        file.write(str(insert))
        else:
            system.Output.error("Please specify a file.")