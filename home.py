from flask import Flask

my_obj = Flask (__name__)
@my_obj.route("/")
def home():
    name  = {'username': 'Lisa'}
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    return '''
    <html>
    <body>
        <h1>
        Welcome '''+ name['username'] + ''' </h1>
        <div>
            <a href ="https://www.google.com">not google</a>
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
