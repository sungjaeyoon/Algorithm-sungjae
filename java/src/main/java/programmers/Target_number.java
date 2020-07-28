package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Target_number {
    private static int target;
    private static int answer;
    private static int[] numbers;

    public static void dfs(int count, int sum) {
        if (count == numbers.length-1) {
            if (sum == target) {
                answer++;
            }
        } else {
            dfs(count + 1, sum + numbers[count + 1]);
            dfs(count + 1, sum - numbers[count + 1]);
        }
    }

    public static int solution(int[] ns, int t) {
        numbers = ns;
        answer = 0;
        target = t;
        dfs(0, -1 * numbers[0]);
        dfs(0, numbers[0]);
        return answer;
    }

    public static void main(String[] args) {
        int arr[] = {1, 1, 1, 1, 1};
        System.out.println(solution(arr, 3));
    }
}
