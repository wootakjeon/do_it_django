const body = document.querySelector('body');
const modal = document.querySelectorAll('.modal');
const btnOpenPopup = document.querySelectorAll('.btn-open-popup');


btnOpenPopup.forEach((item, idx) =>{

    item.addEventListener('click', (e)=>{
    
    console.log(e.target.getAttribute('id'));
    //document.querySelector('.modal .m'+e.target.getAttribute('id')).classList.toggle('show');
    e.target.previousElementSibling.classList.toggle('show');    

    if (e.target.previousElementSibling.classList.contains('show')) {
      body.style.overflow = 'hidden';
    }
    })
    
    item.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.toggle('show');

          if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
          }
        }
      });

});

//Hide modal
window.addEventListener('click', (e) => {
    if (e.target.getAttribute('class') == 'modal show') 
        e.target.classList.remove('show') 
});

/* {% comment %} btnOpenPopup.forEach((item, idx) =>{

    item.addEventListener('click', (e)=>{
    
    console.log(modal[idx]);
    modal.classList.toggle('show');

    if (modal.classList.contains('show')) {
      body.style.overflow = 'hidden';
    }
    })
    
    item.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.toggle('show');

          if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
          }
        }
      });

    }); {% endcomment %} */
