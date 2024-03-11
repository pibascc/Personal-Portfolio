let animArea = document.createElement('div');
animArea.id = 'animation-area';
document.body.appendChild(animArea);
function clickEffect(x, y) {
  let effect = document.createElement('div');
  let style = effect.style;
  style.left = x + 'px';
  style.top = y + 'px';
  effect.classList.add('click-effect');
  document.getElementById('animation-area').appendChild(effect);
  setTimeout(() => effect.remove(), 500);
}

function uiSound(sound) {
  sound.currentTime = 0;
  sound.play()
    .then(() => { sound.muted = false; })
    .catch(() => { sound.muted = true; });
}

const tapSound = new Audio('media/ui-sounds/tap.ogg');
document.addEventListener('click', event => {
  uiSound(tapSound);
  let x = event.clientX;
  let y = event.clientY;
  clickEffect(x, y);
});

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

const loadSound = new Audio('media/ui-sounds/load.ogg');
document.querySelectorAll('.s-load').forEach(element => {
  let timer;
  element.addEventListener('mouseover', () => {
    timer = setTimeout(() => uiSound(loadSound), 250);
  });
  element.addEventListener('mouseout', () => {
    clearTimeout(timer);
  });
});