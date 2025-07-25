import sys

input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder (node):
    if node == '.':
        return
    
    print(node, end='')
    # 튜플의 저장방식이 tree['A'] = ('B', 'C')이므로 tree[node] -> ['A'], [0] -> B, [1] -> C
    preorder(tree[node][0]) # 왼쪽 노드를 먼저 순회하고 끝나면 
    preorder(tree[node][1]) # 오른쪽 노드를 순회

preorder('A')
print()

def inorder (node):
    if node == '.':
        return  
      
    inorder(tree[node][0])
    print(node, end='') # 왼쪽 노드들의  순회가 끝나면 프린트를 하는거야 오른쪽 노드들은 평소랑 똑같이 프린트하고
    inorder(tree[node][1])

inorder('A')
print()

def postoder(node):
    if node == '.':
        return
    
    postoder(tree[node][0])
    postoder(tree[node][1])
    print(node, end='')

postoder('A')