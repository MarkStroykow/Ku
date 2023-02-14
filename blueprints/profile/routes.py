from flask import Blueprint, render_template, request, session
from sql_provider import SQLProvider
from database import work_with_db
from blueprints.authorization.access import login_required
import json


db_config = json.load(open('configs/config.json'))
profile_app = Blueprint('profile', __name__, template_folder='templates')
provider = SQLProvider('blueprints/profile/sql/')


@profile_app.route('/')
@login_required
def index():
    return render_template('profile-index.html')


@profile_app.route('/prov1', methods=['GET', 'POST'])
@login_required
def get_sql1():
    if request.method == 'GET':
        sql = provider.get('selectpat.sql')
        result = work_with_db(config=db_config, sql=sql)
        return render_template('prov1.html', items=result)
    else:
        name_patient = request.form.get('name_patient', None)
        if name_patient is not None:
            sql = provider.get('task1.sql', name_patient=name_patient)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output1.html', str=result)


@profile_app.route('/prov2', methods=['GET', 'POST'])
@login_required
def get_sql2():
    if request.method == 'GET':
        sql = provider.get('selectspec.sql')
        result = work_with_db(config=db_config, sql=sql)
        return render_template('prov2.html', items=result)
    else:
        spec = request.form.get('spec', None)
        if spec is not None:
            sql = provider.get('task2.sql', spec=spec)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output2.html', str=result)


@profile_app.route('/prov3', methods=['GET', 'POST'])
@login_required
def get_sql3():
    if request.method == 'GET':
        sql = provider.get('selectdoc.sql')
        result = work_with_db(config=db_config, sql=sql)
        return render_template('prov3.html', items=result)
    else:
        name_doc = request.form.get('name_doc', None)
        if name_doc is not None:
            sql = provider.get('task3.sql', name_doc=name_doc)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output3.html', str=result)


