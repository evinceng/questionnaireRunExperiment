# runExperiment

1. Run the Mvc.py file with the commandline argument providing userName (for ex: evina) having the following fields in config:
    [MONGODB]
    Host = localhost
    Port = 27017
    DBName = mediaExposureTry
    
    [TOBII]
    DBCollectionName = eyesRolling
2. Connect tobii eyetracker sensor
3. Run tobii eytracker dotnet app.
4. Open the circle in the experiment folder
5. Press the start button through exposuremeter
6. press Connect button via tobii eytracker dotnet app
7. Start rolling eyes on the circle
8. When it is done press Disconnect button via tobii eytracker dotnet app
9. Change the userName is step 1 and repeat the process for second user
10. Press the stop button through exposuremeter
11.Run runExperiment.py in experiment folder having following configuration in the file with proper userNames and session info

host = "localhost"
port = 27017
dbName = "mediaExposureTry"
collectionName = "eyesRolling"

# evina Configuration
userName1 = "evina"
Ts = 0.5 # Sampling frequency
fCode = 1
k = 3 
tMin = 1.6
tMax = 5

# user2 Configuration
userName2 = "user2"
TsUser = 0.5 # Sampling frequency
fCodeUser = 1
kUser = 3 
tMinUser = 3 # 1.49
tMaxUser = 9 # 10.2

# fieldNames variables
xCoordVariable = "leftGaze:x"
yCoordVariable = "leftGaze:y"
timeStampVariable = "relativeTime"
colorUponVariable = "relativeTime"
userNameVariable = "userName"

# query variables
userNames = [ userName1, userName2] # "evina", "user2",
sessions = [ ] #  "evina2018-05-10 14:33:21.185000", "user22018-05-14 12:06:23.842000",
projectionFields = [ "userName", "relativeTime", "leftGaze:x", "leftGaze:y" ]
relativeTime = [ ] # start, end # it will get all times if not provided

12. See both produced log file and agraph having circles on the screen