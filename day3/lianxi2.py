# 练习2：百分制成绩转换为等级制成绩。
# 要求：
# 如果输入的成绩在90分以上（含90分）输出A；
# 80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；60分以下输出E。
score = float(input('请输入成绩：'))     # 将输入的数值导入score变量中
if score >100:           # 分支结构\
    grade = '无，您输入的分数无效'
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score <0:
    grade = '无，您输入的分数无效'
else:
    grade = 'E'
print('对应的等级是:', grade)           # 将结果用print函数打印到屏幕上