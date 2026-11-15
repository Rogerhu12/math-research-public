# R738 — 真实平衡家族、分歧极点到独立值及合法原前缀替代

日期：2026-11-15。**状态：已证明。**

本篇把 R730 的指定极点量 $\Delta_F$ 转成一族**实际**分歧值的线性独立性。
先用原平衡整数 $c$ 的连续区间，随后给一个仍在同一 $\mathcal H_2$
中的二维显式家族。
每个来源的十九角和次数帽均保留，不免费添加乘子。

若这些指定值全落入同一个原镜轴核像，
它们产生一组独立的原首核。
原 $\mathcal W_D$ 的准确首项帽随后给更高 $t$ 前缀的真实核。
只有当原 cube 本来就是**整个**原首核空间中的最大前缀元素时，
才可把这件事用作极值矛盾；
本篇不假定所有原核都是 cube，也不假定原核一维。

## 1. 同一因子、真实商和可变的原平衡区间

保 R730/R731 的同一整来源
$$
P^{\rm fact}=qt^rF^3\in\mathcal W_D,\qquad q=d^{-C_D}Q,
$$
$$
p=6s-1>101,\quad
1\le\ell\le r<h,\quad
k=2h+r-s,\quad0\le k<\ell,
$$
$$
b=\deg_YF\ge2,\quad a_F=\deg_tF,\quad
e=\mathcal EF,\quad \mathcal E=Y\partial_Y,\quad
d=1+8t,\quad h_7=7+4t+16t^2.
\tag{1}
$$
$F,Q,C=(F=0),P=(0,1),\kappa=C^2,\chi=-K_XC$ 和全部十九角整格固定。
$e(P),Q(P)$ 为单位。
保原 $f_D<p$、实际因子提升，以及 R730 用于 $\Delta_F$ 的
固定角最高系数和 tame 条件。

令
$$
\delta_0=0\ (J),\qquad \delta_0=13\ (M),\qquad
T=s-r-\delta_0,\quad q_T=T-h .
$$
仍保
$$
\boxed{h>\kappa,\quad q_T>\kappa,\quad T\le2h.}
\tag{2}
$$
原完整目标均不改变；对 $M$ 仍只逆 $c_*U_0$，不逆 $m_{13}$。

原角平衡区间是
$$
\mu_{d,1}\le c\le u_{\rm cap}-\mu_{\infty,1}.
$$
以下固定一个**实际非空**整数区间
$$
\boxed{
1\le c_0\le c_1,\qquad
\mu_{d,1}\le c_0,\qquad
c_1\le u_{\rm cap}-\mu_{\infty,1}.
}
\tag{3}
$$
若没有这样的区间，本篇不宣称有非空家族。
可取 $c_0=\max(1,\mu_{d,1})$、
$c_1=u_{\rm cap}-\mu_{\infty,1}$。
原强素数条件下这些 $c$ 都小于 $p$；
使用 R727 切向式时 $8c,16c$ 仍为单位。

对每个 $c$，令
$$
U_c=d^c,\qquad
A_c=t^2Y^2(t-1)^2h_7^2d^{c-1}.
\tag{4}
$$
R727 的逐角证明对整个 (3) 同时成立：
$U_c,A_c\in\mathcal H_1$。

所有家族成员共用同一个单位来源
$$
\mathcal N_{\rm v}
=\left\{qt^r(\mathcal W_FH+F^2L):
H\in\mathcal H_2,\ L\in\mathcal L\right\},
\qquad
\mathcal W_FH=F\mathcal EH-2eH.
\tag{5}
$$
$\mathcal L=\ker\lambda$ 也固定：
$\lambda(F)=1$，而所有 $A_c$ 都有 $t^2$ 因子，故 $\lambda(A_c)=0$。
其整单位秩为 $R_{\rm v}=(5\kappa+3\chi)/2$，商映射记为 $\pi_{\rm v}$。
没有随 $c$ 更换一个不相容的 Schur 补。

