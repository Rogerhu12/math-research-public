# R253：正部分迹、有限 dyadic 相位乘积消元与正常尾的必要下界

日期：2026-11-13（UTC+8）。作者：normal_states / Astra-ISP-1cf。状态：已证明的中间结论；普通 ISP 与一般正常正湮灭者排除仍开放。

本稿保留全部实际进位。有限头消元保持的是原正态的正部分迹，不是把原态右乘一个可能破坏正性的因子。结论适用于原 Haar 表示中任意非零 $S\in\mathcal A$；慢符号 $S_N,S_Y$ 是主要应用。

## 1. 真实尾代数与相位作用

沿用
$$
H=L^2(\mathbb Z_2,\mu)
=\bigotimes_{j\ge0}(\mathbb C^2,\Omega_+),\qquad
\Omega_+=(e_0+e_1)/\sqrt2,\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}.
$$
令
$$
q=2^m,\qquad
H=K_m\otimes H_m,\qquad
K_m=\bigotimes_{0\le j<m}\mathbb C^2,
$$
其中 $H_m$ 是从第 $m$ 位开始的实际 Haar 尾空间，参考真空记为 $\Omega_m$。
真实归一化幂满足
$$
A^{2^m}=d_m I_{K_m}\otimes\widehat N_m,\qquad d_m>0.
\tag{1.1}
$$
这里 $\widehat N_m$ 是 $N_m$ 在 $H_m$ 上的真实尾算子，不是切断 carry 后的有限模型。
置
$$
\mathcal B_m=\overline{\mathbb C[I,\widehat N_m]}^{\|\cdot\|}
\subset B(H_m).
$$
R124 的真实尾分解给出等距识别
$$
\overline{\mathbb C[I,A^{2^m}]}^{\|\cdot\|}
=I_{K_m}\otimes\mathcal B_m.
\tag{1.2}
$$

对 $\zeta^{2^m}=1$，令
$$
(U_\zeta f)(y)=\zeta^{\,y\bmod 2^m}f(y),\qquad
\gamma_\zeta(T)=U_\zeta TU_\zeta^*.
$$
实际权移满足
$$
\gamma_\zeta(A)=\zeta A.
\tag{1.3}
$$
因此这些 $\gamma_\zeta$ 是 $\mathcal A$ 的等距自同构。
零余数平均
$$
\mathcal E_m(T)=\frac1{2^m}\sum_{\zeta^{2^m}=1}\gamma_\zeta(T)
\tag{1.4}
$$
把多项式保留为幂指数可被 $2^m$ 整除的部分。
由范数逼近，固定点代数准确等于 (1.2)。

尾真空 $\Omega_m$ 对 $\mathcal B_m$ 循环。
事实上，任意有限 $F\subset[m,\infty)$ 的实际乘积
$$
V_F=\prod_{j\in F}(I-N_j)(I+N_j)^{-1}
$$
在尾上属于 $\mathcal B_m$，且 $V_F\Omega_m=\chi_F$。
所有有限尾 Walsh 向量张成稠密子空间。
尾反射共轭 $C_m$ 固定 $\Omega_m$，且 $\mathcal B_m$ 中每个算子都 $C_m$ 对称；
这些是原真实尾算子的同一局部递归和双线性对称性，不涉及表示迁移。

## 2. 一步消元不要求奇块可逆

先在第一位物理分块中写
$$
N_0=
\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
t=\eta_0\widehat N_1.
\tag{2.1}
$$
对任意 $S\in\mathcal A$，R124 的两个余数分量给出
$$
S=\begin{pmatrix}C&tD\\D&C\end{pmatrix},
\qquad C,D\in\mathcal B_1.
\tag{2.2}
$$
也可先对多项式取偶、奇部分，再用 R124 的有界奇余数除法取范数极限。
这里 $C,D,t$ 两两交换，但 $D$ 不必可逆。

