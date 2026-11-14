# 全次数分拆的 Johnson 恒等式与 Turán 算术延拓的实际障碍

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：以下条件谱恒等式、保全部 nuisance 的全局算术缺陷表示、等权反例和方法费用下界已证明。** 它们不反驳真正相邻或加强 S1；也没有证明原连续尾高出生的统一常数。这里排除的是把 R295 的线性协方差算术步骤直接复制到高次数残差的路线。

## 1. 使用 R296 的同一个完整回归源

取 $M$ 个正权 $b_i$，$z_i=b_i^2$。固定 $s\ge1$、$h=M-2s\ge1$、$1\le n\le h$，置 $k=s+n$。所有 $e_j=e_j(z)$。对同一物理源 $f\in K_s(d)$，沿用 R296

$$
\Phi(I)=\sum_{\substack{J\subset I\\|J|=s}}\frac{f_J}{b_J},
\qquad q_j=\Pi_{\le s-1}^{(j)}\Phi,
\qquad \mathcal R_{j,s}f=\Phi-q_j.
\tag{1.1}
$$

每个 $q_j$ 使用其唯一齐次 $(s-1)$ 次代表；常数及全部更低次数都已吸收在该代表中，不能删除。令

$$
p=\Phi-q_k,\qquad g=q_k-q_{k-1},
$$
$$
\ell=\Pi_{\le s-2}^{(k+1)}(p-g),
\qquad \ell=0\quad(s=1).
\tag{1.2}
$$

$\ell$ 也取唯一齐次 $(s-2)$ 次代表。于是准确有

$$
p+g=\mathcal R_{k-1,s}f\quad\hbox{于第 }k-1\hbox{ 切片},
$$
$$
p-g-\ell=\mathsf Z_n f\quad\hbox{于第 }k+1\hbox{ 切片}.
\tag{1.3}
$$

第二式就是 R296 的共同二阶拟合差公式，不在不同切片之间偷偷更换代表。特别 $\deg p\le s$、$\deg g\le s-1$、$\deg\ell\le s-2$，并且 $p$ 与 $p+g$ 在各自切片均值为零。

记 $C_j=\Gamma_{j,s}^{-1}$，硬端 $C_{h+1}=0$；低出生 Gram 为 $L_j=\Gamma_{j,s-1}$。R296 给出

$$
\|p\|_k^2=\langle C_nf,f\rangle,
\quad \|p+g\|_{k-1}^2=\langle C_{n-1}f,f\rangle,
$$
$$
\|p-g-\ell\|_{k+1}^2
=\langle(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*)f,f\rangle.
\tag{1.4}
$$

范数均为未归一乘积权范数 $\|F\|_j^2=\sum_{|I|=j}z_I|F(I)|^2$。

## 2. 每个交集／对称差中的完整 Johnson 展开

固定不交集合 $A,D$，其中

$$
|A|=k-r,\quad |D|=2r,
\qquad 0\le r\le\min(k,M-k).
$$

一个等秩对子可唯一写成
$I=A\cup X$、$J=A\cup(D\setminus X)$、$|X|=r$。
相邻秩对子使用相同表达而 $|X|=r-1$。两者的单项乘积权都是
$z_A^2z_D$，所以条件分拆在其对应均匀切片上严格均匀；这里没有忽略外场权。

先设 $r\ge1$，$N=2r$。对任意局部多线性多项式 $a(X)$，将其齐次系数写为 $a_\nu\in\mathcal H_\nu(D)$，$0\le\nu\le N$。设

$$
\partial_D=\sum_{i\in D}E_i,\qquad
U_D=\partial_D^*,\qquad
\mathcal K_j(D)=\ker\partial_D\cap\mathcal H_j(D).
$$

无权完整 Boolean 分解唯一给出

$$
a_\nu=
\sum_{0\le j\le\min(\nu,N-\nu)}
\frac{U_D^{\nu-j}}{(\nu-j)!}\,a_{j,\nu},
\qquad a_{j,\nu}\in\mathcal K_j(D).
\tag{2.1}
$$

