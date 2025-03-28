import java.util.Scanner;

public class climbingstairs {
    public static int solution(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int ways = solution(n);
        System.out.println(ways);
    }
}
