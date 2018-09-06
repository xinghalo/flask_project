
修改setup.py、MANIFEST.in、.gitignore中所有your-project-name，替换为自己的项目名字

# 打包

sh deploy.sh

# 启动

python run.py -m 'test'

自动获取对应环境下的参数

# 待解决问题

- uwsgi的使用和切换
- egg_info的调研

# 参考

- setuptools：https://setuptools.readthedocs.io/en/latest/setuptools.html#id35
- setuptools csdn:https://blog.csdn.net/pfm685757/article/details/48651389
- setuptools 伯乐在线:http://python.jobbole.com/87240/