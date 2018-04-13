function validaIdade() {
    var data = document.getElementById("dataNasc").value;
    data = data.split("-");

    var data_atual = new Date();
    var ano = data_atual.getFullYear();

    var idade = ano - data[0];

    if (idade < 17) {
        return false;
    } else {
        return true
    }
}

function validaCPF() {
    var numeros, digitos, soma, i, resultado, digitos_iguais;
    var cpf = document.getElementById("cpf").value;
    digitos_iguais = 1;
    if (cpf.length < 11) {
        return false;
    }
    for (i = 0; i < cpf.length - 1; i++) {
        if (cpf.charAt(i) != cpf.charAt(i + 1)) {
            digitos_iguais = 0;
            break;
        }
    }
    if (!digitos_iguais) {
        numeros = cpf.substring(0, 9);
        digitos = cpf.substring(9);
        soma = 0;
        for (i = 10; i > 1; i--) {
            soma += numeros.charAt(10 - i) * i;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0)) {
            return false;
        }
        numeros = cpf.substring(0, 10);
        soma = 0;
        for (i = 11; i > 1; i--) {
            soma += numeros.charAt(11 - i) * i;
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1)) {
            return false;
        }
        return true;
    } else {
        return false;
    }
}

function validaSenha() {
    var senha = document.getElementById("senha").value;

    var min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"];
    var mai = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "W", "X", "Y", "Z"];
    var numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];

    var contNumeros = 0;
    var contLetras = 0;

    for (var i = 0; i < min.length; i++) {
        for (var j = 0; j < senha.length; j++) {
            if (senha[j] == min[i]) {
                contLetras++;
            }
            if (senha[j] == mai[i]) {
                contLetras++;
            }
        }
    }
    
    for (var k = 0; k < numeros.length; k++) {
        for (var l = 0; l < senha.length; l++) {
            if (senha[l] == numeros[k]) {
                contNumeros++;
            }
        }
    }
  
    if(contLetras>=1 && contNumeros>=1) {
        return true;
    } else {
        return false;
    }
}

function comparaSenha() {
    
}

function validaDados() {
    
}