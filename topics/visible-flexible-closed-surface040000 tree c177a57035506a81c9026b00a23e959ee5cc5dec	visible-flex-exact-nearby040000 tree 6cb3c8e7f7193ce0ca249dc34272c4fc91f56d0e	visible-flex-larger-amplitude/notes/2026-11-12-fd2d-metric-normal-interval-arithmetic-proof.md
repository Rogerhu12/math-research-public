# 连续 metric 消费的 normal-range 区间运算

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

本文只证明一个**包围实现**的改变；实际曲面、材料字段、目标度量及全部非零 Fourier 模均不改变。
实现为 `scripts/fd2d-metric-normal-interval-arithmetic.py`，通过 `install(poly, narrow_owner=None)`
安装到原 `78718-prefix-metric-polynomial-storage-v1.py` 的矩阵乘/卷积接口。
若使用已经定义的窄 Fourier 因子 Toeplitz 实现，传入该 consumer 模块为 `narrow_owner`，
其径向 Toeplitz 公式不变，只有内部矩阵乘和宽因子 fallback 使用本文包围。

## 1. 已观察到的实际瓶颈

对同一实际 prefix 字段的一个完整连续区间调用，真实 profile 给总耗时约 4.47 秒；
其中 145 次区间矩阵乘累计约 3.93 秒，`up`/`down` 的 `nextafter` 调用约 1.6 秒。
这不表示数学上需要删去高模或重新拟合字段。
旧通用实现会把准确零的半径通过 `up(0)` 变成最小正 subnormal，随后在大量稀疏矩阵乘中传播。
本实现使用保守区间膨胀，使这些批量计算远离这条慢路径。
不改变浮点 rounding mode，也没有打开 FTZ 或把非零数偷偷当成零。

## 2. 输入区间的保守替换

置准确二进常数 $\varepsilon=2^{-400}$。
对一个非零输入区间 $[\ell,h]\subset(-\varepsilon,\varepsilon)$，用
$[-\varepsilon,\varepsilon]$ 替换；准确零区间 $[0,0]$ 则原样保留。
这一步显然包含原输入的全部可能值。
它不是 Fourier 模截断：任何被包围的真实系数仍在同一个频率位置上。

随后按原实现计算浮点中心
$c=\operatorname{fl}(\ell/2+h/2)$，半径取

$$r=\operatorname{up}\!\left(\max\{\operatorname{fl}(c-\ell),
\operatorname{fl}(h-c)\}\right).$$

当 max 准确读作零时，改为保留 $r=0$。
这是合法的：此时三个二进数 $\ell,h,c$ 相等；两个不同有限二进数的非零差
至少是最小 subnormal 的整数倍，不会把上述两个差都舍成零。
因此此分支中准确所需的半径确实为零。
其它分支仍作一次向上取整，所以始终有 $[\ell,h]\subset[c-r,c+r]$。

## 3. 矩阵乘的完整误差包围

写输入矩阵为

$$A=A_c+\Delta A,\quad B=B_c+\Delta B,
\qquad |\Delta A|\le A_r,\quad |\Delta B|\le B_r.$$

则逐项有

$$|AB-A_cB_c|
\le |A_c|B_r+A_r|B_c|+A_rB_r.\tag{1}$$

继承原后端的 double dot-product 模型与保守预算：内维为 $k$ 时取
$n=2k+2$、$u=2^{-52}$、$\gamma_n=nu/(1-nu)$，并在运行时检查 $nu<1$。
原 underflow 计费为向上包围的 $n$ 倍最小正 subnormal。
本实现把它**提高**到

$$\eta=\max\{\varepsilon,\operatorname{up}(n\,2^{-1074})\}.$$

所以原任意求和顺序/正确舍入 FMA 的舍入证明仍成立，且允许更大的正误差预算。
具体而言，每个被求和项经历的有限舍入因子满足
$(1+u)^n-1\le nu/(1-nu)$，这给上述 $\gamma_n$；逐项绝对值和支付抵消造成的误差放大。
即使把每次 underflow 的绝对误差沿后续乘加传播也单独计入，
由于 $n$ 为整数、$n<2^{52}$ 且 $1-nu\ge2^{-52}$，有
$n2^{-1074}/(1-nu)<2^{-970}<\varepsilon$。
因此这里较大的 $\eta$ 也足以支付这一更保守的绝对 underflow 计费。
对非负矩阵 $U,V$，向上包围

$$P(U,V)=\operatorname{up}
 \left(\frac{\operatorname{up}(\operatorname{fl}(UV)+\eta)}
 {\operatorname{down}(1-\gamma_n)}\right)\tag{2}$$

满足 $UV\le P(U,V)$。
令 $C=\operatorname{fl}(A_cB_c)$、$M=P(|A_c|,|B_c|)$，并把下式全部加法/乘法向上包围：

$$R=P(|A_c|,B_r)+P(A_r,|B_c|)+P(A_r,B_r)+\gamma_nM+\eta.\tag{3}$$

由 (1)、(2) 与 dot-product 舍入界，得到

$$AB\in[\operatorname{down}(C-R),\operatorname{up}(C+R)].\tag{4}$$

这正是新 `matmul` 的实现。
原实现、窄因子 Toeplitz 实现和本实现都包围真实乘积；不要求它们的浮点输出逐位相同。
准确零半径的合法保留可能去掉旧实现人为添加的宽度，但没有去掉真实误差。

## 4. 二维有限多项式卷积

对径向系数阶数分别为 $n_a,n_b$、Fourier 数目分别为 $m_a,m_b$ 的数组，
仍取原 mixed-radix stride $m_a+m_b-1$，补准确零后展平成一维数组。
这样每个真实二维卷积系数拥有唯一一维索引，没有角频率混叠。
单个输出使用的乘加项数至多两个展平长度的较小值；取
$n=2\min(N_a,N_b)+2$ 的同一 $\gamma_n,\eta$ 即可重复 §3 的证明。
丢弃的仅是原布局末尾没有对应二维系数的补零 suffix，原数学卷积范围完全保留。

最终 consumers 仍直接处理所有实际字段 Fourier 模、所有实际径向盒和完整角弧。
若通过更换包围后端继续一份分区证书，只能复用已有明确 exact endpoint 及输入身份的有效盒；
新 consumer 必须核对整个相同的径向分区，不能凭已完成盒数量跳过未知范围。

## 5. 与当前结果的关系

该模块的源码 SHA 和准确 $\varepsilon$ 会进入实际消费者报告。
这是一项可重复的运算改进，本身不证明本题达到 $2\cdot10^{-9}$。
成功仍以 actual field 的完整连续 linear residual 报告及 R112 精确非线性后验为准。
