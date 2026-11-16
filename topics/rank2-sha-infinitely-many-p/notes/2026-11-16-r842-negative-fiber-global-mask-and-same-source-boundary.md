# 原 R842 负纤维的全局同源 mask 与水平补偿

日期：2026-11-16。**状态：以下同一个原 $G$ 上的全局微分、全部有限纤维残数和真实无穷远成本已证明。指定 $[b_0]$ 在 $\mathscr W_T$ 上的零或非零仍未判定。**

本注接
[负纤维 Jacobian 商](2026-11-16-r842-negative-fiber-jacobian-quotient.md)、
[实际完整边界](2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)
和 [第一层延拓](2026-11-16-r842-first-layer-surjectivity-and-actual-restricted-class.md)。
将已经付清的负水平行换成一个真正全局的亚纯微分，
准确消掉同底纤维的其余有限点，并把代价留在同一原正水平和底无穷远。
不增来源列，不改原 $q$，不把这个亚纯代表称为允许的全局 $\omega_i$。

## 1. 从实际有限行唯一构造一个次数小于 b 的乘子

沿用原已清固定角分母的多项式方程 $F(t,Y)$、
原 $\mathcal H_3$ 多项式代表 $G$，以及
$$
R=q\,t^rG,\qquad q=Y\widetilde q,\qquad
b=\deg_YF<p,\qquad
W_s=t^{r+1-s}(1-t)^{3s},\qquad c_s=\frac{3(-1)^s}{17}.
$$
这里只处理原 $r=2$ 分类中确实存在的非固定负水平点
$Q=(t_Q,0)$；$q(t,0)\ne0$ 的另一类没有这些移动点。
所有局部数据先在原剩余域 $k_Q$ 上读取。

记
$$
F_Q(Y)=F(t_Q,Y)=Y^\ell f_Q(Y),\qquad f_Q(0)\ne0,
$$
$$
u_Q=\min(\ell,\operatorname{ord}_YF_t(t_Q,Y)),\quad
v_Q=\min(\ell,\operatorname{ord}_Y\widetilde q(t_Q,Y)),\quad
d_Q=\max(0,\ell-u_Q-v_Q).
\tag{1}
$$
$F_Q$ 不恒零，因为原整曲线不是底纤维。
前注给同一个完整分支 trace $S_Q$，并证明
$$
\mathfrak b_Q(G)
=-c_st_Q^rW_s(t_Q)\operatorname{CT}_Y
\left[\widetilde q(t_Q,Y)G(t_Q,Y)(1-D_Y)^2S_Q(Y)\right],
\quad D_Y=Y\,d/dY .
\tag{2}
$$
这里已经包括奇点的全部 conductor 分支。

若 $d_Q=0$，原行为零，以下乘子定义为零。
若 $d_Q>0$，前注的精确阶数及 $b<p$ 保证
$$
Y^{d_Q-1}\widetilde q(t_Q,Y)(1-D_Y)^2S_Q(Y)
\in k_Q[[Y]]^\times.
$$
因此有唯一原多项式
$$
\boxed{
R_Q(Y)=
\left[
Y^{d_Q-1}\widetilde q(t_Q,Y)(1-D_Y)^2S_Q(Y)
\right]_{<d_Q},\qquad \deg R_Q<d_Q .
}
\tag{3}
$$
截断只保次数 $0,\ldots,d_Q-1$。
它保留原 $\widetilde q$ 和 $S_Q$ 的全部被读取系数，
不是选择一条具有相同首项的行。

置
$$
\boxed{
N_Q(Y)=Y^{\ell-d_Q}f_Q(Y)R_Q(Y).
}
\tag{4}
$$
于是
$$
\boxed{
\deg_YN_Q\le\deg_YF_Q-1\le b-1,\qquad
\frac{N_Q(Y)}{F_Q(Y)}=\frac{R_Q(Y)}{Y^{d_Q}}.
}
\tag{5}
$$
(2) 准确成为
$$
\mathfrak b_Q(G)
=-c_st_Q^rW_s(t_Q)
\operatorname{Res}_{Y=0}
\frac{G(t_Q,Y)R_Q(Y)}{Y^{d_Q}}\,dY .
\tag{6}
$$
所以 (4) 是该已付实际行的确定 mask。
不是对 $\mathscr W_T$ 的值作插值，也不要求其评价满射。

## 2. 同一原曲线上的全局微分与完整有限纤维

