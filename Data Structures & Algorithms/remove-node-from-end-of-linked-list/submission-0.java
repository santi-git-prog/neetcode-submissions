class Solution {
    public ListNode reverse(ListNode head)
    {
        ListNode prev = null;
        ListNode curr = head;
        ListNode after = null;

        while(curr != null)
        {
            after = curr.next;
            curr.next = prev;
            prev = curr;
            curr = after;
        }

        return prev;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) 
    {
        ListNode h1 = reverse(head);

       
        if(n == 1)
        {
            h1 = h1.next;
            return reverse(h1);
        }

        ListNode temp = h1;

        for(int i = 1; i < n - 1; i++)
        {
            temp = temp.next;
        }

        temp.next = temp.next.next;

        return reverse(h1);
    }
}