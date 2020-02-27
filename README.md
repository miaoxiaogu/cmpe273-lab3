# cmpe273-spring20

#Open this URL in a web browser or run this CLI to see the output.

http://localhost:5000/graphql

GraphQL operations to be implemented.
1. Mutate a new student

        mutation ($nm: String!) {
            mutateNewStudent(name: $nm) {
            name
          }
        }

    and input the following into the QUERY VARIABLES dialog

        {
          "nm": "Bob Smith"
        }


2. Quety an existing student.

        query {
          students(id:1238125) {
            name
          }
        }

3. Mutate a class.

        mutation ($name: String!) {
            mutateNewClass(name: $name) {
            name
          }
        }
    and input the following into the QUERY VARIABLES dialog
    
        {
          "name" : "CMPE-273"
        }
        

4. Query a class.

        query {
          classes(id:1238125) {
            name
            students
          }
        }
        

5. Add students to a class.

        mutation ($sid: Int!,$cid:Int!) {
            addStudentToClass(sid: $sid, cid: $cid) {
            name
            students {
              id
              name
            }
          }
        }
    and input the following into the QUERY VARIABLES dialog
    
        {
          "sid":1238125,
          "cid":1238125
        }
    
        
