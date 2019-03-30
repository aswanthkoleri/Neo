from googletrans import Translator

class Translate():
    def translateMsg(self,msg):
        result = ""
        translator = Translator()
        data = translator.translate(msg)
        if(data.text):
            result += "**Text** : "+data.text
            result += '\n'
        if(data.pronunciation):
            result += "**Pronunciation** : "+data.pronunciation
        if((data.text==None) and (data.pronunciation==None)):
            result += "Couldn't translate :("
        return result

if __name__ == "__main__":
    n = Translate()
    r = n.translateMsg('안녕하세요.')
    print(r)