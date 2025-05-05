# Dataclass objects

To support dataclass objects we added a DataClassType, which functioned similarly to Callable, to map field names to types.
In typecheck, we added cases in tc_stmt for ClassDef's and FieldRef's, as well as kept track of all dataclass-valued variables for later use.
In remove complex operands, we added cases for ClassDef's and FieldRef's. For field refs, we make sure the expression in field ref is atomic.
We created a new pass called eliminate objects before running the typechecker again. In this pass we removed ClassDef's 
and dealt with Fieldref's by turning them into tuple subscripts and turned function calls to object constructors in the form of a primitive tuple where each element in the tuple represents a field of the object.
The rest of the compiler is identical to the passes in assignment 7. 

Some challenges we faced