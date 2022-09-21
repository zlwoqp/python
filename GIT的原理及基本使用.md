# GIT的原理及基本使用

## 一、Git简述

### 1、Git的定义

Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。 也是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。

### 2、Git的优点

（1）适合分布式开发，强调个体

（2）公共服务器压力和数据量都不会太大

（3）速度快，灵活性高

（4）任意两个开发人员更容易冲突；5、离线工作

### 3、Git的缺点

代码保密性差，一旦开发者把整个库克隆下来，就可以公开所有版本和版本信息

## 二、Git的工作原理

### 1、分层操作

（1）git的工作总共分四层

远程仓库(Remote)、本地仓库(Repository)、暂存区(index/Stage)和工作目录(workspace)。其中本地仓库、暂存区和工作目录这三层是在自己本地也就是git仓库进行的。远程仓库是在中心服务器上进行的。

（2）远程仓库(Remote)

托管代码的服务器。它位于中心服务器，我们做好工作之后将其推送到远程仓库，或者从远程仓库更新下来最新代码到本地。

（3）本地仓库(Repository)

位于.git目录下，是安全存放数据的位置，里面有提交所有版本的数据，其中HEAD指向最新放入仓库的版本。

（4）暂存区(index/Stage)

位于.git目录下，实际上是一个文件，用于保存即将提交到文件列表的信息。

（5）工作目录(workspace)

我们执行命令git init时所在的地方，也就是我们执行一切文件操作的地方。

![](https://img-blog.csdn.net/20171129100040582?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWF5Zmxh/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

### 2、Git文件状态：

（1）Untracked：未跟踪，在此文件夹中，但没有加到git库，不参与版本控制，通过git add状态变为staged。
（2）Unmodified：文件已经入库，未修改，即版本库中的文件快照内容与文件夹一致这种类型的文件有两种取出，如果被修改，变为modified，如果被移除版本库git rm，变为Untracked。
（3）Modified：文件已被修改，这个文件有两个去处，第一个是staged，第二个是unmodified。
（4）Staged：执行git commit 则将修改同步到库中，这时库中的文件和本地文件虽为一致，文件为Unmodified。执行git reset HEAD filename取消暂存，文件状态为modified。

![](https://img-blog.csdnimg.cn/c11737a642fd4f238d9b6ff9830c3e3d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA5Liq54Ot54ix5a2m5Lmg55qE5rex5bqm5rij5rij,size_10,color_FFFFFF,t_70,g_se,x_16)

## 三、Git的基本使用

### 1、配置信息

```
配置用户名：git config --global user.name"xxx"
配置邮箱：git config global user.email"xxx"
配置大小写敏感：git config --global core.ignorecase false
查看配置信息：git config --list
```

### 2、初始化本地仓库

```
git init   #将本地文件夹变成一个本地仓库
ll -ah     #可以看到.git隐藏文件夹
```

### 3、新增一个文件

```
git add text.txt                    #新增一个文件
git commit -m "add a text.txt"      #提交信息
```

### 4、如果提交新版本后有bug，退回版本

```
git log                        #查看提交的日志
git reset --head Head^         #回退到上个版本，^表示回退几个版本（如果已经commit，需要这样回退）
```

### 5、分支与标签管理

```
git checkout -b  dev      #创建dev分支
git branch                #查看当前分支
git checkout master       #切换到master分支
git merge dev             #将dev分支合并到当前分支
git branch -d dev         #删除dev分支
```

### 6、设置别名

```
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit          #git commit 对应 git ci
git config --global alias.unstage 'reset HEAD --'     # git reset HEAD 对应git unstage
git merge iss53                     #将 iss53  分支合并到当前分支
git mergetool                       #启动图形化的合并工具
```

### 7、SSH公钥

（1）首先，在Mac上 ，默认情况下，用户的 SSH 密钥存储在其 `~/.ssh` 目录下，带pub扩展名的就是公钥

```
cd ~/.ssh/           #若没有该文件夹，则会提示No such file or directory，则表明无此配置。若有该文件夹，会进入到文件夹中，此时使用ls查看文件夹内容。
ls
id_rsa      id_rsa.pub  known_hosts
```

（2）其次，如果没有，就需要新建一个

```
ssh-keygen -o  
Generating public/private rsa key pair.
Enter file in which to save the key (/home/schacon/.ssh/id_rsa):
Created directory '/home/schacon/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/schacon/.ssh/id_rsa.
Your public key has been saved in /home/schacon/.ssh/id_rsa.pub.
The key fingerprint is:
```

 ssh-keygen 会确认密钥的存储位置（默认是 .ssh/id_rsa），需要我们输入两次密钥口令。 如果我们不想在使用密钥时输入口令，将其留空即可。 然而，如果我们使用了密码，需要确保添加了 -o 选项，它会以比默认格式更能抗暴力破解的格式保存私钥。 我们也可以用 ssh-agent 工具来避免每次都要输入密码。
