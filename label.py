####################################################################################################
"""
클래스 관련 코드.
labels : 대분류, 소분류, 지역라벨, 대분류 - 소분류 라벨
label2id, id2label : 클래스와 index 변환 함수들
"""
####################################################################################################
#For predict
big_label = ['정치', '경제', '사회', '문화', '국제', '스포츠', 'IT_과학']
small_label = ['국회_정당', '북한', '선거', '외교', '청와대', '행정_자치', '골프', '농구_배구', '야구_메이저리그',
               '야구_일본프로야구', '올림픽_아시안게임', '축구_월드컵', '축구_한국프로축구', '축구_해외축구',
               '교육_시험', '날씨', '노동_복지', '미디어', '사건_사고', '여성', '의료_건강', '장애인', '환경',
               '미술_건축', '방송_연예', '생활', '요리_여행', '음악', '전시_공연', '종교', '출판', '학술_문화재',
               '러시아', '미국_북미', '아시아', '유럽_EU', '일본', '중국', '중남미', '중동_아프리카', '국제경제',
               '금융_재테크', '무역', '반도체', '부동산', '산업_기업', '서비스_쇼핑', '외환', '유통', '자동차',
               '자원', '증권_증시', '취업_창업', '과학', '모바일', '보안', '인터넷_SNS', '콘텐츠']
region_label = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '울산', '전남', '전북',
                '제주', '지역일반', '충남', '충북']
BS_label = {'정치': ['국회_정당', '북한', '선거', '외교', '정치일반', '청와대', '행정_자치'],
             '스포츠': ['골프', '농구_배구', '스포츠일반', '야구_메이저리그', '야구_일본프로야구', '올림픽_아시안게임', '축구_월드컵', '축구_한국프로축구', '축구_해외축구'],
             '사회': ['교육_시험', '날씨', '노동_복지', '미디어', '사건_사고', '사회일반', '여성', '의료_건강', '장애인', '환경'],
             '문화': ['문화일반', '미술_건축', '방송_연예', '생활', '요리_여행', '음악', '전시_공연', '종교', '출판', '학술_문화재'],
             '국제': ['국제일반', '러시아', '미국_북미', '아시아', '유럽_EU', '일본', '중국', '중남미', '중동_아프리카'],
             '경제': ['경제일반', '국제경제', '금융_재테크', '무역', '반도체', '부동산', '산업_기업', '서비스_쇼핑', '외환', '유통', '자동차', '자원', '증권_증시', '취업_창업'],
             'IT_과학': ['IT_과학일반', '과학', '모바일', '보안', '인터넷_SNS', '콘텐츠'],
             '지역': ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '울산', '전남', '전북', '제주', '지역일반', '충남', '충북']}

big_label2id = {label: i for i, label in enumerate(big_label)}
big_id2label = {i: label for label, i in big_label2id.items()}

small_label2id = {label: i for i, label in enumerate(small_label)}
small_id2label = {i: label for label, i in small_label2id.items()}

region_label2id = {label: i for i, label in enumerate(region_label)}
region_id2label = {i: label for label, i in region_label2id.items()}

#For train
str_labels = ['국회_정당', '북한', '선거', '외교', '정치일반', '청와대', '행정_자치', '골프', '농구_배구',
       '스포츠일반', '야구_메이저리그', '야구_일본프로야구', '올림픽_아시안게임', '축구_월드컵',
       '축구_한국프로축구', '축구_해외축구', '교육_시험', '날씨', '노동_복지', '미디어', '사건_사고',
       '사회일반', '여성', '의료_건강', '장애인', '환경', '문화일반', '미술_건축', '방송_연예', '생활',
       '요리_여행', '음악', '전시_공연', '종교', '출판', '학술_문화재', '국제일반', '러시아',
       '미국_북미', '아시아', '유럽_EU', '일본', '중국', '중남미', '중동_아프리카', '경제일반',
       '국제경제', '금융_재테크', '무역', '반도체', '부동산', '산업_기업', '서비스_쇼핑', '외환',
       '유통', '자동차', '자원', '증권_증시', '취업_창업', 'IT_과학일반', '과학', '모바일', '보안',
       '인터넷_SNS', '콘텐츠', '강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산',
       '울산', '전남', '전북', '제주', '지역일반', '충남', '충북']

labels = [1004000, 1001000, 1002000, 1003000, 1007000, 1006000, 1005000, 7001000, 7010000, 7013000, 7002001, 7002002, 7006000, 7005000, 7003003, 7003001,
        3004000, 3001000, 3005000, 3008000, 3006000, 3010000, 3002000, 3007000, 3009000, 3003000, 4011000, 4006000, 4007000, 4001000, 4008000, 4003000,
        4009000, 4004000, 4005000, 4010000, 5009000, 5005000, 5003000, 5006000, 5008000, 5001000, 5002000, 5007000, 5004000, 2014000, 2013000, 2008000,
        2001000, 2009000, 2010000, 2005000, 2012000, 2002000, 2003000, 2011000, 2004000, 2006000, 2007000, 8006000, 8001000, 8003000, 8002000, 8005000,
        8004000, 6001000, 6002000, 6003000, 6004000, 6005000, 6006000, 6007000, 6008000, 6009000, 6010000, 6011000, 6012000, 6015000, 6013000, 6014000]

labels = list(map(str, labels))

label2id = {label: i for i, label in enumerate(labels)}
id2label = {i: label for label, i in label2id.items()}