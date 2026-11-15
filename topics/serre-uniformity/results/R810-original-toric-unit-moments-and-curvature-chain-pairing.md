# R810 — 原 toric 线的完整单位偶矩、曲率链配对与源交换子

日期：2026-11-15。状态：**下列原有限表示中的单位矩及其边界已证明；未筛 critical 与 primitive/Legendre 同标签共同非零仍未证明。**

本篇接 [R808 原 Gram 商与 Howe 链](R808-original-cuspidal-Gram-quotient-and-Howe-chain.md)，以及下列依赖中的 FT、OP、QS。
这里的 torus 是 R808 链内部的原 phase torus；不是选择 h 的位置 torus。
不把它错误地当成与完整 heat 连接交换的投影。

## 1. 固定原 toric 线和规范

对原允许标签 h，令
$$
r=\min(h-1,p-h),\qquad 2r\le p-3.
\tag{810.1}
$$
R808 给原轨道格的非退化 Gram 商
$$
W_r=\operatorname{Sym}^{2r}(k^2)\otimes\det^{-r},
\qquad v_{\rm sp}=X_1^rY_1^r.
$$
本篇用 X_1、Y_1 表示表示变量，用 X、Y 表示辅助曲线
Y^2=X^3+16 的坐标。

保留原矩阵族
$$
T_\zeta=\left\{
\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}
\right\}/\mathbf F_p^\times,
\qquad s=\zeta-\zeta^2,\quad s^2=-3.
$$
在 covariant 约定中
$$
v_1=\zeta X_1+Y_1,\qquad v_2=\zeta^2X_1+Y_1,
\qquad w=v_1^rv_2^r=(X_1^2-X_1Y_1+Y_1^2)^r.
\tag{810.2}
$$
令 P_T=(p+1)^{-1}\sum_{t\in T_\zeta}t。
因为 2r<p+1，P_T 的像正是 kw；
在 v_1,v_2 单项式中，它就是保留平衡项的投影。
R808 的实际 split 向量满足
$$
P_Tv_{\rm sp}=s^{-r}P_r(1/s)\,w.
\tag{810.3}
$$
这仍是原 e_0、原 period basis 和原 toric 平均的像。
必须区分固定的 rank-one 线 kw 与原 period 向量的商像
u_h=s^{-r}P_r(1/s)w：当 Legendre 因子为零时，u_h 的商像为零，
并不能把它归一化成 w。本篇只对固定的基向量 w 作归一化；
只有在明确假定原 N_h 为单位的段落，才把结论移给实际 u_h。

在该对称幂中记
$$
E=X_1\partial_{Y_1},\qquad F=Y_1\partial_{X_1}.
\tag{810.4}
$$
这就是 R808 的 Howe 链中乘 uv 与 -partial_u partial_v
经其准确阶乘归一化后的算子；没有任意更换 E 或 split 向量。

## 2. 原 toric 线的完整指数矩

由 X_1=(v_1-v_2)/s，在基 v_1,v_2 中
$$
E=\frac1s\begin{pmatrix}1&1\\-1&-1\end{pmatrix}.
$$
所以在标准二维表示中
$$
\exp(tE)=
\begin{pmatrix}1+t/s&t/s\\-t/s&1-t/s\end{pmatrix},
\qquad \det\exp(tE)=1.
\tag{810.5}
$$
在 W_r 中指数的阶数至多 2r<p，
故所有指数分母均可逆，整数表示恒等式可以准确约化。
R808 使用过的平衡单项式 Legendre 恒等式给
$$
\boxed{
P_T\exp(tE)P_T
=P_r(1+2t^2/3)P_T.
}
\tag{810.6}
$$
具体地，(810.5) 的 ad+bc=1-2t^2/s^2=1+2t^2/3；
det^{-r} 因子是 1。

用
$$
P_r(1+2x)=\sum_{j=0}^r
\binom rj\binom{r+j}j x^j
$$
逐项比较，得到
$$
\boxed{
P_TE^{2j}P_T
=\frac{(2j)!}{3^j}
\binom rj\binom{r+j}j\,P_T
\quad(0\le j\le r),
}
\tag{810.7}
$$
以及
$$
P_TE^{2j+1}P_T=0.
\tag{810.8}
$$
(810.7) 的每一个系数都是 p 单位：
2j\le2r\le p-3、r+j\le2r<p，所有阶乘都严格小于 p。
尤其
$$
P_TEP_T=0,\qquad
P_TE^2P_T=\frac{2r(r+1)}3P_T.
\tag{810.9}
$$
原 h 在这里满足 r(r+1)=h(h-1) mod p，确实非零。

这些式子是所选原 toric 线上的双边矩。
没有把它们写成 E 保持这条线；(810.9) 的第一个等式与 E 不保持该线完全相容。

## 3. 一个真正非退化的整链配对

用线性功能 ell:W_r->k 定义
P_Tv=ell(v)w，故 ell(w)=1。
置 m_j=ell(E^jw)。对 0<=a,b<=2r，考虑
$$
H_{a,b}=\ell(E^{a+b}w)=m_{a+b}.
\tag{810.10}
$$
因为 E^{2r+1}=0，所有 a+b>2r 的项为零；
反对角线上的项全为
$$
m_{2r}
=\frac{((2r)!)^2}{(r!)^2\,3^r}\ne0.
\tag{810.11}
$$
沿反对角线作三角行列式计算给
$$
\det H=(-1)^r m_{2r}^{\,2r+1}\ne0.
\tag{810.12}
$$
允许标签的 r 是偶数，但不需要用这一点来证明可逆。

