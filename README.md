# Healing_time
Recommend healing time space to users

# Project Flow
1. Save Healing Time shops' data that collected by using crowling about naver, daum
2. Customer requests serveice by sending KakaoTalk message
3. The message is sended to AWS EC2 Ubuntu Server(Backend) and We understand the intent of message by Google Dialog Flow model
4. We get information that Customer want from AWS RDS and return it to Customer by KakaoTalk message
5. The steps so far are available 24 hours a day
