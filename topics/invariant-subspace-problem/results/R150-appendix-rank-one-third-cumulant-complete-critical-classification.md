# R150 附录：秩一第三累积量的完整临界集

日期：2026-11-26。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 本稿完成四个两根族的原有理数消元、全部降次/射影边界和判别式零纤维，并穷尽原五次均值极线的所有除子型，准确分类整个非零秩一第三累积量临界层。秩指原三阶 Hankel 张量的一阶展平秩。

## 1. 主定理与原对象

固定原六模式整数矩阵 $K$、$u(a,b)=(a^5,a^4b,\ldots,b^5)^{\mathsf T}$、$H_{ij}=H_{i+j}$、$V_{ijk}=V_{i+j+k}$ 与完整 $\mathcal Q_3$。全部对象和原梯度由[原完整定义](R150-appendix-rank-one-third-cumulant-three-plus-one-plus-one-mean-divisor-classification.md) §1 给出。

**定理。** $\mathcal Q_3$ 的完整临界点中，$\operatorname{rank}V=1$ 的点恰为
$$
\boxed{
y=a\,u(s),\qquad
H=\frac{a^3+4c}{6a}\,u(s)u(s)^{\mathsf T},\qquad
V=c\,u(s)^{\otimes3},\qquad
s\in\mathbb P^1,\quad a,c\ne0.
}                                                    \tag{1.1}
$$
选择任一非零齐次代表 $u(s)$ 后，$a,c$ 相应按相反权变化，所以该式与代表无关。所有这些点的完整第三普通矩
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V \tag{1.2}
$$
均零；任意方向的完整 Bell 立方 $T_3(r,r,r)$ 均零。

上述零矩族与[已登记的非零均值、第三矩零全分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)相容；本稿的新内容是排除秩一 $V$ 下其余全部原临界点。

本定理保留所有 $s$、极线重根、接触退化与无穷远。它只关闭秩一 $V$ 全层，不关闭高秩 $V$、全局 Jacobian 自然幂或普通 Hilbert ISP。

## 2. 原整除与已经证明的分支

对称和 Hankel 性给 $V=c u(s)^{\otimes3}$；其直接秩一证明见[原引理](R150-appendix-rank-one-third-cumulant-three-plus-one-plus-one-mean-divisor-classification.md) §2。置
$$
P_y(x)=(Ky)^{\mathsf T}u(x),\quad
k_s(x)=u(s)^{\mathsf T}Ku(x)=-\Delta_s(x)^2q_s(x),       \tag{2.1}
$$
其中 $\Delta_s(a,b)=s_0b-s_1a$。原三次式的有限图为
$$
q_s(z)=(s^3-5s^2)+(s^3-3s^2+22s)z
 -(3s^2+3s+5)z^2+(s+1)z^3.                           \tag{2.2}
$$
全部最高梯度是
$$
P_y^3-6P_yG_H+4c k_s^3=0,\qquad G_H=u^{\mathsf T}KHK u.
                                                               \tag{2.3}
$$
$K$ 可逆、$k_s\ne0$、$c\ne0$，故 $P_y\ne0$，并且
$$
P_y\mid k_s^3=-\Delta_s^6q_s^3.                        \tag{2.4}
$$

已经证明的完整分支是：

- [所有自身接触阶至少三](R150-appendix-rank-one-third-cumulant-high-contact-mean-divisor-classification.md)，以及该文的空支 $\Delta_s^2\Delta_t^3$、$q_s(t)=0$；
- [三个低接触族](R150-appendix-rank-one-third-cumulant-three-low-contact-mean-divisor-classification.md) $\Delta_s q_s\Delta_t$、$q_s\Delta_t^2$、$q_s^2/\Delta_t$，均保 $q_s(t)=0$。

这些分支的所有存活点满足 $P_y\propto k_s$。它们各自的合流、零参数和射影边界已付，不能凭 generic 分拆就认定穷尽；下面完成余下部分。

## 3. 剩余四个两根族和完整梯度

选有序射影点 $t,r$，要求
$$
\Delta_t\Delta_r\mid q_s.                             \tag{3.1}
$$
允许 $t=r$，但此时必须是真正的二重根。令 $e=q_s/(\Delta_t\Delta_r)$，这是非零齐次一次式。四族为
$$
(j,A,B)=(2,2,1),(1,3,1),(1,2,2),(0,3,2),\qquad
f=\Delta_s^j\Delta_t^A\Delta_r^B,\quad P_y=\sigma f,\quad \sigma\ne0.
                                                               \tag{3.2}
$$
分别简称221、131、122、032，数字始终依次对应 $s,t,r$ 的显示指数。

