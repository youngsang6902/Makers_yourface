import telepot

my_token = telepot.Bot('[bot token]')
send_id = [[member1_room_number],[member2_room_number],[member3_room_number],...,[memberN_room_number]]
member = ['[member1 name]','[member2 name]','[member3 name]',...,'[memberN name]']

def send(number):
	
	n = int(number)

	# send a image
	send_img = '[directory name/image file]'
	my_token.sendPhoto(send_id[n], open(send_img,'rb'))

	# send a message
	send_msg = member[n]+'님이 입장하셨습니다.'
	my_token.sendMessage(send_id[n],send_msg)
