password = 'a123456'
x = 1
while True:
	answer = input('請輸入密碼:')
	if answer == password:
	    print('登入成功！')
	    break
	else:
		if x == 1:
			print('密碼錯誤！還有2次機會')
		elif x == 2:
			print('密碼錯誤！還有1次機會')
		else:
			print('登入失敗 請重新設定密碼')
			break
		x = x + 1



