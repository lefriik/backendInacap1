const root = '/'
const activePage = window.location.pathname;


if(activePage === root){
    
    const link = document.querySelector('nav a.inicio')
    link.classList.add('active')

}else{

    const navLinks = document.querySelectorAll('nav a').forEach(link => {
    
        //console.log(link.href)
        if(link.href.includes(`${activePage}`)){
    
            link.classList.add('active')
        }
    })

}

/*


*/
