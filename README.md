# 装备视情UI自动化测试
### 环境准备：
<ol>
<li> 安装python3
<li>pip安装selenium，unittest
<li>浏览器驱动路径(./driver)设置path环境变量
</ol>
***
Grid多机运行
***
环境要求：
<ul>
<li>本地hub主机与远程node主机直接能ping通
<li>远程主机需安装Java环境
<li>远程主机需安装待测浏览器及驱动，且驱动要放在环境变量path里
</ul>
操作步骤：
1.启动本地hub主机(本地主机IP：192.168.33.86)
>>java -jar selenium-server-standalone-2.48.2.jar -role hub
2.启动远程node主机(设置端口5555，指向的hub主机IP为192.168.33.86)
>>java -jar selenium-server-standalone-2.48.2.jar -role node -port 5555 -hub http://192.168.33.86:4444/grid/register
3.修改脚本中driver远程主机的IP及端口运行脚本
