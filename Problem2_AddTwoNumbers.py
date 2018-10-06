#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@author: Albert
#@Time: 2018/8/13


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2): #求解
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1=self.getNumber(l1)
        number2=self.getNumber(l2)
        number=number1+number2
        l=self.num2LinkedLists(number)
        return l


    def getNumber(self,l):  #将链表转化为数字
        number = 0
        item = 1
        while(item):
            number = number+l.val*item
            item=item*10
            l=l.next
            if l==None:
                item=0
        return number
    def num2LinkedLists(self,num):  #将数字转化为链表

        value=num%10
        rest=int(num/10)
        l=ListNode(value)
        if rest!=0:
            value = rest % 10
            rest = int(rest / 10)
            l.next=ListNode(value)
            temp=l.next
            while(rest!=0):
                value=rest%10
                rest=int(rest/10)
                temp.next=ListNode(value)
                temp=temp.next
        return l

def makeLinkedList(n):  #将一个列表数字转化为题目要求的链表，按照个位，十位，百位的顺序
    l = ListNode(n[0])
    l.next = ListNode(n[1])
    temp = l.next
    for i in n[2:]:
        temp.next = ListNode(i)
        temp = temp.next
    return l

l1=makeLinkedList([2,4,3])
l2=makeLinkedList([5,6,4])

a=Solution()
l=a.addTwoNumbers(l1,l2)
number=a.getNumber(l)
print(number)