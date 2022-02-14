
from math import sqrt,pow

from django.urls import clear_script_prefix

class Point:
   nb=0
   def __init__(self,abs:float=0,ord:float=0) -> None:
       self.__abs=abs
       self.__ord=ord
       Point.nb+=1
   def __str__(self) -> str:
       return f"Point (x={self.__abs},y={self.__ord})"
  # encapsulation
   @property
   def Abs(self)->float:
     return self.__abs
   @Abs.setter
   def Abs(self,new_abs:float)->None:
     self.__abs=new_abs
   @property
   def Ord(self)->float:
     return self.__ord
   @Ord.setter
   def Ord(self,new_ord:float)->None:
     self.__ord=new_ord
   def __eq__(self, p:"Point") -> bool:
       if(self.__abs==p.__abs and self.__ord==p.__ord):
        return True
       else:
        return False
   def calculer_distance(self,p:"Point")->float:
       x=self.__abs-p.__abs
       y=self.__ord-p.__ord
       d=sqrt(pow(x,2)+pow(y,2))
       return d
   @staticmethod
   def calculerDistanceSatique(p1:"Point",p2:"Point")->float:
       x=p1.__abs-p2.__abs
       y=p1.__ord-p2.__ord
       d=sqrt(pow(x,2)+pow(y,2))
       return d
     
    
   def calculer_milieu(self,p:"Point")->"Point":
      x=(self.__abs+p.__abs)/2
      y=(self.__ord+p.__ord)/2
      return Point(x,y)
#Classe TroisPoints
class TroisPoints:
   def __init__(self,point1:"Point",point2:"Point",point3:"Point") -> None:
     self.__point1=point1
     self.__point2=point2
     self.__point3=point3
   @property
   def Point1(self)->"Point":
      return self.__point1
   @Point1.setter
   def Point1(self,p)->None:
    self.__point1=p
   @property
   def Point2(self)->"Point":
      return self.__point2
   @Point2.setter
   def Point2(self,p)->None:
    self.__point2=p
   @property
   def Point3(self)->"Point":
      return self.__point3
   @Point3.setter
   def Point3(self,p)->None:
    self.__point3=p
   def sontAlignee(self)->bool:
    p1p2=self.__point1.calculer_distance(self.__point2)
    p1p3=self.__point1.calculer_distance(self.__point3)
    p2p3=self.__point3.calculer_distance(self.__point2)
    return (p1p2==p1p3+p2p3 or p1p3==p1p2+p2p3 or p2p3==p1p2+p1p3)

   def estIsocele(self)->bool:
        p1p2=self.__point1.calculer_distance(self.__point2)
        p1p3=self.__point1.calculer_distance(self.__point3)
        p2p3=self.__point3.calculer_distance(self.__point2)
        return p1p2==p1p3 or p1p2==p2p3 or p2p3==p1p3
   

