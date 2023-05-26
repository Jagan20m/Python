#!/usr/bin/env python
# coding: utf-8

# #### List

# In[35]:


data=["yo","hlo","hi"]
data1=["ye","le","dede"]
datas=data+data1
print(datas)


# In[36]:


datas.append("jojo")
print(datas)


# In[32]:


avg_price=[10,110,3,15]
avg_price.sort()
print(avg_price)
avg=avg_price
print(avg)


# In[33]:


products=["z",'x',"a","A"]
products.sort()
print(products)


# In[7]:


products=[31,20,10,14]
prod=sorted(products)
print(prod)


# In[9]:


num=[10,11,2,99,100,47]
num.sort(reverse=True)
print(num)


# In[11]:


avg_price=["hoho","jojo","gogo","hihi"]
print(avg_price[0])


# In[15]:


avg_price=[10,20,30,40]
print(20 not in avg_price)


# In[16]:


avg_price=[10,20,30,40]
print(20 in avg_price)


# In[27]:


data=["jake","hlo","hi","yo"]
for name in data:
    if(name=="hi"):
        break
    print(name)


# In[31]:


prod=[10,2,30,40]
len(prod)


# In[37]:


prod=[10,2,30,40]
max(prod)


# In[38]:


prod=[10,2,30,40]
min(prod)


# In[45]:


name=["jake","charles","hlo","yoyo"]
name.sort()
print(name)


# In[46]:


name=["jake","charles","hlo","yoyo"]
name1=sorted(name)
print(name1)


# In[216]:


prod=["jake","jojo","koko","jake","lala","jake","lala"]
prod.pop("3D Objects")
print(prod)


# In[49]:


num=[10,2,30,40]
print(num)
num.clear()
print(num)
num.append(49)
print(num)


# In[50]:


num=[10,2,30,40]
print(num)
num.append(49)
print(num)


# In[51]:


products=["jake","koko","jake","hoho","jojo"]
products.count("jake")


# In[52]:


num=[1,1,2,3,4,1,4,5,6]
num.count(1)


# In[58]:


dairyprod=["milk","butter","yogurt"]
cheese_item=["Edam","parmesan"]
dairyprod.extend(cheese_item)
print(dairyprod)
dairyprod.index("Edam")


# In[211]:


dairyprod=["milk","butter","yogurt"]
cheese_item=["Edam","parmesan"]
dairyprod.extend(cheese_item)
print(dairyprod)
dairyprod.insert(3,"buttermilk")
print(dairyprod)
dairyprod.pop(3)
print(dairyprod)


# In[208]:


dairyprod=["milk","butter","yogurt"]
dairyprod[0:1]


# #### Tuple

# In[70]:


drinks=("tea","coffee","coldcoffee","milk","frappie")
drinks[0:6:3]


# In[72]:


drinks="tea","coffee","coldcoffee","milk","frappie"
print(drinks)
type(drinks)


# In[74]:


drinks=("tea","coffee","coldcoffee","milk","frappie")
print(drinks)


# In[76]:


age=(30,35,20,10,55)
age.sort() 
print(age)


# In[78]:


age=(30,35,20,10,55)
sorted(age)


# In[79]:


age=(30,35,20,10,55)
sorted(age,reverse=True)


# In[83]:


order=("pizza","coke","milk")
n=2
tot=order*2
print(tot)


# In[90]:


online=("mouse","coverpanel","fan")
offline=("cpu","comp","keyboard")
order=online+offline
print(order)


# In[92]:


book=("jojo","ghoul","one piece")
len(book)


# In[105]:


prices=(10,20,30,40,[200.3])
prices[4].append(50)
print(prices)


# In[107]:


books=("machine learning",20,"big data",30,"library",40)
books[0:5]


# #### Dictionary

# In[116]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
person["zalama"]=35
print(person)


# In[118]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
del person["aka"]
print(person)


# In[126]:


random="damn doom da da da damn jake ja"
wordcount={}
for word in random.split():
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]+=1
print(wordcount)
    


# In[129]:


from collections import defaultdict
random="damn doom da da da damn jake ja"
wordcount=defaultdict(int)
for word in random.split():
    wordcount[word]+=1
print(wordcount)




# In[212]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
len(person)


# In[135]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
str(person)


# In[215]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
person.keys()


# In[137]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
person.values()


# In[139]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
person.items()


# In[141]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
print("age of jake is ",person.get("jake"))


# In[143]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30,}
person.setdefault("gg",60)
print(person)


# In[158]:


tup=("jake","jojo","gg","aka")
tip=("20","30","40","50")
dict1=dict.fromkeys(tup)
print(dict1)
dict2=dict.fromkeys(tup,8)
print(dict2)


# In[160]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
person["jake"]=21
print(person)


# In[162]:


person={"jake":20,"jojo":30,"aka":25,"vegeta":30}
del person["aka"]
print(person)


# In[164]:


person={"jake":30,"jake":20,"jojo":30,"aka":25,"vegeta":30}
print(person)


# In[172]:


prod=["fan","table","chair","computer"]
price=[200,500,600,1000]
tot=dict(zip(prod,price))
print(tot)


# In[185]:


series=[]
for i in range(1,11):
    series.append(i*i)
print(series)


# In[186]:


series=[i*i for i in range(1,11)]
print(series)


# In[188]:


item =[1,2,3,4,5,6]
for elements in item:
    print(elements*2)


# In[192]:


item=[1,2,3,4,5,6]
result=[elements*2 for elements in item]
print(result)


# In[199]:


person=["Jake","Jojo","Aka","Vegeta"]
cap=[v[0] for v in person]
print(cap)


# In[203]:


sentence="i am vengence"
vowels=[vowel for vowel in sentence if vowel in "AEIOUaeiou"]
print(vowels)


# In[ ]:




