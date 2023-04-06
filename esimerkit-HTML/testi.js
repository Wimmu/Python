'use strict';
console.log("Moroooo");
const name = prompt('Syötä nimesi:');
document.querySelector('#target').innerHTML = 'Huomenta, ' + name + '!';

const names = ['Silva', 'Veeti', 'Wimmu'];
for(let i = 0; i < names.length; i++) {
    console.log(names[i]);
}