package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P11651_좌표_정렬하기2 {

    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = stringToInt(br.readLine());

        List<Point> points = new ArrayList<Point>();
        for (int i = 0; i < N; i++) {
            String[] in = br.readLine().split(" ");
            points.add(new Point(stringToInt(in[0]), stringToInt(in[1])));
        }
        Collections.sort(points);

        for (Point p : points) {
            System.out.println(p.getX() + " " + p.getY());
        }

    }

    static class Point implements Comparable<Point> {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

//        @Override
        public int compareTo(Point p) {
            if(this.y>p.y){
                return 1;
            }else if(this.y<p.y){
                return -1;
            }else{
                if(this.x>p.x){
                    return 1;
                }else{
                    return -1;
                }
            }
        }
    }
}
