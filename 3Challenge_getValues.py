#Function to get Values from a keyValue pair

def get_values(d):
    for k, v in d.items():
        if isinstance(v, dict):
          #recursively call get_value function
          get_values(v)
        else:
            print("Value if this object is {1}".format(k, v))


D= {"a":{"b":{"c":{"z":"d"}}}}
#D1={"name":"john" , "age":"26"}

print(D)
#Calling get_values function by passing an object
get_values(D)
