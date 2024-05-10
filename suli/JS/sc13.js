let tomb = [];
while (tomb.length < 5) {
  let szam = Math.floor(Math.random() * 90) + 1;
  if (!tomb.includes(szam)) {
    tomb.push(szam);
  }
}
