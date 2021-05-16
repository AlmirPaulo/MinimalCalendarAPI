from MinimalCalendarAPI import create_app, views, models, api 
from urllib.request import urlopen
import os, pytest, MinimalCalendarAPI, sqlite3


def test_app_is_created():
    assert create_app() != None

@pytest.mark.parametrize('modules', [MinimalCalendarAPI])
def test_debug_mode_in_logs(modules):
    #assert modules.logger.level != 10
    assert modules.logger.level == 10

def test_logfile_is_created():
    assert os.path.exists('server.log') == True

def test_database_is_created():
    assert os.path.exists('data.db') == True

#Bugged... Use .check_db.py script instead.
#@pytest.mark.parametrize('tables', [models.Todo, models.User])
#def test_check_db_tables(tables):
#    conn = sqlite3.connect('data.db')
#    c = conn.cursor()
#    c.execute(f'''SELECT * FROM {tables}''')
#    assert c.fetchall()

#Run the tests bellow whith the app running.
@pytest.mark.parametrize('routes', [])
def test_routes(routes):
    url = 'http://127.0.0.1:5000/'+routes
    response = urlopen(url)
    assert response.status == 200
    
