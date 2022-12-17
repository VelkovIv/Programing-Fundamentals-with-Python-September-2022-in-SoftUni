number_of_electrons = int(input())
shell_of_electrons = []
shell_number = 0
while True :
    shell_number += 1
    current_electrons_shell = 2 * shell_number ** 2
    if number_of_electrons > current_electrons_shell :
        number_of_electrons -= current_electrons_shell
        shell_of_electrons.append(current_electrons_shell)
    elif number_of_electrons == current_electrons_shell:
        shell_of_electrons.append(number_of_electrons)
        break
    else:
        shell_of_electrons.append(number_of_electrons)
        break

print(shell_of_electrons)
