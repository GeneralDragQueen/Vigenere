## Vigenère cipher

### Backstory
In our DnD campaign our GM handed out encrypted diary entries that we tried to decrypt.
Two of our group members discovered the encryption method and the key and I wrote this code, so we wouldn't have to
translate it by hand.  
As it turned out the key was 11 numbers long, changed between some entries but merely rotated when it did. So instead
of 40 million options we only had to look at 11.  
My group members asked me to put this up here - so here we go.

### How to use
An object is always created with its corresponding encrypted text. It can then be decrypted like the following:
```python
def main():
    sample = Vigenere(text="Xv öaolr Tfüsvkge")
    sample.decrypt()  # returns the text
```
Mind that the 'decrypt' function will always call 'key_find' and show you the translation for each individual key.  
The user will then have to put in the corresponding number of the text that makes the most sense to them.  

Alternatively the function 'export_all' will prompt the user to put in the corresponding numbers as above but will
then save all translated texts into a text file.

### Example
```python
sample = Vigenere(text=entries.text1)
print(sample.decrypt())
```
_output 1:_
```
Key 0	|   Text:  Jyiüqäa vjr Püebzopy teöö
Key 1	|   Text:  Zlgxtrm las Bovßurgg jzün
Key 2	|   Text:  Mjbäkßc cbe Rbtyxisä aäoß
Key 3	|   Text:  Keerwtx dru Eßoöouir bmaq
Key 4	|   Text:  Fhzßmky tdh Cyrsäkßs rüro
Key 5	|   Text:  Iühtdlk fuf Ööiaqbae dppj
Key 6	|   Text:  ßkökeöä wsa Asuuhcqu unkm
Key 7	|   Text:  Laslunn und Vaklisch sind
Key 8	|   Text:  Bvtögal pqy Dubmyetf nlep
Key 9	|   Text:  Wwfnxüg shg Xlcükvra qcqf
Key 10	|   Text:  Xivavxj jtä Omsoötmd hogä
Please insert matching number: 
```
The user would (if they understood German) correctly put in _7_.
Let's see what'll happen then:  

_output 2:_
```
Laslunn und Vaklisch sind auf dem Weg in den Steinbruch. Sie haben einige Sklaven bei sich und werden dort unseren Stützpunkt vor den Riesen verteidigen. Solange Aadrushian unter unserer Bezahlung bleibt, sollten wir nichts zu
befürchten haben.

Die Methoden von Gavaksha und Sarpakarna faszinieren mich, sie nutzen als Katalysator fuer ihre Spukerscheinungen die Ängste der Bewohner Ravounel selbst. Dies entzündet eine thaumaturgische Kaskade, ein rekursiver Spruch, der von den Bewohnern der Stadt, von Angst und Gerüchten geschürt wird. Die Sorge in der Bevölkerung vor den Verhandlungen mit Nidal bieten eine perfekte Gelegenheit, ich habe aber auch schon Gerüchte ueber Barzillais Geist und seinen Hunden in der Stadt verbreiten lassen. Theoretisch hat dieser Zauber grenzenloses Potenzial und kann dafür sorgen, dass sich Ravounel selbst zerstört - in jedem Fall wird die Blutrote Triade in den Ruinen Fuss fassen können.

In den folgenden Tagen werden wir unseren Hauptstützpunkt in den verlassenen Tanessenturm der Alabaster Akademie verlegen. Es scheint ein gut geeigneter Unterschlupf zu sein, ist er ruhig genug bei Nacht und bietet schon Schlafplätze für künftige Gefangene.

```


Mind you, I put an absurd number of '\n's in the texts to preserve the original formatting of the entries.