# R119 续篇：真实同宽双迹 Schur 投影与完整内部 Green 核

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在同一个实际 $\Gamma^0,t_0$ 参考上，内部标签逆
$D_0^{-1}$ 与真实 $B$ 两迹传播复合后，具有同一角宽的全频界：

$$
 \boxed{\quad
 \|T_B\mathcal H D_0^{-1}g\|_{\mathfrak C_\sigma}
       <2^{42}\|g\|_{\mathfrak Z_\sigma}.
 \quad}                                                       \tag{S.1}
$$

完整零外 raw 高度 Dirichlet 的 $B$ 端 Schur 投影 norm 小于 $2^{44}$。
因此第41束的真实普通／弱源，连两条 $B$ 迹一起，也不必先支付1850标签
逆宽差。这些界包括所有非zero四重频率；真正 mean 的高度和通量仍独立处理。

本篇还给真实全域 Green 的两个齐次列和所有 weak/source 项。它将剩余
内部相对估计定位到 (S.20)--(S.21) 的完整核，而不是只留下一个未定义的
“全网络逆”。同宽 $B$ 投影不自动授予同宽内部 $C^2$ 重建。

## 1. 原全模好线与准确 $B$ 端单位

固定[第41束](R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md)
的真实参考、source 约定和符号。设 $M=|m|\ge4$，
$a_B=a(B),w_B=w(B)$，$L=\omega B$，$7/5<\omega<3/2$。
同一 R74 状态为 $Y=(y,y_u/M)^T$。实际 raw 两迹是

$$
 f_B=\frac4{a_Bw_B}(\omega y-y_u/M^2),\qquad
 k_B=\frac4{a_Bw_B}(\omega y-y_u).
                                                               \tag{S.2}
$$

所有 source 在 $B$ 之前已经停止；此处 total/bare 通量一致。
若在 nonlinear 图中使用 $Z=Z_{\rm ref}-v$，仍按第41束把高度、两迹、
标签和全部源一起翻号；下面的线性矩阵和 norm 不变。

定义实际归一向量和矩阵

$$
 x_m=(M^2f_B,Mk_B)^T
     =\frac{4M^2}{a_Bw_B}\,C_M Y,
 \qquad
 C_M=\begin{pmatrix}\omega&-1/M\\\omega/M&-1\end{pmatrix}.
                                                               \tag{S.3}
$$

准确有 $\det C_M=-\omega(1-M^{-2})$，并且

$$
 \|C_M\|_{1\to1}<2,\qquad\|C_M^{-1}\|_{1\to1}<2.
                                                               \tag{S.4}
$$

例如原矩阵最大列和不超过 $15/8$；逆的两列和分别不超过 $36/35$、
$44/35$。这同时保留高度和斜率，不因 $M$ 大而只看其中一行。

真实平尾允许线在 $B$ 的任一非zero向量记为 $Y_H$。前篇重新选择的
全模好 bump 给

$$
 \left|\sin\angle(Y_H,(1,\omega))\right|\ge2^{-39}.
                                                               \tag{S.5}
$$

这只在此处固定的 $\Gamma^0,t_0$ 使用；不把它自动转授变化参数。
齐次 unit label 的 $Y_H$ 可以极小，但 (S.5) 不依赖它的振幅。

## 2. 真长段零 Dirichlet 行及其完整夹角

写 $c_M=\coth(ML)$，则

$$
 g_m=k_B+Mc_M f_B,
 \qquad M g_m=e_Mx_m,\quad e_M=(c_M,1).
                                                               \tag{S.6}
$$

这是有限 $L$ 的准确长段行，不以 $c_M=1$ 替代。
真实 $L>24514072$ 给 $0<c_M-1<2^{-100}$。
由 (S.3)，

$$
 e_MC_M=(1+1/M)(\omega,-1)
                  +(c_M-1)(\omega,-1/M).
                                                               \tag{S.7}
$$

所以 (S.5) 与 $(\omega^2+M^{-2})^{1/2}<2$ 给

$$
 |e_MC_MY_H|
 >\left(2^{-39}-2^{-99}\right)\|Y_H\|_2
 >2^{-40}\|Y_H\|_2.
                                                               \tag{S.8}
$$

