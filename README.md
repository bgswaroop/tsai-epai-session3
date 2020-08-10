# EPAi session4 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session4 objectives
This assignment, helps to code the concepts that are learnt in the session 4 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 
- Floats :  Coercing to Integer
- Floats :  Rounding
- Decimals
- Decimals :  Constructors and Contexts
- Decimals :  Math Operations
- Decimals :  Performance Considerations
- Complex Numbers
- Booleans
- Booleans :  Precedence and Short-Circuiting

---

The test cases can be executed by executing _pytest_, from python shell

---
### Class Qualean methods

**__init__(self, state)**

    Initialize the Qualean object
     : param state : 
        
**__and__(self, other)**

    Bitwise `&` operator between two Qualeans
     : param other :  Qualean
     : return :  Qualean
    
**__or__(self, other)**

    Bitwise `|` operator between two Qualeans
     : param other :  Qualean
     : return :  Qualean

**__repr__(self)**

    String representation of the object of the Qualean class
     : return :  string
    
**__str__(self)**

    Readable string representation of the qualean
     : return :  string    

---

### Unit tests

**test_readme_exists**
    
    Check if the README file exists
     : return :  None
    
**test_readme_contents**

    Test the length of the README file
     : return :  None
    
**test_readme_file_for_formatting**

    Tests the formatting for the README file
     : return :  None
    
**test_function_name_had_cap_letter**
    
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_invalid_input_type**

    Valid input types to Qualean() class are float, int and Decimal
     : return :  None

**test_invalid_input_value**

    Check input values to Qualean() class. Expected values are {-1, 0, +1}
     : return :  None

**test_invalid_input_for__and__**

    Ensuring correctness of object type, for __and__()
     : return :  None
    
**test_and_case1**

    Test the bitwise and operator on two qualeans
     : return :  None
    
**test_and_case2**

    Test the boolean and operator, in a short-circuit scenario
     : return :  None

**test_invalid_input_for__or__**
    
    Ensuring correctness of object type, for __or__()
     : return :  None
    
**test_or_case1**

    Test the bitwise `or` operator
     : return :  None
    
**test_or_case2**

    Test the boolean or operator, in a short-circuit scenario
     : return :  None

**test_rectangle_repr**
    
    Ensuring that __repr__ yields string in expected format
     : return :  None

**test_rectangle_str**
    
    Ensuring that __str__ yields string in expected format
     : return :  None
    
**test_invalid_input_for__add__**

    Ensuring correctness of object type, for __add__()
     : return :  None

**test_add_case1**

    Test the add operation by adding q1 100 times and check the result
     : return :  None

**test_add_case2**

    Test the add operation by adding 3 random qualeans
     : return :  None

**test_add_case3**

    Test the sum of 1 million different q's
     : return :  None

**test_invalid_input_for__eq__**

    Ensuring correctness of object type, for __eq__()
     : return :  None

**test_eq**

    Test the '==' operator
     : return :  None
    
**test_invalid_input_for__ge__**

    Ensuring correctness of object type, for __ge__()
     : return :  None

**test_ge**

    Test the '>=' operator
     : return :  None

**test_invalid_input_for__gt__**

    Ensuring correctness of object type, for __gt__()
     : return :  None
    

**test_gt**
    
    Test the '>' operator
     : return :  None

**test_invalid_input_for__le__**

    Ensuring correctness of object type, for __le__()
     : return :  None
    
**test_le**

    Test the '<=' operator
     : return :  None

**test_invalid_input_for__lt__**

    Ensuring correctness of object type, for __lt__()
     : return :  None
    
**test_lt**

    Test the '<' operator
     : return :  None

**test_invalid_input_for__mul__**
    
    Ensuring correctness of object type, for __mul__()
     : return :  None
    

**test_mul**
    
    Test the '*' operator
     : return :  None
    
    
**test_sqrt**
    
    Test the sqrt() method
     : return :  None
    
**test_bool**
    
    Test the bool operator
     : return : 
    
---

#### 