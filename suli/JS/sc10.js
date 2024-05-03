atlo1 = prompt("Atl1");
atlo2 = prompt("atl2");
document.writeln("Terület: " + (atlo1*atlo2)/2);
document.write("<br><br><br><br>")
/*------------------------------------------------------------------*/
a = prompt("a");
b = prompt("b");
alfa = prompt("alfa");
document.writeln("terulet: " + a*b*(Math.sin(alfa)));
document.write("<br><br><br><br>")
/*------------------------------------------------------------------*/
iras = prompt("irasbeli:");
szo = prompt("szobeli:");
if(isNaN(iras) == false && isNaN(szo) == false){
szo = szo/50*100;
if(iras>=50 && szo>=50){
document.writeln("gut");
}
else{
document.writeln("nicht gut");
}
}
else{
location.reload();
}