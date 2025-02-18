def lengthOfLongestSubstring(s: str) -> int:
    # Словарь для хранения последнего индекса, на котором встречался каждый символ.
    last_index = {}
    max_length = 0
    left = 0  # Левый указатель окна
    

    # Перебираем строку с правым указателем
    for right, char in enumerate(s):
        # Если символ уже встречался и его индекс находится в текущем окне 
        if char in last_index and last_index[char] >= left:
            # Перемещаем левый указатель за предыдущий индекс этого символа
            left = last_index[char] + 1
        # Обновляем последний индекс для текущего символа
        last_index[char] = right

        # Обновляем максимальную длину окна
        max_length = max(max_length, right - left + 1)

    return max_length


print(lengthOfLongestSubstring('abcabcbb'))
