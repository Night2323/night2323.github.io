-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 8. feladat:
CREATE DATABASE konyvtarak2
	CHARACTER SET utf8
	COLLATE utf8_hungarian_ci;

-- 10. feladat:
UPDATE megyek 
SET megyek.megyeNev="Budapest" 
WHERE megyek.megyeNev="BP";

-- 11. feladat:
SELECT
  konyvtarak.konyvtarNev,
  konyvtarak.irsz
FROM konyvtarak
WHERE konyvtarak.konyvtarNev LIKE "%Szakkönyvtár%"

-- 12. feladat:
SELECT
  konyvtarak.konyvtarNev,
  konyvtarak.irsz
FROM konyvtarak
WHERE konyvtarak.irsz LIKE '1%'
ORDER BY konyvtarak.irsz ASC

-- 13. feladat:
SELECT
  telepulesek.telepNev,
  COUNT(konyvtarak.konyvtarNev) AS konyvtarDarab
FROM konyvtarak
  INNER JOIN telepulesek
    ON konyvtarak.irsz = telepulesek.irsz
GROUP BY telepulesek.telepNev
HAVING COUNT(konyvtarak.konyvtarNev) >= 7

-- 14. feladat:
SELECT
  megyek.megyeNev,
  COUNT(DISTINCT telepulesek.telepNev) AS telepulesDarab
FROM konyvtarak
  INNER JOIN telepulesek
    ON konyvtarak.irsz = telepulesek.irsz
  INNER JOIN megyek
    ON telepulesek.megyeId = megyek.id
WHERE telepulesek.irsz NOT LIKE '1%'
GROUP BY megyek.megyeNev
ORDER BY telepulesDarab DESC

