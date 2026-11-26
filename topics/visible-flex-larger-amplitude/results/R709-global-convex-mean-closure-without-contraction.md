# R709 — 支持内单位种子的全局凸均值闭合：不需要收缩条件

2026-11-26（UTC），Astra-larger-e4e2a2bf-20261126。**已证明：在 R708 的正长度、正垂直余量与半球条件下，三均值方程有唯一正径向根；R708 的额外条件 q<1 可以删除。** 本文给出全局存在/唯一性、同一分支的完整一二角导数、明确逆界及实际残差到准确根的误差界。它允许更宽端层的数学选择；实际端层、原完整度量与几何仍须真实求解。

本结果加强 [R708](R708-supported-unit-meridian-seed-contraction.md) 的均值块，不重做其已登记结论，也不把旧 root、KKT 或固定 normal 分支的失败改写成成功。这里没有新科学执行。新固定 seed 的来源及全部原外层变量必须继续明示；不把准确存在定理当作有限次数 Newton 已完成的记录。

## 1. 同一准确数据和保留的条件

沿用 R708 的准确固定度量、材料图、握持端、帽端、单位参考 $T_0$ 与严格内部支持 $U$。记支持总长度为 $L$，全部端层为 $E\subset U$，其总长度为 $b>0$，中央总长度为 $L_c=L-b$。端层宽度足以使各中央段长度严格正。所有这些区间、宽度和端层阶跃 $\chi(s)\in[0,1]$ 在角变量上固定。

准确需补支持积分仍是

$$
K(\phi)=P(\phi)-\Gamma(\phi)-\int_{[0,S]\setminus U}T_0(s,\phi)\,ds.
\tag{1}
$$

假设在整个角圈上

$$
0<k_-\le |K|\le k_+<L,\qquad K_z\ge k_z>0,
\qquad |T_0|=1,\quad T_{0,z}\ge0\ \text{于 }E.
\tag{2}
$$

保留 R708 的条件

$$
b<k_-,\qquad b<k_z,\qquad k_++2b<L,
\tag{3}
$$

及每个中央段的正长度。**不要求** $b/[\nu(k_--b)]<1$。定义

$$
r_-={k_--b\over L_c},\qquad r_+={k_++b\over L_c},
\qquad \zeta={k_z-b\over k_++b},
\qquad \nu=\sqrt{{1-\sqrt{1-\zeta^2}\over2}}.
\tag{4}
$$

于是 $0<r_-\le r_+<1$，$0<\zeta<1$，$\nu>0$。本稿中的 $r_\pm$ 是无量纲均值长度界；$b,L,L_c,k_\pm,k_z$ 都有长度单位。

对单位方向 $d$，只要分母非零，记

$$
Y(s,d,\phi)=(1-\chi)T_0+\chi d,\qquad
T_b={Y\over |Y|},\qquad B(d,\phi)=\int_E T_b\,ds.
\tag{5}
$$

所需三均值方程是

$$
F(v,\phi):=L_c v+B(v/|v|,\phi)-K(\phi)=0,
\qquad v\ne0.
\tag{6}
$$

正则性与 R708 相同：下面每项经典偏导必须存在；若以后求更高外参数混合导数，必须对真实数据另有那些导数。下文不从仅 $C^2$ 的外参数依赖虚构高阶光滑性。

## 2. 归一化端层向量是一个全局凸函数的梯度

固定 $\phi$。对任意 $d\in\mathbb R^3$，定义

$$
\psi_{s,\phi}(d)=
\begin{cases}
\displaystyle { |(1-\chi)T_0+\chi d|-(1-\chi)\over\chi},&\chi>0,\\[4pt]
T_0\cdot d,&\chi=0,
\end{cases}
\qquad
\Psi_\phi(d)=\int_E\psi_{s,\phi}(d)\,ds.
\tag{7}
$$

分子中的常数只为使 $\chi\to0$ 时的定义有限；它不改变对 $d$ 的梯度。因为 $|T_0|=1$，对固定有界 $d$ 展开范数在 $T_0$ 的一阶导数即得 $\psi_{s,\phi}(d)\to T_0\cdot d$。也可直接使用范数平方差的有理化公式得到同一极限。

每个 $\psi$ 都是凸函数，并且

