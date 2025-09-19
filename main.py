
from datetime import datetime
from flask import session, render_template, redirect, url_for
from app import app


@app.route('/')
def home():

    if 'username' not in session:
        return redirect(url_for('login'))

    role = session.get('role')


    announcements = []
    current_year = datetime.now().year


    template = 'admin_home.html' if role == 'admin' else 'index.html'
    return render_template(template, announcements=announcements, current_year=current_year)




@app.route("/faq")
def faq():
    return render_template("faq.html")


if __name__ == '__main__':
    app.run(debug=True)
