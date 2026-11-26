# R150 附录：保留全部三阶贡献的三个低接触极线族

日期：2026-11-26。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 下述三个完整原秩一第三累积量族的临界点均已分类，所有存活点的第三普通矩为零。后二族不假设 $P_y(s)=0$，完整保留原三阶累积量对低梯度的贡献。

## 1. 原对象、准确分支和规范

使用[原完整定义](R150-appendix-rank-one-third-cumulant-three-plus-one-plus-one-mean-divisor-classification.md) §§1–3 的整数矩阵 $K$、$u(a,b)=(a^5,a^4b,\ldots,b^5)^{\mathsf T}$、原 Hankel 二阶矩 $H_{ij}=H_{i+j}$、三阶累积量 $V_{ijk}=V_{i+j+k}$ 和 $\mathcal Q_3$。该文已从完整有限微分展开导出全部原梯度，本稿不改这些坐标或合并键。

设
$$
V=v u(s)^{\otimes3}\ne0,\quad P_y(x)=(Ky)^{\mathsf T}u(x),\quad
k_s(x)=u(s)^{\mathsf T}Ku(x)=-\Delta_s(x)^2q_s(x),
$$
其中 $\Delta_s(a,b)=s_0b-s_1a$。有限图中
$$
q_s(z)=(s^3-5s^2)+(s^3-3s^2+22s)z
 -(3s^2+3s+5)z^2+(s+1)z^3.                    \tag{1.1}
$$
$q_s$ 为二元三次式；$K$ 可逆，所以它在每个射影 $s$ 上都非零。

取满足 $q_s(t)=0$ 的射影点 $t$，记 $d_{s,t}=q_s/\Delta_t$。这是准确的非零二元二次多项式，不含参数分母。本文处理 $P_y=\sigma f_\bullet$、$\sigma\ne0$ 的三族
$$
f_A=\Delta_s q_s\Delta_t,\qquad
f_B=q_s\Delta_t^2,\qquad
f_C=q_s d_{s,t}=q_s^2/\Delta_t.                 \tag{1.2}
$$
允许 $s=t$、重根和无穷远，不除以判别式或节点差。

$\mathcal Q_3$ 对 $(y,H,V)$ 的权为 $(1,2,3)$。原权缩放可置 $\sigma=1$、$\eta=4v/\sigma^3\ne0$。最高方程为
$$
P_y^3-6P_yG_H+\eta k_s^3=0,\qquad
G_H=u^{\mathsf T}KHK u.
$$
令 $J_2$ 为 $k((1,z),(1,\zeta))^2$ 的完整系数矩阵，即
$(J_2)_{mn}=\sum_{i+a=m,j+b=n}K_{ij}K_{ab}$。由于
$$
\det K=-25600,\qquad \det J_2=-64701092257700249600,
$$
全部最高方程唯一给出
$$
y=K^{-1}[f],\qquad
H_m=X_m+\eta Y_m,\quad
X=\tfrac16J_2^{-1}[f^2],\quad
Y=\tfrac16J_2^{-1}[w],\quad
V=\tfrac\eta4u(s)^{\otimes3},                  \tag{1.3}
$$
其中完整十次式为
$$
w_A=-\Delta_s^5q_s d_{s,t},\quad
w_B=-\Delta_s^6d_{s,t}^2,\quad
w_C=-\Delta_s^6q_s\Delta_t.                   \tag{1.4}
$$
方括号始终表示完整齐次系数；$fw=k_s^3$，所以这里只在多项式整环中取消非零 $f$，没有除以某个可能为零的参数值。

## 2. 完整三阶贡献不能删除

写
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad h=Hp,\quad
b_0=p^{\mathsf T}Hp,\quad \tau_2=\operatorname{tr}((KH)^2),\quad
P=P_y(s),\quad G=G_H(s).
$$
(1.4) 给 $w(s)=0$，故 $G=P^2/6$。A族有 $P=0$，B、C族一般没有。

原完整梯度精确为
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp
       +\eta(P^2-2G)u(s),                    \tag{2.1}
$$
$$
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH
       +\eta P\,u(s)u(s)^{\mathsf T},         \tag{2.2}
$$
$$
\nabla_y\mathcal Q_3=3K\Gamma,\qquad
\partial_{H_m}\mathcal Q_3=-6n_m,\quad
n_m=[z^m]u(1,z)^{\mathsf T}KNKu(1,z).         \tag{2.3}
$$
这是将原 $4V(p,p,\cdot)-8V:(KHK)$ 和 $4V_p$ 全部代入后的公式；(2.1) 的新增向量等于 $2\eta P^2u(s)/3$。

原多项式在 (1.3) 上等于
$$
G_6=F^3-6Fb_0+6F\tau_2+12p^{\mathsf T}HKHp
 -8\operatorname{tr}((KH)^3),
