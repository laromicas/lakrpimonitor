
TIME_DURATION_UNITS = (
    ('week', 60*60*24*7),
    ('day', 60*60*24),
    ('hour', 60*60),
    ('min', 60),
    ('sec', 1)
)

def human_time_duration(seconds, trim=5):
    if seconds == 0:
        return 'inf'
    parts = []
    count = 1
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            count += 1
            parts.append('{} {}{}'.format(amount, unit, "" if amount == 1 else "s"))
        if count > trim:
            break
    return ', '.join(parts)

def human_read_bytes(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"


# human_read_bytes(psutil.virtual_memory().total)