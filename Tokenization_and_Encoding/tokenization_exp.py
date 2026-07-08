import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

text = ("Albany is a very dangerous city !!")

# text = 3
for s in text:
    token_ids = encoder.encode(str(s))

    print(f"Token-Id of {s} - {token_ids}")

org_text = encoder.decode(token_ids)

print(f"decoded original text :: {org_text}")