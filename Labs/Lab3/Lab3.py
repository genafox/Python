import http.client
import urllib.parse
import json
import types
import datetime
import time
import sched

def sendRequest(url):
    params = urllib.parse.urlencode({})
    
    headers = {
        "Content-type": "text/html; charset=WINDOWS-1251",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    
    conn = http.client.HTTPConnection("cist.nure.ua")
    conn.request("GET", "/ias/app/tt/" + url, params, headers)
    response = conn.getresponse()
    data = response.read().decode("windows-1251").replace('\r\n', '')
    
    conn.close()

    try:
        return json.loads(data)
    except:
        return {}

def task1():
    departmentsArray = [];
    allFacultiesUrl = "P_API_FACULTIES_JSON"
    result = sendRequest(allFacultiesUrl)
    
    for faculty in result["university"]["faculties"]:
        facultyUrl = "P_API_DEPARTMENTS_JSON?p_id_faculty=" + str(faculty["id"])
        faculty = sendRequest(facultyUrl)

        for department in faculty["faculty"]["departments"]:
            departmentsArray.append(department["full_name"])

    return departmentsArray

def task2(groupName, timeSpanType):
    def getCurrentGroup(groupName):
        allGroupsUrl = "P_API_GROUP_JSON"
        result = sendRequest(allGroupsUrl)

        for faculty in result["university"]["faculties"]:
            for direction in faculty["directions"]:
                if (len(direction["specialities"]) > 0):
                    for speciality in direction["specialities"]:
                        for group in speciality["groups"]:
                            if (group["name"] == groupName):
                                return group
                else:
                    for group in direction["groups"]:
                        if (group["name"] == groupName):
                            return group

        return '';

    groupId = getCurrentGroup(groupName)["id"]
    
    fromTime = int((datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1) - datetime.datetime(1970,1,1)).total_seconds())
    toTime = fromTime

    if (timeSpanType == "day"):
        toTime = toTime + 60*60*24
    elif (timeSpanType == "week"):
        toTime = toTime + 60*60*24*7
    elif (timeSpanType == "month"):
        toTime = toTime + 60*60*24*31

    groupEventsUrl = "P_API_EVENT_JSON?timetable_id=" + str(groupId) + '&type_id=1' + '&time_from=' + str(fromTime) + '&time_to=' + str(toTime)

    data = sendRequest(groupEventsUrl)
    events = data["events"]
    groups = data["groups"]
    teachers = data["teachers"]
    subjects = data["subjects"]
    types = data["types"]

    currentSubjects = []
    previousSubjectDate = datetime.datetime(1970,1,1)

    for event in events:
        for subject in subjects:
            if (event["subject_id"] == subject["id"]):
                currentSubjects.append(subject["title"])

                currentSubjectDate = datetime.datetime.fromtimestamp(event["start_time"])
                
                if (previousSubjectDate.date() != currentSubjectDate.date()):
                    print('')
                    print(currentSubjectDate.date())
                
                startTime = datetime.datetime.fromtimestamp(event["start_time"])
                endTime = datetime.datetime.fromtimestamp(event["end_time"])
                print(startTime.strftime('%H:%M') + ' - ' + endTime.strftime('%H:%M') + ' ' + subject["title"])

                previousSubjectDate = currentSubjectDate

    return events

def task3(auditoryName):
    def getAuditory(auditoryName):
        allAuditoriesUrl = "P_API_AUDITORIES_JSON"
        result = sendRequest(allAuditoriesUrl)

        for building in result["university"]["buildings"]:
            for auditory in building["auditories"]:
                if (auditory["short_name"] == auditoryName):
                    return auditory

        return '';

    auditoryId = getAuditory(auditoryName)["id"]
    
    fromTime = int((datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1) - datetime.datetime(1970,1,1)).total_seconds())
    toTime = fromTime + 60*60*24

    auditoryEventsUrl = "P_API_EVENTS_AUDITORY_JSON?p_id_auditory=" + str(auditoryId) + '&time_from=' + str(fromTime) + '&time_to=' + str(toTime)

    data = sendRequest(auditoryEventsUrl)
    
    groups = data["groups"]
    teachers = data["teachers"]

    groupNames = []
    teacherNames = []

    print('Groups:')
    for group in groups:
        groupNames.append(group["name"])

    print(groupNames)
    print('')
    
    print('Teachers:')
    for teacher in teachers:
        teacherNames.append(teacher["full_name"])
        
    print(teacherNames)

