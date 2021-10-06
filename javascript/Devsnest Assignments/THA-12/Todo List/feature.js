const inputField = document.querySelector('.inputField')
const addBtn = document.querySelector('.addBtn')
const listContainer = document.querySelector('.list_container')

const addBtnHandler = ()=>{
    const newTodo = document.createElement('div')
    const todo = `
    <li>
        <span>${inputField.value}</span>
        <span class="edit"><button><i class="fas fa-edit"></i></button></span>
        <span class="delete"><button><i class="fas fa-trash"></i></button></span>
    </li>
    `
    newTodo.innerHTML = todo

    listContainer.appendChild(newTodo)
    inputField.value = ""
}

addBtn.addEventListener('click',addBtnHandler)