# Python - Almost Circle !
[Circle](https: //s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4) In this project: Knowledge of object-oriented Python  programming by coding three related classes to represent rectangles and squares.
 I created my own test suite using the unittest module to test all the functions in each class.
 The three classes used the following Python tools.
 * Imports * Exceptions * Private Attributes * Getters/Setters * Classes/Static Methods * Inheritance * File I/O * 'args'/ ' kwargs ' * JSON and CSV Serialization/ Deserialization * Unit tests ## Tests: Heavy_check_mark: * [tests/test_models](.
/tests/test_models): Folder containing the following independently developed test files: * [ test_base.py](.
/tests/test_models/test_base.py) * [test_rectangle.py](.
/tests/test_models/test_rectangle.py) * [test_square.py](.
/tests/ test_models /test_square .py ) ## Class: cl: ### Base Represents the "base" class for all other classes in the project.
 Contains: * Private class attribute "__nb_objects = 0 ".
 * Public instance attribute 'id'.
 * Class constructor 'def __init__(self, id=None): ' * If 'id' is 'None', increment '__nb_objects' and assign its value to  public instance attribute 'id'.
 * Otherwise,  the public instance attribute 'id' is set to the specified 'id'.
 * Static method 'def to_json_string(list_dictionaries): ' returns her JSON string serialization of the list of dictionaries.
 * If "list_dictionaries" is "None" or empty,  the string "[]" is returned.
 * Class method 'def save_to_file(cls, list_objs): ' that writes the JSON serialization of a list of objects to a file.
 * The ``list_objs'' parameter  is expected to be a list of ``Base'' inherited instances.
 * If list_objs is None, the function saves an empty list.
 * The file will be saved as ".json" (e.g.
 "Rectangle.json").
 * Overwrite the file if it already exists.
 * Static method "def from_json_string(json_string): " that returns a list of objects deserialized from a JSON string.
 * The json_string parameter  is expected to be a string representing a list of dictionaries.
 * If json_string is None or empty, the function returns an empty list.
 * The class method 'def create(cls, **dictionary): '  instantiates an object with the specified attributes.
 * Instantiate the object with the attributes specified by "**dictionary".
 * Class method 'defload_from_file(cls): ' that returns a list of objects instantiated from a JSON file.
 * Read from  JSON file ".json" (i.e.
 "Rectangle.json").
 * If the file does not exist, the function returns an empty list.
 * Class method 'def save_to_file_csv(cls, list_objs): ' that writes a CSV serialization of a list of objects to a file.
 * The ``list_objs'' parameter  is expected to be a list of ``Base'' inherited instances.
 * If list_objs is None, the function saves an empty list.
 * The file will be saved as ".csv" (i.e.
 "Rectangle.csv").
 * Serialize objects in the format ',,,,' for 'rectangle' objects and ',,,' for 'square' objects.
 object.
 * Class method 'defload_from_file_csv(cls): ' that returns a list of objects instantiated from a CSV file.
 * Read from  CSV file ".csv" (i.e.
 "Rectangle.csv").
 * If the file does not exist, the function returns an empty list.
 * Static method 'defdraw(list_rectangles, list_squares): ' draws 'Rectangle' and 'Square' instances in the GUI window using the 'turtle' module.
 * Parameter ``list_rectangles'' must be a list of ``Rectangle'' objects to print.
 * Parameter ``list_squares'' must be a list of ``square'' objects to print.


### Rectangle 
Represents a rectangle.
Inherits the following from "Base": * Private instance attributes "__width", "__height", "__x", and "__y".
 * Each private instance attribute has its own getter/setter.
 * Class constructor 'def __init__(self, width, height, x=0, y=0, id=None): ' * Any of 'width', 'height', 'x', or 'y'.
 If either integer is not specified, a "TypeError" exception is thrown with the message "Must be an integer".
  * If "width" or "height" >= 0, a "ValueError" exception is thrown with the message "must be > 0".
 * If either "x" or "y" is less than 0,  a "ValueError" exception is thrown with the message "Must be >= 0".
 * Public method ``def area(self): '' that returns the area of ​​a ``Rectangle'' instance.
 * Public method ``def display(self): '' that prints the ``Rectangle'' instance to ``stdout'' using the ``#'' character.
 * Print a newline at the "y" coordinate and a space at the "x" coordinate.
 * Override the __str__ method to output a Rectangle instance in the form [Rectangle] () /.
 * Public method ``def update(self, *args, **kwargs): '' that updates an instance of ``rectangle'' with the specified attributes.
 * '*args' must be specified in the following order: * First: 'id' * Second: 'width' * Third: 'height' * Fourth: 'x' * 5 : 'y' * '**kwargs' is intended to be a double pointer to a dictionary of new key/value attributes to update 'Rectangle'.
 * '**kwargs' is skipped if '*args' is present.
 * Public method ``def to_dictionary(self): '' that returns a dictionary representation of a ``Rectangle'' instance.


### Square 

Represents a square.
Inherited from ``Rectangle'': * Class constructor ``def __init__(self, size, x=0, y=0, id=None): ' * The ``width'' and ``height'' of ``rectangle''.
 difference".
 ' The superclass is assigned a 'size' value.
 * Override the "__str__" method to output "Square" instances in the format "[Square] () /".
 * Public method ``def update(self, *args, **kwargs): '' that updates an instance of ``Square'' with the specified attributes.
 * '*args' must be specified in the following order: * First: 'id' * Second: 'size' * Third: 'x' * Fourth: 'y ' * ' **kwargs' will be a double pointer to a directory of new key/value attributes to update 'square'.
 * '**kwargs' is skipped if '*args' is present.
 * Public method 'def to_dictionary(self): ' that returns the dictionary representation of 'square'.


