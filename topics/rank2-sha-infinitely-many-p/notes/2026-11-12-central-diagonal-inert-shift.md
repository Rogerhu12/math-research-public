# 中央对角的惰性首层平移与不可消去的分母列

日期：2026-11-12。**状态：以下模 \(p\) 平移及预算下界已证明。**

固定中央 theta 笔记的
\[
d_m=[z^mw^m]\mathscr K(z,w),\qquad
e_m=d_m/f^{2m+1}\in\mathbb Q,\qquad f=34(1+i).
\]
本篇不把 BK 的 ordinary 整性用到 supersingular places。
从固定代数微分系统直接得到：

> 若 \(p\ge7,\ p\equiv3\pmod4\)，则对 \(0\le s\le p-3\)，
> \[
> p^2d_{p+1+s}\equiv \kappa_p^2d_s\pmod p,
> \qquad
> \kappa_p=\delta^{p-1}X
> =-\frac12(-1)^{(p+1)/4}
> \binom{(p+1)/2}{(p+1)/4}17^{(p+1)/4}
> \in\mathbb F_p^\times.
> \]
> 左侧确为 integral 后才作上述还原。
> 对固定任一个 \(d_{m_0}\ne0,\ m_0\ge1\)，
> 几乎所有 inert \(p\) 满足 \(v_p(e_{p+1+m_0})=-2\)。

因此中央对角的 inert 截断系数预算至少为 \(\log k+O(1)\)。
与 ordinary 笔记合并，直接系数缩放预算至少为 \(2\log k+O(1)\)。
这仍不是 Herblot 最优评价映射 \(\alpha\) 的下界。

## 1. 代数微分系统与 supersingular 的常数

沿用
\[
\mathcal R=\mathbb Z_{(p)}[U,X,Y]/(Y^2-X^3+17X),
\]
\[
\mathcal DU=-X,\qquad \mathcal DX=2Y,\qquad
\mathcal DY=3X^2-17,\qquad \mathcal L=\mathcal D+U,
\]
\[
C_n=\mathcal L^n1,\qquad
q_j=[w^j]\frac{w}{\sigma(w)}.
\]
在曲线子代数上记 \(\delta=\mathcal D|_{\mathbb Z_{(p)}[X,Y]}\)。

在惰性 \(p\) 处，Hasse 不变量为零，所以
\[
\delta^p=0
\quad\text{在模 }p\text{ 的曲线函数域上}.
\tag{1.1}
\]
令
\[
\kappa=\delta^{p-1}X.
\]
这是常数：
\(\delta^{p-1}X\in\mathbb F_p[X]\) 的次数至多 \((p+1)/2<p\)，
而其 \(\delta\) 导数由 (1.1) 为零；
因此普通多项式导数为零，只能是常数。

\(\mathcal D^p\) 在特征 \(p\) 中仍为导子。
它在 \(X,Y\) 上为零，在 \(U\) 上为 \(-\kappa\)，故
\[
\boxed{\quad \mathcal D^p=-\kappa\partial_U.\quad}
\tag{1.2}
\]
注意这与 ordinary 的 \(\mathcal D^p=A_p\mathcal D\) 不同。

\(\partial_U\) 与 \(\mathcal D\) 交换，而
\([\partial_U,\mathcal L]=1\)，所以
\[
\partial_UC_n=nC_{n-1}.
\tag{1.3}
\]
Bell/Jacobson 恒等式给
\[
\mathcal L^p=\mathcal D^p+B,\qquad
B=C_p=U^p-\delta^{p-2}X,
\tag{1.4}
\]
从而
\[
\mathcal DB=-\kappa,\qquad \mathcal D^2B=0,
\]
\[
\boxed{\quad
C_{p+n}=-\kappa nC_{n-1}+BC_n\pmod p.
\quad}
\tag{1.5}
\]

## 2. 真实 torsion 初值满足 \(B(S)=0\)

这一点必须对实际导子轨道证明，不能对任意 \(U\) 初值假定。

对 \(S\in\mathcal S\)，有
\[
[34]S=T=(0,0),\qquad
U_S=\zeta(z_S)-\bar z_S/A.
\]
定义
\[
F_S(z)=e^{-z\bar z_S/A}\frac{\sigma(z_S+z)}{\sigma(z_S)}.
\]
整数 \(a=34\) 的 division function 给出一般分配式
\[
F_T(az)=F_S(z)^{a^2}
\frac{\Psi_a(S+z)}{\Psi_a(S)}.
\tag{2.1}
\]
因 \(S\) 的阶素于 \(p\)，它既不还原到 \(O\)，也不还原到
非零 \(a\)-torsion；所以 \(\Psi_a(S)\) 是单位。
\(a\) 本身也是单位。

