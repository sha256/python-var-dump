# var_dump #
**for python**


---



**var\_dump** is a PHP's `var_dump()` equivalent function for python. It displays structured information such as type, value etc of a python `object`, `list`, `tuple`, `dict` & other types. 

### Installation ###

----------
using `pip`

	pip install var_dump

Or

clone the project & cd into the `python-var_dump` directory
then run:
	
	python setup.py install
### Examples ###
----
#### Example #1: ####
	from var_dump import var_dump
	
	var_dump(123) 					# output: #0 int(123)
	var_dump(123.44) 				# output: #0 float(123.44)
	var_dump("this is a string") 	# output: #0 str(16) "this is a string"
	var_dump(None) # output: 		# output: #0 NoneType(None)
	var_dump(True) # output 		# output: #0 bool(True)

#### Example #2: ####
you can pass more than one argument:

	from var_dump import var_dump
	
	var_dump(123, 123.44, None, False)

#### Output: ####
	#0 int(123) 
	#1 float(123.44) 
	#2 NoneType(None) 
	#3 bool(False) 

#### Example #3: ####
    
	from var_dump import var_dump

	class Base(object):
	
	    def __init__(self):
	        self.baseProp = (33, 44)
			self.fl = 44.33

	class Bar(object):
	
	    def __init__(self):
	        self.barProp = "I'm from Bar class"
			self.boo = True
	
	
	class Foo(Base):
	
	    def __init__(self):
	        super(Foo, self).__init__()
	        self.someList = ['foo', 'goo']
	        self.someTuple = (33, (23, 44), 55)
	        self.anOb = Bar()
			self.no = None
	
	foo = Foo()
	var_dump(foo)

#### Output ####
	#0 object(Foo) (6)
	    baseProp => tuple(2) 
	        [0] => int(33) 
	        [1] => int(44) 
	    someTuple => tuple(3) 
	        [0] => int(33) 
	        [1] => tuple(2) 
	            [0] => int(23) 
	            [1] => int(44) 
	        [2] => int(55) 
	    no => NoneType(None) 
	    someList => list(2) 
	        [0] => str(3) "foo"
	        [1] => str(3) "goo"
	    fl => float(44.33) 
	    anOb => object(Bar) (2)
	        boo => bool(True) 
	        barProp => str(18) "I'm from Bar class"


**License: BSD License**
