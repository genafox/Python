import sys
from DbConnectionSettings import *
from DbContext import *

def main():

    connSettings = DbConnectionSettings().getDict();

    createCourseTemplate = """
        INSERT INTO course (name, price)
        VALUES (%s, %s)
        RETURNING id"""

    with DbContext(connSettings) as context:
        # seed
        course1Id = context.executeScalar(createCourseTemplate, "Course-1", 10.99);
        course2Id = context.executeScalar(createCourseTemplate, "Course-2", 0.99);
        course3Id = context.executeScalar(createCourseTemplate, "Course-3", 0.0);

        rows = context.executeQuery("SELECT * FROM course");
        for row in rows:
            print(row);

    input("press enter to exit...") 

if __name__ == "__main__":
    sys.exit(int(main() or 0))