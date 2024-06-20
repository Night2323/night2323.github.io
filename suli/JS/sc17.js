function szokoev (a){
  if (a%400==0) return true;
  if (a%100==0) return false;
  if (a%4==0) return true;
  return false;
}

function naptar (ev, ho, nap){
  var ossznap=0;
  for (var i=1900; i<ev; i++){
    if (szokoev(i)) ossznap+=366;
    else ossznap+=365;
  }
  for (var i=0; i<ho-1; i++){
    ossznap+=honapnapjai[i];
  }
  if (szokoev(ev) && ho>2) ossznap++;
  ossznap+=nap;
  return hetnapjai[ossznap%7];
}
