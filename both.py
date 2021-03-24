from flask import Flask
from operations import Operation
from exe import *
app=Flask(__name__)
@app.route('/<method>/<int:a>/<int:b>')
def adding(method,a,b):
        obj=Operation(a,b)
        if method=="add":
                try:
                        if a<10 and b<10 :
                                res=obj.add()
                                return str(res)
                        else:
                                raise adderror("more than 10 add will not performed")
                except adderror as e:
                      return str(e)
        if method=="sub":
                try:
                        if a>b:
                                res1=obj.sub()
                                return str(res1)
                        else:
                                raise suberror("b is greater") 
                except suberror as f:
                        return str(f)
        if method=="mul":
                try:
                        if a<10 and b<10 :
                                res2=obj.mul()
                                return str(res2)
                        else:
                                raise mulerror("more than 10 mutiplication is not possible")
                except mulerror as g:
                        return str(g)
        if method=="div":
                try:
                        if b!=0:
                                res2=obj.div()
                                return str(res2)
                        else:
                                raise diverror("provide b as non zero value")
                except diverror as h:
                        return str(h)
        
if __name__ == "__main__":
    app.run(port=5009,debug=True)