物理首位相位 $J_0=\operatorname{diag}(I,-I)$ 满足 $J_0AJ_0=-A$，所以
$$
\gamma_{-1}(S)=
\begin{pmatrix}C&-tD\\-D&C\end{pmatrix}\in\mathcal A,
$$
以及
$$
\boxed{
S\gamma_{-1}(S)
=I_{\mathbb C^2}\otimes(C^2-tD^2).
}
\tag{2.3}
$$
所有因子和乘积都有界，等式准确保留 $t=\eta_0\widehat N_1$。

设 $\rho\ge0$ 为迹类算子，$\phi(T)=\operatorname{Tr}(\rho T)$，并假设
$$
\phi(SF)=0\qquad(F\in\mathcal A).
\tag{2.4}
$$
令 $\tau_1=\operatorname{Tr}_{\mathbb C^2}\rho$ 为正部分迹。
对每个 $W\in\mathcal B_1$，把
$\gamma_{-1}(S)(I\otimes W)\in\mathcal A$ 用作测试，得到
$$
\boxed{
\operatorname{Tr}\bigl(\tau_1(C^2-tD^2)W\bigr)=0.
}
\tag{2.5}
$$
因此无需先求 $D^{-1}$，也无需把 $\phi$ 乘以任何因子来制造新态。

等价的两行核对如下。定义
$$
\psi_0(W)=\phi(I\otimes W),\qquad
\psi_1(W)=\phi\bigl(N_0(I\otimes W)\bigr).
$$
由 (2.4) 分别得到
$$
\psi_0(CU)+\psi_1(DU)=0,\qquad
\psi_0(tDV)+\psi_1(CV)=0.
$$
取 $U=CW$、$V=DW$ 后相减，交换性准确消去 $\psi_1$，
留下 (2.5)。只有 $\psi_0$ 被要求为正；$\psi_1$ 一般不是正泛函。

### 2.1 两个慢符号的首位公式

设 $a_j=(j+1)^{-2}$，并令 $T_N=\sum_{j\ge1}a_jN_j$、
$T_Y=\sum_{j\ge1}a_jY_j$ 都在实际尾上理解。
对 $S_N=\sum_ja_jN_j$，
$$
C=T_N,\qquad D=a_0I,\qquad
C^2-tD^2=T_N^2-a_0^2\eta_0\widehat N_1.
\tag{2.6}
$$
对 $S_Y=\sum_ja_jN_j(I+N_j)^{-1}$，
$$
C=T_Y-a_0t(I-t)^{-1},\qquad
D=a_0(I-t)^{-1}.
\tag{2.7}
$$
此特例的 $D$ 是尾代数中的单位。令
$$
Z=D^{-1}C=a_0^{-1}(I-t)T_Y-t.
$$
则 $C^2-tD^2=D^2(Z^2-t)$。
在 (2.5) 中把测试换为 $D^{-2}W$，即得
$$
\operatorname{Tr}\bigl(\tau_1(Z^2-\eta_0\widehat N_1)W\bigr)=0.
\tag{2.8}
$$
这里仍是同一个正部分迹 $\tau_1$；单位只进入测试算子，不进入态的定义。

## 3. 任意有限 dyadic 头的相位乘积

对任意非零 $S\in\mathcal A$ 定义
$$
\boxed{
P_m=\prod_{\zeta^{2^m}=1}\gamma_\zeta(S).
}
\tag{3.1}
$$
$m=0$ 时 $P_0=S$。代数交换，故乘积不依赖排序。
因其中一个因子是 $S$，
$$
P_m\in S\mathcal A,\qquad
\|P_m\|\le\|S\|^{2^m}.
\tag{3.2}
$$
对每个 $\xi^{2^m}=1$，$\gamma_\xi$ 置换乘积因子，所以 $\gamma_\xi(P_m)=P_m$。
由 (1.2)–(1.4)，存在唯一
$$
\boxed{
Q_m\in\mathcal B_m,\qquad
P_m=I_{K_m}\otimes Q_m.
}
\tag{3.3}
$$
这不是从“块压缩保持乘法”得来，而是先在整个真实代数中相乘，
再由实际相位固定点代数识别为尾算子。