另一方面，$\|C_MY_H\|_1<2\sqrt2\|Y_H\|_2<3\|Y_H\|_2$。
对 $x_H=4M^2C_MY_H/(a_Bw_B)$，两式直接给

$$
                    \frac{\|x_H\|_1}{|e_Mx_H|}<2^{42}.
                                                               \tag{S.9}
$$

共同的极小物理尺度和单位标签振幅在同一个商中准确消去，没有分别估计
其倒数。$D_{0,m}=g_m(\mathcal H_me_m)$，故 (S.9) 正是 (S.1) 的逐模式。

## 3. 完整双迹 Schur 投影和真实 source 边界图

对任意 $B$ 两迹向量，定义完整逐模投影

$$
 \Pi_m=I-\frac{x_H e_M}{e_Mx_H}.
                                                               \tag{S.10}
$$

它准确满足 $\Pi_m^2=\Pi_m$、$\Pi_mx_H=0$ 和 $e_M\Pi_m=0$。
$\|e_M\|_{\ell^1\to\mathbb C}=c_M<2$，所以

$$
 \|I-\Pi_m\|_{1\to1}<2^{43},\qquad
                         \|\Pi_m\|_{1\to1}<2^{44}.
                                                               \tag{S.11}
$$

全部 $m$ 的同一个常数直接作用于任意 Fourier--Wiener 权
$e^{\sigma M}$。在两分量 Euclidean Sobolev norm 中只多一个 $\sqrt2$，
因此可用 $2^{45}$。这里没有截断高频，也没有换成低模理想矩阵。

令 $X^p=\mathcal Gf$ 是第41束的实际零总标签 particular，
$x^p=T_BX^p$。真正零外 raw 高度 Dirichlet 的 $B$ 状态准确是

$$
 x^{\rm reg}=\Pi x^p
 =T_B\,[\mathcal G-\mathcal H D_0^{-1}E\mathcal G]f.
                                                               \tag{S.12}
$$

对宽度不足以重建整个内部场的输入，右边先逐模定义，左边给同宽的完整
闭边界实现；第41束的强径向 Green 行极限和 Fourier 收敛仍指定同一个值。
由其 $\|x^p\|_{\mathfrak C_{s_\beta}}<2^{-431}\|f\|_{\mathcal F_\beta}$，
得到新的实际两迹合同

$$
 \boxed{\quad
 \|x^{\rm reg}\|_{\mathfrak C_{s_\beta}}
       <2^{-387}\|f\|_{\mathcal F_\beta},\qquad
 s_\beta=\beta-88823/400.
 \quad}                                                       \tag{S.13}
$$

此处 $\|x\|_{\mathfrak C_s}$ 指原定义
$\sum e^{sM}(|x_1|+|x_2|)$。普通源或完整 weak canonical 源还给
$2^{63}\|\mathcal J\|_{\mathcal S_{1,\beta}}$。
在实际 $\beta=224$，两迹都处于物理角宽 $1.9425$。
源的另一个外输出是第41束的完整 Wronskian $r(f)$；它与 (S.13) 来自
同一个源和同一允许线，不是两个可以独立指定的边界数据。

若外负荷为非zero $g$，在 (S.12) 加
$x_H M g/(e_Mx_H)$；其范数正是 (S.1)。weak 源的内部 bare 端点和
原标签仍按第41束的 $Q,\ell(Q)$ 恢复，不能借此投影删除它们。

## 4. 真实全域 Green 的两列：外 Wronskian 准确为 $-1$

下面使用物理 raw 高度和同向总通量状态 $Z=(h,\pi)^T$。
源只在 mixed tail，homogeneous 参考在整个 tail、connector、bump 和长段
是同一个可逆方程。令 $q$ 是前篇 grounded 外归一 $(v,p)=(1,-\gamma_m)$
的真实平尾解。先记其物理 raw 外高度为 $b_m=q_h(t_o)$。
R74 的准确两迹转换给

$$
 b_m=1+\frac{(A_0-4\omega)(\gamma_m/M^2-1/A_0)}{1-M^{-2}},
 \qquad 1-2^{-35}<b_m<1.
                                                               \tag{S.14a}
$$

