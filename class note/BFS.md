# Breadth-First Search (BFS、廣度優先搜尋)
## 簡介
### Breadth-First Search(BFS，廣度優先搜尋)，是廣義的Level-Order Traversal，同樣的原理使用在 Graph，就叫做 BFS 。他是已同層次(level)的節點優先，由低層次到高層次。
## 執行步驟
### 1、從頂點Ｓ開始。讓此頂點位於，即為level 0。
### 2、查找可從此起始頂點Ｓ立即訪問的所有其他頂點，將這些頂點標記為level 1。
### 3、找到所有與level 1上所有頂點，立即可訪問到的所有其他頂點，將這些頂點標記為level 2。
### 4、重複以上過程，直到所有的點都被訪問。

## 參考資料
#### https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
