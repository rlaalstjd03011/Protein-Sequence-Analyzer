# Protein Sequence Analyzer: Amino Acid Composition Tool
# 단백질 서열에서 **각 아미노산의 조성(빈도 및 비율)**을 분석하는 간단한 도구 만들기
# Bioinformatics에서 단백질 특성 파악, 비교 분석, 기초 통계 처리에 자주 사용됨

#FASTA 형식의 단백질 서열 파일을 읽는다

# 서열에서 각 아미노산의 등장 횟수와 비율을 계산한다

# 그 결과를 표와 그래프로 시각화한다

# (선택 확장) 아미노산 특성(예: 소수성, 극성 등)에 따른 그룹 분석

from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


sequence = ''
with open('p53 protein.fasta', 'r') as f:
        for line in f:
            if not line.startswith('>'):
                sequence += line.strip().upper()

counts = Counter(sequence) # counter : 한줄로 모든 개수들을 다 세줘서 엄청 유용함!
print(counts) # 아미노산 종류: 개수로 딕셔너리에 저장!

total = len(sequence)
print(f'Total numbers of Aminoacid: {total}')

for aminoacid, count in counts.items(): # counts.items():딕셔너리에 저장된 모든 (키,값)을 꺼내주는 함수
    ratio = count/total * 100
    print(f'{aminoacid}: {count}회, 비율:{ratio:.2f}%')

# pandas 이용해서 데이터 프레임 생성하기

data = [(aminoacid, count, count/total*100) for aminoacid, count in counts.items()] # 리스트 컴프리헨션: for문을 한줄로 표현함
df = pd.DataFrame(data, columns=['aminoacid', 'count', 'ratio']) # 데이터 프레임 생성(표 생성)
df = df.sort_values(by='ratio',ascending=False)  # 비율 기준으로 , 큰 값이 위에서부터 정렬해라!
df = df.reset_index(drop=True) # 인덱스 초기화!

'''df['ratio'] = df['ratio'].apply(lambda x:f'{x:.2f}%')
print(df)'''

# matplotlib을 이용한 시각화!
plt.bar(df['aminoacid'], df['count'])
plt.xlabel('aminoacid')
plt.ylabel('count')
plt.title('Amino Acid Composition(%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




