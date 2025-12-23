'''

An Example Lib to aid begginers to know how to create their own libaries.
Basically adds two numbers together from the Command Line Arguments.

Also yes, there is WAAAY too many comments. If you dont like it, REMOVE IT.
Dont be lazy. Sometimes you can learn from example, and not just lecturing

(the commenting itself last an hour at ~3 AM 😭)

'''

class Environment:

    LibInfo = {
        "name": "ExampleLib",                # The name of the library. Doesnt have to be filename.
                                             # I don't really know how this could apply to an absolute
                                             # nesscisary feature, because you dont really see it 
                                             # unless you do something with info. Which, is a small
                                             # chance. I guess it can enable you to have a really long
                                             # and random filename that could be looked up through info,
                                             # but.. dont. Please. Just don't.
        "credits": ["PersonA", "PersonB"],   # The people who helped make this. Interpreted as
                                             # a list object because there may be more than one
                                             # person. If there is only one, just go with a list
                                             # with only one index; e.g: "credits": ["PersonA"],
        "version": 10.1,                     # The version of this library file. 
        "reqVersion": 1.3,                   # The version that the system needs to be. Note: 
                                             # this was implimented in ~v1.4 so, v1.3 will not
                                             # check for this variable. However, post 1.3, it
                                             # will return an warning if it doesnt exist - to
                                             # introduce a "safety" feature for old versions
                                             # of system without that many features.
        "description": "An Example Lib to aid begginers to know how to create their own libaries.\nBasically adds two numbers together from the Command Line Arguments.",
        "helpinfo": "examplelib [A] [B]\nReturns [A] + [B] in text\n[A] and [B] have to be integer friendly to work."
    }

    # Include the system - so we can do text formatting, output, etc.
    # We import libload (the custom library importing tool)
    # so we can dynamically import the system
    import libload as lib
    # Then we make 2 variables global - so they can be used anywhere
    global libs, system
    # Now, we initialize the libraries, allowing every lib to be
    # accessed from here.
    libs = lib.load_libs()
    # Pick the system library - so we can use it later in the script
    # for some stuff - such as easy coloured text, custom messages,
    # and more
    system = libs["system"]


    # This is the entrypoint of the library. Sort of like how C-based
    # languages have the main() function. This will have the CLI
    # arguments passed through func, the variable in there.
    # func is a list of all arguments - for example:
    # $ library arg1 arg2  
    # would become RunFromEnv(["arg1", "arg2"])
    def RunFromEnv(func):
        # SYSTEM.LPRINT :  Prints text (for libs) - and then automatically resets the text at the end.
        #      ||||||      It makes it easier & smaller to print out text :) However, it sacrifices
        #      VVVVVV      some stuff - such as arguments e.g: print("Hello!", end="!!!")
        system.lprint(system.Output.Format.BLUE + "Examplelib Arguments: "+str(func))

        # Because it is a list of command line arguments, we can check
        # how many arguments there are with a simple len().
        if len(func) != 2: # Check if running without 2 Command Line Args
            # Keep output DIM always, for clarity.
            # For example, avoid using Output.Format.RESET
            # Instead use, Output.Format.LIB_RESET
            print("This is an example library that adds two numbers.")
            print("How about try running this via")

            # A simple function in the system that is meant to reduce the size of formatted print().
            # It works by adding Output.Format.LIB_RESET at the end to make sure it resets to normal
            # formatting - and also keeping the script smaller.
            system.lprint(system.Output.Format.ITALIC + system.Output.Format.RED + "examplelib 1 1")
            # This shows as red italic text saying: "examplelib 1 1"
        else: # This means it has exactly 2 CLI arguments, e.g: examplelib 1 1
            # Capture the addition of 2 variables into a variable.
            # This is to make it quicker & easier to use later.
            # (as seen soon)
            output = Environment.add(func[0], func[1])
            # Add the 2 Command Line Args together through a simple function we made.
            # You don't need it in the Environment class. 

            # In the adding function, it returns false
            #  if the code fails with an error. This is 
            # because of a try/except block. The code shows:
            #
            # def add(a,b):
            #   try: ...
            #   except:
            #       return False

            if output != False:
                # Nothing hasn't gone wrong, because the try/except hasn't
                system.lprint(system.Output.Format.ITALIC + str(func[0]) +" + "+str(func[0])+" = "+str(output))
                # Italic text that shows:
                # a + b = answer
                # where a,b,answer are variables. For example,
                # if ran via examplelib 1 2, you would of 
                # gotten the output of:
                # 1 + 2 = 3
            else:
                # There was an error, probally because the
                # arguments where not numbers. This is because
                # to avoid concatination, I used int(), which
                # also has a bonus of allowing to catch strings.
                # this is because you cant convert a string to
                # an int, and it returns a TypeError or something,
                # and that will be caught onto the except block.
                # Resulting in False - and then ultimately this
                # code block
                print("Hey, those aren't numbers!")

        # This is a demo showing that you do not need to have the functions
        # in the Environment class, like Environment.add(), and you can just
        # use a global-scope function. This should print "Functions don't need 
        # to be in the Environment Class!" because it returns that, and then
        # it will be printed by the print block below.
        print(Fact())

    # Defining the function that adds up 2 numbers and
    # returns them to show how you could use the functions.
    def add(a, b):
        # try/except block to detect if A or B is a 
        # string, because an int() of a string will
        # release a TypeError - triggering the 
        # return False code block.
        try:
            # int() to avoid concatenation & also 
            # detect if it is a string.
            return int(a)+int(b)
        except:
            # Uh-oh! Not an integer, because this 
            # caught the int() TypeError from a 
            # different data-set, e.g: string or
            # list and went to this code block.
            return False


def Fact():
    return "Functions don't need to be in the Environment Class!"