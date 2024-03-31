# 字符串

## 字符串格式化

- %
- Template/subtitle()
- format() {}
- f  简写方式 字段与变量名相同

格式字符串 分三部分 都可选

- 替换字段名 索引或标识符，还可以指定值的特定部分
- 转换标志 `!` r(表示repr)、s(表示str)、a(表示ascii) 如果指定转换标志，将先进行转换再做格式设置
- 格式说明符 `:`后的字符串 包括格式类型、字段宽度和精度、符号位置、千位分隔符、对齐方式和填充方式
  - 格式类型 s、d、e、f、b、o、x、c、g、n、F、G、%(百分比)
  - `.` 精度
  - 对齐方式 <(左对齐)、>(右对齐)、^(居中)
  - 填充字符用于扩充对齐说明符 放在对齐方式说明之前,且需要指明对齐方式
  - `=`指定将填充字符放在符号和数字之间 需要放在指定填充字符之后
  - 符号 +、-、空格
  - `#` 放在符号说明符和宽度之前 可以为数值加相应数制前缀
  - 千位分隔符 不能放在对齐说明符和宽度之前

## 字符串方法

- 子串查找 find()/index()/startswith()/endswith()/count()
- 字符串拼接/分割 jion()/split()
- 字符串替换 replace()/translate()
- 去除首尾字符 strip()
- 字符转换 lower()/upper()
- 字符判断 isalnum()/isdigit()/isspace()/isnumeric()