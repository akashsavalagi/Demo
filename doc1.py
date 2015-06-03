import math

class Airplane:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_plane):
        diff_x = self.x - another_plane.x
        diff_y = self.y - another_plane.y
        distance_total = math.sqrt(diff_x**2 + diff_y**2)
        return distance_total
		
class Res:
	def cs():
		airplane1=Airplane(1,3)
		airplane2=Airplane(4,3)
		print airplane1.distance(airplane2)
	cs()