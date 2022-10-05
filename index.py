"""functions"""
temp = "global"
def sandbox():
    print("in first function")

    def another():
        print("one level deep",temp)
    
    return another

sandbox()()
    
