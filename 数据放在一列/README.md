# 数据放在一列
该脚本只是为了针对性的解决将这类的数据格式转化为
| AU           |                |                |           |         |
|--------------|----------------|----------------|-----------|---------|
| Abdullahi,SB | Chamnongthai,K | Bolon-Canedo,V | Cancela,B |         |
| Tong,JY      | Tang,SY        | Zheng,JD       | Zhao,HJ   | Wu,Y    |
| Li,GC        | Xu,SX          | Zhang,LY       | Sun,L     | Jiang,R |
下面的这样的数据格式
| AU             |
|----------------|
| Abdullahi,SB   |
| Chamnongthai,K |
| Bolon-Canedo,V |
| Cancela,B      |
| Tong,JY        |
| Tang,SY        |
| Zheng,JD       |
| Zhao,HJ        |
| Wu,Y           |

# 数据实例
<AU.xlsx>文件就是输入的数据格式，在运行脚本的时候只需要将代码中的第九行双引号中的内容修改即可
输出的文件会在该目录下，也可以修改第24行中引号中的内容来修改生成的文件的名字
