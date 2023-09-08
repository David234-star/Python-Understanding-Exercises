# Solution 1

str_x = "Ranadheer is good programmer, but Ranadheer is not good person."

words = str_x.split()
repeated = []

seen_words = set()  # it will store unquie words, so that's why it will be used as for encountering the repeated words

for word in words:
    if word in seen_words and word not in repeated:
        repeated.append(word)
    else:
        seen_words.add(word)

if repeated:
    print("Repeated words are: ", repeated)

else:
    print("No repeated words found.")


# Solution 2

cnt = str_x.count("Ranadheer")  # type: ignore

print("Ranadheer is repeated", cnt)
