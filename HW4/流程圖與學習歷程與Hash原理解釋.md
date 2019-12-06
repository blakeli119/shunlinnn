# Hash Table
## 流程圖
![](/image/S__81805386.jpg)
## 學習歷程
#### 一開始使用while迴圈，讓他跑到最後終止，但一直error，怎麼改都還是error，甚至後來跑不出結果，直接陷入無限迴圈。
![](/image/螢幕截圖%202019-12-05%2017.08.54.png)
#### 後來直接放棄使用while，改成以下方法，是參考網路上的作法，contains是我最先完成的，因為我覺得他比較容易思考。
![](/image/螢幕截圖%202019-12-06%2011.56.37.png)
#### 再來是進入加密的部分，先幫他設個defunction，然後每個功能下也都要再執行一次加密動作。
![](/image/螢幕截圖%202019-12-06%2011.57.30.png)
![](/image/螢幕截圖%202019-12-06%2011.57.38.png)
#### 再來是add跟remove，我覺得其實三種功能的邏輯滿像的，這次作業也不像上次那麼卡。
![](/image/螢幕截圖%202019-12-06%2011.57.11.png)
![](/image/螢幕截圖%202019-12-06%2011.56.58.png)
## Hash Table與Hash function 原理
### Hash Table(雜湊表、哈希表）
#### 1、儲存實際資料的，是Entry物件。
#### 2、主要方法為，put、get、remove等。
#### 3、根據Key直接查詢資料結構內的內存位置。
#### 4、透過函數計算鍵值，將所查詢的數據放置到表中的位置來查詢記錄。
#### 5、存放記錄的數組稱做Hash Table，加速了尋找的速度，簡單說就是將資料分類，方便查詢。
### Hash function(雜湊函數、雜湊演算法）
#### 1、壓縮資料，將資料變小，固定資料的格式。
#### 2、將資料打亂混合，重新建立雜湊值。
#### 3、雜湊值通常用一個短的字母和數字組成的字串來表示。
#### 4、雜湊值當作陣列的索引，資料儲存在這個索引中。
#### 5、性質：運算速度快、不可逆性。
## 參考資料
#### https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
#### http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
#### https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view
#### https://zh.wikipedia.org/wiki/散列函數
#### https://zh.wikipedia.org/wiki/哈希表
#### https://www.itread01.com/content/1544966282.html
#### https://stackoverflow.com/questions/10039788/what-does-distribution-of-the-hash-function-mean
#### https://www.eecs.wsu.edu/~ananth/CptS223/Lectures/hashing.pdf
