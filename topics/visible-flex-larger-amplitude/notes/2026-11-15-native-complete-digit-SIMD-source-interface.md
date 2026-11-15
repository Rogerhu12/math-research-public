# R414 完整 signed-digit SIMD 源码接口

作者：OpenAI / ChatGPT，2026-11-15。

## 1. 交付与发布位置

本交付是可被独立完整后继包含的源码和条件证明。没有新科学请求，不修改 request186、190、192，也没有声称实际 CPU 已使用 SIMD 或完整链已提速。

| 发布路径（课题内） | bytes | SHA256 |
|---|---:|---|
| computations/geometry_20261115_native_simd_exact_digit128.hpp | 9006 | 1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6 |
| results/R414-complete-signed-digit-SIMD-and-RN113-equivalence.md | 15800 | 9b5bd117b0a44a618ff15ebf77dbb4dda9271d66cf4ed03276021eba86085d95 |

直接依赖是已刊 R405 头文件 computations/geometry_20261115_native_exact_digit128.hpp，18871 B / 5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc。本新头文件确实包含该 basename。没有 BLAS、Boost、第三方 SIMD 库、额外 package 或动态安装。

完整数学范围见 [R414](../results/R414-complete-signed-digit-SIMD-and-RN113-equivalence.md)。它证明在约定编译与输入条件下，对同一已完成 dot 返回 R405 相同字词；不扩成原顺序 Q 算术图的等价，不扩成 R402 全链误差证书。正文保真实名义 Lhat 与 C 的区别。

## 2. 本次实际改动

R405 20-bit 每个 plane-pair 的原 scalar partial 被独立实现替换。其余完整对象仍直接使用旧函数或保持相同全文循环：

| 部分 | 新实现的责任 |
|---|---|
| 原 binary128 解码、113-bit 尾数、符号、实际指数跨度 | 直接调用 R405 prepare |
| 原十二层快速上限、64 MiB packing、完整 Word fallback | 直接调用 R405 prepare |
| 准确 partial | 新 scalar reducer 或 AVX2 even+odd reducer |
| 跨层 shift、完整正负宽整数、唯一 RN113 | 直接调用 R405 ExactSum |
| 已为零或任一对象未 packed | 直接调用 R405 dot |
| 矩阵左右准备与全 i,j 覆盖 | 保持 R405 的完整 row-major 循环及分配 |
| CPU 检测和覆盖计数 | 新增执行 metadata；不参加数学接受 |

每个 block 仍至多 2048 项。对每项 $|\mathrm{digit}|\le 2^{20}-1$，任意部分和绝对值均小于 $2^{51}$。AVX2 的四个 even 和四个 odd 位置全部进入准确 int64；odd 先在每个 64bit lane 内逻辑右移 32，再由 signed mul_epi32 解释低 32bit。所有尾项标量准确乘加。

完整 k 可以更大，由原分块循环覆盖。指数差较宽不压进十二层，而委托原 full-width 整数路径。没有丢尾、取低 32 位乘积、无符号误乘、统一六层截断或省略 odd lanes。

## 3. C++ API 与 source-only 最小接点

新命名空间 exact_digit_simd128：

- Q、Poll、VectorView、PackedVector 与 R405 类型兼容。
- prepare、encode、checked_product、poll_if 直接引用原函数。
- DIGIT_BITS、REDUCTION_BLOCK、FAST_LIMB_LIMIT、PACKING_BYTES_LIMIT 对应原常数，前三个以编译期结构断言固定 20/2048/12。
- Stats 继承 exact_digit128::Stats，并有新 backend/覆盖字段和 join。
- dot(PackedVector, PackedVector, Stats&, Poll)、dot(VectorView, VectorView, Stats&, Poll)。
- multiply(const Q*, const Q*, size_t m, size_t k, size_t n, Stats&, Poll)。
- selected_backend()、selected_backend_name()、avx2_body_compiled()。

假设未来另建完整 R402/192 消费者，必须给新源码 basename/schema/pin，并在它自身明确将原 dot/multiply 及 Stats 改接本 namespace。原 prepare 的 PackedVector 可以继续使用；Stats 必须是新 derived 类型，不能仍声明旧 Stats 后丢失新 metadata。新头文件自身不通过宏重命名旧 namespace，也不运行时篡改旧实现。

