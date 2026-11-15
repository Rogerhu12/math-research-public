# R392：两条自然总通量与响应 E 分量的真实联调及完整联合商接口

日期：2026-11-15。**原文复核与有限纸面构造；没有执行新的几何、profile、原根、秩、积分或人工计算。**

本稿完整读取
[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、
[R222](R222-simultaneous-real-pure-and-eight-flux-control.md)、
[R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md)
的实际截面、原型和完整基准，并回读
[R101](R101-finite-replication-and-signed-fourth-character-costs.md)
的真实复制恒等式。

得到一项可以立即完整实现的联合结论：固定 R390 的两条自然读出后，可以在**同一条有限真实路径**上同时任意指定它们及 $E$ 的全部响应分量。此结论保留了每个原型新增的清零块成本，并明确区分最后复制数之前和之后固定的参数。

它没有直接升级为 whole $E$ 与两条自然读出的全部联合控制。真正剩余的是第 9 节的同一个实际联合商，而不是重新计算 R333 的成员身份或省去原型成本。

## 1. 原 whole E、响应像和两条固定读出

沿用真实完整成本空间 $U$、响应空间 $\mathcal R$，以及
$$
E=(\pi,\mathcal Q):U\longrightarrow\mathscr P=E(U),
$$
$$
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0).
\tag{1}
$$
$\mathcal Q$ 是对所有真实紧 profiles 的整个 universal self 函数。它不是总通量，也不等于整个 mixed 输出。

记
$$
\mathscr L=E(\mathcal R),\qquad
\mathscr C=\mathscr P/\mathscr L,\qquad
q:\mathscr P\longrightarrow\mathscr C.
\tag{2}
$$
R333 已证明
$$
E(\mathcal S)=\mathscr P
\tag{3}
$$
并给紧目标集上的有限真实 $C^1$ 截面。这里 $\mathcal S$ 是同 scalar/frame 端口、$M=\mathbf T=0$ 的实际第四成本集合。

但 R333 的已付响应等号准确为
$$
E(U)_0=E(\mathcal R)_0,
\tag{4}
$$
而不是全权的 $\mathscr P=\mathscr L$。R333 的证明本身保留了 (2) 的商。

固定
[R390](R390-actual-joint-control-of-two-fixed-natural-total-fluxes.md)
从起点选择的两个真实 profiles $u_+,u_-$，共同物理窗口和右锚，并置
$$
A(V)=\bigl(\Lambda_{u_+}(V),\Lambda_{u_-}(V)\bigr)\in\mathbb R^2.
\tag{5}
$$
每个 $\Lambda$ 都是原完整自然读出
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
$$
原真实 Green 与有序尾已支付
$$
A(\mathcal R)=0.
\tag{6}
$$
R390 又给
$$
A(\mathcal S)=\mathbb R^2
\tag{7}
$$
及紧目标集上的同一有限路径类型的 $C^1$ 截面。该截面的全部 $E$ 成本并未被置零。

选一个固定线性分裂
$$
\mathscr P=\mathscr L\oplus\mathscr C_*,
\qquad P_{\mathscr L}:\mathscr P\longrightarrow\mathscr L,
\quad P_{\mathscr L}|_{\mathscr L}=\mathrm{id},
$$
并定义
$$
F=P_{\mathscr L}E.
\tag{8}
$$
$\mathscr C_*$ 是实际有限函数空间中的一个代表补空间；没有将它当成零。

## 2. 本稿实际完成的联合定理

**定理。** 可以从一开始使用共同合法 $I$、原右锚、R390 的两个固定 profiles 和同一个常值端口，使对任意
$$
z\in\mathscr L,\qquad \lambda\in\mathbb R^2
$$
存在一条有限真实路径 $B$，满足
$$
\boxed{
M_B=\mathbf T_B=0,\qquad
F(V_B)=z,\qquad A(V_B)=\lambda.}
\tag{9}
$$
紧目标集有一个固定有限字、整数和参数域中的 $C^1$ 真实截面。可进一步用原 Klein 字闭合空间位移，保留其完整固定基准。