采用原平面伴随微分
$$
\Omega_{\rm pl}=\frac{dY}{F_t}=-\frac{dt}{F_Y}.
$$
它是原仿射平面曲线的对偶化生成元。
两个显示式只作函数域恒等使用；
在 $F_t=0$、$F_Y=0$ 或奇点不将分母冒充单位。
定义
$$
\boxed{
\Theta_Q(G)=
c_st_Q^rW_s(t_Q)\,
G(t,Y)\frac{N_Q(Y)}{t-t_Q}\,\Omega_{\rm pl}.
}
\tag{7}
$$
这是同一个 $G$ 的线性全局亚纯微分。

**完整纤维恒等式。** 对底纤维 $t=t_Q$ 的全部有限 $Y$ 点，
包括非约化点和全部正规化分支，有
$$
\boxed{
\sum_{\substack{t=t_Q\\Y\ {\rm finite}}}
\operatorname{Res}\Theta_Q(G)=\mathfrak b_Q(G).
}
\tag{8}
$$
其中除 $Q=(t_Q,0)$ 外的每个原点的分支残数和均为零。
其余有限底点、有限 $Y$ 处也有相同的零和性质。

证明使用完整有序 Grothendieck 留数。
写 $\tau=t-t_Q$，
$$
F(t,Y)=F_Q(Y)+\tau A_Q(t,Y),\qquad
A_Q(t,Y)=\frac{F(t,Y)-F_Q(Y)}{t-t_Q}\in k_Q[t,Y].
\tag{9}
$$
将有序方程 $(F,\tau)$ 交换为 $(\tau,F)$，
再以单位三角变换改为 $(\tau,F_Q)$，
准确得到
$$
\sum_{\substack{t=t_Q\\Y\ {\rm finite}}}
\operatorname{Res}
\frac{G N_Q}{\tau}\frac{dY}{F_t}
=
-\sum_{F_Q(\alpha)=0}
\operatorname{Res}_{Y=\alpha}
\frac{G(t_Q,Y)N_Q(Y)}{F_Q(Y)}\,dY.
\tag{10}
$$
(5) 把右侧的全部 $\alpha\ne0$ 项消掉，
在 $\alpha=0$ 留下 (6) 的负号。
该完全交转换不要求 $F_t(Q)$ 为单位，
也不先把奇点拆成可自由赋值的支。

还可在原曲线上直接核查所有额外有限点：
由 (9)，
$$
\boxed{
\frac{N_Q(Y)}{t-t_Q}
=-\,A_Q(t,Y)\frac{R_Q(Y)}{Y^{d_Q}}
\quad\text{于 }C.
}
\tag{11}
$$
在同底纤维的 $Y\ne0$ 点，右式真正正则；
在其它底纤维，(7) 的系数真正正则。
因此相应微分在原平面曲线上是对偶化正则，
其全部 conductor 分支残数和为零。
在固定吹起点上，这句话只消整个原点的分支和，
不把每个例外点或每条正规化支分别赋零。

原 $P=(0,1)$ 不在目标底纤维，故
$$
\operatorname{Res}_P\Theta_Q(G)=0
\tag{12}
$$
对全部原 $G$ 成立，不需先附加高前缀。

## 3. 所有移动负水平只需同一个次数至多二的底分母

对原全部非固定负水平闭点取剩余域迹，定义
$$
\Theta_-(G)=\sum_Q\operatorname{Tr}_{k_Q/k}\Theta_Q(G).
\tag{13}
$$
因为原 $F(t,0)=\lambda d^cH(t)$ 且 $\deg H\le2$，
这些 $t_Q$ 的平方自由多项式 $H_{\rm mov}(t)$ 的次数至多二。
(13) 准确可写成
$$
\boxed{
\Theta_-(G)=
c_s\,G(t,Y)\frac{B_-(t,Y)}{H_{\rm mov}(t)}\,\Omega_{\rm pl},
\quad
\deg_tB_-<\deg H_{\rm mov}\le2,\quad
\deg_YB_-\le b-1 .
}
\tag{14}
$$
系数来自 (3)、(4) 和原值 $t_Q^rW_s(t_Q)$ 的同一有限域迹。
若没有非零负行，取 $B_-=0$。
这里的平方自由底分母不删去原二重纤维：
其全部非约化厚度仍在 (1)–(6) 的 $F_Q$ 和 $R_Q$ 中。

(14) 只是精确的全局部分分式合并。
没有将 $W_s(t_Q)$ 换成一个近似相位，
也没有把它在目标底域之外的 Frobenius 资料删掉。

## 4. 原正水平及无穷远的全部成本

### 4.1 所有有限底点的正水平

