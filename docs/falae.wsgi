# vim: syntax=python
import sys
# Na linha abaixo basta  informar o caminho completo para o arquivo bin/activate_this.py dentro da pasta do virtual env
activate_this = '/home/olimpiodev/apps_wsgi/falae/.venv/Scripts/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
sys.path.append('/home/olimpiodev/apps_wsgi/falae')
from run import app as application