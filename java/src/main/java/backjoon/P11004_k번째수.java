package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P11004_k번째수 {
    public static int K;

    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static int partition(int arr[], int left, int right) {
        int pivot = arr[right];
        int i = left - 1;

        for (int j = left; j <= right - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[right];
        arr[right] = temp;

        return i + 1;
    }

    public static void quickSort(int arr[], int left, int right) {
        if (left < right) {

            int p = partition(arr, left, right);
            if (p >= K) {
                quickSort(arr, left, p - 1);
            } else {
                quickSort(arr, p + 1, right);
            }

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String in[] = br.readLine().split(" ");

        int N = stringToInt(in[0]);
        K = stringToInt(in[1]);

        int arr[] = new int[N];

        String numString = br.readLine();

        StringTokenizer tokens = new StringTokenizer(numString, " ");

        for (int i = 0; i < N; i++) {
            arr[i] = stringToInt(tokens.nextToken());
        }

        quickSort(arr, 0, N - 1);

        System.out.println(arr[K - 1]);


    }
}