# R99：完整均值四场差到五个物理导数差的正矩阵

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。
日期：2026-11-12。
状态：完整条件定理；给出可执行精确有理消费者和两项精确多项式恒等式核对。它不证明外头真解存在，也不证明输入的四个场误差已经成立。

本文接 [R95](R95-seg7-curvature-margin-and-physical-jet-budget.md) 的物理导数误差门，使用 [R64](R64-general-outer-mean-and-compatible-defect.md)、[R75](R75-complete-mean-transport-and-shear-constraint.md)、[R77](R77-complete-mean-defect-zero-mode.md) 的完整均值与实际候选缺陷。两个完整均值根的差界见 [同根比较引理](../notes/2026-11-12-tail-two-complete-mean-roots-rational-difference.md)；本文重写全部需要的常数，不借用被截掉的均值或高频方程。

## 1. 对象、坐标和量词

在同一个真实胞元或其闭子区间，固定

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad
E=1+w^2,\qquad r>0,\quad w>0.
\tag{99.1}
$$

若使用原源坐标 $x$，令 $r_x>0$，并记

$$
z=w^2,\qquad s=\frac{r_x}{r},\qquad
\ell=\frac{w_x}{w}.
\tag{99.2}
$$

所有 $r$ 导数都指真实物理半径；$\theta$ 是同一个源曲面角坐标，并非已经重建的 Cartesian 图角。各个公式先在背景及高度具有所需导数的胞元内部使用；端点结论须由同一背景与实际 $C^2$ 高度迹连续延拓，不额外假定尚未证明的全局嵌入。

令 $\widehat h$ 是一个固定兼容候选。其非均值高度、径向导数和二阶导数均来自同一函数。令 $h$ 是在相同 $g$ 上满足**完整、未作 Fourier 投影的 Darboux 方程**的真实高度；此存在性是外部假设。定义

$$
P=\frac{h_\theta}{rw},\qquad
K=\frac{h_r}{w}-1=c+\overline K,\qquad
T=P_\theta,\qquad U=\overline K_\theta-P,
\tag{99.3}
$$

帽号表示候选的对应量。两侧都采用同一个完整小均值分支，$\overline K$、$P$、$T$ 的角均值为零。全部非零频率为偶数，最小绝对频率为 $2$；允许真实解具有无限高模。

记

$$
A=1-zP^2,\qquad
D=E-z(1+K)^2-EzP^2,\qquad
L=1+K+ET.
\tag{99.4}
$$

两侧完整均值方程是

$$
\left\langle
\frac{1+z(1+K)T/A}{\sqrt D}
\right\rangle=1.
\tag{99.5}
$$

必须给出两侧真实 $A,D,L$ 的正下界。候选的有限求值采样、一个投影解或只含低模的误差，均不能代替本节假设。

本文输入的四个误差是同位置的 Fourier $A^0$ 质量界：

$$
\begin{aligned}
e_K&\ge\|\overline K-\widehat{\overline K}\|_{A^0},&
e_P&\ge\|P-\widehat P\|_{A^0},\\
e_T&\ge\|T-\widehat T\|_{A^0},&
e_\theta&\ge\|\overline K_\theta-\widehat{\overline K}_\theta\|_{A^0}.
\end{aligned}
\tag{99.6}
$$

这里 $A^0$ 范数是全部正负 Fourier 系数绝对值之和。因此它控制所有真实角度的上确界。本文不会把输出的实角度 $h_{rr}$ 上界重新解释成未支付的解析条带范数。

## 2. 一个保留真实候选残差的精确恒等式

对任意兼容高度，定义完整分子

$$
J=L K_x+
\ell(2K+T+K^2+zP^2+KT)-EsU^2.
\tag{99.7}
$$

它包含候选的实际 $c_x$，不把完整均值设为零。若非均值高度截到模式 $40$，这里有限分子仍保留直到模式 $80$，以及全部标量均值项。

令

$$
\Phi(P,K,T,U)=
\frac{w_r[1+z((1+K)T-P^2)]+(Ew/r)U^2}{L}.
\tag{99.8}
$$

则精确有

$$
h_{rr}=\Phi(P,K,T,U)+\frac{w}{r_xL}J.
\tag{99.9}
$$