$$
|\psi(d_1)-\psi(d_2)|\le |d_1-d_2|,
\qquad |\psi(d)|\le |d|.
\tag{8}
$$

第一式由范数的反三角不等式消去 $\chi$；第二式再取 $d_2=0$，注意 $\psi(0)=0$。$\chi=0$ 的分支同样成立。因此 $\Psi_\phi$ 在整个 $\mathbb R^3$ 上有限、连续、凸且 $b$-Lipschitz。特别，每个凸次梯度 $p\in\partial\Psi_\phi(d)$ 都满足

$$
|p|\le b.
\tag{9}
$$

证明 (9) 时，在次梯度不等式中取 $d+te$，再用 (8) 得 $p\cdot e\le b$；对所有单位 $e$ 取上确界即可。该结论即使某个 $Y$ 为零也成立，不在非光滑点预先假定梯度存在。

在 $Y$ 有一致正下界的地方，可以在积分内微分，且

$$
\nabla_d\psi=T_b,\qquad
D_d^2\psi={\chi\over|Y|}(I-T_bT_b^T).
\tag{10}
$$

$\chi=0$ 时梯度为 $T_0$、Hessian 为零，与 (10) 相容。因而 $B=\nabla\Psi$，并且

$$
M:=D_dB=\int_E{\chi\over|Y|}(I-T_bT_b^T)\,ds
\tag{11}
$$

是对称半正定矩阵。这个符号结构来自完整三分量端层积分，并非仅来自其轴向分量。

## 3. 闭单位球上的最小值给出实际正根

**定理 1。** 在 (2)(3) 与中央正长度条件下，(6) 有唯一根 $v_*$。该根满足

$$
r_-\le |v_*|\le r_+,qquad
 d_*={v_*\over|v_*|},\quad (d_*)_z\ge\zeta,
\qquad |Y(s,d_*,\phi)|\ge\nu\quad(s\in E).
\tag{12}
$$

**存在性证明。** 在闭单位球 $\overline{\mathbb B}$ 上最小化连续凸函数
$\Psi_\phi(d)-K\cdot d$。紧性给出一个极小点。连续凸目标和有内点的凸球满足一阶凸最优性条件：存在 $p\in\partial\Psi_\phi(d_*)$ 及球的外法向量 $n$，使 $K=p+n$。具体地，球内部有 $n=0$，边界上有 $n=\alpha d_*$、$\alpha\ge0$。这也可由目标在球上的支持超平面与球的法锥直接得到；此处使用的是凸次梯度条件，未先假定目标可微。

若在内部，或若边界乘子 $\alpha=0$，则 $K=p$，与 $|K|\ge k_->b\ge|p|$ 矛盾。因此

$$
|d_*|=1,\qquad K=p+\alpha d_*,\qquad
k_--b\le\alpha\le k_++b,quad\alpha>0.
\tag{13}
$$

取垂直分量得

$$
(d_*)_z={K_z-p_z\over\alpha}
\ge {k_z-b\over k_++b}=\zeta>0.
\tag{14}
$$

因为 $T_{0,z}\ge0$ 且 $|T_0|=|d_*|=1$，有
$T_0\cdot d_*\ge-\sqrt{1-\zeta^2}$。于是

$$
|Y|^2=1-2\chi(1-\chi)(1-T_0\cdot d_*)
\ge {1-\sqrt{1-\zeta^2}\over2}=\nu^2.
\tag{15}
$$

所以该极小点附近的全部端层分母一致避零，(10) 可真实使用，且原次梯度实际只有 $p=B(d_*,\phi)$。令

$$
\rho_*={\alpha\over L_c},\qquad v_*=\rho_*d_*.
\tag{16}
$$

(13) 给出 (6) 和 (12) 的长度界；(3) 保证 $\rho_*<1$。存在性证明没有使用收缩定理，也没有删去端层在任何方向上的贡献。证毕。

**唯一性证明。** 任何满足 (6) 的 $v\ne0$ 都写成 $v=\rho d$，其中 $\rho>0$、$|d|=1$；令 $\alpha=L_c\rho$。其方程为 $K=B(d)+\alpha d$。$|B|\le b$ 再次给出 (13)(14)，所以任何根都处在同一正半球的光滑域。