按原权 $(1,2,3)$ 置 $\sigma=1$、$\eta=4c/\sigma^3$。由原 $J_2$ 可逆，最高方程唯一给
$$
y=K^{-1}[f],\qquad H_m=X_m+\eta Y_m,\quad
X=\tfrac16J_2^{-1}[f^2],\quad Y=\tfrac16J_2^{-1}[w],
\quad V=\tfrac\eta4u(s)^{\otimes3},                    \tag{3.3}
$$
$$
w=-\Delta_s^{6-j}\Delta_t^{3-A}\Delta_r^{3-B}e^3.       \tag{3.4}
$$
各指数非负，$fw=k_s^3$ 准确成立，$f$ 从不恒零；不除节点差或判别式。方括号始终表示完整齐次系数。

全部原低梯度必须使用以下公式。记 $p=Ky,F=y^{\mathsf T}Ky/2,h=Hp,b_0=p^{\mathsf T}Hp,\tau_2=\operatorname{tr}((KH)^2)$，$P=P_y(s)$，由 $w(s)=0$ 得 $G=G_H(s)=P^2/6$。则
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp+\eta(P^2-2G)u(s),
$$
$$
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH
 +\eta P u(s)u(s)^{\mathsf T},
$$
$$
\nabla_y\mathcal Q_3=3K\Gamma,\quad
\partial_{H_m}\mathcal Q_3=-6n_m,\quad
n_m=[z^m]u(1,z)^{\mathsf T}KNKu(1,z).                  \tag{3.5}
$$
032族一般有 $P\ne0$，三阶贡献不可删除。新源保全部六 mean、十一二阶、十六最高梯度，并核四参数 $s,t,r,\eta$ 的完整链式法则。

## 4. 两次原除法和三层结式

有限 $s,t,r$ 时，以 $q_s(z)=q_0+q_1z+q_2z^2+q_3z^3$ 定义
$$
d(z)=(q_1+q_2t+q_3t^2)+(q_2+q_3t)z+q_3z^2,\qquad
e(z)=q_2+q_3(t+r)+q_3z.
$$
准确恒等式为
$$
q_s(z)=(z-t)d(z)+q_s(t),\qquad d(z)=(z-r)e(z)+d(r).
                                                               \tag{4.1}
$$
所以 (3.1) 的真正有限约束是
$$
q_s(t)=0,\qquad d(r)=0.                               \tag{4.2}
$$
在 $t=r$ 时，第二条正是需要的重数条件，不能换成重复的 $q_s(t)=0$。

先在整个参数平面定义 (3.3)、(3.4)，置 $E=q_s(t)+(z-t)d(r)$。原最高残差是
$$
f^3-6fG_H+\eta k_s^3
=-\eta(z-s)^6 E\{3q_s(z)^2-3q_s(z)E+E^2\}.            \tag{4.3}
$$
全部低梯度由 (3.5) 给出，仍对 $\eta$ 至多二次。对
$a=a_2\eta^2+a_1\eta+a_0$、$b=b_2\eta^2+b_1\eta+b_0$，采用固定四阶 Sylvester 行列式
$$
\mathscr R_2(a,b)=(a_2b_0-a_0b_2)^2
 -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
$$
共同有限根必使它为零，首项特殊化降次不影响必要性。取
$$
R_{01}=\mathscr R_2(n_0,n_1),\quad R_{02}=\mathscr R_2(n_0,n_2),
$$
$$
N_i(s,t)=\operatorname{Res}_r(d(r),R_{0i}),\qquad
A_i(s)=\operatorname{Res}_t(q_s(t),N_i),\quad i=1,2.   \tag{4.4}
$$
任一同源有限完整临界点都使 $A_1(s)=A_2(s)=0$。两层根结式在原有理数多项式环中定义，不删特殊降次。

定义
$$
D(s)=5s^8+50s^7+153s^6-936s^5-2888s^4
 +15936s^3-3392s^2-25472s+9600.                       \tag{4.5}
$$
完整 QQ 运算给：

| 族 | 两个 $A_i$ 次数 | QQ gcd，差非零常数 | 两余因子次数 | 完整阶数 | 行列式 mod1009 |
|---|---|---|---|---:|---:|
| 221 | 620,620 | $s^{24}(s+1)^{156}D^8$ | 376,376 | 752 | 12 |
| 131 | 620,620 | $s^{24}(s+1)^{156}$ | 440,440 | 880 | 610 |
| 122 | 648,648 | $(s+1)^{168}$ | 480,480 | 960 | 294 |
| 032 | 648,648 | $(s+1)^{168}$ | 480,480 | 960 | 198 |

