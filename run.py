#set FLASK_DEBUG=1
#set FLASK_APP = "flaskblog.py"
#python flaskblog.py






from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)