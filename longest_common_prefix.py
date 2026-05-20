def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


strings = [
    "flower",
    "flow",
    "flight"
]

print("Longest Common Prefix:")
print(longest_common_prefix(strings))
