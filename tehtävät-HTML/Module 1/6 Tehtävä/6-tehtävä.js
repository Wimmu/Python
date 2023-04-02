let vastaus = confirm('Should I calculate square root?');

if (vastaus == true){
    let numero = parseInt(prompt('Input number:'));
    if (numero < 0){
        document.querySelector('#vastaus').innerHTML = 'The square root of a negative number is not defined.';
    } else {
        neliöjuuri = Math.sqrt(numero).toFixed(2)
        document.querySelector('#vastaus').innerHTML = 'Numeron ' + numero + ' neliöjuuri on ' + neliöjuuri;
    }
} else {
    document.querySelector('#vastaus').innerHTML = 'The square root is not calculated.';
}