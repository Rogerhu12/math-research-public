# 原加权交换发生器的统一扇形形式、全阶热平滑与同顶部配对

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 结论及实际模型

沿用[保原下降算子的加权交换 resolvent 稿](R271-appendix-commuting-weighted-exchange-resolvent-and-same-source-paired-regularization.md)的原连续远尾
$$
D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad x\ge1,
$$
及其同一物理硬核空间。记 $U_i$ 为相邻两位的酉交换，
$$
P_i^-=\frac{I-U_i}{2},\qquad
\theta_i=\log\frac{i+2}{i+1},\qquad
H_i=n_{i+1}-n_i,
$$
$$
S_i=e^{\theta_iH_i},\qquad V_i=S_iU_iS_i^{-1}.
$$
原稿已证明 $V_iD_x=D_xV_i$。发生器在每个固定远孔层 $\mathcal H_n$ 上定义为
$$
\mathcal L_{x,n}=\sum_{i\ge x}(I-V_i),\qquad
\|\mathcal L_{x,n}\|\le10n,
$$
再取闭直和 $\mathcal L_x=\bigoplus_n\mathcal L_{x,n}$；其自然域为
$\{v:\sum_n\|\mathcal L_{x,n}v_n\|^2<\infty\}$。全直和通常无界。

本文证明
$$
\boxed{
\mathcal T_x=e^{-x\mathcal L_x/4},\qquad
\|\mathcal T_x\|\le e^{1/2},\qquad
\|\mathcal L_x^k\mathcal T_x\|
\le e^{3/2}k!\left(\frac8x\right)^k
\quad(k\ge0).
}
\tag{0.1}
$$
这里所有阶数均使用同一个 $\mathcal T_x$，其自身范数不随 $k$ 或 head 高度增长。特别，$\operatorname{Ran}\mathcal T_x\subset\bigcap_k\operatorname{Dom}\mathcal L_x^k$。

$\mathcal T_x$ 与原 $D_x$、独立实际 head $C$、远孔及总尾孔 cut 对易；它保持所有 $\ker D_x^r$ 和实际 head 旗，但不声称与正交核投影或 MP 对易。$\mathcal T_x,\mathcal T_x^*$ 在原物理空间同时强趋 $I$。

该平滑可放入原同一个 $u_Q$ 的完整两端 partial 配对。本文仍不证明非正交返回算子 $\mathscr A_n\mathcal T_x$ 的预算。

## 1. 一个统一的真实扇形形式

在单占据空间上 $H_iU_i$ 是反自伴算子，在 $00,11$ 上为零；它只交换 $U_i$ 的正、负谱子空间。准确有
$$
I-V_i
=2P_i^--(\cosh2\theta_i-1)U_iP_{i,\mathrm{one}}
-\sinh(2\theta_i)H_iU_i.
\tag{1.1}
$$
因而
$$
|\operatorname{Im}\langle(I-V_i)v,v\rangle|
\le2\sinh(2\theta_i)\|P_i^-v\|\,\|v\|.
\tag{1.2}
$$
对有限边和先用 Cauchy--Schwarz，再延拓到固定层及自然闭形式域，得
$$
|\operatorname{Im}\langle\mathcal L_xv,v\rangle|
\le2a_x^{1/2}\mathfrak e_x(v)^{1/2}\|v\|,
\quad
a_x=\sum_{i\ge x}\sinh^2(2\theta_i),
\quad
\mathfrak e_x(v)=\sum_{i\ge x}\|P_i^-v\|^2.
\tag{1.3}
$$
设 $t=(i+1)^{-1}\le1/2$。直接计算
$$
\sinh(2\log(1+t))\le2t,
\qquad
\sinh(\log(1+t))\le t.
$$
第一式等价于 $(1-t^2)^2\le1$，在此范围成立。因此
$$
a_x\le\frac4x,\qquad
\epsilon_x:=\sum_i(\cosh2\theta_i-1)\le\frac2x.
\tag{1.4}
$$
原稿的实部界为
$$
\operatorname{Re}\langle\mathcal L_xv,v\rangle
\ge2\mathfrak e_x(v)-\epsilon_x\|v\|^2.
\tag{1.5}
$$
于是令
$$
\mathcal A_x=\mathcal L_x+\frac4xI,
$$
则
$$
\operatorname{Re}\langle\mathcal A_xv,v\rangle
\ge2\mathfrak e_x(v)+\frac2x\|v\|^2
\ge\frac4{\sqrt x}\mathfrak e_x(v)^{1/2}\|v\|
\ge|\operatorname{Im}\langle\mathcal A_xv,v\rangle|.
\tag{1.6}
$$
所以每层真实算子的 numerical range 都落在角度 $\pi/4$ 的右扇形，常数与孔数无关。这不是由一般非自伴相似的环境条件数得到的估计。

