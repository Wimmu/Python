let x = parseInt(prompt('Give first number:'));
let y = parseInt(prompt('Give second number:'));
let a = parseInt(prompt('Give third number:'));

let summa = x + y + a;
let tulo = x * y * a;
let keskiarvo = summa / 3;

document.querySelector('#summa').innerHTML = 'Summa:' + summa;
document.querySelector('#tulo').innerHTML = 'Tulo:' + tulo;
document.querySelector('#keskiarvo').innerHTML = 'Keskiarvo:' + keskiarvo;