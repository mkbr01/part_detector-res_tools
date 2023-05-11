#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

struct PCAData {
    std::vector<double> center;
    double area;
    std::vector<double> axes;
    std::vector<double> eigen_values;
    std::vector<std::vector<double>> eigen_vectors;
    double total_variance;
    std::vector<double> percentage_variance;
    std::vector<double> angles;
    double eccentricity;
    double slope;
    std::vector<int> handles;
};

PCAData pca2d(std::vector<double> u, std::vector<double> v) {
    PCAData s;
    
    // Centering the data
    double sum_u = 0.0, sum_v = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        sum_u += u[i];
        sum_v += v[i];
    }
    double mean_u = sum_u / u.size();
    double mean_v = sum_v / v.size();
    s.center = { mean_u, mean_v };
    
    // Removing NaN values
    std::vector<double> cleaned_u, cleaned_v;
    for (size_t i = 0; i < u.size(); ++i) {
        if (std::isfinite(u[i]) && std::isfinite(v[i])) {
            cleaned_u.push_back(u[i]);
            cleaned_v.push_back(v[i]);
        }
    }
    
    // Calculating covariance matrix and eigenvalues
    size_t n = cleaned_u.size();
    double cov_uu = 0.0, cov_uv = 0.0, cov_vv = 0.0;
    for (size_t i = 0; i < n; ++i) {
        double dev_u = cleaned_u[i] - mean_u;
        double dev_v = cleaned_v[i] - mean_v;
        cov_uu += dev_u * dev_u;
        cov_uv += dev_u * dev_v;
        cov_vv += dev_v * dev_v;
    }
    cov_uu /= n;
    cov_uv /= n;
    cov_vv /= n;
    
    std::vector<std::vector<double>> eigvecmat(2, std::vector<double>(2));
    std::vector<double> eigvalmat(2);
    
    eigvalmat[0] = (cov_uu + cov_vv + sqrt((cov_uu - cov_vv) * (cov_uu - cov_vv) + 4.0 * cov_uv * cov_uv)) / 2.0;
    eigvalmat[1] = (cov_uu + cov_vv - sqrt((cov_uu - cov_vv) * (cov_uu - cov_vv) + 4.0 * cov_uv * cov_uv)) / 2.0;
    
    eigvecmat[0][0] = cov_vv - eigvalmat[0];
    eigvecmat[1][0] = cov_vv - eigvalmat[1];
    eigvecmat[0][1] = cov_uv;
    eigvecmat[1][1] = cov_uv;
    
    // Calculating eigenvalues and eigenvectors
    std::vector<double> eigval(2);
    std::vector<std::vector<double>> eigvecmat_t(2, std::vector<double>(2));
    eigval[0] = eigvalmat[0];
    eigval[1] = eigvalmat[1];
    eigvecmat_t[0][0] = eigvecmat[0][0];
    eigvecmat_t[1
