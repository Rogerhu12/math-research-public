# R1015：原双 Poincaré 的 class-(2,2) 投影与 bare 高系数的完整三角桥

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / root。

**已证明：同一个 norm-seven 双 Poincaré 源的另一实际投影，保留原 bare balanced 系数，并以显式单位把它与一个指定平方及完整低总阶卷积余项相连。** 两原行的单位比值分别为 \(6/49\) 和 \(342/7^8\)。余项没有被删除，其与平方的差非零仍 OPEN；这不是由源非零直接推出 bare 高坐标单位。

## 1. 固定原源和完整 class-(2,2) 空间

保持 R1001 的原模型、微分、sigma 规范及 CM 嵌入：
\[
E_-:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad S=\sigma(z)^6,
\]
\[
s^2=-3,\qquad \alpha=2+s,\quad\overline\alpha=2-s,\quad
\alpha\overline\alpha=7.
\]
原 bare 核与 norm-seven section 为
\[
K(z,t)=\frac{\sigma(z+t)}{\sigma(z)\sigma(t)},\qquad
W_\alpha=\frac{\sigma(\alpha z)}{\alpha\sigma(z)}
 =(x^3-c_\alpha)S,
\quad c_\alpha=-\frac{2+6s}{7}.
\]
使用同一个真实双 Poincaré 乘积
\[
\mathscr P_\alpha(z,t)=
 \alpha W_\alpha(z)W_{\overline\alpha}(t)
 K(\alpha z,t)K(z,-\overline\alpha t).
\tag{1015.1}
\]
R1001 已逐 multiplier/semicharacter 核准：它是实际
\(L_6\boxtimes L_6\) 的 meromorphic section，两个原点轴的极阶至多二，没有其它极。

仍取原 \(\mu_6\) 投影
\[
\Pi_a^z R=\frac16\sum_{\epsilon\in\mu_6}
 \epsilon^{-a}R(\epsilon z,t),
\]
另一变量同理。令
\[
U=x^2S=z^2\sum_{j\ge0}u_jz^{6j},\qquad u_0=1.
\tag{1015.2}
\]
轴上可有二阶极的实际一变量 section 空间，除以 \(S\) 后有完整基
\[
1,x,y,x^2,xy,x^3,x^2y,x^4.
\]
其中 class two 恰为一维 \(\langle x^2\rangle\)，没有隐藏的极部。
因此存在准确常数 \(C_{22}\) 使
\[
\Pi_2^z\Pi_2^t\mathscr P_\alpha=C_{22}U(z)U(t).
\tag{1015.3}
\]

## 2. 从原首项确定全部常数

原核对称，且
\[
[z^3t^2]K=[z^2t^3]K=c_3^-=-\frac16.
\tag{1015.4}
\]
例如直接使用 R1001 的原 \(\sigma=z-z^7/210+\cdots\) 即给 (1015.4)。

在 (1015.1) 的 \(z^2t^2\) 系数中，两个 \(W\) 必须都取常数。
两个核必须一个取上述总阶五的系数，另一个取原简单极项。
四个贡献的完整和为
\[
c_3^-\left(
 \alpha^4-\frac{\alpha^3}{\overline\alpha}
 +\overline\alpha^2-\alpha\overline\alpha^3
 \right)
=\frac6{\overline\alpha}
 (\alpha^3-\overline\alpha^3)c_3^-.
\]
由 \(\alpha^3-\overline\alpha^3=18s\)，得到
\[
\boxed{\quad
C_{22}=-\frac{18s}{\overline\alpha},\qquad
N(C_{22})=\frac{972}{7}.
\quad}
\tag{1015.5}
\]
所以它在全部 \(p\ge41\) 处都是单位。式 (1015.3) 是完整投影的恒等式；没有再减一个未指定的 polar summand。

## 3. 完整有限 Laurent 卷积和四个最高单核项

取
\[
n=6\ell+3\ge3,\qquad
c_n^-=[z^nw^{n-1}]K(z,w).
\]
本节等式在特征零成立；暂不将 \(n\) 限定到某个素数附近。\(\ell\) 为整数指标，第二形式变量记为 \(w\)。

令
\[
\mathcal I=\{(-1,0),(0,-1)\}\cup\mathbf Z_{\ge0}^2,\qquad
k_{u,v}=[z^uw^v]K(z,w),\quad k_{-1,0}=k_{0,-1}=1,
\]
\[
w_a=[z^{6a}]W_\alpha,\qquad
\overline w_b=[w^{6b}]W_{\overline\alpha}.
\tag{1015.6}
\]
其它不存在的系数都保留为零。

