import tree

a0 = tree.Tree(tree.Node('Pierre'), None, None)
a1 = tree.Tree(tree.Node('Romain'), None, None)
a2 = tree.Tree(tree.Node('Philippe'), a0, a1)
a3 = tree.Tree(tree.Node('Xavier'), None, None)
a4 = tree.Tree(tree.Node('Michel'), a2, a3)
a5 = tree.Tree(tree.Node('Vincent'), None, None)
a6 = tree.Tree(tree.Node('Olivier'), None, None)
a7 = tree.Tree(tree.Node('Claude'), a5, a6)
a8 = tree.Tree(tree.Node('Louis'), a4, a7)

print(a8.print_prefix())