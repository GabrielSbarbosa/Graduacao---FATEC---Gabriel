// Exercicio de calculadora em JavaScript // 

<!doctype html>
<html lang="pt-BR">
<head>
	<meta charset="utf-8">
	<title>Praticando Javascript - Exercício 3</title>
</head>
<body>

<h1>exercicio da calculadora em javascript</h1>
       
</body>
     
	<script type="text/javascript">
    
		var numero1 = prompt("Insira o primeiro número: ");
		var numero2 = prompt("Insira o segundo número: ");
		var ler = prompt("Insira o operador: +, -, /, *");
		
		function recarregarAPagina(){
         window.location.reload();
        } 
		
		 if( numero1 < 0 || numero2 < 0 ){
		 alert(" Coloque um numero inteiro positivo");
		 recarregarAPagina();
		 }else{
		 
		 function operation(ler, numero1, numero2) {
		
			  if (ler == "+") {
			    resultado = 0;
				resultado = parseFloat(numero1) + parseFloat(numero2);
				return resultado
			} else if (ler == "-") {
				resultado = 0;
				resultado = numero1 - numero2;
				return resultado
			} else if (ler == "*") {
				resultado = 0;
				resultado = numero1 * numero2;
				return resultado
			} else if (ler == "/") {
				resultado = 0;
				resultado = numero1 / numero2;
				return resultado
			} else {
				alert('Operação inválida, coloque um operador correspondente!');
				return recarregarAPagina();
			}
		}

		prompt('O resultado é' , +operation(ler, numero1, numero2));
		 
		 }
				
		
	</script>
  
</html>