定义有限指标集 \(\mathcal T_n\) 为
\[
\begin{gathered}
0\le a,b\le\ell,\qquad (u,v),(u',v')\in\mathcal I,\\
u+u'=n-1-6a,\qquad
v+v'=n-1-6b.
\end{gathered}
\tag{1015.7}
\]
端点准确为 \(\ell\)：若 \(a\ge\ell+1\)，则 \(u+u'\le-4\)，低于真实最小值 \(-2\)；另一轴相同。这里包含两个核的全部极项，没有按最终全纯性擅自删掉它们。

再定义四项集合 \(\mathcal E_n\subset\mathcal T_n\)：四项均有 \(a=b=0\)，而两个核的指数依次为
\[
\begin{array}{c|c}
(u,v)&(u',v')\\ \hline
(n,n-1)&(-1,0)\\
(n-1,n)&(0,-1)\\
(-1,0)&(n,n-1)\\
(0,-1)&(n-1,n).
\end{array}
\tag{1015.8}
\]
由于核对称，其中两个 balanced 系数相等，均为 \(c_n^-\)。

定义完整余项
\[
\boxed{\quad
R_n=\alpha
 \sum_{\mathcal T_n\setminus\mathcal E_n}
 w_a\overline w_b\,
 \alpha^u(-\overline\alpha)^{v'}k_{u,v}k_{u',v'}.
\quad}
\tag{1015.9}
\]
这是实际源的有限卷积定义，没有自由归一化或未命名误差。
特别，负指数 \(v'=-1\) 时仍使用
\((-\overline\alpha)^{-1}\) 的原符号。

式 (1015.8) 的四项给出的 \(c_n^-\) 系数为
\[
\begin{aligned}
D_n
&=\alpha^{n+1}-\frac{\alpha^n}{\overline\alpha}
 +\overline\alpha^{\,n-1}-\alpha\overline\alpha^{\,n}\\
&=\frac6{\overline\alpha}
  (\alpha^n-\overline\alpha^n).
\end{aligned}
\tag{1015.10}
\]
这里 \(n\equiv3\pmod6\) 为奇数，已用于两个负号。

从 (1015.3) 取 \([z^{n-1}w^{n-1}]\)，得到准确的原三角桥
\[
\boxed{\quad
C_{22}u_\ell^2=D_n c_n^-+R_n.
\quad}
\tag{1015.11}
\]

### 余项确实只有更低单核总阶

由 \(\mu_6\) 对称性，\(K\) 的非极项总阶为 \(5\bmod6\)，最小为五。
在 \(\mathcal T_n\) 的一项中，两核总阶的和是
\(2n-2-6(a+b)\)。

若 \(a+b\ge1\)，另一核总阶至少 \(-1\)，故任一单核总阶至多 \(2n-7\)。
若 \(a=b=0\) 且另一核为极项，该项正是 (1015.8) 已取出的四项之一。
剩余情形两个核都为非极项，各至少五，故任一单核总阶也至多 \(2n-7\)。
因此
\[
\boxed{\quad
R_n\text{ 的每个非零单核输入总阶}\le2n-7.
\quad}
\tag{1015.12}
\]
该三角性针对单核总阶；它并不声称余项为零，或只依赖另一个 bare balanced 序列。

## 4. 两个原 near-\(p\) 行的逐项整性

现设 \(p=6N+5\ge41\)，并取原两行：
\[
(n,\ell)=
\begin{cases}
(p-2,N),&p\equiv11\pmod{12},\\
(p-8,N-1),&p\equiv5\pmod{12}.
\end{cases}
\tag{1015.13}
\]
O2 的原 \(p\equiv2,5\pmod9\) 限制在其应用时继续保留；本篇恒等式不以它为删除项的理由。

对 (1015.7) 中任一核，每个指数均不超过 \(n\le p-2\)，因为另一核单轴指数最低为 \(-1\)。同一个核的两个指数不可能同时等于 \(n\)：否则另一核的两个指数都为负，要求 \((-1,-1)\)，它不在 \(\mathcal I\) 中。

所以当 \(n=p-2\) 时，可用核对称性让第二指数至多 \(p-3\)，第一指数至多 \(p-2\)。这恰在 R984 §3 的原有限整核范围内。\(n=p-8\) 时更在其内部。极项本身的系数为一，亦为整。

R984 正文使用 \(E_+\)。这里仅为整性结论作已固定的 \(E_+\leftrightarrow E_-\) 单位尺度运输：可在未分歧扩张中取六次根单位，sigma 与每个有限系数按相应单位幂运输。全部 (1015.1)–(1015.11) 的等式和符号仍在原 \(E_-\) 上，没有把 \(c_n^+\) 代入 \(c_n^-\)。

此外，两个 \(W\) 的前缀 \(a,b\le\ell\le N\)，以及
\(u_\ell=[z^{n-1}]U\)，均在 R702 的原首-\(p\) 整块中。
\(\alpha,\overline\alpha\) 为 \(p\)-单位。因此 (1015.9) 的每个完整乘积单独为整，(1015.11) 可合法逐项约化。

本证明没有先将整个无限 sigma 核约化，也不靠最终和的相消来掩盖未审的分母。

## 5. 两行的实际单位比值

模 \(p\) 有 \(\alpha^p=\overline\alpha\)，故对 \(n=p-r\)，
\[
\frac{D_{p-r}}{C_{22}}
=-\frac{\alpha^{p-r}-\overline\alpha^{p-r}}{3s}
\equiv
\frac{\alpha^{r+1}-\overline\alpha^{r+1}}{3s\,7^r}.
\tag{1015.14}
\]
消费 R1001 已证明的原固定值
\[
\alpha^3-\overline\alpha^3=18s,\qquad
\alpha^9-\overline\alpha^9=1026s.
\]
于是
\[
\boxed{\quad
\frac{D_{p-2}}{C_{22}}\equiv\frac6{49},\qquad
\frac{D_{p-8}}{C_{22}}\equiv\frac{342}{7^8}.
\quad}
\tag{1015.15}
\]
两者在所有 \(p\ge41\) 处是单位，第二分子
\(342=2\cdot3^2\cdot19\) 没有原范围内的坏素数。

因此两个原 bare 高坐标准确为
\[
\boxed{\begin{aligned}
\overline c_{p-2}^-
 &=\frac{49}{6}
 \left(\overline u_N^{\,2}-\frac{\overline R_{p-2}}{\overline C_{22}}\right),\\
\overline c_{p-8}^-
 &=\frac{7^8}{342}
 \left(\overline u_{N-1}^{\,2}
       -\frac{\overline R_{p-8}}{\overline C_{22}}\right).
\end{aligned}}
\tag{1015.16}
\]
所有余项都是 (1015.9) 的指定实际有限卷积。

## 6. 与原非零任务的关系

R1001 的 \(\Pi_4\boxtimes\Pi_0\) 投影恢复原 \(F\boxtimes G\)。
本篇 \(\Pi_2\boxtimes\Pi_2\) 则给另一个真实来源，并在其最高单核层保留了 bare \(c_n^-\) 的单位系数。两者不能混作同一个投影。

式 (1015.16) 将原两行的非零问题化为一个指定平方与全部 \(R_n/C_{22}\) 的差非零。尚未证明这个差非零。即使另外得到 \(u_N\) 或某个完整 \(U\boxtimes U\) 卷积非零，也不能删除 \(R_n\) 或据此推得该差非零。

后继须继续比较这个完整余项与实际小 theta 源、Fay 关系或原 divided Ramanujan 坐标。原 primitive/Legendre 同 \(h\)、实际全局高度和 O0 覆盖也没有因本三角桥而完成。

## 7. 依赖与核准

- [R1001](R1001-norm-seven-dual-Poincare-source-and-original-filtered-tensor.md) §§1–3、7：同一个 norm-seven 双 Poincaré 源、完整轴极空间、全部符号和固定 \(\alpha\) 幂差。
- [R702](R702-first-pole-block-and-uniform-shifted-units.md)：原六维 sigma section 的首-\(p\) 整块。
- [R984](R984-frobenius-regularized-finite-Kronecker-kernel-and-rational-Cartier-descent.md) §3：保原两个指数的有限整核；本篇明确使用核对称性核准其边界。
- [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：O2 原 bare 系数、两行与实际高迹的已证等价。

o2_high_coefficient 与 root 独立纸面核准 class-two 的完整空间、四个最高单核项、余和全部端点、两行有限整性及两个单位比值。无数学程序执行，无数值窗口或固定常数重算。
