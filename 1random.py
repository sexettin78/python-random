import random
x=21
y=9
dizi = ['furkan','d','leafyet','yazılım','siber']
random.random() #0.0-1.0 arası rastgele sayı üretir. üretilen sayılar float değerindedir

random.uniform(x,y) #belirtilen parametreler arasında sayı üretir. float türünde üretir

random.randint(x,y) #belirtilen aralıkta sayı üretir. üretilen sayı int türündedir

random.choice() #dizi içinden rastgele eleman seçer

random.shuffle() #belirtilen dizideki elemanları rastgele dağıtır. sıra değiştirir

random.randrange(4) #4 sayısı dahil olmadan 4 sayısına kadar değer üretir. int türündedir

random.sample(dizi,5) #diziden 5 elemanı rastgele seçer

