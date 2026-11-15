# R414. 完整 20-bit digit 点积的 SIMD 偶奇覆盖、整数等价与一次 RN113

作者：OpenAI / ChatGPT，2026-11-15。

## 1. 对象、已付范围与独立源码

本结果接续 [R405](R405-complete-dyadic-digits-and-once-rounded-binary128-dot-products.md) 和 [R402](R402-recorded-literal-block-operator-equivalence-and-rounding-scope.md)。目标是加速 R405 已有的一个很具体的步骤：两个完整 signed-20-bit digit plane 在至多 2048 个坐标上的准确整数点积。所有完整字词解码、实际指数跨度、最多十二层的快速表示、宽指数替代路径、符号重构和唯一最终 RN113 舍入继续由原 R405 源码完成。

独立实现是 [geometry_20261115_native_simd_exact_digit128.hpp](../computations/geometry_20261115_native_simd_exact_digit128.hpp)，9006 B，SHA256：

1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6

它直接包含原 [geometry_20261115_native_exact_digit128.hpp](../computations/geometry_20261115_native_exact_digit128.hpp)，18871 B，SHA256：

5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc

旧文件不改。本次没有请求、运行、性能样本或科学数值输出。源码已按原文及下面的整数论证构造；没有本地编译、导入、数值执行、benchmark 或 fixture。未来是否纳入完整执行，仍须另有准确源身份与完整同 job 入口；本文件的存在不代表该入口已经执行。

**条件结论。** 对相同有限 binary128 输入字词、相同尺寸和原 packing 规则，假设原 R405 实现满足其已列的表示合同，所用编译器正确实现下述整数及 AVX2 指令语义，内存有效，且调用未因资源或外部预算中止，则新内核和 R405 返回相同的 binary128 字词。这个结论包括 subnormal、准确抵消、负非零舍入到负零和溢出规则。它不是与旧顺序 binary128 求和图的逐词等价，不是完整根导数的准确性证明，也不许把名义三角因子的乘积替换成原形成矩阵。

## 2. 原完整字词如何到达有限 digit 问题

对每个非零有限 binary128 字词，R405 精确写成

$$
x_n=\sigma_n M_n2^{e_n},\qquad
\sigma_n\in\{-1,1\},\quad M_n\in\mathbb N.
$$

正规字的原始尾数包含全部 113 位，指数为存储 exponent field 减 $16383+112$；次正规字使用固定指数 $-16494$。只允许去除尾数里实际为零的末位；没有截取统一六层或舍弃小尾数。

令一个实际向量的最小非零位指数为 $e_a$。原 prepare 在跨度允许时形成

$$
a_n=2^{e_a}\sum_{\ell=0}^{L_a-1}a_{\ell n}2^{20\ell},
\qquad
a_{\ell n}\in\mathbb Z,\qquad
|a_{\ell n}|\le D:=2^{20}-1.
$$

这里 $L_a$ 由整个向量真实最高位和最低位决定。另一向量类似。快速层数上限仍为十二，原全局 packing 内存上限仍为 64 MiB。超过层数或原 packing 预算时保留每个完整原 Word，并走原宽整数乘积路径；不是量化到可装下的层数。

因此准确点积满足

$$
\sum_n a_nb_n
=
2^{e_a+e_b}
\sum_{\ell=0}^{L_a-1}\sum_{r=0}^{L_b-1}
2^{20(\ell+r)}
\sum_n a_{\ell n}b_{rn}.
$$

新源码只更换最内层整数和的实现。原 layer-major 顺序、真实非零 plane 标识、每个完整输入坐标、每个至多 2048 项的 block、每个 block 的位移 $20(\ell+r)$ 都保留。跳过的只是在原 prepare 中逐项确认全零的 plane，不是抽样列、截断高位或低秩近似。

## 3. 为什么所有局部累加均不会溢出

设一个真实 block 的长度为 $0\le m\le 2048$，其中整数 $u_i,v_i$ 均满足 $|u_i|,|v_i|\le D$。每个乘积均先做 signed int32 到 signed int64 的准确拓宽，再相乘。因此

$$
|u_iv_i|\le D^2<2^{40},
$$

而任意坐标子集 $I$ 都有

$$
\left|\sum_{i\in I}u_iv_i\right|
\le
\sum_{i\in I}|u_iv_i|
\le
2048(2^{20}-1)^2
<
2^{51}
<
2^{63}.
$$

