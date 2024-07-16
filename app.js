//**inserindo texto no paragrafo (saidas )
//document.getElementById("rain").innerHTML = // 3 formas de saida para o usuario da pagina em javascript 
      //"meu primeiro codigo <b>JS</b>";

alert('fala vitão');

console.log("oi isso é um console log");

//fim 
function minhafuncao(){
    alert('fala vitão');  //instrução em bloco 
    alert('fala vitão');
    alert('fala vitão');
}
var a = 1;
var b = 2;
var c = a + b;  // variaveis 
console.log(c);

//
function soma( valor1,valor2){
    return valor1 + valor2;
}
document.getElementById("rain").innerHTML = soma(10,10)

const carro = {
     marca: "ford",
     modelo: "ka ",  //CONSTANTE OBJ
     ano: 2015,
     placa: "ABC-1234",
     buzina: function ()  {  alert('biiii')  }
};

console.log(carro["placa"]);