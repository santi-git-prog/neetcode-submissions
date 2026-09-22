class Solution { 
    public int orangesRotting(int[][] grid) { 

        Queue<int[]> q = new LinkedList<>(); 

        int n = grid.length;       
        int m = grid[0].length;    


        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < m; j++) { 
                if (grid[i][j] == 2) { 
                    q.offer(new int[]{i, j}); 
                } 
            } 
        }  

        int time = 0; 
 
        int[][] dir = { 
            {1, 0}, 
            {-1, 0}, 
            {0, 1}, 
            {0, -1} 
        }; 
 
        while (!q.isEmpty()) { 
 
            int size = q.size(); 
 
            for (int k = 0; k < size; k++) { 
 
                int[] curr = q.poll(); 
 
                int i = curr[0]; 
                int j = curr[1]; 
 
                for (int[] d : dir) { 
 
                    int ni = i + d[0]; 
                    int nj = j + d[1]; 
 
                    if (ni >= 0 && ni < n && 
                        nj >= 0 && nj < m && 
                        grid[ni][nj] == 1) { 
 
                        grid[ni][nj] = 2; 
                        q.offer(new int[]{ni, nj}); 
                    } 
                } 
            } 
 
            if (!q.isEmpty()) { 
                time++; 
            } 
        } 
 
        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < m; j++) { 
                if (grid[i][j] == 1) { 
                    return -1; 
                } 
            } 
        } 
 
        return time; 
    } 
}