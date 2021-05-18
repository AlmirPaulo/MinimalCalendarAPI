from MinimalCalendarAPI import create_app, views, models, api 
from urllib.request import urlopen
import os, pytest, MinimalCalendarAPI


def test_app_is_created():
    assert create_app() != None

@pytest.mark.parametrize('modules', [MinimalCalendarAPI])
def test_debug_mode_in_logs(modules):
    #assert modules.logger.level != 10
    assert modules.logger.level == 10

def test_logfile_is_created():
    assert os.path.exists('server.log') == True

def test_database_is_created():
    assert os.path.exists('MinimalCalendarAPI/data.db') == True

#Should show User and Todo tables.
@pytest.mark.parametrize('tables', [models.Todo, models.User])
def test_check_db_tables(tables):
    assert tables 


#Run the tests bellow whith the app running.
#@pytest.mark.parametrize('routes', [])
#def test_routes(routes):
#    url = 'http://127.0.0.1:5000/'+routes
#    response = urlopen(url)
#    assert response.status == 200
    
#def test_new_user():
#   ...
    
#def test_user_authentication():
#    ...
#
#def test_read_tasks():
#    ...
#
#def test_update_tasks():
#    ...
#
#def test_delete_task():
#    ...
