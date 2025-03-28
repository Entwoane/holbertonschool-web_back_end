# ES6 Classes

## Learning objectives


- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Tasks

### 0. You used to attend a place like this at some point

Implement a class named ClassRoom:

- Prototype: export default class ClassRoom
- It should accept one attribute named maxStudentsSize (Number) and assigned to _maxStudentsSize

File: 0-classroom.js


### 1. Let's make some classrooms

Import the ClassRoom class from 0-classroom.js.

Implement a function named initializeRooms. It should return an array of 3 ClassRoom objects with the sizes 19, 20, and 34 (in this order).

File: 1-make_classrooms.js


### 2. A Course, Getters, and Setters

Implement a class named HolbertonCourse:

- Constructor attributes:
    - name (String)
    - length (Number)
    - students (array of Strings)
- Make sure to verify the type of attributes during object creation
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.

File: 2-hbtn_course.js


### 3. Methods, static methods, computed methods names..... MONEY

Implement a class named Currency:

- Constructor attributes:
  - code (String)
  - name (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.
- Implement a method named displayFullCurrency that will return the attributes in the following format name (code).

File: 3-currency.js


### 4. Pricing

Import the class Currency from 3-currency.js

Implement a class named Pricing:

- Constructor attributes:
  - amount (Number)
  - currency (Currency)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter and setter for each attribute.
- Implement a method named displayFullPrice that returns the attributes in the following format - currency_name (currency_code).
- Implement a static method named convertPrice. It should accept two arguments: amount (Number), - (Number). The function should return the amount multiplied by the conversion rate.

File: 4-pricing.js


### 5. A Building

Implement a class named Building:

- Constructor attributes:
	- sqft (Number)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter for each attribute.
- Consider this class as an abstract class. And make sure that any class that extends from it should implement a method named evacuationWarningMessage.
	- If a class that extends from it does not have a evacuationWarningMessage method, throw an error with the message Class extending Building must override evacuationWarningMessage

File: 5-building.js


### 6. Inheritance

Import Building from 5-building.js.

Implement a class named SkyHighBuilding that extends from Building:

- Constructor attributes:
	- sqft (Number) (must be assigned to the parent class Building)
	- floors (Number)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Implement a getter for each attribute.
- Override the method named evacuationWarningMessage and return the following string Evacuate slowly the NUMBER_OF_FLOORS floors.

File: 6-sky_high.js


### 7. Airport

Implement a class named Airport:

- Constructor attributes:
	- name (String)
	- code (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- The default string description of the class should return the airport code (example below).

File: 7-airport.js


### 8. Primitive - Holberton Class

Implement a class named HolbertonClass:

- Constructor attributes:
	- size (Number)
	- location (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- When the class is cast into a Number, it should return the size.
- When the class is cast into a String, it should return the location.

File: 8-hbtn_class.js


### 9. Hoisting

Fix this code and make it work.
```
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
  }
}


export const listOfStudents = [student1, student2, student3, student4, student5];
```
Result:
```
bob@dylan:~$ cat 9-main.js
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
    student => student.fullStudentDescription
);

console.log(listPrinted)

bob@dylan:~$ 
bob@dylan:~$ npm run dev 9-main.js
[
  StudentHolberton {
    _firstName: 'Guillaume',
    _lastName: 'Salva',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'John',
    _lastName: 'Doe',
    _holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Albert',
    _lastName: 'Clinton',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Donald',
    _lastName: 'Bush',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  },
  StudentHolberton {
    _firstName: 'Jason',
    _lastName: 'Sandler',
    _holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
  }
]
[
  'Guillaume Salva - 2020 - San Francisco',
  'John Doe - 2020 - San Francisco',
  'Albert Clinton - 2019 - San Francisco',
  'Donald Bush - 2019 - San Francisco',
  'Jason Sandler - 2019 - San Francisco'
]
bob@dylan:~$ 
```

File: 9-hoisting.js


### 10. Vroom

Implement a class named Car:

- Constructor attributes:
	- brand (String)
	- motor (String)
	- color (String)
- Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
- Add a method named cloneCar. This method should return a new object of the class.

Hint: Symbols in ES6

File: 10-car.js
