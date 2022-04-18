import json
import sys

# def X():
with open(sys.argv[1], 'r') as f:
    a = json.load(f)    #此时a是一个字典对象
print(a)

 


# if __name__ =='__main__':
#     X()
