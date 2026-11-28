# 全负区真实矩阵变形的物理傅里叶算子范数

固定原内禀参数 $\eta_0$、实 $|\delta|\le10^{-8}$，物理角周期 $l=\pi/2$，归一角测度 $d\phi/l$。令 $n=4|j|$，$P$ 可取真 $X,\Phi_+,\Phi_-$ 中任一提升。对任意 $S\subset\{|j|\ge97\}$，任意二维复向量输入，及原全负区的每个 $r$，有
$$
 \left\|\sum_{j\in S}e^{4ijP(\phi)} n^2(B_j-H^{-1}_{\operatorname{sgn}j})(r,\phi)f_j\right\|_{L^2_\phi}
 \le {1\over4500}\|f\|_{\ell^2(S)},                                      \tag{BPF.1}
$$
算子范数本身严格小于 $1/4500$。全输出均值和低频均包含在此范数中。将左边视为同一输入对应的径向函数，其 $L^2(dr;L^2_\phi)$ 算子范数小于 $1/315000$，$L^1(dr;L^2_\phi)$ 算子范数小于 $1/22500000$。

## 真支撑内的二次径向因子

记 $R=1/50,L=1/2000$, $y=T_\phi,x=X_\phi$, $D=x^2+Ty^2$。由 [GDG.5–11](R133-supplement-complete-global-genuine-determinant-from-supported-potential.md) 支撑闭包含于 $\rho=r_*-r\le R$，该处 $-T=\rho A^{2/3}, A>4$。当 $-T\le L$ 时，
$$
 \rho\le L/A^{2/3}<1/5000=R/100,
 \qquad (5/2)^3<4^2.                                                \tag{BPF.2}
$$
在 [M.5–8](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md) 的有序积分中，把 $|X_{\phi\phi}(s\rho)|$ 按 $D_2s\rho e^{3D_1R}$ 付费，共同漂移角导按 $e^{D_1R}$ 付费，$\frac32\int_0^1s^{3/2}ds=3/5$。故 $A_\phi$ 的界留一个 $\rho$，$T_\phi$ 留两个。已登记整域 $B_T<7/1000$ 即用于 $T_\phi$ 的 M.8 正系数乘完整长度平方，原不确定根长度上界至少是 $R$。在任何含支撑点的径向圆上，全部角均有
$$
 |y|\le(7/1000)(\rho/R)^2\le Y=7/10^7,
 \quad p=P_\phi>79/80,\quad D>D_0=977/1000,
 \quad \|H_\epsilon^{-1}\|_\Sigma<H_0=21/10 .                    \tag{BPF.3}
$$
这里 $\|\cdot\|_\Sigma$ 是完整矩阵各条目模之和。两真分支角导下界见原整域角导门，平均给 $X$。在其余径向圆 $B_j-H^{-1}_\epsilon=0$。各原接缝按两侧真实值接收。[原完整过程与归一](R133-supplement-actual-piecewise-root-radius-one-over-fifty-and-full-seams.md)

## 按真势的共同物理水平集接收所有频率

令 $z_j=j^{-2}$，$T_c=\max(-L,T)$。在 $[-L,0]$，同一原势对所有 $z_j$ 满足 $|V|<M=276$, $|V_T|<M_1=26431$。原最大域的共同坐标像半径严格大于 $L$。[原 A.5、A.8](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)

对于每个整数 $k\ge1$，
$$
 V(z_j,T_c)^k=V(z_j,-L)^k+
     \int_{-L}^0 {\bf1}_{\{T_c(\phi)>t\}}\,\partial_t[V(z_j,t)^k]dt .
                                                                        \tag{BPF.4}
$$
右端每个 $t$ 对所有输入标签使用同一个物理乘子。先在真实频率空间作对角乘，再用同一个 $C_P:f\mapsto f\circ P$，最后左乘指示函数。直接换元给 $\|C_P\|\le\sqrt{80/79}<101/100$。于是对应振幅 $V(z_j,T_c)^k$ 的算子范数至多
$$
 {101\over100}\,[ M^k+L k M^{k-1}M_1 ] .                            \tag{BPF.5}
$$
此序允许各 $z_j$ 任意依赖 $j$。同样容许在输入右乘任意频率对角，其费用为上确界。证明先取有限输入，再对实际范数稠密延拓。

[GDG.19](R133-supplement-complete-global-genuine-determinant-from-supported-potential.md) 对原真实矩阵给以下逐频收敛展开，$\chi=\chi_V(T)$、$\lambda=n^{-2}$：
$$
 n^2(B_j-H_\epsilon^{-1})=
 \sum_{m\ge0}{y\over D}(yH_\epsilon^{-1}-E_{12})
        (y^2/D)^m\chi^{m+1}\lambda^m V(z_j,T_c)^{m+1}.               \tag{BPF.6}
$$
其共同物理左乘子中，将 $H_\epsilon^{-1}=H_e+\epsilon H_o$ 分开，$H_e,H_o$ 仅依赖 $r,\phi$。这两个矩阵由 $H_+^{-1}$、$H_-^{-1}$ 的平均与半差得到，各自完整条目和至多 $H_0$。符号 $\epsilon$ 保留在输入对角。因为 $0\le\chi\le1$，有限项按 (BPF.5) 在物理 $L^2$ 接收后可按范数求和。记 $u=MY^2/(388^2D_0)<10^{-12}$；总费用严格小于
$$
 {101\over100}\,{Y(1+2Y H_0)\over D_0}
    \left({M\over1-u}+{L M_1\over(1-u)^2}\right)<{1\over4500}.     \tag{BPF.7}
$$
最后一式只需 $Y=7/10^7,D_0=977/1000,H_0=21/10$ 及上述整数；也可逐因子用 $101/100$, $1+2YH_0<1001/1000$, $1/D_0<103/100$, 括号 $<290$ 相乘。支撑径向长度 $<1/5000$ 且 $70^2<5000$，即得两种积分范数。各处为保原 $j=\pm|j|$ 的整块算子估计。

对 $n\ge N\ge388$ 的输入，若将原 $n^2$ 除回，则该矩阵变形从物理 $H^{-4/3}$ 到 $L^2$ 的费用至多
$$
 {1\over4500}N^{-2/3}(1+N^{-2})^{2/3}.                              \tag{BPF.8}
$$
对 $N=262144=64^3$，此量小于 $1/18000000$。这是该真实矩阵因子在物理角内的费用。其余 Airy 列、前后强迫振幅、非局部原圈重构、非零界面、均值和正区回馈仍按各自源接收；本项没有给整个 waist 映射赋此数值。
