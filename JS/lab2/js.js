document.getElementById('wrapper').addEventListener('click', function(){
    if(event.target.style.color != 'blue' && event.target.style.color != 'red'){
        if(event.target.tagName.toLowerCase() === 'p'){
            event.target.style.color = 'blue'
        }

        if(event.target.classList.contains('color')){
            event.target.style.color = 'red'
        }} else{
            event.target.style.color = ''
        }
})