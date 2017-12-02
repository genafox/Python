import sys
from datetime import datetime
from DataMapper import *
from DbConnectionSettings import *
from DbContext import *

getAllCoursesTemplate = """
        SELECT id, name, price FROM course ORDER BY id"""
getTopPopularCourse = """
     SELECT	id,  
		name,  
		price,
        mark
    FROM  
    (  
    	SELECT  id,  
    			name,  
    			price,  
    			mark,  
    			ROW_NUMBER() OVER (ORDER BY id asc) row_number
    	FROM   
    	(  
    		SELECT  c.id,  
    				c.name,  
    				c.price,  
    				AVG(cm.mark) AS mark  
    		FROM course c 
    			INNER JOIN mark cm ON (c.id = cm.course_id)  
    		GROUP BY c.id, c.name, c.price
                 HAVING AVG(cm.mark) > %s
    	) RatedCourses  
    ) Numbered  
    WHERE %s < row_number AND row_number <= %s"""
getCourseByIdTemplate = """
    SELECT *
    FROM course
    WHERE id = %s"""
createCourseTemplate = """
    INSERT INTO course (name, price)
    VALUES (%s, %s)
    RETURNING id"""
updateCourseTemplate = """
    UPDATE course
    SET name = %s, price = %s
    WHERE id = %s"""
deleteCourseTemplate = """
    DELETE FROM course
    WHERE id = %s"""


createLectureTemplate = """
    INSERT INTO "lecture" (name, course_id, content)
    VALUES (%s, %s, %s)
    RETURNING id"""


createMarkTemplate = """
    INSERT INTO "mark" (course_id, user_id, mark, comment, date)
    VALUES (%s, %s, %s, %s, %s)"""


createSessionTemplate = """
    INSERT INTO "session" (start_date, end_date, course_id)
    VALUES (%s, %s, %s)
    RETURNING id"""


createUserTemplate = """
    INSERT INTO "user" (login, password)
    VALUES (%s, %s)
    RETURNING id"""


createSessionUserTemplate = """
    INSERT INTO session_users (session_id, user_id)
    VALUES (%s, %s)"""

def seed(context):
    course1Id = context.executeScalar(createCourseTemplate, "Course-1", 10.99)
    course2Id = context.executeScalar(createCourseTemplate, "Course-2", 0.99)
    course3Id = context.executeScalar(createCourseTemplate, "Course-3", 0.0)
    courseToDeleteId = context.executeScalar(createCourseTemplate, "Course-4", 100.0)

    user1Id = context.executeScalar(createUserTemplate, "Superman", "Password12")
    user2Id = context.executeScalar(createUserTemplate, "AquaMan", "Password12")
    user3Id = context.executeScalar(createUserTemplate, "Flash", "Password12")
    user4Id = context.executeScalar(createUserTemplate, "WonderWoman", "Password12")

    session1Id = context.executeScalar(createSessionTemplate, '10-12-16', '10-01-18', course1Id)
    session2Id = context.executeScalar(createSessionTemplate, '10-10-17', '10-12-17', course2Id)

    context.executeNonQuery(createSessionUserTemplate, session1Id, user1Id)
    context.executeNonQuery(createSessionUserTemplate, session1Id, user2Id)
    context.executeNonQuery(createSessionUserTemplate, session2Id, user1Id)
    context.executeNonQuery(createSessionUserTemplate, session2Id, user4Id)

    context.executeNonQuery(createLectureTemplate, 'Lecture 1', course1Id, 'This is content of the Course 1 lecture 1')
    context.executeNonQuery(createLectureTemplate, 'Lecture 2', course1Id, 'This is content of the Course 1 lecture 2')
    context.executeNonQuery(createLectureTemplate, 'Lecture 3', course1Id, 'This is content of the Course 1 lecture 3')
    context.executeNonQuery(createLectureTemplate, 'Lecture 1 C2', course2Id, 'This is content of the Course 2 lecture 1')
    context.executeNonQuery(createLectureTemplate, 'Lecture 1 C3', course3Id, 'This is content of the Course 3 lecture 1')

    context.executeNonQuery(createMarkTemplate, course1Id, user1Id, 5.0, 'This course is awesome!', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    context.executeNonQuery(createMarkTemplate, course1Id, user2Id, 4.5, 'This course is quite good enough!', datetime(2017, 9, 23, 15, 8, 24).strftime('%Y-%m-%d %H:%M:%S'))
    context.executeNonQuery(createMarkTemplate, course2Id, user1Id, 3.5, 'Does not like it much', datetime(2017, 10, 17, 15, 00, 00).strftime('%Y-%m-%d %H:%M:%S'))
    context.executeNonQuery(createMarkTemplate, course2Id, user4Id, 5.0, None, datetime(2017, 10, 12, 18, 00, 00).strftime('%Y-%m-%d %H:%M:%S'))

def getAllCourses(context, dataMapper, shouldPrint=True):
    rows = context.executeQuery(getAllCoursesTemplate)
    courses = list(map(lambda row: dataMapper.MapCourse(row), rows));
    if shouldPrint:
        for c in courses:
            print(c.toString());
    return courses;

def main():

    dataMapper = DataMapper()
    connSettings = DbConnectionSettings().getDict()

    with DbContext(connSettings) as context:
        # seed
        seed(context);

        #get all courses
        courses = getAllCourses(context, dataMapper);

        context.executeNonQuery(updateCourseTemplate, courses[2].name, 100.99, courses[2].id);
        courses = getAllCourses(context, dataMapper);

        context.executeNonQuery(deleteCourseTemplate, courses[3]);
        courses = getAllCourses(context, dataMapper);

        #get course ordered by mark which has mark > 4.5
        rows = context.executeQuery(getTopPopularCourse, 4.5, 0, 10)
        for row in rows:
            course = dataMapper.MapCourseInfo(row)
            print(course.toString(0))


    input("press enter to exit...") 

if __name__ == "__main__":
    sys.exit(int(main() or 0))