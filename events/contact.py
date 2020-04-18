from .observable import EventHandler
from .observers import MailNotification, MailAdminNotification

class ContactMadeEvent(EventHandler):
    MAIL = {}
    """ An Event, Contact made. that send via Mail message to the admin when a contact is made
        we can use other pipeline in the future
    """
    def __init__(self, name=False,email=False,budget=False,project_type=False,details=''):
        #activating all the observers of the event
        self.activate()

        #registering the mail
        self.MAIL = {
            'name': name,
            'budget' : budget,
            'project_type': project_type,
            'email' : email,
            'details' : details
        }

        #making the event
        self.trigger(**self.MAIL)
        
        pass
    def via(self):
        return ['mail','admin_mail' ,'console'] 



    