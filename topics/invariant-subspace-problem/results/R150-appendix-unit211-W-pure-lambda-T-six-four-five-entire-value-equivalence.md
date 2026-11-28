# R150：W 全原值子系统的纯 lambda,T 六次、四次、五次等价表示

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论与准确范围

在当前 W 的原互异两值、物理 $D\ne0$ 图上，
原值二、三矩、原 Delta 和完整 $N_4(V_{\rm val})$
可以同点改写成三个纯 $(\lambda,T)$ 多项式：
$$
\boxed{\qquad \mathcal R_6=0,\quad
\mathcal C_4=0,\quad \mathcal N_5=0.\qquad}            \tag{1}
$$
其总几何次数分别至多 $6,4,5$，系数的分母仅为先行已付纯权单位。
$\mathcal N_5$ 是下面完整定义和证明的新五次。
(1) 的正反恢复只使用当前原 $m,D,M,\ell,\Phi,Q$ 已付范围，
不倒 $b_0$、$A_*$ 或任一新多项式首项。

因此这份等价覆盖整个 $b_0=0$ 和其互补图。
它比先前只在 $b_0\ne0$ 恢复完整 N4 的三个四次更完整。
同时，(1) 只等价本篇列出的原值子系统，
**不宣称它已经包含原全部均值、NS/PS 或个别 N/P 条件**。

本篇是已刊原身份的完整纸面推导，没有新计算门。
没有再运行 native、大两列、旧 R6 投影或已成 b0 八阶结式。

## 2. 沿用的完整原身份

沿[两个原四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)
以及
[完整 N4 的 f 消失](R150-appendix-unit211-W-full-NV-f-independent-pure-lambda-T-quartic.md)，
使用同一点的原值中心 $s$ 和
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3.
$$
当前纯权量记为
$$
\delta=1-Q,\quad m=u-\ell,\quad M=\ell^2\delta-m^2=4bc\delta,
$$
$$
A_*=4uQ-J,\qquad C_*=A_*m^2+J\delta\ell^2,
$$
$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2\\
 &+2MuQ(3-2\lambda)\ell T+DC_*,\\
b_0={}&2m\{A_*T+uQ(3-2\lambda)\ell\}.
\end{aligned}
$$
原二、三矩及 Delta 的准确身份为
$$
q=Ms^2-D=\ell E_2,                                  \tag{2}
$$
$$
H=K-2mDs=\ell(2ms+3\ell+3T)E_2-\ell^2E_3,             \tag{3}
$$
$$
L=a_\Delta+Mb_0s,\qquad
\Phi L=M\ell^2E_\Delta-C_*\Phi q.                    \tag{4}
$$
没有把 q、H、L 的某个无来源消元式冒充原方程；
(2)–(4) 保留原组合。

完整原 N4 是同一个 s 上的二次：
$$
\widetilde N:=\ell^2N_4(V_{\rm val})
=Z_0+Mz_1s+Mz_2s^2.                                \tag{5}
$$
这里 $Z_0,z_1,z_2$ 均取已刊短式的准确自由 f 形式，
不是只保最高次或偶部。
由 (2)、(3)，不作任何除法即得到
$$
2mD\,\widetilde N
=2mD(Z_0+Dz_2)+MKz_1-Mz_1H+2mDz_2q.                \tag{6}
$$

## 3. 新五次的纯 f 系数消除

已刊纯四次纸证逐项给出了
$$
MQ[f]z_1=2b_0,\qquad
MQ[f](Z_0+Dz_2)=2a_\Delta.                          \tag{7}
$$
两者对 f 均至多一次，且 $D,K,a_\Delta,b_0$ 不含 f。
因此
$$
\begin{aligned}
[f]\{2mD(Z_0+Dz_2)+MKz_1\}
 &=\frac{4mDa_\Delta+2MKb_0}{MQ}\\
 &=\frac{2\mathcal C_4}{MQ},\\
\mathcal C_4&=2mDa_\Delta+MKb_0.
\end{aligned}                                      \tag{8}
$$
这不是仅某点的导数判断；一次性保证下面的完整相等。

记星号为准确 f 常数项，定义
$$
Z_*=Z_{0*}+Dz_{2*},\qquad
\boxed{\quad \mathcal N_5=2mD Z_*+MKz_{1*}.\quad}    \tag{9}
$$
星号量由前篇的自含式
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t_*=-\frac{P_c}{bcQ\Phi},\quad
V_*=-\frac GQ-\frac{P_c}{Q\Phi},\quad
W_*=\frac{T_0}{2},\quad A_{1*}=\frac{2G}{Q},
$$
$$
x_*=\frac{(u-\ell Q)V_*-mW_*}{M},\qquad
y_*=\frac{\ell W_*-uV_*}{M}
$$
完全确定。再记 $c_\lambda=3-2\lambda,\ w=\lambda-1-T$，则
$$
z_{1*}=-2(\ell c_\lambda+2T)y_*-2\ell w+mTt_*/\delta,
$$
$$
z_{2*}=2(\ell x_*-my_*-bc\,t_*),
$$
$$
Z_{0*}=\ell^2A_{1*}+2\ell uw(\ell c_\lambda+T)
 +2V_*(\ell^2+\ell c_\lambda T+T^2)
 +2bc\,t_*(T^2-\ell^2).
