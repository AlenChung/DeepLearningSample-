admins = {'Justin', 'caterpillar'}  # 建立 set
users = {'momor', 'hamini', 'Justin'}
print('Justin' in admins)  # 是否在站長群？
print(admins & users)      # 同時是站長群也是使用者群的？
print(admins.intersection(users))      
print(admins | users)
print(admins.union(users))      # 是站長群或是使用者群的？
print(admins - users)      # 站長群但不使用者群的？
print(admins.difference(users))
print(admins^users) # XOR

for item in users:
    print(item)

admins = {'WeiYen', 'WeiYen', 'caterpillar'}
print(admins) #{'WeiYen', 'caterpillar'}
#print(admins[0]) #TypeError: 'set' object does not support indexing
admins = ['WeiYen', 'WeiYen', 'caterpillar']
print(admins)
print(admins[0]) #works