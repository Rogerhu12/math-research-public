# R150 附录：L=0 且两个约化权重之和为零的整支排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126。日期：2026-11-26 UTC。

**状态：已证明原物理分支为空。** 本文处理 unit $2+1+1$、孤立零点非零 mean 的原 U 值图，完整排除 $L=0,\ b+c=0$。此前已关闭的 $w=0,w=1$ 与规范 $p+q=2$ 下 $u=1$ 不重算；本文补齐其余全部参数和每条原 P1 首项零纤维。没有宣称一般 $L=0$、全部 unit211 或普通 ISP 完成。

来源：[原 U 值覆盖](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)、[L0/w1 全纤维排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-L0-w1-exclusion.md)、[本定理自含原源码](../notes/2026-11-26-unit211-L0-zero-weight-sum-original-fibers-347c.py)与[实际执行小回执](../notes/2026-11-26-L0-zero-weight-sum-original-fiber-exclusion-347c.json)。$w=0$ 和 $u=1$ 的已闭结论及完整来源见[结果索引](../results.md)。

## 1. 原 L0 条件给出全局两参数图

原非零配对分支的 $p,q,p-q,p+q$ 都非零。在已经付清的共同规范 $p+q=2$ 下，令

$$
p=1+\kappa,\quad q=1-\kappa,\quad Q=pq,\quad
\Delta=1-Q=\kappa^2\ne0.
$$

原 $L=q(h-1)-p(k-1)=0$ 给

$$
h=1+\rho p,\qquad k=1+\rho q,\qquad \rho\ne0.
$$

原 $h=k=1$ 值碰撞不在当前未闭图中。设

$$
R=\lambda-1-w,\quad A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
u=bp+cq,\qquad V_2=bp^2+cq^2.
$$

原三个 U 矩恰为

$$
\rho u=R,\qquad \rho^2V_2=A,\qquad
\rho^3(bp^3+cq^3)=B.
\tag{1}
$$

本支 $c=-b$，故 $V_2=(p+q)u=2u$，且
$bp^3+cq^3=(p^2+pq+q^2)u=(4-Q)u$。于是

$$
\boxed{\rho=\frac{A}{2R},\quad
u=\frac{2R^2}{A},\quad
Q=4-\frac{4BR}{A^2},\quad
b=\frac{u}{2\kappa},\quad c=-b,\quad a=1.}
\tag{2}
$$

$R=\rho u\ne0$，因此 $A=2\rho R\ne0$ 是原式迫出的单位，并非任意删除的谱。所有 $\kappa$ 根均保留：计算在
$\mathbb Q(\lambda,w)[\kappa]/(\kappa^2-\Delta)$ 中以偶部和奇部进行，未选择某个平方根，也不假设二次代数不可约。

再令

$$
2P_0=(4-Q)u-3uV_2+2u^3,\qquad T_0=V_2-2u^2.
$$

原 $N(V)=0$ 在 $w(w-1)\ne0$ 图上给唯一

$$
\boxed{
f=-\frac{u(w/2-w^2)+\rho T_0/4+\lambda\rho^2P_0}{w(w-1)}.
}
\tag{3}
$$

(1)–(3) 同时满足原 $P(V)=0$。两条恒等式及三个矩均在实际源中从原定义直接展开核验。

所有清分母只使用以下已付非零量的多项式分子：

$$
\lambda,\quad w,\quad w-1,\quad R,\quad A,\quad
\Delta,\quad Q,\quad P_0,\quad u-1.
\tag{4}
$$

最后一项来自此前独立排除的整个 $u=1$ 图。没有除以 f、t、原 P1 系数或新结式首项。$b,c,u,\rho,p,q,p-q$ 的非零性由 (2)、(4) 支付。

## 2. 同一个 Frobenius 代数和全部原九式

取原 Frobenius 代数

$$
\mathcal A=\mathbb C[\varepsilon]/(\varepsilon^2)\oplus
\mathbb C\oplus\mathbb C,\qquad 1=(1,0,1,1),
$$

乘法为

$$
(xy)_0=x_0y_0,\quad
(xy)_\varepsilon=x_0y_\varepsilon+x_\varepsilon y_0,\quad
(xy)_B=x_By_B,\quad (xy)_C=x_Cy_C,
$$

并用原迹 $\tau(x)=a x_0+x_\varepsilon+b x_B+c x_C$，此处 $a=1$。下式均在该原代数中相乘。设

$$
W_1=T_0/2+2uf,\qquad
W_2=uT_0+2\lambda P_0+(V_2+2u^2)f-bcQt,
$$

$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)},
$$

$$
r=X-ap-ct,\quad s=Y-aq-bt,\qquad
J=2f-2bX-2cY+2bct.
$$

原四个 K 行为

$$
K_0=(0,0,p,q),\quad K_1=(0,J,r,s),\quad
K_B=(p,r,0,t),\quad K_C=(q,s,t,0).
\tag{5}
$$

