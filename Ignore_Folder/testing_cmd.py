import cmd


class Hello(cmd.Cmd):
    """Command line for the class"""

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    def do_hi(self, person):
        """[Hi]: Greet the named person"""
        if person:
            print(f"Hi -{person}-")
        else:
            print("HI, Welcome stranger")

    def help_hi(self):
        print ('\n'.join(['greet [person]',
                         'Greet the named person',
                         ]))

    def do_exit(self, line):
        """[Exit]: Exit from current session"""
        print("Goodbye\n...\n..\n.")
        return True

    def complete_hi(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f
                           for f in self.FRIENDS
                           if f.startswith(text)
                           ]
        return completions
    

if __name__ == "__main__":
    Hello().cmdloop()