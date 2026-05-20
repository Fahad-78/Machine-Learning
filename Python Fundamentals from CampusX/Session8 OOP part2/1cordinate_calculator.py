"""Write OOP classes to handle the following scenarios:
    ->A user can create and view 2D coordinates
    ->A user can find out the distance between 2 coordinates
    ->A user can find the distance of a coordinate from origin
    ->A user can check if a point lies on a given line
    ->A user can find the distance between a given 2D point and a given line
    """

class point:
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '({},{})'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        #return ((self.x_cod)**2+(self.y_cod)**2)**0.5
        return self.euclidean_distance(point(0,0))
    

class line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "Not lies on the line"

    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C) / (line.A**2 + line.B**2)**0.5
    
p1 = point(0,0)
p2 = point(1,1)
print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())

l1 = line(1,1,-2)
p3 = point(1,1)
print(l1.point_on_line(p3))

l2 = line(1,1,-2)
p4 = point(1,5)
print(l2.shortest_distance(p4))
