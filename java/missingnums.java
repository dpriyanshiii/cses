import java.util.Scanner;

class somme{
    long patsumis;
    long totalis;

    void numsum(int n, int nums[]){
        for (int i = 0; i < (n-1); i++){
            patsumis = patsumis + nums[i];
        }
    }

    void totalsum(int n){
        totalis = ((long)n * (n+1)) / 2;
    }

    long returnmiss(){
        return (totalis - patsumis);
    }
}

public class missingnums {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int[] nums = new int[n-1];
        for (int i = 0; i < (n-1); i++){
            nums[i] = input.nextInt();
        }

        if ( n >= 2 && n <=200000){
        somme iss = new somme();
        
        iss.numsum(n, nums);
        iss.totalsum(n);
        
        System.out.print(iss.returnmiss());
        }


    }
}