这个界同时覆盖：

1. scalar 原顺序的每个部分和；
2. SIMD 每个 even lane 或 odd lane 的每个部分和；
3. 将八个 lane 累积量合并的任意中间部分和；
4. 追加最后零至七项 scalar 尾部的每个部分和。

故 signed int64 的所有实际 C++ 标量加法和乘法都在可表示范围内，没有 signed overflow 或由其导致的未定义行为。AVX2 的 64 位向量加法虽按机器字给出低位结果，但上述界证明本调用从不发生数学溢出，故其返回字词就是准确有符号和。

此处没有依赖浮点加法、FMA、BLAS 的归约顺序或 binary64 中间量。也没有先做 int32 乘法再转 int64；后者会丢掉乘积高位，不满足本证明。

若完整 $k>2048$，原分块循环逐 block 应用本界，再把完整 int64 结果送入 R405 任意宽度的准确有符号累加器。不存在把全部 $k$ 项强行塞进一个 int64 的步骤。

## 4. 偶数与奇数位置的逐项覆盖

### 4.1 一次八项载入

一次向量循环只在剩余项至少为八时进入。通过 memcpy 精确读八个连续 int32 字词：

$$
A=(u_i,u_{i+1},\ldots,u_{i+7}),\qquad
B=(v_i,v_{i+1},\ldots,v_{i+7}).
$$

memcpy 表达不依赖输入对齐的合法字节复制；本次读取的范围不越过真实 block。源码不将原 int32 指针解引用成一个有更强对齐要求的向量对象。

官方 intrinsic 定义中，signed _mm256_mul_epi32 选择八个 int32 中的偶数位置，给出四个完整 signed int64 乘积。它不同于只返回乘积低 32 位的 _mm256_mullo_epi32，也不同于 unsigned 乘法。[1]

于是 even 累加器的四个本次增量为

$$
(u_iv_i,\ u_{i+2}v_{i+2},\ u_{i+4}v_{i+4},\ u_{i+6}v_{i+6}).
$$

### 4.2 奇数 lane 不能遗漏，也不能错误无符号化

在每个 64 位 lane 内逻辑右移 32 位，原高半部 int32 的全部 32 个 bit 被原样移到低半部。原高半部可能表示负整数；其符号位并没有丢失，它此时成为新低半部的第 31 位。

接着仍调用 signed _mm256_mul_epi32。该 intrinsic 按 signed int32 解释低半部，而不是将整个经逻辑移位后的 64 位字当作非负整数。因此四个 odd 增量准确是

$$
(u_{i+1}v_{i+1},\ u_{i+3}v_{i+3},\
 u_{i+5}v_{i+5},\ u_{i+7}v_{i+7}).
$$

上半部补零不改变这个 signed int32 解释。原 odd digit 为负时仍产生正确符号。本步不使用 unsigned _mm256_mul_epu32。[1]

### 4.3 全部 loop、horizontal reduction 和尾部

写 $m=8q+t$，$0\le t<8$。向量 loop 的起点依次为 $0,8,\ldots,8(q-1)$，每次处理上述八个互异位置。其 even 与 odd 的覆盖集合不交，并集恰为 $\{0,\ldots,8q-1\}$。

四个 even lane 与四个 odd lane 通过 memcpy 返回八个 int64 字。源码按 lane 逐个加入 scalar 总和，再逐项加入 $\{8q,\ldots,m-1\}$ 的 $t$ 个乘积。由第 3 节，每个中间量准确可表示。最终值因整数加法结合律恰为

$$
P=\sum_{i=0}^{m-1}u_iv_i.
$$

没有 horizontal 指令只处理一个 128 位半向量的遗漏，也没有把两个 128 位 half 的 lane 重复算两次。完整 $m=2048$ 时，八个 lane 各收 256 个乘积；短 block 和非八倍数长度使用同一覆盖论证，未访部分只可能来自外部明确中止。

## 5. 从 partial 等价提升到整个 dot 与矩阵

### 定理 1：每个已完成 packed dot 与 R405 逐词相同

两版本使用同一 prepare，故完整 digit、base、layers、active 标识一致。对每个相同的 $(\ell,r,\mathrm{block})$，R405 scalar partial 与新 SIMD 或新 scalar partial 根据第 3–4 节相等。

