strings = [“foo”, “card”, “bar”, “aaaa”, “abab”]

strings.sort(key=lambda x: len(set(x)))