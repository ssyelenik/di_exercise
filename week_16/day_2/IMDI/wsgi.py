from film_project import create_app, models, db, forms
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

app=create_app()


@app.shell_context_processor
def shell_context():
    return {
        'models':models,
        'db':db,
        'forms': forms,
    }

if __name__=="__main__":
    app.run(debug=True)
