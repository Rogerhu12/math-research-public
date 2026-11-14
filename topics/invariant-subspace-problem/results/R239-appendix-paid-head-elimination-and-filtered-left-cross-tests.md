# R239 附录：两费用中的首头消元与保全左交叉项的正过滤测试

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：本文的联合费用消元、完整同源运输及双侧稳定的首头过滤测试均已证明。它没有证明原全源三 Gram 上界；留下的源图空间和未滤首头部分均明确保留。

本文接[首源头度量分裂](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)和[完整源 Schur 坐标](R239-appendix-complete-source-schur-coordinates-and-growing-head-observation.md)。前稿中的物理首头投影只约化两种右度量，未被证明约化左度量。下面在不假定这种额外交换性的条件下处理其左交叉项。

## 1. 同一个源上的三个真实算子

固定原合法 $m\ge5,d=2^m,4d\le q\le e^{d^3/4}$。全部算子保持在原完整源空间 $\mathscr R_q$ 上。写
$$
L=J_q^{-1},\qquad B=J_{b,q}^{-1},\qquad G=G_q,
\qquad C=F_{\rm flag}^*L.
$$
于是对原源 $r$，
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
c^\flat(r)=Cr,\quad
\lambda_{\rm flat}(r)^2=\|Cr\|^2.
\tag{1.1}
$$
定义真正已付的两费用平方和及其度量
$$
\boxed{\chi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle Mr,r\rangle,\qquad M=B+C^*C=B+LGL.}
\tag{1.2}
$$
这里没有把裸链换成完整右最小链。

令 $P$ 为物理第零源头投影，$Q=I-P$，$\mathscr R_0=P\mathscr R_q$；以 $\iota_0$ 表示其等距嵌入。前稿证明
$$
[B,P]=[G,P]=0,\qquad
B|_{\mathscr R_0}=K,\qquad G|_{\mathscr R_0}=K^{-1},
\tag{1.3}
$$
其中
$$
K=(D_{q+1}^{\dagger}|_{E_{d-1,q}})^*
   (D_{q+1}^{\dagger}|_{E_{d-1,q}})
$$
含全部允许的尾短核阶。记 $k_h$ 为只有首段第零头非零、该项等于 $D_{q+1}^{\dagger}h$ 的实际零返回链，则
$$
F_{\rm flag}k_h=\iota_0h,\qquad
\|k_h\|^2=\langle Kh,h\rangle.
\tag{1.4}
$$
它同时是这个源的裸及完整右最小链。

固定参数下所有算子有界。若 $\nu=\|D_m\|$，每条裸可行链的首段都满足 $Da_1=r$，因此 $B\succeq\nu^{-2}I$；特别 $M$ 及下面的压缩均有界可逆。并不从这个下界推断 $L$ 的温和上界。

## 2. 在已付两费用中消去首头

按 $\mathscr R_0\oplus Q\mathscr R_q$ 写 $M=(M_{ij})$。由 (1.3)，
$$
M_{00}=K+C_0^*C_0,\qquad
M_{01}=C_0^*C_1,
\quad C_0=C\iota_0,\quad C_1=C|_{Q\mathscr R_q}.
\tag{2.1}
$$
定义
$$
\boxed{
P_Mr=\iota_0M_{00}^{-1}\iota_0^*Mr,\qquad
s=P_Mr,\quad \widehat r=r-s.}
\tag{2.2}
$$
这是 $M$ 内积中到原首头子空间的真正正交投影。它不是物理投影 $P$，也不是左度量投影。直接乘回得
$$
P_M^2=P_M,\qquad
\iota_0^*M\widehat r=0,\qquad Q\widehat r=Qr,
$$
以及
$$
\boxed{\chi(r)^2=\chi(s)^2+\chi(\widehat r)^2.}
\tag{2.3}
$$
因 $s$ 的源支持在首头，前稿的同源配对准确给
$$
\mu(s)^2\le\alpha(s)\lambda_{\rm flat}(s)
\le\frac12\chi(s)^2.
$$
所以
$$
\boxed{
\mu(s)\le\chi(r)/\sqrt2,\qquad
\alpha(\widehat r)^2+\lambda_{\rm flat}(\widehat r)^2
\le\chi(r)^2.}
\tag{2.4}
$$
这同时支付了左源修正及修正后两种费用，不需要另行假定平坦源运输收缩。各单项费用未被声称分别小于各自原项；不增的是 (1.2) 的实际平方和。

