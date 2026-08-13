

var tl = gsap.timeline({
    scrollTrigger:{
        trigger: '.two',
        start: '0% 95%',
        end: '70% 50%',
        scrub: true,
        markers: true // depuração //
    },
})

tl.to(
    '#fanta',
    {
        top: '120%', //move o elemento com id fanta pra 120% do topo
        left: '0%',
    
    },
    'orange',
); // nomneando este trecho da animacao como orange para sincornizacao

tl.to(
    '#laranja-cortes',
    {
        top: '160%',
        left: '23%',
    },
    'orange'
);

tl.to(
    '#laranja',
    {
        width: '15%',
        top: '170%',
        right: '10%'
    },
    'orange'
);

tl.to(
    '#folha',
    {
        top: '110%',
        rotate: '130deg',
        left: '70%',
    },
    'orange'

);

tl.to(
    '#folha2',
    {
        top: '110%',
        rotate: '1080deg',
        left: '0%',
    },
    'orange'
);

//timeline 2
 
var tl2= gsap.timeline({
    scrollTrigger:{
        trigger: '.three',
        start: '0% 95%',
        end: '20% 50%',
        scrub: true,
        markers: true // depuração //
    },
})

tl2.from(
    '.lemon1',
    {
        rotate: '-90deg',
        left: '-100%',
        top: '110%',
    },
    'ca'
);

tl2.from(
    '#coca',
    {
        rotate: '-90deg',
        left: '-100%',
        top: '110%',
    },
    'ca'
);

tl2.from(
    '.lemon2',
    {
        rotate: '90deg',
        left: '100%',
        top: '110%',
    },
    'ca'
);

tl2.from(
    '#pepsi',
    {
        rotate: '90deg',
        left: '100%',
        top: '110%',

    },
    'ca'
);

tl2.to(
    '#laranja-cortes',
    {
        width: '18%',
        left: '41%',
        top: '204%',
    },
    'ca'
);

tl2.to(
    '#fanta',
    {
        width: '37%',
        left: '32%',
        top: '210%',
    },
    'ca'
);