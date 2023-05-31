class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.travel_time={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in.pop(id)
        duration= t - start_time

        travel = (start_station, stationName)

        if travel in self.travel_time:
            travel_duration, count = self.travel_time[travel]
            self.travel_time[travel]=(travel_duration + duration, count+1)
        else:
            self.travel_time[travel]=(duration, 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        time, count = self.travel_time[travel]
        return time/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
