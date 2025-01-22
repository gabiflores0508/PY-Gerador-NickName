let opcaoAtual = "";

function selecionarOpcao(element, tipo) {
    let opcoes = document.querySelectorAll('.escolha p');
    opcoes.forEach(item => item.classList.remove('selecionado'));

    element.classList.add('selecionado');
    opcaoAtual = tipo;
    document.getElementById('opcaoSelecionada').innerText = element.innerText;

    // Esconde todos os campos extras antes de mostrar o correto
    document.getElementById('extraFieldsTema').style.display = "none";
    document.getElementById('extraFieldsPalavra').style.display = "none";
    document.getElementById('extraFieldsPersonalizado').style.display = "none";

    // Mostra os campos adicionais de acordo com a opção selecionada
    if (tipo === "tema") {
        document.getElementById('extraFieldsTema').style.display = "block";
    } else if (tipo === "palavra") {
        document.getElementById('extraFieldsPalavra').style.display = "block";
    } else if (tipo === "personalizado") {
        document.getElementById('extraFieldsPersonalizado').style.display = "block";
    }
}

async function gerarNickname() {
    if (!opcaoAtual) {
        alert("Por favor, selecione uma opção antes de gerar um nickname.");
        return;
    }

    let requestData = { tipo: opcaoAtual };

    // Captura os dados conforme a opção selecionada
    if (opcaoAtual === "tema") {
        requestData.tema = document.getElementById("tema").value;
    } else if (opcaoAtual === "palavra") {
        requestData.palavra = document.getElementById("palavra").value;
    } else if (opcaoAtual === "personalizado") {
        requestData.tema = document.getElementById("personalizadoTema").value;
        requestData.incluir_simbolos = document.getElementById("personalizadoSimbolos").value === "true";
        
        // Captura e valida o número personalizado
        let numeroInput = document.getElementById("personalizadoNumero").value;
        requestData.numero_customizado = numeroInput !== "" ? parseInt(numeroInput) : null;

        // Captura e valida a inicial
        let inicialInput = document.getElementById("personalizadoInicial").value.trim().toUpperCase();
        if (inicialInput.length !== 1 || !/^[A-Z]$/.test(inicialInput)) {
            alert("Por favor, insira uma única letra válida para a inicial.");
            return;
        }
        requestData.inicial = inicialInput;
    }

    document.getElementById('nicknameGerado').value = "Gerando...";

    try {
        const response = await fetch('http://127.0.0.1:5000/api/gerar_nickname', {  
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        });

        const data = await response.json();
        if (data.nickname) {
            document.getElementById('nicknameGerado').value = data.nickname;
        } else {
            document.getElementById('nicknameGerado').value = "Erro ao gerar nickname.";
        }
    } catch (error) {
        document.getElementById('nicknameGerado').value = "Falha na conexão!";
    }
}


function copiarNickname() {
    let nicknameInput = document.getElementById("nicknameGerado");

    if (nicknameInput.value === "" || nicknameInput.value === "Gerando...") {
        alert("Nenhum nickname para copiar!");
        return;
    }

    nicknameInput.select();
    nicknameInput.setSelectionRange(0, 99999);
    document.execCommand("copy");

    alert("Nickname copiado: " + nicknameInput.value);
}
