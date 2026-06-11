# 00_quiz.py

from __future__ import annotations

def main() -> None:

    #1) 기사 제목을 변수로 저장하고 출력
    title = "미국 기준금리 동결"
    print("== 1) 제목 변수 ==")
    print(title)
    print()
    
    # 2) 기사 메타정보 변수 저장 후 한 줄 출력
    date = "2026-02-07"
    category = "스포츠"
    views = 8700
    print("== 2) 메타정보 변수 ==")
    print(date, category, views)
    print()    
    
    # 2_1) 1만 이상 views일 경우 출력
    print("=2-1) 1만회 이상 클릭 시 출력 ==")
    if views > 10000:
        print("기준금리 기사 클릭 수 1만 회 돌파")
    else:
        print("조금 더 분발하세요")     
    print()   
    
    # 3) 기사 제목 목록(리스트) 만들고 첫 번째 출력
    titles = [
        "미국 기준금리 동결",
        "중국 경기 둔화 우려",
        "국제유가 급등",
    ]
    print("== 3) 제목 리스트 ==")
    print("첫 번째 제목:", titles[2])
    print("두 번째 제목:", titles[0])    
    print()
    
    # 4) 기사 1건 딕셔너리 만들고 title 출력
    article = {
        "title": title,
        "date": date,
        "category": category,
        "views": views,
    }
    print("== 4) 기사 딕셔너리 ==")
    print("딕셔너리 title:", article["title"])
    print()

    #4_1) 딕셔너리 조회수 출력
    
    print("==4-1) 조회수 출력 ==")
    print("딕셔너리 조회수:", article["views"])
    print()

# 5의 선제 조건) 함수를 만들어서 주요 기사 여부 판단하기
    def classify_article(views: int, threshold: int = 10000) -> str:
        """조회수 기준으로 주요/일반 분류"""
        return "주요 기사" if views >= threshold else "일반 기사"
    print()
    
    # 5) 주요기사여부 판단하기
    views = 12700
    print("== 5) 주요기사 여부 ==")
    if views >= 10000:
        print("주요 기사")
    else:
        print("일반 기사")
    print()

    # 5_0) 조회수가 높거나, 스포츠 기사라면 주요기사로 처리
    print("== 5-0) 조건부 주요기사 판별 ==")
    
    if (views >= 10000) and (category == "스포츠"):
        print("결과: 주요 기사로 송출합니다.")
    else:
        print("결과: 일반 기사입니다.")
    print()

    # 5_1)함수를 만들어서 주요 기사 여부 판단하기     
    print("== 5_1) 함수로 주요/일반 기사 판단 ==")
    print("분류:", classify_article(article["views"]))
    print()    
        
if __name__ == "__main__":
    main()