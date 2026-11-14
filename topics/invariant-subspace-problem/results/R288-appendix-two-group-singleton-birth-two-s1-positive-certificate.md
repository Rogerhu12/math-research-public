# 两普通组加一异常位：出生二真实创新 S1 的严格全参数证书

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下所列范围的 S1 已证明。** 这里证明的是一般相邻序所需的更强三次桥费用，不把已知“两普通组加一异常位”的普通相邻序重新登记。本稿处理两个普通组长度 $q,L\ge3$、任意三个正权，以及两组置换固定部分的相对出生二；第二异常位的完整四维首边仍须支付 S2。普通 ISP、原无限尾及原 graph 逆传播均没有在这里关闭。

## 1. 物理命题与合法高度

取 $q$ 个权 $a>0$ 的物理位、$L$ 个权 $1$ 的物理位和一个权 $u>0$ 的异常位，记
$$
z=a^2,\qquad w=u^2,\qquad d=\sum_i b_iE_i,
\qquad C=\sum_i b_i^3E_i.
$$
先将整个物理空间限制到两个普通组的共同置换固定部分。这个子空间同时约化 $d,d^*,C,C^*$、各完整层 Gram 和它们的逆。

记 $K$ 为该部分的相对出生二 primitive 空间，$L_-$ 为相对出生一 primitive 空间。两者的维数均为二；完整出生层的维数分别是五和三。令
$$
G_j=\Gamma_{j,2},\qquad L_j=\Gamma_{j,1},\qquad
\Gamma_{j,s}=P_{K_s}\left(\frac{d^j(d^*)^j}{(j!)^2}\right)^{-1}\bigg|_{K_s},
$$
其中始终先取完整物理层的逆。

旧上出生的高度为 $q+L-3\ge3$，故 $G_1,G_2$ 合法；旧下出生高度为 $q+L-1\ge5$，故 $L_1,L_2,L_3$ 合法。深出生为真空，第四阶亦合法。置
$$
C_1=G_1^{-1},\quad C_2=G_2^{-1},\quad
B=C|_K:K\longrightarrow L_-,
$$
$$
\Delta=\frac12(C_1B^*L_3-B^*L_2).
$$
**定理。** 对全部 $q,L\ge3$ 和全部 $z,w>0$，上述整个真实二维源上严格有
$$
\boxed{C_1^2-C_2-\Delta L_3^{-1}\Delta^*>0.}
\tag{1.1}
$$
这正是 R275 的 S1，包含真实桥费用。$B^*$ 是原 Hilbert 伴随，不能用任意源坐标中的普通转置替代。

## 2. 共同聚合坐标与两个实际源

使用[八维完整逆表示](R273-appendix-eight-dimensional-aggregate-polynomial-gram.md)同样的去权后聚合坐标，这里只有三个占据分量
$$
I=(r,b,\ell),\qquad b\in\{0,1\},
$$
$$
p_I=\binom qr\binom L\ell z^rw^b,
\qquad g_I=\binom qr\binom L\ell a^ru^b f_I,
\qquad\|f\|^2=\sum_I|g_I|^2/p_I.
\tag{2.1}
$$
在一层取共同源多项式
$$
E_1:\ (x-t),\ (y-t),
$$
在二层取
$$
E_2:\ (x-t)^2,\ (x-t)(y-t).
\tag{2.2}
$$
这些是聚合系数中的常数整数源矩阵。它们均被 $\partial_x+\partial_y+\partial_t$ 消去，且穷尽对应三维、五维层的完整 primitive 核。

