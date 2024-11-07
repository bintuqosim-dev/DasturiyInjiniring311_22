from heapq import heappush, heappop

#Graph
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        yordamchi = ListNode(0)
        joriy = yordamchi

        ustuvorlik_navbati = []

        for i, tugun in enumerate(lists):
            if tugun:
                heappush(ustuvorlik_navbati, (tugun.val, i, tugun))

        while ustuvorlik_navbati:
            qiymat, i, tugun = heappop(ustuvorlik_navbati)

            joriy.next = tugun
            joriy = joriy.next

            if tugun.next:
                heappush(ustuvorlik_navbati, (tugun.next.val, i, tugun.next))

        return yordamchi.next
