var pont = prompt("Pontszám:")

if (pont>100 || pont<0){
    alert("Hibás adat.")
    window.location.reload()
}

switch(pont>100 || pont<0){
    case pont >= 0 && pont <50:
        alert("1");
        break;
    case pont >=50 && pont<65:
        alert("2");
        break;
    case pont >=65 && pont<80:
        alert("3");
        break;
}