在同一模 $p$ 角格中，R730 给
$$
K_{\rm mir}=
\ker\bigl(\mathcal H_2\to k[t]/t^T,\ 
B\mapsto B(t,\psi e^{2\eta_0})\bigr),
$$
$$
\boxed{
\ker(\operatorname{res}_Z|_{K_{\rm mir}})=kF^2,\qquad
Z=V(F,e),\quad \operatorname{length}Z=\kappa,
}
\tag{6}
$$
以及实际像的同构
$$
\boxed{
\frac{\operatorname{im}\overline{\mathsf M}_0(qt^rF\mathcal H_2)
+\operatorname{im}\overline{\mathsf M}_0(\mathcal N_{\rm v})}
{\operatorname{im}\overline{\mathsf M}_0(\mathcal N_{\rm v})}
\simeq
\frac{H^0(Z,\mathcal O_Z(2C))}
{\operatorname{res}_ZK_{\rm mir}}.
}
\tag{7}
$$

## 2. 原极点量不随平衡整数变化

在原正规曲线 $\widetilde C$ 上，仍用 R730 的固定六纤维
$$
S=\{0,1,-1/8,\text{$h_7$ 的两个根},\infty\}.
$$
定义
$$
\boxed{
\Delta_F=
\sum_{t(Q)\notin S}
\bigl(\operatorname{ord}_Qe-\operatorname{ord}_Q(U_cA_c)\bigr)_+.
}
\tag{8}
$$
在这些点 $d,t,t-1,h_7$ 为单位，且 $Y$ 没有极点，
所以 $\operatorname{ord}_Q(U_cA_c)=2\operatorname{ord}_QY$。
(8) 因而对所有 (3) 的 $c$ 相同。

R730 已付
$$
\boxed{
\Delta_F\ge
\max\left(0,\left\lceil\frac{h-4a_F-8b}{3}\right\rceil\right).
}
\tag{9}
$$
以下独立性定理使用真实 $\Delta_F$；
若只知道 (9)，可代入右边的整数下界。
不把一个未知的更大值直接当作已计算数据。

设 $\mathsf S\in\mathcal H_2$ 在整个 $Z$ 上为零。
因为 $Z$ 在 $C$ 上是 $e|_C$ 的 Cartier 零除子，
必有
$$
\mathsf S|_C=eL_C,\qquad L_C\in H^0(C,\mathcal O_C(C)).
\tag{10}
$$
所以 $\mathsf S/e$ 拉回正规曲线后，在固定角之外没有极点。
(10) 用的是包含固定角、重交点和非约化结构的完整 $Z$；
只在若干简单分歧点验值不够。

## 3. 连续 c 家族的真实独立性

由 (4)，准确有
$$
U_{c_0+i}A_{c_0+i}=d^{2i}U_{c_0}A_{c_0}.
\tag{11}
$$

**定理 1。** 若
$$
\boxed{
0\le L\le c_1-c_0,\qquad
2bL<\Delta_F,
}
\tag{12}
$$
则
$$
\boxed{
(U_{c_0+i}A_{c_0+i})|_Z,\qquad 0\le i\le L,
}
\tag{13}
$$
在 $H^0(Z,\mathcal O_Z(2C))$ 中线性独立。
等价的整数上界为
$$
\boxed{
L\le
\min\left(c_1-c_0,\left\lfloor\frac{\Delta_F-1}{2b}\right\rfloor\right).
}
\tag{14}
$$
若 $\Delta_F=0$，(14) 没有可用的非负 $L$。

**证明。** 非平凡线性关系由非零 $f(X)\in k[X]_{\le L}$ 给出
$$
f(d^2)U_{c_0}A_{c_0}|_Z=0.
$$
左侧仍属于同一 $\mathcal H_2$，因为它是 (13) 的真实线性组合。
由 (10)，$f(d^2)$ 的零必须抵消
$U_{c_0}A_{c_0}/e$ 在固定角之外的全部 $\Delta_F$ 极点，
包括其真实重数。

