# 同一 phase 图的全径向角原函数尾界

状态：**已给覆盖全径向区间的解析截断/混叠预算及向外运算程序；
尚未给三角采样和实际 FFT 的舍入预算，亦非等距存在性证明。**

输入固定为 `phase_ring_continuation/type_fixed_step02.npz`，SHA256
`05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`。
此前仅在五个径向点计算的角尾预算不能当作全区间界；这里将相位、
背景权与实际周长半径的全部径向 knot 合并成1396个单元，覆盖 $[0,3]$。
每一单元使用 B-spline 控制系数凸包和精确乘积公式，不用径向抽样
代替上界。普通样本仅作输入/索引的附加核查。

## 1. 被比较的两个对象

把保存的二进制浮点 spline 系数与 knot **解释成精确实数**，由它们
定义有限相位 $\beta(x,\theta),\gamma(x,\theta)$ 及周长半径 $a(x)$。
用R33的精确三角公式定义无限角 Fourier 的单位切向量 $T$，并设

$$
F_\infty=aP_\theta T+Ze_z.
$$

另在每个 $x$ 对精确 $T$、$T_x$、$T_{xx}$ 样本作**数学上的精确 DFT**，
保留 Cartesian $0<|n|\le509$ 的零均值原函数，得到 $F_{\rm DFT}$。
Q256四分之一圈与全圈N1024在这个cut下相同：最高水平频率509，
最高竖直频率508，被丢掉的四分之一圈Nyquist全部在cut外。
固定Cartesian平均为零由四重与奇对称精确成立。

本记录给的是 $F_\infty-F_{\rm DFT}$ 的误差。
实际浮点代码求三角样本和FFT时的误差还要另加；这里没有把它们
冒充精确DFT。$Z$ 在两对象中相同，因此角原函数差中不出现高度项。

## 2. 径向单元凸包

设 $s=\sum_i c_iB_{i,k}$。在一个没有内部knot的单元上，非负基函数
和为1，因此

$$
|s(x)|\le\max_{i\text{ active}}|c_i|.
$$

导数控制系数为

$$
c_i^{(1)}=\frac{k(c_{i+1}-c_i)}{t_{i+k+1}-t_{i+1}},
$$

递归即可界每阶导数。相位 raw spline 的负侧**控制系数**由保存的
正侧系数按偶/奇符号复制；它使用实际保存/物化的全部二进制 knots。
这些 knots 的反射有约1.8e-15的浮点缺陷，背景/mean的控制系数也有
约1e-15的偶性缺陷，所以不能把整个实数 spline 的径向偶/奇性
自动当成精确恒等式。本记录直接计算每个正侧单元的凸包，
不依赖这种径向反射，亦不从正侧界推断负侧界。
$\beta_j=a_{\rm ref}^3b_j$、
$\gamma_j=a_{\rm ref}^2c_j$。若单元上
$|a_{\rm ref}^{(r)}|\le A_r$、$|b_j^{(r)}|\le B_{jr}$，则对$p=3$或2，

$$
\begin{aligned}
|a_{\rm ref}^pb_j|&\le A_0^pB_{j0},\\
|(a_{\rm ref}^pb_j)'|&\le A_0^pB_{j1}+pA_0^{p-1}A_1B_{j0},\\
|(a_{\rm ref}^pb_j)''|&\le A_0^pB_{j2}+2pA_0^{p-1}A_1B_{j1}\\
&\quad+[p(p-1)A_0^{p-2}A_1^2+pA_0^{p-1}A_2]B_{j0}.
\end{aligned}
$$

实际 $a$ 含三个真实 mean 以及保存的 `radius_shift`；它的三阶数
0/1/2上界分别从这些同一 spline 的凸包相加得到。没有拿背景半径
代替实际周长半径。

## 3. 角strip与Fourier预算

对每个单元，以相位系数上界乘 $\cosh(4j\sigma)$ 求和，得到
$B,P,B_x,P_x,B_{xx},P_{xx}$。令

$$
E=e^P,\qquad H=2e^{\sigma+B}.
$$

R33的实际 Cartesian 公式在 $|\operatorname{Im}\theta|\le\sigma$ 上给
向量分量绝对值和的上界

$$
\begin{aligned}
M_0&=E(H+1),\\
M_1&=EH B_x+M_0P_x,\\
M_2&=EH(B_{xx}+2B_xP_x)
       +M_0(P_{xx}+2E^2B_x^2+P_x^2).
\end{aligned}
$$

这些量支配相应Euclidean范数。对任一 strip 范数不超过$M$的向量场，
Fourier系数满足 $|\widehat T_n|\le M e^{-\sigma|n|}$。
取$q=e^{-\sigma}$、cut $K=509$、样本数$N=1024$，原函数及两阶角导数
的截断项依次不超过

