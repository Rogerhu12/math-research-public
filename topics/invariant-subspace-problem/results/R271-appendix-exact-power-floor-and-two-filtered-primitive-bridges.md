# R271 附录：原裸费用的准确真幂底项与两道滤波 primitive 桥

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue。

状态：**已证明。** 本文把[最低深度与 Euler 压缩](R271-appendix-bare-minimizer-lowest-depth-primitive-source-and-euler-compression.md)中的正交余项明确识别为同一个原首源的全部真幂最小原像。旧裸费用的真幂下界由此成为一个准确平方分解。实际剩余源通过两道受限 $D_3^*$、两个真实完整孔层滤波和一个出生一的加权差分最小逆；这些算子的顺序全部保留。没有给高链逆费用一个新上界。

## 1. 同一个原源及两种源孔层的幂逆

保留原 $m\ge5,d=2^m$、合法 $q$、$A=A_m,D=D_m$ 和全部联合旗。记 $p=q+1$。首段和首源分别为
$$
\mathscr X_q=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p},\qquad
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q}.
$$
给定 $r\in\mathscr R_q$，所有首段可行点满足 $Dx=r$。

需要区分两个完整源孔层上的真正 Moore--Penrose 逆：
$$
U_j=(D^j|_{\mathcal H_{p+j}})^\dagger:
\mathcal H_p\to\mathcal H_{p+j},
\qquad
V_t=(D^t|_{\mathcal H_{q+t}})^\dagger:
\mathcal H_q\to\mathcal H_{q+t}.
\tag{1.1}
$$
约定 $U_0=I$。它们先在完整孔层取最小逆；原尾固定有限孔层满射保证所有逆有界。一般 $U_jV_1$ 不等于 $V_{j+1}$。

在 $K_p=\ker D\cap\mathcal H_p$ 上记
$$
J_j=U_j|_{K_p},\qquad H_j=J_j^*J_j,
\qquad H_0=I.
\tag{1.2}
$$
$J_j$ 是 $K_p$ 到 $W_{j+1,p+j}=E_{j+1,p+j}\ominus E_{j,p+j}$ 的有界双射。前稿给原低链
$$
(\mathcal T x)_{j+1}=(-1)^jU_jA^jx,
\qquad0\le j<d,
\tag{1.3}
$$
以及最低深度的等距坐标
$$
(\mathcal I\xi)_{j+1}=(-1)^jJ_jH_j^{-1/2}\xi_j.
\tag{1.4}
$$
这里
$$
\xi\in\mathcal E=\bigoplus_{j=0}^{d-1}
\left(\operatorname{span}\{e_0,\ldots,e_{d-j-1}\}\otimes K_p\right).
$$
全部头矩阵与纯尾算子交换。

## 2. 同源真幂原像的正交分解

定义由原首源唯一确定的链
$$
\boxed{b_{j+1}(r)=(-1)^jV_{j+1}A^jr,\qquad0\le j<d.}
\tag{2.1}
$$
第 $d$ 项为零，因为原 $r$ 的头指标至多 $d-2$，故 $A^{d-1}r=0$。

对任意可行首段 $x$，$U_jA^jx$ 与 $V_{j+1}A^jr$ 解同一个方程
$$
D^{j+1}y=A^jr.
$$
前者与 $E_{j,p+j}$ 正交；后者与更大的 $E_{j+1,p+j}$ 正交。两者的差因而属于
$$
E_{j+1,p+j}\cap E_{j,p+j}^{\perp}=W_{j+1,p+j}.
\tag{2.2}
$$
这是同一个物理孔层中的准确正交分解，不使用顺次单步 MP 比较。

首段普通最小原像为 $x_0=V_1r=D_X^\dagger r$。它自动保原逐头旗；任何可行点为 $x_0+g$，$g\in\mathbb C^d\otimes K_p$。定义
$$
\kappa_j(r)=D^jV_{j+1}r-V_1r\in K_p,
\qquad\kappa_0=0.
\tag{2.3}
$$
primitive 归属来自
$D(D^jV_{j+1}r-V_1r)=r-r=0$。
在 (2.2) 上再施加 $D^j$，并用 $J_j$ 的唯一性，得到
$$
\boxed{
U_jA^j(x_0+g)
=V_{j+1}A^jr+J_jA^j\bigl(g-\kappa_j(r)\bigr).
}
\tag{2.4}
$$
因此整个原低链准确为
$$
\boxed{\mathcal T(x_0+g)=b(r)+\mathcal I\xi(g),}
\qquad
\xi_j(g)=H_j^{1/2}A^j\bigl(g-\kappa_j(r)\bigr),
\tag{2.5}
$$
且两项正交。每个 $b_{j+1}$ 都与 $E_{j+1,p+j}$ 正交，所以它恰是前稿的 $(I-P_{\min})\mathcal T x_0$，并不只是一个可比较的候选。

