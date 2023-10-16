#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Represents the class command interpreter"""

    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Signals the End of File"""
        print("")
        return True

    def emptyline(self):
        """ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file and prints id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                new_instance = HBNBCommand.__classes[class_name]()
                print(new_instance.id)
                storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in instances:
                print("** no instance found **")
            else:
                print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in instances:
                print("** no instance found **")
            else:
                del instances[key]
                storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of a given class
            If no class is specified, displays all instantiated objects
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instances = []
            for instance in storage.all().values():
                if len(args) > 0 and args[0] == instance.__class__.__name__:
                    instances.append(instance.__str__())
                elif len(args) == 0:
                    instances.append(instance.__str__())
            print(instances)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if len(args) < 5:
            obj = instances[key]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = instances[key]
            for key_s, value in eval(args[2]).items():
                if (key_s in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key_s])
                        in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key_s])
                    obj.__dict__[key_s] = valtype(value)
                else:
                    obj.__dict__[key_s] = value
        storage.save()

        def do_count(self, arg):
            """Retrieve the number of instances of a given class."""
            args = arg.split()
            count = 0
            instances = storage.all()
            for obj in instances.values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
