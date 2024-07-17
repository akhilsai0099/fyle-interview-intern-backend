from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B

def test_grade_assignment (client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        headers=h_principal
        , json={
            "id": 3,
            "grade": GradeEnum.A.value
        }
    )

    assert response.status_code == 200
    
def test_list_teachers(client, h_principal):
    response = client.get('/principal/teachers', headers=h_principal)

    assert response.status_code == 200

    assert 'data' in response.json
    assert isinstance(response.json['data'], list)
    for teacher in response.json['data']:
        assert 'id' in teacher

# def test_list_teachers_non_principal(client, h_teacher):
#     response = client.get('/principal/teachers', headers=h_teacher)

#     assert response.status_code == 403
#     assert response.json['error'] == 'Forbidden'