对 $s=1,2$ 定义
$$
(v_I)_O=\prod_{j=1}^3\binom{I_j}{O_j},\qquad |O|=s,
$$
$$
\mathcal F_{s,n}=\sum_{|I|=s+n}p_Iv_Iv_I^*,
\qquad H_n=E_2^*\mathcal F_{2,n}^{-1}E_2,
\qquad \Lambda_n=E_1^*\mathcal F_{1,n}^{-1}E_1.
\tag{2.3}
$$
求和始终限于真实合法占据。证明与所引稿完全相同：$D^n/n!$ 在聚合坐标中就是包含矩阵 $v_I$，输入度量为 $P^{-1}$，故最小费用必须先取 (2.3) 的完整五维或三维逆。

特别
$$
H_0=E_2^*P_2^{-1}E_2,
\qquad \Lambda_0=E_1^*P_1^{-1}E_1
$$
是非正交源的真实物理度量，后续没有将它们置为单位阵。

在聚合坐标中，实际三次下降变成
$z\partial_x+w\partial_y+\partial_t$。因此从二层源到一层源的准确桥及继续到真空的桥分别为
$$
\boxed{
K_B=\begin{pmatrix}2(z-1)&w-1\\0&z-1\end{pmatrix},
\qquad K_-=\begin{pmatrix}z-1&w-1\end{pmatrix}.}
\tag{2.4}
$$
于是连续两次真实桥为
$$
\boxed{K_Y=K_-K_B=2(z-1)\begin{pmatrix}z-1&w-1\end{pmatrix}.}
\tag{2.5}
$$
深出生第四阶 Gram 是
$$
\Gamma_{4,0}=e_4(z^{[q]},1^{[L]},w)^{-1}.
\tag{2.6}
$$

## 3. 用真实三塔身份消去上出生完整逆

[一般 S1 三塔 Schur 消元](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md) §6 已证明任意共同非正交源的准确二次型身份。它的推导保留非primitive Schur 源、完整第三阶逆及 $C^2$ 的深出生塔；这里使用其完整结论，不将旧普通相邻界当成创新费用的估计。

写
$$
S=qz+L+w,\qquad
\widehat H=E_2^*P_2^{-1}
\operatorname{diag}\bigl(S-2(rz+bw+\ell)\bigr)E_2,
$$
$$
\widehat F_2=E_2^*P_2^{-1}\mathcal F_{2,2}P_2^{-1}E_2,
\qquad M=K_B^*\Lambda_2K_B,
\qquad N=K_B^*\Lambda_2\Lambda_3^{-1}\Lambda_2K_B.
\tag{3.1}
$$
这里 $\widehat F_2$ 是完整物理 $d^2(d^*)^2/4$ 的压缩，**不是** $H_2^{-1}$。

所需 S1 二次型准确为
$$
\boxed{\begin{aligned}
\mathcal E={}&\widehat H H_0^{-1}\widehat H-\widehat F_2
-MH_0^{-1}M+2N\\
&+\frac{K_Y^*K_Y}{4e_4(z^{[q]},1^{[L]},w)}.
\end{aligned}}
\tag{3.2}
$$
它正是 $E_{2,\rm phys}^*(C_1^2-C_2-\Delta L_3^{-1}\Delta^*)E_{2,\rm phys}$。最后一项在一般出生二确实存在，不能删除。

为核对不同坐标写法，也可从完整 $H_1,H_2,\Lambda_2,\Lambda_3$ 直接构造
$$
\Delta_{\rm coord}=
\tfrac12(H_1^{-1}K_B^*\Lambda_3-H_0^{-1}K_B^*\Lambda_2),
$$
$$
D_{\rm coord}=H_1^{-1}H_0H_1^{-1}-H_2^{-1}
-\Delta_{\rm coord}\Lambda_3^{-1}\Delta_{\rm coord}^*.
$$
两式准确关系为
$$
\boxed{\mathcal E=H_0D_{\rm coord}H_0.}
\tag{3.3}
$$
所以 (3.2) 保持实际源度量，严格正性与 (1.1) 完全等价。

## 4. 覆盖全部参数的精确正系数证书

