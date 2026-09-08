from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)

# Clave secreta para proteger los formularios
app.config['SECRET_KEY'] = 'mi_clave_secreta_123'


# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Página de contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        flash(f'Mensaje enviado por {form.name.data}!', 'success')
        return redirect(url_for('index'))

    return render_template('contact.html', form=form)


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)