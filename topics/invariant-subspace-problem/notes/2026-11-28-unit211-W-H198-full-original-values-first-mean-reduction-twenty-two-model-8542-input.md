# R150：H198 补图的完整原值二十行二列新模型

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。源尚未执行。

## 1. 更小的精确 I6 表示

沿已完成的 N1 斜率坐标和 H198 非零补图，置 $R=A_W[H198^{-1}][\lambda]$。坐标为

$$
n=p_0+p_1x+p_2y,\quad z=ax+cy,\quad
\Delta_N=ap_2-cp_1,\quad
\hat x=(p_2z+cp_0)/\Delta_N,\quad
\hat y=(-p_1z-ap_0)/\Delta_N.
\tag{1}
$$

$\Delta_N$ 是图内纯权单位，$p_1=a\lambda+b,p_2=c\lambda+d$；$n=N_1+\sum_{i=1}^3\nu_iF_i$，$F_i$ 为三条原均值。此前原源已实际返回 $z$ 的首一平方

$$
q_z=z^2+\beta_1(\lambda)z+\beta_0(\lambda)\in(F_1,F_2,F_3,N_1).
\tag{2}
$$

换基可逆，消去 n 后将三个均值代入 (1) 得到

$$
\widetilde F_i=A_i z^2+B_i z+C_i.
$$

由此前 z 平方的真实均值迹，源码实际检查

$$
q_z=-\sum_i\theta_i\widetilde F_i,\qquad
N_1(\hat x,\hat y)=-\sum_i\nu_i\widetilde F_i.
\tag{3}
$$

这里 $\theta_i$ 是此前真实 $z^2$ 均值约化乘子，没有新增单位。定义

$$
\ell_i=\widetilde F_i-A_iq_z.
$$

它们对 z 至多一次；(3) 与反向 $\widetilde F_i=\ell_i+A_iq_z$ 给出完整理想等式

$$
(\widetilde F_1,\widetilde F_2,\widetilde F_3)
=(q_z,\ell_1,\ell_2,\ell_3).
\tag{4}
$$

令明确自由二次环境 $S=R[z]/(q_z)$。其内任意由若干线性元素 $r_j$ 生成的理想，作为 R 模精确由 $r_j,zr_j$ 生成，因为 S 由 $1,z$ 生成。故完整 I4 商由三条 $\ell_i$ 及各自 z 倍给出精确六行二列。

对同一点原 $N_S,P_S$，先按三条均值降到 $(1,x,y)$，再用 (1) 变为线性余式 $r_S,r_P$。其与原 NS/PS 的差属于 I4。因此加入 $r_S,zr_S,r_P,zr_P$ 后，完整

$$
I_6=(F_1,F_2,F_3,N_1,N_S,P_S)
$$

给出精确十行二列表示。这不是删掉旧十五行中的某些必要交换子；是通过 (3)–(4) 直接给出整个原理想的双向表示。原 I6 商仍不要求自由。此前已完成十五行二列及两条本原六次式的结果保持成立，本次不重跑那两个 cofactor。

## 2. 五个完整原值条件

在相同原变量与权量中记

$$
\begin{gathered}
m=u-\ell,\quad \delta=1-Q,\quad M=4bc\delta,\\
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3.
\end{gathered}
\tag{5}
$$

以下全部式保持原同一点的值，未倒置 D 或任何 D 范数。第一条是已刊原 C4 的首一 T 四次式。定义

$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2,\quad c=3-2\lambda,
$$

$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQc\ell T+C_*D,\quad
b_\Delta=2Mm(A_*T+uQc\ell),
$$

$$
q_{T,4}=\frac{2mD a_\Delta+K b_\Delta}
 {8muQ\ell^2\delta}.
\tag{6}
$$

分母仅为当前已付权量。第二条保完整两矩条件：

$$
R_6=MK^2-4m^2D^3.
\tag{7}
$$

设 $n_b,p_b$ 分别为原 $N_4(\mathrm{row}_B)$、$P_2(\mathrm{row}_B)$ 在 $\rho^2=\delta$ 中的完整 $\rho$ 奇部系数，$A_0=1+T/\ell$。第三、四条是此前已刊 D 降幂后的个别原式：

$$
N_{\rm low}=Dn_b+\frac{2\lambda P_{02}}mKA_0
 +\frac{4\lambda P_{02}m}{\ell M}D^2,
\tag{8}
$$

$$
P_{\rm low}=Dp_b+\frac{3P_{02}}{2m}KA_0^2
 +\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD
 +\frac{6P_{02}m}{\ell M}A_0D^2.
\tag{9}
$$

最后一条保整个原 $N_4(V)$，没有换成某个 $\Phi$ 倍数。原二次型以

$$
V_0=(1,\lambda-1-T,1+T/\ell,1+T/\ell),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho)
$$

定义

$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2.
$$

三个量均为 rho 偶部；源码实际核出奇部为零。使用

$$
V_{\rm low}=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}.
\tag{10}
$$

式 (6) 沿已发表的原 C4/E2/E3/两线恒等式。式 (7)–(10) 的定义与已刊原 D 降幂源 [2026-11-27-unit211-W-global-monic-T3-D-linear-eleven-by-six-original-return-8542.py](2026-11-27-unit211-W-global-monic-T3-D-linear-eleven-by-six-original-return-8542.py) 完全一致；本次不运行该旧门。

