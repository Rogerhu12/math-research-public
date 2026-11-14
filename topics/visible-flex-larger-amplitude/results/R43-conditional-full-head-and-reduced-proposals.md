# R43：全频头部的条件性联合闭合与214维提案分解

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）。2026-11-12。

**已证明（条件定理）。** 本文给出 R33、R42 正核所需的完整 Banach
条件，并证明428维提案可通过214维矩阵构造后逐项验回。
**428个实际映射/收缩门尚未通过；本文不把90734的未知终态当作成功。**
条件付清时，结论仅涉及真实 node12 至无穷 cuff 的全频高度解；
外0..11、强前缀联解和全时闭曲面的几何条件仍须另付。

## 1. 固定实对象和未知空间

固定 R26 的同一个真实源与 R18 的完整深图，不改变冻结参数、
全局warp、宽度38、physical node225/F224对应或度规。
令 $L_*$ 为 R38 或 R39 已证明的辅助低46解，$z_*^{\,0}$ 为它的真实
far低高度参数。这里的中心是那个准确辅助解，不是保存浮点轨道。
它的线性参考、完整修正盒和参数界已知即可，不要求预先知道其每一点。

取全部213个胞元 $I_n$，$12\le n\le224$。
使用 R33 的同一连续正角宽 $\tau(r)$、分段正包络 $V(r)$、
$B_n\ge1$，以及先逐模取径向sup的物理强范数

$$
X_n(u)=\sum_{m\ne0}(1+|m|)
\left[
\sup_{I_n}e^{\tau(r)|m|}|B_np_m(r)|/V(r)
+\sup_{I_n}e^{\tau(r)|m|}|\kappa_{\perp,m}(r)|/V(r)
\right].
\tag{43.1}
$$

所有频率为偶数，signed两半均计入。两个物理分量的sup分别取。
假设 $X_n(L_*)\le1$，并记 $A_n\ge\sup_{I_n}V/w$。
不在这里把角宽提升到38；far评估另用R42的真实行。

将新变化写为 $e=\ell+h+u$：

- $\ell$ 含 $2\le|m|\le92$，浅端46个高度为齐次条件；
- $h$ 含 $94\le|m|\le8190$，浅端高度不另固定；
- $u$ 含全部 $|m|\ge8192$，同样没有浅端零条件。

用一个全头部范数 $X_\infty(u)$ 控制 $u$，使
$X_n(u)\le X_\infty(u)$。取 R33 的全头部“先sup后sum”定义即可；
不能将其换成各胞元点态质量的sup。字段在接口满足真实物理连续性；
归一分量因 $B,V$ 改变而产生的跳变按既有核证明处理。

再引入独立的46维far参数增量 $\delta z$。其坐标已吸收
$e^{38m}/S_F$，范数是普通 $\ell^1$；不重复施加角权。
指定 $0<Z\le2^{-1948}$，最后一块的范数为 $|\delta z|_1/Z$。
在这个空间中 far 评估有单独方程，不能未经证明把物理窄范数换成
$|\delta z|_1$。

各有限头部区间闭且 $V>0$、$\tau>0$。加权连续 Fourier 场及其
真实接口条件构成 Banach 空间；无限窗也是带径向sup的加权
$\ell^1$ 空间，故完整性保留。实性、偶对称和浅端齐次条件都是闭条件。

## 2. 准确的联合映射

记 $f$ 为 R33 保留完整mean小根和点态逆分母的非线性源。
记 $D=\Gamma_{224}-\Gamma^{\rm lin}_{224}$ 为 R18 的完整raw图差。
在 $|z|_1\le Z$ 中

$$
\|D(z)\|\le C_DZ^2,\qquad
\|D'(z)\|\le4C_DZ,\qquad C_D=2^{1967}.
\tag{43.2}
$$

$G_{\rm lo}$ 是 R42 的零浅高度、零线性far缺陷 Green；
$\mathcal B_{\rm lo}$ 是准确低边界提升。
$G_{\rm hi}$ 为从真实far向外的全高窗强制传播，
$\mathcal B_{\rm hi}$ 同时提升高窗的两个真实far分量。
这些高窗不是任意浅Dirichlet问题。

令 $\mathcal E$ 为准确的低高度far评估。定义

