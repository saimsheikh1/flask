from flask import Flask

my_obj = Flask (__name__)
name  = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']
@my_obj.route("/")
def home():

    return '''
    <html>
    <body>
        <h1>
        Welcome '''+ name + ''' </h1>
        <div>
            <a href ="www.google.com">notgoogle</a>
        </div>
        <ul>
            <li> '''+city_names[0]+''' </li>
            <li> '''+city_names[1]+''' </li>
            <li> '''+city_names[2]+''' </li>
            <li> '''+city_names[3]+''' </li>
        </ul>
    </body>
    </html>
    '''
# my_obj.run()
