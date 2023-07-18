# 4.1 GIT (начало проекта)

# пример оптимизации кода без вложенных циклов, соответственно, ассимптотическая сложность кода гораздо меньше и не приведет к виду n**2, если все символы уникальны
# s = 'aab'
# syms_count = {}
# for syms in s:
#     syms_count[syms]=syms_count.get(syms,0)+1
#
# print(syms_count)

# git init - инициализация проекта
# git status - чек несохраненных файлов (красные не сохранены)
# git add .   - добавить все, или прописать нужные
# git commit   - сохранение изменений + коммент


def palindrome(slovo):
    if slovo==slovo[::-1]: return True
    else: return False

slovo = input('Введите слово для проверки на пaлиндром: ').lower()
print(palindrome(slovo))










