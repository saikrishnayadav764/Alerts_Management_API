from app import create_app

# Creating the Flask application using the create_app function from app module
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
