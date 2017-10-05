#Manage wifi router thrue http interface
#If my Ip4 not 92.xx.xx.xx or not 87.xx.xx.xx then reboot
#provider dhcp 92... and 87... white, over ip grey.  

import requests
from time import sleep
import mydata


def getIp():
	with requests.Session() as sess:
		r= sess.get(mydata.statusUrl, auth=(mydata.login, mydata.psw))
		if r.status_code==200:
			s = r.text
			posMac= s.find(mydata.mac)
			posstartIp = posMac+21
			posEndIp = s.find("\"",posstartIp, posstartIp+16)
			return s[posstartIp:posEndIp:1]

def changeIp():

	requests.get(mydata.DisconnectUrl, auth=(mydata.login, mydata.psw))
	sleep(6)
	requests.get(mydata.ConnectUrl, auth=(mydata.login, mydata.psw))
	sleep(6)


def main():
	print ('Program is started')

	while True:
		myIp = getIp()
		print (myIp)
		indexIp =myIp[0:2]
		if indexIp =='92' or indexIp =='87':
			sleep(240)
		else:
			changeIp()


if __name__ == "__main__":
	main()
