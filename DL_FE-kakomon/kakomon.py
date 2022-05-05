from japanera import Japanera
from datetime import date
import urllib.request

def download(startYear, endYear):
    # URLの共通（前半）部分
    urlbase = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_"
    # Japanera
    jpnera = Japanera()
    # 春期と秋期
    seasons = {1:"h", 2:"a"}
    months = {1:4, 2:10}
    # 時間帯
    times = ["am", "pm"]
    # 問題・解答・講評
    qacs = ["qs", "ans", "cmnt"]

    print("downloading...")

    # [startYear]年度から[endYear]年度のPDF（問題・解答・講評）をダウンロード
    for year in range(startYear, endYear + 1):
        for season in seasons.items():
            (sKey, sValue) = season
            # 年度の文字列（例: 2015h21）
            nendo1 = str(year) + jpnera.strftime(date(year, 4, 1), "%-a%-o").lower()
            nendo2 = str(year) + jpnera.strftime(date(year, months[sKey], 1), "%-a%-o").lower()

            for time in times:
                for qac in qacs:
                    # 講評は午後のみ
                    if not (time == "am" and qac == "cmnt"):
                        try:
                            url = urlbase + nendo1 + "_" + str(sKey) + "/" + nendo2 + sValue + "_fe_" + time + "_" + qac + ".pdf"
                            filename = nendo2 + sValue + "_fe_" + time + "_" + qac + ".pdf"
                            urllib.request.urlretrieve(url, "{0}".format(filename))
                        except urllib.error.HTTPError:
                            # ダウンロードできなかったファイル名を表示
                            print("Error: " + filename)

    print("finished!")

if __name__ == "__main__":
    # [第1引数]年度から[第2引数]年度のPDF（問題・解答・講評）をダウンロード
    download(2015, 2019)
