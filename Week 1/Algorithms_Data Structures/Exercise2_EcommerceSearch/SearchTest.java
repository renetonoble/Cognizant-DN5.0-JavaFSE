import java.util.Arrays;
import java.util.Comparator;

public class SearchTest {

    static Product linearSearch(Product[] products, String name) {
        for (Product p : products) {
            if (p.productName.equalsIgnoreCase(name)) {
                return p;
            }
        }
        return null;
    }

    static Product binarySearch(Product[] products, String name) {
        int low = 0, high = products.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            int cmp = products[mid].productName.compareToIgnoreCase(name);
            if (cmp == 0) return products[mid];
            else if (cmp < 0) low = mid + 1;
            else high = mid - 1;
        }
        return null;
    }

    public static void main(String[] args) {

        Product[] products = {
            new Product(101, "Laptop", "Electronics"),
            new Product(102, "Headphones", "Electronics"),
            new Product(103, "Running Shoes", "Footwear"),
            new Product(104, "Coffee Maker", "Appliances"),
            new Product(105, "Java Book", "Books"),
            new Product(106, "Monitor", "Electronics"),
            new Product(107, "Backpack", "Accessories")
        };

        System.out.println("Linear Search:");
        Product result = linearSearch(products, "Coffee Maker");
        System.out.println(result != null ? "Found: " + result : "Not found");

        result = linearSearch(products, "Tablet");
        System.out.println(result != null ? "Found: " + result : "Not found");

        Product[] sorted = products.clone();
        Arrays.sort(sorted, Comparator.comparing(p -> p.productName.toLowerCase()));

        System.out.println("\nBinary Search (sorted array):");
        result = binarySearch(sorted, "Java Book");
        System.out.println(result != null ? "Found: " + result : "Not found");

        result = binarySearch(sorted, "Tablet");
        System.out.println(result != null ? "Found: " + result : "Not found");
    }
}
