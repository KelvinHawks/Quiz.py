print('welcome to my computer quiz!')

playing = input('Do yo want to play? ')

if playing.lower() != 'yes':
    quit()

print('Okay lets play')
score = 0

answer = input('What does the cpu stand for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input('What does the GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input('What does the RAM stand for? ')
if answer.lower() == 'random access memory':
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input('What does the PSU stand for? ')
if answer.lower() == 'power supply':
    print('correct!')
    score += 1
else:
    print('incorrect')

print('you got ' + str(score) + ' questions correct!')
print('you got ' + str((score / 4) * 100) + '%')


