# R150 附录：L=0 的线性 lambda 投影曲线完整原排除

作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：已证明。** 在单位 $2+1+1$ 非零孤立点均值的原 $L=0$ 图中，整个曲线
$$
\mathcal W(\lambda,w)=4\lambda w+2\lambda-2w^2-4w-1=0
\tag{1}
$$
没有合法原临界点。这里保原全部九式、同一 Gram 和全部 $P_1$ 首项零纤维。结论只关闭 (1)，不关闭 $L=0$ 的其他投影曲线、孤立交点或一般 $LS\ne0$ 图。

## 1. 已付原分支与没有遗漏的参数化

沿用[完整原 U 值坐标](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)。
零/相等/相反配对、零孤立点均值、整个 $P_0=0$ 和共同规范 $u=1$ 已分别排除。
$L=0$ 的 $w=0,1$ 及[整个零权重和 $b+c=0$](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-zero-weight-sum-exclusion.md)也已关闭，本稿只引用。

在其余图中作原允许的共同规范 $p+q=2$，写
$$
p=1+\kappa,\quad q=1-\kappa,\quad
\kappa^2=\Delta=1-Q,\quad Q=pq,
$$
$$
h=1+\rho p,\qquad k=1+\rho q.
\tag{2}
$$
这保持 $q(h-1)-p(k-1)=0$。所有规范化只沿用原坐标图，后面不独立缩放某条配对。

定义
$$
R=\lambda-1-w,\quad
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
C=RB-A^2.
$$
原三个 U 矩给
$$
u=\frac R\rho,\quad V_2=\frac A{\rho^2},\quad
Q=\frac{2A\rho-B}{\rho^2R},\quad
l=b+c=\frac{2u-V_2}{Q},
\tag{3}
$$
$$
b=\frac l2+\frac{u-l}{2\Delta}\kappa,\qquad
c=\frac l2-\frac{u-l}{2\Delta}\kappa,\qquad a=1-l.
\tag{4}
$$
完整二次代数 $\mathbb Q(\rho,\lambda,w)[\kappa]/(\kappa^2-\Delta)$ 保留两个原分配，并未选平方根。

进一步有精确原身份
$$
bc=\frac{l^2\Delta-(u-l)^2}{4\Delta},\qquad
C=4\rho^4bcQ\Delta,
$$
$$
2P_0=(2-3u)V_2-Qu+2u^3
=\frac{B-3RA+2R^3}{\rho^3}.
\tag{5}
$$
原 $N(V)$ 的一次图给
$$
f=-\frac{u(w/2-w^2)+\rho(V_2-2u^2)/4+\lambda\rho^2P_0}
 {w(w-1)}.
\tag{6}
$$

本稿全部分母来自原已付单位
$$
\rho,\lambda,w,w-1,R,C,\Delta,Q,P_0,u-1,l.
\tag{7}
$$
特别没有把 $A$ 当作单位；$A=0$ 的整个纤维保留。

在曲线 (1) 上
$$
(4w+2)\lambda=2w^2+4w+1.
$$
若 $2w+1=0$，原 (1) 左边恰为 $1/2$，不可能为零。因此 (1) 全部有限点准确参数化为
$$
\lambda=\frac{2w^2+4w+1}{4w+2},\qquad 2w+1\ne0.
\tag{8}
$$
新增分母由 (1) 本身支付，不是删除一个尚未处理的首项零分支。代入后 (2)–(6) 都处在 $\mathbb Q(\rho,w)[\kappa]/(\kappa^2-\Delta)$。

## 2. 同一原 Gram 与原九式

以同一个原双点乘法和迹
$$
(x_0,x_1,x_B,x_C)(y_0,y_1,y_B,y_C)
=(x_0y_0,x_0y_1+x_1y_0,x_By_B,x_Cy_C),
$$
$$
\tau(x)=ax_0+x_1+bx_B+cx_C
$$
重建原条件。令
$$
T_0=V_2-2u^2,\quad
W_1=T_0/2+2fu,\quad
W_2=uT_0+f(V_2+2u^2)-bcQt+2\lambda P_0.
$$
原基点 mean 和第二梯度的解为
$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)},
$$
$$
r=X-ap-ct,\qquad s_1=Y-aq-bt,\qquad
A_1=2f-2bX-2cY+2bct.
\tag{9}
$$
完整原活跃 Gram 仍为
$$
K=\begin{pmatrix}
0&0&p&q\\
0&A_1&r&s_1\\
p&r&0&t\\
q&s_1&t&0
\end{pmatrix}.
\tag{10}
$$
源码直接验证原基点三式、全部 U 矩、$P(V)=N(V)=0$、B/C 共轭以及 (6) 与 (9) 的原式身份。

在同一 $\kappa$ 代数中，三 mean、三最高阶及三第二梯度取不变/反变分量，给九条 $\mathbb Q[\rho,w][t]$ 多项式，标签及 t 次数为
$$
\begin{array}{c|ccccccccc}
 &E_1&E_B^+&E_B^-&P_1&P_B^+&P_B^-&N_1&N_B^+&N_B^-\\
