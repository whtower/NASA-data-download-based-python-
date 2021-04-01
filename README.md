### 实现原理

用基于**Selenium**使用**Python**驱动**Chromedriver**，在**Chrome**浏览器模拟进行点击下载，避免了直接批量下载过程中可能出现的 需要获取权限 问题。程序能够自主判断文件是否下载完成，没有下载完成自动继续下载，下载完成则退出程序

### 依赖环境

**selenium包**：使用 **pip install selenium** 进行安装

**chromedriver**驱动：在**resource**文件夹中进行复制，然后粘贴到使用的**python**文件夹中，与**python.exe**处于同一文件夹**需要注意的是这里的驱动仅适用于89版本的Chrome浏览器，如果为其他版本浏览器还需自行下载驱动**

**Ghelper**:用于在中国境内顺利连接上NASA下载服务器，需要15.99元/月。具体可直接百度**Ghelper**进入官网

**chrono**:浏览器下载插件，内部调用插件进行下载比默认方式更快

**Ghelper**与**chrono**已经在**resource**文件夹中进行了集成

### 路径说明

**inPutFilePath**为下载链接文件地址，文件样式可以参考file文件夹中的**t.txt**

**outPutFilePath**为保存文件地址

### 内容替换

需要填写 ghelper账号密码
需要填写NASA账号密码
需要填写文件路径等信息

### 使用方法
运行 connect.py