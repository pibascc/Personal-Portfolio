document.addEventListener("DOMContentLoaded", () => {
    const hoverSound = new Audio("media/ui-sounds/hover.ogg");
        
    document.querySelectorAll('.s-hover').forEach(element => {
        element.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0;
            hoverSound.play();
        });
    });
});