# numberBomb
文艺节使用的数字炸弹游戏，基于Django，CSDN，ChatGPT，bing，文新一言。

## 下载
使用git glone  
```shell
git clone https://github.com/tanqiyuaneric/ScoreBoard.git
```  

## 部署
>需提前安装Python运行环境

``` shell
pip install -r requirements.txt #安装依赖
```

``` shell
python manage.py migrate #创建数据库
```

``` shell
python manage.py collectstatic # 生成静态文件
```  

```shell
python manage.py createsuperuser # 创建管理员账号
```  

### 使用Django的测试服务器部署
（不推荐，但这个方法确实简单）
```shell
python manage.py runserver [本机IP地址:运行端口] # 运行测试服务器
```

将部署地址添加到```numberboom/settings.py```中的```ALLOWED_HOSTS```中
```python
ALLOWED_HOSTS = ['本机IP地址']
```

### 使用标准方法部署
参考：[Django官方文档](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/)


## 部署至公网
使用任意内网穿透服务即可将网站部署至公网  

将公共网域名和地址添加至```numberboom/settings.py```中的```ALLOWED_HOSTS```和```CSRF_TRUSTED_ORIGINS```中
```python
ALLOWED_HOSTS = ['公网域名']
CSRF_TRUSTED_ORIGINS = ['公网地址']
```

## URL结构
| 地址       | 功能                 |
|----------|--------------------|
| /        | 主页&计分板             |
| /admin   | Django数据库管理，用于管理游戏 |

## 使用方法
### 创建比赛