源直接计算首一 QQ gcd，再准确核其等于表中首一化因子。全部除法余式零；每个余因子系数分母模1009为单位，两个最高项约化不消失。因此完整固定 Sylvester 行列式定义于 $\mathbb Z_{(1009)}$，非零约化严格推出有理数行列式非零，两个余因子没有共同复根。

221只余 $s=0,-1$ 或 $D(s)=0$；131只余 $s=0,-1$；122与032只余 $s=-1$。这只是必要条件，以下把各纤维完整返回原方程。

## 5. $s=-1$ 的全部有限和射影根对

原式是
$$
q_{-1}(a,b)=-a(6a^2+26ab+5b^2).
$$
记 $h(T)=5T^2+26T+6$，其判别式556非零，所以两有限根不同，无穷远也仅是单根。(3.1) 的全部有序根对仅有：

1. $t=T,r=-26/5-T$，$h(T)=0$；
2. $t=\infty,r=T$，$h(T)=0$；
3. $t=T,r=\infty$，$h(T)=0$。

不允许两个无穷远或重复有限根。

第一种在 $E_h=\mathbb Q[T]/(h)$ 中，将原 $R_{01}$ 代入 $s=-1,t=T,r=-26/5-T$，得到准确余类 $v$。四个族均求出 $w$ 并回乘核
$$
vw=1\quad\text{于 }E_h.                              \tag{5.1}
$$
这排除原 $R_{01}=0$，不需选复嵌入或近似根。

另两种须直接用齐次式。置 $\ell(z)=5z+26+5T$；在 $h(T)=0$ 上有 $h(z)=(z-T)\ell(z)$。准确仿射式为
$$
\begin{array}{c|c|c}
&f(1,z)&w(1,z)\\\hline
t=\infty,r=T&(-1)^A(1+z)^j(z-T)^B&
(-1)^A(1+z)^{6-j}(z-T)^{3-B}\ell(z)^3\\
t=T,r=\infty&(-1)^B(1+z)^j(z-T)^A&
(-1)^B(1+z)^{6-j}(z-T)^{3-A}\ell(z)^3
\end{array}                                         \tag{5.2}
$$
均补足五次、十次齐次系数；$\Delta_\infty=-a$ 的符号已经保留。对原 $u(-1)$，按 (3.3)、(3.5) 重建全部原矩与梯度，先在 $E_h$ 中核十六最高式全零，再对两原二阶梯度取四阶 $\eta$ 结式。所得 $v$ 仍分别有 (5.1)。

| 族 | 有限/有限 $\deg_Tv$ | 无穷远/有限 $\deg_Tv$ | 有限/无穷远 $\deg_Tv$ | 完整 QQ 核验 |
|---|---:|---:|---:|---|
| 221 | 1 | 1 | 1 | 三个 $vw\equiv1\pmod h$ |
| 131 | 1 | 1 | 1 | 三个 $vw\equiv1\pmod h$ |
| 122 | 0 | 1 | 1 | 三个 $vw\equiv1\pmod h$ |
| 032 | 1 | 1 | 1 | 三个 $vw\equiv1\pmod h$ |

$v$ 由 (3.3)–(3.5)、固定四阶行列式与显示代入完全确定；$w$ 由源中的准确扩展 Euclid 算法计算后重新回乘核每个系数。这是有限有理数 Bézout 证书。若某个复根对应原临界点，将 (5.1) 送至该根即得 $0=1$。所以四族的整个 $s=-1$ 射影纤维均空。

## 6. 221族的八次判别式纤维

直接展开原三次判别式给
$$
\operatorname{disc}_z q_s(z)=s^2D(s).                 \tag{6.1}
$$
在 $E_D=\mathbb Q[s]/(D)$ 写 $q_s(z)=a_3z^3+a_2z^2+a_1z+a_0$。源准确证明 $a_3=s+1$ 与 $2(a_2^2-3a_3a_1)$ 均为单位，故定义
$$
\alpha=\frac{9a_3a_0-a_2a_1}{2(a_2^2-3a_3a_1)},\qquad
\beta=-a_2/a_3-2\alpha.                              \tag{6.2}
$$
各分母以 QQ 逆身份支付，原 $D$ 的任何复根都未被删除。逐项准确核验
$$
q_s(z)=a_3(z-\alpha)^2(z-\beta)\quad\text{于 }E_D[z],  \tag{6.3}
$$
并核 $\alpha-\beta,s-\alpha,s-\beta$ 均为单位。因此每个 $D$ 根对应一个真正二重根 $\alpha$ 和不同单根 $\beta$，均异于 $s$，没有隐藏三重根或接触边界。

