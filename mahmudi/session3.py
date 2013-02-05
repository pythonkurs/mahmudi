import os

class ContextManager(object):
    def __init__(self, path):
        self.path = path
        self.oldPath = None
    
    def __enter__(self):
        self.oldPath = os.getcwd()
        os.chdir(self.path)
    
    def __exit__(self, *_):
        os.chdir(self.oldPath)


class CourseRepo(object):
    
    def __init__(self, surname):
        self._surname = surname

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def required(self, surname):
        self._required = [".git","setup.py", "README.md","scripts/getting_data.py","scripts/check_repo.py", surname + "/__init__.py", surname + "/session3.py"]


    def check(self):
        for i in range(0,len(self.required)):
            if not os.path.exists(self.required[i]):
                return False
        return True