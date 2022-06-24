let passs = "Pourquoipasnous?@"

let x = document.getElementById('pw')
let sub = document.getElementById('sub')

function go(){
}
let child
let pp = document.getElementById('mess')
function print(){
    pp.innerHTML=''
    child = document.createElement('p')
    if(x.value ==''){
        child.innerText=''
    }
    else if(x.value != passs){
        console.log("check if the password you typed is correct")
        child.innerText = "The password is incorrect"
        child.style.color = "red"
        sub.disabled = true
    }
    else if(x.value == passs){
        console.log("The password is correct :)")
        child.style.color = "green"
        child.innerText = "The password is correct"
        sub.disabled = true
    }
    pp.appendChild(child)
}
function wipee(){
    let t = document.getElementById('pw')

    t.value=""
    console.log(x.value + "Love")
    console.table(listAll)
}
function listen(){
    x.addEventListener('keyup', go)
    x.addEventListener('keyup', print)
    document.addEventListener('load', wipee)
}

listen()