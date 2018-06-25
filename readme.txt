çŽ¯å¢ƒå‡†å¤‡ï¼š
python3
<<<<<<< HEAD
pip°²×°selenium£¬unittest
ä¯ÀÀÆ÷Çý¶¯Â·¾¶ÉèÖÃpath»·¾³±äÁ¿

Grid¶à»úÔËÐÐ£º
»·¾³ÒªÇó£º
----±¾µØhubÖ÷»úÓëÔ¶³ÌnodeÖ÷»úÖ±½ÓÄÜpingÍ¨
----Ô¶³ÌÖ÷»úÐè°²×°Java»·¾³
----Ô¶³ÌÖ÷»úÐè°²×°´ý²âä¯ÀÀÆ÷¼°Çý¶¯£¬ÇÒÇý¶¯Òª·ÅÔÚ»·¾³±äÁ¿pathÀï¡£
²Ù×÷²½Öè£º
1¡¢Æô¶¯±¾µØhubÖ÷»ú(±¾µØÖ÷»úIP£º192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role hub
2¡¢Æô¶¯Ô¶³ÌnodeÖ÷»ú(ÉèÖÃ¶Ë¿Ú5555£¬Ö¸ÏòµÄhubÖ÷»úIPÎª192.168.33.86)
	java -jar selenium-server-standalone-2.48.2.jar -role node -port 5555 -hub http://192.168.33.86:4444/grid/register
3¡¢ÐÞ¸ÄÔ¶³ÌÖ÷»úµÄIP¼°¶Ë¿Ú£¬ÔÚÆäÉÏÃæµÄFirefoxÔËÐÐ½Å±¾
=======
pipå®‰è£…seleniumï¼Œunittestï¼Œå³å¯

å¤šæœºè¿è¡Œï¼š
å…ˆå¯åŠ¨java -jar å¯åŠ¨selenium server
>>>>>>> bfdfa4d776867d82aa3c6c2980d9fc5241e90b22
