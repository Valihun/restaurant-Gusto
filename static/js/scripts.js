
let header__burger = document.querySelector('.header__burger');
let header_menu = document.querySelector('.menu__body');
let back = document.querySelector('body');
let header__list = document.querySelector('.menu__list');

header__burger.onclick = function () {
	header__burger.classList.toggle('active');
	header_menu.classList.toggle('active');
	back.classList.toggle('lock');
}

header__list.onclick = function () {
	header__list.classList.remove('active');
	back.classList.toggle('lock');
}


new Swiper('.image-slider', {
	// Стрелки
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev'
	},
});



let intager = 1;
let charfield = 'char';
let double = 1.5;

console.log(intager + charfield);
console.log(double + intager);
console.log(charfield + double);