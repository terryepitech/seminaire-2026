export class Timer {
    constructor(durationSeconds = 25 * 60) {
        this.duration = durationSeconds;
        this.remaining = durationSeconds;
        this.running = false;
        this.mode = 'work';
    }

    start() {
        this.running = true;
    }

    pause() {
        this.running = false;
    }

    reset() {
        this.remaining = this.duration;
        this.running = false;
    }

    formatRemaining() {
        const minutes = Math.floor(this.remaining / 60);
        const seconds = this.remaining % 60;
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }

    modeLabel() {
        return this.mode === 'work' ? '作業中' : '休憩中';
    }
}