证明由 $h_r=w(1+K)$ 得

$$
\frac{r_x}{w}h_{rr}=\ell(1+K)+K_x.
$$

将其乘以 $L$ 并代入 (99.7)，剩下的线性项使用

$$
(1+K)L-(2K+T+K^2+zP^2+KT)
=1+z((1+K)T-P^2).
\tag{99.10}
$$

这给出 (99.9)。该计算未使用候选的 Darboux 方程。

对真解，$J=0$，所以只有真解一侧可以用 $\Phi$ 代替实际 $h_{rr}$。对候选，必须保留

$$
\widehat R_H=\frac{w}{r_x\widehat L}\widehat J.
\tag{99.11}
$$

从而

$$
h_{rr}-\widehat h_{rr}
=\Phi(P,K,T,U)-\Phi(\widehat P,\widehat K,\widehat T,\widehat U)
-\widehat R_H.
\tag{99.12}
$$

这是本文避免免费取得径向误差导数的关键。误差场趋于零时，非零候选残差不会自动消失。

和已存审计的物理 Darboux 单位对应，

$$
\widehat{\mathcal D}
=\frac{w^2}{rr_xE^2}\widehat J,
\qquad
\widehat R_H=\frac{rE^2}{w\widehat L}\widehat{\mathcal D}.
\tag{99.13}
$$

两个公式都要求完整的同一个候选分子。只保留非均值或低频的 $J$ 不能使用。

## 3. 完整均值差的显式正系数

取共同真实上界

$$
|P|_{A^0}\le p,\quad |K|_{A^0}\le k,\quad
|T|_{A^0}\le t,\quad |U|_{A^0}\le u,
\tag{99.14}
$$

它们必须同时覆盖两侧完整场。取

$$
r\in[r_-,r_+],\quad w\in[w_-,w_+],\quad
|w_r|\le v,\quad r_x\ge q_->0,
$$

并定义

$$
z_*=w_+^2,\quad E_*=1+z_*,\quad
a=\min(1,A_-),\quad d=\min(1,D_-),\quad l=L_->0.
\tag{99.15}
$$

两侧之间按完整实状态 $(c,\overline K,P,T)$ 作线性插值。沿此线，$A,D$ 为凹函数，$L$ 为仿射函数，所以同一个正下界覆盖整条线。中间状态无需满足均值方程。

令

$$
v_D=z_*(2k+k^2+E_*p^2).
$$

定义

$$
\begin{aligned}
C_K&=\frac{k+E_*t}{d^2}+\frac{3v_D}{2d^3},\\
C_T&=\frac{k+z_*p^2}{ad}+\frac{v_D}{2d^2},\\
C_P&=\frac{E_*p[1+z_*(1+k)t/a]}{d^2}
+\frac{2z_*p(1+k)t}{a^2d}.
\end{aligned}
\tag{99.16}
$$

则两个完整均值根满足

$$
|c-\widehat c|\le a_K e_K+a_P e_P+a_T e_T,
\qquad
(a_K,a_P,a_T)=\frac{E_*^2}{l}(C_K,C_P,C_T).
\tag{99.17}
$$

为完整说明，均值泛函的三个实偏导权是

$$
B_K=L D^{-3/2},\quad
B_T=\frac{1+K}{A\sqrt D},\quad
B_P=
\frac{EP[1+z(1+K)T/A]}{D^{3/2}}
+\frac{2zP(1+K)T}{A^2\sqrt D}.
$$

利用 $\langle\delta\overline K\rangle=\langle\delta T\rangle=0$，在对应两项中准确减去常数 $1$。由 $|D-1|\le v_D$ 和 $a,d\le1$，分别得到 $|B_K-1|\le C_K$、$|B_T-1|\le C_T$、$|B_P|\le C_P$。完整实均值导数满足

$$
\langle B_K\rangle\ge lE_*^{-3/2}\ge lE_*^{-2}.
$$

对整条状态线积分，便得 (99.17)。因此没有把均值导数遗漏，也没有从实正性推断复条带逆。

## 4. 五个物理导数的正矩阵

定义完整分子的共同绝对上界

$$
N_*=v[1+z_*((1+k)t+p^2)]
+\frac{E_*w_+}{r_-}u^2.
\tag{99.18}
$$

