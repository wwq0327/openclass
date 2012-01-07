简介
====================================

OpenClass


项目初始化
====================================

- 安装 virtaulenv: 可使用 ``easy_install`` 进行安装。
- 生成项目环境： ``virtualenv openclass`` 。
- 启动虚拟环境： ``source openclass/bin/active`` 。
- 获取项目代码： 进入 ``openclass`` 目录，执行 ``git://github.com/wwq0327/openclass.git`` ，如果没有git，请先安装。
- 安装项目所需模块： 进行项目目录 ``openclass`` ， 执行 ``pip install -r requirements/project.txt`` ，等待模块安装完成。

启动
====================================

开发服务器
------------------------------------
使用的配置文件是 ``settings_local.py`` .

``./dev_manage.py runserver``

生产服务器
------------------------------------
使用的配置文件是 ``settings.py``

``./manage.py runserver``

服务器
====================================

合作
====================================

当被管理员添加到合作者后，可以通过下面操作提交代码：

- 按README所述，创建一个虚拟环境
- pull 代码到本地
- 连接并提交

::

  cd openclass
  git remote add origin git@github.com:wwq0327/openclass.git
  git push -u origin master

就这就OK了。
