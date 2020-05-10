from django.db import models
import numpy as np
import os
import matplotlib 
import matplotlib.pyplot as plt
from PIL import Image
# Create your models here.

path=r"F:\pilot_workflow"
os.chdir(path)
def read_files(y,p):
    #entry="F:/pilot_workflow/AOD/"+ p+"/"+y
    wpath=os.path.join(path,p)
    wpath=os.path.join(wpath,y)
    a=os.listdir(wpath)
    data=[]
    for i in a:
        img=Image.open(os.path.join(wpath,i))
        img.load()
        a=(np.asarray(img))/255
        data.append(a)
    return data


def average_data(a):
    avg=[]
    for i in a:
        avg.append((np.average(i)))
    return avg
    
#For Delhi
del_17=read_files("2017","Delhi")
avg_del_17=average_data(del_17)
del_18=read_files("2018","Delhi")
avg_del_18=average_data(del_18)
del_19=read_files("2019","Delhi")
avg_del_19=average_data(del_19)
del_20=read_files("2020","Delhi")
avg_del_20=average_data(del_20)

y=np.arange(1,9)
plt.plot(y,avg_del_17,label="2017")
plt.plot(y,avg_del_18,label="2018")
plt.plot(y,avg_del_19,label="2019")
plt.plot(y,avg_del_20,label="2020")
locs, labels = plt.xticks()
plt.xticks(np.arange(0, 9, step=1))
plt.xticks(np.arange(8), ('feb26-5march', '6march-13mearch', '14mearch-21march', '22march-29march', '30march-6april','7april-14april','15april-22april','23april-301april'),rotation=30)
plt.ylabel("AOD")
plt.title("DELHI- Values of AOD")
img = plt.legend()
plt.imsave("templates/mainsite/pics/aod/Delhi_AOD.png", img)

#For Mumbai
mum_17=read_files("2017","Mumbai")
avg_mum_17=average_data(mum_17)
mum_18=read_files("2018","Mumbai")
avg_mum_18=average_data(mum_18)
mum_19=read_files("2019","Mumbai")
avg_mum_19=average_data(mum_19)
mum_20=read_files("2020","Mumbai")
avg_mum_20=average_data(mum_20)
y=np.arange(1,9)
plt.plot(y,avg_mum_17,label="2017")
plt.plot(y,avg_mum_18,label="2018")
plt.plot(y,avg_mum_19,label="2019")
plt.plot(y,avg_mum_20,label="2020")
locs, labels = plt.xticks()
plt.xticks(np.arange(0, 9, step=1))
plt.xticks(np.arange(8), ('feb26-5march', '6march-13mearch', '14mearch-21march', '22march-29march', '30march-6april','7april-14april','15april-22april','23april-301april'),rotation=30)
plt.ylabel("AOD")
plt.title("MUMBAI- Values of AOD")
img = plt.legend()
plt.imsave("templates/mainsite/pics/aod/Mumbai_AOD.png", img)

#For Kolkata
kol_17=read_files("2017","Kolkata")
avg_kol_17=average_data(kol_17)
kol_18=read_files("2018","Kolkata")
avg_kol_18=average_data(kol_18)
kol_19=read_files("2019","Kolkata")
avg_kol_19=average_data(kol_19)
kol_20=read_files("2020","Kolkata")
avg_kol_20=average_data(kol_20)
y=np.arange(1,9)
plt.plot(y,avg_kol_17,label="2017")
plt.plot(y,avg_kol_18,label="2018")
plt.plot(y,avg_kol_19,label="2019")
plt.plot(y,avg_kol_20,label="2020")
locs, labels = plt.xticks()
plt.xticks(np.arange(0, 9, step=1))
plt.xticks(np.arange(8), ('feb26-5march', '6march-13mearch', '14mearch-21march', '22march-29march', '30march-6april','7april-14april','15april-22april','23april-301april'),rotation=30)
plt.ylabel("AOD")
plt.title("Kolkata- Values of AOD")
img = plt.legend()
plt.imsave("templates/mainsite/pics/aod/Kolkata_AOD.png", img)

#For Chennai
y=np.arange(1,9)
plt.plot(y,avg_che_17,label="2017")
plt.plot(y,avg_che_18,label="2018")
plt.plot(y,avg_che_19,label="2019")
plt.plot(y,avg_che_20,label="2020")
locs, labels = plt.xticks()
plt.xticks(np.arange(0, 9, step=1))
plt.xticks(np.arange(8), ('feb26-5march', '6march-13mearch', '14mearch-21march', '22march-29march', '30march-6april','7april-14april','15april-22april','23april-301april'),rotation=30)
plt.ylabel("AOD")
plt.title("Chennai- Values of AOD")
plt.legend()
plt.plot(y,avg_che_20,label="2020",color="red")
locs, labels = plt.xticks()
plt.xticks(np.arange(0, 9, step=1))
plt.xticks(np.arange(8), ('feb26-5march', '6march-13mearch', '14mearch-21march', '22march-29march', '30march-6april','7april-14april','15april-22april','23april-301april'),rotation=30)
plt.ylabel("AOD")
plt.title("Chennai- Values of AOD")
img = plt.legend()
plt.imsave("templates/mainsite/pics/aod/Chennai_AOD.png", img)


