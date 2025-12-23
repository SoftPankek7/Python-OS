global formatting
formatting = True

class Environment:
    LibInfo = {
        "name": "SYSTEM",
        "credits": ["Charlie T"],
        "version": 1.7,
        "reqVersion": None,
        "description": "The full insides - Formatting, Commands, and Runtime.",
        "helpinfo": "<< THIS IS NOT A LIB. >>"
    }
    def RunAsEnv(func):
        print("<< THIS IS NOT A LIB. >>\n<< THIS IS A SYSTEM FILE >>")

class Output:
    class Format:
        if formatting:
            RESET = "\033[0m"
            BOLD = "\033[1m"
            DIM = "\033[2m"
            ITALIC = "\033[3m"
            UNDERLINE = "\033[4m"
            BLINK = "\033[5m"
            REVERSE = "\033[7m"
            HIDDEN = "\033[8m"
            STRIKETHROUGH = "\033[9m"
            BLACK = "\033[30m"
            RED = "\033[31m"
            GREEN = "\033[32m"
            YELLOW = "\033[33m"
            BLUE = "\033[34m"
            MAGENTA = "\033[35m"
            CYAN = "\033[36m"
            WHITE = "\033[37m"
            BRIGHT_BLACK = "\033[90m"
            BRIGHT_RED = "\033[91m"
            BRIGHT_GREEN = "\033[92m"
            BRIGHT_YELLOW = "\033[93m"
            BRIGHT_BLUE = "\033[94m"
            BRIGHT_MAGENTA = "\033[95m"
            BRIGHT_CYAN = "\033[96m"
            BRIGHT_WHITE = "\033[97m"
            BG_BLACK = "\033[40m"
            BG_RED = "\033[41m"
            BG_GREEN = "\033[42m"
            BG_YELLOW = "\033[43m"
            BG_BLUE = "\033[44m"
            BG_MAGENTA = "\033[45m"
            BG_CYAN = "\033[46m"
            BG_WHITE = "\033[47m"
            BG_BRIGHT_BLACK = "\033[100m"
            BG_BRIGHT_RED = "\033[101m"
            BG_BRIGHT_GREEN = "\033[102m"
            BG_BRIGHT_YELLOW = "\033[103m"
            BG_BRIGHT_BLUE = "\033[104m"
            BG_BRIGHT_MAGENTA = "\033[105m"
            BG_BRIGHT_CYAN = "\033[106m"
            BG_BRIGHT_WHITE = "\033[107m"

            LIB_RESET = "\033[0m\033[2m"
        else:
            RESET = ""
            BOLD = ""
            DIM = ""
            ITALIC = ""
            UNDERLINE = ""
            BLINK = ""
            REVERSE = ""
            HIDDEN = ""
            STRIKETHROUGH = ""
            BLACK = ""
            RED = ""
            GREEN = ""
            YELLOW = ""
            BLUE = ""
            MAGENTA = ""
            CYAN = ""
            WHITE = ""
            BRIGHT_BLACK = ""
            BRIGHT_RED = ""
            BRIGHT_GREEN = ""
            BRIGHT_YELLOW = ""
            BRIGHT_BLUE = ""
            BRIGHT_MAGENTA = ""
            BRIGHT_CYAN = ""
            BRIGHT_WHITE = ""
            BG_BLACK = ""
            BG_RED = ""
            BG_GREEN = ""
            BG_YELLOW = ""
            BG_BLUE = ""
            BG_MAGENTA = ""
            BG_CYAN = ""
            BG_WHITE = ""
            BG_BRIGHT_BLACK = ""
            BG_BRIGHT_RED = ""
            BG_BRIGHT_GREEN = ""
            BG_BRIGHT_YELLOW = ""
            BG_BRIGHT_BLUE = ""
            BG_BRIGHT_MAGENTA = ""
            BG_BRIGHT_CYAN = ""
            BG_BRIGHT_WHITE = ""

            LIB_RESET = ""

    def halt(Content, Code, Format=True):
        if Format:
            print("[ "+ Output.Format.RED+Output.Format.BOLD+Output.Format.BLINK+"HALT"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ HALT ] :  "+Content)
        exit(Code)

    def error(Content, Format=True):
        if Format:
            print("[ "+ Output.Format.RED+Output.Format.BOLD+Output.Format.DIM+"ERROR"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ ERROR ] :  "+Content)
    
    def info(Content, Format=True):
        if Format:
            print("[ "+ Output.Format.BLUE+Output.Format.BOLD+Output.Format.DIM+"INFO"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ INFO ] :  "+Content)
    
    def warn(Content, Format=True):
        if Format:
            print("[ "+ Output.Format.YELLOW+Output.Format.BOLD+Output.Format.DIM+"WARN"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ WARN ] :  "+Content)

    def debug(Content, Format=True):
        if Format:
            print("[ "+ Output.Format.GREEN+Output.Format.BOLD+Output.Format.DIM+"DEBUG"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ DEBUG ] :  "+Content)
    
    def temp(Content, Format=True):
        if Format:
            print("[ "+ Output.Format.BLINK+Output.Format.BOLD+"TEMP"+Output.Format.RESET+" ] :  "+Content)
        else:
            print("[ TEMP ] :  "+Content)
    
    def ShellOutput(Content, Format=True):
        if Format:
            print(Output.Format.DIM+"  "+str(Content)+Output.Format.RESET)
        else:
            print("  "+str(Content))

