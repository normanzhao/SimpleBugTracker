import json
import os.path

if not os.path.exists('data.json'):
    open('data.json','w')
#read and write a JSON file as a list of dicts to store the issues/bugs 

class io():
    issues = {}
    current_key = 0

    def write(self):
        with open('data.json', 'w') as f:
            json.dump(self.issues, f)

    def show_all(self, order=True, status=None):
        print "ID\tPriority\tStatus\tDescription"
        keys = sorted(self.issues.keys(), reverse=order)
        if status != None:
            keys = [key for key in keys if self.issues[key]['status'] == status]
        for key in keys:
            print key,'\t', self.issues[key]['priority'],'\t\t', self.issues[key]['status'],'\t',self.issues[key]['description']

    def new(self, priority, description):
        self.current_key += 1
        self.issues[str(self.current_key)] = {'priority':priority, 'description':description,'status':'open'}
        self.write()

    def close(self, issue_id):
        self.issues[issue_id]['status'] = 'closed'
        self.write()

    def edit(self,issue_id, priority = "", description = ""):
        editted = self.issues[issue_id]
        editted['priority'] = priority if priority != "" else editted['priority']
        editted['description'] = description if description != "" else editted['description']
        self.issues[issue_id] = editted
        self.write()

    def append(self,issue_id,description=""):
        self.issues[issue_id]['description'] += description
        self.write() 

    def __init__(self):
        #open json file initially to read the data, if empty then pass and current_id is 0
        try:
            with open('data.json', 'r') as f:
                self.issues = json.load(f)
                self.current_key = int(max(self.issues.keys()))
        except:
            pass