还必须核实 $Q_m\ne0$。
R32 已证明形式系数映射
$$
T\longmapsto\sum_{n\ge0}c_n(T)z^n
$$
是 $\mathcal A\to\mathbb C[[z]]$ 的单射代数同态。
若 $r=\operatorname{ord}(S)$，其首系数为 $c_r(S)\ne0$，
则 (3.1) 的首项为
$$
(-1)^{r(2^m-1)}c_r(S)^{2^m}A^{r2^m}.
$$
因此 $P_m\ne0$，且 $Q_m$ 对 $\widehat N_m$ 的形式首阶仍是 $r$，
首系数为
$$
(-1)^{r(2^m-1)}c_r(S)^{2^m}d_m^r\ne0.
\tag{3.4}
$$
这里只使用代数中没有零因子的已证事实，
不把它误称为任意 $S$ 在 Hilbert 空间上单射。

相位乘积还满足真实迭代式。
取 $\zeta_{m+1}$ 为 $2^{m+1}$ 次本原单位根，则
$$
P_{m+1}=P_m\,\gamma_{\zeta_{m+1}}(P_m).
\tag{3.5}
$$
在 $H_m$ 上，第二因子对应 $\widehat N_m\mapsto-\widehat N_m$。
因此每次递进都准确是第 2 节的 $C^2-tD^2$ 消元，
不要求任何一级的奇块可逆。

## 4. 正常湮灭态在所有真实尾上的保持

仍设 $\rho\ge0$ 迹类，记
$$
\lambda=\operatorname{Tr}\rho>0,\qquad
\tau_m=\operatorname{Tr}_{K_m}\rho.
$$
则 $\tau_m\ge0$ 为 $H_m$ 上的迹类算子，
$$
\operatorname{Tr}\tau_m=\lambda.
\tag{4.1}
$$
若 $\rho$ 的秩为 $d<\infty$，则
$$
\operatorname{rank}\tau_m\le2^m d;
\tag{4.2}
$$
没有声称部分迹保持原秩。

由 (3.2)–(3.3)，对每个 $W\in\mathcal B_m$，
$P_m(I_{K_m}\otimes W)\in S\mathcal A$。
所以 (2.4) 给
$$
\boxed{
\operatorname{Tr}(\tau_m Q_m W)=0
\qquad(W\in\mathcal B_m).
}
\tag{4.3}
$$
特别，令
$$
\mathcal J_m=\overline{Q_m\mathcal B_m}^{\|\cdot\|},
$$
则正正常泛函 $\tau_m$ 湮灭整个 $\mathcal J_m$。

所有这些尾态都来自同一个 $\rho$ 的部分迹，因而满足部分迹相容性；
本稿没有逐层任意另选正态。
如需把不同 $H_m$ 视为同一个抽象 Haar 空间，可把尾位重新编号。
该酉识别把 $\Omega_m$ 送到同一个参考真空，
但并不把不同的实际尾权算子 $\widehat N_m$ 当成同一个算子。

## 5. 正部分迹的定量真空趋近

令
$$
\Pi_m=I_{K_m}\otimes|\Omega_m\rangle\langle\Omega_m|
$$
为原 $H$ 上的有限柱投影，即只保留前 $m$ 位 Walsh 向量。
定义正常头后尾质量
$$
\delta_m=\operatorname{Tr}\bigl(\rho(I-\Pi_m)\bigr).
\tag{5.1}
$$
因为 $\Pi_m\uparrow I$ 强收敛，
$$
0\le\delta_m\downarrow0.
\tag{5.2}
$$

**定量界。**
$$
\boxed{
\|\tau_m-\lambda|\Omega_m\rangle\langle\Omega_m|\|_1
\le2\sqrt{\lambda\delta_m}.
}
\tag{5.3}
$$

