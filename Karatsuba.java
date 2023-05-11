import java.math.BigInteger;
import java.util.Scanner;
public class Karatsuba {
    private static int numberLength(BigInteger num){
        return num.toString().length();
    }

    public static BigInteger karatsubaMultiplication(BigInteger numOne, BigInteger numTwo){
        if(numberLength(numOne)<2 && numberLength(numTwo)<2) {
            return numOne.multiply(numTwo);
        }
        int halfLength = (int) Math.ceil(Math.max(numberLength(numOne),numberLength(numTwo))/2);
        BigInteger half = new BigInteger("10").pow(halfLength);
        BigInteger a = numOne.divide(half);
        BigInteger b = numOne.mod(half);
        BigInteger c = numTwo.divide(half);
        BigInteger d = numTwo.mod(half);
        BigInteger x = karatsubaMultiplication(a,c);
        BigInteger y = karatsubaMultiplication(a.add(b),c.add(d));
        BigInteger z = karatsubaMultiplication(b,d);
        BigInteger firstMiddleOp = x.multiply(new BigInteger("10").pow(halfLength*2));
        BigInteger secondMiddleOp = y.subtract(x).subtract(z).multiply(new BigInteger("10").pow(halfLength));
        BigInteger result = firstMiddleOp.add(secondMiddleOp).add(z);
        return result;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        BigInteger a,b;
        a = input.nextBigInteger();
        b = input.nextBigInteger();
        System.out.println(karatsubaMultiplication(a,b).toString());
    }
}
