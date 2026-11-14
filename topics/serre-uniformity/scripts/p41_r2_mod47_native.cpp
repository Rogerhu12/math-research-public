#include <algorithm>
#include <cstdint>
#include <vector>

namespace {
constexpr int p = 47;
int inv(int a) {
    for (int x = 1; x < p; ++x) if (a*x % p == 1) return x;
    return 0;
}
}

extern "C" int r2_rank_p(int m, int n, const int64_t* in_r, const int64_t* in_i,
                          int32_t* selected_rows, int32_t* selected_cols) {
    std::vector<int32_t> ar(m*n), ai(m*n), permutation(m), pr(n), pi(n);
    for (int i = 0; i < m*n; ++i) {
        ar[i] = (in_r[i] % p + p) % p;
        ai[i] = (in_i[i] % p + p) % p;
    }
    for (int i = 0; i < m; ++i) permutation[i] = i;
    int rank = 0;
    for (int c = 0; c < n && rank < m; ++c) {
        int pivot = rank;
        while (pivot < m && ar[pivot*n+c] == 0 && ai[pivot*n+c] == 0) ++pivot;
        if (pivot == m) continue;
        if (pivot != rank) {
            for (int j = c; j < n; ++j) {
                std::swap(ar[rank*n+j], ar[pivot*n+j]);
                std::swap(ai[rank*n+j], ai[pivot*n+j]);
            }
            std::swap(permutation[rank], permutation[pivot]);
        }
        selected_rows[rank] = permutation[rank];
        selected_cols[rank] = c;
        int a = ar[rank*n+c], b = ai[rank*n+c];
        int ii = inv((a*a+b*b) % p);
        int ir = a*ii % p;
        ii = (p-b*ii % p) % p;
        for (int j = c; j < n; ++j) {
            pr[j] = (ar[rank*n+j]*ir-ai[rank*n+j]*ii+p*p) % p;
            pi[j] = (ar[rank*n+j]*ii+ai[rank*n+j]*ir) % p;
        }
        for (int i = rank+1; i < m; ++i) {
            int vr = ar[i*n+c], vi = ai[i*n+c];
            if (vr == 0 && vi == 0) continue;
            for (int j = c; j < n; ++j) {
                ar[i*n+j] = (ar[i*n+j]-vr*pr[j]+vi*pi[j]+3*p*p) % p;
                ai[i*n+j] = (ai[i*n+j]-vr*pi[j]-vi*pr[j]+3*p*p) % p;
            }
        }
        ++rank;
    }
    return rank;
}

extern "C" int r2_inverse_p(int n, const int64_t* in_r, const int64_t* in_i,
                             int64_t* out_r, int64_t* out_i) {
    const int cols = 2*n;
    std::vector<int32_t> ar(n*cols, 0), ai(n*cols, 0), pr(cols), pi(cols);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ar[i*cols+j] = (in_r[i*n+j] % p+p) % p;
            ai[i*cols+j] = (in_i[i*n+j] % p+p) % p;
        }
        ar[i*cols+n+i] = 1;
    }
    for (int k = 0; k < n; ++k) {
        int pivot = k;
        while (pivot < n && ar[pivot*cols+k] == 0 && ai[pivot*cols+k] == 0) ++pivot;
        if (pivot == n) return -1;
        if (pivot != k) {
            for (int j = 0; j < cols; ++j) {
                std::swap(ar[k*cols+j], ar[pivot*cols+j]);
                std::swap(ai[k*cols+j], ai[pivot*cols+j]);
            }
        }
        int a = ar[k*cols+k], b = ai[k*cols+k];
        int ii = inv((a*a+b*b) % p);
        int ir = a*ii % p;
        ii = (p-b*ii % p) % p;
        for (int j = 0; j < cols; ++j) {
            pr[j] = (ar[k*cols+j]*ir-ai[k*cols+j]*ii+p*p) % p;
            pi[j] = (ar[k*cols+j]*ii+ai[k*cols+j]*ir) % p;
        }
        for (int j = 0; j < cols; ++j) {
            ar[k*cols+j] = pr[j];
            ai[k*cols+j] = pi[j];
        }
        for (int i = 0; i < n; ++i) {
            if (i == k) continue;
            int vr = ar[i*cols+k], vi = ai[i*cols+k];
            if (vr == 0 && vi == 0) continue;
            for (int j = 0; j < cols; ++j) {
                ar[i*cols+j] = (ar[i*cols+j]-vr*pr[j]+vi*pi[j]+3*p*p) % p;
                ai[i*cols+j] = (ai[i*cols+j]-vr*pi[j]-vi*pr[j]+3*p*p) % p;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (ar[i*cols+j] != int(i == j) || ai[i*cols+j] != 0) return -2;
            out_r[i*n+j] = ar[i*cols+n+j];
            out_i[i*n+j] = ai[i*cols+n+j];
        }
    }
    return 0;
}
