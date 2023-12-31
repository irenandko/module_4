                  # 4.1 GIT(начало проекта)

# пример оптимизации кода без вложенных циклов, соответственно, ассимптотическая сложность кода гораздо меньше и не приведет к виду n**2, если все символы уникальны
s = 'aab'
syms_count = {}
for syms in s:
    syms_count[syms]=syms_count.get(syms,0)+1

print(syms_count)

# git init - инициализация проекта
# git status - чек несохраненных файлов (красные не сохранены)
# git add .   - добавить все, или прописать нужные
# git commit   - сохранение изменений + коммент


#                 4.2 HTML & CSS
# html - язык гипертекстовой разметки для верстки веб страниц
# у html есть теги - они создают способ отображения инфы в браузере
# парные теги - открытие и закрытие, но есть одинарные теги


# СТРУКТУРА    ! (напечатать) и нажать Tab

# head - настройки страницы
# body - все, что будет отображаться
# всего есть h6 порядков, но если h1 - единственный заголовок, то заголовков другого порядка будет хоть сколько

# h - заголовки
# p - тексты
# a href='' - ссылка с текстом
# div - контейнер, группировать несколько элементов