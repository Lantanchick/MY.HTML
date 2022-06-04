from flask import Flask

app = Flask(__name__)

# with open("profile.html", "r") as file:
#    x = file

t = ''
with open("profile.html", "r", encoding='utf-8') as f:
    for i in f:
        t += i


@app.route("/")
def page_profile():
    return t


if __name__ == "__main__":
    app.run(debug=False)
