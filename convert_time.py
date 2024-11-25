def seconds_to_time(seconds):
    if 0 <= seconds < 8640000:
        days, remainder = divmod(seconds, 24 * 60 * 60)
        hours, remainder = divmod(remainder, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        day_word = "День" if days % 10 == 1 and days % 100 != 11 else \
            "День" if 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20) else "Дней"

        time_str = f"{str(days)} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        return time_str
    else:
        return "Число должно быть больше или равно 0 и меньше 8640000."

example_seconds = 5673345
print(seconds_to_time(example_seconds))
