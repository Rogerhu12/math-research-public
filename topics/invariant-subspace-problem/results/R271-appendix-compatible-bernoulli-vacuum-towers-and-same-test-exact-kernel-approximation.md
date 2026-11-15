# R271 附录：同一 Bernoulli 池的精确相容真空塔、完整源短缩与实际测试的有限孔真核逼近

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文把同一个有限 Bernoulli 池条件化后平均，得到原无限连续尾中一整条精确相容的真空预像塔。所有高度使用同一个条件事件，因而逐层满足 $Dv_j=v_{j-1}$，无需把分别最小的预像强行拼接。该塔与原相干塔的完整 Gram 在同一物理源上双侧可比。将其限制到真正的 $\ker C^{L+1}$，并保留这个子空间上的完整源最小化，可把前稿的固定头一次 MP 小量升级为同一个实际 $u_g=(P_{V_Q}-P_{K_Q})i_0g_0$ 的有限孔真核逼近。

主要结论是 (4.5)、(6.1) 和 (6.5)。固定 $m$ 时，取 $L=O_m(\log x)$，得到 $\|u_g\|^2=O_m((\log x)^2/x)\|g\|^2$。这里 $m$ 依赖仍显式保留于真实头相似的物理条件数；本文不把固定头极限自动放入原 moving-$m$ 母窗口，也未关闭原全局 $N=M$。

依赖：
- [原连续尾相干列的随机池原像与准确残量](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)；
- [固定原头的完整物理 Gram 带宽与截断封口](R271-appendix-fixed-head-physical-gram-bandwidth-and-same-test-coherent-top-repair.md)；
- [同实际测试的最小相干代表](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)。

## 1. 原连续尾与同一个条件池

在原 Boolean Hilbert 空间中，取整数 $x\ge1$，记
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad
b_i=(i+1)^{-2},\qquad z_i=b_i^2,\qquad
S_y=\sum_{i\ge y}z_i.
\tag{1.1}
$$
$D$ 在完整孔层直和上有界。设
$$
\omega_r=(D^*)^r\Omega,\qquad
\sigma_r^2=(r!)^2e_r(z),\qquad
\phi_r=\frac{\omega_r}{\sigma_r^2}.
\tag{1.2}
$$
特别 $\sigma_0=1$、$\phi_0=\Omega$。

沿用随机池稿的独立 Bernoulli 子集 $\mathcal P$：
$$
t=(x+1)^{-4},\qquad p_i=z_i/t,\qquad
\mathbb P(i\in\mathcal P)=p_i.
$$
其基数 $N=|\mathcal P|$ 几乎处处有限，因为
$$
\lambda_x:=\mathbb EN=S_x/t<\infty.
$$
对任意有限整数 $L\ge1$，
$$
p_{x,L}:=\mathbb P(N\ge L)>0.
\tag{1.3}
$$
严格正性来自无限多个独立的严格正纳入概率；$p_x=1$ 不构成障碍。

对一个确定的有限池 $P$，若 $|P|=N_P\ge L$，定义
$$
v_r^P=
\frac1{(N_P)_{\underline r}}
\sum_{\substack{J\subset P\\|J|=r}}\frac{e_J}{b_J},
\qquad 0\le r\le L,
\tag{1.4}
$$
其中 $(N_P)_{\underline r}=N_P!/(N_P-r)!$，$r=0$ 时取 $v_0^P=\Omega$。直接逐坐标计数得
$$
Dv_r^P=v_{r-1}^P,\qquad 1\le r\le L.
\tag{1.5}
$$
事实上，对 $|I|=r-1$ 且 $I\subset P$，下降后的系数为
$$
\sum_{i\in P\setminus I}\frac{b_i}{b_Ib_i(N_P)_{\underline r}}
=\frac{N_P-r+1}{b_I(N_P)_{\underline r}}
=\frac1{b_I(N_P)_{\underline{r-1}}}.
$$

所有高度都对**同一个事件 $N\ge L$** 条件化。定义
$$
v_r=\mathbb E[v_r^{\mathcal P}\mid N\ge L],\qquad 0\le r\le L,
\tag{1.6}
$$
先按非负坐标理解；下面的范数界会证明它确为 Hilbert 向量，不预先假设随机向量的 Bochner 可积性。

## 2. 精确相容性与全塔统一范数

