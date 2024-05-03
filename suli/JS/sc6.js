var db = 0

for (i=100; i<=1000;i++){
    if(i%5==0){
        db++;
    }
}
document.write(db,"<br><br><br>")


for(i=0; i<=10; i++){
    document.write("----------------------------------------------------------<br>")
    document.write("|",i,"|",Math.pow(i,2),"|",Math.sqrt(i),"|<br>")
}
document.write("----------------------------------------------------------<br><br><br>")

var db2 = 0
var szum = 0

for (i=10; i<=100; i++){
    if(i%2==0){
        db2++
        szum = szum+i
    }
}
document.write(szum/db,"<br><br><br>")