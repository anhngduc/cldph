import urllib.request
import json
import re
from datetime import datetime

def getResponse():
    print("call api")
    operUrl = urllib.request.urlopen("https:/api.chongluadao.vn/v2/blacklist")
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
        print("Got {} items".format(len(jsonData)))
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    jsonData = getResponse()
    if (jsonData == ""):
        return 0
    lines = ['# Title: Chong Lua Dao Blacklist (Pihole)', '# Expires: 1 day (update frequency)','# Homepage: https:chongluadao.vn', '# License: https:chongluadao.vn', '# Source: https:chongluadao.vn', '# Author: Kent Juno','# ---------- Generic Blocking Rules ----------']
    print(lines)
    with open('CLDBllacklist.7onez', 'w' , encoding="utf-8") as f:
        f.write('\n'.join(lines) + '\n')
    
    blacklist=[]
    
    # print the state id and state name corresponding
    for i in jsonData:
        url = re.compile(r"https?://(www\.)?")
        fin = url.sub('', i["url"]).strip().strip('/')
        fin = fin.replace('*.','')
        fin = fin.replace('/*','')
        fin = fin + ''
        blacklist.append(fin)
    blacklist = list(dict.fromkeys(blacklist))
    print("Black list: {} items".format(len(blacklist)))
    with open('CLDBllacklist.7onez', 'a' , encoding="utf-8") as f:
        f.writelines('0.0.0.0 ' +'\n0.0.0.0 '.join(blacklist))


if __name__ == '__main__':
    main()