例如可以完全按物理层构造

$$
a_{j,\nu}=
\frac{P_{\mathcal K_j(D)}\partial_D^{\nu-j}a_\nu}
{(N-2j)_{\underline{\nu-j}}},
\tag{2.2}
$$

分母为合法降阶阶乘，空幂为一。其他出生在投影后消失，所以 (2.2) 保完整层，不是先对某个局部试探源求逆。

定义取值于同一 $\mathcal K_j(D)$ 的系数多项式

$$
H_j^a(m)=\sum_{\nu=j}^{\min(\deg a,N-j)}
\binom{m-j}{\nu-j}a_{j,\nu}.
\tag{2.3}
$$

在 $|X|=m$ 上，逐单项式计数给

$$
a(X)=\sum_{j=0}^{\min(m,N-m)}
\Phi_{j,H_j^a(m)}(X),
\qquad
\Phi_{j,u}(X)=\sum_{\substack{J\subset X\\|J|=j}}u_J.
\tag{2.4}
$$

不同 $j$ 的项相互正交，并且

$$
\sum_{|X|=m}|\Phi_{j,u}(X)|^2
=\binom{N-2j}{m-j}\|u\|^2.
\tag{2.5}
$$

证明 (2.5) 只需将 $U_D^{m-j}/(m-j)!$ 的平方范数限制到 $\mathcal K_j(D)$；$\partial_DU_D^a u=a(N-2j-a+1)U_D^{a-1}u$ 给出所列二项式。正交性来自不同无权 primitive 塔在同一物理层正交。

还严格有

$$
\Phi_{j,u}(D\setminus X)=(-1)^j\Phi_{j,u}(X).
\tag{2.6}
$$

因为 harmonic 齐次多项式满足 $\sum_i\partial_i\Phi_{j,u}=0$，故沿全一方向平移不变，再代入 $1-X$ 即得 (2.6)。

以上公式同样适用于向量值或算子值系数，使用相应内积或 Gram；没有只证明逐向量标量后误取矩阵平方。

## 3. 同一个真实回归源的条件正、负通道

将 (1.2) 的三个多项式限制到 $A\cup X$，分别记为 $p_A,g_A,\ell_A$，并按 (2.3) 取其 $H_j^p,H_j^g,H_j^\ell$。这些系数都取自同一个 $A,D$；下式不把局部 harmonic 源误认为原全局 primitive 源。

等秩对子使用统计量 $p(I)+p(J)$；相邻对子使用
$(p+g)(I_-)+(p-g-\ell)(I_+)$。它们的完整条件系数是

$$
S_j^0=(1+(-1)^j)H_j^p(r),
\tag{3.1}
$$
$$
\begin{aligned}
S_j^-={}&H_j^p(r-1)+(-1)^jH_j^p(r+1)\\
&+H_j^g(r-1)-(-1)^jH_j^g(r+1)
-(-1)^jH_j^\ell(r+1).
\end{aligned}
\tag{3.2}
$$

令

$$
c_{r,j}=\binom{2r-2j}{r-j},\qquad
\tau_{r,j}=\frac{r-j}{r-j+1},\qquad 0\le j\le r.
$$

$\tau_{r,r}=0$ 准确保留相邻切片的硬端消失。由 (2.5)、(2.6)，条件平方差严格为

$$
\boxed{
\begin{aligned}
&\sum_{|X|=r}|p_A(X)+p_A(D\setminus X)|^2\\
&\quad-\sum_{|X|=r-1}
|(p_A+g_A)(X)+(p_A-g_A-\ell_A)(D\setminus X)|^2\\
&=\sum_{j=0}^r c_{r,j}
\left(\|S_j^0\|^2-\tau_{r,j}\|S_j^-\|^2\right).
\end{aligned}}
\tag{3.3}
$$

当 $r=0$ 时，第二个和为空，第一项就是 $|2p(A)|^2$，单独保留即可。

