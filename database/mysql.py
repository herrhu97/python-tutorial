

#!/usr/bin/python3

import pymysql

# 注意把password设为你的root口令:
conn = pymysql.connect(host='t', user='root', password='123456', database='test')
cursor = conn.cursor()

# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Herrhu'])

print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
