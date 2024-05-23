var hamburger = document.querySelector(".ham");
var navlist = document.querySelector(".nav");
var links = document.querySelector(".nav li");

hamburger.addEventListener("click", function(){
    this.classList.toggle("click");
    navlist.classList.toggle("open");
})



const sliderLine = document.querySelector('.slider-line'),
      prevButton = document.querySelector('.button-prev'),
      nextButton = document.querySelector('.button-next'),
      dots = document.querySelectorAll('.dot')

let position = 0,
dotIndex = 0

const nextSlide = () => {
  if(position < (dots.length - 1) * 584.77) {
    position += 584.77
    dotIndex++
  } else {
    position = 0
    dotIndex = 0
  }

  sliderLine.style.left = -position + 'px'
  thisSlide(dotIndex)
}

const prevSlide = () => {
  if(position > 0) {
    position -= 584.77
    dotIndex--
  }
  else {
    position = (dots.length - 1) * 584.77
    dotIndex = (dots.length - 1)
  }

  sliderLine.style.left = -position + 'px'
  thisSlide(dotIndex)
}

const thisSlide = (index) => {
    for (let dot of dots){
      dot.classList.remove('activesl')
    }
    dots[index].classList.add('activesl')
}




dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      position = 584.77 * index
      sliderLine.style.left = -position + 'px'
      dotIndex = index
      thisSlide(dotIndex)
    })
})

setInterval(() => {
  nextSlide()
}, 3000)