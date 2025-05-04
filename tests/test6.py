class Yes_or_no:
    yes : bool

def is_yes(y: Yes_or_no) -> bool:
    return y.yes

question = Yes_or_no(True)
answer = is_yes(question)

print(answer)