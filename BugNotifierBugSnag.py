from BugNotifier import BugNotifier
import bugsnag

class BugNotifierBugSnag(BugNotifier):
    def __init__(self,apikey):
        bugsnag.configure(
            api_key = apikey,
            project_root = "/path/to/your/app",
        )
    def notify(self,e):
        bugsnag.notify(e)
