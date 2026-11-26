# R213：切向残差的完整兼容算子及真实法向修正入口

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**状态：下列恒等式、等价判据和弱必要条件已证明；未声称当前候选满足可解性或已得到精确闭族。**
本文接 R112 的三分量切向修复，给出其未消部分对应的真实法向方程。
这不是再次更换 least-squares 权重；它指出何种残差必须由改变像集的自由度消去。

## 1. 固定目标及完整复 Fourier 模

在材料环带取

$$g=ds^2+f(s)^2du^2,\qquad f>0,\qquad q=f'/f.$$

在目标正交标架中写实际度量误差
$B=\left(\begin{smallmatrix}e&z\\z&\gamma\end{smallmatrix}\right)$。
下文 $e_k,z_k,\gamma_k$ 是 $e^{iku}$ 的复系数，实场满足共轭条件。
材料字段 $v=a\partial_s+b\partial_u$ 的第 $k$ 模为 $(A_k,B_k)$。
R112 的完整三式是

$$e_k+2A_k'=0,\tag{1}$$
$$z_k+fB_k'+ikA_k/f=0,\tag{2}$$
$$\gamma_k+2qA_k+2ikB_k=0.\tag{3}$$

这里 $B_k$ 是角位移系数，不能与误差矩阵 $B$ 混淆。
所有等式可在一个光滑径向片上经典理解，也可按其分布意义使用；
下面的除法判据只用于明确证明分母不为零的片。

令

