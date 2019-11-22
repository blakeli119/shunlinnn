# Insert
### 流程圖
#### insert6進這個tree，從最頂端開始，6<7往左跑，6>3，6>4，6>5皆往右跑，因此最後位置如圖。
![](/image/E1DE2B7D-E749-45AB-ACDB-D89D95DF027E.jpg)
![](/image/S__81182767.jpg)
### 學習歷程
#### insert是四個之中我第一個完成的功能，因為是第一個，所以花的時間也比較長，在想出下圖迴圈裡還有一個迴圈時，真的卡滿久的。insert跟search其實在程式碼及概念上是滿像的，但因為做完insert，所以在做search的時候，可能腦袋的節已經開了，所以速度變很快。
![](/image/螢幕截圖%202019-11-22%2011.42.40.png)
![](/image/螢幕截圖%202019-11-22%2011.42.55.png)
### 參考資料
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
https://www.geeksforgeeks.org/python-program-for-binary-insertion-sort/
# Search
### 流程圖
![](/image/S__81182765.jpg) 
### 學習歷程
#### 此處要return root 而不是return root.val，因為是要回傳位置，而不是數值。
![](/image/螢幕截圖%202019-11-22%2002.43.56.png)
#### 此處為，一開始我將第一個elif 設為<=，但因為前面的if已經設過等於了，所以不應該再使用<=，這是有bug的地方。
![](/image/螢幕截圖%202019-11-22%2003.03.57.png)
### 參考資料
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
https://www.geeksforgeeks.org/python-program-for-binary-search/
# delete
### 流程圖
#### 若我要刪除tree中的3，則4、5要往上移，必須讓tree保持著，小的往左、大的往右之規則。
![](/image/A4053156-5673-443F-9FE8-005D2D78F02D.jpg)
### 學習歷程
### 參考資料
# modify
### 流程圖
### 學習歷程
### 參考資料
# BST原理
#### 全名為Binary Search Tree。包含了增加、刪除、查詢、修改，有些是可以遞迴實現的。二叉查找樹是二叉樹的一種特殊形式，對於每一個節點來說，其屬性Key值可以比較，其Key值比左節點大，比右節點小。每個節點最多只有兩個子節點的樹，對於每個節點來說，左孩子小於其值，右孩子大於其值，整個二叉樹的中序遍歷輸出爲所有數據的有序序列。
### 參考資料
https://www.twblogs.net/a/5cc33bd2bd9eee3aed78cd2e

https://www.itread01.com/content/1545705032.html