$t:\widetilde C\to\mathbf P^1$ 的次数是 $b$，
故 $d^2=(1+8t)^2$ 的次数是 $2b$。
非零 $f(d^2)$ 的全零除子次数为 $2b\deg f\le2bL$，
与 (12) 矛盾。证毕。

这里从极点数推出秩时使用了**同一个多项式关系**的零除子度数；
不是将 $\Delta_F$ 本身直接认成矩阵秩。

## 4. 一个仍在原 H2 的二维显式家族

定义固定有理函数
$$
\boxed{\mathfrak n=
\frac{t^2Y^2(t-1)^2h_7^2}{d}.}
\tag{15}
$$
于是 $U_cA_c=d^{2c}\mathfrak n$。
取整数 $I,J\ge0$，并要求
$$
\boxed{
c_0+I\le c_1,\qquad
J+1\le\min(b,2c_0),\qquad
2J<b.
}
\tag{16}
$$
考虑准确来源
$$
\boxed{
\mathsf S_{i,j}
=d^{2(c_0+i)}\mathfrak n^{j+1},
\qquad
0\le i\le I,\quad0\le j\le J.
}
\tag{17}
$$

**引理 1（全部实际帽）。** (17) 的每一项都属于同一整 $\mathcal H_2$。

**证明。** 令 $c=c_0+i$、$m=j+1$。
(16) 使 $m\le2c$，所以
$$
d^{2c}\mathfrak n^m
=t^{2m}Y^{2m}(t-1)^{2m}h_7^{2m}d^{2c-m}
$$
是原多项式呈示。
它的 $Y$ 次数为 $2m\le2b$，
相应 $t$ 次数为 $2c+7m$，满足
$$
2c+7m\le2u_{\rm cap}+8m.
$$
所以原 ambient 帽准确成立。

$U_c^2=d^{2c}$ 已属于 $\mathcal H_2$。
R727 对乘子 (15) 的全部十九个中间角值是
$$
\begin{array}{c|c|c}
\text{原链}&\text{序号}&v(\mathfrak n)\\ \hline
0,\ h_7\text{ 两根的 }Y=\infty&1\le j'\le4&2j'-2\\
1\text{ 的 }Y=\infty&1\le j'\le3&2j'-2\\
d=0,\ Y=0&j'=1,2&2-j'\\
t=\infty,\ Z=0&j'=1,2&j'+2 .
\end{array}
\tag{18}
$$
它们全非负，任意实际幂 $m$ 都不降低原角条件。
严格纤维上的新分母已由 $m\le2c$ 消掉，
$Y=\infty$ 和基底无穷远的帽则已由前两项次数检查支付。
故全部原角和次数同时保持。证毕。

特别
$$
\boxed{qt^rF\mathsf S_{i,j}\in\mathcal W_D}
\tag{19}
$$
由原 $qt^r\mathcal H_3$ 的整返回成立，零新增 charge。
当 $j=0$ 时，这是原 R727 的指定 $c$ 家族。
$j>0$ 时只声称 (19) 的真实 $F\mathcal H_2$ 来源，
不把它冒称原切向两个剩余列的另一种免费写法。

### 完整极帽与独立性

在 $\widetilde C$ 上，
$$
\deg(d^2)_\infty=2b,\qquad
\deg(\mathfrak n)_\infty\le2a_F+8b.
\tag{20}
$$
第二式来自 $Y^2$ 的全极次数 $2a_F$，
以及 $t^2(t-1)^2h_7^2/d$ 在基底的一份 $d=0$ 极和七份无穷远极。
重叠若发生只会降低上界，未将不同极点假作不交。
也可用同一实际函数的更小准确极次数替代右边。

**定理 2。** 若 (16) 成立，且
$$
\boxed{2bI+(2a_F+8b)J<\Delta_F,}
\tag{21}
$$
则 (17) 的全部 $(I+1)(J+1)$ 个 $Z$ 值线性独立。