令
$$
\psi_j(r)=H_j^{1/2}A^j\kappa_j(r),\qquad
Q\xi=\sum_{j=0}^{d-1}(A^j)^*H_j^{1/2}\xi_j,
$$
$$
\Pi=I-Q^*(QQ^*)^{-1}Q.
\tag{2.6}
$$
前稿已证明 $QQ^*\succeq I$，$\Pi$ 是到 $\ker Q$ 的正交投影。式 (2.5) 的坐标为 $Q^*g-\psi(r)$，所以裸最小者的最低深度坐标是
$$
\xi_{\rm bare}=-\Pi\psi(r).
\tag{2.7}
$$
由正交性，得到主平方分解
$$
\boxed{
\alpha_q(r)^2
=\sum_{j=0}^{d-2}\|V_{j+1}A^jr\|^2
+\|\Pi\psi(r)\|^2.
}
\tag{2.8}
$$
前一项就是既有真幂 MP 下界的全部项；后一项准确度量这些独立真幂最小原像在原低内部方程中的不相容。它不是先任意选择的误差项。

特别，下界取等当且仅当 $\Pi\psi(r)=0$。若取等，裸最小链恰为 $b(r)$；下一节说明这时其内部残量也为零，故高出生返回为零。

## 3. 真实出生一中间算子是加权差分

原出生一输出第 $t$ 段的尾深度为 $t$，物理孔数为 $q+t=p+t-1$。用等距坐标
$$
\mathcal O_t\zeta_t
=(-1)^{t-1}J_{t-1}H_{t-1}^{-1/2}\zeta_t,
\qquad1\le t<d,
\tag{3.1}
$$
其中头空间为 $\operatorname{span}\{e_0,\ldots,e_{d-t-1}\}$。
第一下降的真实相容式是
$$
P_{W_{t,p+t-1}}D J_t=J_{t-1}.
$$
故原内部算子作用于最低深度低输入后，其出生一部分在这些坐标中准确为
$$
\boxed{
(\mathcal G\xi)_t
=A\xi_{t-1}-H_{t-1}^{1/2}H_t^{-1/2}\xi_t,
\qquad1\le t<d.
}
\tag{3.2}
$$
乘法次序不能互换，尤其没有假定 $H_{t-1}$ 与 $H_t$ 交换。$A$ 将头指标至少降低一，故 (3.2) 保显示的逐段头旗。

$\mathcal G$ 满射：给定任意合法输出 tuple，取 $\xi_0=0$，沿 (3.2) 逐段解出 $\xi_t$ 即可；步骤有限且各 $H_t^{\pm1/2}$ 有界。其核也精确可求：
$$
\mathcal G\xi=0
\iff \xi_t=H_t^{1/2}A^tg\quad(0\le t<d)
\iff \xi=Q^*g.
\tag{3.3}
$$
所以
$$
\boxed{\mathcal G^\dagger\mathcal G=\Pi.}
\tag{3.4}
$$
这是原出生一内部算子的真正最小逆，并非一个顺次幂逆的替代模型。

## 4. 幂最小链的残量只在出生一

对 $1\le t<d$，令
$$
\Delta_{t+1}=DV_{t+1}-V_t:
\mathcal H_q\longrightarrow\mathcal H_{q+t}.
\tag{4.1}
$$
两带删除结构及真幂最小性给
$\operatorname{Ran}\Delta_{t+1}\subseteq W_{t,q+t}$。
将 (2.1) 直接代入原内部算子，准确得到
$$
\boxed{(Sb(r))_t=(-1)^tA^t\Delta_{t+1}r.}
\tag{4.2}
$$
因此 $b(r)$ 的内部残量只有出生一，没有出生零以下或出生二以上分量。它通常不是原低链核中的独立可行链。