定义 $(D_Kx)_i=\tau(K_ix)$、$d=D_K1$、$F_2=\tau(d)=2f$。原三阶与第二梯度多项式为

$$
\mathcal P(x)=\tau\bigl((x-\tau(x)1)^3\bigr),
$$

$$
\mathcal N(x)=
2\tau(dx^2)-F_2\tau(x^2)-4\tau(x)\tau(dx)
+2F_2\tau(x)^2+\tau(xD_Kx).
$$

相应喷射

$$
\mathcal P_1(x,z)=3\tau\bigl((x-\tau(x)1)^2(z-\tau(z)1)\bigr),
\quad
\mathcal N_1(x,z)=\mathcal N(x+z)-\mathcal N(x)-\mathcal N(z).
$$

设 $v_1=2\tau(K_0K_1)$、$v_B=\tau(K_B^2)$、$v_C=\tau(K_C^2)$，并定义

$$
E_j=v_j-2(D_Kd)_j-2d_j^2+2F_2d_j,\qquad j=1,B,C.
$$

除已恒等满足的原 0 行与 $P(V),N(V)$ 外，全部剩余条件是

$$
\begin{aligned}
&E_1=E_B=E_C=0,\\
&\mathcal P_1(K_0,K_1)-6wP_0=0,\\
&\mathcal P(K_B)-2h^3P_0=0,\quad
 \mathcal P(K_C)-2k^3P_0=0,\\
&\mathcal N_1(K_0,K_1)-8\lambda wP_0=0,\\
&\mathcal N(K_B)-4\lambda h^2P_0=0,\quad
 \mathcal N(K_C)-4\lambda k^2P_0=0.
\end{aligned}
\tag{6}
$$

共轭 $\kappa\mapsto-\kappa$ 恰交换 B/C。两条共轭原式同时为零且 $\kappa\ne0$，便迫偶部、奇部同时为零。源先核对共轭关系，随后以九条有理系数 t 多项式

$$
E_1,E_{B,e},E_{B,o},P_1,P_{B,e},P_{B,o},N_1,N_{B,e},N_{B,o}
$$

保存全部条件，其实际 t 次数依次为 $1,2,2,1,3,3,1,3,3$。

每个系数分母逐个用 (4) 验证；只剥所有系数共同拥有的已付单位，再以非零有理常数归一化。没有丢弃原喷射、mean 或 B/C 的一条共轭式。以下用足够排除原解的必要投影，不主张投影有逆向充分性。

## 3. 保留 P1 全部首项零纤维的投影

写原清分母后的 $P_1=\alpha t+\beta$。对原 t 多项式
$F(t)=\sum_{j=0}^dF_jt^j$，使用

$$
\mathcal H_F=\sum_{j=0}^d F_j(-\beta)^j\alpha^{d-j}.
\tag{7}
$$

若原解的 $\alpha\ne0$，(7) 等于
$\alpha^dF(-\beta/\alpha)=0$。若 $\alpha=0$，原解另有
$\beta=0$，正次数 (7) 同样为零；零次 F 则直接保留。
因此未把 $\alpha$ 当单位。

同时取原 mean 及 E1/N1 的 t Sylvester 结果式。各投影只剥 (4)，得到确定的 $\mathbb Q[\lambda,w]$ 多项式。记

$$
H=\mathcal H_{E_1},\quad H_{N_1}=\mathcal H_{N_1},\quad
H_{B,e}=\mathcal H_{E_{B,e}},\quad
H_{P,e}=\mathcal H_{P_{B,e}}.
$$

$R_{E_1,N_1}$、$R_{E_1,E_{B,e}}$ 表示相应原 t 结果式。以 H 为锚，下列五个 w 结果式已给有限 lambda 必要集：

| 另一条原必要投影 | w 结果式的 lambda 次数 | 累积 gcd 次数 |
|---|---:|---:|
| $H_{N_1}$ | 227 | 227 |
| $H_{B,e}$ | 280 | 162 |
| $R_{E_1,N_1}$ | 290 | 159 |
| $R_{E_1,E_{B,e}}$ | 366 | 153 |
| $H_{P,e}$ | 475 | 152 |

每个原有限 $(\lambda,w)$ 点必使这五个结果式为零，包含所有 w 首项降次点。累积 gcd 每步用 QQ 扩展 Euclid，并实际乘回 Bézout 恒等式。

## 4. 全部 lambda 因子及完整原域返回

所得 152 次 gcd 在非零有理常数意义下为

$$
\begin{aligned}
G(\lambda)={}&
\lambda^2(\lambda-1)(4\lambda^2-2\lambda+1)
(8\lambda^2-6\lambda-1)^4\\
&\cdot(4\lambda^6-22\lambda^5+26\lambda^4-20\lambda^3
 +11\lambda^2-4\lambda+1)^4\\
&\cdot(2\lambda^2-2\lambda+1)^9
(3\lambda^2-2\lambda+1)^{15}(2\lambda-1)^{67}.
\end{aligned}
\tag{8}
$$

