import numpy as np
def isgood(func):
    def wrapper():
        x=('is great at his carreer')
        func()
        return x
class worker:
    def __init__(self,name,experience_year,age):
        self.name=name
        self.experience_year=experience_year
        self.age=age
worker1=worker('Nick',6,27)
worker2=worker('david',24,46)
worker3=worker('diana',4,23)
worker3=worker('jackson',12,32)
array_names=np.array([worker1.name,worker2.name,worker3.name])
experience_years=np.array([worker1.experience_year,worker2.experience_year,worker3.experience_year])
names=array_names.tolist()
experience_yearss=experience_years.tolist()
for name,year in zip(names,experience_yearss):
    print(f'{name}:{year}')