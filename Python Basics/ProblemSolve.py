inp = input()

numbers = inp.split()

num_1 = int(numbers[0]);
num_2 = int(numbers[1]);

mod_num_1 = num_1%10;
mod_num_2 = num_2%10;

sum = mod_num_1+mod_num_2;

print(sum)