$$
2M q^{K+1}\left(
\frac1{(K+1)(1-q)},\quad\frac1{1-q},\quad
\frac{K+1}{1-q}+\frac{q}{(1-q)^2}\right).
$$

保留频率$n$的混叠误差系数以
$4M e^{-\sigma(N-n)}/(1-e^{-\sigma N})$ 同时支付正负频率；
乘$n^{-1},1,n$后对$1\le n\le K$求和。程序使用有限几何级数和
带权有限和计算，不以双倍FFT的样本差代替此尾界。

若三种径向原函数预算分别为$e_{T,r}$、$e_{T_x,r}$、
$e_{T_{xx},r}$（$r$为角导数阶），实际半径上界为$A_0,A_1,A_2$，则

$$
\begin{aligned}
e_F&=A_0e_{T,0},&
e_{F_x}&=A_1e_{T,0}+A_0e_{T_x,0},\\
e_{F_\theta}&=A_0e_{T,1},&
e_{F_{xx}}&=A_2e_{T,0}+2A_1e_{T_x,0}+A_0e_{T_{xx},0},\\
e_{F_{x\theta}}&=A_1e_{T,1}+A_0e_{T_x,1},&
e_{F_{\theta\theta}}&=A_0e_{T,2}.
\end{aligned}
$$

每个单元可独立选择$\sigma$，因为所有选择都界同一个DFT cut与同一个
无限函数。程序从81个候选strip中选择，最后用向外算术重算选中界；
选择过程的普通浮点读数不参与最终上界的合法性。

## 4. 基本舍入与指数核

基本$+,-,\times,\div$采用IEEE binary64正确舍入运算，并把每一边界
用`nextafter`向外扩一步。导数控制系数的分子、正分母及商均如此处理。
实际指数没有使用库函数`exp`作为证书端点：
`fourfold_interval_scalar.py`把精确二进制参数减半到$0\le y\le1/8$，
用Python任意精度整数有理数精确计算

$$
S_{24}=\sum_{j=0}^{24}\frac{y^j}{j!},\qquad
0\le e^y-S_{24}\le
\frac{y^{25}}{25!}\frac1{1-y/26}.
$$

后一式由后续相邻项比不超过$y/26$直接得到。精确有理端点转换到
binary64后再作有理比较，必要时向外移动；随后向外平方恢复原参数，
负参数用正区间的倒数。这样指数余项和边界舍入均有明确机制。
14个跨正负、小量和大参数的100位Decimal比较通过，但这些比较
只是核实现的核查；上述Taylor余项是合法性的依据。

## 5. 全区间结果及重做入口

向上取整后的全$[0,3]\times S^1$预算如下：

| Jet | 全径向解析截断+混叠上界 |
| --- | ---: |
| $F$ | $4.426\times10^{-16}$ |
| $F_x$ | $8.474\times10^{-14}$ |
| $F_\theta$ | $2.224\times10^{-13}$ |
| $F_{xx}$ | $4.293\times10^{-11}$ |
| $F_{x\theta}$ | $4.258\times10^{-11}$ |
| $F_{\theta\theta}$ | $1.130\times10^{-10}$ |

六个最大值都出现在径向单元$[.015,.01584809074049698]$，所用
$\sigma=.0815$。因此角原函数的解析表示误差不是当前约$10^{-4}$
metric误差或不同角cut间大$C^2$变化的主要来源。
这不豁免浮点三角/FFT误差，也不提供PDE右逆、闭帽或Newton收敛。

冻结输入是
`data/phase_ring_continuation/type_fixed_step02_uniform_tail_inputs.npz`，
331704字节，SHA256
`41d305d88844ff1548e1b1e45aebe423c134c366c7950de7c36eb8a05973fba9`。
它含这次实际构造的phase/base/mean/radius_shift系数与knots；之后可
完全绕开背景ODE和重新拟合，从同一实数对象重做预算。
完整报告为同目录 `type_fixed_step02_uniform_tail.json`。

求值脚本SHA256：
`d7010fcd486cfe703eab58d0d5ad4e78a193418b7bc6c71f25e308c523b55c61`；
有理指数区间核SHA256：
`0400c59be86f7f143481f89d5a08ca8d0ea992be36aa1687ff9a19d10343dda8`。

```bash
mkdir -p /tmp/visible-exact-tail
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_uniform_tail.py \
  topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02.npz \
  --angles 256 \
  --from-snapshot topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_uniform_tail_inputs.npz \
  --snapshot /tmp/visible-exact-tail/inputs.npz \
  --out /tmp/visible-exact-tail/report.json
```

不加`--from-snapshot`可重新物化当前求值器输入；但若未来背景生成
依赖或求值器改变，那个新对象必须单独标识，不能沿用本文件的哈希。
