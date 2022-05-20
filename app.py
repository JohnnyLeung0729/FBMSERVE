from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions

from ext import db
from api.sku import sku as api_sku_blueprint
from api.category import category as api_category_blueprint
from api.user import user as api_user_blueprint
from api.department import department as api_department_blueprint
from api.post import post as api_post_blueprint
from api.role import role as api_role_blueprint
from api.datadict import datadict as api_datadict_blueprint
from api.language import language as api_language_blueprint
from api.pbox import pbox as api_pbox_blueprint
from api.pboxtype import pboxtype as api_pboxtype_blueprint
from api.consumable import consumable as api_consumable_blueprint
from api.cuslevel import cuslevel as api_cuslevel_blueprint
from api.regional import regional as api_regional_blueprint
from api.roleexcl import roleexcl as api_roleexcl_blueprint


def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {"code": error.code, "description": error.description, "message": str(error)}
        else:
            description = abort.mapping[500].description
            result = {"code": 500, "description": description, "message": str(error)}

        resp = jsonify(result)
        resp.status_code = result["code"]
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    return app


app = Flask(__name__)
app = JsonApp(app)
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
app.register_blueprint(api_pbox_blueprint)
app.register_blueprint(api_pboxtype_blueprint)
app.register_blueprint(api_consumable_blueprint)
app.register_blueprint(api_cuslevel_blueprint)
app.register_blueprint(api_regional_blueprint)
app.register_blueprint(api_roleexcl_blueprint)

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api')
def api_start():
    return 'Hello TonchenTAI World!S'


if __name__ == '__main__':
    app.run()
