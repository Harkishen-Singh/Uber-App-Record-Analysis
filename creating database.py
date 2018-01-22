from pymongo import MongoClient
import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Data_extraction_creation:

    def __init__(self):
        self.source=""
        self.search=""
        self.search_length=0

    def getting_source(self):
        self.file_name=input("Enter the name of the text file to read the source code :\n")
        self.file_name = self.file_name + ".txt"
        self.file_open=open(self.file_name, 'r')
        self.file=self.file_open.read()
        self.search="small text-uber-white"
        search_length=len(self.search)
        c=0
        for i in range(0, len((self.file))-search_length): # for total counting part
            substr = self.file[i:i+search_length]
            if self.search == substr:
                c = c + 1
                if c == 3: # got the total time of the day
                    self.time_total = self.file[i+search_length+2: i+search_length+12]

                if c==4: # got the total distance of the day
                    self.distance_total = self.file[i+search_length+2:i+search_length+7] + " km"

                if c==5: # got the total cash collection
                    self.cash_collection_total = self.file[i+search_length+2:i+search_length+10]

                if c==6: # got the total earnings
                    self.earnings_total = self.file[i+search_length+2: i+search_length+10]
                    break

        #print(self.time_total + self.distance_total + self.cash_collection_total + self.earnings_total)

        self.search="milli display--block" # first day
        search_length=len(self.search)
        c=0
        trip_number=0
        day=""
        for i in range(0, len((self.file))-search_length): # counting individual trip of that day.
            substr = self.file[i:i+search_length]

            if self.search == substr:
                c = c + 1 # day count
                day = self.file[i+search_length+2:i+search_length+13]
                search2="trip-table__row"
                search_length2=len(search2)

                m=0
                for j in range(0, len((self.file))-search_length2):

                    substr2 = self.file[j:j+search_length2]
                    if substr2 == search2:
                        trip_number = trip_number+1
                        m=m+1
                        count=0
                        for k in range(1, 1000): #<td> and </td> count search
                            s1 = "<td>"
                            s2 = "</td>"
                            pos_of_s2=0
                            s3 = self.file[j+search_length2 +k: j+search_length2 +k+4]
                            s4 = self.file[j+search_length2 +k: j+search_length2 +k+5]

                            if s3 == s1:
                                count = count +1
                                if count==1:
                                    for pp in range(0,20):
                                        sear= self.file[j+search_length2 +k+pp: j+search_length2 +k+pp+5]
                                        if sear == s2:
                                            pos_of_s2=pp
                                    trip_start=str(self.file[j+search_length2 +k+4: j+search_length2 +k+pos_of_s2])
                                if count==3:
                                    for pp in range(0,20):
                                        sear= self.file[j+search_length2 +k+pp: j+search_length2 +k+pp+5]
                                        if sear == s2:
                                            pos_of_s2=pp
                                    trip_time=str(self.file[j+search_length2 +k+4: j+search_length2 +k+pos_of_s2])

                                if count==4:
                                    for pp in range(0,20):
                                        sear= self.file[j+search_length2 +k+pp: j+search_length2 +k+pp+5]
                                        if sear == s2:
                                            pos_of_s2=pp
                                    trip_km=str(self.file[j+search_length2 +k+4: j+search_length2 +k+pos_of_s2])

                                if count==5:
                                    for pp in range(0,20):
                                        sear= self.file[j+search_length2 +k+pp: j+search_length2 +k+pp+5]
                                        if sear == s2:
                                            pos_of_s2=pp
                                    trip_cash_collected=str(self.file[j+search_length2 +k+4: j+search_length2 +k+pos_of_s2])

                                if count==6:
                                    break
                        print("day = "+ day)
                        print("trip_number"+ str(trip_number))
                        print("trip_km "+ trip_km)
                        print("trip_time = "+ trip_time)
                        print("trip_start = "+ trip_start)
                        print("trip_cash_collected = "+ trip_cash_collected)
                        print("\n\n")








object= Data_extraction_creation()
object.getting_source()