为写出其真实滤波源，在整个 $\mathcal H_q$ 上定义
$$
F_{t+1}^{(q)}=D^{t+1}(D^*)^{t+1},\qquad
\eta_t(r)=P_{K_q}(F_{t+1}^{(q)})^{-1}r.
\tag{4.3}
$$
再令
$$
C^{(0)}=D_3|_{K_{q+1}}:K_{q+1}\to K_q.
$$
这是实际受限算子；其伴随含 $K_{q+1}$ 投影。与前稿的完整相容缺陷公式相同，交换关系
$[D,[D,D^*]]=-2D_3$、$[D,D_3]=0$ 给
$$
\boxed{
\Delta_{t+1}r
=-t(t+1)J_{t-1}H_{t-1}^{-1}
(C^{(0)})^*\eta_t(r).
}
\tag{4.4}
$$
完整证明可直接在 $E_{t,q+t}$ 上取伴随：
$$
\Delta_{t+1}^*
=-t(t+1)(F_{t+1}^{(q)})^{-1}
D_3D^{t-1}P_{E_{t,q+t}}.
$$
$D^{t-1}P_{E_t}$ 的值域为 $K_{q+1}$；取受限伴随，再用
$$
P_{W_{t,q+t}}(D^*)^{t-1}|_{K_{q+1}}
=J_{t-1}H_{t-1}^{-1}
$$
即得 (4.4)。这一步保留整个 $(F_{t+1}^{(q)})^{-1}$，未改为 primitive 压缩的逆。

结合 (3.1)、(4.2)、(4.4)，幂最小链的出生一源坐标为
$$
\boxed{
\zeta_t(r)
=t(t+1)H_{t-1}^{-1/2}A^t
(C^{(0)})^*\eta_t(r).
}
\tag{4.5}
$$
它满足 $Sb=\mathcal O\zeta$。原低内部方程因此恰是
$$
\mathcal G\xi=-\zeta(r).
$$
最低深度和 $b(r)$ 正交，所以其真正最小解为
$$
\boxed{\xi_{\rm bare}=-\mathcal G^\dagger\zeta(r).}
\tag{4.6}
$$
于是 (2.8) 也写成
$$
\boxed{
\alpha_q(r)^2
=\sum_{j=0}^{d-2}\|V_{j+1}A^jr\|^2
+\|\mathcal G^\dagger\zeta(r)\|^2.
}
\tag{4.7}
$$
从 (4.6)，真幂下界取等当且仅当 $\zeta(r)=0$，此时 $Sb(r)=0$，验证了 §2 的等号陈述。

### 4.1 全高度首段不相容的显式望远镜式

由 (2.3)、(4.1)，有
$$
\kappa_t-\kappa_{t-1}=D^{t-1}\Delta_{t+1}r.
$$
对 (4.4) 施加 $D^{t-1}$ 后得到
$$
\boxed{
\kappa_j(r)
=-\sum_{t=1}^{j}t(t+1)H_{t-1}^{-1}
(C^{(0)})^*\eta_t(r).
}
\tag{4.8}
$$
这给 (2.3) 的完整同源表达，并可直接核验
$\mathcal G(-\psi)=-\zeta$ 以及
$-\Pi\psi=-\mathcal G^\dagger\zeta$。
这里不是把各高度 $\eta_t$ 当成可独立选取的输入；它们始终由同一个 $r$ 经 (4.3) 产生。

## 5. 第二道 primitive 桥与实际高出生返回

令
$$
C^{(1)}=D_3|_{K_{q+2}}:K_{q+2}\to K_{q+1}.
$$
前稿给原高返回在最低深度坐标上的准确算子 $\mathcal R$：
$$
(\mathcal R\xi)_j
=(-1)^{j+1}j(j-1)
P_{W_{j-1,p+j-1}}(D^*)^{j-2}
(C^{(1)})^*H_j^{1/2}\xi_j,
\qquad 2\le j<d,
\tag{5.1}
$$
第 $1$ 段为零。由 (4.2)，$b(r)$ 本身没有高出生返回。因此原裸最小链满足
$$
\boxed{B_qa_q(r)=-\mathcal R\mathcal G^\dagger\zeta(r).}
\tag{5.2}
$$
在 (4.5)、(5.1)、(5.2) 中，第一道 $(C^{(0)})^*$ 从 $K_q$ 到 $K_{q+1}$，第二道 $(C^{(1)})^*$ 从 $K_{q+1}$ 到 $K_{q+2}$。中间仍有真实 $H_j^{\pm1/2}$ 和 $\mathcal G^\dagger$；第一道之前仍有完整 $(F_{t+1}^{(q)})^{-1}$。没有把这些算子移过 $D_3$，也没有把它们换成连续 $D_3^2$ 已知像上的无逆界。

准确的未付高链修复量现可写成
$$
\boxed{S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r).}
\tag{5.3}
$$
式 (4.7) 支付 $\mathcal G^\dagger\zeta(r)$ 本身的原范数，并精确分离已付的真幂底项；它没有支付 (5.3)。原左最小源费用也保持原定义。本文未推出三 Gram 的所需上界或无权 $N=M$。