对 $|J|=r$、$r\ge1$，令 $N_{J^c}=|\mathcal P\setminus J|$。独立性给出 (1.6) 的准确坐标式
$$
(v_r)_J=
\frac{b_J}{t^r p_{x,L}}\,
\mathbb E\left[
\frac{\mathbf1_{\{N_{J^c}+r\ge L\}}}
{(N_{J^c}+r)_{\underline r}}
\right].
\tag{2.1}
$$
删除该指标事件只增大右侧。由 Beta 积分及
$\sum_{i\notin J}p_i\ge S_{x+r}/t$，
$$
\begin{aligned}
\mathbb E\frac1{(N_{J^c}+r)_{\underline r}}
&=\frac1{(r-1)!}\int_0^1
\prod_{i\notin J}(1-p_i+p_is)(1-s)^{r-1}\,ds\\
&\le \left(\frac{t}{S_{x+r}}\right)^r.
\end{aligned}
$$
因此
$$
\|v_r\|\le
\frac{\sqrt{e_r(z)}}{p_{x,L}S_{x+r}^r}.
\tag{2.2}
$$
这证明全部 $v_r$ 都在原 $\mathcal H_r$ 中。由非负项 Tonelli、(1.5) 及 $D$ 的有界性，条件平均给出真正的 Hilbert 等式
$$
\boxed{
v_0=\Omega,\qquad Dv_r=v_{r-1}\quad(1\le r\le L).
}
\tag{2.3}
$$
特别 $D^rv_r=\Omega$，所以
$$
\langle v_r,\omega_r\rangle=1,\qquad
v_r-\phi_r\perp\omega_r.
\tag{2.4}
$$

记
$$
A_{x,L}:=
p_{x,L}^{-1}\left(\frac{S_x}{S_{x+L}}\right)^L\ge1.
\tag{2.5}
$$
利用 $r!e_r(z)\le S_x^r$ 以及 $r\le L$，(2.2) 给
$$
\boxed{
1\le\sigma_r\|v_r\|\le A_{x,L},\qquad
\|v_r-\phi_r\|^2
=\|v_r\|^2-\sigma_r^{-2}
\le\frac{A_{x,L}^2-1}{\sigma_r^2}.
}
\tag{2.6}
$$
这是整个相容塔的一致预算，不是分别寻找各高度的 MP 后假定它们相容。

## 3. 明确连续尾量级

原连续尾满足
$$
\frac1{3(y+1)^3}\le S_y\le\frac1{3y^3}.
$$
取 Chernoff 参数 $\log2$，得到
$$
\mathbb P(N<L)
\le
2^{L-1}e^{-\lambda_x/2}
\le
\varepsilon_{x,L}:=
\exp\left[(L-1)\log2-\frac{x+1}{6}\right].
\tag{3.1}
$$
当 $\varepsilon_{x,L}<1$ 时，
$$
\boxed{
A_{x,L}
\le
\frac1{1-\varepsilon_{x,L}}
\left(1+\frac{L+1}{x}\right)^{3L}.
}
\tag{3.2}
$$
因此 $L=o(\sqrt x)$ 时，$A_{x,L}\to1$。若
$\varepsilon_{x,L}\le1/2$，还可直接写
$$
\boxed{
0\le1-A_{x,L}^{-2}
\le4\varepsilon_{x,L}+\frac{6L(L+1)}x.
}
\tag{3.3}
$$
证明是
$\log A_{x,L}\le2\varepsilon_{x,L}+3L(L+1)/x$
和 $1-e^{-2a}\le2a$。这里没有把全部 $L\asymp x$ 高度称为近最优；当前渐近区域准确为 $L=o(\sqrt x)$。

## 4. 真正的有限孔核及同源完整 Gram

令 $C$ 是任意与远尾作用于不同张量因子的有界算子，且 $C^h=0$。取 $1\le L<h$，定义
$$
R_La=\sum_{r=0}^L(-C)^ra\otimes\phi_r,\qquad
T_La=\sum_{r=0}^L(-C)^ra\otimes v_r,
$$
$$
H_L=R_L^*R_L=
\sum_{r=0}^L\frac{(C^*)^rC^r}{\sigma_r^2},
\qquad W_L=\ker C^{L+1}.
\tag{4.1}
$$
由 (2.3)，
$$
(C+D)T_La=(-1)^LC^{L+1}a\otimes v_L.
$$
所以
$$
T_LW_L\subset\ker(C+D).
\tag{4.2}
$$
这些向量的远孔数至多为 $L$；其位置支撑可以无限。本文的“有限孔真核”不表示有限位置支撑。

不同 $r$ 的远孔层正交；同层上 (2.4) 又给出准确交叉。因此在完整物理源上，
$$
R_L^*T_L=H_L,
$$
$$
T_L^*T_L-H_L
=\sum_{r=0}^L
\left(\|v_r\|^2-\sigma_r^{-2}\right)(C^*)^rC^r.
$$
特别
$$
\boxed{
H_L\preceq T_L^*T_L\preceq A_{x,L}^2H_L.
}
\tag{4.3}
$$
$R_L$、$T_L$ 的零孔行都是恒等，故它们在任何闭源子空间上的像均闭。

