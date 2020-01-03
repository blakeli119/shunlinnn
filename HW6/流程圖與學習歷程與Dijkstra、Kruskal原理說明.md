# 流程圖
![](/image/S__82919656.jpg)
# Dijkstra、Kruskal原理說明
## Dijkstra
### 使用了廣度優先搜尋解決賦權有向圖的單源最短路徑問題。該演算法存在很多變體；原始版本找到兩個頂點之間的最短路徑，但是更常見的變體固定了一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個最短路徑樹。該演算法常用於路由演算法或者作為其他圖演算法的一個子模組。如果圖中的頂點表示城市，而邊上的權重表示城市間開車行經的距離，該演算法可以用來找到兩個城市之間的最短路徑。

# Kruskal
### Kruskal演算法是一種用來尋找最小生成樹的演算法，目的是找出可連結所有點且具最小權重總和的樹
步驟1–>把所有的邊依照權重從小排到大
步驟二–>由最小權重的邊開始，在維持不導致環情況發生的條件下，把邊加入最小生成樹的集合內。
直到所有邊都被檢查過停止。
# 參考資料
#### https://iq.opengenus.org/kruskal-minimum-spanning-tree-algorithm/
#### http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html

