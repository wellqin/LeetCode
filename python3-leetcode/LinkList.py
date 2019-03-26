class Node(object):
    """单链表的结点，节点抽象定义类，为每个节点提供实例化"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
		

class LinkList(object):
    """单链表"""
    def __init__(self):
        self.__head = None  # 私有属性，自己知道就行了

    def is_empty(self):
        """判断链表是否为空，头指向的为空就是空"""
        return self.__head == None

    def length(self):
        """链表长度，需要有一个游标cur去遍历"""
        # cur初始时指向头节点
        cur = self.__head   # 因为是从head开始的，即从0开始的
        count = 0   
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表，需要有一个游标cur去遍历，作用到指定链表就行了，不需要额外参数"""
        cur = self.__head
        while cur != None:
            print (cur.item, end = " ") #可以打印在一行
            cur = cur.next
        print ""
		
	def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 1.将新节点的链接域next指向头节点，即_head指向的位置，若先执行第二步，则后面的找不到了
        # 注意保证原有链表不打断
        node.next = self.__head
        # 2.将链表的头_head指向新节点
        self.__head = node
		
	 def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)  # 将传进来的数据通过节点类封装成节点
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
			
	def insert(self, pos, item):  # 在pos这个位置上插入item
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入，pos为插入的位置，从0开始
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
		
	
	def remove(self,item):
        """删除节点"""
        cur = self._head  # cur从头节点开始
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:  # if cur == self.__head
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # ！！！操作在这里：将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break  # 退出循环，删除完了退出
            else:
                # 继续按链表后移节点，pre先移到cur位置，cur再移动到下一个位置
                pre = cur
                cur = cur.next
		
	def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
            cur = self._head
            while cur != None:
                if cur.item == item:
                    return True
                cur = cur.next
            return False
		
		
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		cur, pre = head, None
		while cur:
		  cur.next, pre, cur = pre, cur, cur.next
		return pre
		
	def reverse(self, head):
            if head is None: return None
            p = head
            cur = None
            pre = None
            while p is not None:
            	cur = p.next
            	p.next = pre
                pre = p
                p = cur
            return pre
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
