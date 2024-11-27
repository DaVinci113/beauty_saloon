from calendar import HTMLCalendar
from datetime import datetime


class Calendar(HTMLCalendar):
    
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month
        super(Calendar, self).__init__()
    