设有两个根 $(d,\alpha)$、$(e,\beta)$。由凸函数梯度的单调性，
$(B(d)-B(e))\cdot(d-e)\ge0$。将两根方程相减并点乘 $d-e$，得到

$$
0=(B(d)-B(e))\cdot(d-e)
 +(\alpha+\beta)(1-d\cdot e).
\tag{17}
$$

两项均非负，且 $\alpha+\beta>0$，所以 $d=e$；原方程再给 $\alpha=\beta$。因此 $v_*$ 唯一。梯度单调性在这里是 (7) 的全局凸性所给，不要求连接两方向的直线段上预先有一个额外小性界。证毕。

## 4. 完整三均值 Jacobian 的正切块与无收缩逆界

在准确根处简记 $v=v_*$、$\rho=|v|$、$d=v/\rho$、$P_d=I-dd^T$。由归一化的完整微分，

$$
J:=F_v=L_cI+{M P_d\over\rho}.
\tag{18}
$$

将 $\mathbb R^3$ 正交分解为 $\operatorname{span}\{d\}\oplus d^\perp$。径向列满足 $P_dd=0$，而 $M$ 对称半正定，所以此基中的矩阵具有形式

$$
J=\begin{pmatrix}
 L_c& d^TM|_{d^\perp}/\rho\\
 0& L_cI_{d^\perp}+P_dM|_{d^\perp}/\rho
\end{pmatrix}.
\tag{19}
$$

其正切块

$$
A_T=L_cI_{d^\perp}+P_dM|_{d^\perp}/\rho
\quad\text{满足}\quad A_T\ge L_cI_{d^\perp}>0.
\tag{20}
$$

因此 $J$ 一定可逆。它通常不对称，不能仅凭 (20) 将整个 $J$ 的最小奇异值写成至少 $L_c$；应使用下面包含非对角块的完整估计。

对右端 $w=w_\parallel d+w_T$，解为

$$
t=A_T^{-1}w_T,\qquad
J^{-1}w=t+\left({w_\parallel\over L_c}
 -{d^TMt\over L_c\rho}\right)d.
\tag{21}
$$

对角解算部分的范数至多 $1/L_c$。剩余秩一部分的范数至多
$\|M\|/(L_c^2\rho)$。由 (11)(15) 有 $\|M\|\le b/\nu$，故

$$
\boxed{\quad
\|J^{-1}\|\le {1\over L_c}\left(1+{b\over\nu(k_--b)}\right)
 ={1+q\over L_c},\qquad q={b\over\nu(k_--b)}.
\quad}
\tag{22}
$$

这里 $q$ 可以大于或等于1。若有更紧的真实 $\|M\|$ 上界，可在 (21) 中直接使用。R708 的 $1/[L_c(1-q)]$ 是其收缩假设下的另一充分逆界；本条不需要该假设，也没有改变原方程。

## 5. 全角共同分支及一、二角导数

均值根唯一，且 (18) 处处可逆。隐函数定理给每个角附近的同一光滑根；在交叠处唯一性强迫这些局部根相同，因此拼成整个角圈上的共同分支。数据的角周期直接给根的同一周期，没有按角独立选择另一极小点。

若原数据具有某个正交对称 $Q$，使对应角处的 $K,T_0$ 都等于原值乘 $Q$，而区间与 $\chi$ 不变，则 (7) 在 $d\mapsto Qd$ 下相容。只要两处属于本定理的假设域，唯一性给 $v\mapsto Qv$。因此 R708 所需的实际周期与反射关系由同一唯一分支继承；不需要在网格点之间另选符号。

以下 $B_\phi,B_{\phi\phi},B_{d\phi},B_{dd}$ 都表示固定 $d$ 的偏导。由于 $L_c$ 与角无关，完整一角导数是

$$
Jv_\phi=K_\phi-B_\phi,\qquad
 d_\phi={P_dv_\phi\over\rho}.
\tag{23}
$$

对任意 $w$，归一化的二次微分为

$$
N_2(v;w):=D^2\!\left({v\over|v|}\right)[w,w]
=-{2(d\cdot w)P_dw+d|P_dw|^2\over\rho^2}.
\tag{24}
$$

