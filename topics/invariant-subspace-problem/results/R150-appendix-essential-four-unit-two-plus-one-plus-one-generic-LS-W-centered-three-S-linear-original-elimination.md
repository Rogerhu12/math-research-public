# R150：一般 W 图中三条原 S 一次式及两个几何变量的完整二次系统降维

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 结论与未闭边界

在此前一般 LS、Delta=0、W=0 的剩余图上，使用已经支付的原物理单位、$H$、$\ell$、$\ell-u$、$u-Q$、$C_9$、$2u-1$ 等。权参数与物理坐标为
$$
e=u-1,\quad Q=ek,\quad V=(e+1)k+2,\qquad
\ell=\frac{u((k+2)^2-2ek)}{kV},
$$
$$
F=2f-u\lambda,\qquad S=T-2\lambda.
$$
此仿射坐标与原 $(x,y,t)$ 的双侧逆在整个图已证明，见
[原物理仿射坐标及 N1 的 S 二次项消去](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-centered-physical-coordinate-and-original-S-linear-row.md)。

本附录证明并实际返回：

- 现已付 $\ell$ 后，原 $E_1$ 的 $S^2$ 系数是单位。原四二次式等价于一条对 $S$ 首一的二次式和三条 $S$ 一次式。
- 三条一次式的 $S$ 系数分别对 $(F,\lambda)$ 仿射；其 $3\times3$ 系数矩阵的行列式只剩下文明确的 27 项多项式 $D_{27}(e,k)$ 未支付。
- 不除该行列式，原余子式组合直接给出三条 $\delta FS+B_F$、$\delta\lambda S+B_\lambda$、$\delta S+B_*$；$B_F,B_\lambda,B_*$ 都是不含 $S$ 的二次式。
- 同样不除 $\delta$，得到两条原三次式与一条原四次式，全部只含两个几何变量 $F,\lambda$。在 $D_{27}\ne0$ 图上，它们加 $S=-B_*/\delta$ 与原四二次式等价；$D_{27}=0$ 整支仍保留原四式及三条原余子式关系。
- 原 $N_s/P_s$ 已在同一个完整 Gram 中再生并核来源，但本次没有把它们的 $S$ 消元余式展开，也没有排空有限点。只列三条降式不等于完整原系统已解。

## 2. 原式及真正已付的 S² 系数

完整自含源重建同一个 $X,Y,t,f,\lambda,T$、原 Gram、$E_0/N_0/P_1$，核三 mean、原 $N_1$、加权 $N_s/P_s$、其通过 $HA/HB$ 返回原值式的迹，以及物理 $D$ 身份。没有用预先猜测的低次式替代这些原公式。

设
$$
L_\ell=2ek-(k+2)^2,\qquad
P_*=2ek-k^2-5k-8,
$$
$$
\begin{aligned}
M_{13}={}&4e^3k^2-3e^2k^3-12e^2k^2-16e^2k
+ek^4+8ek^3+24ek^2+32ek+16e\\
&-k^3-8k^2-20k-16.
\end{aligned}
$$
原权身份为
$$
P_{02}=-\frac{2e^2uP_*}{V},\qquad
M=4bc(1-Q)=-\frac{u^2M_{13}}{kV^2},\qquad
\ell=-\frac{uL_\ell}{kV}.
$$
因此 $P_*,M_{13},L_\ell$ 分别由原 $P_{02},bc$ 及已闭的整 $\ell=0$ 面支付；原 $e,k,u,V,k+4$ 也已付。

从完整原 $E_1$ 实际提取的系数为
$$
h=[S^2]E_1
=-\frac{2ekuV L_\ell P_*^2}{M_{13}(k+4)^2}. \tag{1}
$$
源码对分子、分母全部因式乘回，并对 $h$ 与 $h^{-1}$ 的分母逐项核验只含上述单位。故可以定义
$$
q_0=E_1/h=S^2+L(F,\lambda)S+C(F,\lambda), \tag{2}
$$
其中 $L$ 仿射、$C$ 二次。完整原迹为 $(h^{-1},0,0,0,0,0)$。