全部因子和重数实际乘回，与 G 完全一致。只删除 (4) 已付的 $\lambda$ 与 $A=2\lambda^2-2\lambda+1$；其余六因子平方自由总次数 14。

对每个保留因子 $\phi$，在整个系数代数
$K_\phi=\mathbb Q[\lambda]/(\phi)$ 中将原 H、原 $H_{N_1}$ 及全部 (4) 单位直接特化，再在 $K_\phi[w]$ 运算。未选实根、某个共轭或数值近似。

每次系数求逆均先实际核验

$$
s a+t\phi=g\in\mathbb Q^\times,\qquad a(s/g)=1\pmod{\phi}.
\tag{9}
$$

因此不靠“每个非零元素自动可逆”的假设；所用系数确在整个商代数中有逆。每步 w 除法和扩展 gcd 也实际乘回：

$$
qB+r=A,\qquad sA+tB=\gcd(A,B).
\tag{10}
$$

只有当前共同 w 多项式与已付单位有共同因子时，才精确剥除该因子。这只能去掉违反原非零条件的候选。

| 保留的 lambda 因子 | 原 H 的 w 次数 | 只剥除的已付因子 | 原 $H_{N_1}$ 返回后共同 w 次数 | 系数逆身份数 |
|---|---:|---|---:|---:|
| $\lambda-1$ | 12 | w，一次 | 0 | 48 |
| $4\lambda^2-2\lambda+1$ | 12 | 无 | 0 | 46 |
| $8\lambda^2-6\lambda-1$ | 13 | w−1，两次 | 0 | 53 |
| $4\lambda^6-22\lambda^5+26\lambda^4-20\lambda^3+11\lambda^2-4\lambda+1$ | 13 | Q，两次 | 0 | 53 |
| $3\lambda^2-2\lambda+1$ | 13 | Q，五次 | 0 | 59 |
| $2\lambda-1$ | 13 | w，七次 | 0 | 63 |

所有次数 0 实际都是单位多项式 1。322 次系数逆均验证 (9)，每个 w Bézout 恒等式均验证 (10)。本次没有出现整条 lambda 纤维上的某个原单位多项式恒为零的快捷排除情形。

如有原合法点，(8) 使 lambda 落在六因子之一；(4) 禁止表中全部剥除项；该点须同时满足两条原必要式，与已验证 gcd 1 矛盾。故六因子的全部复根均排除。

用 $\phi$ 代替 $\phi^k$ 只作点集覆盖，因为 $\phi^k(\lambda)=0$ 必有 $\phi(\lambda)=0$；未宣称 primary 理想相等，也不把本结果当全局 Bell 幂证书。

## 5. 旧 rho 二次因子恰是本支

此前 p=1 的 L0 三参数图记

$$
C=RB-A^2,\quad D=A-R\rho,\quad N=B-A\rho,\quad
M=B-2A\rho+R\rho^2,
$$

$$
b=\frac{C}{\rho M},\qquad c=\frac{D^3}{NM},\qquad
\Phi=R^2\rho^2-AR\rho-C.
$$

直接展开得

$$
CN+\rho D^3=-M\Phi,\qquad
\boxed{\Phi=-\rho N(b+c).}
$$

旧图的 $\rho,N,M$ 都是已付原单位，所以其 E1/N1 结果式的整个 $\Phi=0$ 二次因子，正是本文关闭的 $b+c=0$ 支。大补因子仍开放。两张图的 rho 对应不同 p 规范，不能混用其数值；等价通过同一原权重条件表达。

## 6. 实际执行与结论范围

最终源 Git blob：
4f3c05e6f75bb48214364ac5fbab97b37c7d75a8。

源 SHA-256：
65a536af980b382626f1fd79d0bf40fa8de364301d43c980507c46a825820481。

源提交 a8213d2429c498852dde5602ccb9019251f01ff6，Actions run
45823574259 / job 139921814299，结论 success。源执行 3.173630 秒，
driver 3.244702202 秒，峰值子进程 RSS 47168 KiB，源退出码 0。
stdout 19490 字节，SHA-256
9992706ba1903d35f2e921c657a44ce44117403bc4a9792104b63eec6315bc13。

执行前实际 partial clone/pull main 到
a39e5a6f88c9695ae43abcc6358679a422c4d5e8
（2026-11-26 12:51:50 UTC），根及本课题 README 均无差异。

源码从本文原公式重建全部必要系数、五个 QQ 结果式、完整因子分解和六次原域返回，不依赖外存巨大系数阵列。较早三参数 Phi 源实际 1846.988 秒到时未决，继续保留未决执行记录；本次不同输入的成功不是旧任务成功。

本条完整关闭 $L=0,\ b+c=0$。合并已付 w0/w1/u1 边界后，该原分支没有遗漏。下一项为 $L=0,\ b+c\ne0$ 大补因子；一般 LS 图、S0 其余图、其余秩与自然幂、算子桥和普通 ISP 均仍开放。

