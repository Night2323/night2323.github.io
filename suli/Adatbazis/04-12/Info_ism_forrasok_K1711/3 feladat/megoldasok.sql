A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!

1. feladat:

CREATE DATABASE varosok
	CHARACTER SET utf8
	COLLATE utf8_hungarian_ci;

3. feladat:

SELECT
  varos.vnev
FROM varos
WHERE varos.vnev = "%vásár%"

4. feladat:

SELECT
  varos.vnev,
  varos.nepesseg,
  varos.terulet
FROM varos
WHERE varos.terulet >= 400

5. feladat:

SELECT
  varos.vnev,
  varos.nepesseg
FROM varos
  INNER JOIN megye
    ON varos.megyeid = megye.id
WHERE megye.mnev = 'Fejér'
AND varos.nepesseg >= 15000

6. feladat:

SELECT
  varostipus.vtip AS `Városok típusa`,
  COUNT(varos.id) AS `Városok száma`,
  SUM(varos.nepesseg) AS Népesség
FROM varos
  INNER JOIN megye
    ON varos.megyeid = megye.id
  INNER JOIN varostipus
    ON varos.vtipid = varostipus.id
WHERE varostipus.vtip <> "Főváros"
GROUP BY varostipus.vtip

7. feladat:

