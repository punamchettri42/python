'''
program to generate multiplication table from 2 to 20 and write it to different files place this file in a folder for a 13 years old

'''
for i in range(2,21):
    with open(f"tables/multiplication_table_of_{i}", 'w' ) as f:
        for j  in range(1, 11):
            f.write(f"{i}x{j}={i*j}")
    break