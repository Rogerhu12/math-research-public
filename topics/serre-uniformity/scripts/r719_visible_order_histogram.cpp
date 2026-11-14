// R719: exact primary visible points and actual orders for p = 137147.
// All output is a complete finite enumeration. No floating-point arithmetic
// is used in admissibility, field arithmetic, orders, or the cutoff.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using i64 = std::int64_t;
using u64 = std::uint64_t;
using u32 = std::uint32_t;
static constexpr i64 p = 137147;
static constexpr i64 M = (p+1)/3;
static constexpr i64 radius_multiplier = 25;
static constexpr i64 cutoff = radius_multiplier*p;
static constexpr i64 audit_cutoff = 10000;
static constexpr std::array<i64,6> bad{{11,22,1039,2078,11429,22858}};
static constexpr std::array<i64,6> phi{{10,10,1038,1038,10380,10380}};
static constexpr std::array<i64,3> prime_factors{{2,11,1039}};
static i64 mod(i64 x) { x %= p; return x<0 ? x+p : x; }
static u64 isqrt(u64 n) {
    u64 lo=0,hi=1;
    while (hi<=n/hi) hi*=2;
    while (hi-lo>1) { u64 mid=(lo+hi)/2;
        if(mid<=n/mid) lo=mid; else hi=mid; }
    return lo;
}
static bool prime(i64 n) {
    if(n<2) return false;
    for(i64 d=2;d*d<=n;++d) if(n%d==0) return false;
    return true;
}
struct F {
    i64 a,b;
    bool operator==(const F& z) const { return a==z.a && b==z.b; }
};
static F mul(const F& x,const F& y) {
    return {mod(x.a*y.a-x.b*y.b),mod(x.a*y.b+x.b*y.a-x.b*y.b)};
}
static F power(F a,u64 n) {
    F r{1,0};
    while(n) {if(n&1) r=mul(r,a);a=mul(a,a);n>>=1;}
    return r;
}
static i64 order(F u) {
    if(!(power(u,M)==F{1,0})) throw std::runtime_error("u not in C_M");
    i64 o=M;
    for(auto l:prime_factors)
        while(o%l==0 && power(u,o/l)==F{1,0}) o/=l;
    if(!(power(u,o)==F{1,0})) throw std::runtime_error("order failure");
    for(auto l:prime_factors)
        if(o%l==0 && power(u,o/l)==F{1,0})
            throw std::runtime_error("order not exact");
    return o;
}
static i64 first_residue(i64 low,i64 residue) {
    i64 r=(low-residue)%3;if(r<0)r+=3;
    return low+(3-r)%3;
}
int main(int argc,char** argv) {
    try {
        if(argc!=2) throw std::runtime_error("usage: enumerator OUTPUT_DIRECTORY");
        std::filesystem::path out(argv[1]);
        std::filesystem::create_directories(out);
        if(!prime(p)||!prime(11)||!prime(1039)||p%3!=2 ||
           M!=4*11*1039) throw std::runtime_error("fixed parameters invalid");
        std::vector<i64> inv(p,0);inv[1]=1;
        for(i64 a=2;a<p;++a) inv[a]=p-(p/a)*inv[p%a]%p;
        for(i64 a=1;a<p;++a)
            if(a*inv[a]%p!=1) throw std::runtime_error("inverse table failure");
        std::vector<std::array<u32,6>> hist(cutoff+1);
        std::map<i64,u64> all_orders;
        std::array<u64,6> totals{};
        u64 primary_box=0,geometry=0,primitive=0,admissible=0,excluded_6p=0;
        u64 small_count=0,direct_checks=0;
        const i64 box=isqrt((4*cutoff)/3);
        std::ofstream small(out/"small_radius_points.csv");
        if(!small) throw std::runtime_error("cannot open small-radius output");
        small<<"a,b,n,u0,u1,order\n";
        for(i64 b=first_residue(-box,0);b<=box;b+=3) {
            for(i64 a=first_residue(-box,1);a<=box;a+=3) {
                ++primary_box;
                const i64 n=a*a-a*b+b*b;
                if(n<=0||n>cutoff)continue;
                ++geometry;
                if(std::gcd(std::llabs(a),std::llabs(b))!=1)continue;
                ++primitive;
                if(std::gcd(n,6*p)!=1){++excluded_6p;continue;}
                ++admissible;
                F beta{mod(a),mod(b)},conj{mod(a-b),mod(-b)};
                F ratio=mul(conj,conj);
                const i64 ni=inv[n%p];
                ratio={ratio.a*ni%p,ratio.b*ni%p};
                F u=mul(mul(ratio,ratio),ratio);
                const i64 o=order(u);
                ++all_orders[o];
                for(std::size_t j=0;j<bad.size();++j)
                    if(o==bad[j]){++hist[n][j];++totals[j];}
                if(n<=audit_cutoff) {
                    F direct=power(beta,3*(p-1));
                    if(!(direct==u))throw std::runtime_error("direct-power mismatch");
                    ++direct_checks;++small_count;
                    small<<a<<","<<b<<","<<n<<","<<u.a<<","<<u.b<<","<<o<<"\n";
                }
            }
        }
        small.close();
        std::ofstream h(out/"norm_order_counts.csv");
        if(!h)throw std::runtime_error("cannot open norm output");
        h<<"n";
        for(auto o:bad)h<<",order_"<<o;
        h<<"\n";
        u64 nonzero_norms=0;
        for(i64 n=1;n<=cutoff;++n) {
            bool nz=false;for(auto c:hist[n])nz=nz||c!=0;
            if(!nz)continue;
            ++nonzero_norms;h<<n;
            for(auto c:hist[n])h<<","<<c;
            h<<"\n";
        }
        h.close();
        std::ofstream meta(out/"enumeration_metadata.json");
        meta<<"{\n"
            <<"  \"schema\": \"r719.primary-visible-orders.v1\",\n"
            <<"  \"p\": "<<p<<", \"M\": "<<M<<",\n"
            <<"  \"M_factorization\": {\"2\": 2, \"11\": 1, \"1039\": 1},\n"
            <<"  \"radius_multiplier\": "<<radius_multiplier<<",\n"
            <<"  \"norm_cutoff\": "<<cutoff<<", \"coordinate_bound\": "<<box<<",\n"
            <<"  \"independent_audit_norm_cutoff\": "<<audit_cutoff<<",\n"
            <<"  \"primary_box_count\": "<<primary_box<<",\n"
            <<"  \"primary_in_circle_count\": "<<geometry<<",\n"
            <<"  \"primitive_in_circle_count\": "<<primitive<<",\n"
            <<"  \"excluded_by_gcd_6p\": "<<excluded_6p<<",\n"
            <<"  \"admissible_count\": "<<admissible<<",\n"
            <<"  \"small_radius_count\": "<<small_count<<",\n"
            <<"  \"direct_power_checks\": "<<direct_checks<<",\n"
            <<"  \"nonzero_norm_rows\": "<<nonzero_norms<<",\n"
            <<"  \"histogram_omitted_norms_have_all_six_counts_zero\": true,\n"
            <<"  \"bad_orders\": [";
        for(std::size_t j=0;j<bad.size();++j)meta<<(j?", ":"")<<bad[j];
        meta<<"],\n  \"bad_order_phi\": [";
        for(std::size_t j=0;j<phi.size();++j)meta<<(j?", ":"")<<phi[j];
        meta<<"],\n  \"bad_order_totals\": [";
        for(std::size_t j=0;j<totals.size();++j)meta<<(j?", ":"")<<totals[j];
        meta<<"],\n  \"all_exact_order_totals\": {";
        bool comma=false;
        for(const auto& [o,c]:all_orders){meta<<(comma?", ":"")<<"\""<<o<<"\": "<<c;comma=true;}
        meta<<"},\n  \"all_inverse_entries_verified\": true,\n"
            <<"  \"all_u_orders_divide_M_and_are_exact\": true,\n"
            <<"  \"direct_small_radius_checks_complete\": true\n}\n";
        meta.close();
        std::cout<<"Complete exact primary visible enumeration; points="
                 <<admissible<<"; nonzero norm rows="<<nonzero_norms
                 <<"; small radius checked="<<small_count<<"\n";
        return 0;
    } catch(const std::exception& e) {
        std::cerr<<"R719 enumeration failed: "<<e.what()<<"\n";return 1;
    }
}
