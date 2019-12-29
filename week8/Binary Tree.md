# Binary Tree（二元樹）
## 基本介紹
### 一般的樹(Tree)對於樹上的node之child（子結點）數目沒有限制，因此可以有很多個。
![](/image/螢幕截圖%202019-12-29%2011.12.44.png)
### Binary Tree（二元樹)則限制每個node只能有兩個child，兩個子結點分別稱為，左子結點與右子節點，而同時連結這兩個數的，稱為他們的父節點。
![](/image/螢幕截圖%202019-12-29%2011.12.55.png)
#### 以上圖來自http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html#application
## 特性
### 1、所有父結點都有兩個子結點
### 2、所有子結點具有相同等級
### 3、子結點之level為n，整棵樹共有2n−1個node
### 4、第i個node的left child之index為2i，第i個node的right child之index為 2i+1
## 應用
### 1、Binary Search Tree(BST)：新增、刪除、修改等
### 2、Binary Space Partition：於3D電玩遊戲以決定哪些物件需要rendered
### 3、Binary Tries：應用於high-bandwidth router(高頻寬路由器)以儲存router-tables
### 4、Heaps：用以實現高效率的priority queues(優先權佇列)
### 5、Huffman Coding Tree：例如.jpeg、.mp3等壓縮技術皆使用Huffman編碼
## 參考資料
#### http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html
#### http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html
#### https://en.wikipedia.org/wiki/Binary_tree
