## 네이버 쇼핑 곱창 상품 순위 예측

<br>

### Author : DataHyeon

<br>

### Date : 22.12.23

<br>

### Language : Jupyter

<br>

### Dec

- 네이버 쇼핑에서 곱창 상품들의 리뷰, 총 구매횟수, 가격 등을 추출하여 해당 지표들로 순위를 예측

- 셀레니움을 사용하여 데이터 크롤링 후 데이터 전처리 및 중요 변수 확인, 모델평가

<br>

### Progress

- 셀레니움과 BeautifulSoup을 사용해 상품 정보에서 필요한 지표들을 추출

- 결측치 및 이상치 처리

- 이상치가 큰 컬럼들이 많아 log 및 esd 처리

- Xgboost로 베이직 모델 확인 이후 pycaret 모듈을 사용한 다양한 모델 확인

<br>

### Module

- 전처리 : pandas, numpy, selenium
 
- 시각화 : matplotlib, seaborn

- ML : xgboost, pycaret

<br>

### File

- Main : main.ipynb

- Input : 곱창.csv

- Sub : extract.py

<br>

### Conclusion

- 모델 설명력이 말도 안되게 잘못 나오는 현상이 있다.

- 데이터 전처리나 모델 설계에서 잘못된 부분이 있는 거 같은데 이상치를 잘 처리하지 못해서 그런건지
타켓값을 순위로 잡아서 그런건지 더 많은 공부가 필요하다고 느꼈다.
