# R271 第一附录：平方头升级的准确局部不变量与旧头单块修正

日期：2026-11-13（UTC）。作者：boundary_resume_1cf；Astra-ISP-1cf8c51d 复核。
状态：以下实际有限头及纯尾结论已证明；不新增无权核内饱和或普通 ISP 结论。

本稿接 [R271](../results/R271-increasing-head-actual-lift-and-log-four-thirds-stable-range.md) 的平方模型逐头提升，并与 [R239 原线性单块残量](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md) 区分。
后者已处理原线性头、准确修复 Gram 和有限头交换子迹障碍。
这里新增平方矩阵多项式的两个局部不变量及其实际核含义，随后把平方修正准确限制在一个旧头块。
没有将线性结论重新计作新增范围。

## 1. 同一个原位号下的平方矩阵多项式

采用 R254/R271 删除原首位后的图尾记号。
旧头含图尾位 $0,\ldots,m-1$，$d=2^m$；$C_m$ 是真实加权后移的 $d$ 维压缩，
$A_m$ 是对应的慢 $N$ 或 $Y$ 头，$b_j=(j+2)^{-2}$，$\eta=e^{-1070}$。
$C_m$ 是一条非退化加权 $d$ 链，$A_m$ 是 $C_m$ 的无常数多项式。
本稿令
$$
\mathsf P_m(z)=
\begin{cases}
(A_m+zI)^2-\eta C_m,&N\text{ 型},\\
(A_m+zI)^2-\eta C_m(I+A_m+zI)^2,&Y\text{ 型}.
\end{cases}
\tag{1.1}
$$
它是有限矩阵多项式。若以原纯尾 $D_m=\sum_{j\ge m}b_jE_j$ 代入，
便是 R271 的实际混合平方算子 $P_m$；$Y$ 型已经乘去原可逆分母。

固定新尾
$$
D=D_{m+1}=\sum_{j\ge m+1}b_jE_j.
$$
旧模型中仍留在尾内的第 $m$ 位是纯删除 $E_m$，故在这一位的
$|0\rangle,|1\rangle$ 分块下，旧模型准确为
$$
\boxed{
\mathsf P_m(D+b_mE_m)
=
\begin{pmatrix}
\mathsf P_m(D)&b_m\mathsf P'_m(D)\\
0&\mathsf P_m(D)
\end{pmatrix}.
}
\tag{1.2}
$$
这里只用 $E_m^2=0$ 及它与旧头、新尾交换；没有改变 $b_j$ 的物理编号。

真实新头则满足
$$
C_{m+1}=
\begin{pmatrix}C_m&K_m^C\\0&C_m\end{pmatrix},\qquad
A_{m+1}=
\begin{pmatrix}A_m&b_mI+K_m^A\\0&A_m\end{pmatrix},
\tag{1.3}
$$
其中
$$
K_m^C=\frac{\alpha_{m+1}}{\alpha_1}\,e_{d-1}e_0^*.
$$
第二式由每个真实 $\bar N_j$ 的跨最高位递推和 Cayley 块逆得到；
它与 R239 单块式同构，但系数在本稿始终为图尾的 $(j+2)^{-2}$。
$K_m^A$ 保留全部实际进位。不能假设它与 $A_m$ 或 $C_m$ 交换。

记真实新模型的上角块为 $U_m(z)$，则
$$
\boxed{
\mathsf P_{m+1}(z)=
\begin{pmatrix}
\mathsf P_m(z)&U_m(z)\\
0&\mathsf P_m(z)
\end{pmatrix}.
}
\tag{1.4}
$$

## 2. 每个平方头只有一个非单位局部因子

在解析芽环 $\mathbb C\{z\}$ 中，以左右可逆解析矩阵作为等价变换。
两型都准确满足
$$
\det\mathsf P_m(z)=z^{2d}.
\tag{2.1}
$$
因为在加权后移的标准基中，$C_m,A_m$ 严格上三角，(1.1) 的每个对角元都是 $z^2$。

另一方面，
$$
\mathsf P_m(0)=C_m[-\eta I+C_mG_m(C_m)]
\tag{2.2}
$$
其中 $G_m$ 是有限多项式。方括号可逆，故
$$
\operatorname{rank}\mathsf P_m(0)=d-1.
\tag{2.3}
$$
特别，无需任何范数近似就有某个 $(d-1)$ 阶子式在零点不为零。

取该子式作高斯消元：解析行列变换先将其化为 $I_{d-1}$，再消掉其余同行同列。
剩余一个解析标量的行列式由 (2.1) 确定为 $z^{2d}$ 乘解析单位。
最后吸收该单位，即得到实际可逆解析芽矩阵 $L_m,V_m$，使
$$
\boxed{
L_m(z)\mathsf P_m(z)V_m(z)
=\operatorname{diag}(I_{d-1},z^{2d}).
}
\tag{2.4}
$$
这给出了本稿所用的局部 Smith 型，证明只用了单位子式消元。
把 $m$ 换成 $m+1$，同理有
$$
\boxed{
\mathsf P_{m+1}(z)\sim
\operatorname{diag}(I_{2d-1},z^{4d}).
}
\tag{2.5}
$$

