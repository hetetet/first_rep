import requests

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res=requests.get("http://nadocoding.tistory.com",headers=headers)
print("응답 코드: ", res.status_code)

res.raise_for_status()
print("웹 스크래핑 진행")
print(len(res.text))
print(res.text)


with open("mygoogle.html","w",encoding="utf-8") as f:
    f.write(res.text)