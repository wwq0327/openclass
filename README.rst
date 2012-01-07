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
