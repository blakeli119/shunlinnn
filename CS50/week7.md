# Lined list
## 優點
### 1、不需使用連續記憶體空間，不需事先指定串列大小。
### 2、能夠容易的修改指標，插入或移除節點。
## 缺點
### 1、使用額外的記憶體空間紀錄節點指標。
### 2、無法快速索引到某個節點，必須迭代搜索。
# Hash Table（雜湊表）
### 引入Hash Function，將Key對應到符合Table大小m的範圍內，index=h(Key)，即可成為Hash Table的index。
### 1、平均情況：搜尋、插入、刪除，皆為 O(1)
### 2、最壞情況：搜尋、插入、刪除，皆為 O(n)
### 3、O(1) ：常數時間，代表不論雜湊表多麼大，耗費的時間皆維持不變
