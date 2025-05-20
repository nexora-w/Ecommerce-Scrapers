"""
Configuration settings for the application.
Modify these settings based on your environment and requirements.
"""

DEBUG = False
LOG_LEVEL = "INFO"
APPLICATION_NAME = "Inactivity Monitor"

LOG_DIRECTORY = "../logs"
LOG_FILENAME = "application.log"

INACTIVITY_TIMEOUT = 300
CHECK_INTERVAL = 60 