在原 $Y=\infty$ 图令
$$
x=Y^{-1},\quad f=x^bF(t,x^{-1}),\quad
\widehat G=x^{3b}G(t,x^{-1}),
$$
$$
\widehat A_Q=x^bA_Q(t,x^{-1}),\qquad
\widehat R_Q=x^{d_Q-1}R_Q(x^{-1}).
$$
这些系数在有限底点真正正则；
实际次数不足的列保留额外 $x$ 零。
利用 (11) 而非仅给 $(t-t_Q)^{-1}$ 作阶数上界，得到
$$
\boxed{
\Theta_Q(G)=
c_st_Q^rW_s(t_Q)\,
x^{-3b-1}\widehat G\,\widehat A_Q\,\widehat R_Q\,
\frac{dx}{f_t}.
}
\tag{15}
$$
所以乘子相对于原对偶化生成元 $dx/f_t$ 的极帽至多 $3b+1$。
即使目标底纤维本身也经过 $Y=\infty$，(15) 仍完全相同：
(11) 已准确取消了可能额外的 $t-t_Q$ 极，
不能再把它计入而忘掉 $\deg F_Q$ 的对应下降。

在光滑 $f_t$ 单位点，(15) 给普通 $x$ 参数中的这个极帽。
在奇点，它只给原对偶化系数的帽；
正规化上 $dx/f_t$ 的 conductor 极全部保留，
不能把 $3b+1$ 当成忽略 conductor 后的绝对分支极阶。

对第 $j$ 个有限负链原图
$$
t-t_i=x^jz,\quad Y=x^{-1},\quad
F=x^{V_j-b}f_j,\quad G=x^{3V_j-3b}G_j,
$$
同一式准确为
$$
\boxed{
\Theta_Q(G)=
c_st_Q^rW_s(t_Q)\,
x^{\,2V_j-3b+j-1}
G_j\,\widehat A_Q(t_i+x^jz,x)\,\widehat R_Q(x)\,
\frac{dx}{(f_j)_z}.
}
\tag{16}
$$
此式保四、四、四、三步链的每个真实累计重数。
在 $(f_j)_z=0$ 处使用未约去的对偶化微分及全部分支；
其它交叠图由同一个有理微分运输。

在有限正链 $Y=x,\ t-t_i=x^jz$，
改用 (7) 的原多项式 $N_Q$，则
$$
\Theta_Q(G)=
c_st_Q^rW_s(t_Q)\,
\frac{x^{2V_j+j}G_j N_Q(x)}
     {t_i+x^jz-t_Q}\,
\frac{dx}{(f_j)_z}.
\tag{17}
$$
目标 $t_Q$ 非固定，故这里的底分母为单位。
这与第2节完整有限对偶化正则性一致，
而不是在固定角另设一个可选边界值。

### 4.2 原底无穷远及其两步链

保持原 $\mathbb F_4$ 坐标
$$
T=1/t,\quad Z=t^4Y,\quad
F=T^{-u_F}f_\infty(T,Z),\quad
G=T^{-3u_F}G_\infty(T,Z).
$$
$u_F$ 是原同一个线束框的纤维参数。
没有用清分母后的裸 $\deg_tF$ 替换它。
由固定 $Y$ 的原偏导和曲线关系直接得
$$
\Omega_{\rm pl}=T^{u_F+2}\frac{dT}{(f_\infty)_Z}.
$$
所以
$$
\boxed{
\Theta_Q(G)=
c_st_Q^rW_s(t_Q)\,
T^{3-2u_F}
\frac{G_\infty\,N_Q(T^4Z)}{1-t_QT}
\frac{dT}{(f_\infty)_Z}.
}
\tag{18}
$$
若 $N_Q\ne0$，(3) 为单位首项，故
$\operatorname{ord}_YN_Q=\ell-d_Q$；
(18) 还保其实际额外 $T^{4(\ell-d_Q)}$ 零。
这里所有指数都独立于 $s$，
但系数仍是原 $p$ 相关的真实系数。

在严格底无穷远与另一水平的交图，
再取 $w=Z^{-1}$、
$\overline f=w^bf_\infty(T,w^{-1})$、
$\overline G=w^{3b}G_\infty(T,w^{-1})$ 及
$\widehat N_Q=w^{b-1}N_Q(T^4/w)$。
后者是真正正则的两变量多项式。
(18) 同时给
$$
\Theta_Q(G)=
-c_st_Q^rW_s(t_Q)\,
T^{3-2u_F}w^{-3b-1}
\frac{\overline G\,\widehat N_Q}{1-t_QT}
\frac{dT}{\overline f_w}.
\tag{18a}
$$
两条边界相交处不能只保其中一个指数。

