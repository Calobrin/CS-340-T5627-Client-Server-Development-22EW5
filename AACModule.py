from pymongo import MongoClient
from bson.objectid import ObjectId
import bson.json_util as json_util
from bson.json_util import dumps




#Note: I had to use the Admin User I created for the previous milestone. Using "aacuser" and the password of "Ultimate"
#causes an authorizaton error in Jupyter

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:46360' % (username, password))
        self.database = self.client['AAC']
        
# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            if data:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True            #Returns True if succseful
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                return False           #Otherwise raises Exception and returns False
# Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            if data:
                result = self.database.animals.find(data)
                return result          #Returns result, which produces the cursor location of the data if found
            else:
                exception = "Nothing to read, because data parameter is empty"
                return exception       #Otherwise it returns the error message set to "exception"
# Method to implement a "retreive all" function
    def readAll(self, data):
        #Similar method to read, except the data being passed is an empty dictionary with no search criteria.
        #This causes it to just find, essentially, all documents, but is being limited to just 35.
        result = self.database.animals.find({}).limit(35)    
        return(result)
# Method to implement the U in CRUD    
    def update(self, data, newData):
        if data is not None:
            if data:
                result = self.database.animals.update_one(data, newData)
                #return dumps(result)#Returns result in JSON format
                return dumps(newData)
                ##I need to return this as a JSON format, for now
            else:
                exception = "Nothing to update, because data parameter is empty"
                return exception       #Otherwise it returns the error message set to "exception"
# Method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            if data:
                self.database.animals.delete_one(data)
                return json_util.dumps(data) #Returns the data passed in (because it was deleted)
                #This is a baind-aid fix. It "works" but is kind of sloppy...
            else:
                exception = "Nothing to delete, because the data parameter is empty"
                return exception       #Otherwise it returns the error message set to "exception"