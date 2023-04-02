let vuosi = String(prompt('Syötä vuosi:'));

if (vuosi % 100 == 0){
    if (vuosi % 400 == 0) {
        document.querySelector('#vastaus').innerHTML = vuosi + ', on karkausvuosi.';
    } else {
        document.querySelector('#vastaus').innerHTML = vuosi + ', ei ole karkausvuosi.';
    }
} else {
    if (vuosi % 4 == 0) {
        document.querySelector('#vastaus').innerHTML = vuosi + ', on karkausvuosi.';
    } else {
        document.querySelector('#vastaus').innerHTML = vuosi + ', ei ole karkausvuosi.';
    }
}