#include <iostream>
#include <vector>
#include <omp.h>

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

void find_primes(int start, int end, std::vector<int>& primes, double& thread_time) {
    double start_time = omp_get_wtime();
    for (int i = start; i <= end; ++i) {
        if (is_prime(i)) {
#pragma omp critical
            primes.push_back(i);
        }
    }
    double end_time = omp_get_wtime();
    thread_time = end_time - start_time;
}

int main() {
    const int N = 100000000;

    std::vector<int> primes;
    primes.reserve(N / 10);

    for (int num_threads = 1; num_threads <= 8; ++num_threads) {
        omp_set_num_threads(num_threads);

        double total_time = 0.0;

#pragma omp parallel
        {
            int thread_id = omp_get_thread_num();
            int chunk_size = N / num_threads;
            int start = thread_id * chunk_size + 1;
            int end = (thread_id == num_threads - 1) ? N : (thread_id + 1) * chunk_size;

            double thread_time;
            find_primes(start, end, primes, thread_time);

#pragma omp critical
            total_time += thread_time;
        }

        std::cout << "Using " << num_threads << " threads, Total execution time: " << total_time << " seconds" << std::endl;
    }

    return 0;
}
