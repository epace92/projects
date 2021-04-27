import tree
import EvalExp

a0 = tree.Tree(tree.Node(1), None, None)
a1 = tree.Tree(tree.Node(2), None, None)
a2 = tree.Tree(tree.Node("+"), a0, a1)
a3 = tree.Tree(tree.Node(3), None, None)
a4 = tree.Tree(tree.Node("x"), a2, a3)
a5 = tree.Tree(tree.Node(4), None, None)
a6 = tree.Tree(tree.Node(5), None, None)
a7 = tree.Tree(tree.Node("x"), a5, a6)
a8 = tree.Tree(tree.Node("+"), a4, a7)

print("a8.print_prefix():", a8.print_prefix())
print("a8.height1():", a8.height1())
print("a8.count_leaf():", a8.count_leaf())
print("a8.print_infix():", a8.print_infix())
exp = EvalExp.EvalExp()
print("exp.evaluate(a8.print_prefix()):", exp.evaluate(a8.print_prefix()))