from tornado.ncss import Server, ncssbook_log
from tornado import template
import methods

loader = template.Loader('templates')

def index_handler(request):
    with open('index.html') as file:
        request.write(file.read())

def recipient_handler(request, year_level, id):
    year_level = int(year_level)
    id = int(id)
    recipients = methods.find_recipients_by_year(year_level)
#    print(id, year_level, recipients)
    student = methods.get_student(id)
    loader.reset()
    response = loader.load('recipients.html').generate(year_level=year_level, id=id, recipients = recipients, student = student)
    request.write(response)
    
def invalid_url_handler(request):
    with open('static/404.html') as file:
        request.write(file.read())
 
server = Server()
server.register(r'/', index_handler)
server.register(r'/year/(\d*)/student/(\d*)', recipient_handler)
server.register(r'.+', invalid_url_handler)
server.run()