这是完整响应 $E$ 分量与两条自然通量的实际联调。它不是声称
$E(V_B)=z$，因为 $qE(V_B)$ 还可能非零。

先核线性目标范围：由 (7)，$A(U)=\mathbb R^2$。对任意一个指定 $A$ 值，先选 $V\in U$；再加响应可任意改变 $F$，而由 (6) 不改 $A$。所以
$$
(F,A)(U)=\mathscr L\oplus\mathbb R^2.
\tag{10}
$$
下面证明整个 (10) 是实际像；不能仅用这个线性论证代替路径。

## 3. 原响应列、原型和共同物理域

选有限个真实响应 $K_1,\ldots,K_m$，使
$$
\mathsf K=(F(K_1)\ \cdots\ F(K_m)):
\mathbb R^m\longrightarrow\mathscr L
$$
可逆。这里 $m=\dim\mathscr L$；若 $m=0$，结论直接是 R390。

每列按原响应来源写成有限组合
$$
K_j=\sum_{\nu=1}^{N_j}c_{j\nu}
\mathcal B_{P_{j\nu}}(\tau_{j\nu}).
\tag{11}
$$
选原实际第三 prototypes
$$
M_{L_{j\nu}}=0,\qquad
\mathbf T_{L_{j\nu}}=\tau_{j\nu},\qquad
V_{L_{j\nu}}=v_{j\nu}.
\tag{12}
$$
这些正是 R333 §5.3 使用的完整响应原型。原 R71/R77 实现以及 R302 的整块正则化、真实倒行均保全部第三槽；不用 diagonal 覆盖替代它们。

本稿不要求另一个已冻结窄区间能容纳新增库。可以先固定这一有限库及二阶小族，用
[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)
的真实共同 $\omega$ 平移提高它们的下界，再以
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)
的 M0/frame 桥搬到 R390 的共同端口。

共同平移会同时变换原型及响应列；$\mathscr L$ 在该已付可逆仿射作用下稳定，所以变换后的列仍可选为其基。这里不把原列值标签假称未变。M0 夹心运输又保完整第三算子，但增加真实第四基准，全部计入 (12)。

因此可以保留 R390 已固定的两个 profiles 和右辅助包，使全部原型、小二阶族、后续 R390 校正都在同一个 $I$ 与严格 $x+\omega>0$ 的包络中。以后大参数只用原小族的有限重复，不扩大该包络。常值端口、真实 frame、正时间余量和共同右锚在每次调用结束时准确复位。

## 4. 先把原型的整个 A 基准准确清零

令
$$
v_j=\sum_{\nu=1}^{N_j}v_{j\nu}.
$$
注意这里的基准和不乘 (11) 中的系数 $c_{j\nu}$：那些系数进入二阶参数，而不是负路径复制。

用 R390 对有限目标 $-A(v_j)$ 取真实块 $D_j$，满足
$$
M_{D_j}=\mathbf T_{D_j}=0,\qquad
A(V_{D_j})=-A(v_j).
\tag{13}
$$
将 $D_j$ 追加到第 $j$ 组一个固定 prototype 后面。因为两段均为 M0，
原 R83 的完整加法给新的第三算子仍是原 $\tau_{j\nu}$，响应列 (11) 不变。

记新一组原型成本和为
$$
\widehat v_j=v_j+V_{D_j}.
$$
于是
$$
\boxed{A(\widehat v_j)=0.}
\tag{14}
$$
$F(V_{D_j})$、$qE(V_{D_j})$ 都不置零。特别，当这个新 prototype 随后重复 $n$ 次时，**整个 $V_{D_j}$ 也随之重复 $n$ 次**。这一成本进入下一节的 leading 仿射基准，不能塞入一个与 $n$ 无关的误差。

所有 (13) 的目标和所用 R390 参数现在固定。它们没有使用末尾尚未选择的 $n$。

## 5. 原 R101 字和大有限参数的真实允许域

