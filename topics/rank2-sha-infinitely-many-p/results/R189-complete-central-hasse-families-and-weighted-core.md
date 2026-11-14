# R189. 完整中央条件的 Hasse 族、逐带读取成本与准确 Smith 格

日期：2026-11-12。**状态：本文的条件行、全部次数的整数逆、
加权 core 读取和一层、两层 Smith 公式均已证明。** 这些公式
始终作用在同一个原有限次数源上。本文没有将输入 core 的覆盖
当成真实曲线前缀的可逆观测，也没有由条件行的数量推出新的
饱和 jet 预算。

## 1. 同一个原源与两个实际中央标量

固定惰性素数
$$
 p=4r-1\ge7,\qquad p\ne11,17,
 \qquad \mathcal O=\mathbb Z_p.
 \tag{1}
$$
沿用 R185、R188 的实际函数 $A=A_2,B$，以及整径向坐标
$$
 x=\Gamma^{17}-1,\qquad y=\zeta,
 \qquad A=(1+x)f(y),\quad B=(1+x)g(y).
 \tag{2}
$$
其中
$$
 f(y)=y+O(y^2),\qquad g(y)-f(y)=-22y^2+O(y^3),
 \qquad f,g\in\mathcal O[[y]].
$$
原源是 $E_D=\mathcal O[A,B]_{\le D}$，范数始终是这个原
多项式源的 Gauss 范数。

R185 给同一组实际权 $\omega_s=\lambda_{17,s}/\lambda_{17,1}$，
满足
$$
 \omega_1=1,\qquad
 v_p(\omega_s)=s-1+v_p((s-1)!).
 \tag{3}
$$
对 $N\ge1$，记
$$
 \begin{aligned}
 L_N&=N+v_p(N!),\\
 q_{A,N}&=\sum_{s=1}^N\omega_s[y^{rs}]f,
 &q_{B,N}&=\sum_{s=1}^N\omega_s[y^{rs}]g.
 \end{aligned}
 \tag{4}
$$
本篇使用的条件是原来的两个**完整**中央导数消失：
$$
 J_A'(0)=J_B'(0)=0.
 \tag{5}
$$
由 R185 的完整尾界，(5) 准确推出
$$
 q_{A,N},q_{B,N}\in p^{L_N}\mathcal O
 \quad\text{对每个 }N\ge1.
 \tag{6}
$$
这里没有将中央泛函传给乘积，也没有在原 $w$ 的高中央系数上
免费改用输出参数 $v=V(w)$。

## 2. 所有 D 的整径向逆与单条条件行

将 $P\in E_D$ 按原 $A,B$ 齐次次数分解，准确写成
$$
 \widetilde P(x,y)=\sum_{m=0}^D(1+x)^m g_m(y),
 \qquad \operatorname{ord}_y g_m\ge m.
 \tag{7}
$$
令 $n_{h,l}(P)=[x^hy^l]\widetilde P$。对 $l\ge1$，置
$M_l=\min(D,l)$，则
$$
 n_{h,l}=\sum_{m=1}^{M_l}\binom mh\,g_{m,l},
 \qquad g_{m,l}=[y^l]g_m.
$$
不论 $D$ 是否小于 $p$，都有准确整数逆
$$
 \boxed{\quad
 g_{1,l}
 =\sum_{h=0}^{M_l-1}(-1)^h(M_l-h)n_{h,l}.
 \quad}
 \tag{8}
$$
证明只用
$\sum_{h=0}^{M-1}(-1)^h(M-h)\binom mh=\mathbf1_{m=1}$，
$1\le m\le M$。对 $m\ge2$，补上系数为零的 $h=M$ 项后，
这是 $(1-1)^m$ 及其一阶导数；$m=1$ 时直接为一。
因此没有 $D!$ 的分母，也不需互异整数在模 $p$ 后仍互异。

定义原源上的整行
$$
 \boxed{\quad
 Z_{D,N}(P)=\sum_{s=1}^N\omega_s
   \sum_{h=0}^{\min(D,rs)-1}
          (-1)^h(\min(D,rs)-h)n_{h,rs}(P).
 \quad}
 \tag{9}
