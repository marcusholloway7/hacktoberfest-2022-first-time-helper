public class FibonacciSeries {
    public static void main(String[] args){

//  fibonacci series = 0,1,1,2,3,5,8,13,21.........
//  it is  the addition of the previous two numbers like 0+1=1, 1+1=2, 2+1=3, 3+2=5,
//   5+3=8, 8+13=21, 13+21=34 and so on.
    int a,b,sum;
    a=0;
    b=1;
    sum=0;
    System.out.println("0");
    for(int i=0;i<=15;i++){
        sum=a+b;
        System.out.println(sum);
        b=a;
        a=sum;
        
    }
    }
}