**证明。** 任一线性组合为
$$
d^{2c_0}\mathfrak n\, f(d^2,\mathfrak n),\qquad
\deg_Xf\le I,\quad\deg_Vf\le J.
\tag{22}
$$
非零多项式 $f$ 在 $C$ 上不变成零：
代入 $\mathfrak n=R(t)Y^2$ 并清固定 $t$ 分母后，
它的 $Y$ 次数至多 $2J<b$。
$F$ 是同一个不可约 $Y$ 次数 $b$ 的最小关系；
而非零系数 $f_j(d^2)$ 不能因非恒定的 $t$ 而消失。
故 (22) 中的乘子是非零有理函数。

其极除子逐点被
$$
I(d^2)_\infty+J(\mathfrak n)_\infty
$$
控制，度数至多 (21) 左侧。
若 (22) 在 $Z$ 上为零，(10) 再次要求该乘子的零抵消
基准 $d^{2c_0}\mathfrak n/e$ 的全部 $\Delta_F$ 极点，
与 (21) 矛盾。证毕。

本证明用的是一个共同极除子，
没有把二维次数三角形中各单项式的单独极度上界
错误地相加成一个更小的统一上界。

如果 $a_F\le C_ab+O(1)$、
$\Delta_F\ge C_\Delta b^2+O(b)$，
且可选 $c_0\ge\eta_0b+O(1)$、
$c_1-c_0\ge\eta_1b+O(1)$，其中这些常数为正，
可取固定 $\alpha,\beta>0$ 满足
$$
\alpha<\eta_1,\qquad
\beta<\min(1/2,2\eta_0),\qquad
2\alpha+(2C_a+8)\beta<C_\Delta.
$$
则 $I=\lfloor\alpha b\rfloor$、$J=\lfloor\beta b\rfloor$
最终满足全部条件，得到
$$
\boxed{(I+1)(J+1)=\alpha\beta b^2+O(b)}
\tag{23}
$$
个已付的真实独立 $Z$ 值。
平衡区间有线性余宽是这里的明确前提，不自动由 (9) 推出。

## 5. 全部吸收时，得到真正的原核子空间

令 $\{\mathsf S_\lambda\}_{\lambda=1}^N$
为定理1或定理2的独立来源家族，定义
$$
z_\lambda=\pi_{\rm v}\overline{\mathsf M}_0
(qt^rF\mathsf S_\lambda).
$$
若所有 $z_\lambda=0$，(6)、(7) 给唯一类
$$
[B_\lambda]\in K_{\rm mir}/kF^2,\qquad
B_\lambda|_Z=\mathsf S_\lambda|_Z.
$$
这些类线性独立，因而
$$
\boxed{
P^{\rm fact},\quad qt^rFB_\lambda\ (1\le\lambda\le N)
}
\tag{24}
$$
是同一个原 $\ker\overline{\mathsf M}_0$ 中的 $N+1$ 个独立元素，
全部具有至少 $t^r$ 的**来源前缀**。

(24) 的独立性先由 $Z$ 值确定所有 $B_\lambda$ 系数，
再由 $F^2$ 确定 cube 系数。
这不是某个多项式呈示中的重复零列。

更一般地，记
$$
V_Z=\operatorname{span}\{\mathsf S_\lambda|_Z\}.
$$
家族在真实单位商中的准确像秩是
$$
\boxed{
N-\dim(V_Z\cap\operatorname{res}_ZK_{\rm mir}).
}
\tag{25}
$$
可以与 R550 已付的 $\dim\ker\alpha_\eta$ / Clifford 上界比较。
若未严格超过该上界，(23) 本身不证明指定类退出镜轴像。
本篇不重登 R550 的一般秩界，也不把 $\Omega(b^2)$ 的记号当成足够大的常数。

## 6. 原 t 前缀的准确分次容量