$$
因为三阶线性部分是 $\eta(P^3-6PG)=0$，二次部分含 $k_s(s)^3=0$。但求原偏导前不能删除这些项。新源使用 (2.1)、(2.2)，并对 $s,t,\eta$ 核验完整链式法则
$$
\partial_\theta G_6=
3(K\Gamma)^{\mathsf T}\partial_\theta y
-6\sum_m n_m\partial_\theta H_m
+4\sum_m[P_y^3-6P_yG_H+\eta k_s^3]_m\partial_\theta V_m. \tag{2.4}
$$
最后一项在保留并计算后才被核为零。全部六 mean、十一二阶和十六最高方程均由原式构造。

## 3. 有限图的准确有理数结式

有限 $s,t$ 时写 $q_s(z)=q_0+q_1z+q_2z^2+q_3z^3$，置
$$
d=(q_1+q_2t+q_3t^2)+(q_2+q_3t)z+q_3z^2,
\quad q_s(z)=(z-t)d+q_s(t).                   \tag{3.1}
$$
在整个有限平面按这些多项式及 (1.2)–(1.4) 构造 (1.3)。记 $q=q_s(z),q_*=q_s(t),\delta=z-s$，则
$$
fw-k_s^3=
\begin{cases}
\delta^6q^2q_*,&A,C,\\
\delta^6q q_*(2q-q_*),&B.
\end{cases}                                 \tag{3.2}
$$
所以在原根约束上最高方程准确成立。

全部 $n_i$ 对 $\eta$ 至多二次。对 $a=a_2\eta^2+a_1\eta+a_0$、$b=b_2\eta^2+b_1\eta+b_0$，定义固定四阶 Sylvester 行列式
$$
\mathscr R_2(a,b)=(a_2b_0-a_0b_2)^2
 -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
$$
存在共同有限根必使其为零，即使首项特殊化后消失也成立。令
$$
R_{01}=\mathscr R_2(n_0,n_1),\quad R_{02}=\mathscr R_2(n_0,n_2),
$$
$$
A_*(s)=\operatorname{Res}_t(q_s(t),R_{01}),\quad
B_*(s)=\operatorname{Res}_t(q_s(t),R_{02}).     \tag{3.3}
$$
任一完整临界点必使两者为零。所有对象均由本文原矩公式作有限有理数运算唯一确定。

实际准确计算给：

| 族 | 两个 $R$ 的 $t$ 次数 | 两个 $s$ 结式次数 | 精确首一 gcd，差常数因子 | 余因子次数 | 完整阶数 | 行列式 mod1009 |
|---|---|---|---|---|---:|---:|
| A | 16,16 | 236,236 | $s^{24}(s-2)^8(s+6)^8(s+1)^{12}$ | 184,184 | 368 | 240 |
| B | 32,32 | 248,248 | $s^{24}(s-2)^8(s+6)^8(s+1)^{24}$ | 184,184 | 368 | 255 |
| C | 20,20 | 256,256 | $s^{12}(s+1)^{24}$ | 220,220 | 440 | 621 |

gcd 先在 QQ 中直接计算，再核验显示因式与准确无余式除法。每个余因子系数的分母模1009为单位，两个首项约化后不消失。因此完整固定 Sylvester 矩阵定义于 $\mathbb Z_{(1009)}$，上表非零约化严格推出有理数行列式非零，余因子在 $\mathbb C$ 无共同根。A、B族只剩 $s\in\{0,2,-6,-1\}$；C族只剩 $s\in\{0,-1\}$。这里没有从有限域无解性直接推复数无解。

## 4. 全部有限特殊纤维

原因式分解为
$$
q_0=t^2(t-5),\quad
q_2=(t-2)(3t^2-17t+6),\quad
q_{-6}=(t+6)(-5t^2-65t-66),\quad
q_{-1}=-5t^2-26t-6.                          \tag{4.1}
$$
A、B族在前三行分别准确除去 $t^2,t-2,t+6$；C族在 $s=0$ 只除去 $t-5$；$s=-1$ 不除因子。记余下因子为 $q_{\rm rem}$，从原 $R_{01}$ 先特殊化再按真实次数计算 $\operatorname{Res}_t(q_{\rm rem},R_{01}(s,t))$：

| 族 | $s$ | 原 $R_{01}$ 真实次数 | 结式 mod1009 |
|---|---:|---:|---:|
| A | 0 | 12 | 979 |
| A | 2 | 16 | 876 |
| A | −6 | 16 | 934 |
| A | −1 | 12 | 959 |
| B | 0 | 32 | 192 |
| B | 2 | 32 | 883 |
| B | −6 | 32 | 838 |
| B | −1 | 24 | 327 |
| C | 0 | 20 | 900 |
| C | −1 | 12 | 307 |

这些原有理数结式的分母均为1009单位，所以全部非零。这排除 $q_{\rm rem}$ 的所有复根，包括重根。因此有限图只余
$$
A,B:\ (0,0),(2,2),(-6,-6);\qquad C:\ (0,5).   \tag{4.2}
$$

## 5. 全部射影边界

$q_\infty(a,b)=a^2(a+b)$，而有限 $s$ 的 $q_s(\infty)=s+1$。因此只有 $(\infty,-1),(-1,\infty),(\infty,\infty)$ 三个组合。令 $h(z)=5z^2+26z+6$。直接取原齐次式得到以下排除门：

