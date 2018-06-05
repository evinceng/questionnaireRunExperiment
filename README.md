# runExperiment

Preperation:

6. Have following fields in config in exposure meter:
    [MONGODB]
    Host = localhost
    Port = 27017
    DBName = mediaExposureTry
    
    [QUESTIONNAIRE] 
    DBCollectionName = questionnaire
    FinalAnswersCollectionName = finalAnswersQuest

Run:
1. Run the Mvc.py file
2. input a userName(ex:evina)
3. Press the start button through exposuremeter
4. Fill the prequestionnaire
5. Close the prequestionnaire
6. Press the stop button through exposuremeter
7. Fill the postquestionnaire
8. Close the postquestionnaire
9. Close the exposuremeter app. 
10.Run runExperiment.py in experiment folder having following configuration in the file with proper userNames and session info

host = "localhost"
port = 27017
dbName = "mediaExposureTry"
collectionName = "finalAnswersQuest"


# evina Configuration
userName1 = "evina" #the username that you inputted in step 2 above

# fieldNames variables
xCoordVariable = "relativeTime"
yCoordVariable = "answer"
timeStampVariable = "relativeTime"
userNameVariable = "userName"

# query variables
userNames = [ userName1 ] # "evina", "user2",
sessions = ["evina2018-06-01 16:02:59.355000" ] # put your sessionID from DB
projectionFields = [ "userName", "relativeTime", "answer" ]
relativeTime = [ ] # start, end # it will get all times if not provided

11. See both produced log file and a graph having numeric answers with relative times