现在给定原 forcing $F=i_0g_0=g_0\otimes\Omega$，令
$$
a_L=H_L^{-1}g_0,\qquad f_L=R_La_L
=P_{\operatorname{Ran}R_L}F.
$$
令 $\iota:W_L\hookrightarrow\mathfrak h$ 为物理等距包含，并保留两个**同一 $W_L$ 上的完整压缩 Gram**
$$
H_{L,W}=\iota^*H_L\iota,\qquad
\widehat H_{L,W}=\iota^*T_L^*T_L\iota.
$$
由于它们都不小于恒等，下面的逆合法。定义
$$
p_L=R_L\iota H_{L,W}^{-1}\iota^*g_0,\qquad
k_L=T_L\iota\widehat H_{L,W}^{-1}\iota^*g_0.
\tag{4.4}
$$
两者分别是 $F$ 向 $R_LW_L$ 与 $T_LW_L$ 的真正交投影。特别 $k_L$ 是真核向量。没有把 $H_{L,W}^{-1}$ 换成 $\iota^*H_L^{-1}\iota$。

由 (4.3) 的同源合同，
$$
\boxed{
\|k_L\|^2
=\langle\widehat H_{L,W}^{-1}\iota^*g_0,\iota^*g_0\rangle
\ge A_{x,L}^{-2}\|p_L\|^2.
}
\tag{4.5}
$$
这一步保留了全部 $W_L$ 源最小化；不要求原 $a_L$ 支撑于低 grade。

## 5. 原头、原 cut 与 grade 截尾的准确费用

现在回到固定原 N 或 Y 头。置
$$
d=2^m,\quad R=x-m,\quad
C=A_m+D_<,\quad
D_<=\sum_{i=m}^{x-1}(i+1)^{-2}E_i,
\quad h=d+R,
$$
且 $g_0=g\otimes\Omega_<$。采用前稿的真实相似
$$
A_mS_m=S_mJ_m,\qquad
I\preceq S_m^*S_m\preceq\chi_mI,
$$
其中 $J_m$ 每次降一个头 grade。所有物理度量仍在
$\mathcal G=S_m^*S_m\otimes I$ 中。也可以采用任何满足相同条件的加权单降阶头；本节只使用其 grade 和物理 Gram。

写
$$
C_0=J_m+D_<,\qquad \mathcal S=S_m\otimes I,\qquad
a_L=\mathcal S a_L^0,
$$
$$
H_L^0=\sum_{r=0}^L\frac{(C_0^*)^rC_0^r}{\sigma_r^2},
\qquad b_L=(H_L^0)^{1/2}a_L^0.
$$
$H_L^0$ 严格保 total grade；$\mathcal S^*H_L\mathcal S$ 的 grade 带宽至多 $d-1$。前稿的完整 Neumann 证明给：若 $\chi_m>1$，令
$$
\rho_m=\frac{\chi_m-1}{\chi_m+1},\qquad
\nu_{m,L}=\left\lceil\frac{L-d+2}{d-1}\right\rceil.
$$
当 $L\ge d-1$ 时，
$$
\|\Pi_{\ge L+1}b_L\|^2
\le \chi_m\rho_m^{2\nu_{m,L}}\|g\|^2.
\tag{5.1}
$$

真正的 $p_L$ 使用的是 (4.4) 的完整压缩逆。仅为估计其距离，可用
$$
a_{\rm trial}=\mathcal S\Pi_{\le L}a_L^0\in W_L
$$
作合法候选，因为 $C_0$ 每次恰降一 grade。$p_L$ 的最小性、物理 Gram 比较及 (5.1) 给
$$
\begin{aligned}
\delta_L^2
&:=\|f_L-p_L\|^2\\
&=\min_{a\in W_L}\|R_L(a_L-a)\|^2\\
&\le\chi_m\|\Pi_{\ge L+1}b_L\|^2
\le\chi_m^2\rho_m^{2\nu_{m,L}}\|g\|^2.
\end{aligned}
\tag{5.2}
$$
同时 $\delta_L^2\le\|f_L\|^2\le\|g\|^2$。若 $\chi_m=1$，则对 $L\ge d-1$，$\delta_L=0$。

令 $V_Q,K_Q$ 是同一原有限头模型
$\mathcal L_m=A_m+D_{\ge m}$ 的实际左可行空间和真核，cut $Q$ 按第 $m$ 位以后的全部物理孔数计。要求
$$
Q\ge R+L.
\tag{5.3}
$$
相干截断稿的逐列低方程身份准确给
$$
P_{V_Q}f_L=P_{V_Q}F,\qquad
P_{K_Q}f_L=P_{K_Q}F.
\tag{5.4}
$$
另一方面，$T_LW_L$ 的强孔不超过 $R$、远孔不超过 $L$，且 (4.2) 是真方程，故
$$
T_LW_L\subset K_Q\subset V_Q.
\tag{5.5}
$$
这里的上包含是对本节新构造的真实核，不是把原 joined 高出生商免费嵌入真核。

