import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html = file.read()

        text_without_tags = re.sub(r'<.*?>', '', html)
        meaningful_lines = [line.strip() for line in text_without_tags.splitlines() if line.strip()]

        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write("\n".join(meaningful_lines))

        print(f"Очищенный текст теперь тут: {result_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {html_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

delete_html_tags('draft.html')
