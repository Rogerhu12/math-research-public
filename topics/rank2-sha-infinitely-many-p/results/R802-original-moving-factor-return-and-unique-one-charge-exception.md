# R802 — 移动常数因子的真实小成本返回、唯一一 charge 例外与原接触核

日期：2026-11-15。**状态：以下返回、唯一例外、最小性及有条件接触核结论已证明。**

R797 的六十四格不能全部以同一个次数预算返回 $\mathcal W_b$。
其中唯一最大角组合是 $A_*=h_7^2d$、$(m_h,\delta_d,\delta_\infty)=(3,1,1)$：
它没有任何非零的同 charge 有理标量返回，但有实际
$$
t h_7Y\,G\in\overline{\mathcal W}_{b+1}.
$$
其余六十三个 mask 的整个来源格均有一个明确 $L(t)$ 使
$LG\in\overline{\mathcal W}_b$。
特别 R797 的所有移动 $H$（$\deg H=1$ 或2）都属于后者。

在对应真实交数门 $h+1>B_{b+\epsilon}.C$ 下，完整 factor 接触核恰为原 $kG$；
允许移动 $H$ 的全部低系数不会增加这个核。
这里 $\epsilon=0$ 或1准确记录上述返回成本。
本篇不把这个条件门当成已经由强接触自动满足，
也不把首核一维当成首 Bockstein 非零。

## 1. 保留的原来源与完整 factor 格

保持 R797 的原
$$
q=Y\widetilde q,\quad
P^{\rm fact}=qt^2F^3\in\overline{\mathcal W}_D,\quad
F_0=\lambda d^cH,\quad
G=\frac{F}{\lambda d^c},\quad G_0=H,
\tag{1}
$$
$$
d=1+8t,\qquad h_7=16t^2+4t+7,\qquad
H\text{ monic},\quad(H,d)=1,\quad z=\deg H\le2,
$$
以及原 $s=2h+2$、$p=6s-1$ 的长度约定，和 $F$ primitive 不可约、$b=\deg_YF\ge3$、
$F_Y(0,1)\ne0$、原 $p>101,f_D<p$。
特别 $H(0)$ 仍可为零。

固定 R797 的一个 mask
$$
A_*=(t-1)^i d^j h_7^k,\qquad
a=i+j+2k\le6-3z.
\tag{2}
$$
令 $\mathcal V_{A,z}$ 为 R797(12) 的整个线性格，
但把常数 charge 扩写为所有 $\mathbf F_p[t]_{\le z}$：
$$
G'=H'(t)+\sum_{n=1}^bY^nr_n p_n(t),\qquad
\deg H'\le z,
\tag{3}
$$
其中所有 $r_n$ 和 $p_n$ 的原帽都保持 R797。
真正 $G$ 属于此格，且其 $H$ 具有准确次数 $z$。

