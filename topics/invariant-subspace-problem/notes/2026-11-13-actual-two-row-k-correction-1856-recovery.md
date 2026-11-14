# 实际双行 k 枢轴：恢复稿、全部原双源与可迭代边界

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：下述代数与定量构造已给完整证明；root 尚待全文读取后整合。原执行环境失联，本文件依根 README 第8条及 root 明确授权，通过现有 GitHub 连接保存小文本；这不是 git pull。未更改任何既有追踪文件。普通 ISP、一般正常见证及统一正常锚均未完成。

本稿新增：真实两二次生成元可以利用第二行，得到常数加实际 carry 的正分母；保留两个生成元时，反向源也廉价。对指定迟首正线性两行，前三位链的费用为较早的 eta_n^{-2}，而非 eta_{n+1}^{-2}。本稿没有将变化的起点当成同一个原理想的全层递推。

## 1. 保完整 carry 的两二次行正规化

在实际第 l 层尾，令
$$
N=N_l,\qquad N^2=t=\eta_lN_{l+1}.
$$
设
$$
U=\alpha N+u,\quad V=\beta N+v,\quad
u,v\in\mathcal B_{l+1},\quad\chi(u)=\chi(v)=0,
$$
其中 alpha 是非零实标量、beta 为正标量。取 epsilon,delta>0，并令
$$
H=V^2-\delta N,\qquad K=U^2+\varepsilon V.
\tag{1.1}
$$
四个真实块系数为
$$
C_H=v^2+\beta^2t,\quad D_H=2\beta v-\delta I,
$$
$$
C_K=u^2+\alpha^2t+\varepsilon v,\quad
D_K=2\alpha u+\varepsilon\beta I.
\tag{1.2}
$$
置
$$
c=\frac{\varepsilon\beta}{2\alpha},\qquad
q_0=\frac{\varepsilon^2\beta^2}{4\alpha^2}
+\frac{\varepsilon\delta}{2\beta}>0,\qquad
q=q_0I+\alpha^2t.
\tag{1.3}
$$
准确的 Bezout 身份是
$$
\boxed{C_K-\frac{u-c}{2\alpha}D_K
-\frac{\varepsilon}{2\beta}D_H=q.}
\tag{1.4}
$$
确实
$$
u^2-\frac{u-c}{2\alpha}(2\alpha u+\varepsilon\beta)
=c^2,
$$
而 epsilon v 被第三项中的 epsilon v 精确抵消，剩余
alpha^2 t+c^2+epsilon delta/(2 beta)。

定义两个当前尾实际右源
$$
A=-\frac{\varepsilon}{2\beta}q^{-1},\qquad
B=\left[N-\frac{u-c}{2\alpha}\right]q^{-1},
\tag{1.5}
$$
和下一尾代表
$$
\boxed{
R=\left[tD_K-\frac{u-c}{2\alpha}C_K
-\frac{\varepsilon}{2\beta}C_H\right]q^{-1}.
}
\tag{1.6}
$$
则
$$
\boxed{P=N+R=HA+KB,\qquad \chi(R)=0.}
\tag{1.7}
$$
证明：按 I,N 展开，奇块是 (1.4) 乘 q^{-1}，恰为 I；偶块恰为 (1.6)。每个 N^2=t 项均已保留。

### 1.1 真逆与廉价反向

q 的常数字符为 q0>0，所以是真实下一尾单位。若
$$
\theta=\alpha^2\eta_l/q_0\le1/2,
$$
则实际算子范数中的 Neumann 级数给
$$
q^{-1}=q_0^{-1}\sum_{r\ge0}(-\alpha^2t/q_0)^r,\qquad
\|q^{-1}\|\le2/q_0.
\tag{1.8}
$$

第一个源 A 是实际单位，而且
$$
\boxed{A^{-1}=-2\beta q/\varepsilon.}
\tag{1.9}
$$
故完整两生成元理想准确满足
$$
\boxed{(H,K)=(P,K),}
\tag{1.10}
$$
其反向身份为
$$
\boxed{
H=-\frac{2\beta}{\varepsilon}qP
+\frac{2\beta}{\varepsilon}
\left[N-\frac{u-c}{2\alpha}\right]K.
}
\tag{1.11}
$$
这里不求 B^{-1}，不省略任何未知商逆。代数、范数闭及超弱闭生成理想都成立 (1.10)。

下一层完整尾交由原实际余式给出
$$
(P,K)\cap\mathcal C_{l+1}
=(R^2-t,\ C_K-RD_K).
\tag{1.12}
$$
范数/超弱闭版本同样由连续/正常余式证明；不是一般地交换闭包与取交。

