import os

from flask import Blueprint, request, render_template, session, current_app
from werkzeug.utils import redirect

from database import work_with_db, make_update
from sql_provider import SQLProvider

from blueprints.authorization.access import login_required


edit_app = Blueprint('edit', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@edit_app.route('/', methods=['POST', 'GET'])
@login_required
def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('p1ras.html')
    else:
        action = request.form.get('action')
        if action == 'Понедельник':
            week = 1
            session['week'] = week
            return redirect('cdoc')
        if action == 'Вторник':
            week = 2
            session['week'] = week
            return redirect('cdoc')
        if action == 'Среда':
            week = 3
            session['week'] = week
            return redirect('cdoc')
        if action == 'Четверг':
            week = 4
            session['week'] = week
            return redirect('cdoc')
        if action == 'Пятница':
            week = 5
            session['week'] = week
            return redirect('cdoc')
        if action == 'Суббота':
            week = 6
            session['week'] = week
            return redirect('cdoc')
        if action == 'Воскресенье':
            week = 7

            session['week'] = week
            return redirect('cdoc')

        delete = request.form.get('delete')
        if delete == 'Удалить':
            inv = request.form.get('inv', None)
            sql = provider.get('delete_edit.sql', inv=inv)
            make_update(config=db_config, sql=sql)
            return redirect('/')






@edit_app.route('/cdoc', methods=['POST', 'GET'])
def cdoc():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        week = session['week']
        sql = provider.get('edit_list.sql', week=week)
        result = work_with_db(config=db_config, sql=sql)
        return render_template('edit.html', items=result)
    else:
        name_doc = request.form.get('name_doc', None)
        if name_doc is not None:
            session['name_doc'] = name_doc
            return redirect('edit_order')




@edit_app.route('/edit_order', methods=['POST', 'GET'])
def edit_order():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        name_doc = session['name_doc']
        sql = provider.get('finlist.sql', name_doc=name_doc)
        result = work_with_db(db_config, sql)
        return render_template('finlist.html', items=result)
    else:
        action = request.form.get('action')
        if action == 'Записать':
            zak_id = request.form.get('zak_id', None)
            session['zak_id'] = zak_id
            return redirect('lastt')


@edit_app.route('/lastt', methods=['POST', 'GET'])
def lastt():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        zak_id = session['zak_id']
        sql = provider.get('get_info_orders.sql', zak_id = zak_id)
        item = work_with_db(config=db_config, sql=sql)
        return render_template('edit_order.html', item=item[0])
    else:
        jalobi = request.form.get('jalobi')
        diagnoz = request.form.get('diagnoz')
        naznach = request.form.get('naznach')
        inv = request.form.get('inv')
        zak_id = session['zak_id']
        sql = provider.get('edit_order.sql', jalobi=jalobi, diagnoz=diagnoz, inv=inv, naznach=naznach, zak_id=zak_id)
        make_update(config=db_config, sql=sql)

        return redirect('edit_order')

