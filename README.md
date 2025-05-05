# Dataclass objects

To support dataclass objects we added a DataClassType, which functioned similarly to Callable, to map field names to types.
In typecheck, we added cases in tc_stmt for ClassDef's and FieldRef's, as well as kept track of all dataclass-valued variables for later use.
In remove complex operands, we added cases for ClassDef's and FieldRef's. For field refs, we make sure the expression in field ref is atomic.
We created a new pass called eliminate objects before running the typechecker again. In this pass we removed ClassDef's 
and dealt with Fieldref's by turning them into tuple subscripts and turned function calls to object constructors in the form of a primitive tuple where each element in the tuple represents a field of the object.
The rest of the compiler is identical to the passes in assignment 7. 

Some challenges we faced include creating test cases that can be parsed by the existing parser, and running typecheck after eliminate_objects. Originally, we tried to write programs with the correct Python syntax for dataclasses and objects, but the parser didn't recognize methods embedded within the class definition, or constructors for a class. In order to overcome this, we stopped trying to use correct Python syntax, and instead focused on writing test cases which would parse, while trying to remain as similar to correct Python as possible. We also struggled with getting the assertions in typecheck to accurately detect when an object's type is a class or not, especially in test cases which implement 'has-a' relationships (see test4 and test5).

We wanted to be able to implement more features in our classes, like being able to use a wider variety of types as fields, or being able to print more to the console, but we were limited by the types that we know how to implement so far (bool and int), as well as the GlobalVal functions (like print_int). We also considered implementing superclasses, as the structure for ClassDef would have supported this. It would have been much more to take on if we wanted to implement these features, but with more time, we could have done so.