该格上的 Gauss 下界为
$$
v_0(G')\ge-3,\quad v_h(G')\ge-M_h,\quad
v_1(G')\ge-M_1,\quad v_d(G')\ge-D_d,\quad
v_\infty(G')\ge-D_\infty,
$$
$$
M_h=\min\!\left(b,\left\lfloor\frac{4k+1}{3}\right\rfloor\right),
\quad M_1=\min(b,i),\quad
D_d=\left\lfloor\frac{2j+1}{3}\right\rfloor,\quad
D_\infty=\left\lfloor\frac{13-2a}{3}\right\rfloor.
\tag{4}
$$
它只允许 $d$ 极，且 $\deg_Y\le b$。
(3) 是真正有限自由来源包络；没有把不同 $Y$ 幂的高尾独立化。

## 2. 六十三格的完整同次数返回

定义
$$
\alpha=\left\lfloor\frac k2\right\rfloor,\qquad
\beta=\left\lfloor\frac{i+1}{3}\right\rfloor,\qquad
\gamma=\left\lfloor\frac{j+2}{3}\right\rfloor,
$$
$$
\boxed{L_{i,j,k}=t\,h_7^\alpha(t-1)^\beta d^\gamma.}
\tag{5}
$$
在 (2) 的范围中，$k\le3,i,j\le6$，所以
$$
4\alpha-M_h\ge-2,\qquad
3\beta-M_1\ge-1,\qquad
2\gamma-D_d\ge0.
\tag{6}
$$
零角另有 $4-3=1\ge-2$。这些不等式同时处理两 h7 角、t=1 和 d，且不会产生其他有限极。

剩下的无穷远条件准确为
$$
2\deg L+D_\infty\le8.
\tag{7}
$$
下表逐一列出 $a\le6$ 时的最大可能次数；它只需对非负
$i+j+2k=a$ 的整数进行符号分类。

| $a$ | $\max\deg L$ | $D_\infty$ | $\max(2\deg L+D_\infty)$ |
|---:|---:|---:|---:|
| 0 | 1 | 4 | 6 |
| 1 | 2 | 3 | 7 |
| 2 | 2 | 3 | 7 |
| 3 | 3 | 2 | 8 |
| 4 | 3 | 1 | 7 |
| 5 | 4 | 1 | 9 |
| 6 | 4 | 0 | 8 |

第 $a=5$ 行唯一达到次数4的组合为
$$
(i,j,k)=(0,1,2),\qquad A_*=h_7^2d.
\tag{8}
$$
其余 $a=5$ 组合的次数至多3。

为核这张表，可先看 $k\ge2$：其 h7 部分已用次数成本4；
要使 $\deg L\ge4$，在剩余 mask 成本至多2中须增加一个
$d$ 因子（最小 $j=1$）或两个 $(t-1)$ 因子（最小 $i=2$）。
当 $a=5$ 时只有第一种，正是 (8)。
若 $k\le1$，则 $\alpha=0$；
$\beta+\gamma\ge3$ 的最小 mask 成本为
$(i,j)=(2,4)$ 或 $(5,1)$，都等于6。
这也证明 $a\le6$ 时次数不会超过4；各其余上界直接由 (5) 取得。

由 R491 的全部 Gauss 双向识别，得到

**定理 1。** 除 (8) 外，R797 每个 mask 的整个 factor 格均有
$$
\boxed{
L_{i,j,k}\mathcal V_{A,z}\subseteq\overline{\mathcal W}_b.}
\tag{9}
$$
这是原 $\mathcal W_b$ 的全部系数帽，不仅是总次数估计。
$L$ 在原点恰为一阶零；其余固定因子在原点为单位。因此对原物理低轴，
$$
\operatorname{ord}_t(LG)(t,\rho)
=\operatorname{ord}_tG(t,\rho)+1=h+1.
\tag{10}
$$
特别所有 $z=1,2$ 格均满足 (9)，因为它们的 mask 成本至多3。

## 3. 唯一例外的准确适用范围与最小新增 charge

在 (8) 中，
$$
M_h=3,\quad M_1=0,\quad D_d=D_\infty=1,\quad z=0,\quad H=1.
\tag{11}
$$
若真正 $G$ 的实际 $m_h\le2$，可删 $L$ 的 h7 因子；
若 $\delta_d=0$，可删 $d$；
若 $\delta_\infty=0$，原 $L=th_7d$ 已满足 (7)。
所以只有同时
$$
\boxed{m_h=3,\qquad m_1=0,\qquad
\delta_d=\delta_\infty=1}
\tag{12}
$$
仍无已付同次数返回。若使用较小实际格，应按这些准确亏损重新取格；不能在较大的 (11) 包络上直接删因子。

**定理 2。** 对满足 (12) 的实际 primitive $G$，
不存在非零 $L_0(t)\in k(t)$ 使
$L_0G\in\overline{\mathcal W}_b$。
另一方面，整个 (11) 格都有
$$
\boxed{th_7Y\,\mathcal V_{A,0}
\subseteq\overline{\mathcal W}_{b+1}.}
\tag{13}
$$
所以在有理标量或多项式乘子返回这一类别内，所需新增 $Y$ charge 的最小值准确为1。

**证明。** 若存在 $L_0$，primitivity 排除其在 $d$ 以外的任何有限极：
在每个这样的点，某个 $F_n$ 为单位，而 $G$ 在那里无分母。
d 角条件又迫 $\operatorname{ord}_dL_0\ge1$，故 $L_0$ 是多项式。
零角、两个 h7 角及 d 角分别迫
$$
\operatorname{ord}_0L_0\ge1,\qquad
\operatorname{ord}_{h_7}L_0\ge1,\qquad
\operatorname{ord}_dL_0\ge1.
$$
因此 $\deg L_0\ge4$。
无穷远的准确 $\delta_\infty=1$ 却要求
$2\deg L_0+1\le8$，矛盾。

对 $M=th_7Y$，全部原赋值直接为
$$
\begin{array}{c|ccccc}
&0&h_7&1&d&\infty\\ \hline
v(MG')\text{ 的下界}&
4-1-3=0&
4-1-3=0&
-1&
1-1=0&
-6+9-1=2 .
\end{array}
$$
均满足原 $\mathcal W$ 下界，且 $\deg_Y(MG')\le b+1$。
这付 (13)。$Y=\rho(0)=1$，所以它同样只将接触 $h$ 改成 $h+1$。
一个非零多项式乘子若不增加 $Y$ 次数，必为 $t$ 的多项式；
前段已经排除。$\square$

本定理不排除更专门的非乘法来源操作。
它也不允许把 (13) 的 $b+1$ 改回 $b$：
后面的交数必须准确使用 $B_{b+1}.C$。

## 4. 移动常数 H 下的完整接触核

记原十九角曲面上完整来源除子为 $B_B$，于是
$\overline{\mathcal W}_B=H^0(X,\mathcal O_X(B_B))$，
保持 R495/R795 的原框架。
对 (9) 取 $B=b,M=L$；
对 (13) 取 $B=b+1,M=th_7Y$。

令真正不可约 $F$ 的严格变换为 $C$，原点
$P=(0,1)$ 为其光滑点，分支为 $Y=\psi(t)$。
原接触精确为 $G(t,\rho)=t^hu(t)$、$u(0)\ne0$，故
$\psi-\rho$ 恰有阶 $h$。考虑整个 (3) 格的实际映射
$$
\operatorname{ev}_{<h}:\mathcal V_{A,z}\longrightarrow k[t]/(t^h),
\qquad G'\longmapsto G'(t,\rho).
\tag{14}
$$

**定理 3。** 若满足真实交数门
$$
\boxed{h+1>B_B.C,}
\tag{15}
$$
则
$$
\boxed{\ker\operatorname{ev}_{<h}=kG.}
\tag{16}
$$
这里包含全部 $H'$ 低系数；没有假定 $H(0)$ 为单位。
可用的充分门为 $h+1>B_B^2$，但只在原 $B_B$ 的 nef 性和
$B_B-C$ 有效已经由真实返回支付时使用。

**证明。** 若 $G'\in\ker\operatorname{ev}_{<h}$，
$\psi-\rho\in t^h k[[t]]$ 及局部系数正则给
$G'(t,\psi)\in t^h k[[t]]$。
因此原来源截面 $MG'\in H^0(B_B)$ 限于 C 后，在 P 至少消失 $h+1$ 阶。
如果该限制非零，其零除子次数为 $B_B.C$，与 (15) 矛盾。
这只用积分曲线上非零线丛截面的次数及 P 光滑，不需要 C 在别处光滑，
也不调用特征零的消失定理。

故 $MG'$ 在 C 恒零。F 不整除固定乘子 M：
F 不可约且 $\deg_YF\ge3$，而 M 仅有 $t,h_7,t-1,d,Y$ 这些固定因子。
清去 d 分母后，所以 $F\mid G'$。
由于 $\deg_YG'\le b=\deg_YF$，存在 $f(t)\in k(t)$ 满足
$$
G'=f(t)G.
$$
对每个 $d$ 以外的有限点，F primitive 保证某个系数为单位，
而 $G'$ 无该处极，故 f 无该处极。
在 d 点，用 $G_0=H$、$H(d)\ne0$ 及 $G'_0\in k[t]$，同样得 f 无极。
所以 f 是多项式。最后
$$
G'_0=fH,\qquad \deg G'_0\le z=\deg H
$$
迫 f 为常数。真正 G 本来就在 (14) 的核内，得到 (16)。$\square$

对于充分门，$MG$ 是原非零截面，其除子包含 C，
故 $B_B-C$ 有效；在原已付 nef 范围，
$B_B.(B_B-C)\ge0$ 给 $B_B.C\le B_B^2$。
特别例外必须使用 $B=b+1$，没有把新增 charge 隐入这个推论。

## 5. 整 prefix、实际第 h 行与没有被证明的一次 p

令 $\mathcal V_{\mathcal O}$ 为 (3) 的显示整自由格。
固定因子按原 Hensel 提升，原 $\rho$ 的所读行均在同一 $\mathcal O$ 中。
(3) 的系数帽没有改变，且 $h+1<s$，所以这里是原实际低轴的整矩阵。

设 $N=\operatorname{rank}\mathcal V_{\mathcal O}$。
用常数 charge 的 $t^z$ 系数定义一个整线性函数 $\lambda_z$，
并令 $\mathcal V^0=\ker\lambda_z$。
真正 G 的该系数为1，所以 (16) 给
$$
\operatorname{ev}_{<h}|_{\overline{\mathcal V^0}}
\text{ 单射},\qquad
\operatorname{rank}_k\operatorname{ev}_{<h}=N-1.
\tag{17}
$$
因此完整 $H'$ 低系数和所有正 charge 原列在此补空间上有单位最大子式。
再加真正第 h 行，因 $[t^h]G(t,\rho)=u(0)\ne0$，得到
$$
\boxed{\operatorname{ev}_{\le h}
\text{ 在整个 }\overline{\mathcal V}_{A,z}\text{ 上单射，且有单位 }N\text{ 阶子式}.}
\tag{18}
$$

对 (17) 的整单位块作原行列消元，只剩一个真实列余向量
$$
\Delta\in p\mathcal O^{\,h-N+1}.
$$
原 factor 首 Bockstein 是这个余向量 $\Delta/p$ 的类。
(18) 说明下一行补回单位；它不证明 $\Delta/p$ 已经非零，
也不证明原前缀的最后 Smith 指数恰为1。
$\Delta$ 可能有更高 p 阶，甚至在这个截断中为零。
这与 R795 的精度边界相同，但现在已完整支付移动 H 和唯一新增 charge。

## 6. 与原完整 forcing 的界线

(9)、(13) 是实际来源返回，不新增任何固定曲线的中央零。
即使 (16) 成立，原 $\mu J(P^{\rm fact})/p$ 的指定类仍须在
完整 $\mathcal W_D$ 和同一个 $R$ 上判定。
本篇没有把 factor 接触核的单位补空间识别成原 M 的全部右核，
也没有丢掉第三 $w^{13}$ 行、两条十三行 carry 或 p³ 的高尾。

对于 R797 的 b=3，公开 producer 的有限接触结论仍独立按真实全部十九角判定。
本篇不依赖该运行是否给出无解，也不把 (15) 视为由
$h\ge\kappa+14$ 自动推出。

下一实际接口仍是：在满足原全帽的强接触因子及完整首次修正中，
把指定 factor Bockstein 和 R790/R797 的整段 normal/carry 共同代入同一原左像。
主目标仍未完成。

依赖：
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R795](R795-original-factor-contact-one-dimensional-kernel-and-unit-next-row.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)。