## 2. 直接构造半群和全部导数，不借全直和有界性

固定一层，$\mathcal A_{x,n}$ 有界。若 $|\arg z|\le\pi/4$，由 (1.6)
$$
\operatorname{Re}\langle z\mathcal A_{x,n}v,v\rangle\ge0.
$$
对 $s\mapsto e^{-sz\mathcal A_{x,n}}v$ 求范数平方导数，得到
$$
\|e^{-z\mathcal A_{x,n}}\|\le1.
\tag{2.1}
$$
这给各层共同的 holomorphic 扇形界；其直和因此在扇形内部构成有界强全纯算子族。

实时间上，(1.5) 同样直接给
$$
\|e^{-t\mathcal L_{x,n}}\|\le e^{\epsilon_xt}
\le e^{2t/x}.
\tag{2.2}
$$
令 $\tau=x/4$，即得 $\|\mathcal T_x\|\le e^{1/2}$。

取复圆 $|z-\tau|=\tau/2$。该圆满足 $|\arg z|\le\pi/6<\pi/4$，且 $\operatorname{Re}z\le3\tau/2$。由 (2.1)
$$
\|e^{-z\mathcal L_{x,n}}\|
=e^{4\operatorname{Re}z/x}\|e^{-z\mathcal A_{x,n}}\|
\le e^{3/2}.
$$
Cauchy 导数公式遂给
$$
\|\mathcal L_{x,n}^k e^{-\tau\mathcal L_{x,n}}\|
\le e^{3/2}k!\left(\frac2\tau\right)^k
=e^{3/2}k!\left(\frac8x\right)^k.
\tag{2.3}
$$
所有常数不依赖 $n$，故取直和得到 (0.1) 及全部自然域结论。这里没有把固定层的 $10n$ 估计当作全空间算子范数。

## 3. 交换能量及完整正交 jet 行

从 (1.5)，对 $z=\mathcal T_xv$ 使用 (0.1) 的 $k=1$ 和 (2.2)，得
$$
\begin{aligned}
2\mathfrak e_x(z)
&\le\|\mathcal L_xz\|\,\|z\|+\frac2x\|z\|^2\\
&\le\frac{8e^2+2e}{x}\|v\|^2.
\end{aligned}
$$
即
$$
\boxed{\mathfrak e_x(\mathcal T_xv)
\le\frac{4e^2+e}{x}\|v\|^2.}
\tag{3.1}
$$
同理，对 $z=\mathcal L_x^k\mathcal T_xv$ 结合相邻两阶 (0.1)，可得
$\mathfrak e_x(z)\le C_kx^{-2k-1}\|v\|^2$，其中一个明确选择是
$$
C_k=\frac12\bigl(c_kc_{k+1}+2c_k^2\bigr),
\qquad c_k=e^{3/2}k!8^k.
\tag{3.2}
$$

令 $F_r=P_{\ker D_x^r}-P_{\ker D_x^{r-1}}$。由已付[整条正交 jet 旗交换行引理](R271-appendix-complete-orthogonal-jet-flag-preserves-fixed-test-exchange-row-budget.md)，对任意 $z$
$$
\left(\sum_r\|P_i^-F_rz\|^2\right)^{1/2}
\le\|P_i^-z\|+4\theta_i\|z\|.
$$
故 (3.1)、$\sum\theta_i^2\le1/x$ 给
$$
\boxed{
\sum_{i\ge x,r\ge1}\|P_i^-F_r\mathcal T_xv\|^2
\le\frac{(\sqrt{4e^2+e}+4e^{1/2})^2}{x}\|v\|^2
<\frac{160}{x}\|v\|^2.
}
\tag{3.3}
$$
这些都是完整行界；对任意实际输出孔带 $F$ 代入 $v=Fu_Q$，右边保留 $\|Fu_Q\|^2$，不另乘 $Q$、$h$ 或带宽。

## 4. 原下降、真实旗及原物理强极限

