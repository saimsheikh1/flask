from app import my_obj

from flask import render_template, flash, Flask, redirect, url_for, request


#my_obj = Flask (__name__)      running this line twice, first init
name  =  'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']
#city_names = list, city = string field 


@my_obj.route("/", methods=['GET', 'POST'])
def home():
    
    if (request.method=='POST'):
        flash(request.form["cityName"])
        return redirect(url_for('home'))
    return render_template("home.html", name = name, city_names= city_names)
    
if __name__ == "__main__":
    my_obj.run(debug=True)
    #app.run(port= 80)




