# 题目内容

# 塔子哥是一位喜欢破译密码的侦探，他经常接到一些奇怪的案件，让他用自己的智慧来解决。有一天，他收到了一封神秘的信件，里面写着一行英文句子，里面包含英文字母，空格以及 ,.?;! 等若干种标点符号。信件没有署名，也没有任何其他的线索。塔子哥觉得这很可疑，于是他决定仔细研究这封信件。

# 他发现这行句子很奇怪，它看起来像是一个正常的英文句子，但是却没有任何逻辑或语法上的意义。他怀疑这是一种暗号，于是他想到了一个方法来解开它。他想将句子内每个单词进行倒序，并将倒序后的语句的输出。他认为这样就能看出信件的真正含义。

# 但是这个句子可能很长，一个个处理很麻烦，于是他想到了一个更好的办法。他想到了编写一个程序来帮助他快速解决这个问题，但是塔子哥的电脑不在身边，你能帮他编写一个程序解决这个问题吗？
# 输入描述

# 输入为一个字符串 SS 。（ 1≤S.length()≤10001≤S.length()≤1000 ）
# 输出描述

# 输出为完成处理以后的字符串。
# 样例
# 样例一

# 输入

# olleh dlroW!

# 输出

# hello World!

# 样例二

# 输入

# i ma! at iz eg .

# 输出

# i am! ta zi ge .


from string import *
s = input()
words = s.split()
s = ' '.join([w[::-1] if w[-1] in ascii_lowercase else w[:-1][::-1]+w[-1] for w in words])
print(s)