交换两个普通组并整体缩放，可取 $z\ge1$。S1 在整体权乘常数 $c>0$ 时乘正因子 $c^4$，所以这不损失任何原正权模型。写
$$
q=3+Q,\quad L=3+R,\quad z=1+Z,\quad w=V,
\qquad Q,R,Z\ge0,\quad V>0.
\tag{4.1}
$$
实际 $Q,R$ 是整数；证书会证明更大的实域。所有 (3.2) 所需的实际计数阶数至多四，故 $\binom{3+Q}{k}$、$\binom{3+R}{k}$（$0\le k\le4$）都有非负系数。完整 $\mathcal F_{s,n}$ 因而是非负系数权乘固定列 Gram 的和；其基点 $Q=R=Z=0,V>0$ 是合法严格正定模型。由单调增加正半定项，它们在整个 (4.1) 上严格正定。

因此 (3.2) 的所有原分母——物理对角 $P_s$、完整层行列式、$\det H_0$、$\det\Lambda_3$ 及 $e_4$——均不为零且有确定正号。逐次约分后的分母是这些非零因子的约因子，在该连通域的符号由一个内点确定。

[完整精确生成器](../notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py)执行以下有限有理运算：以 (2.1)–(2.3) 生成完整核；先精确移除每行的 $p_O$；在仍保留 $P_s^{-1}E_s$ 的右端上做 fraction-free 消元；逐除法核余数为零；按 (3.1)–(3.2) 构造二阶 Hermitian 矩阵；最后生成其首前导元素及行列式。没有数值求逆、浮点特征值或有限参数采样参与符号判断。

运行

```text
python 2026-11-14-two-group-singleton-bridge-certificates-789f-next.py --target s1-direct
```

得到如下完整结果。分子已按其分母在 $(Q,R,Z,V)=(1,1,1,1)$ 的符号作共同符号规范；未使用的第五代数变量 $U$ 不影响任何式子。

| 前导主子式 | 分子项数 | 分子总次数 | 分母项数 | 分母总次数 | 负系数项数 | 仅含 $V$ 的严格正项 |
|---|---:|---:|---:|---:|---:|---|
| 一阶 | 14,040 | 40 | 10,297 | 38 | 0 | 有 |
| 二阶 | 23,778 | 46 | 13,296 | 42 | 0 | 有 |

两分子的完整规范项序列 SHA-256 分别为

```text
adb06b67833688372befc3abc54e7099a34deed76e2183c07341b5ea823976b1
72b66b43024233b4caa9f5847af40c0e6353d46dd3b717cf67a77fb1b8f410cc
```

每个分子都是非负系数多项式，而且至少有一项在 $Q=R=Z=0,V>0$ 仍严格正，所以两个主子式在整个 (4.1) 上严格正。Sylvester 判据给 $\mathcal E>0$；再用 (3.3) 及真实源单射，证明 (1.1)。这里没有从一个零缺额边界的非严格极限推出严格性。

[小型证书清单](../notes/2026-11-14-two-group-singleton-birth-two-s1-certificate-789f-next.json)保存实际参数代换、项数、次数、符号结果和哈希。完整多项式由源码确定，可重新生成，不存大矩阵或巨量展开数据。

## 5. 实现核对与准确未付范围

生成器的 `--check` 另外从原物理 incidence 和组合数 Hilbert 范数独立构造上出生五维、下出生三维的全部所需完整逆，并核对实际立方权 incidence 给出的 (2.4)。在有理参数 $(q,L,a,u)=(3,4,2,3)$，全部逐项相等，且 (3.2) 与 (3.3) 完全相同。这个校准用于检查源、尺度和伴随顺序；全参数正性来自 §4 的完整符号证书。

本稿尚未证明同一旧出生的 S2，也未由此宣称加入第二异常位后的四维首边已完成。$q=2$ 或 $L=2$ 的 S1 需要另行支付，不能从 (4.1) 的正系数域直接外推。全出生、全部高度、一般任意权型与原 graph 源均保持各自原缺口。