对原 $R_i=EBe,EBo,N_1$，先作
$$
\widetilde\ell_i=R_i-[S^2]R_i\,q_0. \tag{3}
$$
再只乘已付单位 $c_i$ 清分母及已付内容，记 $\ell_i=c_i\widetilde\ell_i$。源码保存 $c_i$ 及其逆的已付分母检查，并逐行乘回原六式的完整系数列；因此这不是只对某些投影点成立的关系。在当前局部环内，
$$
(E_1,EBe,EBo,N_1)=(q_0,\ell_0,\ell_1,\ell_2). \tag{4}
$$
每个 $\ell_i$ 均对 $S$ 一次、总几何次数至多二次。

## 3. 三个仿射系数与完整新参数边界

写
$$
\ell_i=(a_{iF}F+a_{i\lambda}\lambda+a_{i0})S+b_i(F,\lambda),
$$
其中 $a_{ij}$ 只含权参数，$b_i$ 二次。令
$$
A=(a_{iF},a_{i\lambda},a_{i0})_{i=0,1,2},
\qquad \delta=\det A. \tag{5}
$$
全部系数按 (3) 与源码已付归一化唯一定义。实际 $\delta$ 是双次数 $(28,36)$ 的参数多项式；不除它进行后续运算。

完整因子覆盖如下。按源码顺序剥已付因子的 gcd，实际非平凡循环次数是
$$
e:1,\quad k:4,\quad u:4,\quad V:4,\quad
P_{02}\text{ 的分子}:3,\quad M\text{ 的分子}:3,\quad
\ell\text{ 的分子}:2.
$$
每次 $g_j=\gcd(\text{当前多项式},\text{已付因子})$ 都检查商乘回，并检查最终所有乘积乘回原 $\delta$。最后准确剩余 $32D_{27}$，即完整恒等式
$$
\delta=32\left(\prod_jg_j\right)D_{27}. \tag{6}
$$
这里每个 $g_j$ 都是所列已付因子的约数，在当前局部环中是真单位；没有省略任何其余未付因子。

唯一未付因子为
$$
\begin{aligned}
D_{27}={}&16e^5k^4-4e^4k^5+32e^4k^4\\
&+2e^3k^6-12e^3k^5-96e^3k^4-384e^3k^3-384e^3k^2\\
&+3e^2k^6+8e^2k^5+60e^2k^4+384e^2k^3+1088e^2k^2+1024e^2k\\
&-10ek^5-28ek^4+48ek^3+64ek^2-512ek-768e\\
&-k^6-18k^5-120k^4-440k^3-1008k^2-1344k-768.
\end{aligned} \tag{7}
$$
其双次数 $(5,6)$、总次数 9、27 项。源码标准多项式字符串 SHA256 为
`171698e50a84a1bb7bf4c4f6f7d6514f48d10a39b86cc4f85c3c7f6c7b2b2b09`。
本附录不支付 $D_{27}$，也未返回其整条零曲线。

## 4. 不除行列式的全部原组合

定义
$$
(Q_F,Q_\lambda,Q_*)^T=\operatorname{adj}(A)(\ell_0,\ell_1,\ell_2)^T,
$$
$$
(B_F,B_\lambda,B_*)^T=\operatorname{adj}(A)(b_0,b_1,b_2)^T.
$$
全部 18 个双侧矩阵积
$$
A\operatorname{adj}(A)=\operatorname{adj}(A)A=\delta I_3
$$
均实际逐项核验。因而有完整原身份
$$
Q_F=\delta FS+B_F,\quad
Q_\lambda=\delta\lambda S+B_\lambda,\quad
Q_*=\delta S+B_* . \tag{8}
$$
三个 $B$ 均不含 $S$，几何次数不超过 2。源码将每条 $Q$ 的完整原六式系数乘回，而非只核其头系数。

