# R542：同一快速 ruling 控制族的完整第二总矩负号与恢复时长门

日期：2026-11-16。**原式纸面证明；没有执行数值、符号、profile、矩阵秩或新科学任务。**

本稿在 R540 已经固定的三十三行母、同一个 $\chi$、同一真实常态前缀及同一个合法 scalar 盒中，核算尚未支付的另一个原八矩坐标。结果是严格的：R536 的净负 $p_1^{\omega_c}$ 与 R540 的真实 $k>2$ 可以同时成立，但该构造的原 $t_1$ 以及固定中心坐标 $t_1^{\omega_c}$ 的**全部累计仍严格为负**。增加有限短脉冲的幅度、细分脉冲或进一步压缩时间都不能消掉这个负号。

这只是当前完整快速控制族的障碍，不是同一母所有可能路径的普遍不可达定理。若允许真正较长的实际轨道，其正静态贡献可能改变结论；本稿给出它必须支付的准确时长和高度速度能量，而不预先宣布该轨道可由同一个 ruling 方程实现。

来源：[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R524](R524-same-gauge-constant-return-gates-and-real-matrix-excursion-obstructions.md)、[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)、[R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)、[R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)。

## 1. 两个坐标均为原八矩的固定线性读出

继续固定 $\omega_c>0$，不沿路径改变中心。记
$$
\eta=\omega-\omega_c,\qquad d_c=h\eta-k,\qquad
a=h_s/h.
$$
原 R73 的 $p$ 列及 $B_2$ 一次系数准确给
$$
p_1=-k(h\omega-k),\qquad p_2=-kh/2,
$$
$$
8t_1=2hk\omega-k^2-1-a^2.
\tag{1}
$$
因此固定的两个线性坐标是
$$
p_1^{\omega_c}=p_1-2\omega_cp_2=-kd_c,
\qquad
t_1^{\omega_c}=t_1+\frac{\omega_c}{2}p_2.
\tag{2}
$$
它们逐点满足
$$
\boxed{
8t_1^{\omega_c}=2hk\eta-k^2-1-a^2
=k^2+2kd_c-1-a^2,
}
\tag{3}
$$
以及
$$
8t_1^{\omega_c}+2p_1^{\omega_c}=k^2-1-a^2.
\tag{4}
$$
(1)–(4)是 R73/R524 已付身份，本稿不把重写这些身份算作新的符号计算。新的内容是将其用于 R536/R540 的**完整实际路径和全部前缀费用**。

对任意真实时刻 $s$，定义累计
$$
\mathcal T(s)=\int_{s_{\rm initial}}^s t_1\,d\sigma,\qquad
\mathcal T_c(s)=\int_{s_{\rm initial}}^s t_1^{\omega_c}\,d\sigma.
\tag{5}
$$
全 $M=0$ 必使两者为零。只有一个局部密度为正，或只在新一段重置积分，并不能支付(5)。

## 2. R540 进入正支以前已有固定的负欠额

R536 的真实常态前缀长度为
$$
t_0=L^{-2},
\qquad (h,k,\omega)=(h_c,0,\omega_c).
$$
这段 $a=k=\eta=0$，所以原两个密度准确相同：
$$
t_1=t_1^{\omega_c}=-1/8.
$$
其完整贡献为
$$
\mathcal T_{\rm prefix}=\mathcal T_{c,\rm prefix}=-t_0/8.
\tag{6}
$$
没有用 $q_j(A_c)=0$ 或全相位 ruling 将这个二阶基准删去。三个 $q_j$ 支付的是原第四方程，原 $M_{\rm raw}$ 仍在累计。

在 R536 的固定有限缩放回路、平滑过渡和负保持中，真实
$$
h\asymp h_c,\qquad k=O(L^3),\qquad\eta=O(L^3).
\tag{7}
$$
这里 $\varepsilon$ 和该稿保持时长已经先固定。故
$$
2hk\eta-k^2-1\le-1/2,\qquad
2hk\omega-k^2-1\le-1/2
\tag{8}
$$
对足够小的同一个有限 $L$ 成立。任意真实高度速度只通过额外的 $-a^2$ 进入(1)(3)，所以这些段的两个密度均严格负；不需要其速度小。