固定层恒等式
$$
D_x\mathcal L_{x,n}=\mathcal L_{x,n-1}D_x
$$
由有限支撑核心延拓为有界恒等式，故与其整个指数函数相容。这给
$$
D_x\mathcal T_x=\mathcal T_xD_x.
$$
同样，独立 head 算子 $C$ 以及全部物理孔 cut 与 $\mathcal T_x$ 对易。因此原左右方程、head 旗、$\ker D_x^r$、源及有限封口均保持。这里只说不变子空间，不说正交旗投影或 MP 交换。

任何固定有限物理向量在充分大的 $x$ 后属于远尾真空层，此层上 $\mathcal L_x=\mathcal L_x^*=0$。所以该向量被 $\mathcal T_x,\mathcal T_x^*$ 精确固定。利用 (2.2) 的统一界与有限物理支撑稠密性，
$$
\mathcal T_x\to I,\qquad\mathcal T_x^*\to I
\quad\text{在原物理空间强收敛}.
\tag{4.1}
$$

## 5. 同一实际 $u_Q$ 的两端 partial 与 paired commutator

固定原已付母窗口中的
$$
u=u_Q=(P_{V_Q}-P_{K_Q})w,\qquad
C=A_m+D_<,\quad C^h=0,\quad x=m+R.
$$
对全部合法 cut $p$ 保 $p+h+R<Q$。记
$$
\mathcal P_{n,j}
=D_n^\dagger D_{n-1}^\dagger\cdots D_{n-j+1}^\dagger D^j.
$$
原普通右链 $c_{p,j}=-\mathcal P_{p+j,j}u_{p+j}$ 满足真实首源、全部右方程和 $c_{p,h}=0$。由 §4，$\mathcal T_xc_{p,j}$ 是同一平滑源 $\mathcal T_xCu_p$ 的合法链。

从该同一源重新取顺次 MP 得到
$-\mathcal P_{p+j,j}\mathcal T_xu_{p+j}$。两链之差是源为零、支撑 $p+1,\ldots,p+h$ 的真正完整 kernel，属于同一 $K_Q$，故与实际 $u$ 正交。于是准确有
$$
\sum_{j=1}^h
\langle u_{p+j},
(\mathcal T_x\mathcal P_{p+j,j}
-\mathcal P_{p+j,j}\mathcal T_x)u_{p+j}\rangle=0.
\tag{5.1}
$$
没有声称两个算子对易。

拼接平滑的同一左 prefix 与负右链，再对 $p=a,\ldots,b$ 求和，得到
$$
\begin{aligned}
\sum_{p=a}^b\langle P_{\le p}u,\mathcal T_xP_{\le p}u\rangle
&=-\sum_{n=a+1}^{b+h}
\langle u_n,\mathcal T_x\mathscr A_nu_n\rangle\\
&=-\sum_{n=a+1}^{b+h}
\langle u_n,\mathscr A_n\mathcal T_xu_n\rangle,
\end{aligned}
\tag{5.2}
$$
其中
$$
\mathscr A_n=
\sum_{\substack{1\le j\le h\\a\le n-j\le b}}\mathcal P_{n,j}.
$$
两个 endpoint partial 原样保留。所有自然域与真实 head 旗同前述 resolvent 稿 §5；$\mathcal T_x$ 不改变物理孔支撑。

由原 late-cut 一致逼近 $P_{\le p}u_Q\to w$、(4.1) 和 $\|\mathcal T_x\|\le e^{1/2}$，对非零 $w$，(5.2) 每个左配对的实部对充分大 $m$ 至少为 $\|w\|^2/2$。这不需要任何未知尾速率。

## 6. 准确剩余目标

同一实际 future 端点现在具有所有发生器导数的统一小量 (0.1)，同时保完整交换行 (3.3)、原同源身份 (5.2) 和非零左锚。它比逐次施加 resolvent 的 $2^k$ 环境范数更强。

尚未证明
$$
-\operatorname{Re}\sum_n
\langle u_n,\mathcal T_x\mathscr A_nu_n\rangle
\le c_mQ\|Fu_Q\|^2.
$$
特别，扇形形式与全阶平滑没有自动控制非正交返回，不能删除 $\mathscr A_n$ 的真实 MP/完整旗，也不能把保持旗升级成正交旗交换。后续仍需对这个同源混合二次型支付真实连续权预算。
