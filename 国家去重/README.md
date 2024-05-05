# 国家去重
## 源数据格式
| C1+RP    |       |          |       |
|----------|-------|----------|-------|
| Thailand | Spain | Thailand |       |
| China    | China | China    | China |
| China    | China | China    | China |
| China    | China | China    |

## 转换后的数据格式
| C1+RP       |        |
|-------------|--------|
| Thailand    | Spain  |
| China       |        |
| China       |        |
| China       |        |
| China       |        |
| China       |        |
| South Korea |        |
| China       |        |
| China       | France |
| Japan       |        |
| Malaysia    | China  |

## 使用方法
同“数据放在第一列”文件夹中的脚本
