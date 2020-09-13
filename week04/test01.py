import pandas as pd
import numpy as np
import os


sales = [{'id': 101,'account': 'Jones LLC','order_id':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'id': 1003,'account': 'Alpha Co01','order_id':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 104,'account': 'Alpha Co02','order_id':'c',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 10,'account': 'Alpha Co03','order_id':'c',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 13,'account': 'Alpha Co04','order_id':'c',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 104,'account': 'Alpha Co9','order_id':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 1003,'account': 'Alpha Co6','order_id':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'id': 102,'account': 'Blue Inc','order_id':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df = pd.DataFrame(sales)
df1 = pd.DataFrame(sales)
df2 = pd.DataFrame(sales)

# 1. SELECT * FROM data;
print(df)
# 2. SELECT * FROM data LIMIT 10;
print(df[1:3])
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(df['id'])
# 4. SELECT COUNT(id) FROM data;
print(df['id'].count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[ (df['id'] > 30) & (df['id'] < 1000) ])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(df.groupby('id').nunique().iloc[:, [1]])
exit()
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(df1, df2, on='id'))
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([df1, df2]))
# 9. DELETE FROM table1 WHERE id=10;
print(df [  df['id'] != 10 ])
# 10. ALTER TABLE table1 DROP COLUMN column_name;
#print(df.drop( 'column_name' ,axis = 1))
print(df.drop( 'Jan' ,axis = 1))