$$
\begin{aligned}
T_\ell={}&G_{\rm lo}\mathscr P_{\rm lo}
 [f(L_*+e)-f(L_*)]\\
&+\mathcal B_{\rm lo}
 [D_{\rm lo}(z_*^{\,0}+\delta z)-D_{\rm lo}(z_*^{\,0})],\\
T_{\rm hi}={}&G_{\rm hi}\mathscr P_{\rm hi}f(L_*+e)
+\mathcal B_{\rm hi}D_{\rm hi}(z_*^{\,0}+\delta z),\\
T_z={}&\mathcal E T_\ell .
\end{aligned}
\tag{43.3}
$$

将第二行按中窗和无限窗分开。最后一行通过R42真实far核计算，不从
(43.1)免费升宽。由于 $L_*$ 已解完整低投影问题，低块和far增量块的
常数项恰为零；高块必须保留 $f(L_*)$ 和真实高深迹。

在固定点上 $\delta z=\mathcal E\ell$，所以
$z_*^{\,0}+\delta z=\mathcal E(L_*+\ell)$。因此 (43.3) 的独立参数
并没有放松实际far高度匹配条件。

## 3. 完整非线性正映射

设R42四个核为 $M,C,Q,R$，分别对应 main、corr、base、remainder；
四个far行记 $F_M,F_C,F_Q,F_R$。其中 $M$ 已含主导数系数，
$C$ 外乘3，$R$ 已含逐点 $V/w$。
设 $H_{kn}$ 为 R33 的完整中窗源核；因向外因果次序，$H_{kn}=0$
当 $n<k$。设 $\gamma_\infty$ 为整个无限窗源核。

给定正半径

$$
x=(r_{{\rm lo},n},r_{{\rm mid},n},r_\infty,r_z),\qquad
t_n=r_{{\rm lo},n}+r_{{\rm mid},n}+r_\infty .
\tag{43.4}
$$

记

$$
P(t)=t+t^2+t^3/3,\qquad
K_n(t)=3t+\tfrac32t^2+216A_nP(t).
\tag{43.5}
$$

R33 §16.7给出所有模的完整源界，特别包含mean与逆分母。
令 $b_n^{\rm pure},b_\infty^{\rm pure}$ 分别是宽辅助中心自产高频在
中窗和无限窗的完整响应界。
令 $b_n^{\rm far},b_\infty^{\rm far}$ 是将 (43.2) 的 $C_DZ^2$
通过准确高边界线性提升后的上界。假设这些常数与同一 $V,\tau$
及同一个 $Z$ 相属；不允许交叉使用另一强度参考原有的角宽函数。

定义

$$
\beta_n=4C_DZ^2 B_{{\rm low},n},\qquad
\beta_z=4C_DZ\,E B_{\rm low}.
\tag{43.6}
$$

由R42固定频谱质量证明和R33完整源式，(43.3)的正映射可取

$$
\begin{aligned}
\Phi_{{\rm lo},k}(x)
={}&\sum_n[(M_{kn}+3C_{kn})t_n
 +\tfrac32Q_{kn}t_n^2+216R_{kn}P(t_n)]
 +\beta_kr_z,\\
\Phi_{{\rm mid},k}(x)
={}&b_k^{\rm pure}+b_k^{\rm far}
 +\sum_nH_{kn}K_n(t_n),\\
\Phi_\infty(x)
={}&b_\infty^{\rm pure}+b_\infty^{\rm far}
 +\gamma_\infty\sum_nK_n(t_n),\\
\Phi_z(x)
={}&\frac1Z\sum_n[(F_{M,n}+3F_{C,n})t_n
 +\tfrac32F_{Q,n}t_n^2+216F_{R,n}P(t_n)]
 +\beta_zr_z.
\end{aligned}
\tag{43.7}
$$

高far项已经按整个参数球取最大值，故其映射上界不必再加一次
$r_z$ 项。其对参数的导数仍保留为 $4b^{\rm far}$，因为这些
$b^{\rm far}$ 来自线性提升乘 $C_DZ^2$，而 (43.2) 给导数
$4C_DZ$，参数范数还乘一个 $Z$。

## 4. 428维完整导数矩阵

选取一个提案域 $\rho>0$，使最后的每个 $t_n\le\rho$。
定义