$$
若 $P$ 的原线性部分是 $c_AA+c_BB$，则 (8) 给
$$
 Z_{D,N}(P)=c_Aq_{A,N}+c_Bq_{B,N}.
 \tag{10}
$$
故 (5) 推出 $Z_{D,N}(E_D)\subset p^{L_N}\mathcal O$。
这是条件对原有限源的准确传递方式；它并不声称
$J_{P(A,B)}'(0)=0$。

## 3. 真实共同 core 的带号成本

记原 Cartan 展开为
$$
 \widetilde P(U,V)=\sum_{i,l\ge0}L_{i,l}(P)U^iV^l.
$$
对 $l=j+rt$，$0\le j<r$，若 $i+t>0$，定义
$$
 b(i,t)=\left\lfloor\frac{i+t-1}{p-1}\right\rfloor,
 \qquad
 \kappa(i,l)=t+b(i,t).
 \tag{11}
$$
若 $i=t=0$，令 $\kappa(0,j)=0$。后一类系数就是初始低行。

这是 R179 中该项的准确最低出现成本。事实上，置
$$
 \alpha=i+t-(p-1)b(i,t)\in\{1,\ldots,p-1\}.
$$
在最早允许的深度 $b(i,t)$，相应项准确是
$p^{t+b(i,t)}g_0^iL_{i,l}$，其中 $g_0$ 为单位。
对更深行它的系数仍是这个 $p$ 幂乘整系数。故一个精度为
$p^M$ 的加权输入 core 可定义为全部
$$
 p^{\kappa(i,l)}L_{i,l}(P)\pmod {p^M},
 \qquad \kappa(i,l)<M,
 \tag{12}
$$
另保上述低行。R179 的每条 $v$ 输出行模 $p^M$ 都是该数组的
整组合。

原 $w$ 输出仍须使用 R182 的 $\mathcal G,\mathcal V$。若
$k=r\{\alpha+(p-1)t_0\}+j$，其归一行是
$$
 \begin{aligned}
 \mathcal B^w_{t_0,\alpha,j}
 ={}&\sum_{b=0}^{t_0}\sum_{s=0}^{\alpha+(p-1)b}
 p^{b+s}[T^{t_0-b}]
 \mathcal G^{\alpha+(p-1)b-s}\mathcal V^{j+rs}
 L_{\alpha+(p-1)b-s,j+rs}\\
 &+\mathbf1_{\alpha=p-1}
   p^{-1}[T^{t_0+1}]\mathcal V^jL_{0,j}.
 \end{aligned}
 \tag{13}
$$
端点后一项不可删除；其系数因
$\mathcal V\in1+pT\mathcal O[[T]]$ 而整，也由低行读取。
因此 (12) 同样足以生成原 $w$ 行，但不把两种输出行混同。

这里的“输入 core”只是同一组有限原源泛函及其实际权重。
并未证明可以从曲线前缀的观测值反解 (12) 的每个分量。
特别，core 所有指标的最大总阶不意味着它包含该总阶以下的
整个 Taylor 单纯形。

### 3.1. 单行 Z 的足够精度

R179 的角色和截面性质给正反换参
$$
 U\in x\mathcal O[[x,y^r]],\qquad
 V\in y\mathcal O[[x,y^r]].
 \tag{14}
$$
故 $n_{h,rs}$ 只读取 $L_{i,rt}$，其中 $i\le h,t\le s$。
记 $M_s=\min(D,rs)$。第 $s$ 项需要的最大成本至多
$$
 s+\left\lfloor\frac{M_s+s-2}{p-1}\right\rfloor.
 \tag{15}
$$
乘上 (3) 后，若要计算 (9) 模 $p^{L_N}$，未除 $p$ 的输入
core 取精度
$$
 \boxed{\quad
 p^{L_N+1+\epsilon_{D,N}},\qquad
 \epsilon_{D,N}
 =\max_{1\le s\le N}
 \left\lfloor\frac{M_s-1+s_p(s-1)}{p-1}\right\rfloor
 \quad}
 \tag{16}
