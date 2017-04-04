// # Objective 
// # Today, we're learning about Interfaces. Check out the Tutorial tab for learning materials and an instructional video!

// # Task 
// # The AdvancedArithmetic interface and the method declaration for the abstract int divisorSum(int n) method are provided for you in the editor below. Write the Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum method must be public and take an integer parameter, , and return the sum of all its divisors.

// # Note: Because we are writing multiple classes in the same file, do not use an access modifier (e.g.: public) in your class declaration (or your code will not compile); however, you must use the public access modifier before your method declaration for it to be accessible by the other classes in the file.

// # Input Format

// # A single line containing an integer, .

// # Constraints

// # Output Format

// # You are not responsible for printing anything to stdout. The locked Solution class in the editor below will call your code and print the necessary output.

// # Sample Input

// # 6
// # Sample Output

// # I implemented: AdvancedArithmetic
// # 12

import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}


class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n){
        int sumDivisors = 1 + n;
        if (n == 1) return 1;
        
        for(int i = 2; i < (n/2 + 1); i++){
            if( n % i == 0){
                sumDivisors += i;
            }
        }
        return sumDivisors;
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}