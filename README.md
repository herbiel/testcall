# testcall


### 默认端口8000
### 打包镜像
docker build -t testcall:v1 .
### 运行容器
docker run -d --name=testcall -p8000:8000 testcall:v1 
### 挂载配置文件
docker run -d -vconfig:/app/config --name=testcall -p8000:8000 testcall:v1 
