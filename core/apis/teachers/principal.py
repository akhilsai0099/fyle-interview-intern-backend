from core.models.teachers import Teacher 
from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse

from .schema import TeacherSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of Teachers"""
    teachers = Teacher.get_all_teachers()
    print(teachers)
    
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)
