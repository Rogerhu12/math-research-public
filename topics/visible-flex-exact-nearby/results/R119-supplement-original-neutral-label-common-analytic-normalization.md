# R119 续篇：原中性层标签的准确公共角宽与有限幂物理规范

2026-11-14，visible-exact-astra-ac0d。

**状态：完整恒等式及界已证明。** 本文只使用原来的内部标签、
\(\zeta_j\)、\(\tau_j\)、两行 canonical 状态和中性层定义；
没有为新的谱估计另选标签或重置源空间。
给出所有物理四重频率 \(M=|m|\ge M_*\) 的同一解析宽度
\(\tau_\infty\)，以及保留真实全局常数的有限幂上下界。
这解决的是原标签与其真实取值层的物理规范，尚不是全 Green
核、任意物理源或完整非径向逆的估计。

## 1. 原定义、适用对象与固定标签

采用[强首剪切局部图](R119-supplement-stronger-deep-first-shear-and-complete-local-map.md)
和[强全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
的准确定义：
\[
 \delta_j=\frac2{25}2^{-j},\quad
 h_j=8\delta_j^{1/256}\ (j>4096),\quad
 \tau_{128}=\frac{5177}{400},\quad
 \tau_j-\tau_{j-1}=h_j,
\]
其中 \(h_j=9/100\) 当 \(129\le j\le4096\)。
深段的原权是
\[
 C_\zeta=\epsilon\delta_{8192}^{-485/4},\qquad
 \zeta_j=C_\zeta\delta_j^{131}\quad(j>8192).           \tag{N.1}
\]
常数 \(C_\zeta\) 不能删去或改成1。原两行状态为
\[
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{M\tau_j}V_{m,j}.        \tag{N.2}
\]

令 \(n_0(m)\) 为第一次 \(M\le\widehat M_j\) 的层；
深层 \(\widehat M_j=2^{-40}\delta_j^{-1/8}\)。
原定义中的 \(j_m\) 是从 \(n_0\) 起第一次
\(a_{m,j}\ge1\) 的层，\(b_m=j_m-1\)，其中
\[
 a_{m,j}=D_Me^{-Mh_j},\qquad
 D_M=2^{-131}\Lambda_{M,\mathsf K,C},\quad
 \mathsf K=2^{128},\ C=16\sqrt2,\ \alpha_s=65/64,
 \quad \nu_M=M^2(M^2-1)/12.                          \tag{N.3}
\]
这里 \(\alpha_s\) 是首剪切常数，不是主体振幅参数。
原标签准确是
\[
 a_m^{\rm lab}=\ell_m(X)
       =(E_M(b_m)^{-1}X_{m,b_m})_1.                  \tag{N.4}
\]
[第53束受控全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
保持这些低窗、内部标签、接缝和权。因此下述恒等式同样适用于
当前受控实际尾图；没有随 \(\Gamma\)、profile 或未知 \(X\)
重新移动取值层。

深低窗的第一个阈值准确为
\[
 M_*=2^{-40}\delta_{8193}^{-1/8}
     =2^{984}25^{1/8}>2^{984}>1024.                  \tag{N.5}
\]
它不是整数，故物理频率 \(M\in4\mathbb N\)、\(M\ge M_*\)
实际满足 \(M>M_*\)，从而 \(n_0>8193\)。

## 2. 真实中性层：只损一个固定的几何步长

原谱根界给
\[
 (\mathsf K-1)\alpha_s\nu_M<\Lambda_M
                 <(\mathsf K+1/16)\alpha_s\nu_M.
\]
对 \(M\ge4\)，\(1-M^{-2}\ge15/16\)；直接有理比较得
\[
            \frac{M^4}{128}<D_M<\frac{M^4}{64}.      \tag{N.6}
\]
特别地 \(q_M:=\log D_M\) 在本篇范围满足
\[
                    2\log M<q_M<4\log M.            \tag{N.7}
\]

第一次进入低窗的定义和 \(\delta_{j-1}=2\delta_j\) 给
\[
 2^{-321}M^{-8}<\delta_{n_0}\le2^{-320}M^{-8}.        \tag{N.8}
\]
于是
\[
 Mh_{n_0}>2^{447/256}M^{31/32}>2M^{31/32}>4\log M.
\]
最后一步对 \(M\ge1024\) 成立：先用 \(M^{31/32}\ge\sqrt M\)，
在1024处 \(2\sqrt M=64>4\log1024\)，以后
\(\sqrt M/\log M\) 递增。因此 \(a_{m,n_0}<1\)，
真正中性穿越在 \(n_0\) 之后发生，\(b_m\ge n_0>8193\)。

置
\[
 \kappa=2^{1/256},\qquad A=\frac1{\kappa-1},\qquad
 u_M=Mh_{b_m}.
\]
原定义 \(a_{m,b_m}<1\)、\(a_{m,b_m+1}\ge1\) 准确等价于
\[
                       q_M<u_M\le\kappa q_M.        \tag{N.9}
\]
等号方向不能随意交换；它保留可能恰好落在中性层上的情况。
这里不需要数值枚举巨大层号。

两个有限整数不等式
\[
 257^{256}>2\cdot256^{256},\qquad
 513^{256}<2\cdot512^{256}
\]
给出
\[
              256<A<512,\qquad A\kappa=A+1<513.     \tag{N.10}
\]
这也可直接由二项式展开证明。

## 3. 所有频率共同的准确物理解析宽度

原角宽的完整和为
\[
 \tau_\infty
 =\frac{5177}{400}+3968\frac9{100}
      +\frac{h_{4097}}{1-2^{-1/256}}
 =\frac{5921}{16}+(A+1)h_{4097}.                    \tag{N.11}
\]
有 \(h_{4097}=2^{-13}25^{-1/256}\)。
由 \(513^{256}<25\cdot512^{256}\) 及 (N.10)，得到
\[
                   \frac{5921}{16}<\tau_\infty
                                      <\frac{2961}{8}. \tag{N.12}
\]
这是370.0625与370.125之间的同一个常数，并非随 \(M\) 的宽度。

对每个真正标签层 \(b=b_m\)，完整未来几何级数准确给
\[
                   \tau_\infty-\tau_b=Ah_b.         \tag{N.13}
\]
定义原 canonical 物理状态的标量泛函
\[
 z_m=(E_M(b_m)^{-1}V_{m,b_m})_1,\qquad
 N_M=\zeta_{b_m}e^{-M\tau_{b_m}}.
\]
由 (N.2)、(N.4) 得完整恒等式
\[
 z_m=(-1)^{b_m}N_M a_m^{\rm lab},                    \tag{N.14}
\]
而 (N.1)、(N.13) 和 \(\delta_b=(h_b/8)^{256}\) 给
\[
 \boxed{
 N_M=C_\zeta e^{-\tau_\infty M}
       \left(\frac{u_M}{8M}\right)^{33536}e^{Au_M}.
 }                                                   \tag{N.15}
\]
符号、原全局 \(C_\zeta\)、指数33536和实际层号均保留。

令 \(p=33536\)。由 (N.9)，有更精确的双侧比较
\[
 \left(\frac{q_M}{8M}\right)^pe^{Aq_M}
 <
 \frac{e^{\tau_\infty M}N_M}{C_\zeta}
 \le
 \left(\frac{\kappa q_M}{8M}\right)^pe^{A\kappa q_M}. \tag{N.16}
\]
右端与左端的比准确为
\[
                \kappa^p e^{A(\kappa-1)q_M}
                            =2^{131}D_M.            \tag{N.17}
\]
所以跨过中性层的离散取整没有引入新的指数角宽损失。

## 4. 显式有限幂界及对应的标签范数

这里给无需对数权的较宽整数幂界，以便直接消费。
由 (N.7)、\(A>256\)、\(q_M/8>1\)，有
\[
 \left(\frac{u_M}{8M}\right)^pe^{Au_M}
                              >M^{-33536+512}
                              =M^{-33024}.          \tag{N.18}
\]
另一方面，\(\kappa<2\)、(N.7)、\(A\kappa<513\) 给
\[
 \left(\frac{u_M}{8M}\right)^pe^{Au_M}
             <M^{-33536+2052}(\log M)^{33536}.        \tag{N.19}
\]
置 \(x=\log M\)。由 (N.5)、\(\log2>1/2\)，\(x>492\)。
对 \(x\ge492\)，
\[
 \log x<x/64.
\]
证明是在左端用
\(\log492<\log512=9\log2<27/4<492/64\)，
随后用 \(1/x<1/64\)。其中 \(\log2<3/4\) 来自
\(1+3/4+(3/4)^2/2+(3/4)^3/6=269/128>2\)；
\(\log2>1/2\) 可由指数级数与严格几何级数比较得到。
因此
\((\log M)^{33536}<M^{524}\)，最终
\[
 \boxed{
 C_\zeta e^{-\tau_\infty M}M^{-33024}
       <N_M<
 C_\zeta e^{-\tau_\infty M}M^{-30960}.
 }                                                   \tag{N.20}
\]

为准确说明范数含义，只在 \(M\ge M_*\) 的原标签泛函上定义
\[
 \|z\|_{\sigma,s}
   =\sum_{\substack{m\in4\mathbb Z\setminus\{0\}\\|m|\ge M_*}}
             e^{\sigma|m|}|m|^s|z_m|.
\]
则对任意原标签权 \(\beta\)，(N.14)、(N.20) 给
\[
 \|z\|_{\beta+\tau_\infty,30960}
       \le C_\zeta\|a^{\rm lab}_{\ge M_*}\|_{\ell^1_\beta}
       \le \|z\|_{\beta+\tau_\infty,33024}.            \tag{N.21}
\]
对非零且相关和有限的序列，两端不等式严格。
这陈述的是同一实际标签泛函的规范夹逼，绝不把一条泛函
当成两行状态的完整范数。原 \(\|E^{-1}\|_\infty<17/16<2\)
只另给 \(|V_{m,b_m}|_\infty>N_M|a_m^{\rm lab}|/2\)
（非零标签时）；未从这条不等式反推整个状态的上界。

## 5. 明确保留的全部后续费用

(N.14)--(N.21) 对真实解、非线性标签图或其固定标签变分都只是
准确的取值层换算；另一条 canonical 行、mean 小根、
独立高度及 ordinary/weak 源单位仍由原完整方程决定。
在未单独估计前，不能将源项的标签泛函套用为其完整状态范数。

本篇没有：

- 将 \(M<M_*\) 的巨大但有限频段删去或免费授予统一常数；
- 连接不同径向端口的全 Green 核与完整 relative Jacobi 源；
- 将已选径向 middle 的双侧谱权直接改成原 \(\mathcal X_\beta\) 同宽逆；
- 证明更新后非径向网络的可逆性或最终 \(\mathcal F=0\)。

它确实消除了一个明确的障碍：原标签层随 \(M\) 移动，
但其真实物理规范中的指数角宽准确是同一个 \(\tau_\infty\)，
剩余变化全部可用显式有限幂支付，原 \(C_\zeta\) 没有消失。

配套脚本 \(\texttt{fourfold\_original\_neutral\_label\_normalization.mjs}\)
保存上述整数/有理门与依赖源SHA，实际运行报告位于
\(\texttt{2026-11-14-R119-original-neutral-label-normalization-rational.json}\)。
全频结论来自上述解析证明；有限整数门没有代替中性层、
几何级数或无限范数的推导。