## 3. 旧模型跨一位后的两个幂准确为 2d−1 与 2d+1

对任意解析矩阵芽 $F(z)$，定义
$$
\mathcal J_b(F)=
\begin{pmatrix}F&bF'\\0&F\end{pmatrix},
\qquad b\ne0.
$$
Leibniz 公式给
$$
\mathcal J_b(FG)=\mathcal J_b(F)\mathcal J_b(G).
\tag{3.1}
$$
所以解析单位送成解析单位，且
$\mathcal J_b(F)^{-1}=\mathcal J_b(F^{-1})$。

把 (2.4) 送入该同态，并作常数置换，将同一对角坐标的两个副本排在一起。
旧模型因而等价于 $I_{2d-2}$ 加上
$$
\begin{pmatrix}
z^{2d}&2db_m z^{2d-1}\\
0&z^{2d}
\end{pmatrix}
=
z^{2d-1}
\begin{pmatrix}z&2db_m\\0&z\end{pmatrix}.
\tag{3.2}
$$
右侧内矩阵有非零常数单位 $2db_m$。
交换列、用它消掉同行同列、再吸收非零常数，准确得到
$\operatorname{diag}(1,z^2)$。因此
$$
\boxed{
\mathcal J_{b_m}(\mathsf P_m)(z)
\sim
\operatorname{diag}(I_{2d-2},z^{2d-1},z^{2d+1}).
}
\tag{3.3}
$$

(2.5) 与 (3.3) 的行列式阶数相同，都是 $4d$，但局部因子不同。
特别旧矩阵在 $z=0$ 的秩为 $2d-2$，新矩阵的秩为 $2d-1$。
故不存在在零点可逆的解析左右矩阵 $L(z),V(z)$，使
$$
L(z)\mathcal J_{b_m}(\mathsf P_m)(z)V(z)
=\mathsf P_{m+1}(z).
\tag{3.4}
$$
相似是左右等价的特例，也被排除。
极小进位仍改变了准确局部不变量，不能仅因范数很小而把它消去。

## 4. 这些解析等价确实能在原纯尾上求值

纯删除 $D=\sum_{j\ge m+1}b_jE_j$ 有界且拟幂零。
为见后者，将它拆成有限头纯删除和任意小范数的余尾；
二者交换，有限部分幂零，故谱半径不超过余尾范数，令余尾趋零即可。

因此每个在零点解析的标量芽 $f(z)=\sum f_nz^n$ 都可以在 $D$ 上按算子范数求和：
其系数至多指数增长，而 $\|D^n\|^{1/n}\to0$。
矩阵芽逐项同样成立。解析单位及其解析逆相乘仍为单位，故 (2.4)、(2.5)、(3.3)
在原头张量原纯尾上成为实际有界等价，不是形式相似。

令 $K_{\rm old}$、$K_{\rm new}$ 分别为 (1.2)、(1.4) 代入 $D$ 的核。
对应的右解析单位给有界可逆坐标，准确识别
$$
\boxed{
K_{\rm old}\simeq
\ker D^{2d-1}\oplus\ker D^{2d+1},
\qquad
K_{\rm new}\simeq\ker D^{4d}.
}
\tag{4.1}
$$
这些坐标均与 $D$ 交换；单位坐标的核为零。

该区别不只存在于形式环。
例如选择 $4d-1$ 个新尾位组成 $F$，则
$$
D^{4d-1}|F\rangle=(4d-1)!\prod_{j\in F}b_j\,|\varnothing\rangle\ne0,
\qquad D^{4d}|F\rangle=0.
$$
所以 $D|_{K_{\rm new}}$ 的幂零阶准确为 $4d$；
同理由 (4.1) 知旧核上的幂零阶准确为 $2d+1$。
于是甚至不存在一个满射线性交织 $W:K_{\rm old}\to K_{\rm new}$，
满足 $WD|_{K_{\rm old}}=D|_{K_{\rm new}}W$。
更一般，任何与 $D$ 交织的有界 $W$ 都满足 $D^{2d+1}W=0$，其像落在新核内 $\ker D^{2d+1}$ 这一真闭子空间，不能有稠密像。
这不排除不与纯尾交换的实际修正；R271 的相容原像恰不具这种交换性。

## 5. 每个固定混合模型核确有有限孔核心

对任意 $s$，$\ker D^s$ 是按纯尾孔次数分级的：
$$
D^sP_{\le Q}=P_{\le Q-s}D^s.
$$
故有限孔截断在该核中收敛到恒等。
每个解析矩阵单位 $V(D)$ 只含删除幂，因而把有限孔向量送到有限孔向量。
由 (4.1) 得
$$
\overline{K_{\rm old}\cap\bigcup_Q\mathcal H_{\le Q}}
=K_{\rm old},
\qquad
\overline{K_{\rm new}\cap\bigcup_Q\mathcal H_{\le Q}}
=K_{\rm new}.
\tag{5.1}
$$

