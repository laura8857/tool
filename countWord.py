str = 'DATA RARELY SPEAKS for itself. Not cogently, anyway. That’s what tables, graphs, and diagrams are for. The right visualization can focus a jumbled heap of facts and figures into something concise, captivating, informative, persuasive, or misleading. The challenge is choosing how best to showcase the data you’re interested in—and your options are surprisingly numerous, as designer Nathan Yau demonstrates in a recent series of 25 visualizations. Every graphic is based on the same data set—life expectancy figures, by country, from the World Health Organization—but each tells a slightly different story.\
Yau says most of his designs begin with questions. Answering them leads to a tighter focus on a given data set. “This leads to more questions, usually, and different chart types are better at answering some questions than others,” he says. Asking the WHO data set a question like “what’s the median” might lead to a bar chart comparing countries with the highest and lowest life expectancy. At a glance, you can see just how sizable a different there is between a country like Japan, which has the highest life expectancy, and Sierra Leone, which has the lowest.\
A more refined question, like “which countries experience the most fluctuations,” gives rise to a very different visualization. Take the chart below. For this graphic, Yau traced the life expectancy trend for each country with a line and overlaid them atop each other. The result is a jumbled mess, save for one conspicuous outlier: Haiti’s trend line plummets in 2010, a reaction to that year’s devastating earthquake. It’s a very specific visualization—one that would be silly to use in reference to any other country.\
Information designers have a saying: “Let the data speak for itself.” But Yau says presenting data is more complicated than that. “It’s a nice idea in theory—you want to visualize the data, and not get in the way,” he says. But without a point of view, data tends to ramble. A designer’s responsibility is to impose that point of view. Giving information shape has a powerful influence on the way viewers process it—designers must decide what they want that shape to say.'

# # 方法1 使用count
# print(str.count('in'))
#
# # 方法2 使用regular expression
# import re
#
# print(len(re.findall('in', str)))
#
# # 方法3 使用切割法查找
# str_list = str.split(' ')
# count = 0
# for item in str_list:
#     if item == 'in':
#         count += 1
# print(count)

# 方法4使用set找自己統計所有字串的個數
str_list = str.split(' ')
myset = set(str_list)  # 將str_list內的值找出不重複的資料
for item in myset:
    print("%s: %s" % (item, str_list.count(item)))