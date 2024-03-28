// #region Animation Effects
let animArea = document.createElement('div');
animArea.id = 'animation-area';
document.body.appendChild(animArea);

// Click Ripple Effect
function clickEffect(x, y) {
  let effect = document.createElement('div');
  effect.style.left = `${x}px`;
  effect.style.top = `${y}px`;
  effect.classList.add('click-effect');
  effect.addEventListener('animationend', () => effect.remove());
  animArea.appendChild(effect);
}

// Custom Alert
function uiAlert(message) {
  let alertBox = document.createElement('div');
  let alertText = document.createElement('p');
  alertBox.classList.add('ui-alert');
  alertText.textContent = message;
  alertBox.appendChild(alertText);
  alertBox.addEventListener('animationend', () => alertBox.remove());
  animArea.appendChild(alertBox);
}
// #endregion

// #region Sounds
function uiSound(sound) {
  sound.currentTime = 0;
  sound.play()
    .then(() => { sound.muted = false; })
    .catch(() => { sound.muted = true; });
}

// Tap Sound
const tapSound = new Audio('media/ui-sounds/tap.ogg');
document.addEventListener('click', event => {
  uiSound(tapSound);
  let x = event.clientX;
  let y = event.clientY;
  clickEffect(x, y); // Tap Effect
});

// Hover Sound
const hoverSound = new Audio('media/ui-sounds/hover.ogg');
document.querySelectorAll('.s-hover').forEach(element => {
  element.addEventListener('mouseenter', () => uiSound(hoverSound));
});

// Click Sound
const clickSound = new Audio('media/ui-sounds/click.ogg');
document.querySelectorAll('.s-click').forEach(element => {
  element.addEventListener('click', () => uiSound(clickSound));
});

// Ding Sound
const dingSound = new Audio('media/ui-sounds/ding.ogg');
document.querySelectorAll('.s-ding').forEach(element => {
  element.addEventListener('click', () => uiSound(dingSound));
});

// Loading Sound
const loadSound = new Audio('media/ui-sounds/load.ogg');
document.querySelectorAll('.s-load').forEach(element => {
  let loading = false;
  element.addEventListener('mouseover', () => {
    loading = true;
  });
  element.addEventListener('mouseout', () => {
    loading = false;
  });
  element.querySelector('.progress').addEventListener('transitionstart', () => {
    if (loading) {
      uiSound(loadSound)
    }
  });
});
// #endregion

document.querySelectorAll('img').forEach(element => {
  element.addEventListener('dragstart', event => {
    event.preventDefault();
  });
});
document.querySelectorAll('a').forEach(element => {
  element.addEventListener('dragstart', event => {
    event.preventDefault();
  });
});