from core.models.teachers import Teacher 
from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from .schema import TeacherSchema

teachers_resources = Blueprint('teachers_resources', __name__)


@teachers_resources.route('/principal/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of Teachers"""
    teachers = Teacher.get_all_teachers()
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)