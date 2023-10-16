# AirBnB_clone
AirBnB clone Projects

In this project We are supposed to create out own Airbnb clone especially console.

We are supposed to create the command intepreter using cmd module which will help us manage
our instances and objects.

The tasks that we have to complete are:

1. Write a class BaseModel that defines all common attributes/methods for other classes
	Public instance attributes:
	id: string - assign with an uuid when an instance is created

	Public instance methods:
	save(self): updates the public instance attribute updated_at with the current datetime
	to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance

2. you will use *args, **kwargs arguments for the constructor of a BaseModel

3. Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)
It’s not human readable
Using this file with another program in Python or other language will be hard.
So, you will convert the dictionary representation to a JSON string.
	We have to Write a class FileStorage that serializes instances to
	a JSON file and deserializes JSON file to instances

4. Write a program called console.py that contains the entry point of the command interpreter:

You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF and help to exit the program

a custom prompt: (hbnb)

5. In our command interpreter we have to update it by :
	create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
	show: Prints the string representation of an instance based on the class name and id
	destroy: Deletes an instance based on the class name and id (save the change into the JSON file).
	all: Prints all string representation of all instances based or not on the class name.
	update: Updates an instance based on the class name and id by adding or updating attribute

6. We have to Write a class User that inherits from BaseModel:

	Public class attributes:
	email: string - empty string
	password: string - empty string
	first_name: string - empty string
	last_name: string - empty string
	Update FileStorage to manage correctly serialization and deserialization of User.

	class State:
	
	Public class attributes:
	name: string - empty string

	class City:

	Public class attributes:
	state_id: string - empty string: it will be the State.id
	name: string - empty string

	class Amenity:

	Public class attributes:
	name: string - empty string

	class Place:

	Public class attributes:
	city_id: string - empty string: it will be the City.id
	user_id: string - empty string: it will be the User.id
	name: string - empty string
	description: string - empty string
	number_rooms: integer - 0
	number_bathrooms: integer - 0
	max_guest: integer - 0
	price_by_night: integer - 0
	latitude: float - 0.0
	longitude: float - 0.0
	amenity_ids: list of string - empty list: it will be the list of Amenity.id later

	class Review:

	Public class attributes:
	place_id: string - empty string: it will be the Place.id
	user_id: string - empty string: it will be the User.id
	text: string - empty string


7. Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

8. Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.