这里 $0<A_0-4\omega<2^{-34}$、$M/7<\gamma_m<M/5$、$A_0<6.01$；
例如括号的绝对值小于 $1/4$，再除 $1-M^{-2}\ge15/16$ 即得所示界。
令 $v$ 是 raw 外初值 $(h,p_h)=(0,-1/b_m)$ 的另一齐次解。
后者只作为核的伴随列，不称它满足平端条件。
不能用 grounded 外高度为0替换此条件，因为实际长段 $f_*=0$ 指 raw
竖直高度为0。这个区别在极小尺度上仍必须准确保留。

由 R74 与 raw 的两个准确 determinant，第41束 (E.17)--(E.18) 给

$$
                    W(q,v):=q_hv_p-q_pv_h=-1
                                                               \tag{S.14}
$$

在整个实际径向区间准确不变。不存在一个还要估计的非zero标量分母。
条件数会出现在两个真实列的大小，不能因 (S.14) 就宣称它们小。

源约定为 $\operatorname{div}(G_0\nabla h)=s-\operatorname{div}F$，
$G_0=\operatorname{diag}(\mu,\mu A)$、$\mu=w/a$，总通量
$\pi=\mu h_t+F^t$。于是对第 $m$ 模

$$
 Z_t=\begin{pmatrix}0&\mu^{-1}\\\mu A m^2&0\end{pmatrix}Z
       +J_m,\qquad
 J_m=\binom{-F_m^t/\mu}{s_m-imF_m^\theta}.
                                                               \tag{S.15}
$$

写 $[z,J]=z_hJ_p-z_pJ_h$。满足平端允许条件和外零 Dirichlet 条件的
准确全域 Green 是

$$
 \boxed{\quad
 Z(t)=-q(t)\int_t^{t_o}[v(s),J_m(s)]ds
       -v(t)\int_{t_f}^{t}[q(s),J_m(s)]ds.
 \quad}                                                       \tag{S.16}
$$

对原 source 空间中已经有完整 realization 的输入，积分是该解的表示；
对于一般输入，必须先验证这些积分及所得内部 norm，不能由 (S.13) 猜测。
有限支持/有限 Fourier 时由常数变易直接证明：以 $(q,v)$ 为基，
两系数导数为 $[v,J]$ 和 $-[q,J]$；取外端第一系数0、平端第二系数0
即得 (S.16)。第41束已有 realization 的数据再按真实 Green 行极限传递。

在外端 $q$ 的系数为0，因为 $b_m\ne0$ 而 $v_h(t_o)=0$。
又 $W_{\rm grounded}(q,v)=1$，即 $p_v+\gamma_m v_v=1$，所以 $v$ 的系数
$-\int[q,J]$ 仍准确等于前篇 (E.20) 的外 affine 通量。在内部，另一列
$v$ 及其积分也真实存在于公式中，不能只保外端的 $q$ 配对。

## 5. 长段造成的指数在 $B$ 的完整双列框架中准确相消

上述真实 raw 外初值给

$$
 Y_v(0)=\left(\frac1{(M^2-1)b_m},
                  \frac{\omega M}{(M^2-1)b_m}\right)^T,
 \qquad b_m>31/32,
 \quad\|Y_v(0)\|_2<2/M.
                                                               \tag{S.17}
$$

长段准确 transfer 是
$\left(\begin{smallmatrix}\cosh(M\omega u)&\sinh(M\omega u)/\omega\\
\omega\sinh(M\omega u)&\cosh(M\omega u)\end{smallmatrix}\right)$，
Euclidean norm 小于 $2e^{M\omega u}$，故
$\|Y_v(B)\|_2<4e^{ML}/M$。
前篇 $\|Y_q(B)\|_2<2^{42}e^{-ML}$ 同时保留。

令 $d_M=1-M^{-2}$，$\widehat Y=(4Md_M)^{1/2}Y$，
$\lambda_M=e^{ML}/\sqrt M$。则同一个实际完整 $B$ 框架

$$
 \mathcal Z_{B,m}
    =(\lambda_M\widehat Y_q(B),\lambda_M^{-1}\widehat Y_v(B))
$$

准确满足

$$
 \det\mathcal Z_{B,m}=1,
 \quad\|\mathcal Z_{B,m}\|_2<2^{44},
 \quad\|\mathcal Z_{B,m}^{-1}\|_2<2^{44}.
                                                               \tag{S.18}
$$

