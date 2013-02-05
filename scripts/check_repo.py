import sys, os
from mahmudi.session3 import CourseRepo, ContextManager

if len(sys.argv) != 2:
    print "Error: Insufficient arguments!\nExpecting:\n check_repo <path>"
    sys.exit()

if not os.path.exists(sys.argv[1]):
    print "Error: Invalid path!"
    sys.exit()

thepath = sys.argv[1]
surname = os.path.basename(thepath)

with ContextManager(thepath):
    obj = CourseRepo(surname)
    if obj.check():
        print "PASS"
    else:
        print "FAIL"