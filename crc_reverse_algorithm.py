import binascii, struct, random, string
import requests
import base64
import time

# 1. 변수 초기화
# 1-1.  hexid 초기화
hexid = "2019103232".encode('utf-8').hex()
print("hexid :", hexid)
# 1-2.   hex_g_prefix 초기화
hex_g_prefix = requests.get("http://pwnlab.kr:2575/prefix").text.encode('utf-8').hex()
print("hex_g_prefix :", hex_g_prefix)
print()

# 2. 중간에 도출된 crc32(hex_g_prefix+hexid)값을 사용하여, 이후에 사용될 초기 divisor 구하기
first_divisor = binascii.crc32(bytes.fromhex(hex_g_prefix+hexid))^0xffffffff
print("first_divisor :",hex(first_divisor))


# 3. hexcode를 구해보자. 4byte의 hexcode를 AB/CD/EF/GH로 두자.
# 3-1. AB를 구하자.
first_divisor_front = first_divisor>>8 # first_divisor 처음 3바이트
print("first_divisor_front :",hex(first_divisor_front))
first_divisor_back = first_divisor&0xff # first_divisor 끝 1바이트
print("first_divisor_back :",hex(first_divisor_back))

hexcode=(0x3c^first_divisor_back)<<24 # table index와 first_divisor_back를 xor한 것이 AB일 것이다.
print("AB :", hex(0xdf^first_divisor_back))
print()

# 3-2. CD를 구하자.
second_divisor = 0x2f6f7c87^first_divisor_front # crc32 table의 값과 first_divisor_front를 xor하여 second_divisor를 구한다.
print("second_divisor :",hex(second_divisor))
second_divisor_front = second_divisor>>8 # second_divisor 처음 3바이트
print("second_divisor_front :",hex(second_divisor_front))
second_divisor_back = second_divisor&0xff # second_divisor 끝 1바이트
print("second_divisor_back :",hex(second_divisor_back)) 

hexcode^=(0xa0^second_divisor_back)<<16 # table index와 second_divisor_back xor한 것이 CD일 것이다.
print("CD :", hex(0xa0^second_divisor_back))
print()

# 3-3. EF를 구하자.
third_divisor = 0xd6d6a3e8^second_divisor_front
print("third_divisor :",hex(third_divisor))
third_divisor_front = third_divisor>>8 # third_divisor 처음 3바이트
print("third_divisor_front :",hex(third_divisor_front))
third_divisor_back = third_divisor&0xff # third_divisor 끝 1바이트
print("third_divisor_back :",hex(third_divisor_back))

hexcode^=(0x4f^third_divisor_back)<<8 # table index와 third_divisor_back xor한 것이 EF일 것이다.
print("EF :", hex(0x4f^third_divisor_back))
print()

# 3-4. GH를 구하자.
fourth_divisor = 0xe6635c01^third_divisor_front
print("fourth_divisor :",hex(fourth_divisor))
fourth_divisor_front = fourth_divisor>>8
print("fourth_divisor_front :",hex(fourth_divisor_front))
fourth_divisor_back = fourth_divisor&0xff
print("fourth_divisor_back :",hex(fourth_divisor_back))

hexcode^=(0x34^fourth_divisor_back) # table index와 fourth_divisor_back xor한 것이 GH일 것이다.
print("GH :", hex(0x34^fourth_divisor_back))
print()
print("hexcode :",hex(hexcode)[2:])
print()

# 4. 답 확인
datas = {
    "student_id" : "2019103232",
    "hexcode" : hex(hexcode)[2:],
}

response = requests.post("http://pwnlab.kr:2575/auth", json=datas).text
print("status code :", response)

