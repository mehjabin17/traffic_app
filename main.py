from application import create_app
from application.auth import create_admin_user

app = create_app()
app.app_context().push()
create_admin_user()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