class ShellRuntime:
    class LibRunner:
        def __init__(self, library):
            self.library = library
        def LoadLib(name,func):
            try:
                import libload as lib
                libs = lib.load_libs()
                if name in libs:
                    print(Output.Format.DIM, end="")
                    reqv = libs[name].Environment.LibInfo
                    try:
                        if reqv["reqVersion"] > Environment.LibInfo["version"]:
                            Output.warn(f"Version incompatible. Sys v{str(Environment.LibInfo["version"])} < Lib v{str(reqv["reqVersion"])}")
                            return True
                        else:
                            libs[name].Environment.RunFromEnv(func)
                    except NameError:
                        Output.warn("Add a reqVersion tag to your LibInfo")
                        libs[name].Environment.RunFromEnv(func)
                        
                    print(Output.Format.RESET, end="")
                    return True
                else:
                    return False
            except Exception as Error:
                Output.error("LoadLib has failed. Error:\n"+str(Error))
    class CommandRunner:
        def Exec(command, arguments=[]):
            if command == "" or command[0] == "`":
                pass
            elif command[0:4] == "exit":
                if not len(command) == 4:
                    exit(command[5:])
                else:
                    exit(0)
            elif command[0:4] == "echo":
                Output.ShellOutput(command[5:])
            elif command[0:5] == "panic":
                if not len(command) == 5:
                    Output.halt(command[6:], 3)
                else:
                    Output.halt("User Created a Panic Signal.", 3)
            else:
                if not "no_error" in arguments:
                    try:
                        if not ShellRuntime.LibRunner.LoadLib(command.split(" ")[0].lower(),command.split(" ")[1:]):
                            Output.ShellOutput(f"'{command}' is not a known command or Library.")
                    except IndexError:
                        if not ShellRuntime.LibRunner.LoadLib(command.lower(),True):
                            Output.ShellOutput(f"'{command}' is not a known command or Library.")
        def ExecFromFile(file, arguments=[]):
            try:
                with open(file, "rt") as file:
                    list = file.readlines()
                runlist = []
                for i in range(len(list)):
                    if not list[i] == "\n" or list[i] == "":
                        runlist.append(list[i].strip())
                for i in range(len(runlist)):
                    ShellRuntime.CommandRunner.Exec(runlist[i])
            except FileNotFoundError:
                if not "no_error" in arguments:
                    Output.error("File does not exist.")
                    return False

        def TestRun():
            Output.debug("TEST RUN FLAG")
            input()

def lprint(string):
    print(string + Output.Format.LIB_RESET)

if __name__ == "__main__":
    Output.halt("Cannot run as file.",1)
else:
    Output.info("Loaded System")