R540 的选支下降段也保持 $k,\eta=O(L^3)$、$h=h_c+O(\sqrt L)$，因而仍满足(8)。虽然它的高度速度为 $O(L^{-3/2})$，这只进一步减小两个密度。该段全部真实 $m,T$ 继续恢复，不影响(1)(3)的逐点性。

记 $\mathfrak e$ 为 R540 已完成真实 $X>0$ 接入的时刻。于是得到
$$
\boxed{
\mathcal T(\mathfrak e)\le-t_0/8,\qquad
\mathcal T_c(\mathfrak e)\le-t_0/8.
}
\tag{9}
$$
事实上后继非恒段还给严格额外负值；下文只需(9)这个保守界。

## 3. 有限合法盒中任意后继的完整账

沿 R540 的同一固定盒 $\mathcal B$ 定义
$$
q(S)=2hk\omega-k^2-1,\qquad
q_c(S)=2hk\eta-k^2-1.
$$
令
$$
Q=\max\{0,\sup_{\mathcal B}q\},\qquad
Q_c=\max\{0,\sup_{\mathcal B}q_c\}.
\tag{10}
$$
它们是有限常数，只依已固定的 scalar 盒。此处不需要计算其数值，也不把它们当成由真实 ruling 自由实现的静态状态。

取从 $\mathfrak e$ 出发的任意一条真实后继，记实际长度为 $T>0$，并置
$$
\mathcal E_h=\int_{\mathfrak e}^{\mathfrak e+T}(h_s/h)^2\,ds.
\tag{11}
$$
只要 scalar 留在 $\mathcal B$，积分原(1)(3)就给完整的准确式和上界：
$$
8\mathcal T_{\rm final}
=8\mathcal T(\mathfrak e)+\int q(S)\,ds-\mathcal E_h
\le-t_0+QT-\mathcal E_h,
$$
$$
\boxed{
8\mathcal T_{c,\rm final}
=8\mathcal T_c(\mathfrak e)+\int q_c(S)\,ds-\mathcal E_h
\le-t_0+Q_cT-\mathcal E_h.
}
\tag{12}
$$
这是同一起点到终点的总量，不是后继段的增量符号。

## 4. R540 全部有限短脉冲都不能清掉该总矩

R540 的 $p_1^{\omega_c}$ 负余量具有
$$
0<\mathfrak n'_L=O(L^7).
\tag{13}
$$
这里 R536 的非恒部分为 $L^3/t_0^2=L^7$ 乘一个先固定的有限缩放积分；选支下降段只再加 $O(L^8)$。这一上界不要求重新算任何 profile 或新积分。

该稿为了保留负累计，选所有大速度平台及平滑过渡的真实总长度
$$
T<\frac{\mathfrak n'_L}{2(C'_p+1)}.
\tag{14}
$$
因此 $T=O(L^7)$，而常态前缀的负欠额为 $t_0=L^{-2}$。$Q,Q_c$ 在母初选前选定的同一盒中固定。对充分小的同一个有限 $L$，
$$
QT<t_0/2,\qquad Q_cT<t_0/2.
$$
式(12)立即给
$$
\boxed{
\mathcal T_{\rm final}<-t_0/16<0,\qquad
\mathcal T_{c,\rm final}<-t_0/16<0.
}
\tag{15}
$$

这是对 R540 使用的整个控制族的完整结论：步骤数可以是任意有限数，平台正幅可以逐次任意增大，全部实际 $m,T$ 可以很大；只要后继仍在同一盒内并保(14)，(15)都成立。无需假设 $\mathsf H_{22}$ 或 null 高度分量 $b$ 的符号，也无需用 principal 近似任何原密度。

