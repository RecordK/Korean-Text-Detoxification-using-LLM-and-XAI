# import pandas as pd
# # data = open('/home/jupyter/Korean_Text_Detoxification/results/converted_sentences_NoExamples.txt','r') 
# data = open('/home/jupyter/Korean_Text_Detoxification/results/Final_noexams.txt','r') 
# lines = data.readlines()
# ori,detox = [],[]

# for line in lines:
#     if '기존 댓글' in line:
#         ori.append(line)
#     elif '순화' in line:
#         detox.append(line)
# print(len(ori),len(detox))

# with open('/home/jupyter/Korean_Text_Detoxification/results/Final_noexams_clear.txt', 'w') as f:
#     for line in range(len(detox)):
#         f.write(ori[line])
#         f.write(detox[line])
#         f.write('\n')
        
# import pandas as pd

# # .csv 파일 불러오기
# df = pd.read_csv("/home/jupyter/Korean_Text_Detoxification/results/final_ours.csv")

# with open('/home/jupyter/Korean_Text_Detoxification/results/Final_ours_clear.txt', 'w') as f:
#     for line in range(len(df)):
#         f.write(f'기존 문장: {df.iloc[line,1:][0]}')
#         f.write('\n')
#         f.write(f'순화된 문장: {df.iloc[line,1:][1]}')
#         f.write('\n')
#         f.write('\n')



import pandas as pd
data = open('/home/jupyter/Korean_Text_Detoxification/results/dddd.txt','r') 
lines = data.readlines()
ori,detox = [],[]

for line in lines:
    # if '순화' in line:
    if line.strip():
        detox.append(line)

with open('/home/jupyter/Korean_Text_Detoxification/results/detoxOnly_nomask.txt', 'w') as f:
    for line in range(len(detox)):
        f.write(detox[line])
        # f.write('\n')