这里的 $v_t(P)$ 是把 $P$ 看成 $Y$ 多项式、系数在 $k(t)$ 时
各系数 $t$ 阶的最小值；
原 $d$ 分母在 $t=0$ 为单位。
它不同于把 $Y$ 代入 $g(t)$ 之后的接触阶。

令
$$
\mathscr K=\ker\overline{\mathsf M}_0,\qquad
\mathscr K^{\ge n}=\mathscr K\cap t^n k[[t]][Y].
\tag{26}
$$
整个原来源仍准确为
$$
\mathcal W_D=
\bigoplus_{j=0}^D Y^jq_j(t)\mathcal O[t]_{\le e_{j+1}},
$$
$$
A_j=\lfloor(j+1)/4\rfloor,\quad
B_j=\lfloor(j+1)/3\rfloor,\quad
C_j=\lfloor j/2\rfloor,
$$
$$
f_j=\lfloor9j/2\rfloor+4,\quad
e_{j+1}=f_j-3A_j-B_j+C_j.
$$
置原最高来源前缀
$$
b_j^{\rm src}=A_j+e_{j+1},\qquad
I_D(n)=\{0\le j\le D:A_j\le n\le b_j^{\rm src}\},
$$
$$
\boxed{g_D(n)=\max(0,|I_D(n)|-2).}
\tag{27}
$$

**引理 2。** 若
$$
\boxed{\ell\le n<s-\delta_0,}
\tag{28}
$$
则
$$
\boxed{
\dim_k(\mathscr K^{\ge n}/\mathscr K^{\ge n+1})
\le g_D(n)\le4n+1.
}
\tag{29}
$$

**证明。** 同一来源的 $t^n$ 首系数空间
准确由 $Y^j,\ j\in I_D(n)$ 张成：
$q_j/t^{A_j}$ 在原点为单位，
而来源多项式的次数帽准确给 (27) 的上下界。
这一步不放宽任何系数帽。

对 $P=t^nP_n(Y)+O(t^{n+1})\in\mathscr K^{\ge n}$，
原 $g(0)=1$ 和完整 Gaussian 的前两行给
$$
P_n(1)=0,\qquad(\mathcal EP_n)(1)=0.
$$
由 $f_D<p$，所有 $0\le j\le D$ 模 $p$ 互异；
这两个真实行在 (27) 首系数空间上的秩为
$\min(2,|I_D(n)|)$。
故得第一界。
$n\ge\ell$ 时第三行已经由公共前缀截掉，
没有另添未付的第三个条件。

对 $M$，(28) 正保证 $n+13<s$，
前两行在乘 $w^{13}$ 后仍真实可读。
这里已合法逆掉 $c_*U_0$，
并保 $t/w$ 的首单位和原两条十三行 carry；
$n\ge s-13$ 时不再使用这个双零论证。

最后 $A_j\le n$ 给 $j\le4n+2$，
所以 $|I_D(n)|\le4n+3$，得粗界 $4n+1$。
实际分次核未必实现所有这些首项，
因此第一式是明确的上界，不是声称任意双零首项可延成原核。证毕。

## 7. 更高前缀的合法替代，以及何时才有极值矛盾

取整数 $v\ge1$，要求
$$
r+v\le s-\delta_0.
$$
由 (29)，
$$
\boxed{
\dim(\mathscr K^{\ge r}/\mathscr K^{\ge r+v})
\le G_D(r,v):=\sum_{n=r}^{r+v-1}g_D(n)
\le v(4r+2v-1).
}
\tag{30}
$$

**定理 3。** 对第5节的 $N$ 个真实独立输入，若
$$
\boxed{N+1>G_D(r,v),}
\tag{31}
$$
则以下二者至少有一个成立：

- 某个 $z_\lambda$ 在同一个真实单位商中非零，
  因而该指定实际家族确实提供单位列；
- 原完整 $\mathscr K$ 中存在非零元素，来源前缀至少为 $r+v$。