def task4():
    fromTime = int((datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1) - datetime.datetime(1970,1,1)).total_seconds())
    toTime = fromTime + 60*60*24
    
    allGroupsUrl = "P_API_GROUP_JSON"
    data = sendRequest(allGroupsUrl)
    faculties = data["university"]["faculties"]

    for faculty in faculties:
            for direction in faculty["directions"]:
                if (len(direction["specialities"]) > 0):
                    for speciality in direction["specialities"]:
                        i = 1
                        print(speciality["full_name"])
                        for group in speciality["groups"]:
                            groupEventsUrl = "P_API_EVENT_JSON?timetable_id=" + str(group["id"]) + '&type_id=1' + '&time_from=' + str(fromTime) + '&time_to=' + str(toTime)

                            data = sendRequest(groupEventsUrl)
                            
                            if (data != {}):
                                for subject in data["subjects"]:
                                    for hour in subject["hours"]:
                            
                                        if (hour["type"] == 0 or hour["type"] == 1 or hour["type"] == 2):
                                            print(' ' + str(i) + ') ' + subject["title"])
                                            i = i + 1
                else:
                    i = 1
                    print(direction["full_name"])
                    for group in direction["groups"]:
                        groupEventsUrl = "P_API_EVENT_JSON?timetable_id=" + str(group["id"]) + '&type_id=1' + '&time_from=' + str(fromTime) + '&time_to=' + str(toTime)

                        data = sendRequest(groupEventsUrl)
                        if (data != {}):

                            for subject in data["subjects"]:
                                for hour in subject["hours"]:
                                    if (hour["type"] == 0 or hour["type"] == 1 or hour["type"] == 2):
                                        print(' ' + str(i) + ') ' + subject["title"])
                                        i = i + 1
            
            print('')

def task5():
    previousSchedule = {}

    def getNewSchedule():
        allGroupsUrl = "P_API_GROUP_JSON"
        result = sendRequest(allGroupsUrl)
        changes = [];

        for faculty in result["university"]["faculties"]:
            for direction in faculty["directions"]:
                if (len(direction["specialities"]) > 0):
                    for speciality in direction["specialities"]:
                        for group in speciality["groups"]:
                            groupEventsUrl = "P_API_EVENT_JSON?timetable_id=" + str(group["id"])
                            data = sendRequest(groupEventsUrl)


                            if (data != {}):
                                if (group["id"] not in previousSchedule.keys()):
                                    previousSchedule[group["id"]] = data["events"]
                                elif (previousSchedule[group["id"]] != data["events"]):
                                    previousSchedule[group["id"]] = data["events"]

                                    changes.append(data["events"])
                                
                else:
                    for group in direction["groups"]:
                        groupEventsUrl = "P_API_EVENT_JSON?timetable_id=" + str(group["id"])
                        data = sendRequest(groupEventsUrl)

                        if (data != {}):
                            if (group["id"] not in previousSchedule.keys()):
                                previousSchedule[group["id"]] = data["events"]
                            elif (previousSchedule[group["id"]] != data["events"]):
                                previousSchedule[group["id"]] = data["events"]

                                changes.append(data["events"])

        if (len(changes) == 0):
            print('No changes found')
        else:
            print(changes)
    
    s = sched.scheduler(time.time, time.sleep)
    getNewSchedule()
    s.enter(600, 1, getNewSchedule, ())
    s.run()
    
#print(task1())
#task2("ПІ-14-4", "month")
#task3("165-5")
#task4()
task5()

    
