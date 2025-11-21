from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# In-memory database
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)


def add(a: int, b: int):
    return a + b

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

def create_app():
    return app

def useless_function_1():
     return ""

def feature_1()
    # feature 1 version 1
    return "result_feature_1"

if __name__ == '__main__':
    app.run(debug=True)
