import os

from flask import Blueprint, request, render_template, session, current_app
from werkzeug.utils import redirect

from database import work_with_db, make_update
from sql_provider import SQLProvider

from blueprints.authorization.access import login_required


record_app = Blueprint('record', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))







@record_app.route('/', methods=['POST', 'GET'])
@login_required
def record_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        sql = provider.get('listpat.sql')
        result = work_with_db(config=db_config, sql=sql)
        return render_template('insert_recording.html', items=result)
    else:
        invdate = request.form.get('invdate', None)
        session['invdate'] = invdate
        name_patient = request.form.get('name_patient', None)
        session['name_patient'] = name_patient

        return redirect('docc')


@record_app.route('/docc', methods=['POST', 'GET'])
def docc():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        sql = provider.get('listdoc.sql')
        make_update(config=db_config, sql=sql)

        invdate = session['invdate']
        name_patient = session['name_patient']

        sql = provider.get('insert_record.sql', invdate=invdate, name_patient=name_patient)
        make_update(config=db_config, sql=sql)

        return redirect('/')
