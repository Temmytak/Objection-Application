activate_this = 'C:/Objection-Application/env/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Objection-Application/env/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Objection-Application')
# sys.path.append('C:/Objection-Application/Objection-Application')

os.environ['DJANGO_SETTINGS_MODULE'] = 'objectionApp.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "objectionApp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()