两列的各自界是 $2^{43}$ 和8；二维 determinant 为1时，两个奇异值互为
倒数，给逆的同一个界。这里使用的是实际 $q,v$，不是两个形式增长/衰减
指数。$\lambda_M$ 的输入列重标度已明确显示；与角频率混合的 source 或
扰动复合时，仍须保留这两个 Fourier 乘子，不能因为 (S.18) 的常数统一
就删除其共轭。

## 6. Mean、weak 荷和 source 的完整保留

mean 不使用 (S.3) 中的除 $M$ 公式。物理 raw mean 准确满足

$$
 \pi_0(t)=\int_{t_f}^{t}s_0(u)du,\qquad
 h_0(t)=\rho\lambda+
                  \int_{t_f}^{t}\frac{\pi_0-F^t_0}{\mu}du.
                                                               \tag{S.19}
$$

指定外 mean 高度时，只用第二式确定唯一 $\lambda$；总 mean flux
$\pi_0(t_o)=\int s_0$ 仍是输出。它是否满足实际 holonomy 条件，仍须消费
完整 metric/source 行，而非由此强制清零。

所有非mean weak 源在 (S.15)--(S.16) 中的实际配对都是
$z_h(s_m-imF^\theta_m)+(z_h)_tF^t_m$。这与前篇的完整 canonical 两行
完全相同，不包含未支付的 $\partial_tF^t$。
在任意有弱端荷的切口先使用总状态，最后恢复
$p^{\rm bare}=\pi-F^t$；source norm 本身若不授 $F^t$ 的端点迹，就不能
断言恢复后的 bare 端口有界。普通、weak、mean 和 metric 列都遵循此规则。

## 7. 实际相对估计现在需要支付的精确核

在同一个物理 $(t,\theta)$ 中，真实非zero背景的 raw Jacobi 主部已经有
完整散度形式，见[真实 density 证明的 (S.5)](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)。
在全部类型上，它的同一个公式是
$G_a=(w_{\rm ref}/a)JD^{-3/2}(1,-d;-d,d^2+A v^2)$，
$d=E(V-P)/J$、$v=\sqrt D/J$；在根处也没有除 $A$。
写它为 $\operatorname{div}((G_0+\Delta G_a)\nabla h)$。
把差移到右边就是本篇的真实 weak source

$$
 F=\Delta G_a\nabla h,\qquad s=0,
 \quad
 J_{a,m}(h)=
 \binom{-(\Delta G_a\nabla h)^t_m/\mu}
       {-im(\Delta G_a\nabla h)^\theta_m}.
                                                               \tag{S.20}
$$

参数、固定角图或原 source 带来的额外 ordinary 与 weak 列另以同一
(S.15) 加入，不在此主差中藏掉。
于是整个已固定参考的内部相对作用准确是

$$
 \mathcal K_a h(t)=
 -q(t)\int_t^{t_o}[v,J_a(h)]ds
 -v(t)\int_{t_f}^{t}[q,J_a(h)]ds.
                                                               \tag{S.21}
$$

将其取各实际离散端口、执行原规范、并恢复 bare 荷后，就是第41束
$[\mathcal G-\mathcal H D_0^{-1}E\mathcal G]\delta\mathcal L_a$
的同一个算子。它的外 $B$ 两迹已经由 (S.13) 控制；内部同权范数仍要
逐项支付两个真齐次列的乘积、真实 Fourier 混合及全部转向框架。

正段的完整 DN diagonal shear 可以先实施，随后的源须保留该 shear
产生的 height/flux 列；两端恢复按第40束与第41束 (E.28) 进行。
这些代数步骤没有任何 $P_{+-}^{-1}$，但也没有仅由局部酉差或
$\sum 2^{240000}N_j\|X\|$ 自动得到 (S.21) 的小范数。
这就是当前继续计算的具体全网络门。

## 8. 必要核算

`scripts/fourfold_actual_boundary_Schur_Green_20261113.py` 检查两个真实
trace 矩阵、完整投影、有限长段初值、Hamiltonian 常数变易的两列及全部
新数字费。报告为
`notes/2026-11-13-R119-actual-boundary-Schur-Green-budget.json`。
无限 Fourier 和源域的结论由上述统一逐模界及第41束的真实 Green 极限证明。
