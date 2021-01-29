
// let btn = document.querySelector('#btn');
// let divList = document.querySelector('.rando'); 

// btn.addEventListener('click', () => {
//     if(divList.style.display =='none') {
//         divList.style.display = 'block';
//     } else  {
//         divList.style.display = 'none';
//     }
// })


let container = document.querySelector('main')


var startingScrollPosition = localStorage.getItem("scrollPosition") || 0;
// console.log(startingScrollPosition);
container.scrollTop = startingScrollPosition;



var links = document.querySelectorAll("a");
console.log(link)

for (var i = 0; i < links.length; i++) {
    link = links[i];
    link.onclick = function () {
        // console.log(container.scrollTop);
        let scrollPosition = parseInt(container.scrollTop);
        localStorage.setItem("scrollPosition", scrollPosition);
        //console.log(container.scrollTop)
    }

}
