# The String Split
# text="I am going to Kundapura"
# split_string=text.split(" ")
# print(split_string)

# text="arn:partition:service:region:account-id:resource-type/resource-id"
# split_string=text.split("/")
# print(split_string)

# # if we need particular data
# text="arn:partition:service:region:account-id:resource-type/resource-id"
# split_string=text.split("/")
# print(split_string[1])


# text="arn:partition:service:region:account-id:resource-type/resource-id"
# split_string=text.split(":")
# print(split_string)

# text="arn:partition:service:region:account-id:resource-type/resource-id"
# split_string=text.split(":")
# print(split_string[2])

text ="arn:aws:iam::123456789012:server-certificate/division_abc/subdivision_xyz/ProdServerCert"
split_string=text.split("/")
print(split_string)
print(split_string[3])
print(len(split_string))  # it will