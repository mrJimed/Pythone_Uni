import threading
import urllib
import requests
import json
import sys
import subprocess


class Pair:
    name = ''
    text = ''
    def __init__(self, name, text):
        self.name = name
        self.text = text


def openJson():
    with open('data.json') as json_file:
        data = json.load(json_file)
        json_file.close()
        return data

def saveJson(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()


def openSCSS(path):
    with open(path) as file:
        data = file.read()
        file.close()
    return data

def saveSCSS(jsonStyle, path):
    data = openSCSS(path)
    with open('style.scss', 'w') as save:
        save.write(jsonStyle['style'] + "\n" + data)
        save.close()

def createSCSS(path):
    data = openSCSS(path)
    with open('style.scss', 'w') as save:
        save.write(data)
        save.close()


def saveToCss(scssF):
    with open('style.css', 'w') as save:
        save.write(scssF)
        save.close()


def openHTML():
    with open('index.html', 'r', encoding="utf-8") as file:
        data = file.readlines()
        file.close()
    return data

def createHTML():
    pair = []
    with open('style.css') as file:
        data = file.readlines()
        file.close()
    name = ''
    txt = ''
    b = False
    for i in range(len(data)):
        if(data[i].find('{') >= 0):
            b = True
            name+=data[i].split(' {')[0]
            continue
        elif(data[i].find('}') >= 0):
            b = False
        if(b):
            txt += data[i].split('\n')[0] + ' '
        else:
            if(name != '' and txt != ''):
                pair.append(Pair(name, txt))
            name = ''
            txt = ''
    htmlF = openHTML()
    newHTNL=''
    tf = False
    for i in range(len(htmlF)):
        for k in range(len(pair)):
            if(htmlF[i].find(pair[k].name) >= 0):
                tf=True
                for d in range(len(htmlF[i])):
                    if((htmlF[i])[d] != '>'):
                        newHTNL += (htmlF[i])[d]
                    elif((htmlF[i])[1] != '/' and (htmlF[i])[d] != '/'):
                        newHTNL += " style=\"" +pair[k].text + "\">"
                    elif((htmlF[i])[1] == '/'):
                        newHTNL+=">"
        if(tf == False):
            newHTNL+=htmlF[i]
        tf = False
    saveHTML(newHTNL)

def saveHTML(htmlFile):
    with open('newIndex.html', 'w', encoding="utf-8") as save:
        save.write(htmlFile)
        save.close()




if len(sys.argv) == 1:
    path = 'style.scss'
else:
    path = sys.argv[1]
    createSCSS(path)

jsonStyle = requests.get('https://0x72.ml/files/style.json').json()
saveJson(jsonStyle)
# jsonStyle = openJson() #- если нельзя загрузить файл

saveSCSS(jsonStyle, path)
saveToCss(subprocess.run('sass style.scss', shell=True).stdout)

urllib.request.urlretrieve('http://www.websovet.com/50-besplatnyx-shablonov-sajtov-na-html5-i-css3', 'index.html')
createHTML()