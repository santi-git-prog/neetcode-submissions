class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] ans = new int[k][2];
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> b[2] - a[2]
        );
        for(int[] m: points)
        {
            int b=m[0]*m[0]+m[1]*m[1];
            pq.offer(new int[]{m[0],m[1],b});
            if(pq.size() > k)
            {
                pq.poll();
            }
        }
        for(int i=0;i<k;i++)
        {
            int[] curr = pq.poll();
            ans[i][0]=curr[0];
            ans[i][1]=curr[1];
        }
        return ans;
    }
       
}