若暂取 $g=\ell=0$，则偶 $j$ 的相邻系数是
$2H_j^p(r)+\Delta^2H_j^p(r)$；奇 $j$ 的相邻系数是
$H_j^p(r-1)-H_j^p(r+1)$，而其等秩系数为零。因此差测度的 Catalan 正系数本身不能保证 (3.3) 正：非线性统计量还会在不同分拆切片中激活新的 harmonic 通道。

最上次数的通道仍有一个准确正性范围。若 $s\le r$，则 $H_s^p$ 为常数，而 $H_s^g=H_s^\ell=0$。其在 (3.3) 中的贡献为

$$
c_{r,s}(1-\tau_{r,s})(1+(-1)^s)^2\|H_s^p\|^2\ge0.
\tag{3.4}
$$

所以任何负项都来自局部 $j\le s-1$。这不表示它们是可自由删除的全局低阶 nuisance：即使所有全局 $q_j$ 都为零，下节反例中的局部低 harmonic 负项仍然存在。

更精确地，$j=s-1\le r$ 时 $H_j^p(m)$ 是一次多项式、$H_j^g(m)$ 是常数、$H_j^\ell=0$。若 $s$ 为奇数，该通道贡献非负；若 $s$ 为偶数，其贡献准确为

$$
-4c_{r,s-1}\tau_{r,s-1}
\|H_{s-1}^g-\partial_mH_{s-1}^p\|^2.
\tag{3.5}
$$

它是在同一个局部分拆中形成的实际平方，不是任意独立的负矩阵。

## 4. 全局算术缺陷的完整等式

将 (3.3) 乘以 $z_A^2z_D$，再对全部合法 $A,D,r$ 求和。独立等秩对子及 $p$ 的均值为零给

$$
\sum_{|I|=|J|=k}z_Iz_J|p(I)+p(J)|^2
=2e_k\|p\|_k^2.
$$

相邻对子的交叉均值同样消失，因为 $p+g=\mathcal R_{k-1,s}f$ 均值为零，故

$$
\begin{aligned}
&\sum_{|I_-|=k-1,|I_+|=k+1}z_{I_-}z_{I_+}
|(p+g)(I_-)+(p-g-\ell)(I_+)|^2\\
&\qquad=e_{k+1}\|p+g\|_{k-1}^2
+e_{k-1}\|p-g-\ell\|_{k+1}^2.
\end{aligned}
$$

结合 (1.4)，(3.3) 准确分解了下面的同源算术缺陷：

$$
\boxed{\mathcal A_{s,n}=
2e_k C_n-e_{k+1}C_{n-1}
-e_{k-1}\left(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*\right).}
\tag{4.1}
$$

所有 $\le s-1$ 拟合和 $\le s-2$ 重新投影都明确在 (3.2) 中。这里只是恒等式，未声称 $\mathcal A_{s,n}\succeq0$。

出生一时局部统计量 $p_A(X)+p_A(D\setminus X)$ 不依赖分拆，$g$ 是常数而 $\ell=0$；(3.3) 恰退化为 R295 的 Catalan 正余量。这解释其在线性层成立的原因。高次数则必须继续支付 (3.2) 的完整共同项。

## 5. 完整等权模型中的严格负例：不是加强 S1 反例

取所有 $b_i=1$、$M=24$、$s=4$、$n=1$，所以 $h=16$、$k=5$。可以取单位物理源

$$
f=\frac14(e_1-e_2)(e_3-e_4)(e_5-e_6)(e_7-e_8)\in K_4.
$$

这里乘积表示互不相交位上的 square-free 张量乘积；其 $16$ 个系数绝对值均为 $1/4$，故范数为一。无权删除在每一对上相消，所以 $df=0$。

无权完整 primitive 塔给

$$
C_j=\binom{h}{j}I_{K_s},\qquad
q_j=0,\qquad \delta_{n+1}=0.
$$

因此所用三个真实精度是 $C_0=1,C_1=16,C_2=120$，而

$$
e_4=10626,\quad e_5=42504,\quad e_6=134596.
$$

在整个 $K_4$ 上 (4.1) 给

$$
\boxed{\mathcal A_{4,1}
=2(42504)(16)-134596-(10626)(120)
=-49588<0.}
\tag{5.1}
$$

