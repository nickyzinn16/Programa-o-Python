// eeroo se inserir vaziu
// erro ao inferior 10 carateres e supereior a 20 carateres,
// tpc - ao enves de li e ul, colocar como tabela span numa coluna e btn em outra coluna

console.log("Bem-vindo ao app Tarefas - Seu gestor de tarefas");

// const inputTask = document.getElementById("new-Task");
const inputTask = document.querySelector("#new-task");

// const addBtn = document.getElementById("add-btn");
const addBtn = document.querySelector("#addbtn");

// const taskList = document.getElementById("task-list");
const taskList = document.querySelector("#task-list");

// CORREÇÃO: declarar o span de erro
const erroSpan = document.querySelector("#erro");

function addNewTask(){
    const task_text = inputTask.value.trim();
    // mplementar algum sistema de validacao de nome (nos vamos fazer)

    erroSpan.style.display = "none";


    // ###################### TPC ########################3
    // erro se inserir vazio
    if (task_text === "") {
        erroSpan.textContent = "o nome da tarefa não pode ser vazio.";
        erroSpan.style.display = "block";
        return;
    }

    // erro se o nome forinferior a 10 caracteres e a 20 carateres
    if (task_text.length < 10) {
        erroSpan.textContent = "A tarefa deve ter no mínimo 10 caracteres.";
        erroSpan.style.display = "block";
        return;
    }

    if (task_text.length > 20) {
        erroSpan.textContent = "A tarefa deve ter no máximo 20 caracteres.";
        erroSpan.style.display = "block";
        return;
    }
    // #####################################################

    // criar o elemento li para contar os itens das tarefas
    const li = document.createElement("li");

    // criar um atriuto class para o elemento li, para permitir a formatacao
    li.className = "task";

    // Criar texto da tarefa
    li.textContent = task_text;

    // criar um botao de interacao ao lado da tafera
    const delBtn = document.createElement("button");

    // Para atribuir um texto a um botao
    delBtn.textContent = "Delete";

    // Manipular evento para o botao, que no caso sera sobre eliminar o item (li) do documento
    delBtn.addEventListener("click", function () {
        li.remove();
    });

    li.appendChild(delBtn);
    taskList.appendChild(li);

    inputTask.value = "";
    inputTask.focus();  
}

// CORREÇÃO: não colocar () senão executa logo
addBtn.addEventListener('click', addNewTask);

inputTask.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        addNewTask();
    }
});