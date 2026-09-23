import java.util.Scanner;

class findtotal{
    int diff = 0;
    long total = 0;

    long findtotal(int n, int[] xi){
        for(int j = 0; j < (n-1); j++){
            diff = 0;

            if (xi[j] > xi[j+1]){
                diff = xi[j] - xi[j+1];
                xi[j+1] = xi[j];
            }
            
            total = total + diff;
        }

        return(total);
    }

}


public class increasingarray {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        int[] xi = new int[n];
        for (int i = 0; i < (n); i++){
            xi[i] = input.nextInt();
        }

        if (1 <= n && n <= 200000){
            findtotal t = new findtotal();
            //t.findtotal(n);
            System.out.print(t.findtotal(n, xi));
        }


    }
}