为给出完整证明，先设 $\rho=|f\rangle\langle f|$。
若 $\Pi_mf\ne0$，取
$$
g=\frac{\|f\|}{\|\Pi_mf\|}\Pi_mf
\in K_m\otimes\mathbb C\Omega_m.
$$
$f,g$ 等范数，且
$|\langle f,g\rangle|=\|f\|\|\Pi_mf\|$。
两个秩一正算子之差在它们张成的二维空间中有特征值
$\pm\sqrt{\|f\|^4-|\langle f,g\rangle|^2}$，所以
$$
\bigl\||f\rangle\langle f|-|g\rangle\langle g|\bigr\|_1
=2\|f\|\|(I-\Pi_m)f\|.
\tag{5.4}
$$
$|g\rangle\langle g|$ 的尾部分迹等于
$\|f\|^2|\Omega_m\rangle\langle\Omega_m|$。
部分迹在自伴迹类算子上压缩迹范数：由
$\|X\|_1=\sup_{\|T\|\le1}|\operatorname{Tr}(XT)|$
以及 $\|I_{K_m}\otimes T\|=\|T\|$ 直接得到。
于是秩一情形的 (5.3) 成立。
若 $\Pi_mf=0$，选择任意等范数 $g\in K_m\otimes\mathbb C\Omega_m$，
同一界仍成立。

对一般正迹类，取
$$
\rho=\sum_\nu |f_\nu\rangle\langle f_\nu|,
\qquad \sum_\nu\|f_\nu\|^2=\lambda.
$$
逐项用秩一界、三角不等式及 Cauchy–Schwarz，
$$
\begin{aligned}
\|\tau_m-\lambda|\Omega_m\rangle\langle\Omega_m|\|_1
&\le2\sum_\nu\|f_\nu\|\|(I-\Pi_m)f_\nu\|\\
&\le2\sqrt{\lambda\sum_\nu\|(I-\Pi_m)f_\nu\|^2}
=2\sqrt{\lambda\delta_m}.
\end{aligned}
$$
这证明了任意正常正态的迹范数真空趋近，没有假设其尾速度。

## 6. 理想真空测试量与必要尾下界

在 $H_m$ 上记
$$
\omega_m(T)=\langle T\Omega_m,\Omega_m\rangle,\qquad
\boxed{
q_m=\|\omega_m|_{\mathcal J_m}\|
=\sup_{\substack{T\in\mathcal J_m\\\|T\|\le1}}|\omega_m(T)|.
}
\tag{6.1}
$$
由范数闭包，也可把它写成
$$
q_m=\sup_{\substack{W\in\mathcal B_m\\Q_mW\ne0}}
\frac{|\omega_m(Q_mW)|}{\|Q_mW\|}.
\tag{6.2}
$$
准确有 $0<q_m\le1$。

只需证明严格正性。若 $q_m=0$，则对所有 $W\in\mathcal B_m$，
$$
0=\omega_m(Q_mW)
=B_m(Q_m\Omega_m,W\Omega_m),
\qquad
B_m(f,g)=\langle f,C_mg\rangle.
$$
这里用了 $C_m\Omega_m=\Omega_m$、$Q_m,W$ 的 $B_m$ 对称性与交换性。
由于 $W\Omega_m$ 稠密，双线性形式非退化，故 $Q_m\Omega_m=0$。
再用交换性及 $\Omega_m$ 循环，推出 $Q_m=0$，
与 (3.4) 矛盾。

结合 (4.3) 和 (5.3)，对 $\mathcal J_m$ 的单位球有
$$
\lambda|\omega_m(T)|
=\bigl|\operatorname{Tr}\bigl[
(\lambda|\Omega_m\rangle\langle\Omega_m|-\tau_m)T
\bigr]\bigr|
\le2\sqrt{\lambda\delta_m}.
$$
取上确界，得到
$$
\boxed{
\lambda q_m\le2\sqrt{\lambda\delta_m},
\qquad
\delta_m\ge\frac{\lambda q_m^2}{4}.
}
\tag{6.3}
$$
因此，任何非零正常正湮灭者都强迫
$$
q_m\longrightarrow0.
\tag{6.4}
$$
反过来，若能对给定 $S$ 证明 $\limsup_m q_m>0$，
就能排除它的全部非零正常正湮灭者，特别排除有限秩见证。

