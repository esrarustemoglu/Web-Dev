const form = document.querySelector(".form");
const addInput = document.querySelector("#NewTask");
const todoList = document.querySelector(".list-group");
const firstCardBody = document.querySelector(".formdiv");
const secondCardBody = document.querySelector(".cardbody");


runEvents();

function runEvents(){
    form.addEventListener("submit", addTodo);
    
}

function addTodo(e){
    e.preventDefault();
    const inputText = addInput.value.trim();
    if(inputText == null || inputText == ""){
        alert("Please enter NewTask!");
    }
    else{
        addToDoUI(inputText);
    }
}

function addToDoUI(inputText){
    const li = document.createElement("li");
    li.className="ListToDo";

    const checkbox = document.createElement("input");
    checkbox.type ="checkbox";

    checkbox.addEventListener("change" , function() {
        li.classList.toggle("done");
    });

    const span = document.createElement("span");
    span.textContent = inputText;

    const deleteBtn = document.createElement("button");
    deleteBtn.className="delete";
    deleteBtn.textContent = "X";

    deleteBtn.addEventListener("click", function () {
        todoList.removeChild(li);
    });



    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);
    todoList.appendChild(li);
    addInput.value="";

}