## 2. 两条原 N 线性行的全部源

固定起点 n，记 m=n+1、l=n+2。取真实范数收敛行
$$
S=\sum_{j\ge n}a_jN_j,\qquad
Z=\sum_{j\ge n}c_jN_j,\qquad a_n,a_m>0,
\quad a,c\in\ell^1(\mathbb R).
\tag{2.1}
$$
定义
$$
r_n=c_n/a_n,\quad b_j=r_na_j-c_j\ (j\ge m),\quad b_m\ne0,
$$
$$
P_m=\frac{r_nS-Z}{b_m}=N_m+V,\qquad
V=\sum_{j\ge l}\frac{b_j}{b_m}N_j,
$$
$$
F=\sum_{j\ge m}a_jN_j,\qquad
U=\sum_{j\ge l}a_jN_j-a_mV.
\tag{2.2}
$$
所以 F=a_m P_m+U。令
$$
\varepsilon=\eta_na_n^2,\quad\delta=\eta_m,\quad
H=V^2-\eta_mN_l,\quad K=U^2+\varepsilon V.
\tag{2.3}
$$
这就是 §1 的两行。物理系数准确为
$$
\boxed{\beta=b_l/b_m,\qquad \alpha=a_l-a_m\beta.}
\tag{2.4}
$$
u,v 由 U,V 去掉第 l 项而得。只要 beta>0、alpha!=0，§1 的正分母成立。

例如正 a_j 且 r_j=c_j/a_j 严格单调时，
$$
\beta=\frac{a_l(r_n-r_l)}{a_m(r_n-r_m)}>0,\qquad
\alpha=\frac{a_l(r_l-r_m)}{r_n-r_m}\ne0.
$$
alpha 可为负，q0 只用 alpha^2。

### 2.1 原双源显式公式

由真实 N_n^2=eta_n N_m，
$$
Q=(F-a_nN_n)S=F^2-\varepsilon N_m.
$$
置
$$
E=a_m^2P_m+2a_mU-\varepsilon I.
\tag{2.5}
$$
代入 F=a_m P_m+U 与 N_m=P_m-V，得到 Q=K+P_m E。因此
$$
\boxed{H=(V-N_m)\frac{r_nS-Z}{b_m},}
$$
$$
\boxed{
K=(F-a_nN_n)S-\frac{r_nS-Z}{b_m}E.
}
\tag{2.6}
$$
与 (1.7) 合并得
$$
\boxed{P=S\mathcal U+Z\mathcal V,}
\tag{2.7}
$$
其中两个原右源完整为
$$
\mathcal U=\frac{r_n}{b_m}(V-N_m)A+
\left[F-a_nN_n-\frac{r_n}{b_m}E\right]B,
$$
$$
\mathcal V=-\frac{V-N_m}{b_m}A+\frac{E}{b_m}B.
\tag{2.8}
$$
全部因子属于真实原范数代数；只有列明的非零标量及 q 被求逆。

### 2.2 完整尾交而非仅成员性

第一位的奇系数是非零标量 a_n。原完整尾交定理给
$$
(S,Z)\cap\mathcal C_m=(Q,P_m).
$$
由 Q=K+P_m E 及 K 属于下一尾，
$$
(Q,P_m)=(K,P_m).
$$
再次以 P_m=N_m+V 作原余式，得到
$$
\boxed{(S,Z)\cap\mathcal C_l=(H,K)=(P,K).}
\tag{2.9}
$$
对闭理想的版本仍逐次使用原连续/正常余式，不交换闭包和取交。反向因子 a_n^{-1},b_m^{-1},E 与 (1.11) 已全部显示。

## 3. 指定迟首正系数族：精确 carry 及双向预算

取
$$
a_j=(j+1)^{-2}\ (j\ge n),\qquad
c_n=0,\quad c_j=a_j^2=(j+1)^{-4}\ (j>n).
\tag{3.1}
$$
这是实际 N 线性行族，本身不含任意 H_zeta 或 Cayley 快补项。令 x=n+1>=1。此时 r_n=0、b_m=-c_m，
$$
P_m=Z/c_m,\quad
V=\sum_{j\ge l}\frac{a_j^2}{a_m^2}N_j,\quad
U=\sum_{j\ge l}a_j(1-a_j/a_m)N_j,
$$
$$
\boxed{
\alpha=\frac{2x+3}{(x+2)^4},\quad
\beta=\frac{(x+1)^4}{(x+2)^4},\quad
\varepsilon=\eta_n/x^4,\quad\delta=\eta_{n+1}.
}
\tag{3.2}
$$
所有 U,V 的系数非负。积分估计给
$$
\|V\|\le(x+1)/3\le x,\quad
\|U\|\le1/(x+1)\le1/x,\quad
\|v\|\le x,\quad\|u\|\le1/x.
\tag{3.3}
$$
例如 sum_{k>=x+2} k^{-4}<=1/[3(x+1)^3]；最后两式由物理块压缩。还可使用
$$
(81x^3)^{-1}\le\alpha\le5x^{-3},\qquad 1/6\le\beta\le1.
\tag{3.4}
$$

