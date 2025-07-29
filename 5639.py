import sys
sys.setrecursionlimit(20000)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except EOFError:
        break

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]
    idx = start + 1
    
    while idx <= end and preorder[idx] < root:
        idx += 1
    
    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)

if preorder:
    postorder(0, len(preorder) - 1)