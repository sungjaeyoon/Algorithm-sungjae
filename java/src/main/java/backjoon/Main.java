package backjoon;

class Book{
    private int id;
    private String name;
    private String artist;
    private int count;
    public Book(int id, String name, String artist, int count) {
        this.id = id;
        this.name = name;
        this.artist = artist;
        this.count = count;
    }
    public void display(){
        System.out.println("책ID: " +id +", 책 이름: "+name+", 저자: "+artist+", 가격: "+count+", 종류:");
    }
}

public class Main {

    public static void main(String[] args) {
        Book[]books = new Book[5];
        books[0]=new Book(1,"가가가","고고고",20000);
        books[1]=new Book(2,"나나나","너너너",40000);
        books[2]=new Book(3,"다다다","더더더",30000);
        books[3]=new Book(4,"라라라","러러러",27000);
        books[4]=new Book(5,"마마마","머머머",21000);

        for(Book book : books){
            book.display();
        }
    }
}