在其第 $j=1,2$ 原正链中，
$T=x^jz,\ Z=x,\ f_\infty=x^{V_j}f_j,\
G_\infty=x^{3V_j}G_j$，完整式为
$$
\boxed{
\Theta_Q(G)=
-c_st_Q^rW_s(t_Q)\,
x^{\,2V_j+j(4-2u_F)}z^{\,3-2u_F}
\frac{G_j\,N_Q(x^{4j+1}z^4)}{1-t_Qx^jz}
\frac{dx}{(f_j)_z}.
}
\tag{19}
$$
两个坐标的零极、交点和单位分母均显示在内。
(15)–(19) 不删严格底无穷远纤维，也不省去任一 conductor 条件。

因此本全局化真正留下的是原正水平和底无穷远上的明确补偿。
它不是一个全纯全局延拓：
例如在正水平，若要把 $\Theta_Q/G$ 乘 $e^2$ 放进
$\mathcal Q_T=H^0(\omega_CN^{-1}(TP))$，
仍必须消掉 (15) 的实际极。
本文没有证明这些极消失，也不允许用局部可逆性任选一个全局 $\nu$。

## 5. 原受限类中的精确合并

取真正 $V_0\in\mathscr W_T$，
其唯一伴随 $V_1\in\mathscr V_T$ 满足
$D_3V_0=V_1|_Z$。
按 R836 取同一个原 $G_V\in\mathcal H_3$ 同时实现
$G_V|_C=V_0,\ (\mathcal EG_V)|_C=V_1$。
全部实现之差为 $F^2\mathcal H_1$。

在第一层注的任一真正 $\omega_1\in\mathcal Q_T$ 下，
$V_1$ 的 $T$ 阶零与 $\omega_1$ 的至多 $T$ 阶极相消，
且 $e(P)$ 为单位。因此准确有
$$
\boxed{
[b_0](V_0)=
\mathfrak G_F(qt^rG_V).
}
\tag{20}
$$
这里不存在一个可另调的 $\omega_1$ 原点残数。

令 $\mathcal D_R$ 为实际边界注的同一全局代表，置
$$
\widehat{\mathcal D}_R=\mathcal D_R-\Theta_-(G_V).
\tag{21}
$$
(8)、(10) 证明其所有移动负水平残数和严格为零；
(12) 保原点残数不变；
其在原非固定仿射分歧概形 $Z^\circ$ 上仍读取同一
$\mathfrak G_F(R)$。
全部其余有限点的新增总残数为零。
故 (20) 的真实全局行成为
$$
\boxed{
[b_0](V_0)
=-\operatorname{Res}_P\mathcal D_R
-\sum_{\substack{\text{全部原边界}\\
                 \text{除 }P\text{ 与移动负水平}}}
 \operatorname{Res}\widehat{\mathcal D}_R .
}
\tag{22}
$$
和式保原有限底纤维、正水平、十九角、底无穷远及全部 conductor 分支。
各支只按原几何合并一次。
已付 $t=1$ 额外预算门和有限 $h_7$ 消去可照原范围使用；
不把它们扩成所有固定边界的零。

原点尾也没有被 (21) 消掉。
确切分部式中 $W_s'$ 两项相消，给
$$
-\!d(W_sF_t/e)+(W_s'F_t+W_sF_{tt})dt/e
=
W_s\left(\frac{F_t\,de}{e^2}-\frac{F_{tY}}e\,dY\right).
$$
于是当 $T=s-r-13$ 时，
$$
\operatorname{ord}_P\mathcal D_R\ge r-12.
\tag{23}
$$
$r\ge12$ 才自动无原点残数；$r\le11$ 时仍保实际
$0,\ldots,11-r$ 系数，特别原 $r=2$ 保十个系数。
它们来自同一个 $G_V$，不取自由 normal 行。

最后，$G_V$ 改为 $G_V+F^2L$ 时，
$G_V|_C$ 与 $(\mathcal EG_V)|_C$ 均不变。
所以 $\mathcal D_R$、$\Theta_-(G_V)$ 和 (22) 本身都不变，
不只是最终数值偶然相同。

(22) 将负水平的局部未知准确并入同源正水平/无穷远补偿；
没有判定整个行在 $\mathscr W_T$ 或更小三长核上为零、非零，
也没有把它等同一条已经杀原完整 $M$ 的左行。
同一 $q$、原 $P_{134}/U_0$、全部十三 carry、物理前缀和下一位继续保持。

全文只用原符号恒等式、完全交留数转换与真框运输；没有数学程序执行或新增可重算输出。
