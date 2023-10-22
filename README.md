# crc32-preimage
## CRC32란?
CRC(Cyclic Redundancy Check)는 시리얼 전송에서 데이터의 신뢰성을 검증하기 위한 에러 검출 방법의 일종이다.<br><br>

## CRC32 역연산?
CRC32는 단방향 해시 함수로, 원본 데이터를 복원하는 데 필요한 정보가 체크섬으로서 데이터에 포함되지 않기 때문에 일반적으로는 역연산이 불가능하다.<br>
그리고 CRC는 일반적으로 암호화보다는 에러 검출을 위해 사용하므로 역연산을 하는 경우도 드물다.<br>
<br>
그러나 초기 divisor와 crc테이블을 아는 특수한 상황에서는 CRC 역연산이 가능한데,<br>
이 프로젝트에서는 이러한 특수 상황에서의 CRC 역연산을 수행한다. <br>
<br>
CRC의 동작 원리를 정확히 이해하기 위해 역연산 알고리즘을 작성하였다.<br><br>


## CRC32 역연산 그림
![crc32-reverse-illustration](https://github.com/yonding/crc32-preimage/assets/70754463/7654cafb-7763-4594-8816-b3e2681b6f54)