原实际 carry 的准确指数为
$$
u_j=-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j,
\quad770\,16^j\le u_j\le1400\,16^j.
\tag{3.5}
$$
由 (3.2)–(3.4)，
$$
q_0\ge\eta_n^2/(3600x^2),
$$
$$
\frac{\alpha^2\eta_{n+2}}{q_0}
\le90000\,\frac{\eta_{n+2}}{\eta_n^2}
\le90000e^{-194320\,16^n}<1/2.
\tag{3.6}
$$
因此真实小参数逆预算是
$$
\boxed{\|q^{-1}\|\le7200x^2\eta_n^{-2}.}
\tag{3.7}
$$
支付的是较早的 eta_n^{-2}，没有使用 eta_{n+1}^{-2}。

### 3.1 目标、前向原双源、反向源

写 J=-(u-c)/(2 alpha)。由 eta_n<=e^{-1070}，
$$
|c|\le41\eta_n/x<1/x,\quad\|J\|\le81x^2,\quad
\|C_H\|\le2x^2,
$$
$$
\|C_K\|\le2/x^2,\qquad\|D_K\|\le11/x^4.
\tag{3.8}
$$
例如 C_K 范数至多 x^{-2}+25 eta_{n+2}x^{-6}+eta_n x^{-3}。
(1.6) 分子范数小于164，所以
$$
\boxed{
\|R\|\le1.2\cdot10^6x^2\eta_n^{-2},\quad
\|B\|\le6\cdot10^5x^4\eta_n^{-2},\quad
\|A\|\le22000x^{-2}\eta_n^{-1}.
}
\tag{3.9}
$$
这些常数仅是可复核的上界。

在迟首 r_n=0 时，全部原源化为
$$
\boxed{
\mathcal U=(F-a_nN_n)B,\qquad
\mathcal V=\frac{V-N_m}{c_m}A-\frac{E}{c_m}B.
}
\tag{3.10}
$$
这里 c_m=(x+1)^{-4}，且
$$
\|F-a_nN_n\|\le2/x,\quad\|E\|\le5/x^3,
$$
$$
\|(V-N_m)/c_m\|\le32x^5,\qquad\|E/c_m\|\le80x.
$$
因此
$$
\boxed{
\|\mathcal U\|\le1.2\cdot10^6x^3\eta_n^{-2},\qquad
\|\mathcal V\|\le5\cdot10^7x^5\eta_n^{-2}.
}
\tag{3.11}
$$

反向也有实际预算：
$$
q_0\le1644\eta_n^2/x^2,\qquad \|q\|\le2466\eta_n^2/x^2.
$$
所以 (1.11) 的两个系数满足
$$
\boxed{
\|(2\beta/\varepsilon)q\|\le5000x^2\eta_n,\qquad
\|(2\beta/\varepsilon)(N+J)\|\le164x^6\eta_n^{-1}.
}
\tag{3.12}
$$
这次完整两生成元身份没有未支付的反向单位。

## 4. 完整商、同一个正常态和精确条件锚

固定原 S,Z。式 (2.7) 给当前 l=n+2 层真实 P=N_l+R。若旧规范是
S_l=D_l(N_l+G_l^{old})，原余式
r_l(a+N_l b)=a-G_l^{old}b 给
$$
R-G_l^{old}\in\mathcal J'_{l+1}(S,Z).
$$
所以 (3.9) 确是旧完整联合商的实际代表上界，而非从 raw 范数或像范数推断商费用。

