
const tantargyak = ["matek", "magyar", "töri", "matek", "töri", "magyar", "matek", "magyar", "töri", "töri", "magyar", "matek"];
const szavazatok = {};
for (const tantargy of tantargyak) {
  if (!szavazatok[tantargy]) {
    szavazatok[tantargy] = 0;
  }
  szavazatok[tantargy]++;
}
const eredmeny = Object.entries(szavazatok).sort((a, b) => b[1] - a[1]);
for (const [tantargy, szavazat] of eredmeny) {
  alert(`${tantargy}: ${szavazat}`);
}
```

2.
```
const bruttok = [300000, 400000, 500000, 600000, 700000];

// a)
alert(`a) ${bruttok.length} programozó dolgozik a cégnél.`);

// b)
const osszeg = bruttok.reduce((sum, brut) => sum + brut, 0);
const atlag = osszeg / bruttok.length;
alert(`b) Az átlagfizetésük: ${atlag}`);

// c)
const max = Math.max(...bruttok);
alert(`c) A legmagasabb bér: ${max}`);

// d)
const min = Math.min(...bruttok);
alert(`d) A legalacsonyabb bér: ${min}`);

// e)
const kulonbseg = max - min;
alert(`e) A különbség a legmagasabb és a legalacsonyabb között: ${kulonbseg}`);

// f)
const netto = [];
for (const brut of bruttok) {
  const jovedelemado = brut * 0.15;
  const tarsadalombiztositasi = brut * 0.185;
  const szocialis = brut * 0.13;
  const adok = jovedelemado + tarsadalombiztositasi + szocialis;
  const nett = brut - adok;
  netto.push(nett);
}
alert(`f) A nettó bérek: ${netto}`);
