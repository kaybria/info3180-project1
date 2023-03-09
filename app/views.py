"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort,send_from_directory
from app import db
from app.forms import PropertyForm
from app.models import Property 
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create",methods =['GET','POST'])
def add_property():
    propform = PropertyForm()

    if request.method  == 'POST':
        if propform.validate_on_submit():
            title = propform.title.data
            description = propform.description.data
            rooms = propform.rooms.data
            bathrooms = propform.bathrooms.data
            price = propform.price.data
            ptype = propform.ptype.data
            location = propform.location.data
            photo = propform.photo.data
            pname=secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],pname))

            newprop = Property(title,description,rooms,bathrooms,price,ptype,location,pname)
            db.session.add(newprop)
            db.session.commit()

            flash('Property Added!','success')
            return redirect(url_for('view_properties'))
    else:
        flash_errors(propform)
    return render_template('create.html',form = propform)

@app.route('/properties')
def view_properties():
    properties = Property.query.all()
    return render_template('properties.html',properties=properties)

@app.route('/uploads/<filename>')
def getimages(filename):
    #rootdir = os.getcwd()
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)
@app.route('/property/<propertyid>')
def speceficproperty(propertyid):
    propertyid = int(propertyid)

    prop = Property.query.filter_by(id=propertyid).first()
    return render_template('speceficproperty.html',property=prop)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