### 2.1 只含有界正收缩的显式公式

置
$$
z=K^{1/2}Pr,\qquad V=C_0K^{-1/2},\qquad c=Cr.
$$
这里 $Pr$ 已识别为 $\mathscr R_0$ 中的向量。令
$$
u=(I+V^*V)^{-1}(z+V^*c).
\tag{2.5}
$$
则
$$
s=\iota_0K^{-1/2}u,\qquad
\alpha(s)=\|u\|,\qquad
c^\flat(s)=Vu.
\tag{2.6}
$$
该式保留 $L$ 的全部真实交叉块，因为 $V=F_{\rm flag}^*L\iota_0K^{-1/2}$ 使用完整 $L$。

归一化修正后的首头裸变量与完整平坦链准确为
$$
\widehat z=z-u,\qquad \widehat c=c-Vu,
\qquad
\boxed{\widehat z+V^*\widehat c=0.}
\tag{2.7}
$$
这是消元后尚须保留的真实来源关系，不是令首源头为零。

由谱演算，
$$
\|(I+V^*V)^{-1}\|\le1,\qquad
\|V(I+V^*V)^{-1}\|\le\tfrac12,
$$
$$
\|V(I+V^*V)^{-1}V^*\|\le1.
\tag{2.8}
$$
因此 (2.5) 并未单独支付 $V$ 或整个头逆的巨大范数。更准确地，$u\mapsto(u,Vu)$ 的闭图正交投影给
$$
\|z\|^2+\|c\|^2
=\|u\|^2+\|Vu\|^2+\|\widehat z\|^2+\|\widehat c\|^2.
\tag{2.9}
$$
裸链的其余物理源头与上述首头裸链正交，且在 (2.2) 中保持不变；加回该部分正是 (2.3)。

## 3. 剩余图空间与准确左交叉块

定义闭图空间
$$
\mathscr R_{\rm rem}=\ker(\iota_0^*M)
=\left\{\mathcal R x:x\in Q\mathscr R_q\right\},
\qquad
\mathcal R x=(-M_{00}^{-1}M_{01}x,x).
\tag{3.1}
$$
它是两费用中的补空间；一般不等于物理 $Q\mathscr R_q$。其真实费用为
$$
M_{\rm rem}=\mathcal R^*M\mathcal R
=M_{11}-M_{10}M_{00}^{-1}M_{01}.
\tag{3.2}
$$
其真实左度量必须保留为
$$
\boxed{
\begin{aligned}
L_{\rm rem}:=\mathcal R^*L\mathcal R
={}&L_{11}-L_{10}M_{00}^{-1}M_{01}
-M_{10}M_{00}^{-1}L_{01}\\
&+M_{10}M_{00}^{-1}L_{00}M_{00}^{-1}M_{01}.
\end{aligned}}
\tag{3.3}
$$
这不是 $L$ 的通常 Schur 补，也不能只留下 $L_{11}$。

**精确常数转移。** 若在 (3.1) 的剩余图空间上证明
$$
L_{\rm rem}\preceq C_mM_{\rm rem},
\tag{3.4}
$$
则在原完整源空间上
$$
\boxed{L\preceq(C_m+\tfrac12)M.}
\tag{3.5}
$$
证明：对 (2.2) 的分解，左最小原像的线性性、(2.4) 与 (3.4) 给
$$
\mu(r)\le\mu(s)+\mu(\widehat r)
\le\tfrac1{\sqrt2}\chi(s)+\sqrt{C_m}\chi(\widehat r).
$$
再在这两个实数上作 Cauchy，并用 (2.3)，即得 (3.5)。反向显然：原全源估计限制到该图空间仍成立。

因此只要在剩余图上支付原目标常数，首头及其全部左交叉项最多增加 $1/2$；没有把未证的左交换性作为输入。

### 3.1 真实来源的合法运输

