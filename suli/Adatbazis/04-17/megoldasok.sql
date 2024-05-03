A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


1. feladat:
CREATE DATABASE teke
	CHARACTER SET utf8
	COLLATE utf8_hungarian_ci;

3. feladat:
SELECT
  versenyzok.nev
FROM versenyzok
WHERE versenyzok.korcsop = 'A'
ORDER BY versenyzok.nev

4. feladat:
SELECT
  eredmenyek.versenyzo
FROM eredmenyek
WHERE eredmenyek.ures > 0
GROUP BY eredmenyek.versenyzo

5. feladat:
SELECT
  versenyzok.nev,
  AVG(eredmenyek.tarolas) AS atlagpont
FROM eredmenyek
  INNER JOIN versenyzok
    ON eredmenyek.versenyzo = versenyzok.rajtszam
GROUP BY versenyzok.nev
ORDER BY atlagpont DESC

6. feladat:
SELECT
  egyesuletek.nev,
  COUNT(versenyzok.nev) AS Versenyzők
FROM versenyzok
  INNER JOIN egyesuletek
    ON versenyzok.egyid = egyesuletek.id
GROUP BY egyesuletek.nev
ORDER BY Versenyzők DESC
LIMIT 1

7. feladat:
SELECT
  versenyzok.nev,
  SUM(eredmenyek.tarolas + eredmenyek.teli) AS eredmeny,
  SUM(eredmenyek.tarolas) AS tarolas,
  SUM(eredmenyek.ures) AS ures
FROM versenyzok
  INNER JOIN eredmenyek
    ON eredmenyek.versenyzo = versenyzok.rajtszam
WHERE versenyzok.korcsop = 'B'
GROUP BY versenyzok.nev
ORDER BY eredmeny DESC, tarolas DESC, ures
