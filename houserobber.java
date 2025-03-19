public class houserobber {
    public static int solution(int[] num) {
        if (num == null || num.length == 0) {
            return 0;
        }
        if (num.length == 1) {
            return num[0];
        }
        int n = num.length;
        int[] dp = new int[n];
        dp[0] = num[0];
        dp[1] = Math.max(num[0], num[1]);
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + num[i]);
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        int[] num = { 2, 7, 9, 3, 1 };
        houserobber sol = new houserobber();
        System.out.println(sol.solution(num));
    }
}
