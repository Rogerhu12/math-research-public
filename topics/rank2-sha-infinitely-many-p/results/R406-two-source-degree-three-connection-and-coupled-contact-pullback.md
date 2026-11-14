# R406：加入真实 T72 后的次数三连接、整像与双接触的准确分离

日期：2026-11-14。**状态：已证明。** 在 R403 的真实扩源中，旧次数二算子遗漏了 $H_{38}$ 的固定角零。本篇给出一个原归一化中的次数三乘子，支付整个扩源的导子操作及 $\zeta$ 连接；其物理成本仍只有一次行移。给出明确的来源饱和范围，并将两种不同 Gaussian charge 的真正 double-Euler 拉回同时写出。原 $P_2,\lambda_2$、两条接触尾、十三行和全 $U_0$ 均保留；不将这些整像身份替代 R403 的两个中央基准条件。

## 1. 同一个扩源及其十七个独立部分

采用 R403 的共同 $E_1$、$p=6s-1>83$，
记
$$
h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad
f=(1+8t)a/7,\quad \alpha=36/17,
$$
$$
V=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
$$
用 $\mathscr R$ 表示相对径向变量，其物理值为
$\rho=\Theta^{17}(1+8t)$。
实际新来源为 $T=\Theta^{36}fV$。
它在原来源函数域中准确满足
$$
\boxed{T^{17}(1+8t)^{19}
=\mathscr R^{36}(aV/7)^{17}.}
\tag{1}
$$
右边的 $\mathscr R$ 赋值是三十六，与十七互素；
因此 $1,T,\ldots,T^{16}$ 在 $K(\mathscr R,t)$ 上线性独立，
特征为好 $p\ne17$ 时同样成立。
这是原指数三十六与十七的实际区别，未倒置 $T$ 获得新来源。

沿 R352 取整个旧相对 canonical 模
$$
\mathcal V_n=\mathscr R^nq_n(t)R_0[t]_{\le e_{n+1}},\qquad
q_n=\frac{(t h_7)^{a_n}(t-1)^{b_n}}{(1+8t)^{c_n}},
$$
$$
a_n=\lfloor(n+1)/4\rfloor,\quad
b_n=\lfloor(n+1)/3\rfloor,\quad c_n=\lfloor n/2\rfloor,
$$
$$
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2,
\qquad
\deg q_n+e_{n+1}=f_n=\lfloor9n/2\rfloor+4.
\tag{2}
$$
系数环取原 $R_0$ 再倒置十七；在共同好惰性范围这是单位扩张。
对 $0\le J\le16$，定义实际有限来源
$$
\mathcal W_{D,J}=
 \bigoplus_{n=0}^{D}\ \bigoplus_{j=0}^{J}\mathcal V_nT^j .
\tag{3}
$$
乘回原 $G_0$ 后，每一列都是旧原导子的一列乘真实 $T^j$。
(1) 保证 (3) 是直接和；旧整基与同一个赋值证明也保证其模 $p$ 独立。
这里不主张它已经是新代数的整个归一化或整个导子。

