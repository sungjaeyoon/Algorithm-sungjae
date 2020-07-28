package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class P7567_그릇 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strings = br.readLine().split("");
        Stack<String> stack = new Stack<String>();

        stack.add(strings[0]);
        int count = 10;
        for (int i = 1; i < strings.length; i++) {
            if (stack.peek().equals(strings[i])) {
                count += 5;
            } else {
                count += 10;
            }
            stack.add(strings[i]);
        }
        System.out.println(count);


    }
}
