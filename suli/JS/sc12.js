var szamok = new Array(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21);
var l = szamok.length;
document.write("A szám páros: ", "<br>");
for (i = 0; i < l; i++) {
  if (szamok[i] % 2 == 0) {
    document.write(szamok[i], "<br>");
  }
}

/*1.*/

var db = 0;
for (i = 0; i < l; i++) {
  if (szamok[i] % 2 == 0) {
    db++;
  }
}
document.write("A páros számok száma: ", db, "<br>");

/*2.*/

var osszeg = 0;
for (i = 0; i < l; i++) {
  osszeg += szamok[i];
}
var atlag = osszeg / l;
document.write("A számok átlaga: ", atlag, "<br>");

/*3.*/

if (szamok.includes(50)) {
  document.write("Van 50 a számok között", "<br>");
} else {
  document.write("Nincs 50 a számok között", "<br>");
}

/*4.*/

var index = szamok.findIndex((szam) => szam > 20);
document.write("A legnagyobb 20-nél nagyobb szám indexe: ", index, "<br>");

/*5.*/

var szamokNegyzete = szamok.map((szam) => szam * szam);
document.write("A számok négyzete: ", szamokNegyzete, "<br>");

/*6.*/

var szamok1020 = szamok.filter((szam) => szam > 10 && szam < 20);
document.write("A számok 10 és 20 között: ", szamok1020, "<br>");

/*7.*/

var paros = [];
var paratlan = [];
for (i = 0; i < l; i++) {
  if (szamok[i] % 2 == 0) {
    paros.push(szamok[i]);
  } else {
    paratlan.push(szamok[i]);
  }
}
document.write("Páros számok: ", paros, "<br>");
document.write("Páratlan számok: ", paratlan, "<br>");

/*8.*/

var min = Math.min(...szamok);
document.write("A tömb legkisebb eleme: ", min, "<br>");

/*9.*/

var max = Math.max(...szamok);
document.write("A tömb legnagyobb eleme: ", max, "<br>");
