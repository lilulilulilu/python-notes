# 1.用docker安装mongo
docker pull mongo:latest
##（1）以不需要密码验证的方式启动mongo
docker run -d -p 27017:27017 --name my-mongo-container mongo
##（2）以需要密码验证的方式启动mongo
docker run -itd -p 27017:27017 --name mongo mongo --auth
docker exec -it mongo mongosh admin
###（2.1）创建管理员用户
db.createUser({ user:'admin',pwd:'mongo666',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
###（2.2）然后就可以用mongosh连上去了
mongosh "mongodb://admin:mongo666@192.168.85.7:27017"


# 2.用Mongo shell连上去创建账号密码
brew install mongosh
mongosh --host 127.0.0.1 --port 27017
show dbs
use admin
db.createUser({ user:'admin',pwd:'mongo666',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});


# 3.执行motor_connection.py,用mongo shell连上去查看
test> show dbs;
admin       132.00 KiB
config      108.00 KiB
local        40.00 KiB
mydatabase   40.00 KiB
test> use mydatabase;
switched to db mydatabase
mydatabase> show collections;
mycollection
mydatabase> db.mycollection.find()
[ { _id: ObjectId('6622dc8e2689323863d6fc55'), name: 'Bob', age: 30 } ]

# 4.启动motor server: python motor_server.py, python motor_client.py测试服务端接口