**证明。** 若全部 $z_\lambda=0$，
(24) 在 $\mathscr K^{\ge r}$ 中给 $N+1$ 维子空间。
(30)、(31) 迫其与 $\mathscr K^{\ge r+v}$ 有非零交。
这个向量是 (24) 中实际来源的线性组合，
不是从环境 jet 中新补的列。证毕。

其模 $p$ 来源可以在原同前缀整格中提升：
逐个原 $Y^jq_j$ 分量，使用原次数帽内的
$t^{\max(0,r+v-A_j)}$ 倍多项式。
这保持全部角和帽。
这种选择只保证原首核和真实来源前缀；
它与原线性组合提升之间可能相差 $p\mathcal W_D$，
后续必须把这项计入同一个 $R$。
没有自动得到模 $p^2$ 或 $p^3$ 提升。

### 全 K1 中的合法最大值

因为 $\mathcal W_D$ 是有限来源，
非零来源前缀有上界 $\max_jb_j^{\rm src}$。
当 $\mathscr K\ne0$ 时，
$$
r_{\max}=\max\{v_t(P):0\ne P\in\mathscr K\}
$$
因此有严格的定义。

只有在所用**这个原 cube** 恰满足 $r=r_{\max}$ 时，
定理3的第二项才是矛盾。
这时已能用 $v=1$：
$$
\boxed{
N+1>g_D(r)
\quad\Longrightarrow\quad
\text{至少一个指定 }z_\lambda\ne0.
}
\tag{32}
$$
连续 $c$ 家族的一个直接充分条件是
$$
\boxed{c_1-c_0\ge4r,\qquad \Delta_F>8br.}
\tag{33}
$$
因为可取 $L=4r$，从而 $N=L+1=4r+1$，
并且 $N+1>4r+1\ge g_D(r)$。

(32)/(33) 没有假定 $\mathscr K$ 一维。
但此前原因子化选择并未给出 $r=r_{\max}$，
所以不能把这个极值条件补写成已有事实。
在所有 cube 中最大化 $r$ 也不够：
定理3产生的新核一般是 $qt^rFB$，不必仍为 cube。
同样不能为继续迭代而假定每一条新核都有相同立方分解。

更精确地，在合法 $r=r_{\max}$ 下，
(25) 的实际家族像秩至少为
$$
\boxed{\max(0,N+1-g_D(r)).}
\tag{34}
$$
因为任何 $d$ 维被吸收的 $Z$ 子空间都会连同原 cube
给 $d+1$ 维的 $\mathscr K^{\ge r}$；
其首项映射此时单射，受 (29) 控制。

## 8. 仍保原实际 forcing 的全范围

本篇的线性和二维家族全部来自同一 $\mathcal H_2$，
对应列全部已经通过原十九角返回同一个 $\mathcal W_D$。
$\Delta_F$ 只经非零有理函数的准确零、极度数
转成 (13)/(17) 的独立性，没有被当成自由的 Smith 因子数。

得到单位列时，仍须与 R722 的切向截源、
原其余全部列和指定 forcing 作同一个整 Schur 消元。
得到更高前缀核时，也只得到真实原首核；
它的因子类型、原 Bockstein、完整高尾均须重新按其实际来源读取。

原 $P_{134}/U_0$、两条十三行 carry、完整 $\xi/V_1$、
低行右逆及同一个 $P_2=P^{\rm fact}+pR$、第三精度 $d_2/G_2$
全部保留。
没有新增任何中央零，也没有由 (23) 或合法极值的条件推论
宣称固定曲线的无穷素数主目标已完成。

依赖：
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R545](R545-angular-balanced-connection-and-full-physical-unit-block.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R637](R637-original-short-three-block-square-root-surjectivity.md)；
[R727](R727-original-balanced-sections-and-single-residual-column-in-vertical-unit-quotient.md)；
[R730](R730-specified-ramification-class-linear-contact-bound-and-actual-mirror-kernel.md)；
[R731](R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)。
