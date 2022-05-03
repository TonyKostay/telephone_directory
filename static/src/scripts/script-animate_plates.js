const animate_icons = document.querySelectorAll('.plate__animate-icon');

let icon_animate = function(element){
    element.style.animation = 'animate-icon 500ms ease-in-out';
    element.addEventListener('animationend',()=>{
        element.style.animation ='none';
        window.location.href = element.alt;
    });
};


animate_icons.forEach((element)=>{
    element.parentElement.parentElement.addEventListener('click',(event)=>{
        icon_animate(element);
    });
});



