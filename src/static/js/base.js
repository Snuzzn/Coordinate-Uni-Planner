// const container = document.querySelector('#container');
console.log(3)

let btn = document.querySelector('#btn');
let divList = document.querySelector('.rando'); 

btn.addEventListener('click', () => {
    if(divList.style.display =='none') {
        divList.style.display = 'block';
    } else  {
        divList.style.display = 'none';
    }

})

