from flask import Flask, escape, request, jsonify
from ariadne import gql, make_executable_schema, QueryType, graphql_sync, MutationType
from ariadne.constants import PLAYGROUND_HTML


type_defs = gql("""
    type Student {
        id: Int
        name: String
    }

    type Class{
        id: Int
        name: String
        students: [Student]
    }

    type Query{
        students(id: Int): Student
        classes(id: Int): Class
    }

    type Mutation{
        mutateNewStudent(name: String): Student
        mutateNewClass(name: String): Class
        addStudentToClass(sid: Int, cid: Int): Class
    }
""")

query = QueryType()
mutation = MutationType()

DB = {"students":[],
    "classes":[]
}

SID = 1238125
CID = 1238125



#Mutate a new student
@mutation.field("mutateNewStudent")
def resolve_mutateNewStudent(_, info, name):
    global SID
    Student = {
        'id' : SID,
        'name' : name
    }
    SID = SID + 1
    DB["students"].append(Student)
    return Student

#Mutate a new class
@mutation.field("mutateNewClass")
def resolve_mutateNewClass(_, info, name):
    global CID
    Class = {
        "id" : CID,
        "name" : name,
        "students" : []
    }
    CID = CID + 1
    DB["classes"].append(Class)
    return Class


#Quety an existing student
@query.field("students")
def resolve_Student(_, info, id):
    for Student in DB["students"]:
        if Student['id'] == id:
            return Student

#Quety an existing class
@query.field("classes")
def resolve_Class(_, info, id):
    for Class in DB["classes"]:
        if Class['id'] == id:
            return Class

#Add students to a class
@mutation.field("addStudentToClass")
def resolve_mutateNewStudent(_, info,sid,cid):
    for Student in DB["students"]:
        if Student['id'] == id:
            break
    for Class in DB["classes"]:
        if Class['id'] == cid:
            studentBefore = Class['students']
            studentBefore.append(Student)
    return Class



schema = make_executable_schema(type_defs, [query, mutation])

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    infomation = request.get_json()
    success, result = graphql_sync(
        schema,
        infomation,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/printall', methods = ['GET'])
def getAll():
    return DB
