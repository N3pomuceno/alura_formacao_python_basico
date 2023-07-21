

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if (x1 < x2 and y1 < y2):
            self.SupDireito = (x2, y2)
            self.SupEsquerdo = (x1, y2)
            self.InfDireito = (x2, y1)
            self.InfEsquerdo = (x1, y1)
        elif (x1 < x2 and y1 > y2):
            self.SupDireito = (x2, y1)
            self.SupEsquerdo = (x1, y1)
            self.InfDireito = (x2, y2)
            self.InfEsquerdo = (x1, y2)
        elif (x1 > x2 and y1 < y2):
            self.SupDireito = (x1, y2)
            self.SupEsquerdo = (x2, y2)
            self.InfDireito = (x1, y1)
            self.InfEsquerdo = (x2, y1)
        elif (x1 > x2 and y1 > y2):
            self.SupDireito = (x1, y1)
            self.SupEsquerdo = (x2, y1)
            self.InfDireito = (x1, y2)
            self.InfEsquerdo = (x2, y2)

    def __str__(self):
        return "[{},{}]".format(self.InfEsquerdo, self.SupDireito)

    def __add__(self, other):
        xmin = min(self.InfEsquerdo[0], self.InfDireito[0], other.InfEsquerdo[0], other.InfDireito[0])
        xmax = max(self.InfEsquerdo[0], self.InfDireito[0], other.InfEsquerdo[0], other.InfDireito[0])
        ymin = min(self.InfEsquerdo[1], self.InfDireito[1], other.InfEsquerdo[1], other.InfDireito[1])
        ymax = max(self.InfEsquerdo[1], self.InfDireito[1], other.InfEsquerdo[1], other.InfDireito[1])
        return Rectangle(xmin, ymin, xmax, ymax)


r = Rectangle(3, 5, 1, 2)
s = Rectangle(2, 4, 8, 1)
print(r, s)

print(r + s)

