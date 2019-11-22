//This javascript file controls the slider for the introductions and images on the home page

//Creating the variables
var sliderImages = document.querySelectorAll('.slide'),
    arrowLeftArchitect = document.querySelector('#arrow-left-architect'),
    arrowRightArchitect = document.querySelector('#arrow-right-architect'),
    arrowLeftPlan = document.querySelector('#arrow-left-plan'),
    arrowRightPlan = document.querySelector('#arrow-right-plan'),
    arrowLeftInterior = document.querySelector('#arrow-left-interior'),
    arrowRightInterior = document.querySelector('#arrow-right-interior'),
    arrowLeftExtension = document.querySelector('#arrow-left-extension'),
    arrowRightExtension = document.querySelector('#arrow-right-extension'),
    current = 0;

// Clear all the images
function reset() {
    for(var i = 0; i < sliderImages.length; i++) {
        sliderImages[i].style.display = 'none';
    }
}    

// Initialising the image slider
function startSlide() {
    reset();
    sliderImages[0].style.display = 'block';
}

// Show previous
function slideLeft() {
    reset();
    sliderImages[current - 1].style.display = 'block';
    current--;
}

// Show Next
function slideRight() {
    reset();
    sliderImages[current + 1].style.display = 'block';
    current++;
}

// Arrow clicks for architect slide
// Left arrow click
arrowLeftArchitect.addEventListener('click', function() {
    if(current === 0) {
        current = sliderImages.length;  
    } 
    slideLeft();
});
// Right arrow click
arrowRightArchitect.addEventListener('click', function() {
    if(current === sliderImages.length - 1) {
        current = -1;  
    }
    slideRight();
});

// Arrow clicks for plan slide
// Left arrow click
arrowLeftPlan.addEventListener('click', function() {
    if(current === 0) {
        current = sliderImages.length;  
    } 
    slideLeft();
});
// Right arrow click
arrowRightPlan.addEventListener('click', function() {
    if(current === sliderImages.length - 1) {
        current = -1;  
    }
    slideRight();
});

// Arrow clicks for interior slide
// Left arrow click
arrowLeftInterior.addEventListener('click', function() {
    if(current === 0) {
        current = sliderImages.length;  
    } 
    slideLeft();
});
// Right arrow click
arrowRightInterior.addEventListener('click', function() {
    if(current === sliderImages.length - 1) {
        current = -1;  
    }
    slideRight();
});

// Arrow clicks for extension slide
// Left arrow click
arrowLeftExtension.addEventListener('click', function() {
    if(current === 0) {
        current = sliderImages.length;  
    } 
    slideLeft();
});
// Right arrow click
arrowRightExtension.addEventListener('click', function() {
    if(current === sliderImages.length - 1) {
        current = -1;  
    }
    slideRight();
});

startSlide();