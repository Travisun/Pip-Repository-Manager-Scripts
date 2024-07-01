# Python Pip Repository Manager Scripts

这是基于 Python、Shell、PowerShell 一起编写的Pip源一键切换脚本，即便Pip源的手动切换步骤已经足够简洁了。
但我发现每次配置新环境或者遇到网络问题时，都需要切换一下源，因此就会重复做下列操作：

1. 从Baidu或者Google搜索引擎搜索关键词`Pip国内源`
2. 然后从众多查询结果中挑选一个可靠的网页，点击打开
3. 遇到一个不熟悉的网页还要仔细查找一会儿，找到源地址后再复制下载
4. 进入Python环境下，输入一堆陌生的命令来更改源设置
5. 如果一个源不那么可靠（可能是你网络问题），那么还得再次切换

不知道你是否是这样操作进行切换，或者你已经熟记了各大源服务的网址。但无论如何，
我从开始计划到实施，总共花费了4小时，来让这个小工具诞生了。你只需要执行简短的命令，即可再各大源之间灵活切换，
特别的，我还未这个脚本工具增加了测速功能，这样你可以始终选择最快速的源。

## Windows 切换Pip源
打开你的 PowerShell 窗口, 注意不是 CMD装口或Windows Terminal窗口，执行这一行代码即可：
```shell
irm https://sh.evzs.com/prm | iex
```

## Linux/MacOS 切换Pip源
直接进入你的操作系统上的命令行窗口，执行下列代码即可：
```shell
curl -s https://sh.evzs.com/prm/ | bash
```

## 切换指引
执行命令后将进入下列选项表：
```shell
{Python Pip Repository Manager}

目前可用的 Python Pip 源服务：

1. 清华大学: https://pypi.tuna.tsinghua.edu.cn/simple/ (延迟: 196.88 ms)
2. 中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple/ (延迟: 159.47 ms)
3. 华为云: https://repo.huaweicloud.com/artifactory/pypi-public/simple/ (延迟: N/A)
4. 腾讯云: https://mirrors.cloud.tencent.com/pypi/simple/ (延迟: 414.42 ms)
5. 阿里云: https://mirrors.aliyun.com/pypi/simple/ (延迟: 104.24 ms)
6. Pip官方源: https://pypi.python.org/simple/ (延迟: 7785.45 ms)

q. 退出

请选择一个 Python Pip 源 (输入序号) 或 输入 'q' 退出:
```
此时你只需要根据连接情况或你的偏好，选择一个编号，然后回车(Enter)即可完成切换。

Enjoy it😊!

## 协议授权
此项目遵循 MIT 协议，免费使用并且后果自担，不提供任何保障和维修，同时禁止将本项目用于任何非法目的。