接着有两条原三次组合
$$
G_F=FQ_*-Q_F=FB_*-B_F,
\qquad
G_\lambda=\lambda Q_*-Q_\lambda=\lambda B_*-B_\lambda. \tag{9}
$$
再由 (2)、(8) 得原四次身份
$$
\begin{aligned}
G_4
&=\delta^2q_0-(\delta S+\delta L-B_*)Q_*\\
&=B_*^2-\delta L B_*+\delta^2C.
\end{aligned} \tag{10}
$$
式 (9)、(10) 全部不含 $S$。源码既检查右端的相等，也直接核完整原六式组合；最后仅剥已付因子归一化，分母及比例因子的正反向检查俱全。

实际归一化输出规模如下：

| 原必要式 | 权双次数 $(e,k)$ | 几何次数 | 项数 | 完整原迹 |
|---|---:|---:|---:|---|
| $G_F$ | $(14,16)$ | 3 | 1335 | 已乘回 |
| $G_\lambda$ | $(12,15)$ | 3 | 1043 | 已乘回 |
| $G_4$ | $(24,29)$ | 4 | 6438 | 已乘回 |

三条标准输出 SHA256 依次为
`5e8efbf135baa4658e71bde18bbfdf6312e49720f5d8b1b821258cbae4f2fb97`、
`0de46bccae9db119280b906d957122ca108155a8f814eeff187978e743b3cb0a`、
`a62eb4b6f74c5b65777850e35c3916e725775f59b8491fdd52ad59ff750766fe`。
大系数多项式不另存缓存；公开自含源准确再生它们。

## 5. 非零图的双向返回与零图的保留

在 $D_{27}\ne0$ 图，(6) 使 $\delta$ 成为单位。若原四二次式为零，则 (8)–(10) 给 $G_F=G_\lambda=G_4=0$ 及 $S=-B_*/\delta$。

反过来，给定同一 $(F,\lambda)$ 满足这三条降式，定义同一个 $S=-B_*/\delta$。则 $Q_*=0$；由 (9)，$Q_F=Q_\lambda=0$。再由 $A(Q_F,Q_\lambda,Q_*)^T=\delta(\ell_0,\ell_1,\ell_2)^T$ 得三条 $\ell_i=0$；由 (10) 得 $q_0=0$。结合 (4)，全部四个原二次式返回。因此这是非零图上原四二次系统的等价消元，不是只取结式后另选相位解。

在 $D_{27}=0$ 图，从 (8) 仍有原必要式 $B_F=B_\lambda=B_*=0$，并保留原 $q_0,\ell_i$。式 (9)、(10) 在此仍为原必要式，但它们单独不是充分条件；不在此解 $S$，不删除该零纤维。

原加权 $N_s/P_s$ 必须在同一个恢复的 $S$ 上继续返回。本次源保留它们及其原值迹身份，未展开其关于 $S$ 的消元余式，未把仅有的四二次消元当作完整原 N/P 系统等价。

## 6. 实际执行与再生源

自含源：

`notes/2026-11-27-unit211-generic-LS-W-centered-three-S-linear-original-elimination-8542.py`。

Git blob `ba7a258674bfa7e9dac677c1e16adde5170e6900`，
15770 字节，SHA256：
`4da946c486a2e3ca9b22faa16df13f8e24068ea390eed52135a1f2e49dcd6a30`。

唯一首次实际 Actions 为 run **45967269487**、job **140398862236**。源耗时 **4.295034424 秒**，驱动 **4.369695979 秒**，最大子进程 RSS **90176 KiB**，退出码 **0**，边界 180 秒、4 GiB。stdout **11545 字节**，SHA256：
`1b8315a93284979b8812039da358cbd769f7e828d254b2e2291c77617c5e2a48`。

实际 pull 于 2026-11-27 08:38:58.346089 UTC，前后均为
`7fa9ee46b275f29803d8e1cbd4c7774d93b5880f`。
根 README blob `282e86b03385d3b6245ce7100ae2e2af7b103c2d`，
课题 README blob `5fbd905291dd044c88d35bd9c07ac0e586ff795a`，均未变化。

本次没有重跑旧参数 cofactor、旧 Gröbner 门或六行头 atlas。新数学输入是全部原 $S$ 一次行的 $3\times3$ 系数矩阵及 (8)–(10) 的小原组合。一般 W 的全部有限原返回仍须继续，普通 ISP 未因本附录达到完成标准。