由于 \(T\) 为二挠点，
\[
U_T(z)=\zeta(z+z_T)-\zeta(z_T)
\]
为奇函数。故
\[
U_T(0)=0,\qquad U_T^{(p-1)}(0)=0.
\]
令 \(h=\delta\log\Psi_a\)。对 (2.1) 的对数分别取一次和 \(p\) 次导数，
得到
\[
h(S)=-a^2U_S,\qquad
(\delta^{p-1}h)(S)=-a^2(\mathcal D^{p-1}U)(S).
\tag{2.2}
\]
对于任意局部单位有理函数 \(g\)，
\(\delta+h_g=g^{-1}\delta g\)，其中 \(h_g=\delta g/g\)。
由 (1.1) 及 Bell/Jacobson 公式，
\[
\delta^{p-1}h_g=-h_g^p.
\]
代入 (2.2)，使用 \(a^{2p}\equiv a^2\pmod p\)，得到
\[
(\mathcal D^{p-1}U)(S)=-U_S^p,
\]
即
\[
\boxed{\quad B(S)=C_p(S)=0\pmod p.\quad}
\tag{2.3}
\]

此证明使用 \(34\)，不因固定整数 \(69\) 而额外排除 \(p=23\)。
所有 \(U_S,X(S),Y(S)\) 都在当前未分歧局部整数环中整。

## 3. \(q_j=w/\sigma(w)\) 在第一个区间的完整分母

下面只需 \(j<2p\)，不假定所有 Hurwitz 系数的统一全局估计。

首先，形式指数 \(t=\exp_E(z)\) 的次数 \(<p^2\) 的系数均为整。
确实，\(\delta\) 保持 \(\mathbb Z_p[[t]]\)，且
\(\delta^p\) 模 \(p\) 为零。
所以 \(\delta^p/p\) 是保持该整环的线性算子。
若 \(n=ap+r<p^2,\ 0\le r<p\)，则
\[
\delta^n=(\delta^p)^a\delta^r
\]
取值被 \(p^a\) 整除，而 \(v_p(n!)=a\)。
因此流的系数 \((\delta^nt)(O)/n!\) 为整。
严格逆形式对数在同一有限次数范围也整。

由 \(x(t)\in t^{-2}\mathbb Z_p[[t]]\)，于是
\[
x(z)=z^{-2}+\sum_{n\ge1}a_nz^{4n-2}
\]
在 \(4n-2\le2p-3\) 时 \(a_n\) 为整。
因此
\[
\log\frac{\sigma(w)}w
=
-\sum_{n\ge1}\frac{a_n}{(4n-1)(4n)}w^{4n}
\tag{3.1}
\]
在次数 \(<2p\) 内只有一个可能非整项，即次数 \(p+1\)。

令 \(r=(p+1)/4\)。
\(\delta^{p-1}x\) 的 Laurent 展开常数项为 \((p-1)!a_r\)，所以
\[
\kappa\equiv-a_r\pmod p.
\]
于是 (3.1) 的次数 \(p+1\) 系数乘 \(p\) 后为 \(\kappa\)。
该常数也可以由 R38 的已证明首坏项读出：
严格的整换元在次数 \(p+1\) 保留首个 \(p^{-1}\) 剩余，
具体地，在所需截断内 \(t(z)/z\in1+z^4\mathbb Z_p[[z^4]]\)，
所以 \(\log(t(z)/z)\) 到 \(p+1\) 次只使用少于 \(p\) 个因子，
其对数展开的整数分母均为单位。这个附加对数为整，
不会从 \(\Sigma(t)/t\) 到 \(\sigma(z)/z\) 新增同阶的 \(p\)-分母。
而
\[
p[w^{p+1}]\log\frac{\sigma(w)}w
\equiv-\frac{w_r}{2},\qquad
w_r=(-1)^r\binom{2r}{r}17^r.
\]
因此
\[
\boxed{\quad\kappa=-w_r/2\in\mathbb F_p^\times.\quad}
\tag{3.2}
\]
非零性来自 \(2r=(p+1)/2<p\)，相应二项式及 \(17\) 均为单位。

