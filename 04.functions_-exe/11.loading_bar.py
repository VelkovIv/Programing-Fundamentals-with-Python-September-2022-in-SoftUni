def loding_bar(num) :
    if num == 100 :
        return f'100% Complete!\n[%%%%%%%%%%]'
    return f'{num}% [{"%" * (num // 10)}{"." * (10 - num // 10)}]\nStill loading...'


number = int(input())
print(loding_bar(number))
