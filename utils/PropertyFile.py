import configparser
import os
config = configparser.ConfigParser()

# set the path for config.ini file
configFile = 'config.ini'
current_directory = os.path.dirname(__file__)
configFilePath = os.path.join(current_directory, configFile)

# Function to set the Attributes of Json Values
def getValue(Attrb1, Attrb2):
    config.read(configFilePath)
    value = config.get(Attrb1, Attrb2)
    return value

# Function to set the Format of Date Values
def getDateFormat(DBDate):
    Month = DBDate.strftime('%m')
    Date = (DBDate.strftime('%d'))
    Year = str(DBDate.year)
    DateVal = Month + '/' + Date + '/' + Year
    return DateVal
