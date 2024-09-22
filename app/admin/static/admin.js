var archiveButtons = document.getElementsByClassName('archive-button');
for(let i = 0; i < archiveButtons.length; i++){
    archiveButtons[i].addEventListener('click', e => {
        console.log(e.target.id)
    })
}


// archiveButton.addEventListener('change', (e) => {
//     console.log(e)
// })