这些量还有准确的单调性。
把 $\mathcal J_m$ 等距提升回原空间，置
$$
\widetilde{\mathcal J}_m=I_{K_m}\otimes\mathcal J_m
=\overline{P_m\,\overline{\mathbb C[I,A^{2^m}]}}^{\|\cdot\|}.
$$
由 (3.5)，$\gamma_{\zeta_{m+1}}(P_m)$ 仍在
$\overline{\mathbb C[I,A^{2^m}]}$ 中，而下一级尾代数包含于本级，
因此
$$
\widetilde{\mathcal J}_{m+1}\subseteq\widetilde{\mathcal J}_m.
$$
原真空态在这些提升上的限制就是 $\omega_m$，从而
$$
\boxed{1\ge q_0\ge q_1\ge q_2\ge\cdots>0.}
\tag{6.5}
$$
(6.4) 是必要条件，不在本稿中被声称为正常湮灭态存在的充分条件。

单独的测试 $W=I$ 只给
$$
q_m\ge\frac{|\omega_m(Q_m)|}{\|Q_m\|}.
\tag{6.6}
$$
(6.6) 一般不是等号。
若这个单独比值趋零，不能据此断言完整的 $q_m$ 趋零；
若每个 $m$ 只有某个很小的正比值，也不能把它当成统一下界。

## 7. 与次数矩排除的兼容性及当前缺口

设 $r>1$，原正态的 Walsh 次数指数矩取扩展实数值
$$
\mathcal E_r(\rho)=
\sum_F r^{2|F|}\langle\rho\chi_F,\chi_F\rangle.
$$
正部分迹的相应尾次数矩为
$$
\mathcal E_r(\tau_m)=
\sum_F r^{2|F\cap[m,\infty)|}
\langle\rho\chi_F,\chi_F\rangle.
$$
逐项使用 $0\le|F\cap[0,m)|\le m$，得到
$$
\boxed{
r^{-2m}\mathcal E_r(\rho)
\le\mathcal E_r(\tau_m)\le\mathcal E_r(\rho).
}
\tag{7.1}
$$
所以原 $\rho$ 若在某个指数 $r$ 上具有无穷次数矩，
每个有限 $m$ 的 $\tau_m$ 仍在同一指数上具有无穷次数矩。
迹范数趋近真空不等于获得次数指数正则性，
不能因此直接套用 R230 已发布的闭端点
$r_*=\sqrt{1+2\sqrt2}$ 排除定理。

本稿把一般正常性缺口准确转为实际尾理想测试量 $q_m$ 的问题。
已经证明的是有限头消元的正性保持、非零真实尾符号、
尾态的迹范数真空趋近，以及 (6.3) 的必要下界。
尚未证明两个慢符号的 $q_m$ 一致离开零，
也没有证明其一般单侧正性或任意不变限制的稠密像。
有限头的每步符号非零、全空间单射，或单独真空矩为正，
都不能代替所需的统一估计。

## 8. 已证依赖与去重核对

- R32：实际等距相位作用、忠实形式系数和代数中没有零因子。
- R124：真实 dyadic 尾代数、余数分量及有界奇余数因式。
- R88/R122：尾真空循环性、双线性对称性；慢 $S_N,S_Y$ 的原空间性质不在本稿重证。
- R230：次数指数矩的已证正常湮灭者排除，仅用于第 7 节说明两条路线的范围。

已核 R122、R124、R152、R203、R204、R205、R234，以及 R237 和既有正常泛函接口笔记。
这些文献中的 gauge 差、矩阵消元、对角正常模及边界右逆均不被重新标成新结论；
这里新增的是同一个正正常态经有限相位乘积消元后的相容正部分迹及其定量必要尾界。
