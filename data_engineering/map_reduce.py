# Generated with chat gpt4o

from collections import defaultdict

# Función map


def map(document: str):
    for word in document.split():
        # Normalizamos las palabras (por ejemplo, eliminamos puntuación y las hacemos minúsculas)
        word = ''.join(char for char in word if char.isalnum()).lower()
        yield (word, 1)

# Función reduce


def reduce(word: str, partial_counts: iter):
    total = sum(partial_counts)
    return (word, total)


# Texto proporcionado
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vulputate turpis ac felis aliquet, aliquet aliquet
"""

# Aplicación de la función map
mapped = []
for result in map(text):
    mapped.append(result)

# Agrupamos los resultados por palabra
grouped = defaultdict(list)
for word, count in mapped:
    grouped[word].append(count)

# Aplicación de la función reduce
reduced = {}
for word, partial_counts in grouped.items():
    reduced[word] = reduce(word, partial_counts)

# Mostramos los resultados
for word, count in reduced.items():
    print(f"{word}: {count}")
