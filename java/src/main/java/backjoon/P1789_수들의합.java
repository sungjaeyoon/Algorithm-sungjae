package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P1789_수들의합 {
    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Long S = Long.parseLong(br.readLine());
        Long N = Long.valueOf(1);
        Long sum = Long.valueOf(0);

        while (sum < S) {
            sum = sum + N;
            N++;
        }
        if (sum == S) {
            System.out.println(N - 1);
        } else {
            System.out.println(N - 2);
        }
    }
}
/*

 */