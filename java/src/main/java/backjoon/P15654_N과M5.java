package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class P15654_N과M5 {

    static private int N;
    static private int M;
    static private int arr[];
    static private boolean visited[];


    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    static public void fun(int cur, int count, String str) {
        if (count == M) {
            System.out.println(str);
            return;
        } else {
            visited[cur] = true;
            for (int i = 0; i < N; i++) {
                if (!visited[i] && (i != cur)) {
                    fun(i, count + 1, str + " " + arr[i]);
                }
            }
            visited[cur] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input[] = br.readLine().split(" ");
        N = stringToInt(input[0]);
        M = stringToInt(input[1]);

        input = br.readLine().split(" ");
        arr = new int[input.length];
        visited = new boolean[input.length];
        for (int i = 0; i < N; i++) {
            arr[i] = stringToInt(input[i]);
        }

        Arrays.sort(arr);

        for (int i = 0; i < N; i++) {
            fun(i, 1, "" + arr[i]);
        }

    }
}