这些条件的原值意义也可直接核明。置 $s=(\ell\zeta-T)/u$；完整两个矩条件给

$$
Ms^2=D,\qquad 2mDs=K.
$$

因此原单值为 $h=A_0+ms/\ell-\rho s$、$k=A_0+ms/\ell+\rho s$。原个别 N 残式的 rho 奇部是

$$
n_b+4\lambda P_{02}(A_0s+ms^2/\ell),
$$

P 残式的 rho 奇部是

$$
p_b+P_{02}\bigl(3A_0^2s+6A_0ms^2/\ell
 +(3m^2/\ell^2+\delta)s^3\bigr).
$$

分别乘 D 并用两个矩身份，恰得到 (8)、(9)。整个 $N_4(V_0+sV_1)$ 乘 D 后同理恰为 (10)。这是完整原奇部与完整原二次型，未用某个选择性的 trace 代替。

在原 $D\ne0$ 图，$s=K/(2mD)$ 唯一；(7) 迫 $Ms^2=D$。原 NS/PS 的加权残式分别为 $\ell$ 倍偶部加 m 倍奇部，所以 (8)、(9) 连同 NS/PS=0 和已付 $\ell\ne0$ 恢复两对个别原 N/P。这里的 D 非零只用于等价范围；新代数构造没有倒置 D 或其范数。

为避免任何命名歧义，本稿所构造的确切理想始终显式定义为

$$
I_{11}=I_6+(q_{T,4},R_6,N_{\rm low},P_{\rm low},V_{\rm low}).
\tag{11}
$$

新精确模表示首先是 (11) 的表示，不把必要式擅自外推一般碰撞图。

## 3. 先原均值降次，再一次换坐标

若直接在 (2) 中堆叠 T 六次，可能重复引入 H198 高次分母。本次每个新值先在已实际返回的原三生成元 $(1,x,y)$ 中构造。设原真实矩阵满足

$$
xv=M_xv+E_xF_{\rm mean},\qquad
yv=M_yv+E_yF_{\rm mean}.
$$

对两个已具有原均值来源的线性余式 $a v,b v$，固定乘法取

$$
c=a\,(b_0I+b_1M_x+b_2M_y).
\tag{12}
$$

原线性多项式乘积与 $cv$ 的差恰为

$$
\sum_i a_i(b_1(E_x)_i+b_2(E_y)_i)F_{\rm mean}.
\tag{13}
$$

将两输入已有来源一起组合即得完整乘法 DAG。无需假设 $M_x,M_y$ 在自由三维空间交换，亦不假设余式唯一或三生成元自由。相同固定表达式的归纳已经足够。

新原 Gram 基础输入 $T,n_b,p_b,Z_0,Z_1,Z_2$ 先经过同一物理 lambda 可逆代入，再实际逐项核回原三均值约化。式 (6)–(10) 的每个加法、乘法和已付权除法继承 (12)–(13) 的原来源。所有这些计算只用原三规则，尚未倒置 H198。

每个完整新值最后只作一次 (1) 换基。若三行是 $r=(r_0,r_1,r_2)$，令

$$
s_0=r_0+(cr_1-ar_2)p_0/\Delta_N,\quad
s_1=(p_2r_1-p_1r_2)/\Delta_N,\quad
\kappa=(-cr_1+ar_2)/\Delta_N.
$$

源实际核回三个系数，故该新值与 $s_0+s_1z$ 的差位于 I4。每条加入这个线性行及其 z 倍

$$
z(s_0+s_1z)\equiv-\beta_0s_1+(s_0-\beta_1s_1)z\pmod{q_z}.
\tag{14}
$$

式 (14) 与 $s_1q_z$ 的精确乘回均实际检查。结合第一节的十行，即得 (11) 的精确二十行二列表示。没有把 I11 商称为自由二维模。

## 4. 唯一新标量目标与所有零支

在二十行全部构造完成后，固定仅尝试两对新的原行：

- $R_6,V_{\rm low}$；
- $N_{\rm low},P_{\rm low}$。

对二列行 A、B，只从两个实际乘子 $(B_1,-A_1)$ 共同约去 gcd，再逐项返回 $(C,0)$。随后只剥当前权单位及本节明确的 H198 补图因子。所有未付 scalar 内容、lambda 首项零和整条 H198=0 均保留；不是对旧 Norm、旧十二结果式或旧十八行 module 换算法续跑。

新源：

2026-11-28-unit211-W-H198-full-original-values-first-mean-reduction-twenty-two-model-8542.py

14921 字节，SHA-256：

f6f07b2f3fdb50f59565ef6501cbc2121d5882ce7cb32f7d17a4a1d2d139b6a1

固定 180 秒 / 4 GiB，尚未执行。signal.alarm 与 signal.setitimer 同时钳制到初始绝对截止。仅依赖 N1 slope 源、三均值源、physical-lambda 源与原 C9 Gram 源四件已冻结小源码；只执行必要前缀，不执行旧因式或计算尾段。大系数与展开最终迹均不保存、编码或分片。

本次纸面 (3)–(4)、(12)–(14) 给出了准确原输入与精确表示证明；具体二十行系数、两个新标量与实际退出状态等待唯一首次运行。
