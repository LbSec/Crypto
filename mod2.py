AD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

List = [104,290,356,313,262,337,354,229,146,297,118,373,221,359,338,321,288,79,214,277,131,190,377]

flag = ""
for items in List:
    newItem = pow(items, -1, 41)
    if newItem in range (1,38):
        flag += (AD[newItem-1])
print("picoCTF{" + flag + "}")
        
