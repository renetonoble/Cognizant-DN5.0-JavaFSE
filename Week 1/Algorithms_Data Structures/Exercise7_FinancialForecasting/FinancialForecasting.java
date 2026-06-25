public class FinancialForecasting {

    static double futureValue(double amount, double rate, int years) {
        if (years == 0) return amount;
        return futureValue(amount * (1 + rate), rate, years - 1);
    }

    public static void main(String[] args) {

        double principal = 10000.0;
        double rate = 0.08;
        int years = 10;

        System.out.println("Principal: " + principal);
        System.out.println("Rate: " + (rate * 100) + "%");
        System.out.println("Years: " + years);
        System.out.println();

        for (int y = 1; y <= years; y++) {
            double fv = futureValue(principal, rate, y);
            System.out.printf("Year %2d: %.2f%n", y, fv);
        }

        System.out.printf("%nFuture value after %d years: %.2f%n", years, futureValue(principal, rate, years));
    }
}