第 $(j,\nu)$ 个二阶族在参数 $c_{j\nu}t_j$ 上调用，第三 prototype 使用 (14) 的已修正版本。按原 R101 §2，正负参数、同一原型的 $n$ 次出现及其整个真倒行共享当次同一条路径。

拼接各组，准确得到
$$
\boxed{
V_{Z(t,n)}
=E_0(t)+n\left(2\sum_{j=1}^m\widehat v_j+
\sum_{j=1}^mt_jK_j\right),
\qquad M_Z=\mathbf T_Z=0.}
\tag{15}
$$
$E_0(t)$ 是完整偶基准，包括二阶族自身的未知第三、第四成本和真实桥。
它在定下参数盒后为固定 $C^1$ 函数，与末复制数 $n$ 无关。

定义完整 leading 基准
$$
a=2\sum_jF(\widehat v_j),\qquad
t^0=-\mathsf K^{-1}a.
\tag{16}
$$
式 (16) 包含所有 (13) 的清零块成本；一般 $a\ne0$。
取固定紧盒
$$
\mathcal B=t^0+[-1,1]^m
$$
及其稍大的开邻域。

此时需要支付任意有限 $t^0$，而不是默认为小参数。原 R101 §4 给准确方法：先固定真实正时间小族
$$
A_0(s),\quad |s|\le s_*,\qquad M_{A_0(s)}=sP.
$$
对每个所需有限参数范围选择一个固定整数 $q$，使
$|c_{j\nu}t_j|/q<s_*$ 在整个扩大的盒上成立，然后使用
$$
A_{j\nu}(t_j)
=A_0(c_{j\nu}t_j/q)^q.
\tag{17}
$$
矩阵按原式直接相加，故
$M_{A_{j\nu}(t_j)}=c_{j\nu}t_jP$。
每个小块的 scalar/frame 和全部常值 germs 准确复位，
所以正时间余量及物理包络保持。

这些有限重复可能改变二阶族的第三与第四成本；它们完整进入 (15) 的 $E_0(t)$。R101(8) 只需真实 $M=tP$，不要求该族的第三、第四量线性。
所有正负 $t$ 均使用同一个 (17)。

选择顺序严格是：
先修正 prototypes，得到有限的 $a,t^0$；
再固定 $\mathcal B$ 及 (17) 的整数 $q$；
之后才选择最后的 $n$。
$E_0(t)$ 的大小可以依赖这些已固定整数，不能依赖还未取的 $n$。

## 6. 后置 A 校正及其全部 F 成本

由 (6)、(14)、(15)，准确有
$$
A(V_{Z(t,n)})=A(E_0(t)).
\tag{18}
$$
这是原型实际清零之后的结果；不能仅由 $A(K_j)=0$ 推出它。

给定紧目标集
$$
\mathcal K\subset\mathscr L\oplus\mathbb R^2,
$$
令 $\mathcal K_A$ 为其第二投影。集合
$$
\mathcal Y=
\{\lambda-A(E_0(t)):
\lambda\in\mathcal K_A,\ t\in\mathcal B\}
\tag{19}
$$
紧，并且在选择 $n$ 前已经固定。

R390 给包含 $\mathcal Y$ 的邻域上的同一个实际 $C^1$ 截面 $\mathscr D_A(y)$：
$$
M_{\mathscr D_A(y)}=\mathbf T_{\mathscr D_A(y)}=0,\qquad
A(V_{\mathscr D_A(y)})=y.
$$
它自己的所有脉冲尺度、桥和整数对这个紧集一次固定。
原成本 $F(V_{\mathscr D_A(y)})$ 仍完整保留。

定义实际字
$$
\widetilde Z(t,n;\lambda)
=Z(t,n)\,
\mathscr D_A\bigl(\lambda-A(E_0(t))\bigr).
\tag{20}
$$
所有块 M0/T0，故第四成本严格相加。于是对每个 $t$，
$$
\boxed{A(V_{\widetilde Z})=\lambda,}
\tag{21}
$$
而
$$
\boxed{
F(V_{\widetilde Z})
=\mathcal E(t,\lambda)+n(a+\mathsf Kt),}
\tag{22}
$$
其中
$$
\mathcal E(t,\lambda)
=F(E_0(t))
+F\!\left(V_{\mathscr D_A(\lambda-A(E_0(t)))}\right).
\tag{23}
$$
第二项不是零，不假设它线性，也不假设它只改变响应方向。

