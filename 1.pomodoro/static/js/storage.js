export class Storage {
    constructor() {
        this.key = 'pomodoro-settings';
    }

    getDefaultDuration() {
        const stored = this.read();
        return stored?.duration ?? 25 * 60;
    }

    read() {
        try {
            const value = window.localStorage.getItem(this.key);
            return value ? JSON.parse(value) : null;
        } catch (error) {
            return null;
        }
    }

    write(data) {
        try {
            window.localStorage.setItem(this.key, JSON.stringify(data));
        } catch (error) {
            // ignore storage errors
        }
    }
}
