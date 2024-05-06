from typing import List
import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 如果一行只有一个单词，则靠左边
        if len(words) == 1:
                return [words[0] + " " * (maxWidth - len(words[0]))]
        
        # 如果所有单词都在第一行
        line_len = sum([len(word)+1 for word in words]) - 1
        if line_len <= maxWidth:
            return [" ".join(words)]

        # 如果能拆成多行，则切割出第一行的单词数组
        n = len(words)
        lines = []
        start = 0
        while start < n:
            line = []
            prelen = 0
            j = start
            while j < n:
                if prelen + len(words[j]) <= maxWidth:
                    line.append(words[j])
                    prelen = prelen + len(words[j]) + 1
                else:
                    lines.append(line)
                    start = j
                    break
                j = j + 1
            if j == n:
                lines.append(line)
                break


        def lineJustify(line: list[str]) -> str:
            if len(line) == 1:
                return line[0] + " " * (maxWidth - len(line[0]))

            total_word_len = sum([len(word) for word in line])
            total_space = maxWidth - total_word_len
            gap = len(line)-1 # 有几个间隔
            b = total_space % gap  # 多余出来的空格数目
            avg_space_num = total_space / gap #平均每个间隔要插入的空格数
            if b == 0:
                spaces = " " * int(avg_space_num)
                return spaces.join(line)
            else:
                a1 = math.ceil(total_space / gap)
                a2 = math.floor(total_space / gap)
                spaces = []
                for k in range(b):
                    spaces.append(" " * a1)
                for k in range(gap - b):
                    spaces.append(" " * a2)
                line_str = ''
                for i in range(len(line)):
                    if i < gap:
                        line_str = line_str + line[i] + spaces[i]
                    else:
                        line_str = line_str + line[i]
                return line_str
            

        result = []
        k = 0
        while k < len(lines):
            if k < len(lines) -1:
                result.append(lineJustify(lines[k]))
            #如果是最后一行
            if k == len(lines) -1:
                last_line_str = " ".join(lines[k])
                result.append(last_line_str + " " * (maxWidth-len(last_line_str)))
            k = k + 1

        return result
    


print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))