let vastaus = prompt('Kuinka monta noppaa heitetään?');

let kerrat = 0;
let summa = 0;
let max = 6;
let min = 1;

while (kerrat != vastaus) {
    noppa = Math.floor(Math.random() * (max - min + 1) + min);
    summa = summa + noppa;
    kerrat = kerrat + 1;
}

document.querySelector('#vastaus').innerHTML = 'Noppien silmälukujen summa on: ' + summa;