特别，R540 已准确到达 $k>2$ 不与(15)冲突。大曲率只改变(10)中的有限正静态项，有限短时间不能支付(6)的长前缀欠额，高度速度平方还只会增加欠额。因此该整条实际路径不是 $M=0$。

## 5. 真实归零必须支付的时长和高度变化

式(12)也给一个适用于本入端的明确恢复门。

若 $Q_c=0$，则任何仍留在 $\mathcal B$ 的正时长后继都不能使
$\mathcal T_{c,\rm final}\ge0$。若 $Q_c>0$，则达到非负必须满足
$$
\boxed{
Q_cT\ge -8\mathcal T_c(\mathfrak e)+\mathcal E_h
\ge t_0+\mathcal E_h.
}
\tag{16}
$$
原 $t_1$ 同样必须满足
$$
QT\ge-8\mathcal T(\mathfrak e)+\mathcal E_h.
\tag{17}
$$
这是必要条件，不授予这些长度上的同规范 ruling 解存在。

还可以保实际端高度而加强(16)。由 Cauchy，
$$
\mathcal E_h
\ge\frac1T\left(\log\frac{h_{\rm final}}{h(\mathfrak e)}\right)^2.
\tag{18}
$$
令
$$
D_c=-8\mathcal T_c(\mathfrak e)>0,\qquad
v_h=\left|\log\frac{h_{\rm final}}{h(\mathfrak e)}\right|.
$$
若 $Q_c>0$，则
$$
\boxed{
T\ge
\frac{D_c+\sqrt{D_c^2+4Q_cv_h^2}}{2Q_c}.
}
\tag{19}
$$
若想保整个中间高度变化，而不只是两端，可将 $v_h$ 换成实际总变差
$\int|h_s/h|\,ds$，同一 Cauchy 仍成立。对于 R540 某条非恒高度参考弧的足够精确 scalar shadow，也可仅取有限几个真实采样时刻的对数高度变化下界；无需声称 shadow 的全部导数接近。

这解释了两个不同障碍：即使高度不变，也至少要支付一个与真实前缀欠额同阶的实际时长；若依靠快速高度变化控制几何，还要额外支付(18)的不可删能量。把幅度送大不会改善这个下界。

## 6. 不能从全 history null 图推出慢归零段

R533 的正则速度图对全部有限 $m$ 成立，R540 也已真实进入同一 $X>0$ 支；这些收据并没有自动支付(16)所需的慢轨道。

例如欲从某个实际状态准确取 $h_s=0$，完整方程须满足
$$
\mathsf H_{22}(S)\delta^2+\mathsf l_\delta(S,m)\delta+
\mathsf c_\nu(S,m)=0.
\tag{20}
$$
这里保全部真实 $m$ 与同一个固定 $\nu$。若 $\mathsf H_{22}\ne0$，需检查完整
$$
\mathscr D=\mathsf l_\delta^2-4\mathsf H_{22}\mathsf c_\nu
$$
以及所取根的实际 $X>0$ 坐标；不能由 $\det\mathsf H<0$ 推出(20)必有实根。即使入端有一个非退化根，也还须沿真实 $m_s=M_{\rm raw}$ 证明它存在到(16)要求的有限时长。

本节只是标明下一真实控制对象，不把(20)写成新增已付的正向段，也不以另一份母或另一份 Gram 的正 $t_1$ 收据替代它。

## 7. 已闭范围

同一个 R533/R536/R540 圆和同一个 $\chi$ 已有净负
$p_1^{\omega_c}$ 与 $k>2$ 的实际路径。本稿完整证明：其余坐标中，原 $t_1$ 和固定中心的 $t_1^{\omega_c}$ 总值仍严格负；继续使用同一有界、任意有限高幅、总时间为 $O(L^7)$ 的快速脉冲族不能使它们归零。

原八矩、第三 history 和全路径基准在每一步都保留。结论排除的是这一具体快速配平策略，不排除另一个真正有足够实际时长且满足同一完整 ruling 的后继。取得这样的后继并同时保其它矩、末 germ 和位姿，仍是下一实际问题。

