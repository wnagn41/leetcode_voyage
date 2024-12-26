class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        parklotmax_1 = big
        parklotmax_2 = medium
        parklotmax_3 = small
        

    def addCar(self, carType):
        parklot_1 = 0
        parklot_3 = 0
        parklot_3 = 0
        if carType == 1 and parklot_1 < parklotmax_1:
            parklot_1 +=1
        elif carType == 2 and parklot_2 < parklotmax_2:
            parklot_2 +=1
        elif carType == 3 and parklot_3 < parklotmax_3:
            parklot_3 +=1  
        else:
            return False
        return True      


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.


## 知识点 ：记得学习python中的 字典 dictionary
print(tiem)