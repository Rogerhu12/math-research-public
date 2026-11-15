# R758 — 原 Norm3 的全部统一乘子空间与最优主阶预算

日期：2026-11-15。**状态：已证明。**

本篇在 R756 的同一个原来源格中，准确分类所有共同乘法返回。
它不只考察 R756 选出的乘子形状：允许任意非零有理函数
$\Gamma(t,Y)$，只要求它把**全部**原列的真实 Norm3 代入
同时送回一个原 canonical 格。

结论是一个显式直和。由此，任何这种返回的最高 charge $L$ 都满足
$$
L\ge3D+\left\lceil\frac{36D+65}{47}\right\rceil.
$$
R756 已给上界
$3D+\lceil(36D+181)/47\rceil$，两界相差至多三个 charge。
因此 $177D/47$ 是整个统一乘法返回类的最优主阶。
这个结论不限制只对实际因子 $F$ 成立的专用返回，
也不把曲线上的合同关系当成来源环恒等式。

## 1. 与原十九角完全相同的格

保持 R756/R680 的
$$
d=1+8t,\quad h=7+4t+16t^2,\quad v=1-4t,\quad A=v^3-216t,
$$
$$
\varphi=-27t/v^3,\qquad B=Av^{14}/d^3,\qquad
\Psi^*P=P(\varphi,BY^3).
\tag{1}
$$
对整数 $n\ge0$，
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,\quad
f_n=\lfloor9n/2\rfloor+4,
$$
$$
q_n=(th)^{A_n}(t-1)^{B_n}d^{-C_n},\qquad
e_{n+1}=f_n-3A_n-B_n+C_n .
$$
原完整来源就是
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n\,R[t]_{\le e_{n+1}},
\qquad R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)].
\tag{2}
$$
以下固定 $D\ge3$。也可把 $R$ 换成其特征零分式域，
或任一原允许剩余特征的域。因只用固定首系数单位和
原底点的互素性，所有式子在这三个意义下都成立。

对预算 $L$ 定义真正的统一乘子空间
$$
\mathcal U_{D,L}
=\{\Gamma\in R(t,Y):
\Gamma\Psi^*(\mathcal W_D)\subseteq\mathcal W_L\}.
\tag{3}
$$
$R(t,Y)$ 在这里可先理解为分式域；要求右侧属于原整格
本身就会恢复下面所述的整性。

## 2. 三组有限角阈值和唯一新极

对每个 $m\ge0$ 置
$$
\begin{aligned}
a_{D,m}&=\max_{0\le n\le D}(A_{3n+m}-A_n),\\
b_{D,m}&=\max_{0\le n\le D}(B_{3n+m}-B_n),\\
c_{D,m}&=\max_{0\le n\le D}(3n-2B_n-C_{3n+m}).
\end{aligned}
\tag{4}
$$
特别 $a_{D,m}\ge A_m\ge0$、$b_{D,m}\ge B_m\ge0$、
$c_{D,m}\ge-C_m$；最后一个整数允许为负。
定义原有理函数和其无穷远次数
$$
G_{D,m}=v^{12}(th)^{a_{D,m}}(t-1)^{b_{D,m}}d^{c_{D,m}},
$$
$$
K_{D,m}=\deg_\infty G_{D,m}
=12+3a_{D,m}+b_{D,m}+c_{D,m}.
\tag{5}
$$
负的 $c_{D,m}$ 只表示原 $d=0$ 允许极；不产生新的底点。

### 2.1 四类旧角的必要条件确实取到

对原单列 $Y^nq_n$，其拉回的 $Y^{3n}$ 系数记为 $R_n$。
R756 的准确代入给：

| 底点 | $\operatorname{ord}(R_n)$ |
|---|---:|
| $t=0$ | $A_n$ |
| $h$ 的每个根 | $A_n$ |
| $t=1$ | $B_n$ |
| $d=0$ | $2B_n-3n$ |

这些是等号，因而可用于下界。逐项验证如下。
$\varphi(0)=0$ 且 $\varphi'(0)=-27$；
在 $h$ 的每个根，$\varphi(t)=t$，
$$
\varphi'(t)=-27d(t)/v(t)^4\ne0.
$$
原 $h$ 在这些点无重根，$v,d$ 均非零，$B$ 是单位。
在1，用
$$
\varphi-1=(t-1)d^2/v^3
\tag{6}
$$
得简单零，其他因子为单位。
在 $d=0$，(6) 的零阶准确为2，而 $B$ 的极阶准确为3；
这里 $A(-1/8)=243/8$ 为单位，$\varphi=1$，其余角因子为单位。
这些常数的可能例外都已在原固定坏集中。

