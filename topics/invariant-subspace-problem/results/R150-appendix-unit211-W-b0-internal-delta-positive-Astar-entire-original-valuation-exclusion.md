# R150：W/b0 内部 delta 正估值的整个 Astar 正阶分支排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**结论。** 当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图，在剩余特征1009的赋值下不存在
$$
v(e)=v(k)=v(u)=0,\qquad v(\delta)>0,\qquad v(A_*)>0
\tag{1}
$$
的原解。这里 $u=e+1,Q=ek,\delta=1-Q$。证明允许 mu 的任意极点、零值、正阶与单位；不用 Astar 的首值作逆，不要求固定的权首项为非零。

这是新的完整纸面分层。关键是完整原 N5 在 $T$ 极点上的准确一阶式；没有运行局部 jet、因式、投影、旧初始理想或任何复算门。本稿只关闭 (1)，其他 delta 正估值的一般有限 mu 图仍保留。

## 1. 完整原定义与 Astar 零剩余曲线

使用 [完整 b0/N5 原源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**、SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8** 的准确同点定义。只引用已经成立的原必要性，不重新执行其两个标量或 QQ gcd。

记
$$
\begin{gathered}
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad m=u-\ell,\quad
M=\ell^2\delta-m^2,\quad bc=M/(4\delta),\\
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,\\
\mu=2\lambda-3,\quad
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,\\
A_*T=uQ\ell\mu,\quad
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3 .
\end{gathered}
\tag{2}
$$
当前 b0 的 Astar 是物理非零量；这里只使用其准确正阶，不把它当作赋值环单位。原 q2、R6 为
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,
\qquad R_6=MK^2-4m^2D^3=0.
\tag{3}
$$

设 $U=\bar u\ne0,1$。由于 Q 剩余为1，
$$
\bar k=\frac1{U-1}.
$$
若 ell 有极点，$A_*=-Q\ell+2u+2u^2+4u(Q-1)$ 也有同阶极点，与 (1) 冲突。因此 ell 整。若 U=2/3，W 的 ell 分子剩余非零、分母剩余为零，又迫 ell 有极点，故 U 不等于2/3。于是
$$
\ell_0=\frac{U(2U^2-1)}{3U-2},\qquad
(A_*)_0=\frac{U(4U^2+2U-3)}{3U-2}.
$$
整个 (1) 迫
$$
F(U):=4U^2+2U-3=0,\quad
L:=\ell_0=2U(U+1),\quad
m_0=-U(2U+1).
\tag{4}
$$
F 与 $U,U-1,U+1,2U+1,2U-1,3U-2$ 均无共同根于特征1009。故 ell、m、M 均为赋值环单位，且 $M_0=-m_0^2$。

原参数
$$
T_0=2u-\ell Q-2u^2,\quad
\Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3
$$
在 (4) 上满足
$$
(T_0)_0=-4U^2,\qquad
\Phi_0=6(U-1),\qquad
(P_{02})_0=2U(U-1)(2U-1).
\tag{5}
$$
所以 T0、Phi、P02 的剩余也非零。以下所有 m、M、Phi 分母都是赋值环单位；唯一需要追踪的 Astar 和 delta 则始终保留其准确正阶。

## 2. 完整 N5 在 T 极点上的统一一阶式

准确定义
$$
\begin{gathered}
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,\\
t_s=-P_c/(bcQ\Phi),\quad
V_s=-G/Q-P_c/(Q\Phi),\quad
y_s=(\ell T_0/2-uV_s)/M,\quad
w=\lambda-1-T,\\
z_1=-2(-\ell\mu+2T)y_s-2\ell w+mTt_s/\delta,\qquad
z_2=-2G/Q-4my_s,\\
Z_0=2(T-\ell\mu)(\ell u w+V_sT)+2bc\,t_sT^2,\\
N_5=2mD(Z_0+Dz_2)+MKz_1.
\end{gathered}
\tag{6}
$$
这些是完整原 N5 的 f 常数表达，不是原物理 f=0。其来源
$$
N_5=2mD\ell^2NV+Mz_{1,\rm full}H
       -2mDz_{2,\rm full}q-\frac{2f}{MQ}C_4
\tag{7}
$$
在当前同点 b0、q2 下给 N5=0；没有把不同原值的必要范数当成同根充分性。

现在只在实际 T 有极点时置
$$
\xi=\mu/T,\qquad \eta=1/T.
$$
下面的有理多项式身份也可把 xi、eta 视为形式变量；其系数只用本节已证单位作分母。定义
$$
\begin{aligned}
\widehat G&=G/(QT)
 =\frac{P_{02}}{2Q}\xi+
   \frac{3P_{02}/2+(u-1)T_0}{Q}\eta,\\
\widehat P&=P_c/(Q\Phi T)
 =\frac{P_{02}}{\Phi}(1+\ell\eta)-\frac{T_0}{\Phi}\widehat G,\\
\widehat w&=w/T=-1+(\xi+\eta)/2,\qquad
\widehat y=y_s/T
 =\{\ell T_0\eta/2+u(\widehat G+\widehat P)\}/M .
\end{aligned}
\tag{8}
$$
由完整 (6)，逐项而非按猜测最高次得到
$$
\begin{aligned}
\widehat z_2:=z_2/T&=-2\widehat G-4m\widehat y,\\
\widehat z_1:=z_1/T^2
 &=2\ell\xi\widehat y-4\widehat y
       -2\ell\widehat w\eta-4m\widehat P/M,\\
\widehat Z_0:=Z_0/T^3
 &=2(1-\ell\xi)(\ell u\widehat w\eta-\widehat G-\widehat P)
      -2\widehat P.
\end{aligned}
\tag{9}
$$
特别 $mTt_s/\delta$ 在这里精确变成 $-4m\widehat P/M$；没有余下 delta 逆。

又
$$
\widehat D:=D/T^2
=-1+\ell(\xi^2/2+2\xi\eta+5\eta^2/2),
$$
$$
\widehat K:=K/T^3
=2-3\ell(\xi^2/2+2\xi\eta+5\eta^2/2)
 +\ell^2(\xi^3/2+3\xi^2\eta+6\xi\eta^2+7\eta^3/2).
\tag{10}
$$
于是
$$
N_5/T^5=2m\widehat D(\widehat Z_0+\widehat D\widehat z_2)
                  +M\widehat K\widehat z_1.
$$
模 delta，$M=-m^2$；模 $(\xi,\eta)^2$，$\widehat D=-1,\widehat K=2$。把 (8)、(9) 代入后，常数项整式相消，线性项准确为
$$
\boxed{\quad
\frac{N_5}{T^5}
=4\ell^2\left(m\eta+\frac{P_{02}}{\Phi}\xi\right)
       +\mathcal E,\qquad
\mathcal E\in(\xi^2,\xi\eta,\eta^2,\delta).
\quad}
\tag{11}
$$
这里理想系数在包含上述权单位逆的整局部环中。一个直接核对方式是先以 $\widehat D=-1,\widehat K=2,M=-m^2$ 代入；未取线性部分前的表达式为
$$
4\ell^2\left\{
m\widehat w\eta(-1+u\xi)
 +\xi(\widehat G+\widehat P+T_0\eta/2)
\right\}.
$$
其线性项就是 (11)；替换 D、K 和 M 的误差全部落在显示的余项理想。因而 (11) 保有极点的所有原 N5 项，不是只保其中 Z0 或某个奇部。

## 3. R6 的完整极点比较式

定义
$$
\mathcal C_3=
4B_3T^3-3A_2^2T^2-6\ell A_2B_3T
                    +\ell^2B_3^2+4\ell A_2^3 .
$$
直接展开有
$$
K^2+4D^3=\ell^2\mathcal C_3,\qquad
R_6/\ell^2=\delta K^2-m^2\mathcal C_3.
\tag{12}
$$
此处 ell 是赋值环单位。记
$$
b=v(A_*)>0,\qquad d=v(\delta)>0,\qquad s=v(\mu).
$$
当 mu 非零时，由原 b0，
$$
v(T)=s-b,\qquad v(\xi)=b.
\tag{13}
$$
mu 恰零时 T=0，原 q2 中 $2M\ell Q(3-4\lambda)=-6M\ell Q$ 是唯一单位项，直接矛盾；以下无需预先把 mu 付成单位。

## 4. mu 极点全部排除

设 s<0。则 T 的极点比 mu 更深。K 的唯一最低项是 $2T^3$；在 $\mathcal C_3$ 中，唯一最低项为 $4B_3T^3$，因为
$$
v(B_3)=3s,\quad v(A_2)=2s,\quad v(T)=s-b.
$$
这两个最低项系数均为1009单位。原 (12) 两项同阶强迫
$$
d=3b .
\tag{14}
$$
在 (11) 中，xi、eta、delta 的阶分别为
$$
b,\quad b-s>b,\quad 3b.
$$
余项的每项都比 xi 高阶。因此
$$
\frac{N_5}{\mu T^4}
\longrightarrow
4L^2\frac{(P_{02})_0}{\Phi_0}
=\frac43\,UL^2(2U-1)\ne0.
\tag{15}
$$
这与原 N5=0 矛盾。mu 的任意深极点全部排除，不需要再确定 $v(\mu)$ 与 b 的比例，也没有对未付的 mu 头作逆。

## 5. mu 正阶全部排除

设 s>0。若 s 大于等于 b，则 T 整。Cstar 的阶为正，原 q2 的第一项和 T 平方项都为正阶；第二项的剩余为 $6m_0^2L\ne0$，矛盾。

若 $0<s<b$，T 有极点，而 $A_2\to5/2,B_3\to7/2$ 均为单位。q2 中第一项仍为正阶，第二项为单位，故第三项也必须为单位：
$$
d=2(b-s).
\tag{16}
$$
另一方面，K 最低项是 $2T^3$、$\mathcal C_3$ 最低项是 $4B_3T^3$，(12) 迫
$$
d=3(b-s).
\tag{17}
$$
(16)、(17) 与 s<b 冲突。故所有 mu 正阶也排除。

## 6. mu 为单位：只余负三除以二，再用完整 N5

设 s=0，T 的阶为 -b。

若 $\bar\mu\ne-3/2$，原 q2 的第二项是单位，第一项为正阶，第三项阶为 d-2b；因此只能 d=2b。然而 K 的阶为 -3b，$\mathcal C_3$ 的阶至少 -3b。于是 (12) 第一项阶 -4b，第二项阶至少 -3b，不可能相消。该支排除。

故只余 $\bar\mu=-3/2$。此时 $B_3\to-7/16$ 是单位，所以 K、$\mathcal C_3$ 的唯一最低项仍分别为 $2T^3$、$4B_3T^3$；原 R6 迫
$$
d=3b.
\tag{18}
$$
在 (11) 中 xi 与 eta 同阶 b，且 $\xi/\eta=\mu\to-3/2$；二次余项和 delta 都严格更高。因此
$$
\frac{N_5}{T^4}
\longrightarrow
4L^2\left(m_0-\frac32\frac{(P_{02})_0}{\Phi_0}\right)
=-2UL^2(6U+1).
\tag{19}
$$
这仍非零。事实上若 6U+1=0，则
$$
F(-1/6)=-29/9\ne0
$$
于特征1009，和 (4) 冲突。故最后一个单位 mu 支也排除。

## 7. 覆盖与限定

mu 恰零、正阶、单位和任意极点已经全部处理。所有需要 T 非零或有极点的归一都在该分支先由原 b0/q2/R6 推出；(11) 的余项逐项给出，未预设 T 或 mu 的分歧形式。F 的全部剩余根同时覆盖，未选一个数值根，也不要求 F 在剩余域不可约。

因此 (1) 的整个 Astar 正阶边界为空。这个结论来自准确同点原 q2/R6/N5，既没有令原物理 f 为零，也没有把非零但正阶的 Astar 当单位。其他 delta 正估值分支保留；没有新的全 W 空性、点数或 Artin 长度声明。

**执行说明。** 本文没有新脚本或实际运行，没有重算既有标量、投影、初始理想、局部 jet 或系数证书。第2节是完整原 N5 的新显示恒等式及余项理想；其余为原式上的完整估值证明。