$$D_k=k^2+ff''-(f')^2=k^2+f^2q',$$
$$N_k=ikfz_k-\tfrac12 f^2\gamma_k'+\tfrac12ff'e_k.\tag{4}$$

### 命题 1：非零模式的准确消元

设 $k\ne0$ 且在所考察闭区间上 $D_k\ne0$。则 (1)–(3) 有解当且仅当

$$\boxed{2\left(N_k/D_k\right)'+e_k=0.}\tag{5}$$

若要求位移在某端点或某开领上为零，还须在相同位置满足

$$N_k/D_k=0,\qquad \gamma_k+2qN_k/D_k=0.\tag{6}$$

解唯一，且为

$$A_k=N_k/D_k,\qquad
B_k=-\frac{\gamma_k+2qA_k}{2ik}.\tag{7}$$

**证明。** 由 (3) 解出 $B_k$，微分后代入 (2)，再用 (1) 中
$A_k'=-e_k/2$，得到 $D_kA_k=N_k$。这给必要性及唯一性。
反向令 (7) 定义字段，则 (3) 恒成立，(5) 给 (1)；将同一消元倒序代回即给 (2)。
端点零值准确等价于 (6)，没有丢掉角位移的端值。
若要求在开领恒零，(6) 必须在整个开领成立；仅两个端点值不够。证毕。

对 R112 的实奇偶模式
$e=E\cos ku,z=Z\sin ku,\gamma=G\cos ku$，
实版本为 $N=kfZ-f^2G'/2+ff'E/2$。不能在复版本中删掉 $i$。

在 $D_k=0$ 处，正确必要关系仍是 $D_kA_k=N_k$，此时必须先检查 $N_k=0$；
本文既不在那里除法，也不据此宣称有或没有穿越解。

### 零模式

$k=0$ 时，选定左端常量 $A_0(s_0),B_0(s_0)$ 后解只能是

$$A_0(s)=A_0(s_0)-\tfrac12\int_{s_0}^s e_0,
\quad B_0(s)=B_0(s_0)-\int_{s_0}^s z_0/f,$$

并必须处处满足 $\gamma_0+2qA_0=0$。
两端都固定时还须有 $\int e_0=0$ 和 $\int z_0/f=0$。
这保留独立 mean；不能把 $k\ne0$ 的除法公式代入零模。

## 2. 不微分数值误差的弱检验

强式 (5) 会微分 $\gamma_k$ 两次，不适合直接对浮点残差作差分。
以下给出等价消元所导出的稳定弱必要条件。

先取实奇偶模式，令 $\chi$ 为某个 $D_k\ne0$ 光滑径向片内紧支撑的实函数。
定义

$$\psi=f^2\chi'/D_k,$$
$$T_1=\frac{q\psi-\chi}{kf},\qquad
T_2=\frac{\psi}{f^2},\qquad
T_3=\frac{\psi'}{kf}.\tag{8}$$

则对任意足够正则的实字段 $(A,C)$，

$$\int f\{T_1(2A')+2T_2(fC'-kA/f)
 +T_3(2qA+2kC)\}\,ds=0.\tag{9}$$

**证明。** 两次一阶分部积分后，$2A$ 和 $2C$ 的系数分别是

$$-(fT_1)'+f'T_3-kT_2,
\qquad -(f^2T_2)'+kfT_3.$$

第二式由 (8) 立即为零。第一式乘 $k$ 为

$$-(q\psi-\chi)'+q\psi'-k^2\psi/f^2
=\chi'-(q'+k^2/f^2)\psi=0.$$

紧支撑消去全部边界项。证毕。

因此若试图只用切向重标消掉残差，必须有

$$\boxed{b_\chi:=\int f(T_1E+2T_2Z+T_3G)\,ds=0.}\tag{10}$$

该积分只用原误差值，不微分它；$f,D_k,\chi$ 的导数来自已固定的解析目标和测试函数。
可把 $\chi$ 选在现有样条的单个光滑片内部，故这不向全曲面附加 $C^3$ 完成标准。
令完整测试张量
$\mathsf T(s,u)=\left(\begin{smallmatrix}T_1(s)\cos ku&T_2(s)\sin ku\\T_2(s)\sin ku&T_3(s)\cos ku\end{smallmatrix}\right)$。
任意实际切向修复后的完整线性残差 $R(s,u)$ 还满足明确下界

$$\sup_{s,u}\|R(s,u)\|_{\rm op}\ge
\frac{\pi|b_\chi|}
{\int f(s)\int_0^{2\pi}\|\mathsf T(s,u)\|_*\,du\,ds}.
\tag{11}$$

其中 $\|\mathsf T\|_*$ 为两个特征值绝对值之和，
$E,Z,G$ 分别是 $R_{11}$ 的 cosine、$R_{12}$ 的 sine、$R_{22}$ 的 cosine 实幅度。
证明是角正交性和 (9) 给配对恰等于 $\pi b_\chi$，再逐点使用
$|\operatorname{tr}(\mathsf TR)|\le\|\mathsf T\|_*\|R\|_{\rm op}$ 并积分。
特别地，保留完整角积分避免将 Fourier 系数矩阵的范数误作实际场的上确界。
这只限制一阶切向修复；对有限微分同胚，须再扣除 R112 已给出的真实非线性余项，
不能将 (11) 原样称为任意有限重标的下界。

## 3. 真正法向位移进入同一个兼容条件

本节先在**准确** $X^*e=g$ 的参考浸入处推导。取法向 $n$，约定
$II_{ij}=\langle X_{ij},n\rangle$，在目标正交标架中写

$$II=\begin{pmatrix}\ell&m\\m&\nu\end{pmatrix}.$$

法向变分 $W=wn$ 的一阶度量变化是 $-2wII$。
事实上 $\langle X_i,n\rangle=0$ 微分给
$\langle X_i,n_j\rangle=-II_{ij}$，而 $w_i n$ 与 $X_j$ 正交。
故完整切向—法向线性修复方程为

$$B+\mathcal L_vg-2wII=0.\tag{12}$$

若参考 $II$ 随角度变化，乘积的第 $k$ 模必须用**完整卷积**。
令

$$\widetilde e_k=e_k-2(\ell w)_k,\quad
\widetilde z_k=z_k-2(mw)_k,\quad
\widetilde\gamma_k=\gamma_k-2(\nu w)_k.$$

将这三式代入命题 1 得

$$\widetilde N_k=N_k-2ikf(mw)_k
+f^2((\nu w)_k)'-ff'(\ell w)_k,\tag{13}$$
$$\boxed{2(\widetilde N_k/D_k)'
+e_k-2(\ell w)_k=0.}\tag{14}$$

再按 (7) 恢复全部切向字段，并检查 (6)、零模、开领和所有接缝。
这给出一个有实际法向未知量的闭合线性系统，不能把 $m$ 项或卷积高模删掉后声称同一系统。

### 旋转参考的单模方程

若 $\ell,\nu$ 只依赖 $s$ 且 $m=0$，准确 Codazzi 方程是

$$\nu'=q(\ell-\nu).\tag{15}$$

由此 (13) 化为
$\widetilde N_k=N_k+f^2\nu(w_k'-qw_k)$，因此法向方程恰为

$$\boxed{
\left[\frac{f^2\nu}{D_k}(w_k'-qw_k)\right]'
-\ell w_k=-\frac{e_k}{2}-\left(\frac{N_k}{D_k}\right)'.}
\tag{16}$$

这包含全部一阶项，尤其不能删去 $-qw_k$。
在 $\nu=0$ 的平坦或退化端仍保持未除法的式 (13)–(14)；
本文不以形式二阶方程绕过退化端口。

对实函数 $a(s,u)$ 明确定义实幅度
$\mathcal C_k(a)=\pi^{-1}\int_0^{2\pi}a\cos ku\,du=2\operatorname{Re}(a_k)$、
$\mathcal S_k(a)=\pi^{-1}\int_0^{2\pi}a\sin ku\,du=-2\operatorname{Im}(a_k)$。
对 (12) 与 (8) 的实应力配对，还得到直接作用于法向未知量的弱条件

$$2\int f\{T_1\mathcal C_k(\ell w)+2T_2\mathcal S_k(mw)
 +T_3\mathcal C_k(\nu w)\}\,ds=b_\chi.\tag{17}$$

等价地，$2\int f\int_0^{2\pi}w\operatorname{tr}(\mathsf TII)\,du\,ds=\pi b_\chi$。
这里不能把 (13)–(14) 的复系数 $(\cdot)_k$ 直接放入实式 (17)。

它适合加到当前真实位置求解的设计方程，或用作法向预条件器的选行依据。
有限个这样的矩条件只消去对应的有限个误差分量，不等于解了全部模式或非线性方程。

## 4. 可实施的法向矩修正及端口

选 C² 试函数 $w_j$，每个在需要固定的领圈附近恒零。
若参考法向仅全局 C¹，则应使 $w_j$ 支撑在一个法向光滑的实际片内部，
并在该片边界消掉 0–2 阶 jet；这样 $W_j=w_jn$ 延零后仍为 C²。
对现有有限分片解析表示，这可以用单元内部的 $t^3(1-t)^3$ 型函数和角 Fourier 模实现。
不能仅凭 $X\in C^2$ 就认定任意 $wn\in C^2$。

选有限个测试函数 $\chi_i$，令 $K_{ij}$ 为式 (17) 左边对 $w_j$ 的系数。
则 $Kc=b$ 是真实法向位移 $w=\sum_jc_jw_j$ 必须满足的完整矩系统。
若 $K$ 方且可逆，$c=K^{-1}b$ 精确消去这批线性矩；若长方，必须保留其真实兼容条件。
若 $K$ 秩亏，增添真实法向基或换测试位置，而不是给切向拟合增加频数。

实际应用还要重建 (7) 的切向字段并满足开领的全部 jet。
特别是给 (16) 仅规定 $w=0$ 的两端 Dirichlet 条件，并不自动给 $A_k=B_k=0$。
若残差在端部恒零且 $f^2\nu/D_k\ne0$，则 $A_k=0$ 还要求 $w_k'=0$。
这些附加端口可能形成真正的兼容条件，不能由“二阶方程可解”一笔带过。

## 5. 数值参考不精确时的正确使用方法

目前 R208 等实际图的 $h=X^*e$ 不等于目标 $g$。
精确的切向线性化是 $\mathcal L_vh$，不能在完整 Newton 中悄悄换成 $\mathcal L_vg$。
式 (13)–(17) 可以作为固定目标的预条件器或试探方向，但最终必须计算真实位置变化。

对任意 C² Cartesian 修正 $W$，有无余项的恒等式

$$ (X+W)^*e-g=E+2\operatorname{sym}\langle dX,dW\rangle
+\langle dW,dW\rangle.\tag{18}$$

故当前代码已有的 $X_s,X_u$ 及新增 $W_s,W_u$ 足够检验真实新度量；
二阶 jets 再用于实际曲率、C² 接合和 reach。
若先取 $Y=X+W$ 再作材料微分同胚，非线性拉回用 R112 的完整恒等式和实际界，
不能以线性矩消失代付其后验。

当前 R201/R205 的参数通过单位角切向量与 primitive 定义位置，
尚无单独的 $W$ 列；因此必须将上述法向方向准确注入原参数空间，
或者明确增加 C² Cartesian 自由度后重算实际 baseline/J/normal。
不能将一个未被原参数实现的法向试探记录为真实接受步。

## 6. G5 中有限证据与后续工作的精确边界

R114 的已登记结论是同一 $g$ 下 M8→M12→材料修复的有限下降至 $2\cdot10^{-9}$。
R112 和本文不由此推出无限维解存在；另一方面，有限证据也不因未证明无限极限而自动作废。
需要继续降低误差时，(10) 的实际值可判断剩余误差是否仍在切向算子的像中。
若连续区间积分给 $|b_\chi|$ 超过相应非线性预算，则该测试槽必须用真实几何修正消去。

一个完全不线性化的辅助检验是面积：任意把同一紧环带映到自身的微分同胚 $\Phi$ 都有
$\operatorname{Area}(\Phi^*h)=\operatorname{Area}(h)$。
若相对目标的谱误差至多 $\epsilon<1$，两特征值均在 $[1-\epsilon,1+\epsilon]$，故

$$\epsilon\ge
\frac{|\operatorname{Area}(h)-\operatorname{Area}(g)|}
{\operatorname{Area}(g)}.\tag{19}$$

这是全体重标的下界，但本文尚未计算当前 M12 的带误差面积差，因此不宣称它已排除当前候选。
新实施应先测 (10)/(19) 的实际量，再选择真实法向模式，并用 (18) 检查同一固定 $g$ 的实际下降。

### 来源

- 本题 [R112](R112-noncircular-metric-repair-and-stable-pullback.md)：完整三分量切向应变及精确拉回后验。
- 本题 [R114](R114-actual-noncircular-repair-to-original-tolerance.md)：当前有限数值对象、修复支撑和实际容差。
- 本题 [R201](R201-half-period-mean-phase-closure-without-reflection.md)、[R205](R205-complete-bent-annulus-cut-lifting-and-fixed-collar.md)：当前真实位置表示及开放固定领。

本文所有新式均在上文直接推导，不引用未核查的外部存在性结果。
