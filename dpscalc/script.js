function calculateDPS() {
    let rpm = document.getElementById("rpm").value;
    let dmg = document.getElementById("dmg").value;
    let dps = parseInt(rpm) * parseInt(dmg) / 60;
    let dpm = parseInt(rpm) * parseInt(dmg);
    document.getElementById("dps").innerText += dps;
    document.getElementById("dps").innerText += " DPS \n";
    document.getElementById("dps").innerText += dpm;
    document.getElementById("dps").innerText += " DPM \n\n\n";

}
