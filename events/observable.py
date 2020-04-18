from .observers import Observer, MailAdminNotification, MailNotification, ConsolePrinter

class Observable:
    observers = []
    observers_states = []
    def register(self, observer):
        """ register an observer to the event
        @params = Observer object
        """
        self.observers.append(observer)
        pass
    def unregister(self, observer):
        """  delete an obsever that was registered
        @params = Observer object
        """
        if observer in self.observers:
            try:
                self.observers.remove(observer)
            except ValueError : 
                print(f'Error during unregistering of observer : {observer.name}')
        pass
    def unregister_all(self,*args):
        self.observers *= 0
        
    def register_all(self, *args):
        for observer in args:
            self.register(observer)
        pass
    def update_observers(self, *args, **kwargs):
        #we initialise again
        self.observers_states *= 0

        for observer in self.observers:
            observer.update(*args,**kwargs)
            self.observers_states.append(observer.state)
        pass
        

class EventHandler(Observable):
    """ Pipeline Manager for Observable object
    Directing all the observers to be updtated when an event is made
    """
    PIPELINES = [
        ('mail', MailNotification()),
        ('admin_mail', MailAdminNotification()),
        ('console',ConsolePrinter())
    ]
    gates = []
    def trigger(self, *args, **kwargs):
        """ Trigger the notification via somme ways writen in gates
        """ 
        self.update_observers(*args, **kwargs)

        print('counting trigeger call ' )
        pass

    def activate(self):
        """ creating ways to triggers by their names
            Adding to gates open piplines and after registering all observers
        """
        #cleaning registered observers
        self.observers *= 0 

        roads = self.via()
        names = list(map(lambda x:x[0], self.PIPELINES))
        for road_name in roads:
            if road_name in names:
                #adding the the gates the pipeline
                self.gates.append(self.PIPELINES[names.index(road_name)])
            pass

        for (pipeline_name, pipeline) in self.gates:
            self.register(pipeline)

    def via(self):
        """
        Adding a pipeline by name, the name must be in PIPELINES list
        eg: ['console',''mail']
        """

        return ['console']


            
       