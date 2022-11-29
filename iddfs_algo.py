##ID DFS algo
graph ={
         'a' : ['b','c'],
         'b' : ['d','e'],
         'c' : ['g'],
         'd' : [],
         'e' : ['f'],
         'f'  : [],
         'g' : []
}
def dfs(currNode, goalNode, depth, graph):
     print("Checking node : ",currNode)
     if currNode == goalNode:
          return True
     if depth<=0:
          return False
     for node in graph[currNode]:
          if dfs(node, goalNode, depth-1, graph):
               return True
     return False

def iddfs(currNode, goalNode, depth, graph):
     for i in range(depth):
          if dfs(currNode, goalNode, i, graph):
               return True
     return False

if iddfs('a', 'g', 5, graph):
     print("path exists")
else:
     print("path not found")
     