将保持 $\mathscr R$ 不动的 $t\partial_t$ 延伸到 (1)。
准确有
$$
t\partial_tT=L_T(t)T,
$$
$$
\boxed{
L_T=1+\frac{t}{t-1}+\frac{t h_7'}{h_7}
 +\frac{tV'}{V}-\frac{152t}{17(1+8t)} .
}
\tag{4}
$$
最后一项等于 $8(1-\alpha)t/(1+8t)$。
总相对 Euler 为
$$
\boxed{\mathcal E(\mathscr R^nq_nP\,T^j)
=(n+\alpha j)\mathscr R^nq_nP\,T^j.}
\tag{5}
$$

## 2. 原次数三乘子与完整整闭合

定义
$$
\boxed{
W_3=\mathscr R^3\,t(t-1)^2h_7^2V,\qquad
\mathcal Q_3=W_3\,t\partial_t .
}
\tag{6}
$$
$W_3$ 确属于旧原归一化的次数三部分：
其标准基本分式为
$$
\mathscr R^3\,\frac{t(t-1)h_7}{1+8t},
\qquad d_3=10,
$$
而商为 $(t-1)(1+8t)h_7V$，次数准确为十。
所以它乘整个旧原导子保持原来源，不是新增的外部有理乘子。

**定理1。** 对全部 $n\ge0$、$0\le j\le16$，
$$
\boxed{
W_3\mathcal V_nT^j\subset\mathcal V_{n+3}T^j,\qquad
\mathcal Q_3\mathcal V_nT^j\subset\mathcal V_{n+3}T^j.
}
\tag{7}
$$
$\mathcal Q_3$ 是原整来源中的算子，包含 (4) 的全部项。

**证明。** 记
$$
\Delta_a=a_{n+3}-a_n\in\{0,1\},\quad
b_{n+3}-b_n=1,\quad
\Delta_c=c_{n+3}-c_n\in\{1,2\}.
$$
对原基 $\Phi_{n,k,j}=\mathscr R^nq_nt^kT^j$，
$\mathcal Q_3\Phi_{n,k,j}$ 等于
$\mathscr R^{n+3}q_{n+3}T^j$ 乘下面完整多项式：
$$
\begin{aligned}
B_{n,k,j}={}&
 t^{k+1-\Delta_a}(t-1)h_7^{2-\Delta_a}
 (1+8t)^{\Delta_c}V\\
&\quad\cdot\left[
 k+a_n+j+
 \frac{(a_n+j)t h_7'}{h_7}
 +\frac{(b_n+j)t}{t-1}
 +\frac{8(-c_n+j(1-\alpha))t}{1+8t}
 +\frac{jtV'}V\right].
\end{aligned}
\tag{8}
$$
所有显示的分母都有真正因子支付。
特别 $V$ 不被约成原点单位后遗忘；它清掉新来源的全部固定角极。

多项式次数至多 $k+12-3\Delta_a+\Delta_c$。
另一方面由 (2)，
$$
e_{n+4}-e_{n+1}=11-3\Delta_a+2\Delta_c,
$$
所以剩余度数为 $\Delta_c-1\ge0$。
这同时支付全部有限零极和无穷处界。
只乘 $W_3$ 的公式是 (8) 去掉方括号，也满足同一界。$\square$

## 3. 完整核及来源像的饱和范围

**定理2。** 特征零下
$$
\ker(\mathcal Q_3|\mathcal W_{D,J})
=R_0\cdot1\oplus R_0\cdot\mathscr R
\quad(D\ge1).
\tag{9}
$$
对好 $p$，若
$$
\boxed{
p>\max\{17f_D+151J,\ 17c_D+19J\},
}
\tag{10}
$$
则 (9) 在模 $p$ 后仍是准确核。因此
$$
\boxed{
\mathcal W_{D,J}/\langle1,\mathscr R\rangle
\xrightarrow{\ \mathcal Q_3\ }\mathcal W_{D+3,J}
\quad\text{的像是 }p\text{-饱和的。}
}
\tag{11}
$$
这里的 $1,\mathscr R$ 是相对列；乘回 $G_0$ 后不是原点原子或新增质量一来源。

**证明。** 在固定 $\mathscr R$ 的函数域上以 $\Theta$ 为变量，则
$$
t=\frac{\mathscr R\Theta^{-17}-1}{8},\qquad
T=\frac{\mathscr R}{7}\Theta^{19}a(t)V(t).
\tag{12}
$$
任一 $\mathscr R^nq_nP\,T^j$ 是
$K(\mathscr R)[\Theta,\Theta^{-1}]$ 中的 Laurent 多项式。
其指数范围准确包含于
$$
-17f_n-151j\ \le\ \deg_{\Theta,\rm monomial}\
 \le17c_n+19j.
\tag{13}
$$
因为 $aV$ 的次数为十，(13) 直接由 (2)、(12) 得出。
该部分的所有指数模十七同余于 $2j$；
$0\le j\le16$ 时这些剩余类不同。

特征零的 $t$ 导数核是固定 $\mathscr R$ 的常数。
在模 $p$ 后，(10) 保证每一个非零 Laurent 指数的绝对值小于 $p$，
故导数为零也只允许指数零。
只有 $j=0$ 能出现该剩余类。
回到独立变量 $\mathscr R,t$，各 $n$ 的 $q_nP$ 必须分别为常数；
$n\ge2$ 的 $t=1$ 强迫零排除该常数，而 $q_0=q_1=1$。
因此准确得到 (9)。
(8) 是整矩阵，其特征零和模 $p$ 秩相同；
原来源、目标都有上述真实整基，故得到 (11)。$\square$

(11) 是原来源映射的饱和，不是评价矩阵已经没有深 Smith 因子的断言。

## 4. 同一个物理三块的完整连接及一次行移

保持 R352/R403 的
$$
w^s=p\epsilon,\quad\epsilon^3=0,\quad
\mathscr R_{\rm phys}=g(w)e_2(a_p\epsilon),\quad
L=2s+\ell,\quad M=m_{13}J .
$$
新 $T$ 按 R403 的实际 charge $\alpha$ 评价。
共同目标和所有系数使用已经付出的第三精度模型，不换原源。

令
$$
\mathsf E_w=w\partial_w,\quad\mathsf E_w\epsilon=s\epsilon,\qquad
\nu=\frac{(1-t)^{-1/2}}{h(t)},\qquad
\Lambda=\mathsf E_w\log g+s a_p\epsilon.
$$
完整链式法则给
$$
\boxed{
M_+\mathcal Q_3
=B_3(\mathsf E_w-13)M_-
-B_3\Lambda M_-\mathcal E,
\qquad B_3=W_{3,\rm phys}\nu .
}
\tag{14}
$$
其中 $\mathcal E$ 是 (5) 的实际混合权，而不是只读 $n$。
因为 $t=-w+\cdots$、$V(0)=1$，
$$
\boxed{B_3=-49w\cdot U_3(w,\epsilon),\qquad U_3(0)=1.}
\tag{15}
$$
$U_3$ 是完整目标中的整单位。
因此来源增加 relative charge 三，目标只增加一行。

取完整长度 $T_0=2s+\ell+13$，并要求 $T_0+1<3s$。
在基 $e_r=w^r/p^{\lfloor r/s\rfloor}$ 上乘 $w$，
恰只在 $r=s-1,2s-1$ 两处带一因子 $p$。
所以各精度 Smith 核长度的新增损失仍在零与二之间。
这是额外成本；原 $G_0$、charge 四十、十三行和旧至多二十六边界成本没有被删除。

若 $M_{\rm orig}=U_0M$，则 (14) 中第一算子准确换为
$$
\mathsf E_w-13-\frac{\mathsf E_wU_0}{U_0}.
\tag{16}
$$
整个公共 theta、$P_{134}$ 和 $G_0$ 的连接都在此式中。

## 5. 新扩源的真实 zeta 像包含

仍用 R351 的整物理恒等式
$$
\nu\mathsf E_w=-\frac{x}{6y}D_z,\qquad
\nu\Lambda=c(t)-\frac{17x\zeta}{3y},
\quad c(t)=-\frac{17+112t}{3(1+8t)}.
\tag{17}
$$
两式作用于整个算子；不能单独使用 $\nu$ 的 $Z_p$ 分母。

置
$$
A_3=W_3c(t),\qquad
\mathcal D_{\zeta,3}=\mathcal Q_3+A_3\mathcal E,\qquad
Z_3^{\rm conn}=W_{3,\rm phys}\frac{x\zeta}{y}.
\tag{18}
$$
这里 $Z_3^{\rm conn}$ 是连接乘子，**不是** R382 的第三坐标。
$A_3$ 也是真正的 $\mathcal N_3$ 元素：
相对 §2 的标准基本分式，其商为
$$
-\frac13(t-1)h_7V(17+112t),
$$
次数十。因此 (18) 是全部 (3) 上的原来源操作。

(14)、(17) 准确给
$$
\boxed{
M_+\mathcal D_{\zeta,3}
=B_3(\mathsf E_w-13)M_-
+\frac{17}{3}Z_3^{\rm conn}M_-\mathcal E .
}
\tag{19}
$$
连接乘子整，因
$$
Z_3^{\rm conn}=\frac3{17}(A_{3,\rm phys}-B_3\Lambda).
$$
因此对任意真正 $P_r\in K_r(M_-)$，
$$
\boxed{
Z_3^{\rm conn}M_-(\mathcal EP_r)
\in\operatorname{im}(M_+\bmod p^r).
}
\tag{20}
$$
一个准确来源代表是 $(3/17)\mathcal D_{\zeta,3}P_r$。
对满足 $\lambda_rM_+\equiv0\bmod p^r$ 的整左核，
其配对因而为零模 $p^r$。
乘回 $U_0$ 后，按 (16) 保全部额外项，(20) 仍成立。

(20) 不要求 $\mathcal EP_r$ 自身在核中。
它给的是新扩源上的真实像约束；没有把 $\zeta$ 或 $Z_3^{\rm conn}$
当作可任意新增的来源。

对应的完整 Serre 式也可直接使用。
令 $\Omega_{\lambda,n+3,j}$ 为带原
$p^{\lfloor r/s\rfloor}$ 权、$w^{13}$、$\rho^{n+3}T^j$ 的真实拉回对偶，
并记 $\omega=\Omega/dt$、$W_3=\mathscr R^3 w_3(t)$。
对同一 $F=q_nP$，
$$
\boxed{\begin{aligned}
\langle\lambda,M_+\mathcal D_{\zeta,3}
                 (\mathscr R^nFT^j)\rangle
=\operatorname{Res}_{t=0}F\big[
&-d(tw_3\omega)
+jw_3L_T\Omega\\
&+(n+\alpha j)w_3c(t)\Omega\big].
\end{aligned}}
\tag{21}
$$
其中 $jL_T$ 是必须保留的新项。
$\lambda$ 必须是实际整左核提升，不能用任意模 $p$ 函数代替。

## 6. S 与 T 对同一双接触的真实拉回

本节取 $J\le15$，以便乘 $T$ 后仍在上述十七部分内。
取同一个 $P_2\in K_2(M_-)$，
其 R338 两条真实接触尾记为 $D_1,D_2$。
乘以 $S$、$T$ 是实际来源乘法，且各自物理首阶都是 $w$，
故在完整多一行目标中 $SP_2,TP_2$ 都仍在模 $p^2$ 核。
这是矩阵乘法的自然性，不用中央零传播。

写模 $p$ 的完整乘子
$$
S_{\rm phys}=v_S(w)e_2(a_p\epsilon),\qquad
T_{\rm phys}=v_T(w)e_2(\alpha a_p\epsilon),
$$
$$
v_S=w+\cdots,\qquad v_T=w+\cdots,\qquad
h=v_T/v_S\in1+w k[[w]].
\tag{22}
$$
$v_S,v_T$ 是各自真正 regularized 前缀；
所需次数低于 $s$，故其商使用已经给出的整单位，不产生新来源。

两乘积都可放入 $\mathcal W_{D+1,J+1}$ 的同一多一行目标；
若同时使用 (20)，再完整保留其次数三和一行成本。
在这个同一实际大左核 $\lambda_2$ 下，
令 $K=s-14$，$d_r=6r(6r+1)$，并保实际第三块长度 $\ell_+$。
定义同一个有限对偶的两个耦合向量
$$
\begin{aligned}
q_r={1\over d_r}\bigg\{
 &\sum_{j=r}^{K}\lambda_{1,j+13}[w^{j-r}]D_1
 +\sum_{j=r}^{\ell_+-1}\lambda_{2,j+13}[w^{j-r}]D_2\bigg\},\\
r_r={1\over d_r}
 &\sum_{j=r}^{\ell_+-1}\lambda_{2,j+13}[w^{j-r}]D_1,
\qquad1\le r\le K .
\end{aligned}
\tag{23}
$$
空和为零，全部 $+13$、末行 $\ell_+-1$ 和原左核提升都保留。
$q,r$ 由同一个 $P_2,\lambda_2$ 给出，不能把它们自由化。

用 R372 的实际 double-Euler 算子
$$
\mathcal T(v)=\mathcal L^{-1}\operatorname{pp}(v\mathcal L\,\cdot),
\qquad
\mathcal L=\mathsf E(\mathsf E-1),\quad
\mathsf E=6w\partial_w ,
$$
作用于 $\sum_{n=1}^Kq_nw^{-n}$。
真正两条拉回准确是
$$
\boxed{
q_S=\mathcal T(v_S)(q+\bar a_pr),\qquad
q_T=\mathcal T(v_T)(q+\alpha\bar a_pr).
}
\tag{24}
$$
证明是先按 (22) 乘两条接触：
第三块分别为 $v_S(D_2+a_pD_1)$、
$v_T(D_2+\alpha a_pD_1)$，
再交换 (23) 的完整有限和。
所以 (24) 保留 Gaussian charge 差及 double-Euler 交换差。

特别，由 $\mathcal T(vu)=\mathcal T(v)\mathcal T(u)$，
$$
\boxed{
q_T-\mathcal T(h)q_S
=(\alpha-1)\bar a_p\,\mathcal T(v_T)r .
}
\tag{25}
$$
这不是把两个拉回认作 $v_Sq,v_Tq$。

在整个环境负 Laurent 格的两份直和上，(24) 的核准确为
$$
\langle w^{-1}\rangle\oplus\langle w^{-1}\rangle,
$$
秩为 $2K-2$，且整像 $p$-饱和。
确实，先用单位 $\mathcal T(h)^{-1}$ 变换第二输出，
再用常数矩阵
$$
\begin{pmatrix}1&\bar a_p\\1&\alpha\bar a_p\end{pmatrix}
$$
分离两输入；行列式 $(\alpha-1)\bar a_p$ 是单位。
最后两个相同的 $\mathcal T(v_S)$ 各只损失首列，
其其余子式由 R372 为单位。
此结论在实际双线性像上的使用，仍必须保 (23) 的同源限制。

## 7. 与两条完整中央条件的准确接口

R403 的两条完整中央观察是不同 Gaussian 下的真实
$\mathfrak C_S,\mathfrak C_T$，包含全部 wrap 和两个基准。
本篇支付此前不能免费使用的三个步骤：

- (7) 使加入 $T$ 后的整个有限 canonical 来源对一个固定低次数导子闭合；
- (19)–(21) 给同一个原核、同一个整左核的真实 $\zeta$ 像包含；
- (24)–(25) 给两个不同 charge 对同一接触的完整拉回，含原点主部投影与交换差。

它们尚不证明 R403 的两个完整基准等于 (20) 的零配对。
尤其不能从 (24) 的环境原始性推出实际 $q,r$ 遍历全部格，
也不能从 $S,T$ 的中央零使其乘积列或上述单个残数为零。
接下来的比较可以直接使用 (21)、(23)，无需再重付新 $V$ 的固定极，
但仍须在同一个 $P_2,\lambda_2$ 上完成。

## 依赖与同步

R335 的完整原导子整基；R338 的同一双接触及真正 $C_2$；
[R351](R351-original-canonical-serre-adjoint-and-integral-second-lift-connection.md)、
[R352](R352-whole-canonical-degree-two-derivation-and-original-moving-poles.md)
的全整连接与物理目标；
[R372](R372-original-fixed-torsion-boundaries-and-true-double-euler-pullback.md)
的 double-Euler 拉回；
[R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)、
[R403](R403-two-original-rank-two-sources-joint-carry-and-second-top-row.md)
的两条真实来源、charge 和全部第三精度。

全篇为统一代数及整矩阵证明，不扫描目标素数。
执行环境不可用期间按根规矩用小文本 API 保存，不冒称 git pull。