因此
$$
w,Ew,\ldots,E^{2r}w
$$
是一组基，且
$$
\ell,\ell E,\ldots,\ell E^{2r}
$$
是对偶空间的一组基。
当原 N_h 为单位时，(810.3) 中的系数为单位，所以原 toric 平均像
P_T v_sp 本身也有这个完整循环性。
这是一条实际原有限商上的非退化结论，不是凭维数假定某功能非零。

它需要整组观测值：
对任意 v，若 ell(E^jv)=0 对全部 0<=j<=2r 成立，则 v=0。
仅有 ell(v)=0，甚至仅有某一个中心系数为零，都不够。
例如 r>=1 时 Ew非零而 ell(Ew)=0。

## 4. 在完整八通道连接中的准确含义

保留辅助曲线的原 Hasse A、B：
$$
D^2A=-XA/4,\qquad A(P_0)=0,\qquad DA(P_0)=B\ne0.
$$
设 M_f=M_e tensor I+I tensor M_o。
在固定 h 的 R808 链中，原八通道连接是
$$
\mathcal K
=D+\frac13F-\frac{3X}{4}E-M_f.
\tag{810.13}
$$
FT、OP 给，在 P_0=(0,4) 评价其 p 曲率，
$$
\mathcal K^p|_{P_0}=3B^2E\otimes I_8.
\tag{810.14}
$$
原辅助曲线上 $D^p=0$，故 $\mathcal K^p$ 正是函数域线性的 $p$ 曲率；所以其整数次幂可以先相乘再评价。
因此 (810.7)--(810.8) 给准确的压缩式
$$
\boxed{
(P_T\otimes I_8)\mathcal K^{2jp}(P_T\otimes I_8)|_{P_0}
=(3B^2)^{2j}
\frac{(2j)!}{3^j}
\binom rj\binom{r+j}j
(P_T\otimes I_8).
}
\tag{810.15}
$$
0<=j<=r 时显示乘数都是单位。特别 j=1 的乘数是
6B^4r(r+1)。

然而 P_T 并不水平。因为 P_T 是常数矩阵，
$$
\boxed{
[\mathcal K,P_T]
=\frac13[F,P_T]-\frac{3X}{4}[E,P_T].
}
\tag{810.16}
$$
即使在 P_0，第一项仍存在。
(810.15) 不是把 K 限制到 toric 线后求幂所得的式子。
交换 $X_1,Y_1$ 保持原二次型、并把 $E$ 换成 $F$，故 (810.9) 也给 $P_TFP_T=0$。因此投影后的连接
P_T K P_T 在该线上只有 D-M_f；它的 p 曲率为零。
(810.15) 中的非零高阶矩准确经过线外的分量。
若先把线外分量丢去，便丢去了全部这个单位来源。

## 5. 原源方程必须保留的项

QS 中的原五次 lift 满足
$$
\mathcal K\widehat\Omega=\mathcal R\mathcal S,
\qquad\mathcal R=L_z^2L_t^3.
$$
位置字符投影 mathsf E_h 与 K 交换；
先取 v_h=mathsf E_h widehat Omega、
s_h=mathsf E_h mathcal R mathcal S，则
$$
\mathcal K v_h=s_h.
$$
链内再取原 toric 平均时，真正的方程是
$$
\boxed{
\mathcal K(P_Tv_h)
=P_Ts_h+[\mathcal K,P_T]v_h,
}
\tag{810.17}
$$
第二项不能删去。

此外，R808 已指出 v_h 在总次数 p-1 的中心坐标，
是原 z,t 系数经完整 Krawtchouk 变量替换后的 h 坐标。
它目前不等于原
f_i g_{N-1-i}，h=6i+7。
(810.7)--(810.15) 没有改变这个事实。
原目标仍要求同一 h 的
$$
P_{h-1}(1/s)f_i g_{N-1-i}\ne0.
$$
因此本篇所给完整单位矩，可用于一个准确整链源配对或左逆；
它本身既不证明该指定观测值非零，
也不证明原未筛 critical 乘积中必有一项非零。
没有新增有限素数扫描或重算旧数据。

## 依赖

- [R808 原 Gram 商与 Howe 链](R808-original-cuspidal-Gram-quotient-and-Howe-chain.md)：原 covariant torus、(810.3)、Howe 链及其阶乘规范。
- [FT 完整 heat 与偶源](../notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)：全部有限值通道的显式可分平凡化和零 $p$ 曲率。
- [OP 首 $p$ 振子曲率](../notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md)、[QS 水平五次 lift](../notes/2026-11-15-sigma-horizontal-quintic-lift-and-Steinberg-coefficients.md)：原振子 $p$ 曲率、水平五次 lift 及完整源方程。
- [DP 原 critical 投影障碍](../notes/2026-11-15-sigma-critical-projection-curvature-obstruction.md)：原稀疏空间上无漏出的非恒定对角筛不能水平。
