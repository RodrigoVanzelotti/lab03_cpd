'''Função RADIX SORT contém subfunções
- Função para
- Counting Sort
'''
def radix_sort_msd(strings, radix=256, cutoff=10):
    def key_value(string, position):
        return ord(string[position]) if position < len(string) else 0

    def counting_sort(strings, position):
        count = [0] * (radix + 1)
        n = len(strings)
        output = [None] * n

        for i in range(n):
            count[key_value(strings[i], position)] += 1

        for r in range(radix):
            count[r + 1] += count[r]

        for i in range(n - 1, -1, -1):
            char_pos = key_value(strings[i], position)
            output[count[char_pos] - 1] = strings[i]
            count[char_pos] -= 1

        for i in range(n):
            strings[i] = output[i]

    def msd_radix_sort(strings, low, high, position):
        if high <= low + cutoff:
            # Usar Insertion Sort para partições pequenas
            insertion_sort(strings, low, high, position)
            return

        counting_sort(strings[low:high + 1], position)

        char_pos = key_value(strings[low], position)
        start = low
        for r in range(radix):
            end = low + counting_sort(strings[low:high + 1], position, char_pos)
            msd_radix_sort(strings, start, end - 1, position + 1)
            start = end

    def insertion_sort(strings, low, high, position):
        for i in range(low + 1, high + 1):
            j = i
            while j > low and strings[j] < strings[j - 1]:
                strings[j], strings[j - 1] = strings[j - 1], strings[j]
                j -= 1

    msd_radix_sort(strings, 0, len(strings) - 1, 0)
    return strings


if __name__ == '__main__':
    strings = ["apple", "banana", "grape", "orange", "cherry", "apricot"]
    sorted_strings = radix_sort_msd(strings)
    print(sorted_strings)