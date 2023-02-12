# 0x00. AirBnB clone - The console
## Project Description
This is a clone of the AirBnB project. This project handles the backend of the project interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python (serialization/deserialization)

## Command interpreter
This is just like the Bash shell to manage the AirBnB objects (`User`, `State`, `City`, `Place`, `Review` etc.) It is used to: 
 - Create new objects
 - Save object to file in json format
 - Retrieve an object form a json file
 - Do operations on objects (count, compute stats etc.)
 - Update attributes of an object
 - Destroy an object
Some of the commands available are: `show`, `create`, `update`, `destroy`, `count` etc.

## Usage of interpreter
1. First clone this repository
2. Locate the `console.py` file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
3. When this command is run the following prompt should appear:
```
(hbnb)
```
4.  This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

### Commands
```
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
```

###  Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:
```
Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
```
Advanced syntax is implemented for the following commands:
```
* all - Shows all objects the program has access to, or all objects of a given class

* count - Return number of object instances by class

* show - Shows an object based on class and UUID

* destroy - Destroys an object based on class and UUID

* update - Updates existing attributes an object based on class name and UUID
```

## Available commands and what they do
The recognizable commands by the interpreter are the following:
| Command | Description | Usage |
| ------- | ----------- | ----- |
| **quit or EOF** | Exits the program | By itself |
| **help** | Provides a text describing how to use a command. | By itself --or-- `help <command\>` |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. | `create <class name\>`|
| **show** | Prints the string representation of an instance based on the class name and `id`  | `show <class name\> <id\>` --or-- `<class name\>.show(<id\>)` |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file). | `destroy <class name\> <id\>` --or-- `<class name>.destroy(<id>)` |
| **all** | Prints all string representation of all instances based or not on the class name.  | By itself or `all <class name\>` --or-- `<class name\>.all()` |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file). | `update <class name\> <id\> <attribute name\> "<attribute value\>"` ---or--- `<class name\>.update(<id\>, <attribute name\>, <attribute value\>)` --or-- `<class name\>.update(<id\>, <dictionary representation\>)`|
| **count** | Retrieve the number of instances of a class.  | `class name\>.count()` |

## Examples
### Primary Command Syntax
**Example 0: Create an object**
Usage: create <class_name>
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
**Example 1: Show an object**
Usage: show <class_name> <_id>
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
  
**Example 2: Destroy an object**
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```

**Example 3: Update an object**
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
## Alternative Syntax
**Example 0: Show all User objects**
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

**Example 1: Destroy a User**
Usage: <class_name>.destroy(<_id_>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
**Example 2: Update User (by attribute)**
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
**Example 3: Update User (by dictionary)**
Usage: <class_name>.update(<_id>, )
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

## Authors
👤 **ABDUL-FATAHU HARDI**
- GitHub: [@at-tawlib](https://github.com/at-tawlib)

👤 **Forster Asamany **
- Github: [@fasamany1](https://github.com/fasamany1)
