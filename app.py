from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/profile_creation_request', methods=['GET', 'POST'])
def profile_creation_request():
    if request.method == 'POST':
        # Traiter la demande de création de profil
        return redirect(url_for('dashboard'))
    return render_template('profile_creation_request.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/work_orders')
def work_orders():
    return render_template('work_orders.html')

@app.route('/work_order/<int:order_id>', methods=['GET', 'POST'])
def work_order(order_id):
    if request.method == 'POST':
        # Traiter la réalisation de l'ordre de travail
        return redirect(url_for('work_orders'))
    return render_template('work_order.html', order_id=order_id)

@app.route('/subcontracting', methods=['GET', 'POST'])
def subcontracting():
    if request.method == 'POST':
        # Traiter la sous-traitance
        return redirect(url_for('work_order', order_id=request.form['order_id']))
    return render_template('subcontracting.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