同一结论在每个固定正指数孔范数中也成立。
若 $\mathcal N_{\rm tail}$ 数新尾孔，则在有限孔上
$$
e^{c\mathcal N_{\rm tail}}V(D)e^{-c\mathcal N_{\rm tail}}
=V(e^{-c}D).
$$
右侧及其逆仍为有界解析求值，故 $V(D)$ 双向保持
$\operatorname{Dom}e^{c\mathcal N_{\rm tail}}$，并给该范数的有界同构。
再用纯幂核的有限孔截断，得到对应加权核心。

这里 $m,c$ 均固定，没有给随头长变化的统一坐标范数。
(5.1) 只是混合模型核内部的核心；真实核是 $P$ 的核，不能由
$\|P-P_m\|\to0$ 自动把这些核心运输到它。

## 6. 平方残量也只在一个旧头块中

令 $Z=A_m+zI$、$F=K_m^A$、$K=K_m^C$，并定义
$$
\Delta_m(z)=U_m(z)-b_m\mathsf P'_m(z).
$$
按 (1.1)、(1.3) 的真实块乘法，两型分别给
$$
\Delta_m(z)=ZF+FZ-\eta K\qquad(N),
\tag{6.1}
$$
$$
\Delta_m(z)=ZF+FZ
-\eta C_m[(I+Z)F+F(I+Z)]
-\eta K(I+Z)^2\qquad(Y).
\tag{6.2}
$$
全部乘序保留；例如没有将 $A_mF+FA_m$ 改为 $2A_mF$。
每个式子只在 $z$ 中至多二次，并与新纯尾 $D$ 交换。

若 $k=(x,y)\in K_{\rm old}$，底块满足
$$
\mathsf P_m(D)y=0.
$$
所以新模型的实际残量为
$$
\boxed{
r=(\Delta_m(D)y,0).
}
\tag{6.3}
$$
由 (2.4) 的实际求值，$D^{2d}y=0$，故
$$
\boxed{D^{2d}r=0.}
\tag{6.4}
$$
这比从整个旧核直接取得的 $D^{2d+1}$ 粗界少一阶，并保留旧 $d$ 维头。

## 7. 修正只须旧 d 头的相容平方逆

设 $m\ge4$，输入的新尾孔数至多为 $Q$。
写
$$
\mathsf P_m(D)=D^2+Q_m(D),\qquad Q_m(D)^d=0,\quad [Q_m(D),D]=0.
$$
这里 $Q_m(D)$ 的全部头系数严格上三角。
同一真实标量预算给
$$
\|Q_m(D)\|\le4/9+(25/9)\eta<1/2;
$$
新尾删除较小，仍满足旧头与纯尾范数和小于 $2/3$ 的界。

在纯尾位 $j\ge m+1$ 上使用 R254J 的同一相容族
$DR_t=R_{t-1}$，最大原像阶只需 $2d$。
可取放宽参数
$$
L=512\sqrt{Q+2d+1}(m+Q+2d+3)^{3/2}.
$$
令
$$
\mathcal G_{m,Q}
=\sum_{\ell=0}^{d-1}(-Q_m(D))^\ell R_{2\ell+2}.
$$
准确望远镜给
$$
\mathsf P_m(D)\mathcal G_{m,Q}=I
$$
于已声明的有限源层，不要求 $Q_m(D)$ 与各 $R_t$ 交换。
取
$$
c=(\mathcal G_{m,Q}\Delta_m(D)y,0).
\tag{7.1}
$$
由 (1.4)、(6.3)，
$$
\boxed{\mathsf P_{m+1}(D)(k-c)=0.}
\tag{7.2}
$$
底块 $y$ 完全保持；修正最多增加 $2d$ 次新尾孔，不必使用整个新 $2d$ 头的 $4d$ 项范围。

(6.4) 和 R254J 的实际受限范数界还给
$$
\boxed{
\|c\|\le d(2L)^{4d-1}\|\Delta_m(D)y\|
\le72\eta_m\,d(2L)^{4d-1}\|y\|.
}
\tag{7.3}
$$
第二步沿用 R271 的真实两层误差 $72\eta_m$；这里的 $\eta_m$ 是原物理比率。
所有界仍保留固定有限源次数 $Q$，不称全 Hilbert 右逆。
(7.3) 改进的是一步平方修正的头范围，未证明对所有 $Q$ 一致的小代价。

## 8. 尚未关闭的量词

局部 Smith 型准确解释旧核的 $2d+1$ 阶运输与新核的 $4d$ 阶重置，
并排除零点正则的有限头左右等价。
实际解析演算给固定混合模型的有限孔核心；
特殊进位又允许只用旧平方头修正一个块。

但这些结论没有控制原真实核的最小修复能量，
没有证明 R239 全整数倒数能量级数发散，也未证明无权 $N=M$。
非解析头尾修正以及完整链 Gram 的真实 Schur 补仍需继续研究。
