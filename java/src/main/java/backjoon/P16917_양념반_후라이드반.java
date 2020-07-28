package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P16917_양념반_후라이드반 {
    public static int stringToInt(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input[] = br.readLine().split(" ");

        int A, B, C, X, Y;
        A = stringToInt(input[0]);
        B = stringToInt(input[1]);
        C = stringToInt(input[2]);

        X = stringToInt(input[3]);
        Y = stringToInt(input[4]);

        int count = 0;

        if ((A + B) <= C * 2) {//case 1
            count += (A * X) + (B * Y);
        } else {//case 2
            if (X > Y) {//case 2-1
                count += Y * (C * 2);
                count += Math.min((X - Y) * A, (X - Y) * (C * 2));
            } else {//case 2-2
                count += X * (C * 2);
                count += Math.min((Y - X) * B, (Y - X) * (C * 2));
            }

        }
        System.out.println(count);
    }
}

/*
 **
 * input : A B C X Y
 * 후라이드 가격 : A  구매 개수 : X
 * 양념 가격 : B     구매 개수 : Y
 * 반반 가격 : C
 *
 *  후라이드1+양념1 과 반반*2 중 무엇이 더 싼가
 *  case 1. 전자 일 경우
 *  (A * X) + (B * Y)
 *
 *  case 2. 후자 일 경우
 *  반반으로 최대한 많은 개수를 확보 -> X, Y 중에 더 적은것을 반반으로 최대한 산다.
 *
 *  X 가 크다면   Y * (C * 2)   그러면 X-Y 개수의 후라이드(A)를 더 사야한다.
 *      case 2-1.
 *          (X-Y)*A 와 (X-Y)*(C*2) 중 작은 값을 더해준다.
 *  Y 가 크다면   X * (C * 2)   그러면 Y-X 개수의 양념(B)를 더 사야한다.
 *      case 2-2.
 *          (Y-X)*B 와 (Y-X)*(C*2) 중 작은 값을 더해준다.
 *
 *
 *
 */
