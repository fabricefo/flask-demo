from website import create_app

/*
IMPORTANT : note that the version of Werkzeug must be < 3.0.0
For this project, we use the 2.2.0 version - see requirements.txt file
*/

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
