from flask import Blueprint , render_template , request , redirect , url_for , flash
from models.contact import Contact
from utils.db import db


contacts = Blueprint('contacts', __name__)

#aqui se muestra el formulario de registro
@contacts.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('index.html' , contacts=contacts)

#guardar contacto
@contacts.route('/new' , methods=['POST'])
def new():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    contact = Contact(fullname, email, phone) 

    db.session.add(contact)
    db.session.commit()
    db.session.close()

    flash('contact added succesfully')
    return redirect(url_for('contacts.home'),302)
   

#actualiaz contacto
@contacts.route('/update/<id>' , methods=['GET', 'POST'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone'] 

        db.session.commit()
        db.session.close()

        return redirect(url_for('contacts.home'), 302)
    flash('contact updated succesfully')
    return render_template('update.html', contact=contact)

#borrar contacto
@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()    
    db.session.close()
    
    flash('contact deleted succesfully')
    return redirect(url_for('contacts.home'),302)


@contacts.route('/about')
def about():
    return render_template('about.html')