## 6. 同一个实际测试的明确范数界

记原实际向量
$$
u_g=(P_{V_Q}-P_{K_Q})F.
$$
因为 $K_Q\subset V_Q$，差为正交投影。利用 (5.4)、(5.5) 和 $k_L=P_{T_LW_L}F$，
$$
\begin{aligned}
\|u_g\|^2
&=\|P_{V_Q}f_L\|^2-\|P_{K_Q}f_L\|^2\\
&\le\|f_L\|^2-\|k_L\|^2\\
&\le\|f_L\|^2-A_{x,L}^{-2}\|p_L\|^2\\
&=(1-A_{x,L}^{-2})\|f_L\|^2+A_{x,L}^{-2}\delta_L^2.
\end{aligned}
$$
于是，当 $\chi_m>1$、$d-1\le L<h$ 且 $Q\ge R+L$ 时，
$$
\boxed{
\|u_g\|^2\le
\left[
1-A_{x,L}^{-2}
+A_{x,L}^{-2}
\min\{1,\chi_m^2\rho_m^{2\nu_{m,L}}\}
\right]\|g\|^2.
}
\tag{6.1}
$$
$\chi_m=1$ 时删去方括号最后一项。这是同一个实际 $u_g$ 的界；既没有重选源，也没有把近核残量的范数直接当核距离。

若 $\varepsilon_{x,L}\le1/2$，可用稍松但更直接的式子
$$
\boxed{
\|u_g\|^2\le
\left[
\frac{6L(L+1)}x
+4\varepsilon_{x,L}
+\chi_m^2\rho_m^{2\nu_{m,L}}
\right]\|g\|^2.
}
\tag{6.2}
$$

固定 $m$，若 $\chi_m>1$，取
$$
\gamma_m=-\frac{2\log\rho_m}{d-1}>0,\qquad
L_m(x)=d+\left\lceil\frac6{\gamma_m}\log(x+1)\right\rceil.
\tag{6.3}
$$
若 $\chi_m=1$，取 $L_m(x)=d$。充分大 $x$ 时，$L_m(x)<h$、
$L_m(x)=o(\sqrt x)$，且在 $\chi_m>1$ 时
$$
\rho_m^{2\nu_{m,L_m(x)}}\le(x+1)^{-6}.
$$
因此对所有 $Q\ge R+L_m(x)$，
$$
\boxed{
\|u_g\|^2\le
\left[
\frac{6L_m(x)(L_m(x)+1)}x
+4\exp\left((L_m(x)-1)\log2-\frac{x+1}{6}\right)
+\chi_m^2(x+1)^{-6}
\right]\|g\|^2,
}
\tag{6.4}
$$
其中 $\chi_m=1$ 时最后一项可删。特别
$$
\boxed{
\sup_{\|g\|\le1}
\|(P_{V_Q}-P_{K_Q})(g\otimes\Omega_{\ge m})\|
=O_m\!\left(\frac{\log x}{\sqrt x}\right)\longrightarrow0.
}
\tag{6.5}
$$
这一次给出的是精确有限孔真核的比较，而非仅一次 MP 修正或小残量。

## 7. 移动头与原全局运输仍需共同支付的条件

全部证明在原无限连续尾和原物理内积中完成，未使用完整孔层逆的指数界。对移动 $m$，一个直接充分条件是，在同一个真实 cut 中选
$$
d-1\le L<h,\qquad Q\ge R+L,\qquad L^2/x\to0,
$$
并满足
$$
\chi_m^2\rho_m^{2\nu_{m,L}}\to0.
\tag{7.1}
$$
(6.1) 比只写“固定 $m$ 后取足够大 $x$”给出了完整参数。

这里的 $\chi_m$ 来自选定真实头相似的完整物理度量。其局部源条件可继续改善，但不能把非酉相似删去。若改用加权齐次头，只需把相应真实 $\chi_m$ 和相同带宽重新代入；不应承担没有必要的单位 Jordan 对角归一化费用，也不能预先宣称高次项相似的物理条件数已付。

此外，$K_Q$ 属于有限头模型 $\mathcal L_m$。从它运输到原全局 $T$ 的真核、原 $W$ 的正交关系及 carry 误差，仍须核对相同 $m,R,Q$ 的合法预算。本文不把 $x$ 任意增大自动视为已有 moving-$m$ 母窗口，不宣称原全局 $N=M$ 已完成。
