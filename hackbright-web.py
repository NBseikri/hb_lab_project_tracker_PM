from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)


    # grades is a list of tuples where each item is a pair of strings.
    # grades[0] = project title, and grades[1] = project grade

    print grades, type(grades)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades
                           )
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("student_added.html",
                           github=github)

@app.route("/project")
def project_info():
    """Display project information."""

    title = request.args.get('title')
    title, description, max_grade= hackbright.get_project_by_title(title)

    # print title, description, max_grade

    grades = hackbright.get_grades_by_title(title)

    return render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade,
                           grades=grades
                           )


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)







# @app.route("/student-search")
# def get_student_form(github=None):
#     """Show form for searching for a student."""

#     return render_template("student_search.html", 
#                             github=github)


# @app.route("/student-add", methods=['POST'])
# def student_add():
#     """Add a student."""

#     github = request.form.get('github')

#     get_student_form(github)

#     # render_template("student_added.html",
#                            # github=github)