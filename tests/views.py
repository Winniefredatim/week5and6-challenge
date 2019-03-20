from flask import Blueprint

from mydiary.diary_api import DiaryApi

index = Blueprint('index_view', __name__)

diary_app = Blueprint('diary_app', __name__)

diary_views = DiaryApi.as_view('Mydiary')

@index.route('/diary/api/v1/Mydiary/', methods=['GET',])
def index():
    return "Welcome"

@index.route('/diary/api/v1/Mydiary/hello')
def api_works():
    return "Enjoy reading"

diary_app.add_url_rule('/diary/api/v1/mydiary/', defaults={'diary_page_id': None},
                     view_func=diary_templates, methods=['GET',])
diary_app.add_url_rule('/diary/api/v1/mydiary/', view_func=diary_templates, methods=['POST',])
diary_app.add_url_rule('/diary/api/v1/mydiary/<int:diary_page_id>', view_func=diary_templates,
                     methods=['GET', 'PUT', 'DELETE',])