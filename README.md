# runExperiment

Preperation:

1. Connect tobii eyetracker sensor
2. Run tobii eyetracker dotnet app.
3. Open the Mvc.py, go to  Run-> Configuration per file 
4. In the "General Settings" section check "Command line options" if not checked and enter the username (for ex: evina)
5. Press OK button 
6. Have following fields in config:
    [MONGODB]
    Host = localhost
    Port = 27017
    DBName = mediaExposureTry
    
    [TOBII]
    DBCollectionName = eyesRolling

7. Open the circle in the experiment folder

Run:
1. Run the Mvc.py file
3. Press the start button through exposuremeter
4. Press Connect button via tobii eytracker dotnet app
5. Start rolling eyes on the circle
6. When it is done press Disconnect button via tobii eyetracker dotnet app
7. Close the exposuremeter app. to change the userName
8. Change the userName as described in Preperation steps 3&4, and repeat the process for second user from step 1
9. Press the stop button in exposuremeter and close the window
10.Run runExperiment.py in experiment folder having following configuration in the file with proper userNames and session info

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

11. See both produced log file and a graph having circles on the screen