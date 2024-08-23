/* 
Faça um programa para calcular o valr de uma viagem.

Voce tera 3 variaveis. Sendo elas:
1 - Preço do combustivel;
2 - Gasto medio de combustivel do carro por Km;
3 - Distancia em Km da viagem;

*/
const precoCombustivel = 5.90;
const gastoMedio = 10;
const distancia = 100;

const gasto = distancia / gastoMedio * precoCombustivel;

console.log(gasto.toFixed(2));