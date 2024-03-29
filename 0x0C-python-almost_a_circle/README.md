# 0x0C. Python - Almost a circle

## Tasks

### [00. If it's not tested it doesn't work]
* All your files, classes and methods must be unit tested and be PEP 8 validated.

### [01. Base class]
* Write the first class `Base`:

### [02. First Rectangle]
* Write the class `Rectangle` that inherits from `Base`:

### [03. Validate attributes]
* Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

### [04. Area first]
* Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

### [05. Display #0]
* Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.

### [06. __str__]
* Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

### [07. Display #1]
* Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`

### [08. Update #0]
* Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

### [09. Update #1]
* Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

### [10. And now, the Square!]
* Write the class `Square` that inherits from `Rectangle`:

### [11. Square size]
* Update the class `Square` by adding the public getter and setter `size`

### [12. Square update]
* Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

### [13. Rectangle instance to dictionary representation]
* Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`:

### [14. Square instance to dictionary representation]
* Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`:

### [15. Dictionary to JSON string]
* JSON is one of the standard formats for sharing data representation.
* Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:

### [16. JSON string to file]
* Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:

### [17. JSON string to dictionary]
* Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:

### [18. Dictionary to Instance]
* Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:

### [19. File to instances]
* Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances:

