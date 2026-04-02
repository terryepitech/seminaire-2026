"""
Pomodoro business logic module.
"""

DEFAULT_DURATIONS = {
    "work": 25 * 60,
    "short_break": 5 * 60,
    "long_break": 15 * 60,
}


def get_duration(mode):
    """Return the duration in seconds for the given mode."""
    return DEFAULT_DURATIONS.get(mode, DEFAULT_DURATIONS["work"])


def format_seconds(seconds):
    """Format seconds as MM:SS."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"