$$
就足够；$s_p(n)$ 表示 $n$ 的 $p$ 进数字和。
这是逐项精度计算：读取 $\omega_s L_{i,rt}$ 模 $p^{L_N}$
需要 $p^{\kappa}L_{i,rt}$ 到精度
$L_N+\kappa-v_p(\omega_s)$。利用 Legendre 公式，准确有
$$
 \left\lfloor\frac{M_s+s-2}{p-1}\right\rfloor
       -v_p((s-1)!)
 =\left\lfloor\frac{M_s-1+s_p(s-1)}{p-1}\right\rfloor.
 \tag{17}
$$
因此不能一般地把 (9) 称为原来同精度的 core 中的一条整行。
例如 $s=N$ 时仍可能有一个正的进位 $b(i,s)$，不能仅用
$v_p(\omega_s)\ge s-1$ 支付。

若只处理正次数原源的中央 $j=0$ 行，$L_{i,0}=0$ 对全部
$i$ 成立，故这些整行可先共同除以一次 $p$；此时 (16) 的
足够精度降低一位，即 $L_N+\epsilon_{D,N}$。
这一次除法不适用于后文混合余数的完整 Hasse 读取。

由数字和界，额外成本满足
$$
 \epsilon_{D,N}
 \le \left\lfloor\frac{D-1}{p-1}\right\rfloor
      +1+\lfloor\log_p N\rfloor.
 \tag{18}
$$
它随大 $N$ 只对数增长；这由真实阶乘权抵消进位得出，不是
从最高总阶的粗上界得出。

## 4. 原 Hasse 族及适配基的逐行成本

先在原 $A,B$ 基定义
$$
 Z^{a,b}_{D,N}(P)
 =Z_{D-a-b,N}
       (\partial_A^{[a]}\partial_B^{[b]}P),
 \qquad a+b\le D-1.
 \tag{19}
$$
原除幂偏导保整且不增 Gauss 范数，故 (5) 使全部 (19) 落在
$p^{L_N}\mathcal O$。这里没有假设各偏导也满足原曲线前缀。

为获得较细的输入成本，改用原整基
$$
 C=B-A,\qquad E_D=\mathcal O[A,C]_{\le D}.
 \tag{20}
$$
其正反变换整；两个中央零条件等价于 $A,C$ 的对应条件。
写 $T(y)=g/f-1$，则 $C=(1+x)f(y)T(y)$，其 $y$ 阶为二。
对原平移 $(A,C)\mapsto(A+u,C+v)$，准确有
$$
 \begin{aligned}
 y'&=T^{-1}\left(T(y)
        \frac{1+v/C}{1+u/A}\right),\\
 1+x'&=\frac{A+u}{f(y')}.
 \end{aligned}
 \tag{21}
$$
它在 $\mathcal O[[x,y]][1/y][[u,v]]$ 中逐阶有定义。