再定义四个非负系数

$$
\begin{aligned}
F_K&=\frac{vz_*t}{l}+\frac{N_*}{l^2},\\
F_P&=\frac{2vz_*p}{l}+\frac{2E_*w_+u}{r_-l},\\
F_T&=\frac{vz_*(1+k)}{l}+\frac{E_*N_*}{l^2},\\
F_\theta&=\frac{2E_*w_+u}{r_-l}.
\end{aligned}
\tag{99.19}
$$

设输入列顺序是 $(e_K,e_P,e_T,e_\theta)$，输出行顺序是

$$
(h_r,\ h_\theta,\ h_{rr},\ h_{r\theta},\ h_{\theta\theta}).
$$

令

$$
\mathcal B=
\begin{pmatrix}
w_+(1+a_K)&w_+a_P&w_+a_T&0\\
0&r_+w_+&0&0\\
F_K(1+a_K)&F_P+F_Ka_P&F_T+F_Ka_T&F_\theta\\
0&0&0&w_+\\
0&0&r_+w_+&0
\end{pmatrix}.
\tag{99.20}
$$

若同候选完整残差满足 $\|\widehat R_H\|_\infty\le d_H$，则五个真实角度的物理导数误差逐项满足

$$
\begin{pmatrix}
\|\delta h_r\|_\infty\\
\|\delta h_\theta\|_\infty\\
\|\delta h_{rr}\|_\infty\\
\|\delta h_{r\theta}\|_\infty\\
\|\delta h_{\theta\theta}\|_\infty
\end{pmatrix}
\le
\mathcal B
\begin{pmatrix}e_K\\e_P\\e_T\\e_\theta\end{pmatrix}
+
\begin{pmatrix}0\\0\\d_H\\0\\0\end{pmatrix}.
\tag{99.21}
$$

证明：$h_r=w(1+c+\overline K)$，$h_\theta=rwP$，$h_{r\theta}=w\overline K_\theta$，$h_{\theta\theta}=rwT$，所以除第三行外的四行直接来自 (99.17)。

第三行由 (99.8) 的商差给出。令 $\Delta K\le e_K+|\delta c|$，则

$$
\begin{aligned}
|\delta L|&\le\Delta K+E_*e_T,\\
|\delta U|&\le e_\theta+e_P,\\
|\delta N|&\le
vz_*\{t\Delta K+(1+k)e_T+2pe_P\}
+\frac{2E_*w_+u}{r_-}(e_\theta+e_P).
\end{aligned}
$$

因此

$$
|\delta\Phi|\le\frac{|\delta N|}{l}
+\frac{N_*|\delta L|}{l^2}
\le F_K\Delta K+F_Pe_P+F_Te_T+F_\theta e_\theta.
$$

代入 (99.17) 和 (99.12)，即得第三行。这里没有取 $\delta K_r$、没有免费恢复一阶角导数，也没有将候选的实际二阶导数换成 PDE 输出。

## 5. 可由已存全频缺陷支付的附加项

若已有同叶完整有限分子 $J_*\ge\|\widehat J\|_{A^0}$，则可取

$$
d_H^{(J)}=\frac{w_+J_*}{q_-l}.
\tag{99.22}
$$

若已有同一个候选的完整物理 Darboux 上界 $D_*$，则亦可取

$$
d_H^{(D)}=\frac{r_+E_*^2}{w_-l}D_*.
\tag{99.23}
$$

二者可以取最小值，因为它们围住同一个 $\widehat R_H$。若已有完整物理 $R_K$ 上界，可加入第三个同量上界。不能在不同候选、不同面板或不同 $x/r$ 单位之间取最小值。

R77 对零模的收紧可用于 (99.22)，但其余所有频率必须保留。普通非均值残差上界不能独自作为 $d_H$；完整标量均值残差还要以相同物理比例加入。

若后续对候选族作参数微分，(99.11) 的导数是

$$
D\widehat R_H[v]
=\frac{w}{r_x}
\left\{\frac{D\widehat J[v]}{\widehat L}
-\frac{\widehat J\,D\widehat L[v]}{\widehat L^2}\right\}.
\tag{99.24}
$$

