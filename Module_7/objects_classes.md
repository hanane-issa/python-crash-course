# welcome to Module 7

In this module, we will go through objects and classes in Python.

# Classes and objects

Python is an object-oriented programming (OOP) language, almost everything in Python is an object. However, Python would also allow you to go away from OOP and use other programming style such as procedural and functional.

### What are classes and objects?

In layman's terms, classes are templates/blueprints that you make your objects out of and objects are instances of a class. 

### Why do we use them?

There are some advantages of using OOP in Python:
- You can have better organization of your code, since you can group related data together.
- You can reuse some of your code, as you can create multiple objects from the same blueprint.
- Build hierarchies of classes, to further organize your code.

## Examples

Let's see some concrete examples of a class, we will write a blueprint to create a "dog" object.

```
class Dog:
    species = 'Canis lupus familiaris'
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

```

`def __init__()` is referred to as the constructor, it is a special method used to initialize your object. The word `self` is the first argument which refers to the specific instance of the object, in fact it does not have to be the word `self` but it is a common convention, no need to change it. In this example, there are three information that you need to create the `Dog` object, name, age and owner. That information will become the attributes of the object you create and you will be able to access them later.

Let's create our first object:
```
Buddy = Dog("Buddy", 5, "Alice")
```
Now, we can ask Python what is this object by typing:
```
type(Buddy)
```
and it will give you this: `__main__.Dog`. This is telling you the class `Dog` is from the module/script `__main__`, and `__main__` is the script that we are executing the code from.


## Attributes

You can access the attributes by using the dot `.` after the name of the object and the attribute you want. For example, if we want to print the name of `Buddy`, we will type:
```
print(Buddy.name)
```
In the same way you can access the age and the name of the owner.

You can also add a new attribute, for example:
```
Buddy.breed = 'Labrador'
```

Now you can type `Buddy.__dict__` to access the attribute names and their values.

However, if you add an attribute that is not in the class blueprint, it will not show up in the new `Dog` object.

Attributes like `name`, `age` and `owner` are instance attributes, meaning they are specific to the objects created. Whereas `species` is a class attribute, this value will be the same for all objects created from the same class blueprint, until it is changed by you.

## Creating methods

We can add methods to the `Dog` class and make it do certain things. 
It is similar to the `.lower()` method of a string class, if you type:
`'DOG'.lower()` Python will return `dog` because the method converted all uppercase letters to lower case.

We can, for example, add a method like so:
```
class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
    
    def bark(self):
        return 'Woof'
```

If we create a new `Dog` instance with `Buddy = Dog("Buddy", 5, "Alice")`, we should be able to use that method like so:
```
print(Buddy.bark())
```
You should get `Woof`. 

## Make setter and getter methods

You can actually change the attributes of the object. If you type `Buddy.name == 'Max`, the attribute `name` will be changed to 'Max'. This sometimes may not be a good behavior that you want, so why don't we try to add another layer to protect the attributes.

```
class Dog:
    def __init__(self, name, age, owner):
        self._name = name
        self._age = age
        self._owner = owner

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("age cannot be negative")
        self._age = new_age
    
    def bark(self):
        return 'Woof'
```

Python does not really hide attributes with `_` in front, but it tells other users they should not modify them directly. 
The `@property` is called a decorator, it changes the properties for the method that it is applied to. In this case, it changes the methods `name()` and `age()` so that they can be called just like an attribute. `name()` and `age()` are getter methods, because they get you the attributes you want. 
So now if you type `Buddy.name = 'Max'`, you should get an error: `AttributeError: can't set attribute 'name'`.

What about setting the attribute? We can do so by using a setter method. The decorator `@age.setter` tells python the method is a setter method for `age`. You can also ensure that the new value makes sense, for example, the new age is not negative.

## Inheritance and polymorphism

What if you want to create several classes and there is a relationship between them? Well, we can try using a concept in OOP called inheritance. 
Let's go straight into an example. Say you want to create a dog class and a cat class, since they are both mammal, domesticated and cute etc. we can create a parent class for them. 

```
class Mammal:
    species_name = ''
        def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_noise(self):
        return ''
```
Now that we have a blueprint of a parent class, we can create blueprints for the child classes. The child classes will build upon the parent class, they will 'inherit' the attributes and methods from the parent. But the child classes can also add new attributes and methods if its own. Let's create a `Dog` and a `Cat` class.
```
class Dog(Mammal):
    species_name = 'Canis lupus familiaris'
    def make_noise(self):
        return 'Woof'
class Cat(Mammal):
    species_name = 'Felis catus'
    def make_noise(self):
        return 'Meow'
```
To inherit from a class, we put the parent class that we want to inherit from in the parenthesis of the new class like so: `class Dog(Mammal)`.
In our `Dog` and `Cat` classes, we do not need to define the `__init__()` method because it is already defined in the parent class. If you want to create a `Dog` object, you will have to specify the name and age like so: `Dog("Buddy",5)`. 
We have redefined the class attribute from the parent class `species_name` in each child class, and redefine the method `make_noise()`. Redefining can also be called overriding in OOP language, we can override the parent attributes and methods and make the child's attributes and methods unique. 
If you do not override, the child will inherit directly from the parent, in our case `species_name` will be an empty string and the method `make_noise()` will also return an empty string.

### Adding methods

