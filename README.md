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
2. DB: PostgresSQL + SQLAlchemy + TestContainers + Alembic
3. CI/CD
4. poetry
5. ATDD、TDD

### 遇到的錯誤資訊
```shell
# Q: ModuleNotFoundError: No module named 'animal_massage'
# A:
export PYTHONPATH=/data/code/AnimalMassage/ 
```

### 學習筆記

#### [pytest](https://codingnote.cc/zh-tw/p/198385/)
- -v(-verbose) : 輸出詳細資訊
- -s = --capture=no : 捕獲方式，顯示print資訊
- -cov : coverage(覆蓋率)

#### alembic
- [別人的筆記](https://medium.com/@acer1832a/%E4%BD%BF%E7%94%A8-alembic-%E4%BE%86%E9%80%B2%E8%A1%8C%E8%B3%87%E6%96%99%E5%BA%AB%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-32d949f7f2c6****)
- 通常會搭配SQLAlchemy一起使用，主要是用來進行migration DB，也可以用來`upgrade`、`downgrade` 
```shell
alembic init myAlembic  # 產出 /myAlembic 資料夾、alembic.ini

# 需在/myAlembic/env.py底下設定下面這兩行，才能抓到指定的table
# from animal_massage.models import User
# target_metadata = User.metadata
alembic revision --autogenerate -m "Create init tables"

alembic upgrade head
```

#### 其他
```shell
# Allow >=2.0.5, <3.0.0 versions
poetry add pendulum@^2.0.5

# Uninstall all package
pip freeze | xargs pip uninstall -y
```