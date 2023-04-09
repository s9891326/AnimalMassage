## 動物按摩

### 功能
1. 官網內容(google、FB、Line、手機登入、一般登入)
2. 部落格 = 文章(圖文穿插)
3. 預約(連結到Line官方帳號)
4. about
5. pdf(報告後台、18條肌肉、7種顏色、小金給圖片用html框肌肉)
6. 維運(獨立domain)

### 技術
1. Python + FastAPI
2. DB: PostgresSQL + SQLAlchemy + TestContainers
3. CI/CD
4. poetry
5. ATDD、TDD

### 參考
```shell
# Allow >=2.0.5, <3.0.0 versions
poetry add pendulum@^2.0.5

# Uninstall all package
pip freeze | xargs pip uninstall -y 
```

#### [pytest](https://codingnote.cc/zh-tw/p/198385/)
- -v(-verbose) : 輸出詳細資訊
- -s = --capture=no : 捕獲方式，顯示print資訊
- -cov : coverage(覆蓋率)

