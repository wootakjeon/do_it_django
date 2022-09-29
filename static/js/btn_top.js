let Top = document.querySelector('.btn_top');

Top.addEventListener('click', function (e) {
    e.preventDefault();
    // document.body.scrollTop = 0;
    // document.documentElement.scrollTop = 0;
    window.scrollTo( { top: 0, behavior: 'smooth'});
})