\deg_t&2&2&2&1&3&3&2&3&3.
\end{array}
\tag{11}
$$
每次清分母后，源码都以 (7) 及 $2w+1$ 检查分母，且只删除这些原单位的公共因子。
没有单独除 $P_1$ 的 t 系数或某个结果式首项。

## 3. 保全部 P1 降次的必要投影

写清分母后的
$$
P_1=\alpha(\rho,w)t+\beta(\rho,w).
$$
对任一原式 $F(t)=\sum_{j=0}^n F_jt^j$，使用完整齐次代入
$$
\mathcal R_{P_1,F}
=\sum_{j=0}^nF_j(-\beta)^j\alpha^{n-j}.
\tag{12}
$$
当 $\alpha\ne0$，(12) 是原共同 t 根的必要条件。
当 $\alpha=0$，原 $P_1=0$ 迫 $\beta=0$，故对于 (11) 的正次数原式，(12) 同样为零。
因此 (12) 不丢首项零或整个 $P_1$ 恒零的原点。

另对原 mean 和 $N_1$ 作完整 t Sylvester 行列式；有限共同 t 根即使令原多项式降次，也仍使这些完整行列式为零。
这一层只提供必要条件，不反称投影点为物理解。

记其中
$$
A_\rho=\mathcal R_{P_1,E_B^-},\quad
B_\rho=\mathcal R_{P_1,N_1},\quad
C_\rho=\mathcal R_{P_1,E_1},\quad
D_\rho=\operatorname{Res}_t(E_1,N_1).
$$
每个合法原点必须使这四个 $\mathbb Q[\rho,w]$ 多项式同时为零。

## 4. 三个真正 QQ 结果式已排全部有限点

现在只对 $\rho$ 作完整结果式
$$
R_B(w)=\operatorname{Res}_\rho(A_\rho,B_\rho),\quad
R_C(w)=\operatorname{Res}_\rho(A_\rho,C_\rho),\quad
R_D(w)=\operatorname{Res}_\rho(A_\rho,D_\rho).
\tag{13}
$$
每个合法有限 $\rho$ 原点仍给三个共同 w 根。
各结果式仅删除 (7) 中与 $\rho$ 无关的已付单位及曲线分母因子；绝不删除依赖 $\rho$ 的单位范数。

实际 $\mathbb Q[w]$ 运算如下：

| 使用的原 rho 结果式 | 剥已付基参数单位后的 w 次数 | 累计 monic gcd 次数 |
|---|---:|---:|
| $R_B$ | 51 | 51 |
| $R_C$ | 60 | 16 |
| $R_D$ | 99 | 0 |

两次扩展 gcd 均实际回乘
$$
s(w)G_{\rm old}(w)+t(w)R_{\rm next}(w)=G_{\rm new}(w).
\tag{14}
$$
最后共同 gcd 为 1。故 (13) 没有合法共同 w 根，继而整个 (1) 没有合法有限原 $\rho,t$ 点。
这里使用真正一变量结果式及完整 Bézout 身份，未以多变量 gcd 无公共曲线代替无孤立点。
由于已在参数轴上取得 1，不需要额外参数域返回；源码里的后备有限纤维循环实际为空。

结合第 1 节已经独立支付的边界，曲线 (1) 的整个原 $L=0$ 分支已排除。

## 5. 实际执行身份与剩余范围

自含源码：
[原完整曲线返回](../notes/2026-11-26-unit211-L0-linear-lambda-curve-original-return-347c.py)。

- Git blob：086b12957534814465fe344874f011ca55a1bba5。
- 源码 SHA-256：37d7e46fb7fe0e42169400986f0dbcaff9894a6860c58af13a31957395442e2b。
- 冻结提交：f3eb4bac533921bfcaa11becb44d7e9e68cccc3e。
- Actions run 45831444045，job 139948952171；实际 success，exit0。
- 原源 0.406508 秒，driver 0.473607752 秒；原源峰值 RSS 41812 KiB，driver 子进程 42380 KiB。
- stdout 11372 字节，SHA-256 b339e4ccc214b9d6ddec210b125b6d13392649a5e08d686d338766503002b065。
- 三个 (13) 的精确多项式 SHA-256 依次为 4949e2541caad5e102b0f775ac6441ad10332a5587b4436637b2801fe890334d、dc3b790e3d8b2249cbf68310fdeb7f34b8d79ff1152ae6e3f9980d44b7aa099c、111f20446ce54b5ccdf7d8014e87a2208c34cd40fd419c70abcf638d79721f28。
- 实际 pull 至上述冻结提交，2026-11-26 13:40:49 UTC；两 README blob 未变。

[实际小回执](../notes/2026-11-26-L0-linear-lambda-curve-execution-347c.json)保留必要阶段、次数、哈希及驱动记录；大中间多项式均由源码生成，不写入仓库。

原 L0 另一个双次数 $(7,4)$ 投影曲线、P1 双系数零面、所有大补面交点及一般 LS 图仍开放。接着使用其他原方程与更小的原投影，不重复本条或已闭的零权重和支。普通 Hilbert ISP 仍未完成。
