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


### Example
```python
def main():
    sample = Vigenere(text=entries.text1)
    print(sample.decrypt())

if __name__ == "__main__":
    main()
```
_output:_
```
5. Abadius 
Laslunn und Vaklisch sind auf dem Weg in den Steinbruch. Sie haben einige Sklaven bei sich und werden dort unseren Stützpunkt vor den Riesen verteidigen. Solange Aadrushian unter unserer Bezahlung bleibt, sollten wir nichts zu befürchten haben.

Die Methoden von Gavaksha und Sarpakarna faszinieren mich, sie nutzen als Katalysator fuer ihre Spukerscheinungen die Ängste der Bewohner Ravounel selbst. Dies entzündet eine thaumaturgische Kaskade, ein rekursiver Spruch, der von den Bewohnern der Stadt, von Angst und Gerüchten geschürt wird. Die Sorge in der Bevölkerung vor den Verhandlungen mit Nidal bieten eine perfekte Gelegenheit, ich habe aber auch schon Gerüchte ueber Barzillais Geist und seinen Hunden in der Stadt verbreiten lassen. Theoretisch hat dieser Zauber grenzenloses Potenzial und kann dafür sorgen, dass sich Ravounel selbst zerstört - in jedem Fall wird die Blutrote Triade in den Ruinen Fuss fassen können.

In den folgenden Tagen werden wir unseren Hauptstützpunkt in den verlassenen Tanessenturm der Alabaster Akademie verlegen. Es scheint ein gut geeigneter Unterschlupf zu sein, ist er ruhig genug bei Nacht und bietet schon Schlafplätze für künftige Gefangene.

```