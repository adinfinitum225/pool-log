from flask import(
        Blueprint, flash, g, redirect, render_template, request, session, url_for
        )

from pool_log.db import get_db


bp = Blueprint('log', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    logs = db.execute(
            'SELECT l.id, created, temperature, ph, chlorine, cya, pressure, clarity'
            ' FROM log l'
            ' ORDER BY created DESC'
            ).fetchall()
    return render_template('log/index.html', logs=logs)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # Get info from the form
        db = get_db()
        error = None
        # Add in errors

        if error is None:
            try:
                db.execute(""
                        # Insert log values into db
                        )
                db.commit()
            except db.IntegrityError:
                # Add in the error
                pass
            else:
                return redirect(url_for('index'))

            flash(error)

            return render_template('log/create.html')