取任一已经支付 $\chi(r_m)\to0$、且原最小左原像 $v_m=E_{q_m}^{\dagger}r_m\to w$ 的实际来源。按同一个源 (2.2) 定义 $\widehat r_m$，则
$$
\boxed{
E_{q_m}^{\dagger}\widehat r_m\to w,\qquad
\chi(\widehat r_m)\le\chi(r_m)\to0,\qquad
\widehat r_m\in\mathscr R_{\rm rem}.}
\tag{3.6}
$$
第一式由 $\|E_{q_m}^{\dagger}s_m\|=\mu(s_m)\le\chi(r_m)/\sqrt2$ 得到。若原源由真实窄通量 $\overline f_m$ 构成，这里先保留那个准确源公式，再施加 (2.2) 的已付线性修正；没有直接把 $\overline f_m$ 换成环境向量。

前稿的强制 primitive 坐标趋零以及中间边界带的必要放大，因只依赖最小左原像强趋于 $w$，亦适用于 (3.6)。这仍不是对放大给出上界。

## 4. 首头完整左压缩的正过滤

前稿把增长头测试精确拆成首头和其余源头时，右费用可正交拆分，但两个分量的左范数未获上界。下面给一个保留小右费且左范数受控的替代分裂。

令
$$
H_0=K^{-1/2}\iota_0^*L\iota_0K^{-1/2}\succ0,
\qquad
T_\tau=\tau(H_0+\tau I)^{-1}\quad(\tau>0).
\tag{4.1}
$$
这是同一原首头上的完整左度量压缩。$T_\tau$ 是真正正自伴收缩，并且
$$
\boxed{
0\preceq T_\tau\preceq I,\qquad
T_\tau H_0T_\tau\preceq\tfrac{\tau}{4}I.}
\tag{4.2}
$$
后一式逐谱值就是 $h\tau^2/(h+\tau)^2\le\tau/4$。不需 $H_0$ 的统一上界。

在完整右零返回空间 $\ker S$ 中定义
$$
U_0h=k_{K^{-1/2}h}.
\tag{4.3}
$$
由 (1.4)，$U_0$ 是到闭子空间
$\mathscr K_0=\{k_h:h\in E_{d-1,q}\}$ 的等距映射。前稿的首段 MP 正交分解给每条完整可行链 $c$
$$
U_0U_0^*c=k_{PF_{\rm flag}c},\qquad
U_0^*c=K^{1/2}PF_{\rm flag}c.
\tag{4.4}
$$
定义完整右空间上的正自伴收缩
$$
\mathcal T_\tau=U_0T_\tau U_0^*.
\tag{4.5}
$$
它的像在原首头零返回子空间；因此下述两条链始终在同一完整旗内。

## 5. 增长头测试的双侧稳定分裂

设原增长头测试链映射为
$$
c:\mathscr Z\longrightarrow\ker S,\qquad \|c\|\le\varepsilon,
\quad f=F_{\rm flag}c,
$$
并有已付的同源左界
$$
\|E_q^\dagger f\|\le M_*
\tag{5.1}
$$
（增长头稿给 $M_*=1+\varepsilon$）。定义
$$
c_{0,\tau}=\mathcal T_\tau c,\qquad
c_{1,\tau}=(I-\mathcal T_\tau)c,\qquad
f_{j,\tau}=F_{\rm flag}c_{j,\tau}.
\tag{5.2}
$$
于是 $f=f_{0,\tau}+f_{1,\tau}$，$f_{0,\tau}$ 只在物理首源头，且
$$
Qf_{1,\tau}=Qf.
\tag{5.3}
$$
两条链不必物理正交。所用的正性足够给两个准确的行、列估计：
$$
\boxed{
c_{0,\tau}^*c_{0,\tau}+c_{1,\tau}^*c_{1,\tau}
\preceq c^*c\preceq\varepsilon^2I_{\mathscr Z},}
\tag{5.4}
$$
$$
\boxed{
c_{0,\tau}c_{0,\tau}^*+c_{1,\tau}c_{1,\tau}^*
\preceq\varepsilon^2I_{\ker S}.}
\tag{5.5}
$$
(5.4) 由 $\mathcal T_\tau^2+(I-\mathcal T_\tau)^2\preceq I$ 得到；(5.5) 先分别用 $cc^*\preceq\varepsilon^2I$，再用同一个算子不等式。因此没有把点态两范数平方和误当作伴随行算子的界。

