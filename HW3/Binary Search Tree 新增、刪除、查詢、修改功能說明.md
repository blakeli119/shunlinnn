# 新增insert
顧名思義就是要將數值加入到原本的tree裡，要在BST的規則下，及左邊小右邊大之規定。若父節點為空的，則直接將質素入其中;若新的值小於父節點，則丟入左邊的子節點;若新的值大於父節點，則丟入右邊的子節點。若以下還有子節點，則繼續執行以上的動作，因此這裡我使用迴圈。
# 查詢search
這個運作方式與insert相似，他是要從tree裡找到一個特定數值。小於節點往左找、大於節點往右找，一個一個往下找，直到找到目標數值則停止，然後回傳數值的位置。若找完整個tree依然找不到，則回傳None;若目標值即為父節點，則直接回傳root。
# 刪除delete
刪除tree中的一個點，這樣會移動到其他的點，但要讓整個tree還是符合BST的規則。
# 修改modify
可以說是刪除與新增合併，刪除指定數字並將它改為其他數值，再依照新的數值大小，來調整數值的位置。
### 參考資料
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.
https://zh.wikipedia.org/wiki/二元搜尋樹
