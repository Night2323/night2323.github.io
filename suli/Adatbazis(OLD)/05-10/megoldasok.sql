-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 9. feladat:
CREATE DATABASE tdhongrie
	CHARACTER SET utf8
	COLLATE utf8_hungarian_ci;

-- 11. feladat:
DELETE FROM csapat WHERE id = 21

-- 12. feladat:
SELECT nev FROM versenyzo WHERE nemzetiseg="HUN" ORDER BY nev ASC

-- 13. feladat:
SELECT nemzetiseg, COUNT(nev) AS indulokSzama FROM versenyzo GROUP BY nemzetiseg ORDER BY indulokSzama DESC

-- 14. feladat:
SELECT
  eredmeny.szakasz,
  eredmeny.ido
FROM eredmeny
  INNER JOIN versenyzo
    ON eredmeny.versenyzoId = versenyzo.id
WHERE versenyzo.nev = 'Valter Attila'

-- 15. feladat:
SELECT
  csapat.csapatNev,
  COUNT(versenyzo.id) AS magyarokSzama
FROM versenyzo
  INNER JOIN csapat
    ON versenyzo.csapatId = csapat.id
WHERE versenyzo.nemzetiseg = 'HUN'
GROUP BY csapat.csapatNev
HAVING magyarokSzama>1


