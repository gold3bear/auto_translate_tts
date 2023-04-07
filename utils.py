def getConfig():
    f = open('.env','r',encoding='utf-8')
    lines =f.read().splitlines()
    configure = {}
    for line in lines:
        key,value = line.split('=')
        configure[key.strip()] = value.strip()
    return configure