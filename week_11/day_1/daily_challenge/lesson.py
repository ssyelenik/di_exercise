import flask
import markdown
 
lesson = flask.Flask(__name__)

@lesson.route('/lesson1')
def index():
    with open("in_this_chapter.md","r") as text1:
        chapter_text=markdown.markdown(text1.read(),extensions=["fenced_code"])
        print(chapter_text)

    with open("exercises.md","r") as text2:
        exercise_text=markdown.markdown(text2.read(),extensions=["fenced_code"])

    with open("templates/home.bin/index.html","r") as webpage:
        html=webpage.read()

    html=html.replace("{{chapter_text}}",chapter_text)
    html=html.replace("{{exercise_text}}",exercise_text)
    

    with open("templates/home.bin/index_done.html","w") as webpage:
        webpage.write(html)
    
    html_done= flask.render_template('home.bin/index_done.html')
    return html_done

lesson.run()


