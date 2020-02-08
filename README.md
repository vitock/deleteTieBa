
## 感谢 rmb122 的项目 [Delete-my-hisroy-in-tieba](https://github.com/rmb122/Delete-my-hisroy-in-tieba  ) 
在此基础上做了一些改动，不需要 vps ，借助免费的Travis 每天/周自动运行
## Step0 fork 本项目到你自己的github

## Step1 提取cookie
使用Chrome 的 [EditThisCookie][2] 插件, 可以直接导出 JSON 下的 Cookie  ，保存在项目目录，文件名为 
cookie.json

然后在终端运行 (提前安装python3 )
```python
pip install -r requirements.txt // 第一次运行需要
python3 test.py
```
会自动生成加密的cookie信息，记住终端中打印的加密的key留作下一步使用
![](./travis0.png)

```
git add .
git commit "cookie"
git push origin master
```
然后推送到github。

## 注册 [Travis](https://travis-ci.org ) (可能要翻墙)
然后在控制面板中 点击 "+"链接你的项目
如图 <br>
![](./travis1.png)


## 添加环境变量
点击项目，看右边进入设置

![](./travis2.png)


### 添加环境变量和定时任务
![](./travis3.png)
---


<br>

<br>
<br>
<br>
  
  
## config.json

相当于设置, 不同项对应不同的行为, 其中  
`thread` 对应主题帖  
`reply` 对应回复  
`followedBa` 对应关注的吧  
`concern` 对应关注  
`fans` 对应粉丝  
  
例如将  
```json
"thread": {
        "enable": true,
        "start": 1,
        "end": 5
    },
```
改为  
```json
"thread": {
        "enable": false,
        "start": 2,
        "end": 6
    },
```
后, 将不会删除主题帖, 且删除范围将从在 [http://tieba.baidu.com/i/i/my_tie](http://tieba.baidu.com/i/i/my_tie) 的 `1-5` 页变为 `2-6` 页  
其他同理, 默认全部开启, 在删除完后可以自行调整关闭, 加快速度.  

~~帖子多的话可以放在 vps 上每天自动运行, 加入到计划任务中就可以啦~~

PS: 记得根据自己的情况调整在文件中的搜索回复贴子的起始和结束页码 (百度有各种奇葩的 bug)  
PS2: 觉得好用的话点个 `Star` 吧 \_(:з」∠)\_  
~~PS3: 还有疑问, 或者遇到 `bug` 的话可以在 `issues` 里提出, 有空的话我会尽量解决的~~

[1]: https://sites.google.com/a/chromium.org/chromedriver/downloads
[2]: https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg
[3]: https://github.com/rmb122/Delete-my-hisroy-in-tieba/blob/master/Guide.md
