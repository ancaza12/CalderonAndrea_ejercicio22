import math 
class Complejo():
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
        self.norma = math.sqrt(real*real + imaginario*imaginario)

    def conjugado(self):
        self.imaginario = -self.imaginario

    def calcula_norma(self):
        self.norma = math.sqrt(self.real**2 + self.imaginario**2)

    def pow(self, n):
        a = Complejo(self.real, self.imaginario)
        self.calcula_norma()
        r = self.norma ** n
        if abs(self.real)<1E-10:
            theta = math.pi/2.0
        else:
            theta = math.atan(self.imaginario/self.real)
        a.real = r * math.cos(n * theta)
        a.imaginario = r * math.sin(n * theta)
        return a
    
    def multi (self, b):
        a= Complejo(self.real, self.imaginario)

        p1= a.real * b.real
        p2=b.real* a.imaginario
        p3=b.imaginario*a.real
        p4=(a.imaginario* b.imaginario)**2

        self.real=p1 + p4
        self.imaginario = p2 +p3
        
        c= complejo.Complejo(8.0, 6.0)
        d= c.multi(complejo.Complejo(2.0, 2.0))
        
        self.assertEqual(c.real, 0)
        self.assertAlmostEqual(d.imaginario,0)
        
