# Функция для прочтения текст из файла 1.docx и возвращения его в виде строки. [26-04-12 - 15:03:56]

from docx import Document
def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

# Функция которая заменяет все [n] на строку с индексом n в списке (список передается в эту функцию) [26-04-12 - 15:03:56]

def replace_placeholders(text, replacements, placeholder_format='[{}]'):
    for i, replacement in enumerate(replacements):
        placeholder = placeholder_format.format(i)
        text = text.replace(placeholder, replacement)
    return text

# Функция которая изменяет файл (путь к файлу передается в эту функцию) основываясь на result из 25 строки (результат замены) [26-04-12 - 15:12:56]

def write_docx(fpath, text, log = True):
    doc = Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)
    doc.save(fpath)
    if log:
        print(f'\nФайл сохранен по пути: {fpath}')

# Пример использования функций [26-04-12 - 15:10:56]

mlp, mpath      = [' m - main, l - list, p - parameter ', 'Ольги', 'Долгопрудный', '88005553535',
'Легенда', 'которая учится в лучшем ВУЗе Россиии - МФТИ'], '/home/codespace/etc/tmp/github/1/'
spath, epath    = mpath + 'a.docx', mpath + 'z.docx'
source          = read_docx(spath)
result          = replace_placeholders(source, mlp)
print(source, result, sep = '\n\n--------------------------------------------------------------\n\n')
write_docx(epath, result)

''' Ошибки при выполнении кода и их решения [26-04-12 - 15:03:56] '''

''' Traceback (most recent call last):
  File '/home/codespace/etc/tmp/github/1/main.py', line 2, in <module>
    from docx import Document
ModuleNotFoundError: No module named 'docx' '''

# Для решения этой проблемы необходимо установить библиотеку python-docx, которая позволяет работать с файлами .docx. Вы можете установить ее с помощью pip (pip install python-docx)