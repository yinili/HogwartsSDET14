def test_env(cmdoption):
    print("环境验证")
    env, datas = cmdoption
    print(f"环境:{env}, 数据: {datas}")
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://' + str(ip) + ":" + str(port)
    print(url)
