class Solution {
    public void islandsAndTreasure(int[][] grid) {

        int m = grid.length;
        int n = grid[0].length;

        Queue<int[]> q = new LinkedList<>();

    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    q.add(new int[]{i, j});
                }
            }
        }

        int[][] dir = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        while (!q.isEmpty()) {

            int[] curr = q.poll();

            int i = curr[0];
            int j = curr[1];

            for (int[] d : dir) {

                int ni = i + d[0];
                int nj = j + d[1];

                if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                    continue;
                }

                if (grid[ni][nj] != Integer.MAX_VALUE) {
                    continue;
                }

                grid[ni][nj] = grid[i][j] + 1;

                q.add(new int[]{ni, nj});
            }
        }
    }
}