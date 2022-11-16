#program to implement expert system using forward chaining
global facts
global is_changed

is_changed = True
facts = [["verterbate","duck"],["flying","duck"],["mammal","cat"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts+=[fact]
        is_changed = True
while is_changed:    
    is_changed = False
    for A1 in facts:
        if A1[0] == "mammul":
            assert_fact(["verterbate",A1[1]])
        if A1[0] == "verterbate":
            assert_fact(["animal",A1[1]])
        if A1[0] == "verterbate" and ["flying",A1[1]] in facts:
            assert_fact(["bird",A1[1]])
print(facts)
