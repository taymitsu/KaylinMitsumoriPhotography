from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_index():
    """Landing Page"""
    return render_template('landing.html', msg='Kayshootz landing page')

if __name__ == '__main__':
    app.run(debug=True)