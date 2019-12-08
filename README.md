# SSEXAM 考试系统

_后端接口 (based on Lin-CMS-Flask)_

## 部署方式

### Server 端必备环境

- 安装`MySQL`（version： 5.6+）

- 安装`Python`环境(version： 3.6+)

### 安装依赖包

有两种方式进行依赖安装，Pipenv或者pip。推荐使用 Pipenv 来创建虚拟环境。关于`Pipenv`的更多使用请参考[Pipenv 官网](https://pipenv.readthedocs.io/en/latest/)。

* 使用 Pipenv 进行安装:

```bash
cd ssexam && pipenv install --dev
```

* 使用 pip 进行安装

```bash
cd ssexam && pip install -r requirements.txt
```

### 数据库配置

打开工程的`app/config/secure.py`，找到如下配置项：

```py
# 数据库配置示例
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/ssexam'
```

请在`SQLALCHEMY_DATABASE_URI`这项中配置 MySQL 数据库的用户名、密码、ip、端口号与数据库名。**请务必根据自己的实际情况修改此配置项**。

> 你所使用的数据库账号必须具有创建数据表的权限，否则无法创建数据表

### 运行

一切就绪后，再次从命令行中使用 Python 命令运行项目根目录下的`starter.py`：

```bash
python starter.py
```

如果你是以 pipenv 创建的虚拟环境，那么请先通过下面命令进入虚拟环境，再运行上面的命令。

```bash
pipenv shell
```

如果一切顺利，你将在命令行中看到项目成功运行的信息。如果你没有修改代码，Lin 将默认在本地启动一个端口号为 5000 的端口用来监听请求。此时，我们访问`http://localhost:5000`，将看到一组字符：

“ssexam"

这证明你已经成功的将后台运行起来了，Congratulations！