从 $L_cv+B(d,\phi)=K$ 再微分一次，将含 $v_{\phi\phi}$ 的项全部留在同一个 $J$ 中，准确得到

$$
\boxed{\begin{aligned}
Jv_{\phi\phi}={}&K_{\phi\phi}-B_{\phi\phi}
 -2B_{d\phi}d_\phi-B_{dd}[d_\phi,d_\phi]
 -M N_2(v;v_\phi),\\
d_{\phi\phi}={}&{P_dv_{\phi\phi}\over\rho}+N_2(v;v_\phi).
\end{aligned}}
\tag{25}
$$

这保留了端层参考的角变化、对方向的全部交叉项和归一化二阶费用。对一个外参数 $p$，在区间、宽度和 $\chi$ 固定时同样有
$Jv_p=K_p-B_p$。若改变支持宽度、积分端点或 $L_c$，则它们的移动边界和乘积导数必须加入，不能直接套用此固定支持公式。

实际固定 seed provider 使用指定参考 core/H 来定义 $K,T_0$ 后，整个 seed 是固定参考。外层当前 $x$ 的导数仍来自原完整 $\exp\omega$、core、H 和原 normal 算子；不能在每个当前 $x$ 重新生成 seed 而删掉这些自由变量的依赖。

## 6. 真残差到唯一准确根的全局误差界

本节允许实际候选尚未在根附近，给出不依赖 $q<1$ 的明确误差控制。固定一角，令 $\widehat v\ne0$ 是待评估的向量，
$\widehat\rho=|\widehat v|$、$\widehat d=\widehat v/\widehat\rho$，并且真实读得
$\widehat d_z\ge\widehat\zeta>0$。假设对**准确方程**有

$$
|F(\widehat v,\phi)|\le\varepsilon_F.
\tag{26}
$$

设准确唯一根是 $v_*=\rho_*d_*$。将两方程相减，点乘
$\widehat d-d_*$，并用 (17) 中同一单调性，得到

$$
{L_c(\widehat\rho+\rho_*)\over2}
 |\widehat d-d_*|^2
\le \varepsilon_F|\widehat d-d_*|.
$$

因此，包括两方向相同的情形在内，

$$
|\widehat d-d_*|\le
E_d:={2\varepsilon_F\over L_c(\widehat\rho+r_-)}.
\tag{27}
$$

为了同时控制径向长度，令 $\zeta_*:=\min(\widehat\zeta,\zeta)>0$。连接两单位方向的直线段上，每点 $y$ 满足 $y_z\ge\zeta_*$。对所有 $\chi>0$，因 $T_{0,z}\ge0$，

$$
|(1-\chi)T_0+\chi y|\ge\chi\zeta_*,
\qquad {\chi\over|(1-\chi)T_0+\chi y|}\le {1\over\zeta_*}.
\tag{28}
$$

在 $\chi=0$ 处 $B$ 对方向的微分为零。故沿整条线段，(11) 给
$\|D_dB\|\le L_B:=b/\zeta_*$，从而
$|B(\widehat d)-B(d_*)|\le L_BE_d$。再使用
$K-B(d_*)=L_c\rho_*d_*$ 与 (26)，范数的反三角不等式给

$$
|\widehat\rho-\rho_*|\le {\varepsilon_F+L_BE_d\over L_c},
$$

$$
\boxed{\quad
|\widehat v-v_*|
\le {\varepsilon_F\over L_c}
 +\left({L_B\over L_c}+r_+\right)E_d.
\quad}
\tag{29}
$$

这是准确积分方程的条件误差界。若实际程序用工作量 $\widehat B,\widehat K,\widehat L_c$ 和浮点向量残差 $R_w$，必须先支付

$$
|F(\widehat v,\phi)|\le |R_w|+\delta_B+\delta_K
 +\delta_{L_c}|\widehat v|+\delta_{\rm arith}=: \varepsilon_F,
\tag{30}
$$

其中 $|R_w|$ 若以有限算术读取，须使用向外范数上界；不能直接把打印的范数当准确上界。$\delta_B$ 包含实际完整端层积分、参考及 $\widehat v$ 的工作单位化、$\chi$ 与端层位置等输入载体误差，
$\delta_K$ 包含帽端/core 逆图、完整补集与准确无限尾，
$\delta_{L_c}$ 包围工作长度与准确长度之差，
$\delta_{\rm arith}$ 包围形成残差的算术费用。若 $L_c$ 用准确数运算，该项可为零；不能从打印的小残差自动令其它费用为零。

