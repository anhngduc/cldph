import urllib.request
import json
import re
from datetime import datetime

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    urlData = "https://api.chongluadao.vn/v2/blacklist"
    jsonData = getResponse(urlData)
    if (jsonData == ""):
        return 0
    print("update 7onez file")
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    lines = ['# Title: Chong Lua Dao Blacklist (Pihole)', '# Updated: ' + date_time, '# Expires: 1 day (update frequency)','# Homepage: https:chongluadao.vn', '# License: https:chongluadao.vn', '# Source: https:chongluadao.vn', '# Author: Kent Juno','# ---------- Generic Blocking Rules ----------']
    print(lines)
    # with open('CLDBllacklist.7onez', 'w' , encoding="utf-8") as f:
        # f.write('\n'.join(lines))
    
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
    with open('CLDBllacklist.7onez', 'a' , encoding="utf-8") as f:
        f.writelines('\n0.0.0.0 '.join(blacklist))


if __name__ == '__main__':
    main()