当前 R192 的 RightCache 已准备右列后逐行调用 dot，这种消费方式可以直接使用本 API；它不要求为 SIMD 改变矩阵维数或重新量化。原 DenseMap 批量 multiply 同样有完整入口。未来接线时需保所有原 assembly 小系数、actual Lhat 两代回、完整 C*ds−right 及原 root/finite/audit范围；本交付未生成该未来 dispatcher、request 或 workflow。

禁止仅替换 source 字符串标签后声称旧已跑 binary 使用新 SIMD。后继真实可执行身份、compiled flags、实际 runtime backend 和必要计数均需由那个真实 job 返回。

## 4. Runtime dispatch 与编译合同

GNU x86 且编译器版本支持时，AVX2 函数单独使用 target("avx2"), noinline。普通运行阶段第一次访问通过 __builtin_cpu_init / __builtin_cpu_supports("avx2") 选函数指针；函数内 static 初始化供线程安全共享。未支持或该专用 body 未编译时，走完整 scalar reducer。

整个调用翻译单元必须保原 baseline 目标选项，不能全局加 -mavx2、-march=native 后冒称运行时 fallback 可保护所有指令。函数级 target 才是新增 ISA 的边界。当前实现只在 GNU x86 分支提供 AVX2 body；其他可满足原 R405 ABI 的编译环境走 scalar。它不新增编译器 portability 声明。

CPU 信息只决定实现方法，不是新科学门。无需先对一组科学数据对拍、预跑微基准、换原数学阈值或跳过任何列。实际平台对 ISA 的报告和编译器实现必须可靠；proof不代付硬件/OS异常。

当前没有运行编译、AST、科学模块导入、numerical probe 或 benchmark。未来完整 Actions 的既存编译阶段负责真实可执行构建；不能把这份源码审核记录写成已编译成功。

## 5. 必要 metadata 与原语义

保原 R405 所有 Stats。新增以下字段：

| 字段 | 含义 |
|---|---|
| scalar_digit_blocks | 运行时 scalar backend 完成的 digit block 数 |
| avx2_digit_blocks | 运行时 AVX2 backend 完成的 block 数 |
| avx2_complete_octets | AVX2 循环完整八项组数 |
| avx2_even_products | even 分支完整 32×32→64 乘积数 |
| avx2_odd_products | odd 分支完整 32×32→64 乘积数 |
| scalar_backend_products | scalar backend 实际项数 |
| avx2_scalar_tail_products | AVX2 backend 中末尾 0–7 项实际数 |
| delegated_zero_calls | 完整 zero 分支直接交原 dot 的次数 |
| delegated_wide_calls | 完整 wide 分支直接交原 dot 的次数 |
| largest_digit_block | 已完成 block 最大项数 |

avx2_body_compiled 与 selected_backend_name 是两项独立记录。专用函数被编译不等于实际使用；unsupported不是科学失败。所有计数是实际消费范围和实现选择，不是接受条件。不得据期望维数伪填这些计数。

每个线程继续拥有自己的 Stats，结束后通过 join 汇总；没有为并发写同一个统计对象增设同步。原 cancellation/poll 和真实异常照付。原 block 分界不变，但运行时间可能不同，因此预算触发时的未完成范围不能照抄旧 job。

字节输出沿完整后继原必要单份 ≤90KB合同；新增上述小字段和实际 backend即可。不要为这一优化另搬 full matrices、原成功列大树或新 encoded raw；需要的原科学必要范围不减。

## 6. 精度、性能与尚未执行

准确结论严格限定为：同完整字词输入、同 R405 packing/宽 fallback、未中止且符合编译/表示合同的调用，新 scalar/AVX2 partial 都等于原准确整数 partial，最终 dot 字词相同。正规/次正规、负零、溢出和全指数范围都继承同一原舍入程序。

这不证明 R405 比190旧有限求和更接近完整实际导数，也不支付 $H_s$ 等小矩阵的原形成/重关联误差。没有把实际 $\widehat L\widehat L^\top$ 变成 $C$，没有新 branch-stability/implicit-root/continuous-ODE声明。

潜在开销改善仅来自 packed digit block 内并行整数乘加。完整 prepare、wide fallback、准确宽累加、矩阵形成、两个三角回代、Stage/RK以及其他消费者仍有原成本。没有倍率、完成576×224所需时间或原预算足够的断言。任何后继都应真实跑完整目标，不能以孤立微基准代替。

本阶段无 request196或其他新请求文件、无未来run/source参数、无本地science、无Gitref更新。186/190/192保持其已发字节和各自原终态责任。