(23) 在固定 $\mathcal B\times\mathcal K_A$ 上为 $C^1$，
其值和一次 $t$ 导数都在选择 $n$ 前固定并有界。
这正是允许把后置校正视为 $O_{C^1}(1)$ 的范围；
它与第 4 节会乘 $n$ 的原型清零成本完全不同。

这里的 $C^1$ 不是仅凭抽象有限维断言：
R333 的 whole E 在其实际函数像上由有限真实 pure/self 查询分离；
R390 的两个自然读出使用固定紧积分、pure 及真实三矩尾查询。
原 R56 恢复和 R302 §8 的真实历史 Duhamel 公式给这些有限路径参数的 $C^1$ 性，
包括全部变量时长和桥成本。

## 7. 一个有限 n 在同一路径上准确联调

对目标 $(z,\lambda)\in\mathcal K$，(22) 等价于
$$
t=t^0+\frac1n\mathsf K^{-1}
\{z-\mathcal E(t,\lambda)\}.
\tag{24}
$$
一次取一个有限正整数 $n$，使右边在整个目标紧集上把 $\mathcal B$ 映入严格内部，
且其 $t$ 导数范数小于 $1/2$。这样的 $n$ 同时大于 (23) 的值界和导数界即可。

原所有参数盒、整数 $q$、prototype 清零块及后置 R390 截面已固定，
所以此处没有以 $n$ 改变一个先前假称 $O(1)$ 的基准。

收缩定理和有限参数 IFT 给唯一的 $C^1$ 选择
$$
t=t(z,\lambda).
$$
把它代入 (20)，便准确得到 (9)。
因此响应列上 $A=0$ 已在本稿通过真实原型基准校正和后置真实截面，
转成一个实际联合控制定理；它不是直接把形式响应当作完整负路径。

## 8. whole E 的哪些部分现已与两条 A 同时支付

可以选择按原真权分解的补空间，使 $P_{\mathscr L}$ 保各权。
[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)
与 R333 已给
$$
E(U_\sigma)=E(\mathcal R_\sigma),
\qquad \sigma=-8,-6,-4,0.
\tag{25}
$$
其中 $E(U_{-8})=0$，权零联合像的已付真维是十；不重算旧秩。

所以 (9) 特别允许在同一路径上：

- 取两条固定自然通量的任意二元目标；
- 同时指定权 $-6,-4,0$ 的完整 universal pure/self 联合投影；
- 同时指定其余所有已处在 $\mathscr L$ 内的响应 E 分量。

这些是整个相应权的函数投影，不是另挑几条母包采样。
例如可以把以上全部响应 E 分量置零，同时让两条自然通量取任意指定值。
但这句不能缩写成 whole $E=0$。

为显式保留未支付部分，对 (20) 取原商 $qE$，得
$$
\boxed{
qE(V_{\widetilde Z})
=qE(E_0(t))
+2n\sum_jqE(\widehat v_j)
+qE\!\left(V_{\mathscr D_A(\lambda-A(E_0(t)))}\right).
}
\tag{26}
$$
响应项 $\sum t_jK_j$ 的商为零，其余三项没有被删除。
特别是 (13) 的清零块可能改变第二项的系数，并随 $n$ 放大。
这是 (9) 与 whole E 联合结论之间真实的成本差别。

## 9. 完整 E 与两条 A 的准确剩余商

记
$$
J=(E,A):U\longrightarrow\mathscr P\oplus\mathbb R^2.
$$
由 (6)，
$$
J(\mathcal R)=\mathscr L\oplus\{0\}.
$$
其真正的联合商可准确写为
$$
\boxed{
J(U)/J(\mathcal R)
\simeq
\mathscr D:=
\{(qE(V),A(V)):V\in U\}
\subset\mathscr C\oplus\mathbb R^2.}
\tag{27}
$$
这里的线性像还可准确付清，但不能将其升级成实际满射。