分母差乘实际缺陷这一项必须保留。本定理是有限误差正矩阵，不是声称非精确候选的 Newton 导数已经支付；它不撤销 R75 中 $DW[v]\widehat R_K$ 的要求。

## 6. 接到已有外场范数与 R95

若真正完整的联合场误差已在同一个实位置证明

$$
\|\delta\overline K\|_{A_\tau^1}
+\|\delta P\|_{A_\tau^1}\le\varepsilon,\qquad \tau\ge0,
\tag{99.25}
$$

则最小非零频率为 $2$ 给

$$
(e_K,e_P,e_T,e_\theta)
\le \varepsilon(1/3,1/3,1,1).
\tag{99.26}
$$

式 (99.21) 因而成为一列可核销的物理导数预算：

$$
\boldsymbol\eta
\le \varepsilon\,\mathcal B(1/3,1/3,1,1)^\mathsf T
+(0,0,d_H,0,0)^\mathsf T.
\tag{99.27}
$$

若 R95 的参考是旧 R48 高度 $h_0$，而真解误差是相对新 carrier 候选 $\widehat h$，还必须加入已付的同位置五导数桥 $\boldsymbol\eta_0$：

$$
\boldsymbol\eta_{\text{R95}}
\le \boldsymbol\eta_0+\boldsymbol\eta.
\tag{99.28}
$$

$\boldsymbol\eta_0$ 须来自旧 R48→PA→CF 的实际自身导数比较；只共端点两 jet 不足以付内部差。PA→CF 的 v3 paired-mean 账本不能冒充旧 R48→CF 的全部差。

把 (99.28) 代入 R95 的非均匀公式即可。较简单的充分门是五项各不超过 $1/8192$，但无需把不同物理单位的五项人为合并为一个更粗范数。若这个充分门失败，只说明所用上界尚未付过；它不证明真曲率超预算。

### 完整高度、均值位置与几何

若还需高度位置，全部非零频率 $|m|\ge2$ 给

$$
\|\delta h^\perp\|_{A^0}
\le \frac{rw}{2}\|\delta P\|_{A^0}.
\tag{99.29}
$$

均值高度须另外使用同一个积分常数：

$$
\delta h_0(r)=\delta h_0(r_0)
+\int_{r_0}^r w(\rho)\delta c(\rho)\,d\rho.
\tag{99.30}
$$

现有五正积分里 $I_{00}+I_{01}=\int w\,dr$ 可以逐叶消费 (99.17)，不需要新积分。越过改造区间后的常数不能重新置零。参考 frame、位置差和真实法向的差还须经过已写的完整 frame 引理；本定理不会把一个非等距候选的参考向量宣布为真法向。

## 7. 实现、已核内容与未付内容

精确有理消费者是 [tail_r99_field_to_physical_jets.py](../computations/tail_r99_field_to_physical_jets.py)。它生成 (99.20) 的完整矩阵、完整均值差、保留的 $d_H$、五导数上界和条件 R95 门。输入使用精确整数、有理数字符串或分子/分母记录；浮点显示值不参与门。

脚本强制显式列出本定理的真解、同根、同 $g$、完整频谱和实际候选导数假设，但**布尔假设记录不是这些数学事实的证书**。输出始终标记真解及输入误差未由此消费者证明。代码尚未在恢复的 Python 执行器上做 AST/数值执行；执行计划保留该步骤。

独立纯 BigInt 多项式核对验证了：

1. 已冻结有限 $J$ 生产式中 $c,c_x$ 全项，与 (99.7) 展开逐单项式完全一致；
2. (99.9) 乘去共同正因子后的完整多项式差为零。

它只支付代数符号和均值项一致性，不支付真实外解、任意一条输入误差或实际曲率门。已有低投影辅助场和条件高块还不能单独作为 (99.25) 的完整误差证书。

原 PM/PA/R77 数据在 2026-11-12 执行器短暂恢复时已实际核出：原件仍在、原资源正式 $0$、原 PM/PA 各 $111$ 叶完整、全部相关原 SHA 一致。此后只读 schema 查询再次遇到 transport 失联。原 schema 的兼容读取必须从原件实读，不能根据重建版猜字段，更不能把原生产者哈希改成重建版。
