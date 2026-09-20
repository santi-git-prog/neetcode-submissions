class Solution {
    public int findKthLargest(int[] nums, int k) 
    {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i: nums)
        {
            pq.offer(i);
        }   
        int a=0;
        for(int i=0;i<k;i++)
        {
            a=pq.poll();
        }
        return a;

    }
}
