var number;
  while (!isFinite(number)){
     number=prompt('kérek egy számot: ')
  }
  document.write('A megadott szám: ', number)

var number=1;
  do{
    number=prompt('kérek egy számot: ')
  }
  while (!isFinite(number))
  document.write('A megadott szám: ', number)