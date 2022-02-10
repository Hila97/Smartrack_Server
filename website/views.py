from flask import Blueprint, render_template, flash ,request
import numpy
from same_size_k_means import eqsc
views = Blueprint('views',__name__)

@views.route('/')
def home():
    if request.method == 'POST':
        name = request.form.get('name', category="success")
        if name == "hila":
           flash(name)
    my_arr = numpy.array([[32.0962934,34.7726703],[51.5478302,-0.1512823],[51.5763589,-0.2236956],[34.008576,-118.498101]])
    return render_template("base.html", text ="Text",user="Hodaya",arr=my_arr)

@views.route('/plan_route/<params>')
def plan_route(params):
    if request.method == 'GET':
        #  str = "32.0962934,34.7726703#51.5478302,-0.1512823#51.5763589,-0.2236956#34.008576,-118.498101"
        list_location = list(params.split("#"))
        for i in range(0,len( list_location)):
            list_location[i] = list( list_location[i].split(","))
            for j in range(0,len( list_location[i])):
                list_location[i][j]=float( list_location[i][j])
            
#     print(type(li[0]))
#     print(li)
#     str1 = [[32.0962934,34.7726703],[51.5478302,-0.1512823],[51.5763589,-0.2236956],[34.008576,-118.498101]]
#     print(type(str1[0][0]))
        X=numpy.array(list_location)
        print(type(X))
        m=eqsc(X,K=3)
        print(type(X))
        return f"Your name is {m}"

    return f"Your name is {params}"
    
    
    # render_template("base.html", text ="Text",user="Hodaya",arr=params)