去掉 (3.1) 的这一个非整项，剩余部分在次数 \(<2p\) 内整且从四次开始。
对它取指数所用的阶乘至多为
\(\lfloor(2p-1)/4\rfloor!\)，仍为单位。
非整项的平方已到次数 \(2p+2\)，超出当前范围。
所以对 \(q_j=[w^j]w/\sigma(w)\) 得到准确关系：
\[
q_j\in\mathcal O\quad(0\le j<p+1),
\qquad v_p(q_j)\ge-1\quad(j<2p),
\]
\[
\boxed{\quad
p q_{p+1+j}\equiv-\kappa q_j\pmod p
\qquad(0\le j\le p-2).
\quad}
\tag{3.3}
\]
本式包括所有零系数的情况；\(q_j=0\) 若 \(4\nmid j\)。

## 4. 第一段中央系数整性

中央 theta 公式为
\[
d_m=\frac1{m!}
\sum_{j=0}^{m+1}
\frac{q_j}{(m+1-j)!}
\operatorname{Tr}_{F/K}
\left((\mathcal D^mC_{m+1-j})(S)\right).
\tag{4.1}
\]
其中 \(S=P_f\)，也可把迹写为对全部 \(\mathcal S\) 求和。

若 \(m\le p-2\)，所有出现的阶乘和 \(q_j\) 都整，所以 \(d_m\) 整。
若 \(m=p-1\)，唯一有 \(p\)-分母的项是 \(j=0\) 的 \(p!\)。
其分子由 (1.4) 满足
\[
\mathcal D^{p-1}C_p=\mathcal D^{p-1}B=0\pmod p,
\]
故这项也整。因此
\[
\boxed{\quad d_m\in\mathcal O\qquad(0\le m\le p-1).\quad}
\tag{4.2}
\]
这里没有对 \(d_p\) 或 \(d_{p+1}\) 的完整整性作结论。

## 5. 模 \(p\) 的中央平移

固定 \(0\le s\le p-3\)，置
\[
m=p+1+s.
\]
于是 \(m+1\le2p-1\)。
(4.1) 中外面的 \(m!\) 恰有一个 \(p\)-因子。
按第 3 节，内层最多另出现一个 \(p\)-分母；
所以 \(p^2d_m\) 确为整。

乘 \(p^2\) 后再模 \(p\)，只有两类项保留：

- \(0\le j\le s+2\)：内层 \((m+1-j)!\) 含一个 \(p\)，而 \(q_j\) 整；
- \(j=p+1+v,\ 0\le v\le s+1\)：阶乘为单位，而 \(q_j\) 可能含一个 \(p^{-1}\)。

其他项只有外面的一个 \(p^{-1}\)，乘 \(p^2\) 后为零。
两类不会重叠。

为简记，在一个实际 torsion 点取值并写
\[
T_{a,n}=(\mathcal D^aC_n)(S).
\]
由 (1.2)、(1.3)，
\[
T_{p+s+1,n}=-\kappa nT_{s+1,n-1}\pmod p.
\tag{5.1}
\]
若 \(n=p+a,\ a\ge1\)，将 (1.5) 应用于 \(C_{p+a-1}\)，
再用 \(B(S)=0,\ \mathcal DB=-\kappa,\ \mathcal D^2B=0\)，得
\[
T_{p+s+1,p+a}
=
\kappa^2a\left\{
(a-1)T_{s+1,a-2}
+(s+1)T_{s,a-1}
\right\}\pmod p.
\tag{5.2}
\]
当 \(a=0\) 时左边为零；式中带零系数的负下标项略去。

由 Wilson 公式，对 \(0\le a<p\)，
\[
\frac{p}{(p+a)!}\equiv-\frac1{a!}\pmod p.
\tag{5.3}
\]
第一类取 \(a=s+2-j\)，用 (5.2)、(5.3) 后贡献为
\[
\kappa^2d_s
+
\frac{\kappa^2}{(s+1)!}
\sum_{j=0}^{s}
\frac{q_j}{(s-j)!}
\operatorname{Tr}_{F/K}T_{s+1,s-j}.
\tag{5.4}
\]
第二类使用 (3.3)、(5.1)、(5.3)，其贡献恰为
\[
-\frac{\kappa^2}{(s+1)!}
\sum_{v=0}^{s}
\frac{q_v}{(s-v)!}
\operatorname{Tr}_{F/K}T_{s+1,s-v}.
\tag{5.5}
\]
两项完全相消，留下
\[
\boxed{\quad
p^2d_{p+1+s}\equiv\kappa^2d_s\pmod p,
\qquad0\le s\le p-3.
\quad}
\tag{5.6}
\]

