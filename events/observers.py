from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Observer:
    state = []
    def __init__(self,name:str):
        """ Creating an observer with a name

        """
        self.name = name
        self.state= [name,'ready']
        self.work_done = False
        pass
    
    def update(self,*args, **kwargs):
        print(args)
        print(kwargs)
        pass

class ConsolePrinter(Observer):
    """ An observer to Print any argument notifiyed
    
    """
    def __init__(self):
        self.name = 'Console_printer'
        self.state= [self.name,'ready']
        self.work_done = False
        pass

    def update(self,*args, **kwargs):
        self.state[1] = 'listening'
        print('=============Console==============')
        if len(args) > 0 :
            print(args)
        for key, value in kwargs.items():
            print(f'{key} : {value}')
        self.work_done = True

        return self.work_done
        
class MailAdminNotification(Observer):
    """ An observer to Send Mail to the Admin
    
    """
    ADMIN_NAME = 'Josias Kasongo'
    ADMIN_MAIL = 'admin@test.com'
    PLATFORM_MAIL = 'system@josiaskasongo.com'

    def __init__(self):
        self.name = 'Admin_mailler'
        self.state= [self.name,'ready']
        self.work_done = False
        pass

    def update(self, *args, name=False, budget=False, project_type= False, **kwargs):
        
        #initialisation of the observer work
        self.state[1] = 'listening'

        #can't send empty messages to people
        verifyed = True
        if False in [name, budget, project_type]:
            verifyed = False

        if verifyed:
            html = self.buildHtml(name, budget, project_type)
            self.send(self.ADMIN_MAIL, html)
        else :
            print('can\'t send the Admin mail')

        return self.work_done

    def buildHtml(self,name, budget, project_type):
        context ={
           'name' : name,
           'project_type' : project_type,
           'budget':budget
        }
        html_message = render_to_string('ThanksMail.html',context)
        plain_message = strip_tags(html_message)
        return (html_message, plain_message)

    def send(self,to,html):
        subject = 'Mail from Portfolio web app' 
        from_email = self.PLATFORM_MAIL 
        to = to 
        send_mail(subject, html[1], from_email, [to], html_message=html[0])
        
        self.work_done = True
        pass

class MailNotification(Observer):
    INFO_MAIL = 'info@josiaskasongo.com'
    def __init__(self):
        self.name = 'mailler'
        self.state= [self.name,'ready']
        self.work_done = False
        pass

    def update(self, *args, name=False, budget=False, project_type= False, email=False, **kwargs):
        """ Sending Mail to aknowledge that we receive the message
        name (str) : name of the client
        budget (int) : amount for the project
        project_type (str) : eg 'Web App'
        email (str)
        """
        #initialisation of the observer work
        self.state[1] = 'listening'

        #can't send empty messages to people
        verifyed = True
        if False in [name, budget, project_type, email]:
            verifyed = False

        if verifyed:
            html = self.buildHtml(name, budget, project_type)
            self.send(email, html)
        else :
            print('can\'t send the mail')
            
        return self.work_done

    def buildHtml(self, name, budget, project_type):
        context ={
           'name' : name,
           'project_type' : project_type,
           'budget':budget
        }
        html_message = render_to_string('ThanksMail.html',context)
        plain_message = strip_tags(html_message)
        return (html_message,plain_message)

    def send(self, to, html):
        subject = 'Thank you for contacting us' 
        from_email = self.INFO_MAIL 
        to = to 
        send_mail(subject, html[1], from_email, [to], html_message=html[0]) 
        self.work_done = True
        pass
    
class DataBaseNotification(Observer):
    def __init__(self):
        self.name = 'Database notification'
        self.state= [self.name,'ready']
        self.work_done = False
        pass
    
    def update(self, *args, notifiyer=False, event=False, users= False, **kwargs):
        self.state[1] = 'listening'

        #can't send empty messages to people
        verifyed = True

        if False in [notifiyer, event, users]:
            verifyed = False

        if verifyed:
            self.write_data(notifiyer, event, users)

        return self.work_done

    def write_data(self, notifiyer, event, users):

        self.work_done = True
        pass