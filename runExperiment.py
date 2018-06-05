# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:49:25 2018

@author: evin
"""
import sys

utilsPath = "../../../03-Tools/00-Utils/"

if utilsPath not in sys.path:
    sys.path.append(utilsPath)

# ===========================================================================================================        
## 1. Short description -------------------------------------------------------------------------------------
# @brief An analysis to see the answers to the pre and post questionnaire
# @author EvinA
# @time 2018-06-04


# ===========================================================================================================
## 2. Configuration, libraries -----------------------------------------------------------------------------

# Trace files 
coreTraceFileName = "_Questionnaire_trace.txt"
traceEnabled = True

# Load libraries -------------------------------------------------------------------------------------------
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import sys
import platform
import matplotlib.pyplot as plt
from datetime import datetime
from numbers import Number
import FileUtils
import QueryUtils
# ===========================================================================================================
# 3. Experimental design ---------------------------------------------------------------------------------------

# Database connection Parameters
host = "localhost"
port = 27017
dbName = "mediaExposureTry"
collectionName = "finalAnswersQuest"

# evina Configuration
userName1 = "evina"

# user2 Configuration
#userName2 = "user2"

# fieldNames variables
xCoordVariable = "relativeTime"
yCoordVariable = "answer"
timeStampVariable = "relativeTime"
userNameVariable = "userName"

# query variables
userNames = [ userName1 ] # "evina", "user2",
sessions = ["evina2018-06-05 12:00:29.266000" ]
projectionFields = [ "userName", "relativeTime", "answer" ]
relativeTime = [ ] # start, end # it will get all times if not provided

# ============================================================================================================
# 4. Load data & trace files ---------------------------------------------------------------------------------
    
# Establish db connection & load data

try:
    client = MongoClient(host=host, port=port)
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)
        
dbh = client[dbName]
collection = dbh[collectionName]

projection = QueryUtils.constructProjectionFileds(projectionFields)
query = QueryUtils.constructQuery(userNames, sessions, relativeTime)
    
resultList = list(collection.find(query, projection))
print resultList

# construct users dict-----------------------------------------------
users = QueryUtils.createUsersDict(userNameVariable, userNames, projectionFields, resultList)
            
# Create trace file
currentTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#if traceEnabled:
path = FileUtils.getAbsPath(currentTime + coreTraceFileName)
traceFileName = open(path, "w")


# =============================================================================================================
# 5. Report ---------------------------------------------------------------------------------------------------
# Basics
FileUtils.traceToFileEOL(traceEnabled, traceFileName, "An analysis to see two circles on a graph via interpolating two users eyeGaze information taken from Tobii eyetracker through time, while rolling eyes")
FileUtils.traceToFileEOL(traceEnabled, traceFileName, "Time: " + currentTime)
FileUtils.traceToFileEOL(traceEnabled, traceFileName, "OS: " + platform.system())
FileUtils.traceToFileEOL(traceEnabled, traceFileName, "Python ver: " + platform.python_version())

# Experimental design
FileUtils.traceToFileEOL(traceEnabled, traceFileName, "")
FileUtils.traceToFileLists(traceEnabled, traceFileName, userNames, "Extracted Users:", "User: ")
FileUtils.traceToFileLists(traceEnabled, traceFileName, sessions, "Extracted Sessions:", "Session: ")
FileUtils.traceToFileLists(traceEnabled, traceFileName, projectionFields, "Extracted Fileds:", "Field: ")
FileUtils.traceToFileLists(traceEnabled, traceFileName, relativeTime, "Extracted Time Period:", "relativeTime: ")

# ============================================================================================================
# 6. Implement Experiment --------------------------------------------------------------------------------------------
#=========================================================================
#print users
# identify x and y coordinatesand for plotting the graph
xCoord = users[userName1][xCoordVariable]
#print xCoord
#print "@@@@@@@"
yCoord = users[userName1][yCoordVariable]
timeStamps = users[userName1][timeStampVariable]
#print yCoord
#print "@@@@@@@"
xCoordNumeric = []
yCoordNumeric = []
for i in range(0, len(yCoord)):
    if isinstance(yCoord[i], Number):
        yCoordNumeric.append(yCoord[i])
        xCoordNumeric.append(xCoord[i])

nonNumericxCoord = list(set(xCoord) - set(xCoordNumeric))
#print nonNumericxCoord
nonNumericyCoord = list(set(yCoord) - set(yCoordNumeric))
#print nonNumericyCoord

#Plot figures
#plt.scatter(xCoordNumeric, yCoordNumeric)
#plt.title(yCoordVariable + " versus " + xCoordVariable)
#plt.xlabel(xCoordVariable)
#plt.ylabel(yCoordVariable)


#f = plt.figure()
f, axes = plt.subplots(nrows = 2, ncols = 1, sharex=True)
axes[0].scatter(xCoordNumeric, yCoordNumeric)
axes[0].set_xlabel(xCoordVariable)
axes[0].set_ylabel("Numeric answers")
axes[1].scatter(nonNumericxCoord, nonNumericyCoord)
axes[1].set_xlabel(xCoordVariable)
axes[1].set_ylabel("Non Numeric answers")
plt.tight_layout()
plt.show()

figPath = FileUtils.getAbsPath(currentTime + "_Questionnaire.pdf")
plt.savefig(figPath)

## Close trace files -------------------------------------------------------------------------------------------------
if traceEnabled:
    traceFileName.close()


