public class Solution {
    public static int calcGCD(int n, int m){
        // Using the Euclidean Algorithm
        while (m != 0) {
            int temp = m;
            m = n % m;
            n = temp;
        }
        return n; // The GCD
    }
}