设同一个原正正常 rho 湮灭 S A'+Z A'。令
$$
\Theta=2P(I+N_l)^{-2}
=S[2\mathcal U(I+N_l)^{-2}]
+Z[2\mathcal V(I+N_l)^{-2}].
\tag{4.1}
$$
在第 l 位取 e=Omega_+ tensor I。真实二乘二式给
$$
e^*(I+N_l)^{-2}e=0,\qquad
e^*N_l(I+N_l)^{-2}e=I/2.
$$
因此
$$
\boxed{e^*\Theta e=I,\qquad\omega_l(\Theta)=1.}
\tag{4.2}
$$
原目标和原双源分别支付
$$
\|\Theta\|\le\frac{8(1+\|R\|)}{(1-\eta_l)^2},
$$
$$
\|2\mathcal U(I+N_l)^{-2}\|
\le\frac8{(1-\eta_l)^2}\|\mathcal U\|,
\quad
\|2\mathcal V(I+N_l)^{-2}\|
\le\frac8{(1-\eta_l)^2}\|\mathcal V\|.
\tag{4.3}
$$
对 (3.1) 有
$$
\|\Theta\|\le2\cdot10^7x^2\eta_n^{-2},
\qquad
\frac{|\omega_l(\Theta)|}{\|\Theta\|}
\ge\frac{\eta_n^2}{2\cdot10^7x^2}.
\tag{4.4}
$$
同一个 rho 湮灭 (4.1)，没有换态、纯化或重新正化。锚仍变小，未得到统一正常锚。

## 5. 可迭代范围：有限链改善与未闭部分

(3.9)、(3.11) 的对数费用为 2u_n+O(log(n+2))。因此对以 n 为起点的两行族，
$$
\limsup_{n\to\infty}16^{-(n+2)}
\log\max\{1,\|R\|,\|\mathcal U\|,\|\mathcal V\|\}
\le175/16.
\tag{5.1}
$$
这是变化起点的指定实际两行族的费用。不能从一个固定原 S,Z 的湮灭删去低位项，再将 (5.1) 当作同一原理想的全层 type。

n=0 时，本构造主要对数费用为 2u_0=2140。此前只用单行 h 修正到第2位的上界是
8u_0+2u_1+5 log8=44480+5 log8。
这里只比较两个已付上界，不声称给最小费用之比的下界。

### 5.1 可以继续的同源递推

从固定 P=S U+Z V 出发，可用 root 已发布的 carry-stable h 修正。
若下一层是
$$
P_{l+1}=(R-N_l)P A_l,
$$
则原两个源同乘这个已付右因子：
$$
\mathcal U_{l+1}=\mathcal U(R-N_l)A_l,\qquad
\mathcal V_{l+1}=\mathcal V(R-N_l)A_l.
\tag{5.2}
$$
(3.9)、(3.11) 初值均小于 exp(240·16^l)，故该稿全层 Neumann 归纳接续成立；全部后继属于同一个原双行理想并由同一个 rho 湮灭。但只沿单行 h 继续，长期主上界回到700/3，不能说175/16已沿固定原理想保持。

保留第二行时，下一完整实际接口准确为
$$
h_{l+1}=R^2-\eta_lN_{l+1},
$$
$$
k_{l+1}=u^2+\alpha^2\eta_lN_{l+1}+\varepsilon v
-R(2\alpha u+\varepsilon\beta I).
\tag{5.3}
$$
(1.9)–(1.12) 已支付完整理想等价和全部来源。
但 k_{l+1} 通常是 u,v 的高次有理式；不能重命名后当成新的两条纯线性行。
继续利用 (5.3) 的特定系数降低全层费用，是当前实际下一问题。

## 6. 原二次见证的适用边界

所有算子都是原 Haar 的真实 N_j；没有删 carry 成为纯 nilpotent 模型。但 (2.1) 要求初始两行均为 N_j 线性和。
一般迟首二次核给同一 gauge 的 S=X+H_zeta、Z=Y-B0+H_zeta^2；Q_j、H_zeta 未被本稿消去。因此不能直接套 (3.1)。

一个精确关联是 N 版本
$$
T_N=X^2-\sum_{j\ge n}a_j^2N_j^2+Y,\quad
X=\sum_{j\ge n}a_jN_j,\quad Y=\sum_{j>n}c_jN_j.
$$
若已经合法选定只翻转第 n 位的 gauge，则一次因子为 S=X-a_nN_n。相同见证的第二行准确为
$$
Z=Y-\sum_{j>n}a_j^2N_j^2
=c_{n+1}N_{n+1}
+\sum_{j\ge n+2}(c_j-a_{j-1}^2\eta_{j-1})N_j.
\tag{6.1}
$$
因此在这个特定 gauge 确有非零见证的前提下，可以从 n+1 对一般 (2.1) 检查 alpha,beta,q0。必须使用 (6.1) 的实际 carry 修正系数；没有证明该 gauge 总可选到，也未未经核验将 (3.2) 套给修正系数。

本稿新增了正 q0、实际原双源、保完整理想的廉价反向和有限层费用改善。尚未证明固定原理想的全层低 type、任意实际 Q/H 双行的同类变换或统一正常锚。