两版本以相同顺序，将该相同 int64 和相同 shift 传入同一个原 ExactSum::add_signed。归纳得到每次添加后的准确正、负整数累加器相同。因此末尾同一个原 ExactSum::rounded 接收相同 base 与准确整数，返回相同字词。这里甚至不必仅依赖最终整数值相等：block 分组及逐项外层加入顺序也保留。

### 定理 2：零向量与 wide fallback 范围保持

零向量、只有一方或双方未 packed 时，新 dot 直接调用原 R405 dot；不复制修改其宽乘法代码。原完整 226 位 significand 乘积、全有限指数跨度、carry、准确正负抵消与末次舍入保持。

prepare 本身也是直接使用原函数。非有限输入在原 decode 阶段报真实错误；没有把它送进 SIMD 或伪装成零。原内存分配失败、格式错误等异常继续是实际失败。快速层数超限和 packing 预算不足则走原准确替代路径，不是数学拒绝条件。

### 推论：完整 row-major matrix API

新 multiply 保持原 $m\times k$ 和 $k\times n$ 尺寸检查，完整准备每个右矩阵列，逐行准备每个左矩阵行，并对全部 $(i,j)$ 调用新 dot。没有只计算部分 stage、部分 224 列、部分 Fourier modes 或 selected rows 的逻辑。

因此，在全部对应调用完成的前提下，新输出的每个字词都与 R405 matrix API 一致。shape、null、size overflow 责任和完整零尺寸返回语义保留。当前头文件只提供这项矩阵能力；它没有独立声称已经形成或运行某个 576-stage 全链。

### 原 deadline 的边界

poll 仍位于原 prepare 和每个 digit block 的相同语义边界。但新程序所需墙钟可以不同，CPU/OS 调度也可不同。若一个实际 deadline 在不同位置触发，不能由上述定理推出两个部分运行留下相同已完成范围。完整结果的等价和预算终止时的覆盖是两件不同责任；后者只能按真实 Actions 输出说明。

## 6. 完整舍入、指数与符号责任没有移交给 SIMD

SIMD 的输出仅是一个严格小于 $2^{51}$ 的 int64 partial，没有做任何 binary128 转换。所有跨 layer 的不同指数和全部 bit 尾继续在 R405 准确整数中重构，最后只做一次 RN113。

特别保留：

- 正规数的完整 113 位、guard、sticky 与 ties-to-even；
- 次正规范围的固定量子 $2^{-16494}$，直接在该量子舍入，不先保留 113 位再二次舍入；
- 最小正规与次正规交界、underflow tie 和 overflow tie；
- 准确抵消按原约定返回正零；
- 准确非零负和若舍入到零，返回负零；
- 原负零输入的记录；
- 全有限产品及 size_t 有界总和的完整宽整数容量，未丢指数尾。

这里的“与 R405 逐词相同”依赖同一 R405 表示与舍入合同；本证明不以新 SIMD 重新替代 R405 第 2–5 节的证明。原格式只支持已声明的 little-endian IEEE binary128/GCC 整数类型，当前源没有扩称所有 C++ ABI 都受支持。

## 7. 运行时选择与编译范围

新头文件只在 GNU x86 编译器分支中编译带函数级 target("avx2") 属性的专用 reducer；其余编译分支保留完整 scalar reducer。AVX2 函数标记 noinline，baseline 调用者没有全局 AVX2 target 需求。

普通程序运行阶段通过 GNU CPU feature detection 初始化并查询 avx2。查询为支持才保存该函数指针；否则保存 scalar 指针。选择使用函数内 static 初始化，使多线程首次访问共享已初始化结果。不是 ifunc 或构造器启动前的调用。[2][3]

这里必须维持真实编译合同：整个翻译单元沿原 baseline 编译选项，不能为这份头文件全局加入 -mavx2 或 -march=native，再称原机器无 AVX2 时能安全 fallback。函数级属性才是限定新增指令的边界。对实际部署平台，CPU/OS 与编译器运行时必须正确报告并支持其所选择的 ISA；本数学证明不证明虚拟化平台的 CPU 报告。

CPU 选择不调用数学函数、不测一组候选矩阵、不跑 fixture，也不改变科学接受门。无 SIMD 支持仍执行所有完整 scalar 项；这是执行方式选择，不是停算或跳过列的理由。必要读回应保存实际 backend、编译器/flags 和新计数，不能仅因源码里有 AVX2 函数就声称该实际 run 使用了它。

