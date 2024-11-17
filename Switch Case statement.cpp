double areaSwitchCase(int ch, vector<double> a) {
    double area = 0.0;

    switch (ch) {
        case 1: {
            // Calculate the area of a circle
            double r = a[0];
            area = M_PI * r * r; // Using M_PI for pi from <cmath>
            break;
        }
        case 2: {
            // Calculate the area of a rectangle
            double l = a[0];
            double b = a[1];
            area = l * b;
            break;
        }
        default:
            // Invalid choice, return 0.0
            area = 0.0;
            break;
    }

    // Return the area rounded to 5 decimal places
    return area;
}
