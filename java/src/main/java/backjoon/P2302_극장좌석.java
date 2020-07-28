package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2302_극장좌석 {
    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = stringToInt(br.readLine());
        int M = stringToInt(br.readLine());
        int arr[] = new int[N + 1];

        for (int i = 0; i < M; i++) {
            arr[stringToInt(br.readLine())] = 1;
        }
        if(N==M){
            System.out.println(1);
            return;
        }

        int dp[] = new int[41];
        dp[0]=1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        for (int i = 4; i < 41; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        int sum = 1;
        int count = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == 0) {
                count++;
            } else if (arr[i] == 1) {
                sum *= dp[count];
                count = 0;
            }
        }
        if (count != 0) {
            sum *= dp[count];
        }

        System.out.println(sum);
    }
}
