let result = document.getElementById('main_result');
let result_caption = document.getElementById('result_caption');
let result_divisor = document.getElementById('result_divisor');

function uiSound(sound) {
  sound.currentTime = 0;
  sound.play()
    .then(() => { sound.muted = false; })
    .catch(() => { sound.muted = true; });
}

let animArea = document.createElement('div');
animArea.id = 'animation-area';
document.body.appendChild(animArea);

function clickEffect(x, y) {
  let effect = document.createElement('div');
  effect.style.left = `${x}px`;
  effect.style.top = `${y}px`;
  effect.classList.add('click-effect');
  effect.addEventListener('animationend', () => effect.remove());
  animArea.appendChild(effect);
}

const primeSound = new Audio('../media/ui-sounds/success.ogg');
const notPrimeSound = new Audio('../media/ui-sounds/fail.ogg');
const errorSound = new Audio('../media/ui-sounds/error.ogg');
const tapSound = new Audio('../media/ui-sounds/tap.ogg');
document.addEventListener('click', event => {
  uiSound(tapSound);
  let x = event.clientX;
  let y = event.clientY;
  clickEffect(x, y);
});

function clearResult() {
  result.textContent = '';
  result_caption.textContent = '';
  result_divisor.textContent = '';
}

function process() {
  let input = document.getElementById('number_input');
  let n = Number(input.value);
  let d = 2;
  if ((n.length != 0) && Number.isSafeInteger(n) && (n > 0)) {
    let l = Math.sqrt(n);
    if (n === 1) {
      result.textContent = 'NO';
      result_caption.textContent = 'It is NOT a PRIME number because it only has ONE factor';
    }
    else {
      let prime = true;
      for (; d <= l; ++d) {
        if (n % d === 0) {
          prime = false;
          break;
        }
      }
      if (prime) {
        result.textContent = 'YES';
        result_caption.textContent = 'It is a PRIME number';
        uiSound(primeSound);
      }
      else {
        result.innerHTML = 'NO';
        result_caption.textContent = 'It is NOT a PRIME number and is divisible by:';
        result_divisor.textContent = String(d);
        uiSound(notPrimeSound);
      }
    }
  }
  else {
    result.textContent = 'ERROR';
    result_caption.textContent = 'Invalid INPUT';
    uiSound(errorSound);
  }
}