原有序根对恰为三种：

- $(\alpha,\alpha)$：$f=\Delta_s^2\Delta_\alpha^3$，已由完整23空支排除；
- $(\alpha,\beta)$：$f=\Delta_s^2q_s/a_3=-k_s/a_3$，为同点族；
- $(\beta,\alpha)$：唯一需另排的反向分配。

对最后一项将同一个原 $R_{01}(s,t,r)$ 按 (6.2) 代入，在 $E_D$ 中约减为七次以下的 $v_D$。源准确求出 $w_D$ 并回乘核
$$
v_Dw_D=1\quad\text{于 }\mathbb Q[s]/(D).              \tag{6.4}
$$
故 $v_D$ 在 $D$ 的任何复根都非零，与完整临界性必需 $R_{01}=0$ 矛盾。整条反向分配被排，判别式纤维只留下 $P_y\propto k_s$。不需要 $D$ 不可约或数值枚举其根。

## 7. $s=0$、$s=\infty$ 及四族全结论

$s=0$ 时 $q_0=z^2(z-5)$，有序根对仅 $(0,0),(0,5),(5,0)$。
$s=\infty$ 时 $q_\infty=a^2(a+b)$，仅 $(\infty,\infty),(\infty,-1),(-1,\infty)$。
原重数约束没有其他可能。

记 $E_5$ 为已排的 $\Delta_s^5$，$E_{32}$ 为已排的 $\Delta_s^3\Delta_t^2$，$E_{23}$ 为已排的 $\Delta_s^2\Delta_t^3$，$S$ 为 $f\propto-k_s$。直接代 (3.2) 得：

| 族 | $(0,0)$或$(\infty,\infty)$ | $(0,5)$或$(\infty,-1)$ | $(5,0)$或$(-1,\infty)$ |
|---|---|---|---|
| 221 | $E_5$ | $S$ | $E_{32}$ |
| 131 | $E_5$ | $S$ | $E_{23}$ |
| 122 | $E_5$ | $E_{32}$ | $E_{32}$ |
| 032 | $E_5$ | $E_{32}$ | $E_{23}$ |

例如221在两纤维上依次是 $z^5,z^4(z-5),z^3(z-5)^2$ 和 $-a^5,a^4(a+b),-a^3(a+b)^2$，比例与无穷远符号均为原齐次身份。所引空支已经保全部原参数与低梯度，不重复旧计算。

有限 $s\ne-1$ 时 $q_s$ 不含无穷远根；有限 $s=-1$ 已由 §5 完成；$s=\infty$ 正是本表。因此没有其余射影边界。结合 §§4–7，四个两根族的所有完整临界点都满足 $P_y\propto k_s$：122和032全空，131只留 $s=0,\infty$ 同点族，221另有判别式中的同点族。

## 8. 所有五次除子型的穷尽

对任意原秩一临界点，设 $j=\operatorname{ord}_sP_y$ 为准确自身接触阶。$j\ge3$ 已闭。对 $j=0,1,2$，写 $P_y=\Delta_s^j h$，$h$ 所有根均异于 $s$。由 (2.4)，它们是 $q_s$ 根，重数至多为在 $q_s$ 中重数的三倍。如下表穷尽：

| $j$ | $h$ 在不同根上的重数分拆 | 已闭族 |
|---:|---|---|
| 2 | $3$ | 完整23空支 |
| 2 | $2+1$ | 两根221 |
| 2 | $1+1+1$ | $h\propto q_s$，直接 $P_y\propto k_s$ |
| 1 | $4$ | 两根131，取 $t=r$ |
| 1 | $3+1$ | 两根131，取不同根 |
| 1 | $2+2$ | 两根122 |
| 1 | $2+1+1$ | $\Delta_s q_s\Delta_t$ |
| 0 | $5$ | 两根032，取 $t=r$ |
| 0 | $4+1$ | $q_s\Delta_t^2$ |
| 0 | $3+2$ | 两根032 |
| 0 | $3+1+1$ | $q_s\Delta_t^2$ |
| 0 | $2+2+1$ | $q_s^2/\Delta_t$ |

若 $h$ 有单根重数四或五，$h\mid q_s^3$ 迫该根在 $q_s$ 至少二重，所以取 $t=r$ 真正满足 (3.1)，没有伪造双根。对于 $4+1$，设根为 $t,r$，则 $q_s$ 必与 $\Delta_t^2\Delta_r$ 成比例，故 $h\propto q_s\Delta_t^2$，额外的重根分配确已包含。

