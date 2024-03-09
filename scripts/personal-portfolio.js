function uiSound(sound) {
  sound.currentTime = 0;
  sound.play()
    .then(() => { sound.muted = false; })
    .catch(() => { sound.muted = true; });
}

const tapSound = new Audio('media/ui-sounds/tap.ogg');
document.addEventListener('click', () => uiSound(tapSound));

const hoverSound = new Audio('media/ui-sounds/hover.ogg');
document.querySelectorAll('.s-hover').forEach(element => {
  element.addEventListener('mouseenter', () => uiSound(hoverSound));
});

const clickSound = new Audio('media/ui-sounds/click.ogg');
document.querySelectorAll('.s-click').forEach(element => {
  element.addEventListener('click', () => uiSound(clickSound));
});

const dingSound = new Audio('media/ui-sounds/ding.ogg');
document.querySelectorAll('.s-ding').forEach(element => {
  element.addEventListener('click', () => uiSound(dingSound));
});