### 9.1 两个真实 ker E 类给出完整线性乘积

取
[R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md)
的完整正规成本
$
V_\delta=\mathcal Q_\delta(1,k,k)\in U,\qquad
\Lambda_u(V_\delta)=\frac{X(u)}{80},\quad
X(u)=\int x(u'')^5.
$
使用
[R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)
**独立第 5 节**从原 R89 证明的真实协变：
$
\Lambda_u(P_{H,c}V)=H^2\Lambda_{C_{H,c}u}(V),\qquad
(C_{H,c}u)(x)=u((x-c)/H).
\tag{28}
$
该身份保完整三矩尾输运；不使用 R365 已撤回的 H 非零值。

因为 $X(C_{H,0}u)=H^{-8}X(u)$，(28) 给
$\Lambda_u(P_{H,0}V_\delta)=H^{-6}X(u)/80$。
U 的原有限整权分解和 R203 的真实有限 Laurent 投影因此准确推出
$
\Lambda_u(\Pi_{-6}V_\delta)=X(u)/80
\quad\text{对全部真实紧 }u.
$
只需在保支撑与 collars 合法的 $H=1$ 邻域比较有限 Laurent 系数；
没有新的根恢复或程序计算。

R323 已付 $E(U_{-6})=E(\mathcal R_{-6})$，故可选同权真实响应 $R_\delta$，使
$
K_X:=\Pi_{-6}V_\delta-R_\delta\in\ker E,\qquad
\Lambda_u(K_X)=X(u)/80.
\tag{29}
$
这里是在真实有限空间里选择成员代表，不把带负系数的 $K_X$ 称为实际路径。

whole E 核已由 R322/R323 证明对正仿射作用稳定。
取足够小的固定 $c\ne0$，再令
$
K_M=\frac{P_{1,c}K_X-K_X}{c}.
$
由 (28) 和 $X(C_{1,c}u)=X(u)+cM(u)$，其中 $M(u)=\int(u'')^5$，有
$
\boxed{K_M\in\ker E,\qquad \Lambda_u(K_M)=M(u)/80.}
\tag{30}
$
两条都是保实际右锚输运的完整泛函身份。

R390 的固定镜像 profiles 满足 $M(u_\pm)=M>0$、
$X(u_\pm)=\pm aM$，故
$
A(K_X)=\frac{aM}{80}(1,-1),\qquad
A(K_M)=\frac{M}{80}(1,1).
$
此二列严格独立。因此
$
\boxed{
A(\ker E)=\mathbb R^2,\qquad
J(U)=\mathscr P\oplus\mathbb R^2,\qquad
\mathscr D=\mathscr C\oplus\mathbb R^2.}
\tag{31}
$
所以 full E 与两条 A 没有尚未辨明的线性目标相容限制。
真正未付的是这个乘积上**同一个实际路径**的联合实现。

### 9.2 剩余的实际截面接口

R333 分别支付 $\mathscr D$ 到 $\mathscr C$ 的投影，R390 支付到 $\mathbb R^2$ 的投影。
这不推出 $\mathscr D$ 上的实际满射。式 (26) 具体展示了两次校正之间的商耦合；
(29)、(30) 也只是已核真实线性类，尚非两条可自由取正负的实际零 E 模块。

一个准确的后继接口是：若从起点取得
$$
V\longmapsto(qE(V),A(V))
$$
在其真实像 $\mathscr D$ 上的有限实际 $C^1$ 截面，
则按本稿第 4–7 节、把基准清零和后置校正同时用于这整个商，
再用同一 $E(\mathcal R)$ 响应基，就能取得 $J(U)$ 上的完整实际 $C^1$ 截面。
反之，完整 J 截面当然投影成该联合商截面。

该接口保留正确的商，不把原型 $qE$ 基准在未知时默认为零。

### 9.3 为什么不能直接再套 R323 的字符排除

