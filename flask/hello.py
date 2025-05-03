from flask import Flask

app = Flask(__name__)

# -------------------------- Routing
@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'> Hello World! </h1>" \
        "<p> This is a paragraph.</p>" #--- Rendering HTML Elements

@app.route('/bye')
def bye():
    return "Bye!!!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!!!"

@app.route("/<name>")
def greetn(name):
    return f"Hello {name + '12'}!!!"

# Converter types: string, int, float, path, uuid
@app.route("/username/<path:name>")
def greetv(name):
    return f"Hello {name}!!!"

@app.route("/username/<name>/<int:number>") 
def greetvi(name, number):
    return f"Hello {name}, you are {number}!!!"
# -------------------------- Routing

# -------------------------- Decorators to Style HTML Tags
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')
@make_bold #
@make_underlined #
def bye():
    return "Bye!!!"
# -------------------------- Decorators to Style HTML

# -------------------------- Special Attributes
if __name__ == "__main__":
    app.run(debug=False)
# -------------------------- Special Attributes

