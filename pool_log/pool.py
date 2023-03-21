from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
        )

from pool_log.db import get_db

bp = Blueprint('pool', __name__, url_prefix='/pools')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        volume = request.form['volume']
        db = get_db()
        error = None

        if not name:
            error = "Pool name required"
        elif not volume:
            error = "Pool volume required"

        if error is None:
            try:
                db.execute(
                        "INSERT INTO pool (name, volume) VALUES (?, ?)", 
                        (name, volume),
                        )
                db.commit()
            except db.IntegrityError:
                error = f"There is already a pool named {name}"
            else:
                return redirect(url_for('index'))

        flash(error)

    return render_template("pools/create.html")

"""
@bp.before_app_request
def pool_selected():
    pool_id = session.get('pool_id')

    if pool_id is None:
        g.pool = None
    else:
        g.pool = get_db().execute(
                'SELECT * FROM pool WHERE id = ?', (pool_id)
                ).fetchone()
"""

@bp.route('/select', methods=('GET', 'POST'))
def select():
    db = get_db()
    pools = db.execute(
            'SELECT id, name, volume FROM pool'
            ).fetchall()

    if request.method == 'POST':
        session.clear()
        session['pool_id'] = request.form['pool']
        return redirect(url_for('index'))

        
    return render_template('pools/select.html', pools=pools)