因此若 $Y^mR(t)$ 是统一乘子的一项，
则在 $0,h_{7,1},h_{7,2}$ 的阶至少 $a_{D,m}$，
在1至少 $b_{D,m}$，在 $d=0$ 至少 $c_{D,m}$。

### 2.2 新点的十二阶不能再省

$n=0$ 的原块包含 $1,t,t^2,t^3,t^4$。
在 $t=1/4$，$\varphi^4$ 有准确十二阶极。
目标 canonical 格在这里无极，故每一个非零 $R(t)$ 必须满足
$$
\operatorname{ord}_{t=1/4}R\ge12.
\tag{7}
$$
另一方面，R756 已证明所有原列的新极阶均不超过12：
齐次化后的 $v$ 指数是
$$
14n-3f_n\ge-12 .
$$
故 (7) 正是统一所需的新点阈值，不是粗略逐列分母总和。

## 3. 无穷远帽的准确最小值

对任意原 $F_n\in R[t]_{\le e_{n+1}}$，
$$
\deg_\infty\bigl(B^n q_n(\varphi)F_n(\varphi)\bigr)
\le14n-2A_n.
\tag{8}
$$
取 $F_n=1$ 时等号成立，因为
$\varphi\sim(27/64)t^{-2}$，$B\sim c_Bt^{14}$，
而 $q_n$ 在0的零阶恰为 $A_n$。

所以 $Y^mR$ 返回全部第 $n$ 块的无穷远条件准确为
$$
\deg_\infty R\le
I_{D,m}:=\min_{0\le n\le D}
\{f_{3n+m}-14n+2A_n\}.
\tag{9}
$$
这次最小值可以完全消去。

**引理。** 对 $D\ge3$，
$$
\boxed{I_{D,m}=f_m-1.}
\tag{10}
$$

**证明。** 写 $n=4q+r$，$0\le r\le3$。
令 $\epsilon_r=1$ 当 $r=3$，否则为0。
括号中的数准确为
$$
\left\lfloor\frac{9m-r}{2}\right\rfloor+2\epsilon_r+4.
\tag{11}
$$
四个余类都存在。若 $m$ 偶，其相对 $9m/2$ 的常数
依次是 $4,3,3,4$；
若 $m$ 奇，其相对 $\lfloor9m/2\rfloor$ 的常数
依次是 $4,4,3,5$。
两种情形的最小值均为 $\lfloor9m/2\rfloor+3$，即 (10)。证毕。

## 4. 全部统一乘子空间的精确分类

令负次数多项式空间为零。

**定理。**
$$
\boxed{
\mathcal U_{D,L}
=
\bigoplus_{0\le m\le L-3D}
Y^mG_{D,m}\,
R[t]_{\le f_m-1-K_{D,m}} .
}
\tag{12}
$$
当 $L<3D$ 时右侧为空直和。式 (12) 仍包括零乘子。

**必要性。** 因 $1\in\mathcal W_D$，任一 $\Gamma$ 满足
$\Gamma\in\mathcal W_L$。
故 $\Gamma$ 自动是 $Y$ 的多项式：
$$
\Gamma=\sum_mY^mR_m(t),
$$
每个 $R_m$ 除原 $d=0$ 外无有限极。
这排除了以一个未显示的 $Y$ 分母作共同清除的可能。

对每个纯 charge 的原列，乘积的不同 $m$ 项具有不同的 $Y$ 次数，
因此不得靠它们相消来逃避某个角条件。
取 $n=D$ 的非零单列，还必有 $3D+m\le L$。

第2节给 $R_m$ 在所有有限点的下界。
除以 (5) 后，商没有任何有限极，所以
$$
R_m=G_{D,m}H_m,\qquad H_m\in R[t].
\tag{13}
$$
整系数断言由固定因子的首系数是 $R$ 的单位得到：
清掉原 $d$ 分母后逐个作整的多项式除法，不引入移动素数。
第3节再给
$$
\deg H_m\le f_m-1-K_{D,m}.
$$
故每项都在 (12) 中。

