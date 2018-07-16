import Command

class SimpleCLI():
    functions = None

    def show_help(self):
        "Prints all help for all defined functions"
        known_commands = set(Command.known_commands.values())
        known_commands.remove('invalid_command')
        for command in known_commands:
            print command,": ",
            getattr(self.functions,command).__help__()


    def parse(self):
        """accept an incoming string, get the first term as a command, terms starting with - as flags, and the remaining is the arg"""
        input_string = raw_input(">").split(" ")
        com = input_string[0]
        options = []
        arg = []
        for term in input_string[1:]:
            if term.startswith('-'):
                options += list(term[1:].strip())
                continue
            arg.append(term)
        return com,options," ".join(arg)
  
    def program_loop(self):
        """infinite loop to run the program"""
        while True:
            com, options, arg = self.parse()
            if com =="":
                continue
            elif com == "help":
                self.show_help()
                continue
            elif com == "exit":
                exit()
            try:
                com = Command.known_commands[com]
                if "h" in options:
                    getattr(self.functions,com).__help__()
                    continue
                getattr(self.functions,com)(options,arg)
            except:
                Command.invalid_command(options,arg)

    def __init__(self, functions):
        self.functions = functions
        self.program_loop()


  