$$
这是原自由 f 公式的系数提取，不要求原物理解 f 为零。

由 (8) 得
$$
2mD(Z_0+Dz_2)+MKz_1
=\mathcal N_5+\frac{2f}{MQ}\mathcal C_4.             \tag{10}
$$
结合 (6)，得到新五次完整的原理想身份
$$
\boxed{
\mathcal N_5
=2mD\ell^2N_4(V_{\rm val})+Mz_1H-2mDz_2q
 -\frac{2f}{MQ}\mathcal C_4 .
}                                                   \tag{11}
$$
(11) 没有 D 逆，没有 b0 逆，也没有新头或范数逆。
它在已有纯权单位环中是原组合；随后用 D 非零只为正向恢复 N4。

所有 starred 恢复量对 $(\lambda,T)$ 仿射，
所以 $\deg Z_*\le3,\deg z_{1*}\le2,\deg D\le2,\deg K\le3$，
由 (9) 得 $\deg\mathcal N_5\le5$。
其分母仍全为已付纯权单位，绝无几何 D 分母。

## 4. 整图正反恢复证明

另两个纯值多项式是
$$
\mathcal R_6=MK^2-4m^2D^3,\qquad
\mathcal C_4=2mDa_\Delta+MKb_0 .
$$
在原 s 环中直接有
$$
\mathcal R_6=MH(K+2mDs)+4m^2D^2q,                  \tag{12}
$$
$$
\mathcal C_4=2mDL+Mb_0H.                           \tag{13}
$$
所以原 $E_2=E_3=E_\Delta=N_4(V_{\rm val})=0$
经 (2)–(4)、(11)–(13) 必给 (1)。

反过来，在当前已付 $mD\ne0$ 图，给满足 (1) 的同一个
$(\lambda,T,f)$，唯一取
$$
s=\frac K{2mD}.                                    \tag{14}
$$
这里没有再选一个独立根，也不把某个分母范数当作逆。
直接乘回：
$$
H=0,\qquad
q=\frac{\mathcal R_6}{4m^2D^2}=0,\qquad
L=\frac{\mathcal C_4}{2mD}=0.                       \tag{15}
$$
由 $\ell,M,\Phi$ 的已付范围，(2)–(4) 依次恢复
$E_2=E_3=E_\Delta=0$。
再用 (11) 和 (1)、(15)，得到
$$
2mD\ell^2N_4(V_{\rm val})=0,
$$
故完整 $N_4(V_{\rm val})=0$。
这证明了 (1) 与指定原值子系统在当前物理图上的双向等价。

D=0 的所有原值碰撞不在本篇恢复范围；
(11)–(13) 虽作为恒等式不倒 D，也不据此把此等价外推给碰撞图。
同样，原全部 Gram 条件仍需在恢复出的同一点另外满足。

## 5. 与纯四次及 b0 整支的准确关系

先前纯四次为
$$
\mathcal B=b_0Z_*-a_\Delta z_{1*}.
$$
用 (9) 直接展开，完整得到
$$
\boxed{\quad
b_0\mathcal N_5-\mathcal C_4z_{1*}=2mD\mathcal B .
\quad}                                             \tag{16}
$$
因此新 (1) 包含旧纯四次条件。
在 $b_0\ne0$ 图，(16) 也允许从旧 $\mathcal C_4,\mathcal B$
恢复 $\mathcal N_5$；但在 $b_0=0$ 上不允许这个反向除法。

在整个 b0 零支，原 $\mathcal C_4=0$ 和 D 单位先给
$a_\Delta=0$，从而旧 $\mathcal B=0$ 自动成立。
新 $\mathcal N_5$ 仍是保留完整原 N4 的独立必要输入，
不能因为旧 Bpure 此时自动为零而丢掉它。
沿已刊合法 $T=-uQ\ell(3-2\lambda)/A_*$ 恢复，
它变成次数至多五的同 lambda 多项式；
可以和原 aDelta 二次、完整 R6 六次作新的原返回。
这只说明后继合法输入，未预报其系数、结式、因式或排空。

## 6. 来源和执行状态

本篇全部推导依据：

- [完整 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)；
- [原值两个四次](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)；
- [完整 N4 的 f 消失与纯值四次](R150-appendix-unit211-W-full-NV-f-independent-pure-lambda-T-quartic.md)；
- [整 b0 支的原 78 次权曲线](R150-appendix-unit211-W-entire-b0-zero-original-78-weight-curve.md)。

式 (6)、(8)、(10)–(16) 已在正文逐项给出完整代数推导。
它们不依赖新工具输出，不等待附加复现门。
目前没有运行新五次投影，未计算新参数覆盖，也没有据本篇宣布整 W 空。
