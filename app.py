from flask import Flask,render_template,request
import requests

api_url = "https://api.github.com/users/"

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method=="POST":
        github_username = request.form.get("githubname")
        api_user = api_url + github_username
        user_response = requests.get(api_user)
        repos_response = requests.get(api_user+"/repos")
        json_user_data= user_response.json()
        json_repos_data = repos_response.json()
        #app.logger.info(json_user_data)

        if "message" in json_user_data:
            return render_template("index.html",error ="User not found")
        else:
            return render_template("index.html",user_data=json_user_data,repos_data = json_repos_data)
    else:
        return render_template("index.html")


if __name__ =="__main__":
    app.run(debug=True)