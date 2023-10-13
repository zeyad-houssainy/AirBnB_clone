import cmd


class Hello(cmd.Cmd):
    """Command line for the class"""

    def do_hi(self, person):
        """[Hi]: Greet the named person"""
        if person:
            print(f"Hi -{person}-")
        else:
            print("HI, Welcome stranger")

    
    def do_exit(self, line):
        """[Exit]: Exit the current program"""
        return True
    

if __name__ == "__main__":
    Hello().cmdloop()