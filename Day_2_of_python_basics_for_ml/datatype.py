
IN PYTHON THERE ARE SOME DATATYPES 
📘 Datatypes in Python
🔹 Python me Datatype kya hota hai?

Python ek dynamically typed language hai.
Iska matlab ye hai ki hume datatype manually define karne ki zarurat nahi hoti.

Example:

x = 10


Yahan humne nahi bataya ki x integer hai,
lekin Python khud samajh jata hai ki 10 ek number (integer) hai.

🔹 Datatype ki zarurat kyun hoti hai?

Programming me hum variables ke saath kaam karte hain.
Har variable ke liye 2 important cheezein hoti hain:

1️⃣ Us variable par kaun-kaun se operations possible hain
2️⃣ Us variable ko kitni memory chahiye

Example:
23 + 10      # ✅ valid
23 + "sum"   # ❌ invalid


Hum insaan easily samajh jate hain ki:

23 ek number hai

"sum" ek string (text) hai

Aur number + text possible nahi hota.

⚠️ Computer ye sab khud se nahi samajhta,
isliye use batana padta hai:

ye number hai

ye string hai

ye decimal hai

ye true/false hai

Isi information ko datatype kehte hain.

🔹 Python Datatypes

Python khud datatype detect kar leta hai,
lekin hume samajhna zaruri hai taaki hum sahi logic likh sakein.

 DATATYPES

1. numeric
  i. interger
  ii. complex 
  iii. float
2. sequence
  i. string
  ii. list
  iii. tuple
3. dictionary
4. set
5. boolean
🔹 Datatypes in Python

Python automatically detects datatypes, but we must understand them to write correct logic.

1️⃣ Numeric Datatypes
i. Integer (int)

Whole numbers (positive or negative)

a = 10
b = -5

ii. Float (float)

Decimal numbers

pi = 3.14

iii. Complex (complex)

Real + imaginary numbers

z = 2 + 3j

2️⃣ Sequence Datatypes
i. String (str)

Text data

name = "Ashish"

ii. List (list)

Ordered and changeable

numbers = [1, 2, 3]

iii. Tuple (tuple)

Ordered and unchangeable

point = (10, 20)

3️⃣ Dictionary (dict)

Stores data in key–value pairs

student = {
    "name": "Ashish",
    "age": 21
}

4️⃣ Set (set)

Stores only unique values

unique_numbers = {1, 2, 3}

5️⃣ Boolean (bool)

Represents True or False

is_logged_in = True

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lets start with integer in memory 

so in python we can store any long integer as it stores in memory like a array of bunch of numbers blocks of numbers 
📌 How Python Stores Large Integers

Yes, in Python we can store very large integers.

Unlike languages such as C or C++, Python does not have a fixed size for integers (like 32-bit or 64-bit).

Example:

x = 10**100
print(x)


Python can handle this without any overflow.

🧠 How does Python store such large numbers?

Internally, Python stores integers as objects, not simple fixed-size numbers.

A Python integer is stored in multiple memory blocks

Each block holds a part of the number

Together, these blocks represent the full integer

You can think of it conceptually like:

a list (array) of number chunks stored in memory

----------------------------------------------------------------------------------------------------------------------------------------------------------------
WHAT ABOUT FLOATING POINT NUMBERS 
🔴 Why integers can be stored as “array of blocks”

Integers are discrete.

Example:

12345678901234567890


This can be perfectly split into chunks:

[d0, d1, d2, ...]


Each chunk represents an exact value.
No ambiguity. No loss.

That’s why Python can store integers as:

array of base-2³⁰ digits

🔵 Why floats are different (CORE REASON)

Floats represent real numbers, like:

0.1
1.3
π
√2


The problem is 👉 most decimal numbers cannot be represented exactly in binary.

Example (VERY IMPORTANT):
0.1 (decimal)


In binary:

0.0001100110011001100110011... (infinite)


⚠️ It never ends.

So if Python tried to store floats as “arrays of digits”:

Memory would be infinite ❌

Operations would never finish ❌

🧠 So what do computers do instead?

They use a scientific-notation-like format called
👉 IEEE-754 Floating Point Representation

A float is stored as:

sign × mantissa × 2^exponent

🧱 Actual Float Structure (64-bit float)
Part	Bits
Sign	1
Exponent	11
Mantissa (fraction)	52

This gives:

Fast calculations

Fixed memory size

Approximate values

⚠️ This is why floats are inaccurate
0.1 + 0.2


Result:

0.30000000000000004


Not a Python bug ❌
This happens in C, Java, JavaScript, everywhere.

❌ Why Python does NOT use arbitrary precision for floats

If Python used “big-float arrays” like integers:

❌ Extremely slow

❌ Huge memory usage

❌ No standard hardware support

❌ Breaks math libraries & CPUs

CPUs are designed in hardware to handle IEEE-754 floats efficiently.

🟢 But can Python do high-precision decimals?

YES ✅
Using decimal module:

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3


But:

Much slower

Used only when precision is critical (finance)

