var szam = prompt("50 és 100 közötti szám: ");
var i = parseInt(szam) 
while(i >= 0){
    if (szam%i==0){
        document.writeln(i)
        
    }
    i--
}

document.write("<br><br><br><br>")
/*fel2*/

r = prompt("Kör Kerület:")
π = Math.PI

if(r==0){
    alert("Pont")
}
else{
    document.writeln(2*r*π)
    document.writeln(Math.pow(r,2)*π)
}

document.write("<br><br><br><br>")
/*fel3*/


atl = prompt("Átlag:")
if (atl<=2.99 && atl>=2){
    document.writeln("8000 Ft/hó (8%)")
}
else if (atl<=3.99 && atl>=3){
    document.writeln("25000 Ft/hó (25%)")
}
else if (atl<=4.49 && atl>=4){
    document.writeln("42000 Ft/hó (42%)")
}
else if (atl>=4.5 && atl<=5){
    document.writeln("59000 Ft/hó (59%)")
}
else{
    document.writeln("16000 Ft/hó (16%)")
}