| 族 | $(s,t)$ | $f(1,z)$ | $w(1,z)$ | 原 $n_0,n_1$ 四阶结式 mod1009 |
|---|---|---|---|---:|
| A | $(\infty,-1)$ | $-(1+z)^2$ | $1+z$ | 627 |
| A | $(-1,\infty)$ | $(1+z)h$ | $(1+z)^5h^2$ | 357 |
| B | $(\infty,-1)$ | $(1+z)^3$ | $-1$ | 872 |
| B | $(-1,\infty)$ | $-h$ | $-(1+z)^6h^2$ | 702 |
| C | $(\infty,\infty)$ | $-(1+z)^2$ | $1+z$ | 627 |
| C | $(-1,\infty)$ | $-h^2$ | $-(1+z)^6h$ | 312 |

每行均使用 $u(\infty)=e_5$ 或 $u(-1)=(1,-1,1,-1,1,-1)^{\mathsf T}$，按 (1.3)、完整 (2.1)–(2.3) 重建全部梯度。B、C的 $s=-1$ 边界一般 $P_y(s)\ne0$，三阶贡献一直保留。各分母与两个二次首项模1009为单位，因此这些非零行列式严格提升，六行全部为空。

A、B留下 $(\infty,\infty)$，C留下 $(\infty,-1)$。其原齐次式都准确为
$$
f=a^4(a+b)=-k_\infty,\qquad w=-a^8(a+b)^2=-k_\infty^2.
$$
所有仿射多项式按原五次、十次齐次系数补足，不因仿射降次遗漏无穷远支撑。

## 6. 完整分类、充分性与 Bell 零性

三个族的完整临界参数恰为
$$
A,B:\ (s,t)=(0,0),(2,2),(-6,-6),(\infty,\infty);
\qquad
C:\ (s,t)=(0,5),(\infty,-1).                  \tag{6.1}
$$
每个存活参数有 $f=-k_s,w=-k_s^2$，所以全部原矩唯一为
$$
y=-u(s),\qquad H=\frac{1-\eta}{6}u(s)u(s)^{\mathsf T},
\qquad V=\frac\eta4u(s)^{\otimes3},\quad\eta\ne0. \tag{6.2}
$$
直接由 $u(s)^{\mathsf T}Ku(s)=0$ 得 $F=Hp=HKH=(KH)^2=0$，且此时 $P_y(s)=0$，全部低梯度为零。最高梯度则为 $\{-1+(1-\eta)+\eta\}k_s^3=0$，所以这些确实是全部原临界点，不是仅满足排除阶段几个必要方程。

完整第三普通矩为
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V
=\{-1+(1-\eta)+\eta\}u(s)^{\otimes3}=0.
$$
故所有方向的完整匹配 Bell 立方均零。原非零权缩放只把此等式同乘 $\sigma^3$。

## 7. 计算来源与恢复说明

[现可复现的完整源码](../notes/2026-11-26-r150-rank-one-three-low-contact-families-verify.py)从原整数 $K$ 重建全部对象，无外部矩阵输入。当前源码 SHA-256 为
4c851d6eae6d894b879bc0845aa449f04ce8fb33fd7089d59eb72173990e6a2b。
以 Python 3.12.14、python-flint 0.9.0，分别运行参数 `s_q_t`、`q_t2`、`q2_over_t`，默认 `--wall-seconds 240`、内存上限1536 MiB，全部 exit0。完整QQ消元、所有有限/射影边界、原三阶贡献及链式法则都准确重现本稿数值。

| 参数 | 源内秒数 | 完整 stdout SHA-256 | 小执行记录 |
|---|---:|---|---|
| s_q_t | 0.3946923930052435 | 50992833520a538fb9c09e9ed3d9c1a6505a340ca0e7b3d276dbfbde68500eae | [A](../notes/2026-11-26-recovered-low-s_q_t-execution.json) |
| q_t2 | 0.6322320850013057 | c6afcfe39ac992463891f5b4a7f0617d4b5f13fb369170a479393ef71afa972a | [B](../notes/2026-11-26-recovered-low-q_t2-execution.json) |
| q2_over_t | 0.5208061630110024 | f0dfd2f0266e262c67d4d2ce559da62ea3f1703f0fda642a761920d0bd4b49b4 | [C](../notes/2026-11-26-recovered-low-q2_over_t-execution.json) |

先前同日的原执行源码 SHA-256 为3190e876b0c5c8bba257867068b8ac08633ed8d89407620aad4796f4bc6f9c1b；原三标签均已成功，时间、实际工具片段身份见[历史执行记录](../notes/2026-11-26-r150-three-low-contact-local-execution.json)。原stdout当时未保存，因此不为其编造SHA。原执行环境随后丢失；恢复源码字节不同，上表属于新源码的新执行，不能以旧SHA冒用。此次只为未登记新源的丢失恢复核对，未重做已登记的高接触或311结论。

本稿只关闭这三个完整原族。其余除子型、全局原 Jacobian 自然幂与普通 Hilbert ISP 不由本稿单独解决。只提交源码、参数、执行身份、SHA与紧凑标量，不保存可重算矩阵数组。
