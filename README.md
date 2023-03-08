Flight Deals
video Demo: 
Description :
 
This project is a Python based program that gives the best Flight deals to the user by notifying the user via sms to his/her phone.The purpose of this building this project was because, I found
that its really time wasting to get the best flight deals for a particular location. But with this program all the user has to do is to insert IATA code location of your destination and the program 
give the user the best flight deals available in its location, the time of flight and the time arrival.

In this project several API's are used, firstly we use a spreadsheet which saves several locations and access them using the sheety.com api which parse the data of the locations around the world using
thier IATA code.Secondly we would need flight deals prices from any location aroud the world and for this we would use the tequila-kiwi API which would provide flight data including prices, timelfight, 
flight_delays, flight_type, max_stopovers and many other query params and lastly,  we would the Twilio API to notify user by sms about the flight deals through the users telephone number

This project also uses the request module to send response to the different API's. In this project there are several api_keys and personal authetification keys which could not be revealed to keep my confidentiality and
users privacy for people who would use the program.

For this project we have 3 different classes which may not be included here because the cs50 program only takes the project.py file but would be included in my github account 
Building this project took me some time with alot of issues encountered for example, try to figure how to parse data from the flight_search class to the Notification manager class which was very complicated to do.

If there is any question to this project let me know in the comments i will try to answer.

This is CS50!