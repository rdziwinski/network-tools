# Free pools
Instrukcja obsługi:
1. Wchodzimy na birda, wykonujemy poniższą komendą i jej wynik wklejamy do pliku znajdującego się w tym samym katalogu co plik free-pools.py
```sh
show route where net ~ 79.110.192.0/20
```
2. Uruchamiamy program.
```sh
python3 free-pools.py nazwa_pliku
```
3. Program zwróci nam następujący wynik:
```sh
192.168.1.64/26
                  | Free: 192.168.1.128/?
192.168.1.192/26
```
Po lewej stronie mamy pule które są zajęte i "otaczają" wolną pulę która jest po prawej stronie. Maskę musimy dobrać sami ponieważ program ten szuka nieciągłości w pulach które są założone.

Na razie działa tylko na adresach zaczynających się na 79.110 co widać w kodzie programu można to zmienić edytując plik *.py. Łatwiejszą edycję dodam w przyszłości.
