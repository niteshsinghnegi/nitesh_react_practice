public class Niven {
    public static void main(String[] args) {
        int num = 9;   
        int temp = num;
        int sum = 0;

  
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        if (num % sum == 0) {
            System.out.println(num + " is a Niven Number");
        } else {
            System.out.println(num + " is not a Niven Number");
        }
    }
}
