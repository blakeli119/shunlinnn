# Heap Sort
## Max Heap 執行步驟
### 1、把第一個node和最後一個node互換位置
### 2、假裝heap的「最後一個node」從此消失不見
### 3、對第一個node進行MaxHeapify()
### 4、重複以上步驟，從heap的最後一個node開始，一路往上，直到root，能找到最好的排列
### MaxHeapify()解釋：「由上而下」，逐一檢查subtree，使subtree滿足Max Heap規則。
## 時間複雜度
### Best Case：Ο(n log n)
### Worst Case：Ο(n log n)
### Average Case：Ο(n log n)
## 空間複雜度：Ο(1)
## 䅰定性：不穩定
# 參考資料
#### http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php
#### https://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
