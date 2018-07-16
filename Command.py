known_commands = {}

def default_run(options, arg):
    "Command was not defined"
    print "Undefined command"
    pass

class Command():
    def verify_options(self,options):
        for option in options:
            if option not in self.options:
                print option, "is not a valid option"
                return False
        return True

    def __call__(self,options,args):
        if self.verify_options(options):
            try:
                self.run(options,args)
            except:
                self.__help__()

    def __help__(self):
        print self.description, self.usage

    def __init__(self, name="",aliases="",options="", usage="", run=None):
        known_commands[name] = name
        if aliases != "":
            for alias in aliases.split(","):
                known_commands[alias] = name 
        self.options = options
        self.usage = usage
        if run == None:
            self.description=default_run.__doc__
            self.run = default_run
            self.usage = "[OPTION] -h"
        else:
            self.description = run.__doc__
            if self.description == None:
                self.description = "No description found for this command"
            self.run = run


invalid_command = Command(name="invalid_command",aliases="",options="")