对首头左费用，(4.1)--(4.4) 给
$$
\|E_q^\dagger f_{0,\tau}z\|^2
=\langle H_0T_\tau U_0^*cz,T_\tau U_0^*cz\rangle
\le\tfrac{\tau}{4}\varepsilon^2\|z\|^2.
$$
再用同源最小左原像的线性性，
$$
\boxed{
\|E_q^\dagger f_{0,\tau}\|\le\tfrac{\varepsilon\sqrt\tau}{2},
\qquad
\|E_q^\dagger f_{1,\tau}\|
\le M_*+\tfrac{\varepsilon\sqrt\tau}{2}.}
\tag{5.6}
$$
特别取 $\tau=\varepsilon^{-2}$，原增长头测试给
$$
\boxed{
\|E_q^\dagger f_{0,\tau}\|\le\tfrac12,\qquad
\|E_q^\dagger f_{1,\tau}\|\le\tfrac32+\varepsilon,
\qquad \|c_{j,\tau}\|\le\varepsilon.}
\tag{5.7}
$$
这是真正同时付清左上界和小右费的分裂，不使用整个原头逆范数。

## 6. 同一个实际平坦源与完整 Schur 坐标

令原完整源坐标为 $a=\Gamma_qr$、左度量为 $\mathcal G_q$。定义测试坐标
$$
S_{j,\tau}=\Gamma_qf_{j,\tau}.
$$
由同一源恒等式，对任意原 $r$，
$$
S_{j,\tau}^*\mathcal G_qa=c_{j,\tau}^*c^\flat(r).
\tag{6.1}
$$
(5.5) 因而给
$$
\boxed{
\|S_{0,\tau}^*\mathcal G_q\Gamma_qr\|^2+
\|S_{1,\tau}^*\mathcal G_q\Gamma_qr\|^2
\le\varepsilon^2\lambda_{\rm flat}(r)^2.}
\tag{6.2}
$$
同时 (5.6) 给真实受限左 Gram 上界
$$
\boxed{
S_{0,\tau}^*\mathcal G_qS_{0,\tau}
\preceq\tfrac{\tau\varepsilon^2}{4}I,\quad
S_{1,\tau}^*\mathcal G_qS_{1,\tau}
\preceq(M_*+\tfrac{\varepsilon\sqrt\tau}{2})^2I.}
\tag{6.3}
$$
首头测试的坐标像仍在前稿整条最小头对角
$$
\operatorname{Ran}S_{0,\tau}
\subseteq
\bigoplus_{t=0}^{d-2}\mathbb Ce_{t+1}\otimes K_{q-t}.
\tag{6.4}
$$
这里没有删掉任何真实尾短核阶。

必须保留过滤的边界：
$$
PF_{\rm flag}c_{1,\tau}
=K^{-1/2}(I-T_\tau)U_0^*c
\tag{6.5}
$$
一般不为零。因此 $S_{1,\tau}$ 并非纯物理首头补空间测试；不能将 (6.3) 冒称前稿未过滤 $(I-\Pi_q)S$ 的左上界。

若 $\mathbf 1_{[0,\Lambda]}(H_0)$ 是这个真实左压缩的谱投影，则未滤残量在该谱段的右归一化范数有准确界
$$
\boxed{
\|\mathbf 1_{[0,\Lambda]}(H_0)(I-T_\tau)U_0^*c\|
\le\frac{\Lambda}{\Lambda+\tau}\varepsilon.}
\tag{6.6}
$$
但尚未把这些谱段与实际低头旗或某个 primitive jet 带统一识别；这种识别需要原 $A$ 的新的分段估计。

## 7. 与已有深 jet 和远低带缩减的关系

本文的消元方向是整条物理首源头，其坐标包含所有 jet 深度。R271 的 deep-source-jet 稿是在完整源 Schur 度量中消去 $k\ge5d/8$ 的真正偏离量，仍用原同一个 $c^\flat$ 支付；前稿最后 $d/4$ 顶带的结论则控制远低 primitive 坐标的直接 Schur 耦合。三者不相同，不能把其中一个的支持结论搬到另一个上。

本文 (3.3) 与 (6.5) 明确留下实际左交叉图和未滤首头残量。下一步仍需使用原 $A_m$ 的真实头旗，控制这些残量与剩余中间 primitive 带、裸输入及增长头测试之间的共同费用。原全源或真实窄源的温和三 Gram 比较、无权 $N=M$ 与普通复 Hilbert ISP 继续开放。
