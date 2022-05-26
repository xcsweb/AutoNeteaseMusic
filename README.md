# 网易云音乐自动签到 + 刷歌
> 网易云音乐自动登录签到 + 刷歌 310 首

## Github Actions 部署指南

### 一、Fork 此仓库
![image-20200727142541791](https://i.loli.net/2020/07/27/jK5H8FLvt7aBeYX.png)


现用cookie 进行签到,变量名为COOKIE 和 CSRFTOKEN

### 三、启用 Action
1. 点击 ***Actions***，再点击 **I understand my workflows, go ahead and enable them**

   ![](https://i.loli.net/2020/07/27/pyQmdMHrOIz4x2f.png)

2. 点击左侧的 ***Star***

   ![image-20200727142617807](https://i.loli.net/2020/07/27/3cXnHYIbOxfQDZh.png)

### 四、查看运行结果
> Actions --> 签到 --> build
>
> 能看到如下图所示，表示成功

![image-20200727143009081](https://i.loli.net/2020/07/27/kvV31BJKYDp9MRm.png)

## 注意事项

1. 每天运行两次，在上午 6 点和晚上 22 点。

2. 可以通过 ***Star*** 手动启动一次。

   ![image-20200727142617807](https://i.loli.net/2020/07/27/87oQeLJOlZvU3Ep.png)
