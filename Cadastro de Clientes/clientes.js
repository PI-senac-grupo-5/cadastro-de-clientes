const API_URL = "http://127.0.0.1:5000/api/clientes";

// ==================================================
// UTILITÁRIOS
// ==================================================

function formatarData(data) {
  if (!data) return "";

  // YYYY-MM-DD -> DD/MM/YYYY
  const [ano, mes, dia] = data.split("-");
  return `${dia}/${mes}/${ano}`;
}

function converterData(data) {
  if (!data) return "";

  // DD/MM/YYYY -> YYYY-MM-DD
  const [dia, mes, ano] = data.split("/");
  return `${ano}-${mes}-${dia}`;
}

// ==================================================
// CADASTRO E ATUALIZAÇÃO
// ==================================================

const formulario = document.querySelector(".formulario");

if (formulario) {
  let clienteId = null;

  function obterDadosFormulario() {
    return {
      nome_completo: document.querySelector("#nome").value,
      email: document.querySelector("#email").value,
      data_nasc: formatarData(document.querySelector("#nascimento").value),
      telefone: document.querySelector("#telefone").value,
      sexo: document.querySelector("#sexo").value,
      cep: document.querySelector("#cep").value,
      cpf: document.querySelector("#cpf").value,
      cnpj: "",
      id: clienteId,
    };
  }

  function preencherFormulario(cliente) {
    document.querySelector("#nome").value = cliente.nome_completo;
    document.querySelector("#email").value = cliente.email;

    document.querySelector("#nascimento").value = converterData(
      cliente.data_nasc,
    );

    document.querySelector("#telefone").value = cliente.telefone;
    document.querySelector("#sexo").value = cliente.sexo || "";
    document.querySelector("#cep").value = cliente.cep || "";
    document.querySelector("#cpf").value = cliente.cpf || "";

    clienteId = cliente.id;

    document.querySelector(".botao-escuro").textContent = "Atualizar cliente";
  }

  // Verifica se existe um cliente para edição
  const clienteEdicao = sessionStorage.getItem("clienteEdicao");

  if (clienteEdicao) {
    preencherFormulario(JSON.parse(clienteEdicao));
    sessionStorage.removeItem("clienteEdicao");
  }

  formulario.addEventListener("submit", async (event) => {
    event.preventDefault();

    const cliente = obterDadosFormulario();
    const metodo = clienteId ? "PUT" : "POST";

    try {
      const resposta = await fetch(API_URL, {
        method: metodo,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(cliente),
      });

      const resultado = await resposta.json();

      if (!resposta.ok) {
        throw new Error(
          resultado.mensagem || resultado.erro || "Erro ao salvar cliente.",
        );
      }

      alert(
        clienteId
          ? "Cliente atualizado com sucesso!"
          : "Cliente cadastrado com sucesso!",
      );

      formulario.reset();
      clienteId = null;

      document.querySelector(".botao-escuro").textContent = "Cadastrar cliente";
    } catch (erro) {
      console.error(erro);
      alert(erro.message);
    }
  });
}

// ==================================================
// CONSULTA, PESQUISA, EDIÇÃO E EXCLUSÃO
// ==================================================

const tabela = document.querySelector(".tabela-clientes tbody");
const campoPesquisa = document.querySelector(".campo-pesquisa");

if (tabela && campoPesquisa) {
  async function listarClientes(filtro = "") {
    try {
      const url = new URL(API_URL);

      if (filtro) {
        url.searchParams.set("filtro", filtro);
      }

      const resposta = await fetch(url);

      if (!resposta.ok) {
        throw new Error("Erro ao consultar clientes.");
      }

      const resultado = await resposta.json();

      const clientes = Array.isArray(resultado)
        ? resultado
        : resultado.clientes;

      renderizarClientes(clientes || []);
    } catch (erro) {
      console.error(erro);
      alert(erro.message);
    }
  }

  // Preenche a tabela
  function renderizarClientes(clientes) {
    tabela.innerHTML = "";

    clientes.forEach((cliente) => {
      const linha = document.createElement("tr");

      const valores = [
        cliente.nome_completo,
        cliente.cpf || "",
        cliente.telefone,
        cliente.email,
      ];

      valores.forEach((valor) => {
        const coluna = document.createElement("td");
        coluna.textContent = valor || "";
        linha.appendChild(coluna);
      });

      const colunaAcoes = document.createElement("td");
      colunaAcoes.classList.add("acoes-tabela");

      // Botão editar
      const botaoEditar = document.createElement("button");
      botaoEditar.textContent = "Editar";
      botaoEditar.classList.add("botao-editar");

      botaoEditar.addEventListener("click", () => {
        editarCliente(cliente);
      });

      // Botão excluir
      const botaoExcluir = document.createElement("button");
      botaoExcluir.textContent = "Excluir";
      botaoExcluir.classList.add("botao-excluir");

      botaoExcluir.addEventListener("click", () => {
        excluirCliente(cliente);
      });

      colunaAcoes.append(botaoEditar, botaoExcluir);
      linha.appendChild(colunaAcoes);

      tabela.appendChild(linha);
    });
  }

  // Encaminha para edição
  function editarCliente(cliente) {
    sessionStorage.setItem("clienteEdicao", JSON.stringify(cliente));

    window.location.href = "../index.html";
  }

  // Exclui cliente
  async function excluirCliente(cliente) {
    const confirmar = confirm(
      `Deseja realmente excluir o cliente ${cliente.nome_completo}?`,
    );

    if (!confirmar) return;

    try {
      const resposta = await fetch(
        `${API_URL}/${encodeURIComponent(cliente.id)}`,
        {
          method: "DELETE",
        },
      );

      // Se houver erro, tenta obter a mensagem do backend.
      if (!resposta.ok) {
        const resultado = await resposta.json();

        throw new Error(
          resultado.mensagem || resultado.erro || "Erro ao excluir cliente.",
        );
      }

      // HTTP 204 não possui corpo, portanto não usamos resposta.json().
      alert("Cliente excluído com sucesso!");

      // Atualiza a tabela mantendo o filtro atual.
      listarClientes(
        campoPesquisa.value.trim().length >= 3
          ? campoPesquisa.value.trim()
          : "",
      );
    } catch (erro) {
      console.error(erro);
      alert(erro.message);
    }
  }

  // Pesquisa após 3 caracteres
  campoPesquisa.addEventListener("input", () => {
    const filtro = campoPesquisa.value.trim();

    if (filtro.length >= 3) {
      listarClientes(filtro);
    } else {
      listarClientes();
    }
  });

  // Consulta inicial
  listarClientes();
}
