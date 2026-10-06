#Error message said TypeError: can't multiply sequence by non-int of type 'str'
# This occurred because you can't multiply strings.
# Fixed it to use + so string would be concatenated
first_name = "Suzy"
last_name = "Mann"
result = first_name + last_name
print ("result: " + result)
