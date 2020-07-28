package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2512_예산 {
    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static boolean isPossible(int arr[], int cur, int ALL) {
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= cur) {
                sum += cur;
            } else {
                sum += arr[i];
            }
        }

        if (sum <= ALL) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = stringToInt(br.readLine());

        String inString[] = br.readLine().split(" ");
        int budgets[] = new int[N];

        for (int i = 0; i < N; i++) {
            budgets[i] = stringToInt(inString[i]);
        }

        int ALL = stringToInt(br.readLine());
        int cur = 1;

        System.out.println(isPossible(budgets, 0, 485));


    }
}