$$
\begin{aligned}
\mathsf L_{kn}
 &=M_{kn}+3C_{kn}+3\rho Q_{kn}
   +216(1+\rho)^2R_{kn},\\
\mathsf H_{kn}
 &=H_{kn}[3(1+\rho)+216A_n(1+\rho)^2],\\
g_n&=\gamma_\infty[3(1+\rho)+216A_n(1+\rho)^2],\\
f_n&=[F_{M,n}+3F_{C,n}+3\rho F_{Q,n}
       +216(1+\rho)^2F_{R,n}]/Z .
\end{aligned}
\tag{43.8}
$$

这些常数作用于差的每胞元总质量。对
$v=(v_{{\rm lo},n},v_{{\rm mid},n},v_\infty,v_z)\ge0$，
置 $s_n=v_{{\rm lo},n}+v_{{\rm mid},n}+v_\infty$，则完整导数上界为

$$
\begin{aligned}
(Jv)_{{\rm lo},k}&=\sum_n\mathsf L_{kn}s_n+\beta_kv_z,\\
(Jv)_{{\rm mid},k}&=\sum_n\mathsf H_{kn}s_n+4b_k^{\rm far}v_z,\\
(Jv)_\infty&=\sum_ng_ns_n+4b_\infty^{\rm far}v_z,\\
(Jv)_z&=\sum_nf_ns_n+\beta_zv_z .
\end{aligned}
\tag{43.9}
$$

总维数是 $2\cdot213+2=428$。无限块的输入同时出现在所有胞元的
$s_n$ 中，所以相应列是完整行和；没有把该耦合丢掉。
低和中窗双向耦合、两者与无限窗的耦合、完整far反馈均在 (43.9)。

## 5. 条件性存在、唯一性与真实深尾接合

**定理43.1。** 假设上述全部核与残差确已包围同一实对象。
若有严格正的428个半径 $x$ 与428个距离权 $W$，满足

$$
\Phi_i(x)<x_i\quad(1\le i\le428),\qquad
\max_n t_n<\rho,\qquad
A_n(1+t_n)<1/64,
\tag{43.10}
$$

$$
|z_*^{\,0}|_1+Zr_z<Z,\qquad
q:=\max_i\frac{(JW)_i}{W_i}<1,
\tag{43.11}
$$

则 (43.3) 在该闭盒内有唯一固定点。它给出全部偶Fourier频率的
完整非线性头部，并准确接到同一 R18 深尾；mean和二阶接口均保留。
所有46个浅低高度不变，其余浅高高度是解的输出。

**证明。** 盒内中心加变化的每胞元范数至多 $1+t_n$。
(43.10) 使R33的完整mean小根及乘法逆在整个盒与所需复圆盘上有效。
R33的二次主部和完整余项沿线段积分给 (43.7)；固定模质量论证保证
这些界在先sup后sum的范数中成立。(43.2)、(43.6) 给低far差，
高块保留全部 $b^{\rm pure}+b^{\rm far}$。
因此 (43.10) 使准确映射把闭盒映入自身。

两点间的线段仍在盒内。对实际范数上界 $1+t_n$ 应用R33导数式，
再用 $t_n\le\rho$ 的单调性，得到 (43.8)–(43.9)。
这里并不需要断言完整mean根在所有大于实际盒的点都存在：
$A_n(1+t_n)<1/64$ 已在实际线段上支付定义域，$\rho$ 只放大正系数。
赋予差空间距离

$$
d_W(Y,\widetilde Y)=
\max_i\frac{\text{第 }i\text{ 块的差范数}}{W_i}.
\tag{43.12}
$$

所有权严格正，且只有有限个块，故此距离仍完备。
(43.11) 与 (43.9) 给 $\operatorname{Lip}(T)\le q<1$。
Banach定理给固定点及盒内唯一性。

在固定点处，低投影方程加回辅助中心恰得到完整源的低输出；
高两窗得到剩余全部频率。均值由同一个完整小根恢复，未将mean设零。
far增量方程使低高度恰为 R18 输入；低斜率满足真实线性图加
$D_{\rm lo}$，高两分量直接等于 $D_{\rm hi}$。所以完整非均值
canonical trace 与同一准确深解相同。

