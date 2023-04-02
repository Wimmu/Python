let nimi = String(prompt('Anna nimesi:'));

let max = 4;
let min = 1;

let vastaus = Math.random() * (max - min) + min;
let huone = "";
let pyörvastaus = Math.round(vastaus)

if (pyörvastaus == 1) {
    huone = "Gryffindor";
} else if (pyörvastaus == 2) {
    huone = "Slytherin";
} else if (pyörvastaus == 3) {
    huone = "Hufflepuff";
} else {
    huone = "Ravenclaw";
}

document.querySelector('#vastaus').innerHTML = nimi + ', you are ' + huone;