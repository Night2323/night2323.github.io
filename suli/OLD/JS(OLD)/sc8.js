for (i=0;i<10;i++) {
    var erme=Math.round(Math.random()*2)+1
    if (erme==1) {
    document.writeln(i+1,"  ","fej" ,"<br>")
    }
    else
    {
    document.writeln(i+1,"írás","<br>")
    }
}

for (i=1;i<=10;i++){
    var kocka = Math.round(Math.random()*6)+1
    document.writeln(kocka)
}

document.write("<br>")

for (i=1;i<=5;i++){
    var otos = Math.round(Math.random()*90)+1
    document.writeln(otos)
}

document.write("<br>")

for (i=1;i<=14;i++){
    var toto = Math.round(Math.random()*3)+1
    if(toto==1){
        document.writeln(toto)
    }
    if(toto==2){
        document.writeln(toto)
    }
    if(toto==3){
        document.writeln("x")
    }

}

document.write("<br>")

for (i=1;i<=1;i++){
    var nyoc = Math.round(Math.random()*90000000)+10000000
    document.writeln(nyoc)
}

document.write("<br>")

var szam = Math.round((Math.random()*100)+1)
var val = parseInt(prompt("Szám:"))
if(val==szam){
    document.writeln("GJ")
}
else{
    document.writeln("NOP")
}