其物理 $p,\kappa_\perp$ 因精确坐标转换而相同。完整mean小根由同一
真实背景和非均值trace唯一确定，故mean径向导数也相同。取深尾mean
高度为积分初值，向外积分这个同一根，得到一个统一的mean高度常数。
没有额外独立mean接缝条件，也没有在每个胞元重置积分常数。

在有限头部 $\tau_{\min}>0$。Fourier级数及所需角导数一致收敛。
准确积分方程给非均值物理场的径向一阶正则性；R33的精确mean消元及
非零分母给mean相同的正则性。由 $h_\theta=rp$、$h_r=\kappa$，
全部二阶高度导数连续。在far两侧，完整trace和同一方程给相同径向导数，
故两阶高度jet接合。更深处的无穷极限与平cuff的 $C^2$ 性由 R18
继承。实性与对称性由映射保持，也可由唯一性与共轭对称得到。证毕。

该结论是准确高度/Darboux解的条件性存在，不自动给全局水平发展、
嵌入、reach或握持幅度；需要时继续使用R32及相应几何证明。

## 6. 不丢428个门的214维提案分解

**定理43.2。** 上述正矩阵有准确分解 $J=\mathsf C\mathsf B$，
其中

$$
\mathsf Bv=(s_1,\ldots,s_{213},v_z),
\tag{43.13}
$$

$\mathsf C$ 将这214个坐标按 (43.9) 的四行输出。
其反序乘积 $\mathsf R=\mathsf B\mathsf C$ 是214维矩阵，
具体为

$$
\mathsf R_{kn}=\mathsf L_{kn}+\mathsf H_{kn}+g_n,\qquad
\mathsf R_{k,z}=\beta_k+4b_k^{\rm far}+4b_\infty^{\rm far},
\tag{43.14}
$$

$$
\mathsf R_{z,n}=f_n,\qquad \mathsf R_{z,z}=\beta_z.
\tag{43.15}
$$

这个降维只构造半径与距离权的提案，不改变原428维映射或盒。

**证明。** 把 (43.13) 代入 (43.9) 即得 $J=\mathsf C\mathsf B$；
将低、中、无限三块相加即得 (43.14)–(43.15)。
所有正矩阵的原始项都出现，特别 $g_n$ 加到每个胞元行。

若 $b$ 是428维常数项，求

$$
(I-\mathsf R)y=\mathsf Bb
\tag{43.16}
$$

并置 $x_0=b+\mathsf Cy$，则
$\mathsf Bx_0=\mathsf Bb+\mathsf Ry=y$，
因而 $(I-J)x_0=b$。若有正提案，可将其加倍后直接检查 (43.10)；
不能仅从解了 (43.16) 宣称实际非线性不变性。

对任意 $0<c<1$ 与严格正的428维种子 $v$，若

$$
(cI-\mathsf R)y=\mathsf Bv,\qquad
W=(v+\mathsf Cy)/c>0,
\tag{43.17}
$$

则 $\mathsf BW=y$，故 $JW=cW-v<cW$。
这给出距离权的准确代数来源。实际使用区间逆或向上取值时，
所得向量只作提案，仍须以 (43.9) 逐项检查428行的 $(JW)_i/W_i$。
因此提案矩阵的舍入不会绕过任何门。

若 $\lambda\ne0$ 是 $J$ 的特征值，则对其特征向量 $v$，
$\mathsf Bv\ne0$，且
$\mathsf R(\mathsf Bv)=\lambda\mathsf Bv$；反方向对
$\mathsf R$ 的非零特征值用 $\mathsf C$ 即得。
故非零谱也一致，但本计算不以浮点谱半径代替正权核验。证毕。

## 7. 执行边界

[新联合入口](../computations/closure_joint_head_box_reduced.py)
按214维提案、原428维直接检查实现上述公式，并输出全部半径、
实际映射值、余量、距离权与Lipschitz行。半径求解失败或一项门失败时，
输出只能是一次未通过的充分条件尝试。

原作业90734仅观察到428维装配完成；随后执行器失联并被替换。
没有半径、最终正盒、Lipschitz或正式退出记录。旧未推Green包也须按
恢复记录重新计算。本文没有使用该未知终态作为任何数值前提。
