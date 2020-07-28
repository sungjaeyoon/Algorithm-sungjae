package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P6996_애너그램 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        loop:
        for (int i = 0; i < T; i++) {
            int firstWordCount[] = new int[26];
            int secondWordCount[] = new int[26];
            String in[] = br.readLine().split(" ");

            String first = in[0];
            String second = in[1];

            for (int j = 0; j < first.length(); j++) {
                firstWordCount[(int) first.charAt(j) - 97]++;
            }

            for (int j = 0; j < second.length(); j++) {
                secondWordCount[(int) second.charAt(j) - 97]++;
            }

            for (int j = 0; j < firstWordCount.length; j++) {
                if (firstWordCount[j] != secondWordCount[j]) {
                    System.out.println(in[0] + " & " + in[1] + " are NOT anagrams.");
                    continue loop;
                }
            }
            System.out.println(in[0] + " & " + in[1] + " are anagrams.");
        }
    }
}