R323 的满闭锥证明使用 whole E 核的正仿射与真实反号稳定性，
并逐权排除正字符。固定 profiles 的两条 $A$ 不能自动当作同一仿射模。
若改用包含它们的整个有限仿射轨道，仍需重新处理增强投影的正字符和真权零商。

R333 的 $H_*,J_4,J_6$ 已付 $E=0$，其原成员身份本身没有给自然 $A$ 值。
不能因为 $\mathcal Q(H_*)=0$ 就断言 $A(H_*)=0$。

不过 (29)、(30) 现在允许准确处理固定 J 上的原正字符。
$\lambda_+$ 为真权零且平移不变，故
$
\lambda_+(K_X)=\lambda_+(K_M)=0.
$
按两列 A 的可逆矩阵选择实数 $\alpha,\beta$，令
$
\widehat H_*=H_*-\alpha K_X-\beta K_M,\qquad A(\widehat H_*)=0.
$
就得到真实线性空间中的完整身份
$
\boxed{
J(\widehat H_*)=0,\qquad\lambda_+(\widehat H_*)=1.}
\tag{32}
$
所以 $\lambda_+$ 确实不能经这个固定 $J$ 下降。
不需要为此重新评价 $H_*$ 的原根；$\alpha,\beta$ 由其两个有限真实读出定义即可。
$\widehat H_*$ 仍未被称为实际路径。

式 (32) 不替代新的满锥证明：固定两条 A 的核尚未证明在仿射作用下稳定，
R127 的字符提取可能离开这两个固定读出的张成空间。
若扩大到整个有限仿射轨道，还须对那个真正增强商重新核其字符与实际截面条件。

因此本稿没有宣称 whole E 与两条 A 不可联合。
它给的是一个真实已完成的响应分量联调，以及尚需支付的准确商 (27)，
而非把“分别可控”当作联合证明。

## 10. 真倒行、共享原型和空间闭合

R101 中的倒行始终是整个当前 M0 块的真倒行。
其 canonical 第三场包含原 $Y_b$ 端历史修正；
完整第四成本同号。所有正负二阶参数和重复出现使用同一实际原语，
不能在副本之间独立修改后仍沿用 (15)。

若从起点另加入 R302 的正则前缀，其第四成本先计入 (12)，
再执行 (13)–(24)。之后允许 prototype 自由漂移时，
R302(22) 仍准确保整字 M/T0，但其响应和基准都会漂移；
必须对本稿全部目标重解增强方程。本稿没有因此自动授
某个旧 Gaussian 芽、Morse 性或另一个被冻结的 g。

空间闭合采用 R390 的同一原 Klein 词。
设所用固定 frame 桥的完整基准为 $V_{\rm K}$，
则闭路径完整成本是
$$
V_X=4V_B+V_{\rm K}.
$$
对联合目标 $(z,\lambda)$，在 (9) 中使用
$$
\left(\frac{z-F(V_{\rm K})}{4},
      \frac{\lambda-A(V_{\rm K})}{4}\right),
$$
即可准确保目标并闭合整个真实位移。
桥成本的商分量仍在 (26) 的未付范围内，不因空间闭合消失。

所有整数和有限路径在选定目标紧集后固定。
可能增长的是真实长度、位移及成本；没有重设位置积分，
没有使用零时长极限、实数次复制或形式负路径。

## 11. 本稿新增结论的使用方式

需要与 R390 两条自然通量同时控制响应 E 分量时，
可以直接使用 (9)，不再为原型的 Λ 基准重开未证明的假设。
若目标确实要求 whole pure/self 与两条自然通量共同为零，
则仍须处理 (26)–(27) 的实际商，不能把 $F=0$ 改写成 $E=0$。

这也是后继最小的新问题：支付真实联合商 $\mathscr C\oplus\mathbb R^2$ 中一个此前未付的实际方向，
或证明其准确的实际锥与截面条件。
旧的 C2/C4/C6 成员结果、十三比较列、pure/self 秩与 R390 四列不需要重算。
