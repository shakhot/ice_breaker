from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from ice_breaker import ice_break


app = Flask(__name__)

#The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break(
        name=name
    )
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "ice_breakers": ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    #The run() method of Flask class runs the application on the local development server.
    app.run(host="0.0.0.0", debug=True)