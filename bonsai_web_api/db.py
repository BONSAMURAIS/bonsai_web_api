import csv, sqlite3

import click

# g is a special object that is unique for each request.
# It is used to store data that might be accessed by multiple functions during the request. 
from flask import current_app, g
from flask.cli import with_appcontext

# get_db will be called when the application has been created and is handling a request, so current_app can be used.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row tells the connection to return rows that behave like dicts.
        # This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    # open_resource() opens a file relative to the bonsai_web_api package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    with current_app.open_resource('exiobase_activity_URIs.csv','r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['uri'], i['name'], i['activity_code_1'], i['activity_code_2'], i['introduction'], i['entityType'], i['graphdbName'], i['dataSpace'], i['abstractField'], i['creationDate'], i[	'sameAs'], i['industry'], i['outputOf'], i['inputOf'], i['productionVolume'], i['productionVolumeUnit'], i['pedigreeMatrix'], i['imageUrl']) for i in dr]
       
    db.executemany('INSERT INTO product ("uri","name", "activity_code_1","activity_code_2","introduction","entityType","graphdbName","dataSpace",	"abstractField","creationDate","sameAs","industry","outputOf","inputOf","productionVolume","productionVolumeUnit","pedigreeMatrix","imageUrl") VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', to_db)
    
    with current_app.open_resource('bw2_methods.csv','r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['name_method'], i['name_impact'], i['unit']) for i in dr]
       
    db.executemany('INSERT INTO method ("name_method","name_impact", "unit") VALUES ( ?, ?, ?)', to_db)
    
    db.commit()
    


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    # click.command() defines a command line command called init-db that calls the init_db function and shows a success message to the user. 
    click.echo('Initialized the database.')
    
def init_app(app):
    # app.teardown_appcontext() tells Flask to call that function when cleaning up after returning the response.
    app.teardown_appcontext(close_db)
    # app.cli.add_command() adds a new command that can be called with the flask command.
    app.cli.add_command(init_db_command)