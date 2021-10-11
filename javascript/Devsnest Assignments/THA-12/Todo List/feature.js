const inputField = document.querySelector('.inputField')
const addBtn = document.querySelector('.addBtn')
const listContainer = document.querySelector('.list_container')
const saveBtn = document.querySelector('.saveBtn')
const saveIndex = document.getElementById('saveId')
const deleteAllBtn = document.querySelector('.deleteBtn')


const loadTodo = ()=>{
    let localTask = localStorage.getItem("todo")
    console.log(localTask)
    if(localTask == null){
        todoItems = []
    }else{
        todoItems = JSON.parse(localTask)
    }
    let todoTitle = ""
    const newTodo = document.createElement('div')
    todoItems.forEach((todo,index )=> {
        console.log(index)
        todoTitle = todoTitle + `
        <li>
            <span class="title">${todo}</span>
            <span>
            <span class="edit"><button onclick="editTodo(${index})"><i class="fas fa-edit"></i></button></span>
            <span class="delete"><button onclick="deleteTodo(${index})"><i class="fas fa-trash"></i></button></span>
            </span>
        </li>
        `
    })
    listContainer.innerHTML = todoTitle
}


loadTodo()
const addBtnHandler = ()=>{
    if (inputField.value ==""){
    }
    else{
        const todo = inputField.value
        let localTask = localStorage.getItem("todo")
        if(localTask == null){
            todoItems = []
        }else{
            todoItems = JSON.parse(localTask)
        }
    
        todoItems.push(todo)
        localStorage.setItem("todo",JSON.stringify(todoItems))
        loadTodo()
        inputField.value = ""
    }
}

addBtn.addEventListener('click',addBtnHandler)

const editTodo = (id)=>{
    let localTask = localStorage.getItem("todo")
    let todoObj = JSON.parse(localTask)
    inputField.value = todoObj[id]
    saveIndex.value = id
    addBtn.style.display = "none"
    saveBtn.style.display = "inline"
}

saveBtn.addEventListener('click', ()=>{
    let localTask = localStorage.getItem("todo")
    let todoObj = JSON.parse(localTask)
    todoObj[saveIndex.value] = inputField.value
    localStorage.setItem("todo",JSON.stringify(todoObj))
    loadTodo()
    inputField.value = ""
})

const deleteTodo = (index)=>{
    let localTask = localStorage.getItem("todo")
    let todoObj = JSON.parse(localTask)
    todoObj.splice(index,1)
    localStorage.setItem("todo",JSON.stringify(todoObj))
    loadTodo()
}

deleteAllBtn.addEventListener("click",()=>{
    let localTask = localStorage.getItem("todo")
    let todoObj = JSON.parse(localTask)
    todoObj = []
    localStorage.setItem("todo",JSON.stringify(todoObj))
    loadTodo()
})



 