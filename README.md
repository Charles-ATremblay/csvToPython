# CSV to Python Class Generator

The CSV to Python Class Generator is a program designed to generate a Python class from a CSV file. The generated Python class will have attributes corresponding to the columns in the CSV file, along with methods for accessing and modifying those attributes.

## Usage

1. Ensure you have Python installed on your system.

2. Clone this repository or download the `csv_to_python.py` file.

3. Prepare your CSV file with the data you want to convert to a Python class.

4. **Modify the JSON config file named `config.json`. The JSON file should have the following structure:**
   ```json
   {
       "csv_file_path": "path\\to\\your\\csv\\file.csv"
   }
   Replace "path\\to\\your\\csv\\file.csv" with the actual path to your CSV file.

   If you skip this step, the program will display an error message and exit.

5. Run the `csv_to_python.py` script using the following command:
    python csv_to_python.py

The program will read the CSV file path from the config file and generate a Python file with the same name as the CSV file in the same directory. The Python file will contain a class representing the attributes of the CSV file.

Use the generated Python class in your Python programs by importing it.

## Example

Suppose you have a CSV file named `sample1.csv` with the following contents:

id,name,age,email
1,John Doe,30,johndoe@example.com
2,Jane Smith,25,janesmith@example.com


Running the program with this CSV file will generate a Python file named `sample1.py` with the following contents:

```python
class Sample1:
    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getEmail(self):
        return self.email

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setEmail(self, email):
        self.email = email
```

You can now import and use the Sample1 class in your Python programs.

Dependencies
    - csv
    - os
    - json