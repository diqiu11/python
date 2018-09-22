# python

基于linux搭建时遇到问题，无法push解决如下
error: failed to push some refs to 'git@github.com:diqiu11/python.git' hint: Updates were rejected because the remote contains work that you do 
hint: not have locally. This is usually caused by another repository pushing 
hint: to the same ref. You may wan
以上是报错

因为初始readme文件没有clone到本地
输入解决命令：git pull --rebase origin master