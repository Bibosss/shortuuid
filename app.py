import shortuuid

identifier = shortuuid.prefixed_uuid("LAB")
prefix, separator, suffix = identifier.partition("-")

assert prefix == "LAB" and separator == "-"
assert len(suffix) == 22
assert all(character in shortuuid.get_alphabet() for character in suffix)

print(f"Generated ID: {identifier}")
print("Prefix, suffix length, and alphabet checks passed.")
print(f"Library loaded from: {shortuuid.__file__}")
