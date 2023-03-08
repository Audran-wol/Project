import pytest

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# Now lets test each class output 

#Lets test the data_manager
#will need to be updated all the way to submitting

def test_data_manager():
    assert instructions() == """
        ****************** Flight_deals data_manager ****************
        Given location:
        if location given the program triggers the api then prints data from
        -the spreadsheet which is commonly the IATA code and the pricing

        Update destination:
        Then we update destination of the given location by --sending a pull requests to the api_testing zone

    """


def test_flight_search():
    if sys.argv[1] == "--location{IATA-code}":
        assert FlightSearch("get_destination_code") == "Check_flights: Gives the query of all the different params"

def test_notification_manager():
    assert instructions() == """
    ********************* Notification Managers ******************

    Message send: 
    Message would be send when the exact location already triggered all the other function then send a 
    ---message on different query which would be used 
    """


