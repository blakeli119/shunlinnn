# Stack
### 堆疊（英語：stack）又稱為棧或堆棧，是電腦科學中的一種抽象資料型別， 只允許在有序的線性資料集合的一端（稱為堆疊頂端，英語：top）進行加入資料（英語：push）和移除資料（英語：pop）的運算。 因而按照後進先出（LIFO, Last In First Out）的原理運作。
## 功能
### 1、Push：把資料放入到stack中。
### 2、Pop：把最上面的資料從stack中移除。
### 3、Top：回傳最上面的資料，且不會影響到資料結構本身。
### 4、IsEmpty：確認Stack裡是否有資料，且不會影響資料結構本身。
### 5、getSize：回傳Stack裡的資料個數，且不會影響資料結構本身。

# Queue
### 佇列，又稱為隊列（queue），是先進先出（FIFO, First-In-First-Out）的線性表。在具體應用中通常用鍊表或者數組來實現。佇列只允許在後端（稱為rear）進行插入操作，在前端（稱為front）進行刪除操作。
## 功能
### 1、Push：把資料從Queue的後面放進Queue，並變成新的back。
### 2、Pop：把front所指向的資料從Queue中移除，並更新front。
### 3、getFront：回傳front所指向的資料。
### 4、getBack：回傳back所指向的資料。
### 5、IsEmpty：確認Queue裡是否有資料。
### 6、getSize：回傳Queue裡的資料個數。
