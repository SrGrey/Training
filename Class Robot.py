class Robot:
    ''' inicialase robot with start position and list of steps named 'way' '''
    def __init__(self, position, way=[]):
        self.position = position
        self.way = way

    '''return list of steps named 'way'''
    def path(self):
        return self.way

    def move(self, steps):
        x = self.position[0]
        y = self.position[1]
        '''current position added in list of steps named 'way'    '''    
        steps_list = [(x, y)]
        for count in range(len(steps)):
            if steps[count] == 'N' and y < 100:
                y += 1
                steps_list.append((x, y))
            elif steps[count] == 'S' and y > 0:
                y -= 1
                steps_list.append((x, y))
            elif steps[count] == 'E' and x < 100:
                x += 1
                steps_list.append((x, y))
            elif steps[count] == 'W' and x > 0:
                x -= 1
                steps_list.append((x, y))
        ''' fixing last way'''
        self.way = steps_list
        '''fixing last position'''       
        self.position = (x, y)
        return (x, y)        

       
'''for inicialasation and moving'''
r = Robot((0, 0))
print(r.move('NENE'))
print(*r.path())
