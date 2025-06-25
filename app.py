from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to My Flask App</h1><p>Navigate to <a href='/hello'>/hello</a></p>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        return redirect(url_for('greet', username=name))
    return '''
        <form method="post">
            Enter your name: <input name="name">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/greet/<username>')
def greet(username):
    safe_name = username.replace("<", "").replace(">", "")
    return f"<h2>Hello, {safe_name}!</h2><a href='/'>Back home</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

