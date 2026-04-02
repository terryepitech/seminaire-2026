import { Timer } from './timer.js';
import { Storage } from './storage.js';

const startButton = document.getElementById('startButton');
const resetButton = document.getElementById('resetButton');
const timerValue = document.querySelector('.timer-value');
const statusLabel = document.querySelector('.status-label');

const storage = new Storage();
const timer = new Timer(storage.getDefaultDuration());

function updateDisplay() {
    timerValue.textContent = timer.formatRemaining();
    statusLabel.textContent = timer.modeLabel();
}

startButton.addEventListener('click', () => {
    timer.start();
    updateDisplay();
});

resetButton.addEventListener('click', () => {
    timer.reset();
    updateDisplay();
});

document.addEventListener('DOMContentLoaded', () => {
    updateDisplay();
});
