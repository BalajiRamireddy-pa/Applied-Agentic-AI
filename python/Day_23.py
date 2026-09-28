# Modules 

'''
in this file we will create some user def funcs,var,class
'''
def greet(name):
    """User define func"""
    return f"Hello {name}"
greet("Code")    

names = {
        'Students':['sai','aksash','ajay'],
        'Ages':[12,25,35]   
}

print(names)

if __name__ == "__main__":
   print(__name__)
print(__name__)


def display():
    yield "Python"
    yield "GenAi"
    yield "Rag"
    yield "Agentic"