含三个不同根时，$q_s$ 必与三因子乘积成比例，表中的三个低接触表示因此准确。四或五个不同根不可能，因为 $q_s$ 只有三次。若 $q_s$ 还含 $s$，可用异点根只会更少；不会增加新分拆。此证明完全在 $\mathbb P^1$ 上，不依赖有限节点或一般位置。

所以整个秩一 $V$ 原临界层都满足 $P_y\propto k_s$。

## 9. 准确参数、充分性和完整 Bell 零性

$K$ 可逆与 $P_y\propto k_s$ 给 $y=a u(s)$，$a\ne0$。代最高式 (2.3)，在多项式整环中取消非零 $k_s$，得
$$
G_H=\frac{a^3+4c}{6a}k_s^2.
$$
原 $J_2$ 可逆，而 $u(s)u(s)^{\mathsf T}$ 的像恰是 $k_s^2$，故 $H$ 唯一为 (1.1)。这证明必要性，没有多余自由二阶矩。

反过来，(1.1) 中 $u(s)^{\mathsf T}Ku(s)=0$ 给
$$
F=Hp=HKH=(KH)^2=P_y(s)=G_H(s)=0.
$$
全部低梯度 (3.5) 为零；最高式的系数是
$$
a^3-6a\frac{a^3+4c}{6a}+4c=0.
$$
因此全部三十三个原梯度为零；同一系数也是 $T_3$ 中 $u(s)^{\otimes3}$ 的系数，故 $T_3=0$。定理的必要性、充分性及任意方向 Bell 零性均证毕。

## 10. 原计算身份与环境恢复

当前可重现源为[2026-11-26-r150-rank-one-two-root-families-verify.py](../notes/2026-11-26-r150-rank-one-two-root-families-verify.py)。初次执行的旧源码字节随后因执行环境丢失，其历史 SHA256 为：
a9a2916849bb6812251c187572dfcc13824271ce1a4b8d4658560bdd3d21b289。

执行命令为 `PYTHONPATH=<python-flint位置> python <该源> <参数> --wall-seconds 240`，内存上限1536 MiB；源码不读取外部数组。四参数 s2_t2_r、s_t3_r、s_t2_r2、t3_r2 于2026-11-26用Python3.12.14和python-flint在原本地执行器全 exit0。完整源从整数K构造逆矩阵、全部原梯度和四方向链式法则；计算三层QQ结式、完整gcd/除法和模1009全矩阵门；最后验证全部二次/八次商代数的QQ逆与回乘，没有复数近似。原stdout SHA依参数顺序为：

- 4c0b1a966d9b092a8e3b57226d46a30a4d7b71eda889d926683fa182b212503f；
- fb127aefa9ded60110d442d230de997d273e10034fab6cbbefe4e374788fc9cb；
- c230376a0aad1d7b653f1768a08f5278e5035b05c430b17f708dc86409dfa729；
- 56d040bd7fc6bbc8891d0fcd3a55c73cbd6a6835162fe3d18c7fa0e2c347f4b9。

四个小回执为[221](../notes/2026-11-26-two-root-s2_t2_r-execution.json)、[131](../notes/2026-11-26-two-root-s_t3_r-execution.json)、[122](../notes/2026-11-26-two-root-s_t2_r2-execution.json)、[032](../notes/2026-11-26-two-root-t3_r2-execution.json)。

原执行环境随后丢失。本正文从本会话的已写完整证明和原工具回执恢复，数学内容和数字保持；不声称原正文逐字节复原。当前重建源码 SHA256 为 13513509b4a11ac1acdfa1fb7f336773ce51efc0d6b36314385b28002b93f1cf，字节身份与旧源不同。为了给当前公开源码提供对应证据，已在新执行器以 Python 3.12.14、python-flint 0.9.0 对四参数重新执行必要 QQ 门，全 exit 0。全部原梯度、三层结式次数、完整 QQ gcd 和余因子、752/880/960/960 阶门、十二个二次商代数单位门和八次纤维的全部逆身份均准确重现。新 stdout SHA256 依次为 33940a10f27c6eade958b600915fa165e337ec51456566ca67e7de0d929da338、2207e8203699ef9cf9c860c49cbb5c31778830e84658a9e41ac3643d0b78d221、e871770cf08c9699aa190a6011f1954c90b30c710a4738a0dd36bf47a26050c1、87604feccdcfcf1df124c8da0bac2876442152aa48feb90ec63f013e42f902ac。上述四小回执各自明确分开旧历史对象与当前新源的完整标量回执，没有把旧 SHA 指向新字节。可重算大数组不入库。

本结果关闭非零rankV1全层；高秩V、原全局自然幂来源、算子费用桥及普通Hilbert ISP仍未闭。

