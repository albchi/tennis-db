import random



# constants
db_name = "db_tennis"
tb_name = "tb_tennis"
repeat_num = 1000000


# drop table
print(f"DROP DATABASE {db_name};")

# create table
print(f"CREATE DATABASE {db_name};")
print(f"\c {db_name};")
print(f"CREATE TABLE {tb_name} (ID SERIAL PRIMARY KEY, FN VARCHAR(255), LN TEXT, DOB DATE, CITY TEXT, RATING FLOAT);")

# populate table

a_fn = ["Al", "Bob", "Charles" "Dan", "Ed", "Frank", "Gary", "Henry", "Ion", "Jerry", "Kilroy", "Mike", "Nick", "Offr", "Pete", "Quincy", "Rob", "Stan", "Tom", "Ulf", "Victor", "Wagner", "Yincy", "Zoe"]

a_ln = ["Smith", "Wang", "Torres", "Mofidian", "Shira", "Lee", "Walker", "Jones", "Stranky", "Maler", "Singn", "Gonzalez", "Rublinski"]

a_ratings = ["3.0", "3.5", "4.0"]

a_city = ["San Francisco", "Los Angeles", "New York", "Santa Clara", "San Jose", "Mountain View", "Sunnyvale", "Palo Alto", "Los Altos"]


for _ in range(repeat_num):
    yy =  random.randint(1980,2010)
    mm =  random.randint(1,12)
    dd =  random.randint(1,30)
    dob =  str(yy) + "-" + str(mm) + "-" + str(dd)


    fn =  a_fn[random.randint(0,len(a_fn)-1)]
    ln =  a_fn[random.randint(0,len(a_ln)-1)]
    rating =  a_ratings[random.randint(0,len(a_ratings)-1)]
    city =  a_city[random.randint(0,len(a_city)-1)]
    # works
    #print(f"INSERT INTO {tb_name} (FN, LN, CITY, RATING) VALUES ( '{fn}', '{ln}', '{city}', {rating});")
    print(f"INSERT INTO {tb_name} (FN, LN, DOB, CITY, RATING) VALUES ( '{fn}', '{ln}', '{dob}', '{city}', {rating});")
