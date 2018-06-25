#ZBSQ
环境准备：
python3
pip安装selenium，unittest
浏览器驱动路径(./driver)设置path环境变量


========================
Grid多机运行：
环境要求：
----本地hub主机与远程node主机直接能ping通
----远程主机需安装Java环境
----远程主机需安装待测浏览器及驱动，且驱动要放在环境变量path里。
操作步骤：
1、启动本地hub主机(本地主机IP：192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role hub
2、启动远程node主机(设置端口5555，指向的hub主机IP为192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role node -port 5555 -hub http://192.168.33.86:4444/grid/register
3、修改脚本中driver远程主机的IP及端口运行脚本