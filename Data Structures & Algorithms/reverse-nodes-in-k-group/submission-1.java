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
 
    public ListNode reverseKGroup(ListNode head, int k)  
    { 
        ListNode temp = head; 
 
     
        for(int i = 1; i < k; i++) 
        { 
            if(temp == null) 
                return head; 
 
            temp = temp.next; 
        } 
 
        if(temp == null) 
            return head; 
 
        ListNode l2 = temp.next; 
        temp.next = null; 
 

        ListNode rev = reverse(head); 
 
    
        ListNode rest = reverseKGroup(l2, k);

        ListNode temp2 = rev; 
 
        while(temp2.next != null) 
        { 
            temp2 = temp2.next; 
        } 
 
        temp2.next = rest; 
 
        return rev; 
    } 
}