等价地，令

$$
A=C_0/e_4,\quad B=C_1/e_5,\quad C=C_2/e_6,
\qquad \rho=e_5^2/(e_4e_6),
$$

则

$$
\frac BA=4,\quad\frac CA=\frac{180}{19},\quad\rho=\frac{24}{19},
\qquad
\boxed{\frac{2\rho B-A-C}{A}=-\frac7{19}.}
\tag{5.2}
$$

全部全局拟合 nuisance 已经为零，所以不能把 (5.1) 归因于漏减某个回归项。真正加强 S1 在同一模型却有严格正缺陷

$$
C_1\Gamma_0C_1-C_2=256-120=136>0.
$$

故此例只排除 $2\rho B\succeq A+C$ 这一算术中间步骤的高出生延拓；它不反驳 $\kappa=1$，也不反驳可能通过其他方法得到的高出生 $\kappa=\rho$。

## 6. 算术比较常数必须支付的出生增长

仍取完整等权模型，但允许任意合法 $s,n,M$。把 $B$ 放在第 $k=s+n$ 切片，$A,C$ 分别放在 $k-1,k+1$，则

$$
B_j=\frac{\binom{M-2s}{j-s}}{\binom Mj}I_{K_s}.
$$

直接计算得到

$$
\frac AB=
\frac{n(M-s-n+1)}{(M-2s-n+1)(s+n)},
$$
$$
\frac CB=
\frac{(M-2s-n)(s+n+1)}{(n+1)(M-s-n)},
\qquad
\rho=\frac{(s+n+1)(M-s-n+1)}{(s+n)(M-s-n)}.
\tag{6.1}
$$

因此任何声称对该类模型成立的 $A+C\preceq\lambda_{s,n}\rho B$ 至少需要

$$
\boxed{\lambda_{s,n}\ge
\frac{n(M-s-n)}{(M-2s-n+1)(s+n+1)}
+\frac{(M-2s-n)(s+n)}{(n+1)(M-s-n+1)}.}
\tag{6.2}
$$

固定 $s,n$ 后令 $M\to\infty$，右侧趋于

$$
\boxed{\frac{n}{s+n+1}+\frac{s+n}{n+1}.}
\tag{6.3}
$$

不含 $\rho$ 的 $(A+C)/B$ 则趋于
$n/(s+n)+(s+n+1)/(n+1)$；两种比值不可混用。特别首边 $n=1$ 的 (6.3) 是
$1/(s+2)+(s+1)/2$，随出生增长。

若沿 R295 的纯代数配方路线，仅凭
$A+C+\text{创新项}\preceq\lambda\rho B$，要对任意相对谱完成
$\kappa\rho BA^{-1}B-\lambda\rho B+A$ 的平方，标准充分选择为
$\kappa=\lambda^2\rho/4$。因此该方法会带入出生平方量级的损失；这不是对真正最优加强常数的下界，等权最优常数仍不超过一。

## 7. 原连续尾的量词边界

上述条件恒等式适用于任意有限正权，故包括原 $z_i=(m+i)^{-4}$ 的每个连续有限头。但第 5 节说明，仅知道 R295 的 $\rho$ 有统一上界不足以支付高出生的 (4.1)。本稿也没有取得随原出生 $s$ 可控的加强常数。

若后续得到 $\kappa_s$，需要在原出生 $s$ 的全部合法高度中保持同一物理源和完整 (1.4)。只在硬顶得到的出生相关常数不能经过会增加出生的弱位归约后，免费视为原出生 $s$ 的常数。即使有多项式 $\kappa_s$，原 graph 的跨出生返回、普通右费及正常尾未知速率仍须按其实际预算另付。

依据：
[R295](../results/R295-birth-one-turan-remainder-law-and-all-height-strengthened-s1.md)，
[R296 主稿](../results/R296-all-birth-residual-regression-two-band-lift-and-physical-innovation.md)，
[完整回归二阶差](../results/R296-appendix-complete-regression-second-difference-and-common-source-invariance.md)。
