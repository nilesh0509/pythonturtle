import java.util.*;
class love{
    public static void main(String args[]){

        // int main() 
        // {
            Scanner scanner = new Scanner(System.in);
            System.out.println("\n press n for 1. ");
            System.out.println("\n press * for 2. ");
            System.out.println("\n press + for 3. ");
            System.out.println("\n Enter Option: ");
            // scanf("%d",&i);
            int i = scanner.nextInt();
        
            switch (i)
            {
            case 1:{
                 System.out.println("\n n n n n n       n           n  n  n     n             n    n n n n       n      n     n n n      n       n  ");
                 System.out.println("\n     n           n          n       n     n           n     n               n   n    n       n    n       n  ");
                 System.out.println("\n     n           n          n       n      n         n      n n n             n      n       n    n       n  ");
                 System.out.println("\n     n           n          n       n       n       n       n                 n      n       n    n       n  ");
                 System.out.println("\n n n n n n       n n n n     n  n  n         n n n n        n n n n           n        n n n        n n n    ");
                break;
            }
            case 2:{
                System.out.println("\n * * * * *       *           *  *  *     *             *    * * * *       *      *     * * *      *       *  ");
                System.out.println("\n     *           *          *       *     *           *     *               *   *    *       *    *       *  ");
                System.out.println("\n     *           *          *       *      *         *      * * *             *      *       *    *       *  ");
                System.out.println("\n     *           *          *       *       *       *       *                 *      *       *    *       *  ");
                System.out.println("\n * * * * *       * * * *     *  *  *         * * * *        * * * *           *        * * *        * * *    ");
                break;
            }
            case 3:{
                System.out.println("\n + + + + +       +           +  +  +     +             +    + + + +       +      +     + + +      +       +  ");
                System.out.println("\n     +           +          +       +     +           +     +               +   +    +       +    +       +  ");
                System.out.println("\n     +           +          +       +      +         +      + + +             +      +       +    +       +  ");
                System.out.println("\n     +           +          +       +       +       +       +                 +      +       +    +       +  ");
                System.out.println("\n + + + + +       + + + +     +  +  +         + + + +        + + + +           +        + + +        + + +    ");
                break;
            }
            
            default:
                break;
            // }
            // return 0;
            }
    }
}
