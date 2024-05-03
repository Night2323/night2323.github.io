const gyümik = [
    "alma",
    "barack",
    "citrom",
    "datoja",
    "eper"
];

const eb = gyümik.map(gyüm => gyüm[0]);

var bb = prompt("Betű:");

if (eb.includes(bb)){
    switch(eb,bb){
        case bb = eb[0]:
            alert(gyümik[0]);
            window.location.reload();
            break;
        case bb = eb[1]:
            alert(gyümik[1]);
            window.location.reload();
            break;
        case bb = eb[2]:
            alert(gyümik[2]);
            window.location.reload();
            break;
        case bb = eb[3]:
            alert(gyümik[3]);
            window.location.reload();
            break;
        case bb = eb[4]:
            alert(gyümik[4]);
            window.location.reload();
            break;
    }
}
else{
    alert("Nincs ilyen betűs gyümölcs a listánkban");
    window.location.reload();
}