官方来源仅支持这里所使用的 intrinsic 和 GNU 编译/运行时接口语义；具体整数界、覆盖、重构等价是本文证明。

## 8. API、计数与资源合同

命名空间为 exact_digit_simd128，提供：

| 入口 | 完整范围 |
|---|---|
| prepare | 直接使用原 R405 prepare；没有新有限字词表示 |
| dot(PackedVector, PackedVector, Stats, Poll) | 原已准备对象；只替换 packed partial，完整 zero/wide 委托原实现 |
| dot(VectorView, VectorView, Stats, Poll) | 原全向量 prepare 后执行新 dot |
| multiply(A,B,m,k,n,Stats,Poll) | 原完整 row-major 矩阵及相同 packing 分配 |
| selected_backend_name / avx2_body_compiled | 分别返回实际运行时选择与是否编译专用 body，二者不能混称 |
| Stats::join | 原所有 R405 计数加新 backend/覆盖计数，用于原线程汇总 |

Stats 继承原字段，新加 scalar/AVX2 digit block 数、完整 octet 数、偶数/奇数乘积数、scalar backend 项数、AVX2 尾项数、直接委托 zero/wide 次数及最大实际 block 长度。计数是运行记录，不是数值通过门。原 per-thread ownership 和末尾 join 方式应继续由完整 caller 负责，不能并发无同步写同一个 Stats 实例。

每个完成的 AVX2 block 在计数上显式区分四个 even 和四个 odd 乘积及 scalar tail；这帮助说明实际方法选择。它不代替源正确性证明，也不要求另一次科学对拍才能继续。原 poll 抛出、内存不足和其他中止要保原真实范围。

新函数只增加固定八个 int64 暂存及少量向量寄存器；原完整 word/digit 存储不增维。运行时 dispatch 一次初始化，以函数指针选择后端。可能的提速来自同一指令处理多个准确整数乘积/和；packing、ExactSum、wide 路径、R402 小矩阵形成、两次三角回代以及整链其他工作仍可能主导成本。本文不给倍数，也不从 instruction 数量推完整 576×224 可以在原预算内完成。

## 9. 对完整 native 后继的明确限制

如果后续独立源接入本头文件，仍须真实重新形成原 R402 的 recorded-literal 矩阵、完整 224 列、全部 576 stage、原 boundary112、endpoint338×112 和独立全 audit。原源、输入、current128 所有权、原 C 方向残差、全部终门和预算不得由这份低层证明代付。

R402 原系数来源保持：实际 binary64-lift 三角表、完整 Gram 索引、名义状态和有限 root 更新记录。不得用理想三角积化和差代换 literal products。小系数的形成误差和乘积重新结合误差不因某个 dot 被正确舍入就消失。

对真实名义三角因子 $\widehat L$，准确实两次代回的对象仍是

$$
(\widehat L\widehat L^\top)^{-1},
$$

除非另有证明，不能替换为 $C^{-1}$。完整实际 $C\,d s-\mathrm{right}$ 仍需按原链保存。SIMD 不改变这些界限，不证明有限分支图是 IEEE 离散映射的导数，也不证明它是真实隐式根的导数。

当前没有改变 request186、190、192，未建立新实际请求；更没有用微基准取代全链科学输出。适当的后继是有独立 source identity 的完整入口及其真实必要读回，而非凭低层证明预填终态。

## 官方接口资料

[1] LLVM/Clang, [avx2intrin.h 公开 intrinsic 定义](https://clang.llvm.org/doxygen/avx2intrin_8h.html)，相关函数为 signed _mm256_mul_epi32、逐 64 位逻辑右移 _mm256_srli_epi64 及 _mm256_add_epi64。这里未复制其源码；只引用所需机器操作语义。

[2] GNU GCC, [x86 Built-in Functions](https://gcc.gnu.org/onlinedocs/gcc/x86-Built-in-Functions.html)，__builtin_cpu_init 与 __builtin_cpu_supports，并明确运行时 feature detection 应保 baseline 编译。

[3] GNU GCC, [x86 Attributes](https://gcc.gnu.org/onlinedocs/gcc/x86-Attributes.html)，函数级 target("avx2") 属性。