对多次数 $(a,b)\ne(0,0)$，整 Hasse 展开给
$$
 \begin{aligned}
 [u^av^b](y'-y)&\in y^{1-a-2b}\mathcal O[[x,y]],\\
 [u^av^b](x'-x)&\in y^{-a-2b}\mathcal O[[x,y]].
 \end{aligned}
 \tag{22}
$$
证明如下。送入 $T^{-1}$ 的增量的该多次数系数至少具有
$y$ 阶 $1-a-2b$。在 $T^{-1}$ 的整 Hasse 展开中，含 $q$
个正阶增量的项具有阶至少 $q-a-2b\ge1-a-2b$。
除以 $f(y)=y\cdot\text{整单位}$ 后，
$f(y')/f(y)-1$ 的同一多次数极点阶至多 $a+2b$；取整几何
逆及乘 $1+u/A$ 保留该界，得到第二式。没有普通偏导阶乘。

置 $h=a+b$。组合原 Hasse Taylor 展开后，若要读取偏导结果
的 $[x^Iy^J]$，原输入只须满足
$$
 \boxed{\quad i\le I+h,\qquad l\le J+a+2b.\quad}
 \tag{23}
$$
确实，替换的 $x$ 因子数至多 $h$；每个被替换的 $y$ 因子在
(22) 的第一式中补回一个 $y$，所以总 $y$ 次数至多降低
$a+2b$。所有系数均整。对实际原多项式，Laurent 负次项在
完整和中相消，结果就是原 Hasse 偏导的正幂整展开。

现在令
$$
 H_s=\min(D-h,rs),\qquad
 t_{a,b}=\left\lfloor\frac{a+2b}{r}\right\rfloor.
$$
(19) 的第 $s$ 项在适配基中只须读取原矩形
$$
 i\le H_s-1+h,\qquad l\le rs+a+2b.
 \tag{24}
$$
再经 (14)，Cartan 输入指标分别不增，且角向次数保持模 $r$
的余类。故由 (11)，最大成本至多
$$
 s+t_{a,b}
 +\left\lfloor
       \frac{H_s+h+s+t_{a,b}-2}{p-1}
   \right\rfloor.
 \tag{25}
$$
于是整个第 $(a,b)$ 条条件行模 $p^{L_N}$，可由未除 $p$ 的
实际输入 core 的精度
$$
 \boxed{\quad
 L_N+1+\epsilon_{a,b}(D,N),\qquad
 \epsilon_{a,b}(D,N)
 =t_{a,b}+\max_{1\le s\le N}
  \left\lfloor
   \frac{H_s+h+t_{a,b}-1+s_p(s-1)}{p-1}
  \right\rfloor
 \quad}
 \tag{26}
$$
读取。这里没有丢掉角向余数 $j\ne0$ 的项，也没有将那些行
共同除以 $p$。

若希望全部 $a+b\le D-1$ 共用一个安全精度，置
$$
 t_D=\left\lfloor\frac{2(D-1)}r\right\rfloor,
 \qquad
 \epsilon_{\rm all}(D,N)
 =t_D+\max_{1\le s\le N}
     \left\lfloor
       \frac{D+t_D-1+s_p(s-1)}{p-1}
     \right\rfloor.
 \tag{27}
$$
取 $L_N+1+\epsilon_{\rm all}$ 即足够。因为
$H_s+h=\min(D,rs+h)$ 随 $h$ 不减，且
$t_{a,b}\le\lfloor2h/r\rfloor$，最坏的矩形界在
$(a,b)=(0,D-1)$ 达到。这个安全读取成本是
$O(D/p+\log_p N)$；它仍是额外输入精度，不能当作已赚得的
前缀范数收益。

## 5. 全部 Hasse 行的原系数格：一个真实方向导数

本节用 (20)。记
$$
 q_N=(q_{A,N},q_{C,N}),\qquad
 q_{C,N}=q_{B,N}-q_{A,N}.
$$
若 $P=\sum c_{i,j}A^iC^j$，则准确有
$$
 \boxed{\quad
 Z_{D-a-b,N}(\partial_A^{[a]}\partial_C^{[b]}P)
 =(a+1)c_{a+1,b}q_{A,N}
  +(b+1)c_{a,b+1}q_{C,N}.
 \quad}
 \tag{28}
$$
因此全部条件行的输出向量，正是下述原多项式的系数向量：
$$
 \boxed{\quad
 \mathcal D_NP
 =q_{A,N}\partial_A P+q_{C,N}\partial_C P
 \in E_{D-1}.
 \quad}
 \tag{29}
$$
这解释了行族的准确依赖，而不是把约 $D^2$ 个输出槽当成任意
独立的算术条件。整数因子 $a+1,b+1$ 不能一概当作单位。

若 $q_N=0$，整个族准确为零。若 $q_N\ne0$，令
$$
 \kappa_N=\min(v_p(q_{A,N}),v_p(q_{C,N})).
$$
将 primitive 向量 $p^{-\kappa_N}q_N$ 用
$\operatorname{GL}_2(\mathcal O)$ 变成 $(1,0)$。相应原变量
线性换基及其逆，在每个有限次数多项式源上都是整同构。
在新变量 $X,Y$ 中，(29) 准确等价于
$$
 P\longmapsto p^{\kappa_N}\partial_XP.
 \tag{30}
$$
于是其特征零秩为 $D(D+1)/2$，核是
$\mathcal O[Y]_{\le D}$，非零 Smith 因子为
$$
 \boxed{\quad
 p^{\kappa_N+v_p(i)},\qquad
 1\le i\le D,\quad\text{每个重复 }D-i+1\text{ 次}.
 \quad}
 \tag{31}
$$
证明是 $X^iY^j\mapsto p^{\kappa_N}iX^{i-1}Y^j$，各输出
单项式只来自一个输入。按赋值排序即为 Smith 形式。
在完整双零条件下，$\kappa_N\ge L_N$；这并不另外决定
$q_N/p^{\kappa_N}$ 的方向。

## 6. 两个真实精度的联合族

对任意 $N,M\ge1$，令
$$
 Q_{N,M}=\begin{pmatrix}
 q_{A,N}&q_{C,N}\\ q_{A,M}&q_{C,M}
 \end{pmatrix}.
 \tag{32}
$$
联合 Hasse 输出准确等价于
$$
 P\longmapsto(\mathcal D_NP,\mathcal D_MP).
 \tag{33}
$$
若 (32) 的秩为二，令其 Smith 指数为
$\kappa_1\le\kappa_2$。在两个输出分量作整行操作，并在原
变量作整线性换基后，(33) 变成
$$
 P\longmapsto
 (p^{\kappa_1}\partial_XP,
  p^{\kappa_2}\partial_YP).
 \tag{34}
$$
每个非恒定单项式 $X^iY^j$ 的两个输出槽与其他输入的输出槽
均不相交。因此 (34) 的非零 Smith 因子准确为
$$
 \boxed{\quad
 p^{\min(\kappa_1+v_p(i),\,\kappa_2+v_p(j))},
 \qquad 1\le i+j\le D,\qquad v_p(0)=+\infty.
 \quad}
 \tag{35}
$$
核仅为常数，输出还有自由余核秩 $D(D-1)/2$。
若 (32) 的秩为一，则回到 (31) 及一个零输出分量；若其秩
为零，则全部联合行均为零。

这些是实际矩阵 (32) 的精确格结论。没有证明其秩一定为二，
更没有假定其行列式是单位。若分别使用 (6) 的不同目标格
$p^{L_N}E_{D-1}\oplus p^{L_M}E_{D-1}$，在 (34) 的整行操作
后须同时运输这个目标格；不能把两个不同精度自由混同。

还可以完全保留原轴数据，写成
$$
 v_s=([y^{rs}]f,[y^{rs}](g-f)),\qquad
 q_N=\sum_{s\le N}\omega_s v_s.
$$
例如相邻精度的实际行列式为
$$
 \det(q_N,q_{N+1})
 =\omega_{N+1}\sum_{s\le N}\omega_s
                   \det(v_s,v_{N+1}).
 \tag{36}
$$
在 (5) 下，收敛的完整和为零，故同一量又准确等于
$$
 \omega_{N+1}\sum_{s\ge N+2}\omega_s
                   \det(v_{N+1},v_s).
 \tag{37}
$$
这给一个可计算的实际两层独立性检验；它没有自行证明该
行列式非零。

**后续存在性输入。** [R190：原正 theta 截面的中央投影单射](R190-central-projection-of-square-theta-sections.md)
现已证明原两个轴向量 $v_s$ 张成 $\mathbb Q_p^2$。由于
$q_N-q_{N-1}=\omega_Nv_N$ 且每个 $\omega_N\ne0$，对每个
固定 $p$，确实存在有限 $N,M$ 使 (32) 秩为二；这在完整双零
条件下仍成立。对任意事先指定的 $N,M$，上述 Smith 结论仍按
(32) 的实际秩使用。R190 没有给出这些层数或行列式赋值的
统一上界，故不改变 (16)、(26) 的精度成本，也不自动给出
下面所需的前缀 Schur 增益。

## 7. 与完整曲线前缀联合时已经支付的范围

### 7.1. 完整早行已无条件支付的原线性块

下面给出一个必须在真实 Schur 补中保留的已有关系。它不使用
(5)。写
$$
 P=\sum c_{i,j}A^iC^j\in E_D,\qquad C=B-A,\qquad v_0=-22.
$$
若原 $w$ 前缀满足
$$
 [w^n]P(A(w),C(w))=0\quad(0\le n<k),\qquad k>r+2,
 \tag{38}
$$
则准确有
$$
 \boxed{\quad
 c_{1,0}=0,\qquad v_0c_{0,1}+c_{2,0}=0,\qquad
 c_{0,1},c_{2,0}\in p\mathcal O.
 \quad}
 \tag{39}
$$
源中不存在的系数按零解释，所以结论也包括 $D=1$。

**证明。** 原函数 $A=w+O(w^2)$、$C=v_0w^2+O(w^3)$。
前两个早行首先给 $c_{1,0}=0$，再给
$v_0c_{0,1}+c_{2,0}=0$，均为特征零准确等式。

还须核准 Cartan 方向的一阶混合项。R185 的 Teich 平均给
$u'(\eta)=1+O(\eta^{p-1})$；结合 R179 的完整截面规范，
在相关低次范围有
$$
 \Gamma=1+U+O(U^2,UV^r),\qquad
 \zeta=V+O(U^2V,UV^{r+1}).
 \tag{40}
$$
特别，$\zeta$ 没有 $UV$ 或 $UV^2$ 项；不能给
$L_{1,2}$ 人为加入一个未存在的角向一阶导数。
由各原齐次块的准确式 $\Gamma^{17m}g_m(\zeta)$，得到
$$
 L_{1,2}=17v_0c_{0,1}+34c_{2,0}
        =-17v_0c_{0,1}.
 \tag{41}
$$
同时沿原曲线，$U=u_0w^r+O(w^{pr})$、
$V=w+O(w^{R+1})$，且 $v_p(u_0)=-1$。
两种误差阶都大于 $r+2$，故
$$
 [w^{r+2}]P=L_{0,r+2}+u_0L_{1,2}.
 \tag{42}
$$
当 $r=2$、即 $p=7$ 时，本来还可能有 $u_0^2L_{2,0}$，
但原 $A,C$ 在 $V=0$ 上恒为零，故 $L_{2,0}=0$，(42) 仍
准确。$L_{0,r+2}$ 整，(38) 因而强迫 $L_{1,2}\in p\mathcal O$。
由于 $17v_0$ 是单位，(41) 和前述准确等式给 (39)。$\square$

所以在 (38) 范围内，整个原线性部分已经属于 $pE_1$，从而
$g_{1,rs}(P)\in p\mathcal O$ 对全部 $s$ 成立。这一步是原
**完整**前缀的无条件后果：$r\ge3$ 时关键的 $r+2$ 行属于
非中央余数 $j=2$，$p=7$ 时由已核的质量零端点给同一结论。
因此 R175 中以 $g_{1,r}\equiv0\pmod p$ 所支付的那一次
$p$，在此完整前缀范围不能再作为独立的条件净收益累计。
R175 的条件命题仍然成立；继续计算时应考察比 (39) 更深的
精度，而不是重复计入这项已有消去。

### 7.2. 尚需计算的联合商格

(9)、(19)、(28) 给的是同一原源上的实际条件行。
(16)、(26) 按每个带号与进位，给它们送入 R179/R182 共同
输入矩阵所需的足够精度；(31)、(35) 则给原系数格中的准确
依赖、核和所有整数乘子的损失。

若要从它们得到某个真实前缀 $S_{D,k}$ 的额外范数收益，还须
在此前全部准确曲线行的核上计算联合矩阵的 Schur 补。
本篇没有证明该 Schur 补非零，没有把一个偏导的前缀假定为
原 $P$ 的前缀，也没有把 (12) 的潜在系数数组当成已经可由
观测恢复的自由坐标。完整双零条件的使用正好是 (6)，不是
乘积上的新中央零性。

## 依赖

- [R185：完整整轴泛函、所有权的准确赋值和尾界](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
- [R188：原源的整检测、整左逆及 Hasse Laurent 运输](R188-original-source-detection-and-integral-hasse-transport.md)。
- [R179：全部深度共同 core 与整径向坐标](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R182：原 w 输出的完整中央行与端点](../notes/2026-11-12-actual-first-as-carry-and-complete-central-rows.md)。

本文只使用这些已经证明的实际等式和整数代数，没有以有限
素数计算替代全次数结论。
