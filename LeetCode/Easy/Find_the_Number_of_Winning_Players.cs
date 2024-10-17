public class Solution {
    public int WinningPlayerCount(int n, int[][] pick) {
        
        int[][] arr = new int[n][];
        int wnrs = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = new int[11];
        }
        for(int i=0; i<pick.Length; i++)
        {
            int person = pick[i][0];
            int color = pick[i][1];
            arr[person][color]++;
        }
        for(int i=0; i<n;i++){
            for(int j=0; j<arr[i].Length;j++){
                if (arr[i][j] > i){
                    wnrs++; 
                    break;
                }
            }
        }
        return wnrs;
    }
}