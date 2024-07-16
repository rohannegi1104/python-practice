#Strings Slicing and Operations on Strings in Python


names = "Rohan"
print(len(names))
print(names[0:5])
print(names[0:3])
print(names[:3])
print(names[1:4])
print(names[:])

#negative slicing

print(names[0:-3]) #or
print(names[0:len(names)-3])  #both will give same output


print(names[-3:-1])    #  r  o  h  a  n
                       # -4 -3 -2 -1  0

# h   a   r   r  y
# -4 -3 -2   -1  0


# ra


nm = "Harry"
print(nm[-4:-2])