(29) 只控制均值向量。它不会自动给角导数误差、完整场六jet误差或 reach；角导数必须使用 (23)(25) 的真实全部数据及其误差，原完整 normal 链继续承担 [R707](R707-fixed-normal-chain-root-jet-error-propagation.md) 的责任。

## 7. 回接 R708 的中央单位曲线与全部端口

由定理1，准确均值长度 $\rho_*(\phi)$ 在同一固定紧区间
$[r_-,r_+]\Subset(0,1)$ 中。R708 的五段对称角 profile 因而仍可使用：固定其参数
$0<\epsilon<\min(1/8,r_-/4)$，按同一个 $h_\epsilon$ 定义

$$
a_\epsilon(\lambda)=\int_0^1\cos(\lambda h_\epsilon(x))\,dx.
\tag{31}
$$

原证明给 $a_\epsilon(0)=1$、$a_\epsilon(\pi/2)\le4\epsilon<r_-$，且在所需解上有严格负导数及一致下界。于是每角有唯一
$\lambda\in(0,\pi/2)$ 使 $a_\epsilon(\lambda)=\rho_*$，并继承完整角导数。

仍用**径向极向量**的投影

$$
w={e_r(\theta_0)-(e_r(\theta_0)\cdot d_*)d_*
 \over |e_r(\theta_0)-(e_r(\theta_0)\cdot d_*)d_*|}.
\tag{32}
$$

因为 $(d_*)_z\ge\zeta$，该分母至少为 $\zeta$。中央各段使用原
$T_c=\cos(\lambda h_\epsilon)d_*+\sin(\lambda h_\epsilon)w$。
反对称性使正弦积分为零，全部中央贡献为 $L_c\rho_*d_*=L_cv_*$。因此

$$
\int_U T\,ds=B(d_*)+L_cv_*=K.
\tag{33}
$$

单位长度、外补集保持、端层/中央平二jet与原 core/cap 六jet端口，均按 R708 的同一完整拼接证明成立。本文只把均值存在性和导数逆界换成更强的定理1及(22)，其它数据与拼接公式不变。由固定 $g$ 的 $g_{ss}=1$ 可得径向 Gram 恒等式；混合、角向 Gram 的全部方程仍须原样求解。

删除 $q<1$ 可能让端层宽度有更大的选择范围，从而缓解 $\chi_s,\chi_{ss}$ 的薄层费用；这不是已经获得更小曲率的实际结论。条件 (3)、中央 profile 的非退化条件、原幅度及全域几何预算均继续存在。实际默认宽度或默认 $\epsilon$ 若未满足相应条件，不能用本定理替它补证明。

## 8. 真实数值入口的含义

式(18)给出了直接求解同一完整三均值方程的 Newton 矩阵，(23)(25)使用相同矩阵求角jet。以实际完整残差进行回溯，可以在不要求 $q<1$ 的情况下尝试该正根；有限次 Newton 的成功必须由本次真实执行返回。存在唯一根与声明预算内到达该根是两个独立命题。

对正权有限求积，(7)(11)仍给相应**离散方程**的凸性/半正定结构。但其权重总和、工作目标及长度必须使用自己的实际值；若权重和为 $b_Q$，相应界就使用 $b_Q$，不能把舍入后的正权和冒成准确物理 $b$。离散根到连续根仍须支付(30)与全部角导数费用。

均值矩阵 $J$ 的可逆性也不推出原 normal 端点算子的六控制 $C_u$ 满秩，不推出沿其固定分段的交叉矩阵可逆。新的 fixed seed 必须以新 source/model/provider 身份接入完整原外层，并真实读当前全部自由变量、每条 Gram 行、全部历史地点和几何。这里没有新增 fixture 或等待本证明才能执行的前门。

本条完成的是同一单位种子均值块的准确全局存在/唯一性和量化控制。课题 README 所需闭面等距、强 C² 全时间族、握持/整像幅度、含反射非全等、全t reach、整面残差及固定问题实际精化，继续由实际候选分别支付。