**充分性。** 反向取 (12) 的一项。
R756 的全列式证明拉回仅可能在旧 $d=0$ 和新 $v=0$ 有有限极；
(4)、(5)、(7) 正好支付所有原目标角条件和新点。
(8)–(10) 支付完整无穷远帽。
除以目标 $q_{3n+m}$ 后是次数不超过
$e_{3n+m+1}$ 的整多项式。
所有 charge 不超过 $L$，故逐列属于 $\mathcal W_L$。
任意有限和仍成立，证明 (12)。

由 R491/R555/R680 对 (2) 的完整识别，
这里支付的是十九角的全部条件，未换成矩形包络。
定理对任意有理 $\Gamma$ 的必要性尤其不依赖先选 R756 的乘子形状。

## 5. 最优主阶和至多三个 charge 的误差

若 (12) 的第 $m$ 块非零，则
$$
K_{D,m}\le f_m-1.
\tag{14}
$$
在 (4) 的最大值中只取真实的 $n=D$，利用整数帽可得
$$
a_{D,m}\ge\frac{2D+m-3}{4},\qquad
b_{D,m}\ge\frac{2D+m-2}{3},
$$
$$
c_{D,m}\ge\frac{5D-3m-4}{6}.
\tag{15}
$$
最后一个界无需假设 $c$ 非负。
将 (15) 代入 (5)，
$$
K_{D,m}\ge
3D+\frac7{12}m+\frac{101}{12}.
\tag{16}
$$
而 $f_m-1\le(9/2)m+3$。合并 (14)、(16) 得
$$
\boxed{47m\ge36D+65.}
\tag{17}
$$
因此每一个非零 charge 分量都满足
$$
m\ge m_-(D):=\left\lceil\frac{36D+65}{47}\right\rceil.
$$
特别任一非零共同返回都必须满足
$$
\boxed{L\ge3D+m_-(D).}
\tag{18}
$$

另一方面，R756 的完整整乘子给
$$
L\le3D+m_+(D),\qquad
m_+(D)=\left\lceil\frac{36D+181}{47}\right\rceil
\tag{19}
$$
的实际可行选择。
设 $L_{\min}(D)$ 为非零统一乘法返回的最小目标预算，则
$$
\boxed{
3D+m_-(D)\le L_{\min}(D)\le3D+m_+(D),\qquad
m_+(D)-m_-(D)\le3 .
}
\tag{20}
$$
所以
$$
\boxed{\displaystyle
\lim_{D\to\infty}\frac{L_{\min}(D)}D=\frac{177}{47}.}
\tag{21}
$$
(12) 更给出每个有限 $D$ 的准确整数判定；
这里没有执行有限扫描，也没有把扫描当成 (21) 的证明。

## 6. 对当前原障碍的实际影响

(18) 特别排除了任何非零统一乘子实现
$$
\Gamma\Psi^*\mathcal W_D\subseteq\mathcal W_{3D}.
$$
即使允许 $\Gamma$ 依赖 $D$、目标素数、全部原系数，
只要仍要求对全部原列成立，结论不变。
允许多个 $Y$-charge 也不会改善主阶，因为 (12) 逐项成立。

这不排除以下更具体的工作：

- 仅对当前实际因子 $F$ 或其某个真子格构造更便宜的返回；
- 使用来源之间的真正线性算子，而非一个共同乘子；
- 在同一曲线上的实际商或同一个修正 $R$ 内使用已付的关系。

这些工作必须分别证明自己的整性、十九角、原共同 $G_0$、
完整 Gaussian 和低尾/carry；本篇没有给它们添中央零。

尤其 R756 的原低轴接触仍是 $h\mapsto h+a$，
不能因 $\Psi$ 的纤维次数为3而写成 $3h$；
完整第二位仍保 $\exp(34n t_3w^s)$。
本篇只关闭了“通过更巧的共同清分母，将整个 Norm3 返回免费塞回
原 $3C$”这一个具体接口。R750 的真实较小因子 Bockstein、
指定全局留数和整个同 $R$ 法向/第三块条件继续开放。

依赖：
[R756](R756-original-norm-three-map-and-complete-canonical-return.md)；
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)；
[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)。

新增公式均为原完整来源上的符号推导；没有新增数学运行或可重算输出。
