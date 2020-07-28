package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P15685_드래곤커브 {
    public static int stringToInt(String s){
            return Integer.parseInt(s);
        }
    public static void main(String[] args) throws IOException {
        /**
         * input 처리
         * */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = stringToInt(br.readLine());
        int arr[][]=new int[N][4];
        //  x, y 시작점, 시작 방향, 세대
        for(int i=0;i<N;i++){
            String line[] = br.readLine().split(" ");
            for(int j=0;j<4;j++){
                arr[i][j]=stringToInt(line[j]);
            }
        }

        /**
         * 방향 구하기
         * */
        int moveDir[][]=new int[N][1024];
        for(int i=0;i<N;i++){
            moveDir[i][0]=arr[i][2];//첫 방향은 시작방향 고정

            int lastIndex=0; // 이전번에 마지막 인덱스
            for(int j=0;j<arr[i][3];j++){//두번째 부터는 역순 +1
                int curIndex=lastIndex+1;
                int reverseIndex=lastIndex;
                while (reverseIndex>=0){ // 마지막 인데스~ 0 방향으로 갈때까지 반복
                    moveDir[i][curIndex]=moveDir[i][reverseIndex]+1;
                    if(moveDir[i][curIndex]==4){
                        moveDir[i][curIndex]=0;
                    }
                    curIndex++;
                    reverseIndex--;
                }
                lastIndex=curIndex-1;
            }
        }

        /**
         * 방향별로 점찍기
         * */
        int graph[][]=new int[101][101];

        for(int i=0;i<4;i++){
            int x = arr[i][0];
            int y = arr[i][1];

            // 0세대 커브
            graph[x][y]=1;
            if(arr[i][2]==0){
                graph[x][y+1]=1;
                y=y+1;
            }else if(arr[i][2]==1){
                if(x>0){
                    graph[x-1][y]=1;
                }
                x=x-1;
            }else if(arr[i][2]==2){
                if(y>0){
                    graph[x][y-1]=1;
                }
                y=y-1;
            }else{
                graph[x+1][y]=1;
                x=x+1;
            }

            for(int j=1;j<Math.pow(2,arr[i][3]);j++){

                

                if(x>=0 && x<101 && y>=0 && y<101){
                    graph[x][y]=1;
                }
            }

        }


        /**
         * 사각형 개수 구하기
         * */
        int count=0;
        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                if(graph[i][j]==1 && graph[i+1][j]==1 && graph[i][j+1]==1 && graph[i+1][j+1]==1 ){
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}

/**
 * 방향
 *      1
 *   2  +  0
 *      3
 *
 *   0 세대  0
 *   1 세대  0 1
 *   2 세대  0 1 2 1
 *   3 세대  0 1 2 1 2 3 2 1
 *  역방향으로 +1 씩 해서 증가함.
 *
 *  10세대 까지 갔을때 배열의 크기가 2^10 이므로 1024
 *  arr[1024] 크기로 충분
 * */
