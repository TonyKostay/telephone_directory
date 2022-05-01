document.addEventListener('click',(event)=>{
    if (event.target.className == 'tab'){
        event.target.nextElementSibling.className = 'tab__list-on';
    }
    else{
        document.querySelectorAll('.tab').forEach((element)=>{
            element.nextElementSibling.className = 'tab__list-off';
            });
        };
    });