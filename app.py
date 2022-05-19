from flask import Flask

from ext import db
from api.sku import sku as api_sku_blueprint
from api.category import category as api_category_blueprint
from api.user import user as api_user_blueprint
from api.department import department as api_department_blueprint
from api.post import post as api_post_blueprint
from api.role import role as api_role_blueprint
from api.datadict import datadict as api_datadict_blueprint
from api.language import language as api_language_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ly818379@localhost:3306/fbmtai"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(api_sku_blueprint)
app.register_blueprint(api_category_blueprint)
app.register_blueprint(api_user_blueprint)
app.register_blueprint(api_department_blueprint)
app.register_blueprint(api_post_blueprint)
app.register_blueprint(api_role_blueprint)
app.register_blueprint(api_datadict_blueprint)
app.register_blueprint(api_language_blueprint)

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