We can also add methods specific to the child classes.
```
class Dog(Mammal):
    species_name = 'Canis lupus familiaris'
    def make_noise(self):
        return 'Woof'
    def swim(self):
        return 'swimming'
class Cat(Mammal):
    species_name = 'Felis catus'
    def make_noise(self):
        return 'Meow'
    def climb(self):
        return 'climbing'
```

We have added a `swim()` method to the `Dog` class and a `climb()` method to the `Cat` class. These methods are specific to their own class. The shows the flexibility of inheritance, even though the two classes inherited from the same parent, you can still make the child classes unique.

### Extending methods

What if you don't want to override the parent's method but to extend it, can we do that? Most certainly yes. We use the method `super()` to do so.

```
class Dog(Mammal):
    species_name = 'Canis lupus familiaris'
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_noise(self):
        return 'Woof'
    def swim(self):
        return 'swimming'
```
Within the new constructor method, we use `super()` to call the constructor method from the parent class and give it the same parameters `name` and `age`. Then, we added another parameter to construct a `Dog` object which is this line `self.breed = breed`. Now, if you want to create a `Dog` object, you will need an extra parameter: `Buddy = Dog("Buddy",5, 'rottweiler')`.


### Why use inheritance?

These are some of the advantages of using inheritance in Python:
- Reuse code. If you are creating multiple child classes, you do not have to write the same code every time.
- Better organization. If you have a real-world relationship between classes you want to preserve, inheritance is a good way to do it. 
- Modularity. You can split your code into different small chunks.
- Flexibility. New attributes and methods can be added to the child classes to make them unique.
- Polymorphism. The child classes can be treated in a similar way because they have inherited the attributes and methods from the parent. We can do so even without knowing the specific methods to each child class.


## Concrete example

So in what way are classes and objects related to what we have learned in the previous modules? Well, remember module 4 where we learned to used Pandas DataFrames and module 5 where we learned how to visualize data? Pandas DataFrame is actually a class and we can create our own child class to visualize the data.

### Loading packages and the data

First, let's do the usual and import necessary packages.
```
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

Now, let's also import the dataset that we have been working on in the previous modules.

```
path_to_file = '/the/path/to/healthcare-dataset-stroke-data.csv'
stroke_data = pd.read_csv(path_to_file)
```

### pandas.core.frame.DataFrame

If you check the type of the object stroke_data with the command `type(stroke_data)`, you will see that it belongs to `pandas.core.frame.DataFrame`.
Just like our example of `Mammal` and `Dog`, it has its own attributes and methods.

For example, `.index`, `.shape` and `.columns` etc., are attributes. `.index` will give you the index of the dataframe, `.shape` will give you the shape of the dataframe and `.columns` will give you the name of the columns.

Whereas `.head()`, `.tail()` and `.info()` etc., are methods of the Pandas DataFrame class. 

### Create our own child class

Now, what if you don't like the way the index of a dataframe is being returned by the Pandas Dataframe class? 
What if you want to customize the the built-in plotting methods so that you don't have to explicitly write the code every time? 
You can create your own child class and inherit from the parent class, which in this case is the Pandas Dataframe class. This way you will retain a lot of other functionalities.

We will write our own child class, we will call it `MyDataFrame`

```
class MyDataFrame(pd.DataFrame):
    @property
    def _constructor(self):
        return MyDataFrame

    @property
    def index(self):
        real_idex = super().index
        return real_idex.tolist()

    def hist(self, column, **kwargs):
        plt.hist(self[column], bins=30, alpha=0.6, edgecolor='black')
        plt.xlabel('Value', fontsize=14)
        plt.ylabel('Probability density',fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.title('Normalized Histogram (Density)', fontsize=18)
        return 
```
We have since `@property` from before in this module, it allows the method `_constructor()` to behave like an attribute so we can call it without the parentheses. We have to define the `_constructor()` method because if we do an operation like slicing (using `.loc`), it will return another object of our class `MyDataFrame` and not the parent class.

We have overridden the `.index` attribute from `pd.DataFrame`. We have called the original attribute by using `super().index`, then we return the index that has been converted to a list object by using `.tolist()`.

We have also overridden the `hist()` method for plotting a histogram plot from the `pd.DataFrame` class. We have opted to use `hist()` method from `matplotlib`, we have also added the x and y labels, ticks and a title. Note that we are using the `matplotlib.pyplot` module in the method, so you will have to import the `matplotlib` before you instantiate your subclass or directly put it in the method just in case.
```
    def hist(self, column, **kwargs):
        import matplotlib.pyplot as plt
        plt.hist(self[column], bins=30, alpha=0.6, edgecolor='black')
        plt.xlabel('Value', fontsize=14)
        plt.ylabel('Probability density',fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.title('Normalized Histogram (Density)', fontsize=18)
        return 
```

### Testing

Now, let's convert a dataframe into our class `my_stroke_data = MyDataFrame(stroke_data)`

If you try `type(my_stroke_data)`, it will return our subclass `MyDataFrame`. NICE!!
Try getting the index with `my_stroke_data.index`, it will return a list. Double NICE!!
And finally, if you try plotting a histogram using `my_stroke_data.hist('age')`, you will get a `matplotlib` histogram instead of the original plot.


## Conclusion

In this tutorial, we have gone through the fundamentals of object-oriented programming in Python using classes and objects. You learned how to define a class, instantiate an object, and use attributes and methods. 

Understanding classes and objects is essential for writing clean, modular and reusable code. This is especially important when building larger applications or modeling real-world systems. As you learn more about Python, you can consider applying what you learned to build scalable tools for your own use or for others. 

Keep calm and code on.








