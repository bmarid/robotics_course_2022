
#A* algorithm

#We store all the children to be evaluated
open_list=[]
#We store the nodes that form the path
closed_list=[]

start_x=0
start_y=0
end_y=7
end_x=7

# print(StartNode)
# print(open_list)
maze=[]

obstacle_list =[(0,3),(4,5),(5,5),(6,5),(7,5)]

class Node():
    def __init__(self,x,y, parent = None):
        self.parent = parent
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0

def astar(maze):
    #Initialing the start and end nodes
    StartNode = Node(start_x, start_y, None)
    EndNode = Node(end_x,end_y, None)

    current = StartNode
    open_list.append(current)
    closed_list.append(current)

    #A list to store the final path
    path = []
    counter = 0

    #Defifining the position that the child can take: up, down, left, right
    child_list=[(0,1),(0,-1),(-1,0),(1,0)]

    while(len(open_list) != 0):
        # counter = counter + 1
        # if (counter > 2):
        #     open_list.clear()
        #     break

        #Setting a high value for lowest f in order for it to start taking the f values of children
        lowest_f = 65

        if current in open_list:
            open_list.remove(current)

        #Looping through the children
        for i in child_list:
            obstacle=0
            childNode = Node(current.x+i[0],current.y+i[1], current)
            # childNode = Child(1,2)
            #print(childNode.x, childNode.y)

            # Checking if it exists in the closed list
            if childNode in closed_list:
                continue
            #Checking if it is an obstacle
            for t in obstacle_list:
                if childNode.x == t[0] and childNode.y == t[1]:
                    obstacle = 1
            if obstacle == 1:
                continue

            # Checking if it is in the maze
            if childNode.x > 7 or  childNode.x < 0 or childNode.y > 7 or childNode.y < 0:
                continue

            # Checking if it is in open list
            if childNode in open_list:
                continue

            #Calculating values for f, g, h
            childNode.g = abs(childNode.x-StartNode.x)+abs(childNode.y-StartNode.y)
            childNode.h = abs(childNode.x-EndNode.x)+abs(childNode.y-EndNode.y)
            childNode.f = childNode.g + childNode.h

            #Appending in open list
            open_list.append(childNode)

        # Checking which child in open list has the lowest f and assigning the next node to be evaluated for lowest f

        for r in open_list:
            if r.f < lowest_f:
                current = r
                lowest_f = r.f
            elif r.f == lowest_f and r.h < current.h:
                current = r

        closed_list.append(current)


        #Checking if it is end Node .List will become empty and the while will be broken
        if current.x == EndNode.x and current.y == EndNode.y:
            path = []
            path.append((current.x, current.y))
            while (current.parent != None):
                current = current.parent
                path.append((current.x, current.y))
            open_list.clear()
            return (path[::-1])
            # break

def main():

    maze = [[ 0, 0, 1, 0, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0]]


    path = astar(maze)
    print(path)

if __name__ == '__main__':
    main()
