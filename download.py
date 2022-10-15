# 유튜브 동영상 다운로드 받는 코드
# pip install pytube 를 먼저한다.
import os
import sys
from pytube import YouTube
DownlodaFolder = 'C:/youtubeDownKYJ' # 다운로드할 폴더
def clear():
    os.system('cls')

while True:
    urls = []# url 지정
    while True:
        clear()
        print('다운로드할 유튜브 영상의 url을 넣고 엔터를 클릭하시오.')
        print('url 입력을 그만하고 싶다면 "end"를 입력 후 엔터를 클릭하면 다운로드가 시작됩니다.\n')
        url=input(f' [{len(urls)+1}] 번째 입력 : ')
        if url == 'end':
            break
        urls.append(url)
    clear()
    for idx,url in enumerate(urls):
        try:
            video = YouTube(url)
            clip = video.streams.get_highest_resolution() 
            clip.download(DownlodaFolder)
            print(f'==============[ {idx+1} ]==============')
            print('영상 제목 : ',video.title) # 영상 제목
            print('영상 제작자 : ',video.author) # 영상 제작자
            print('영상 업로드일 : ',video.publish_date) # 영상 업로드일자
            print('영상 조회수 : ',video.views) # 영상 조회수
            #print('영상 설명 : ',video.description) # 영상의 설명 (태그포함)
        except:
            print(f'!!!!!!! {idx+1}번째 입력한 {url}은 없는 주소 입니다.')
            pass
    while True:
        print('\n=================================\n')
        print('다운로드가 모두 끝났습니다. 파일은 C드라이브 youtubeDownKYJ폴더에 저장되었습니다.')
        print('\n1. end 입력시 프로그램 종료')
        print('\n2. again 입력시 처음으로 돌아가기')
        x=input('\n입력 : ')
        if x.lower()=='end':
            sys.exit()
        elif x.lower()=='again':
            break
        else:
            clear()