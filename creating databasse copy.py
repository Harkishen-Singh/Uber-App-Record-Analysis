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
        #client=MongoClient("mongodb://127.0.0.1:27017")
        #database=client['testing']



        self.file_name=input("Enter the name of the text file to read the source code :\n")
        self.file_name = self.file_name + ".txt"
        self.file_open=open(self.file_name, 'r')
        self.file2=self.file_open.read()
        self.file=BeautifulSoup(self.file2)
        print(self.file + "\n\n")
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

        self.search='<p class="portable-soft-huge--right submenu__item__link layout cursor--pointer"><span class="layout__item portable-one-half one-half">' # first day
        search_length=len(self.search)
        c=0

        day=""
        #collection=database[day]

        day_last_left=0
        for i in range(0, len((self.file))-search_length): # counting individual trip of that day.
            substr = self.file[i:i+search_length]

            if self.search == substr:
                trip_number=-1
                pos=i
                pos_span_ending=0
                ending_span=""
                for oo in range(1, 1000):
                    ss=self.file[pos + oo: pos+oo+7]
                    if ss=="</span>":
                        pos_span_ending=pos+oo
                c = c + 1 # day count
                day = self.file[i+search_length+1:pos_span_ending+1]
                s_trip_start='<span class="trip-list__date layout__item one-quarter">'
                s_trip_time='<span class="trip-list__duration layout__item one-quarter">'
                s_trip_distance='<span class="trip-list__distance layout__item one-quarter"'
                s_trip_earning='<span class="soft-tiny--left"'
                span_endings='</span>'
                s_trip_start_l=len(s_trip_start)
                s_trip_time_l=len(s_trip_time)
                s_trip_distance_l=len(s_trip_distance)
                s_trip_earning_l=len(s_trip_earning)
                e_trip_start=0
                e_trip_time=0
                e_trip_distance=0
                e_trip_earning=0
                check=2
                trip_number = trip_number + 1

                # trip time
                for r in range(e_trip_time, len(self.file)- s_trip_time_l):
                    t = self.file[ e_trip_time + r : e_trip_time + r + s_trip_time_l ]
                    check=2

                    if t == s_trip_time:

                        start = r + s_trip_time_l +1
                        for m in range(1,100): # trip time findings
                            now=self.file[r+m: r+m+7]
                            if now==span_endings:
                                e_trip_time=r+m+7
                                self.trip_time=self.file[start : e_trip_time + 1 ]
                                check=0
                                break
                        if trip_number==0:
                            continue

                        if check==0:
                            check=2
                            break

                # trip start time
                for r in range(e_trip_start, len(self.file)- s_trip_start_l):
                    t = self.file[ e_trip_start + r : e_trip_start + r + s_trip_start_l ]
                    check=2
                    if t == s_trip_start:
                        start = r + s_trip_start_l +1
                        for m in range(1,100): # trip time findings
                            now=self.file[r+m: r+m+7]
                            if now==span_endings:
                                e_trip_start=r+m+7
                                self.trip_start=self.file[start : e_trip_start + 1 ]
                                check=0
                                break
                        if trip_number==0:
                            continue
                        if check==0:
                            check=2
                            break

                #trip distance
                for r in range(e_trip_distance, len(self.file)- s_trip_distance_l):
                    t = self.file[ e_trip_distance + r : e_trip_distance + r + s_trip_distance_l ]
                    check=2
                    if t== s_trip_distance:
                        start = r + s_trip_distance_l +1
                        for m in range(1,100): # trip time findings
                            now=self.file[r+m: r+m+7]
                            if now==span_endings:
                                e_trip_distance=r+m+7
                                self.trip_distance=self.file[start : e_trip_distance + 1 ]
                                check=0
                                break
                        if trip_number==0:
                            continue
                        if check==0:
                            check=2
                            break

                # trip earnings
                for r in range(e_trip_earning, len(self.file)- s_trip_earning_l):
                    t = self.file[ e_trip_earning + r : e_trip_earning + r + s_trip_earning_l ]
                    check=2
                    if t==s_trip_earning:
                        start = r + s_trip_earning_l +1
                        for m in range(1,100): # trip time findings
                            now=self.file[r+m: r+m+7]
                            if now==span_endings:
                                e_trip_earning=r+m+7
                                self.trip_earning=self.file[start : e_trip_earning + 1 ]
                                check=0
                                break
                        if trip_number==0:
                            continue
                        if check==0:
                            check=2
                            break

                # completed trips calcultaion for one trip.
                print("Day "+day)
                print("Trip number "+str(trip_number))
                print("Trip starting "+self.trip_start)
                print("Trip time "+self.trip_time)
                print("Trip distance "+self.trip_distance)
                print("Trip earnings "+self.trip_earning)










object= Data_extraction_creation()
object.getting_source()
