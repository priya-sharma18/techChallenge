def get_values(d):
    for k, v in d.items():
        if isinstance(v, dict):
          #recursively call get_value function
          get_values(v)
        else:
            print("Value if this object is {1}".format(k, v))


#D1= {"a":{"b":{"c":{"z":"a"}}}}
D={"name":"john" , "age":"26"}
print(D)
#Calling get_values function by passing an object
get_values(D)
