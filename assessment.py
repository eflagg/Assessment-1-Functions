# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def calculate_item_cost(cost, state, tax = .05):
	"""Calculates total cost of an item.


	Multiplies the tax by the cost and then adds that to cost to get total. Tax is set
	at %5 by default. Tax changes to 7% when state is California"
	"""

	if state == "CA":
		tax = .07
	total = cost + (cost * tax)
	return total

calculate_item_cost(100, "CA")

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".


def is_berry(fruit):
	"""Determines if fruit is berry or not.

	Returns true if fruit is strawberry, cherry, or blackberry. Otherwise returns false.
	"""

	if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":	
		return True
	else:
		return False


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
	"""Determines shipping cost of fruit
	
	Calls is_berry function, if true, shipping cost is 0, otherwise shipping cost is 5.
	"""

	if is_berry(fruit) == True:
		#print 0 test
		return 0
	elif is_berry(fruit) == False:
		#print 5 test
		return 5

#shipping_cost("apple") test
# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
def is_hometown(town):
	"""Determines if user hometown is same as mine

	If hometowns are the same, returns true. Otherwise, returns false
	"""

	if town == "Washington, DC":
		return True
	else:
		return False


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#

def full_name(first, last):
	"""Creates full name


	Concatenates first and last names to create full name
	"""

	return first + " " + last


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town, first, last):
	"""Creates a greeting using user full name and hometown

	Calls is_hometown and full_name functions and prints greeting using results
	"""

	if is_hometown(town) == True:
		print "Hi, %s, we're from the same place!" % (full_name(first, last))
	elif is_hometown(town) == False:
		print "Hi, %s, where are you from?" % (full_name(first, last))


#hometown_greeting("Washington, DC", "Jane", "Doe") test
#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x = 1):
	"""Outer function in addition

	Sets an integer to a variable, returns inner add function
	"""

	def add(y):
		"""Adds x and y

		Takes x from increment function and adds it to argument y
		"""

		#print x + y test
		return x + y
	return add


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20. 

addfive = increment(5)
addfive(20)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def add_number(number, number_list):
	"""Appends number to list

	Appends number given as argument to list entered as argument
	"""

	number_list.append(number)
	#print number_list test
	return number_list

#add_number(5, [7, 6, 9, 55]) test
#####################################################################