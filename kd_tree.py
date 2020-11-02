class Node(object):
    def __init__(self, left, right):
        self.point = []
        self.left = left
        self.right = right


def createNode(newPoint):
    newNode = Node(None, None)
    newNode.point = newPoint
    return newNode


def insertNode(root, point, dimensions, depthOfTree):
    cou = 0
    if root is None:
        cou += 1
        root = createNode(point)
    else:
        currentDimension = depthOfTree % dimensions
        if point[currentDimension] < root.point[currentDimension]:
            root.left = insertNode(root.left, point, dimensions, depthOfTree + 1)
        else:
            root.right = insertNode(root.right, point, dimensions, depthOfTree + 1)
    return root


def searchNode(root, point, dimensions, depthOfTree):
    if root is None:
        return False
    if root.point == point:
        return True
    else:
        currentDimension = depthOfTree % dimensions
        if point[currentDimension] < root.point[currentDimension]:
            return searchNode(root.left, point, dimensions, depthOfTree + 1)
        return searchNode(root.right, point, dimensions, depthOfTree + 1)


def printTree(root, depthOfTree):
    if root is None:
        return
    print('Point:', root.point, '\tDepth of this point: ', depthOfTree)
    printTree(root.left, depthOfTree + 1)
    printTree(root.right, depthOfTree + 1)



rootNode = None
points = [[3, 6], [17, 15], [13, 15], [13, 15],[6, 12], [9, 1], [2, 7], [10, 19]]
totalSize = len(points)
totalDimension = len(points[0])

i = 0
while i < totalSize:
    rootNode = insertNode(rootNode, points[i], totalDimension, 0)
    i += 1

print('Total dimentions:', totalDimension)
printTree(rootNode, 0)
