学习总结
====
## 一、算法总结
### 数组，链表，跳表（元素需有序），熟悉各个的时间复杂度

### 栈，队列，优先队列，双端队列
* 时间复杂度和空间复杂度分析（完成算法代码之前需清除所写算法的时间复杂度和空间复杂度）
   * 常用时间复杂度表示：O(1)、O(log n)、O(n)、O(n^2)、O(n^3)、O(2^n)、O(n!)
   * 二叉树遍历、图的遍历时间复杂度：O(n) --遍历所有节点
   * 深搜(DFS)、广搜(BFS)时间复杂度：O(n)
   * 二分查找：O(log n)
   * 归并排序：O(n log n)
   
### 哈希表、映射、集合
 * 哈希表：
   * 根据关键码值(Key value)而直接进行访问的数据结构
   * 两个不同输入值对应同一个输出值时，产生哈希冲突
   * 冲突常采用链地址法：为每个Hash值建立一个单链表，当发生冲突时，将记录插入到链表中
   
### 树、二叉树、二叉搜索树
* 二叉树：
   * 由一个根节点加上两棵分别称为左子树和右子树的二叉树组成
   * 二叉树每个节点最多有两颗子树
   * 满二叉树：二叉树中，所有分支结点都存在左子树和右子树，并且所有叶子节点都在同一层上
   * 完全二叉树：如果一棵有N个结点的二叉树，它的前N个结点的结构与满二叉树前N个结点的结构相同，就把它称为完全二叉树
 * 二叉搜索树：
   * 左子树不为空，则它的左子树的结点数值都小于根结点数值
   * 右子树不为空，则它的右子树的结点数值都大于根结点数值
### 堆、二叉堆、图
 * 二叉堆：
   * 二叉堆是完全二元树或者是近似完全二元树，它分为两种：最大堆和最小堆。
   * 最大堆：父结点的键值总是大于或等于任何一个子节点的键值（用于解决 前K个最小值）
   * 最小堆：父结点的键值总是小于或等于任何一个子节点的键值（用于解决 前K个最大值）
   
### 泛型递归、树的递归
 * 递归方法：
   * 递归结束条件
   * 处理当前逻辑
   * 递归下一层
   * 清理当前层
### 分治、回溯
* 分治：
   * 一个大问题可以拆解程若干小问题
   * 每个小问题可以再拆解或者到达终止条件
   * 小问题处理完后能合并回原来的整体
 * 回溯：
   * 仅适用于小数据集，使用范围有限
   * 在树和图的深度优先回溯中，可以通过剪枝优化回溯路径
   
### 深度优先搜索、广度优先搜索
 * 深度优先搜索：
   * 优先搜索一颗子树，然后搜索另外一颗，相比BFS内存消耗更少
   * 能找出所有解决方案
 * 广度优先搜索
   * 广度优先搜索通常用于解决深度最小问题
### 贪心
  * 一个大问题可以拆解程若干小问题
  * 对每一子问题求解，得到子问题的局部最优解
  * 把子问题的局部最优解合成原来问题的一个解

### 二分查找
 * 查找表必须使用顺序的存储结构
 * 查找表必须按关键字大小有序排列
 
 ### 动态规划
 * 动态规划和递归或者分治没有根本上的区别（关键看有无最优子结构，无子结构为分治算法）
 * 动态规划和递归的共性：找到重复子问题进行分析
 * 动态规划找的是最优子结构、中途可以淘汰次优解
 
### 字典树
 * 字典树，即Trie树，典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计
 * 优点：最大限度地减少所谓的字符串比较，查询效率比哈希表高
 
 * 基本性质：
   * 1、节点本身不存完整单词
   * 2、从根节点到某一结点，路径上经过的路径连起来，为该节点对应的字符串
   * 3、每个节点的所有子节点路径代表的字符都不相同
  
 * 核心思想：
   * Tried树是空间换时间
   * 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
 
### 并查集
 * 基本操作：
   * 1、makeSet(s)：建立并查集，其中包含s个单元素集合
   * 2、unionSet(x, y)：把元素x和元素y所在的集合合并（x所在集合和y所在集合不相交，如果相交则不合并）
   * 3、find(x)：找到元素x所在的集合的代表，也可用于判断两个元素是否在同一个集合
  
### 红黑树
 * 每个节点或者是黑色，或者是红色。
 * 根节点是黑色。
 * 每个叶子节点（NIL）是黑色 （叶子节点是指为空(NIL或NULL)的叶子节点）
 * 如果一个节点是红色的，则它的子节点必须是黑色的。
 * 从一个节点到该节点的子孙节点的所有路径上包含相同数目的黑节点
 
### AVL树
 * 本身首先是一棵二叉搜索树。
 * 带有平衡条件：每个结点的左右子树的高度之差的绝对值（平衡因子）最多为1。也就是说，AVL树，本质上是带了平衡功能的二叉查找树（二叉排序树，二叉搜索树）
   
## 二、学习总结
 * 每天要保持题目的训练，让自己保持思维，，尽量多了解一些算法类型。每个题目需要我们认真分析自己的优势和不足，要根据自己算法的不足，加强训练，弥补不足。
 * 做题不是为了迎合数据，要熟悉算法程序的每一句含义和作用，不要为了迎合数据用例而编写代码。只有完全理解自己的代码，这样的程序才真正属于自己，才能做到举一反三，当题目很有典型性的时候还可以将它做成模板，以便对于以后同类型的题目快速解答，提高效率。
 * 决不能一味的做题，以为数量上去了，水平一定会提高。我们必须每隔一段时间对自己所做的题目和类型进行总结，很好的做到五毒神掌。哪些算法是自己非常拿手的，哪些类型还需要强化，对不知道的题目现阶段能否解决，解决的意义有多大，下阶段应该注重哪些类型和算法，有没有经典的题目能够做成模板，以便自己之后能少做无用功，提高效率。
