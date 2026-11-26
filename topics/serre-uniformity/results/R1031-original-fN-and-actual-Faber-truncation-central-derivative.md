# R1031：原 \(f_N\) 与真实 Faber 截断的中心导数

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
o1_theta / root，原 period 与 \(27\) 尺度经 o2_high_coefficient 复核。

**已证明：对每个 \(p=6N+5\ge41\)，原 R697/R949 的 \(f_N\)
模 \(p\) 非零，当且仅当下述同一个截断 Legendre 平方的中心导数非零。**
实际旧形、正 CM 嵌入、二次同源、Hodge frame 和全部单位比例均保留：
\[
d=(p-2)/3,\qquad H(z)=P_d(1-2z),\qquad
R(z)=[H(z)^2]_{\deg\le d},
\]
\[
\boxed{\quad f_N=0\pmod p
             \quad\Longleftrightarrow\quad R'(1/2)=0\pmod p.\quad}
\tag{1031.1}
\]
这里的 \(R\) 是原弱全纯形式的真实 Faber 截断；
不是任意满足相同微分方程的多项式。
本文亦给其准确非齐次方程，但尚未证明 \(R'(1/2)\) 全称非零。
原 primitive/Legendre 的同一个保留标签及 O2 bare 高坐标仍分别开放。

除明确标作特征零原始来源的式子外，以下涉及本素数的比较、Faber 正部、Hasse 分拆和 boxed 导数恒等式，均在所选整模型模 \(p\) 后理解。

## 1. 同一个 Ahlgren–Samart 输入

采用原 \(q=e^{2\pi i\tau}\)，写
\[
g=\eta(3\tau)^8,\quad
w=\frac{\eta(\tau)^3}{\eta(9\tau)^3}+3,\quad
h=\frac{\eta(9\tau)^6}{\eta(3\tau)^2},\quad
G=gw^2=\sum C_{\rm AS}(n)q^n .
\tag{1031.2}
\]
令 \(C=C_{\rm AS}(p)\)。
已有 [AS 精确比较](../notes/2026-11-26-ahlgren-samart-actual-low-coordinate-comparison.md)
证明 \(C=9\beta^3/2\ne0\bmod p\)，其中 \(\beta\) 是该文
原 \(E_+\) Robert 规范的低坐标。
这里仅消费此单位，不把它认作 \(f_N\) 或 bare 高坐标。

AS Lemma 4.3 的实际构造为
\[
\phi_2=h^{-1},\qquad
\phi_p=\phi_2 P_p(w)=q^{-p}+O(q),
\tag{1031.3}
\]
其中 \(P_p\) 整、次数 \(p-2\)，只含指数为 \(p-2\bmod3\)
的 \(w\) 幂。其余尖点的全纯性和唯一主部正是原构造的条件。
AS (4.4) 给完整等式
\[
\Theta_q^3\phi_p=-p^3G_p-Cg,\qquad \Theta_q=q\,d/dq .
\tag{1031.4}
\]

原 period 的准确展开是
\[
h=w^{-2}
 \left(\sum_{n\ge0}\frac{(3n)!}{(n!)^3}w^{-3n}\right)^2 .
\tag{1031.5}
\]
因为 \(w=q^{-1}+O(q^2)\)，模 \(p\) 有
\(w^p=q^{-p}+O(q^{2p})\)。
故原多项式主部唯一性给
\[
\boxed{\quad P_p(w)=[w^ph(w)]_{\text{非负 }w\text{ 幂}}.\quad}
\tag{1031.6}
\]
这里被删掉的首个负指数是 \(-3\)；
再乘 \(h^{-1}=O(w^2)\) 后为 \(O(q)\)。
因此没有遗漏一个 \(q^{-1}\) 项。

## 2. 原 cubic theta、Hasse 与齐次分拆

置 \(t=3\tau\)，使用同一 cubic theta
\[
a=a(t),\qquad b_c=\eta(t)^3/\eta(3t),\qquad
c=3\eta(3t)^3/\eta(t).
\]
它们满足
\[
a^3=b_c^3+c^3,\qquad
b_c(t/3)=a(t)-c(t),\qquad
w=3a/c,\qquad h=c^2/9 .
\tag{1031.7}
\]
Borwein–Borwein Theorem 2.3 给
\[
a={}_2F_1(1/3,2/3;1;z),\qquad z=c^3/a^3 .
\tag{1031.8}
\]
\((3n)!/(n!)^3\) 的 multinomial Lucas 恒等式，使原 Hasse
截面准确为
\[
\mathcal A(t)=a^{p-1}H(z),\qquad H(z)=P_d(1-2z).
\tag{1031.9}
\]
确切地，Lucas 给 period 的 Frobenius 分拆，
故右侧 \(q\)-展开为一；它本身是同权的 level-one Hasse
截面。没有在 supersingular 点把某个单独的 period 形式级数赋值为一。
\(-d\equiv2/3,d+1\equiv1/3\bmod p\)，固定了 Legendre 的方向。

由 (1031.6)，令
\[
\mathcal N=a^{p-2}R(c^3/a^3),\qquad
\Phi_p(t)=\phi_p(t/3),
\]
则
\[
\boxed{\quad \Phi_p=3^p\mathcal N/c^p .\quad}
\tag{1031.10}
\]
因 \(\mathcal A^2\) 的 \(c\) 指数都是三的倍数，存在唯一齐次分拆
\[
\boxed{\quad
\mathcal A^2=a^p\mathcal N+c^p\mathcal M,\qquad
\deg\mathcal N=\deg\mathcal M=p-2 .
\quad}
\tag{1031.11}
\]
\(j\le d\) 的项给 \(\mathcal N\)，其余项有 \(c\) 指数至少 \(p+1\)。
唯一性来自总次数 \(2p-2<2p\)：一个单项式不可能同时被
\(a^p\) 和 \(c^p\) 整除。

## 3. 真正的变换误差是 \(\mathcal A^2\)

取 \(\zeta=e^{2\pi i/3}\)、\(s=i\sqrt3\)。原 theta 变换是
\[
\binom ac\bigm|_1S
 =\frac1s\begin{pmatrix}1&2\\1&-1\end{pmatrix}\binom ac,
\qquad
\binom ac\bigm|_1T
 =\begin{pmatrix}1&0\\0&\zeta\end{pmatrix}\binom ac .
\tag{1031.12}
\]
第一式由 theta inversion 及
\(a(t/3)=a(t)+2c(t),\,b_c(t/3)=a(t)-c(t)\) 得到；
第二式保留 \(c=q_t^{1/3}\mathbf Z[[q_t]]\) 的原相位。

若 \((a,c)^T|_1\gamma=M_\gamma(a,c)^T\)，写
\[
M_\gamma=\begin{pmatrix}u&v\\w_0&x_0\end{pmatrix},
\qquad c_\gamma=w_0a+x_0c .
\]
Hasse 的 level-one 不变性与 (1031.11) 的唯一性给
\[
\binom{\mathcal N}{\mathcal M}(M_\gamma(a,c)^T)
 =(M_\gamma^{(p)})^{-T}
       \binom{\mathcal N}{\mathcal M}(a,c).
\]
所以有准确恒等式
\[
\boxed{\quad
\Phi_p|_{-2}\gamma
 =(\det M_\gamma)^{-p}\Phi_p
 -3^p(\det M_\gamma)^{-p}
       \frac{w_0^p\mathcal A^2}{c^pc_\gamma^p}.
\quad}
\tag{1031.13}
\]
在相关原 supersingular 内点，\(c,c_\gamma\) 都是单位。
因此值及一阶 jet 按真 weight \(-2\) 运输，剩余项及其一次导数均为零。
其 character 为
\(\chi(S)=1,\ \chi(T)=\zeta\)，因为 \(p\equiv2\bmod3\)。
本式没有假定 \(\phi_p\) 本身是一个 CM 本征形式。

## 4. 同一全六层旧形的一阶导数

令 \(F_k\) 为 R949 的原正 CM level-nine 形式，
\[
Q=e^{2\pi i\tau'/6},\qquad
V=V_{p-1}^{\dagger}
 =F_{p-1}(Q)-2^{p-1}\zeta^2F_{p-1}(Q^4).
\]
从原理想系数可逐项核
\[
\Theta_q^2 F_{p-1}=g\pmod p.
\]
对 \(p\nmid n=N\mathfrak a\)，
\(\alpha^{p-2}=\bar\alpha^3/n^2\bmod p\)；
共轭理想保持原 \(\epsilon_3\)，故给所示等式。
在 \(p\) 倍指数上，两个 CM 形式的系数均为零模 \(p\)。
结合 (1031.4) 得
\[
\Theta_q\phi_p=-C F_{p-1}\pmod p .
\tag{1031.14}
\]
此处在 \(p\nmid n\) 才除以 \(n^2\)；
在 \(p\mid n\) 时左边已由 \(\Theta_q\) 杀掉，没有作 \(0/0\)。

置
\[
U_p(\tau')=\phi_p(Q)-\frac{\zeta^2}{4}\phi_p(Q^4).
\]
由 \(2^{p-1}=1\bmod p\) 及 oldform 求导的四倍，
\[
\boxed{\quad \Theta_Q U_p=-C V .\quad}
\tag{1031.15}
\]
在原 \(\tau'\) Hodge frame 中，记 Hasse 为 \(\mathcal A_0\)，
\(B=D\mathcal A_0\)，其中 \(D\) 是原 Serre 导数。
Katz 的原算子为
\[
\Theta_Q=6(\mathcal A_0D+kB)\quad\text{作用于权 }k .
\tag{1031.16}
\]
原 mark \(P:\tau'=\rho=1+\zeta\) 满足
\(\mathcal A_0(P)=V(P)=0\)、\(B(P)\ne0\)。
取 \(k=-2\)，(1031.15) 先给 \(U_p(P)=0\)。
再按完整权数用 Leibniz 求导，得到
\[
\boxed{\quad DV(P)=6B(P)C^{-1}DU_p(P).\quad}
\tag{1031.17}
\]
这里 \(\mathcal A_0\) 是原 \(E_0\) 的 Hasse；
不与 §2 在二次商上使用的 \(\mathcal A(t)\) 混名。

## 5. 固定 CM 路径与 Maass 运输

令 \(t=\tau'/2\)、\(t_0=\rho/2\)。则
\[
U_p(2t)=\Phi_p(t)-\frac{\zeta^2}{4}\Phi_p(4t).
\]
和 R949 一样，取 \(g_0=T^2S\)、\(u(t)=(2-4t)^{-1}\)。
有 \(g_0u(t)=4t\)、\(u(t_0)=t_0\)、\(u'(t_0)=\zeta\)。
(1031.13) 给
\[
\Phi_p(4t)=\zeta^2u(t)^{-2}\Phi_p(u(t))
                +O(\mathcal A(u(t))^2).
\]
这些 elliptic curves 是原指定 degree-two quotient；
在 \(t_0\) 为 supersingular，所以误差不影响这一 jet。

记
\[
\mathcal D_k^*=(2\pi i)^{-1}\partial_t
                   -k/(4\pi\operatorname{Im}t).
\]
直接对上述原 oldform 求导可得
\[
\partial_t U_p(2t)|_{t_0}
 =(1-\zeta)\Phi_p'(t_0)+4\rho\Phi_p(t_0)
 =(1-\zeta)2\pi i\,\mathcal D_{-2}^*\Phi_p(t_0).
\]
因为 \(U_p(P)=0\)，Serre 导数在该点与普通导数相同；
\(\tau'=2t\) 的准确尺度给
\[
DU_p(P)=\frac{1-\zeta}{2}\mathcal D_{-2}^*\Phi_p(t_0).
\tag{1031.18}
\]

再取
\[
t_*=\frac{i}{\sqrt3},\qquad
\gamma=\begin{pmatrix}1&0\\1&1\end{pmatrix}
       =ST^{-1}S^{-1}.
\]
它把 \(t_*\) 送到 \(t_0\)，且 \(\chi(\gamma)=\zeta^2\)。
Maass 导数升至 weight zero；(1031.13) 的误差及其导数在 SS 点消失，
所以
\[
\mathcal D_{-2}^*\Phi_p(t_0)
 =\zeta^2\mathcal D_{-2}^*\Phi_p(t_*).
\tag{1031.19}
\]
\(t_*,t_0\) 的 \(j=54000\)，来自同一个 order \(-12\) 二次商；
原 \(\tau'=\rho\) 的 \(j\) 仍为零，没有把二者混成原 CM 点。

## 6. 在 \(t_*\) 求准确的原导数

\(3t_*=-1/t_*\)。eta 的 \(S\) 律给
\(b_c(t_*)=c(t_*)\)，从而
\[
a(t_*)^3=2c(t_*)^3,\qquad
r=a(t_*)/c(t_*)=\sqrt[3]2,\qquad z(t_*)=1/2,
\tag{1031.20}
\]
其中复嵌入的 \(r\) 为正实根，随后保留所选 \(p\)-进嵌入。

原恒等式
\[
3E_2(3t)-E_2(t)=2a(t)^2
\]
与 \(E_2^*\) 的 \(S\) 协变给
\(E_2^*(t_*)=-a(t_*)^2\)。
Matsuda Theorem 1.1 (1.5) 与 cubic identity 给
\[
D_1a=(-a^3+4c^3)/12,\qquad D_1c=a^2c/4.
\]
第二式也可直接对 \(c=3\eta(3t)^3/\eta(t)\) 求导。
因此在 \(t_*\)
\[
\mathcal D_1^*a=0,\qquad
\mathcal D_1^*c=a^2c/6 .
\tag{1031.21}
\]
在模 \(p\) 的同权式 (1031.10) 中用 Leibniz 法则；
\(c^p\) 的导数为零，\(z\) 的导数为 \(a^2/4\)，得到
\[
\boxed{\quad
\mathcal D_{-2}^*\Phi_p(t_*)=(3^p/4)r^p R'(1/2).
\quad}
\tag{1031.22}
\]
所有这些式子先在整的 theta/Hodge 表达中使用 Serre 导数，
再作 CM 特化及约化。非代数的 \(\pi\) 不被单独拿去取模；
Maass 写法只记录已经配平权数的原 CM 导数。

合并 (1031.17)–(1031.22)，准确为
\[
\boxed{\quad
DV_{p-1}^{\dagger}(P)
 =\frac94(\zeta^2-1)\,
       \frac{B(P)r^p}{C_{\rm AS}(p)}\,R'(1/2).
\quad}
\tag{1031.23}
\]
这里用了 \(3^{p+1}=9\bmod p\) 和
\((1-\zeta)\zeta^2=\zeta^2-1\)。
所有显示因子皆为原 \(p\)-单位。

## 7. 接回原 \(f_N\)

R949 (949.7)、(949.34–36) 在同一个 mark 给
\[
\mathcal C_{p-1}^{\rm mark}
 =\frac{(p-1)!}{24}(-864)^{-N}f_N
 =\frac{DV_{p-1}^{\dagger}(P)}
        {DV_4^\dagger(P)E_6(P)^N}.
\tag{1031.24}
\]
\(E_6(P)\) 与 \(DV_4^\dagger(P)\) 为单位。
后一事实使用 R918 (918.22) 的原代数恒等式
\(V_4^\dagger/E_4\) 在该 full-six mark 为单位；
这个具体恒等式及单位检查在所有 \(p>3\) 有效，
不把 R918 整篇只处理 \(p\equiv11\bmod12\) 的其它结论扩张。
因 \((p-1)!\)、24、864 都是单位，
(1031.23)–(1031.24) 完成 (1031.1)。

## 8. 同一个截断的准确 forcing

令 \(\mu=d(d+1)\)、\(T=z(1-z)\)，定义
\[
\mathcal L
 =T^2\partial^3+3T(1-2z)\partial^2
  +[1+(4\mu-6)T]\partial+2\mu(1-2z).
\tag{1031.25}
\]
由 Legendre 二阶方程取对称平方，
\(\mathcal L(H^2)=0\)。
设 \(c_{d+1}=[z^{d+1}]H^2\)。
在截断低端，\(\mathcal L(z^n)\) 的最低项是 \(n^3z^{n-1}\)；
在截断高端，次数 \(d+1\) 的系数为
\(-d(d+1)(3d+2)[z^d]H^2=0\bmod p\)。
所以
\[
\mathcal L R=-(d+1)^3c_{d+1}z^d .
\]

这个 \(c_{d+1}\) 的实际尺度由原源直接确定。
已有 \(G=h^2(w^3-27)w^2\)、\(\Theta_qw=-h(w^3-27)\)，故
\[
C_{\rm AS}(p)
 =\operatorname{Res}_{w=\infty}(-h w^{p+2}\,dw)
 =27^{d+1}[z^{d+1}]H^2
 =9c_{d+1}\pmod p .
\]
换元 \(z=27/w^3\) 的 \(27^{d+1}=9\) 被保留。
最终
\[
\boxed{\quad
\mathcal L R=-(d+1)^3\frac{C_{\rm AS}(p)}9z^d
            =-(d+1)^3\frac{\beta^3}{2}z^d .
\quad}
\tag{1031.26}
\]
右侧系数是单位。这并不决定指定中心导数 \(R'(1/2)\)；
局部非齐次方程的 forcing 单位不等于该导数单位。

## 来源与完整审核

- [R949](R949-original-all-weight-sigma-CM-marked-identity.md)，
  原正嵌入、full-six oldform、指定 degree-two quotient，
  以及 (949.7)、(949.34–36) 的全部 period 和 factorial 尺度。
- [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md)，
  (918.22)；只按 §7 明列的代数单位范围使用。
- [AS 原坐标比较](../notes/2026-11-26-ahlgren-samart-actual-low-coordinate-comparison.md)，
  原 \(w,h,g,G\)、period 与 \(C_{\rm AS}(p)=9\beta^3/2\)。
- Ahlgren–Samart，
  *A note on cusp forms as p-adic limits*，
  [作者全文](https://arxiv.org/pdf/1602.01036)，
  §4 Proposition 4.2、Lemma 4.3 的实际 \(\phi_p\) 构造和 (4.4)，
  Lemma 4.4 的单位范围；本文另证 (1031.6) 的真正 Faber 正部式。
- J. M. Borwein–P. B. Borwein，
  *A Cubic Counterpart of Jacobi's Identity and the AGM*，
  Trans. AMS 323 (1991), 691–701，
  [作者公开全文](https://www.cecm.sfu.ca/~pborwein/PAPERS/P50.pdf)，
  Theorem 2.3(a),(c)、(2.3) 及 pp.695–697 的 theta inversion。
- Kazuhide Matsuda，
  *Differential equations involving cubic theta functions and Eisenstein series*，
  Osaka J. Math. 57 (2020), 521–542，
  [原刊全文](https://ir.library.osaka-u.ac.jp/repo/ouka/all/76671/ojm57_03_521.pdf)，
  Theorem 1.1 (1.5)、§5.2。

o1_theta 与 root 逐式纸核真实主部、齐次分拆、全部变换误差、
Katz 导数的负权输入、oldform 四倍、固定二次同源路径、
Maass/Serre 整比较、\(9/4\) 相位及 forcing 的 \(27\) 因子；
o2 另核 period 与 forcing 的原坐标尺度。
本篇没有数学执行或有限窗口重算。
原 \(R'(1/2)\) 非零、primitive/Legendre 同标签、bare 高坐标及
Serre 主目标继续 OPEN。
