class 책:
    def __init__(self, 제목, 저자):
        self.제목 = 제목
        self.저자 = 저자
    def 소개하기(self):
        print(f"제목: {self.제목}/저자: {self.저자}")
채식주의자 = 책("채식주의자","한강")
채식주의자.소개하기()