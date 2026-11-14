# R75. 固定周期空间上的两类临界原函数

日期：2026-11-12。**状态：固定对象、准确 prime coefficient、闭形式检验与非 D-finite 性已证明；无穷非零仍开。**

## 1. 两个不随素数变化的准确接口

令 $\mathcal B_1(u)=K M_1=\sum C_nu^n$、$u=L/K$，
$du/dt=1/(sK^2)$、$s=1-4t^2$。定义固定原函数
$$
\mathcal H_i(u)=\int_0^u\mathcal B_1(v)v^{-2}\,dv,
\qquad
\mathcal E(u)=\int_0^u\mathcal B_1(v)\,dv,
\qquad
\mathcal H_o(u)=\int_0^u\mathcal E(v)v^{-1}\,dv.
$$
完整尺度给
$$
\boxed{[u^p]\mathcal H_i=C_{p+1}/p,\qquad
[u^p]\mathcal H_o=C_{p-1}/p^2.}
\tag{1}
$$
两边分别是 R66 的惰性和普通首层充分判据。对应 $t$ 方程为
$$
\mathcal H_i'=M_1K/(sL^2),\quad
\mathcal E'=M_1/(sK),\quad
\mathcal H_o'=\mathcal E/(sKL).
\tag{2}
$$
另有 Euler 原函数 $\mathcal H_e'=M_1/(sL)$。
这些是变化素数前固定的对象，不能将它们与 R68 依赖 $p$ 的整代表混同。

## 2. 实际周期域是明确的代数环境

在使 $M_1$ 单值的任何固定代数覆盖 $k/\mathbb C(t)$ 上，取
$$
X:\ KR-LQ=1/s,
$$
以及 GM 向量场
$\delta t=1,\delta K=Q,\delta L=R,
\delta Q=(K+8tQ)/s,\delta R=(L+8tR)/s$。
实际代入 $Q=K',R=L'$ 的函数域同态为单射。

证明直接使用两个 Legendre cusp 的非平凡 unipotent monodromy：
其固定线不同，任意固定有限覆盖上的适当整数幂仍生成 Zariski 稠密的
$\operatorname{SL}_2$。在一般基点沿这些闭路延拓，任意周期多项式关系
必须在整个行列式 torsor 上成立。因此没有隐藏的额外代数关系。
式 (2) 是这个固定空间上的有理偏连接，尚不是基底上的有限秩平坦连接。

## 3. 准确留数排除直接的闭 Kummer 替换

沿 $D:L=0$，$\delta L=1/(sK)$ 是单位。
$M_1/(sL)$ 的简单留数是 $M_1K$。
对惰性双极项先减
$\delta(-M_1K^2/L)$，留下的简单留数为
$$
sK^2(M_1'K+M_1Q).
\tag{3}
$$
普通第一原函数沿 $K=0$ 的留数为 $-M_1L$。
它们在相应一般除子上都非恒定。

闭有理一形式沿一个光滑除子的极部只能是
$dq+c\,dL/L$，其中 $c\in\mathbb C$；逐项 Laurent 积分和闭性直接证明此式。
由于 $\delta$ 横截该除子，匹配最高极项后，收缩的简单留数必须为常数。
这与 (3) 等矛盾。因此三个右端都不是某个闭有理一形式对 $\delta$ 的收缩。
有限代数扩张中的 exact 加常系数有限 dlog 表达，也由 trace/norm 降回后排除。

## 4. 整条序列不满足固定有限阶线性方程

取不保持 $L$ 线的 cusp unipotent 的各整数幂，得到两两不同的线性形式 $L_n$。
上述两个右端的延拓分支分别沿不同的素除子 $L_n=0$ 有真实简单或双极点，
故在 $k$ 上线性独立。有限阶线性微分方程的局部解空间有限维，产生矛盾。
同理沿 $K_n=0$ 处理 $\mathcal E'$。

所以 $\mathcal H_i,\mathcal H_e,\mathcal E$ 均非 D-finite。
若 $\mathcal H_o$ 是 D-finite，则
$\mathcal E=sKL\mathcal H_o'$ 也会是 D-finite，因为 $K,L$ 本身满足二阶 PF 方程、
D-finite 函数对有限乘积封闭；再次矛盾。

这不排除 (1) 的指定 prime diagonal 另有有限比较，也不排除带 GM 系数的
更高相对对象。下一步仍须为完整中央条件建立这个实际偏连接的额外算术约束。
全文、monodromy 及 Laurent 证明见
[固定周期空间上的临界原函数](../notes/2026-11-12-fixed-period-torsor-primitives-and-residues.md)。
