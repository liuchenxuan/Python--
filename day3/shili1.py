# 用户身份验证
username = input('请输入用户名：')
password = input('请输入密码：')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！是否忘记了密码')
    wangji = input('y/n:')
    if wangji == 'y':
        anqiumima = input('请输入安全密码:')
        if anqiumima == '123456' or anqiumima == '我不知道':
            print('身份验证成功')
            print('用户名：admin 密码：123456')
            print('请返回至验证页')
            fanhui = input('是否返回验证页（y/n）:')
            if fanhui == 'y':
                username1 = input('请输入用户名：')
                password1 = input('请输入密码：')
                if username1 == 'admin' and password1 == '123456':
                    print('身份验证成功！')
                elif username1 =='草你妈' and password1 =='草泥马':
                    print('恭喜您通过终端验证')
                    print('请访问以下链接')
                    print('https://www.bilibili.com/bangumi/play/ep704334?spm_id_from=333.1007.0.0')
                else:
                    print('身份验证失败！您无法再次进行安全验证！')
            else:
                print('身份验证失败！')
        else:
            print('身份验证失败！您无法再次进行安全验证！')
    elif wangji == '草你妈':
        print('恭喜你通过终端安全验证！')
        print('您可以通过安全密码通道输入以下内容查询网址')
        print('用户名：草你妈 密码：草泥马')
    else:
        print('身份验证失败！')