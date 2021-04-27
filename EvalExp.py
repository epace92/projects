import stack_list as iset

class EvalExp:
    def __init__(self):
        """ Creates an instance of class EvalExp
            input   -- self : instance of class EvalExp
        """
        self.e = None

    def evaluate(self, e):
        """Evaluates a string parameter and do some maths
            input   -- self: an instance of class EvalExp
                    -- e: string object
            output  -- float: result of the operations in the string object e
        """
        tab = e.split(" ")
        l = iset.StackList()
        for i in tab:
            if len(i) > 1:
                res = False
                for var in i:
                    if 47 < ord(var) < 58:
                        res = True
                if res is True:
                    l.push(float(i))
            elif 47 < ord(i) < 58:
                l.push(float(i))
            elif ord(i) == 42 or ord(i) == 120:
                a = l.mtop.value
                l.pop()
                b = l.mtop.value
                l.pop()
                ans = a * b
                l.push(ans)
            elif ord(i) == 43:
                a = l.mtop.value
                l.pop()
                b = l.mtop.value
                l.pop()
                ans = a + b
                l.push(ans)
            elif ord(i) == 45:
                a = l.mtop.value
                l.pop()
                b = l.mtop.value
                l.pop()
                ans = b - a
                l.push(ans)
            elif ord(i) == 47:
                a = l.mtop.value
                l.pop()
                b = l.mtop.value
                l.pop()
                ans = b / a
                l.push(ans)
        return l.mtop.value