from flask import Flask, render_template
from abc import ABC, abstractmethod
# classes
class External_Vendors(ABC):
    
    @abstractmethod
    def menu(self):
        pass

class Cooperative_Vendor(External_Vendors):
    def menu(self):
        menu = "week_12/menus/coporative.PNG"
        return menu

class Faith_Vendor(External_Vendors):
    def menu(self):
        menu = "week_12/menus/faith.PNG"
        return menu

class StudentCentre_Vendor(External_Vendors):
    def menu(self):
        menu = "week_12/menus/std_centre.PNG"
        return menu

coop = Cooperative_Vendor()
faith = Faith_Vendor()
std_centre = StudentCentre_Vendor()

coop_menu = coop.menu()
faith_menu = faith.menu()
std_menu = std_centre()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/coop')
def menu1():
    image_url = url_for('static', filename='images/menu1.jpg')
    return render_template('menu.html', image_url=image_url, menu_name="Menu 1")

@app.route('/faith')
def menu2():
    image_url = url_for('static', filename='images/menu2.jpg')
    return render_template('menu.html', image_url=image_url, menu_name="Menu 2")

@app.route('/std_centre')
def menu3():
    image_url = url_for('static', filename='images/menu3.jpg')
    return render_template('menu.html', image_url=image_url, menu_name="Menu 3")


if __name__ == '__main__':
    app.run(debug=True)