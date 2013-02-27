import sys, os
from mahmudi.session3 import CourseRepo, ContextManager

@profile

def main():
    if len(sys.argv) != 2:
        if sys.argv[1].find('check_repo.py') == -1:
    	    print "Error: Insufficient arguments!\nExpecting:\n check_repo <path>"
    	    sys.exit()

    if not os.path.exists(sys.argv[1]):
        if sys.argv[1].find('check_repo.py') == -1:
    	    print "Error: Invalid path!"
    	    sys.exit()

    if sys.argv[1].find('check_repo.py') != -1:
        thepath = sys.argv[2]
    else:
        thepath = sys.argv[1]
    surname = os.path.basename(thepath)

    with ContextManager(thepath):
        obj = CourseRepo(surname)
        if obj.check():
            print "PASS"
        else:
            print "FAIL"


if __name__ == "__main__":
    main()
