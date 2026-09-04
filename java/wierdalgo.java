import java.util.Scanner;

class voila{
    boolean validate(int n){
        if (n >= 1 && n <= 1000000){
            return true;
        }
        else{
            return false;
        }
    }

    void voila(int n){
        if (validate(n) == true){
            while (n!=1){
                System.out.print(n + " ");
                if (n%2 == 0){
                    n = n / 2;
                }
                else{
                    n = (n*3) + 1;
                }
            }
            System.out.print(n);
        }
    }

}

public class wierdalgo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        voila num = new voila();
        num.voila(n);
        
    }
}