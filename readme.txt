����׼����
python3
pip��װselenium��unittest
���������·������path��������

Grid������У�
����Ҫ��
----����hub������Զ��node����ֱ����pingͨ
----Զ�������谲װJava����
----Զ�������谲װ�����������������������Ҫ���ڻ�������path�
�������裺
1����������hub����(��������IP��192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role hub
2������Զ��node����(���ö˿�5555��ָ���hub����IPΪ192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role node -port 5555 -hub http://192.168.33.86:4444/grid/register
3���޸�Զ��������IP���˿ڣ����������Firefox���нű�
