import libload as lib
libs = lib.load_libs()
print()

import os
os.system("")

real_errors = True

class Environment:
    LibInfo = {
        "name": "MAIN",
        "credits": ["Charlie T"],
        "version": libs["system"].Environment.LibInfo["version"],
        "description": "The full insides - Formatting, Commands, and Runtime.",
        "helpinfo": "<< THIS IS NOT A LIB. >>"
    }
    def RunAsEnv(func):
        print("<< THIS IS NOT A LIB. >>\n<< THIS IS A SYSTEM FILE >>")

try:
    shell = libs["system"].ShellRuntime
    system = libs["system"]
    if shell.CommandRunner.ExecFromFile("exec.ep"):
        system.Output.halt("ExecFromFile Proccess Failed. Please re-install.",15)
    while True:
        try:
            command = input(system.Output.Format.BLUE+"$"+system.Output.Format.RESET+" ")
            shell.CommandRunner.Exec(command)
        except KeyboardInterrupt:
            print()
        except EOFError:
            pass
        except Exception as Error:
            system.Output.halt(f"Internal Error - {str(Error)}",2)
except Exception as Error:
    try:
        libs["system"].Output.halt("Critical Main Error! REINSTALL!!",1)
    except:
        print("[ CRITICAL ] :  Critical Main Error!")
        exit(1)