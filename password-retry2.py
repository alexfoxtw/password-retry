password = 'a123456'
x = 3
while True:
	x = x - 1
	pw = input('請輸入密碼:')
	if pw == password:
		print('登入成功！')
		break
	else:
		if x == 0:
			print('登入失敗 請重新設定密碼')
			break
		else:
			print('密碼錯誤！還有', x ,'次機會')
		