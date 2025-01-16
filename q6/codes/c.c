#include <stdlib.h>

void gen_line_points(double slope, double c, int num_points, double *points){
    double left_lim = -10;  // You can adjust this as needed.
    double right_lim = 60; // You can adjust this as needed.
    double h = (right_lim - left_lim) / num_points;

    for (int i = 0; i < num_points; i++){
        points[2*i] = left_lim;  // X-coordinate
        points[2*i + 1] = (slope * left_lim) + c;  // Y-coordinate
        
        left_lim += h;
    }
}

void free_ptr(double *points){
    free(points);
}

int main() {
    int num_points = 100;  // Number of points to generate for each line.
    
    // Allocate memory for storing points for both lines
    double *points_line1 = (double *)malloc(2 * num_points * sizeof(double));  // Points for first line
    double *points_line2 = (double *)malloc(2 * num_points * sizeof(double));  // Points for second line
    
    // Generate points for both lines
    double slope1 = 5.0 / 4.0, c1 = 2.0;
    double slope2 = -7.0 / 6.0, c2 = 3.0 / 2.0;
    
    gen_line_points(slope1, c1, num_points, points_line1);
    gen_line_points(slope2, c2, num_points, points_line2);

    // Free the allocated memory
    free_ptr(points_line1);
    free_ptr(points_line2);

    return 0;
}

