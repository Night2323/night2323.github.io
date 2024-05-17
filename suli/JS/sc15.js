
var szam = prompt("Kérek egy számot: ")
document.write("A szám: ",szam,"<br>")

function dupla(szam){
var ertek=szam*2
document.write("A szám kétszerese: ",ertek)
}
dupla(szam)
```

Függvény:
```
var szam = prompt("Kérek egy számot: ")
document.write("A szám: ",szam,"<br>")
function dupla(szam){
  var ertek=szam*2
return ertek
}
document.write("A szám kétszerese: ",dupla(szam))
```

2.) a) Testtömegindex kiszámítása:
```
function bmi(suly,magassag){
  var bmi=suly/(magassag*magassag)
  return bmi
}
```

b) Négyzet alapú gúla térfogatának kiszámítására:
```
function gula(a,m){
  var terfogat=(a*a*m)/3
  return terfogat
}
```

c) Számolja meg a felhasználótól bekért szövegben az "a" betűket:
```
function aSzamlalo(szoveg){
  var db=0
  for(var i=0;i<szoveg.length;i++){
    if(szoveg.charAt(i)=="a"){
      db++
    }
  }
  return db
}
