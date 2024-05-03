var tomeg = prompt("Adjá tömeget kilóban");
var hossz = prompt("Adjá magasságot méterben");
var bmi = tomeg/(hossz**2);
if(bmi<18.5){
    alert("Sovány vagy");
}
elif(18.5<bmi<25);{
    alert("Jó vagy");
}
elif(bmi>25);{
    alert("Kövér vagy");
}