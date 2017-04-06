/* 
Objective 
Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
Task 
Given an array, , of size  containing distinct elements , sort array  in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:

 
where  is the number of swaps that took place.
 
where  is the first element in the sorted array.
 
where  is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format

The first line contains an integer, , denoting the number of elements in array . 
The second line contains  space-separated integers describing , where the  integer is , .

Constraints

, 
Output Format

There should be  lines of output:

 
where  is the number of swaps that took place.
 
where  is the first element in the sorted array.
 
where  is the last element in the sorted array.
Sample Input 0

3
1 2 3
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3 */


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        bubbleSort(a);
    }
    
    public static void bubbleSort(int[] x) {
        
        int endPosition = x.length - 1;
        int swapPosition;
        int swaps = 0;
        
        while( endPosition > 0 ) {
            swapPosition = 0;
            
            for(int i = 0; i < endPosition; i++) {
                
                if( x[i] > x[i + 1] ){
                    // Swap elements 'i' and 'i + 1':
                    int tmp = x[i];
                    x[i] = x[i + 1];
                    x[i + 1] = tmp;
                    swaps++;
                    
                    swapPosition = i;
                } // end if
            } // end for
            
            endPosition = swapPosition;
        } // end while
        
        System.out.println("Array is sorted in "+ swaps + " swaps.");
        System.out.println("First Element: " + x[0]);
        System.out.println("Last Element: " + x[x.length - 1]);
    } // end bubbleSort
    
    private static void printArray(String s, int[] x) {
        System.out.print(s + " Array: "); 
        for(int i : x){
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
