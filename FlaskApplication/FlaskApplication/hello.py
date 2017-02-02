from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Port %d' %post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
