from django.test import TestCase
from .observable import Observable, EventHandler
from .observers import ConsolePrinter, MailAdminNotification, MailNotification
from .contact import ContactMadeEvent
# Create your tests here.

class ListeningTestCase(TestCase):
    """ Testing if observers can listen and observable can make them works
    """
    def setUp(self):
        pass

    def test_console_ready_to_listen(self):
        consoleEcouteur = ConsolePrinter()
        self.assertEqual(consoleEcouteur.state[1],'ready')

    def test_admin_mail_ready_to_listen(self):
        mailEcouteur = MailAdminNotification()
        self.assertEqual(mailEcouteur.state[1],'ready')

    def test_mail_ready_to_listen(self):
        mailEcouteur = MailNotification()
        self.assertEqual(mailEcouteur.state[1],'ready')    

    def test_console_can_listen(self):
        bruit = Observable()
        consoleEcouteur = ConsolePrinter()
        bruit.register(consoleEcouteur)
        bruit.update_observers(message='testing console listening')
        state = bruit.observers_states
        self.assertEqual(state[0][1],'listening')

        pass
    def test_admin_mail_can_listen(self):
        bruit = Observable()
        MailEcouteur = MailAdminNotification()
        bruit.register(MailEcouteur)
        mail ={
            'name': 'Admin tesing system',
            'budget' : 300,
            'project_type': 'Testing if admin can listen',
        }
        bruit.update_observers(**mail)
        state = bruit.observers_states
        self.assertEqual(state[0][1],'listening')
        pass

    def test_mail_can_listen(self):
        bruit = Observable()
        MailEcouteur = MailNotification()
        bruit.register(MailEcouteur)
        mail ={
            'name': 'Admin testing system',
            'budget' : 300,
            'project_type': 'Testing if mail can listen',
            'email' : 'test@info.com'
        }
        bruit.update_observers(**mail)
        state = bruit.observers_states
        self.assertEqual(state[0][1],'listening')
        pass


class SendingMailTestCase(TestCase):
    """ Testing if mail system works via observers
    """
    def test_admin_mail(self):
        bruit = Observable()
        MailEcouteur = MailAdminNotification()
        bruit.register(MailEcouteur)
        mail ={
            'name': 'Admin tesing system',
            'budget' : 300,
            'project_type': 'Testing admin mail sending',
        }
        bruit.update_observers(**mail)
        state = bruit.observers_states
        self.assertEqual(state[0][1],'listening')
        self.assertEqual(MailEcouteur.work_done,True)
        pass

    def test_mail(self):
        bruit = Observable()
        MailEcouteur = MailNotification()
        bruit.register(MailEcouteur)
        mail ={
            'name': 'Admin tesing system',
            'budget' : 300,
            'project_type': 'Testing mail sending',
            'email':'test@info.com'
        }
        bruit.update_observers(**mail)
        state = bruit.observers_states
        self.assertEqual(state[0][1],'listening')
        self.assertEqual(MailEcouteur.work_done,True)
        pass

class TestEventHandler(TestCase):

    def test_trigger_stystem(self):
        evenement = EventHandler()
        mail ={
            'name': 'Admin testing system',
            'budget' : 300,
            'project_type': 'Testing Event Handler',
            'email':'test@info.com'
        }
        evenement.trigger(**mail)
        state = evenement.observers_states
        self.assertEqual(state[0][1],'listening')

    def test_contact_made_event(self):
        mail ={
            'name': 'Admin testing system',
            'budget' : 300,
            'project_type': 'Testing ContactMade Event',
            'email':'test@info.com'
        }
        evenement = ContactMadeEvent()
        evenement.trigger(**mail)
        state = evenement.observers_states
        self.assertEqual(state[0][1],'listening') #mail
        self.assertEqual(state[1][1],'listening') #adminmail

        