这项相消是在两个明确的分母来源之间发生的，
不是先将 raw numerator 模 \(p\) 再不合法地除以 \(p\)。

特别地，
\[
p^2d_{p+1}\equiv\kappa^2d_0=0\pmod p,
\qquad
p^2d_{p+2}\equiv\kappa^2d_1\pmod p.
\tag{5.7}
\]
第一式只保证 \(v_p(d_{p+1})\ge-1\)，不单独证明其整性。
有限样例中的更强消失需要另证。

## 6. 有理下降后的式子与预算下界

因 \(p\) 惰性，\(\bar f\) 是 \(f\) 的 Frobenius，且
\[
f^{p+1}\equiv Nf\pmod p.
\]
用 \(d_m=f^{2m+1}e_m\) 改写 (5.6)，得到完全有理的剩余式
\[
\boxed{\quad
p^2e_{p+1+s}
\equiv
\frac{\kappa^2}{(Nf)^2}e_s\pmod p.
\quad}
\tag{6.1}
\]

从中央整函数的非多项式性，固定
\(m_0\ge1\) 使 \(e_{m_0}\ne0\)。
除去有限个素数后，\(p\ge m_0+3\)，且 \(e_{m_0}\) 为 \(p\)-单位。
(3.2)、(6.1) 因而强制
\[
\boxed{\quad v_p(e_{p+1+m_0})=-2
\quad\text{对几乎所有 inert }p.\quad}
\tag{6.2}
\]

定义与 ordinary 笔记相同的截断系数量
\[
s_p(k)=
\max_{2\le m\le k}
\left(0,-\frac{v_p(e_m)}{m-1}\right),
\qquad
\mathcal B_{\rm inert}(k)
=\sum_{\substack{p\equiv3\ (4)\\p\text{ good}}}s_p(k)\log p.
\]
由 (6.2)，
\[
\mathcal B_{\rm inert}(k)
\ge
2\sum_{\substack{p\le k-1-m_0\\p\equiv3\ (4)\\p\notin S}}
\frac{\log p}{p+m_0}
=
\log k+O(1),
\tag{6.3}
\]
其中 \(S\) 为固定有限集合。
本篇不据此声称 inert 上界或全部图形的准确 size。

结合已证明的 ordinary
\(\mathcal B_{\rm ord}(k)=\log k+O(1)\)，得到
\[
\mathcal B_{\rm ord}(k)+\mathcal B_{\rm inert}(k)
\ge2\log k+O(1).
\tag{6.4}
\]
因此中央整函数的系数缩放预算不会因为 ordinary 中心块的额外消失
而自动降到 Herblot 所需的 \(1/2\) 以下。

(6.4) 仍只针对明确的截断系数预算。
它不把该量等同于 vanishing-jet filtration 中评价映射的最优高度。

## 7. 已独立数值核验与未扩大之处

另一分支对真实 \(256\) 点轨道作无分歧环计算，
在 \(p=3,7,11\) 的样例中均发现
\(p^2d_{p+2}\equiv\kappa^2d_1\pmod p\)；
本篇的一般证明仅陈述 \(p\ge7\)，不依赖这些样例。
任意未校准的 primitive 轨道只差 \(\mu_4\) 整体伸缩；
对 (5.6)，移位 \(p+1\) 是 \(4\) 的倍数，故两边的共同单位因子相同。

本篇不从有限数值样例推断 \(d_p=0\)、\(d_{p+1}\) 整，
也不把 supersingular 与 ordinary 的 \(\mathcal D^p\) 关系混用。
全部新增结论是 (1.2)、真实初值 (2.3)、首区间 (3.3)、
中央平移 (5.6) 和预算下界 (6.3)。

### 证明依赖

- 中央 theta 对角笔记：固定 \(F_S\)、\(\Psi_{34}\)、\(\mathcal D,C_n,q_j\)
  和准确式 (4.1)；其源头为 Bannai–Kobayashi 的 Kronecker 展开。
- R38 (5)–(7)：固定 sigma 的首个 inert 对数分母，
  \(p c_{(p+1)/4}\equiv-w_{(p+1)/4}/2\)。
- 本篇的 \(\mathcal D^p\)、34 分配、两类分母相消都在上文重新证明，
  没有引用 BK Corollary 2.17 的 ordinary 整性来替代它们。
