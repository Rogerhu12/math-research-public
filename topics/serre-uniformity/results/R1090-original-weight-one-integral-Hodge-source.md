# R1090. 原 full47 的 weight-one 整 Hodge 来源与 ordinary CM 高矩

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**状态：下述来源、整性、有限读数及 CM 算子恒等式已纸面证明。
所选有限候选的 rank95 尚未执行认证，不预设这个秩。**

固定 $p=47$、$X=X_{\rm ns}^+(47)$、$J=\operatorname{Jac}(X)$。
R1078/R1080 给 $g(X)=73$，原全部尖点除子记为 $C_\infty$，
$\deg C_\infty=23$。
下文原 Hodge 格始终是 $X$ 自身的格，不从平方水平曲线搬一个微分基。

## 1. 正确的 weight-one 来源与有理下降

设 $O=\mathbf F_{47^2}=\mathbf F_{47}[i]$、$i^2=-1$，
$x=d+ci$ 对应行向量 $(c,d)$，$N(x)=c^2+d^2$。
取 $\zeta=\exp(2\pi i/47)$。
对 $\Lambda_\tau=\mathbf Z+\mathbf Z\tau$，
$\eta_1,\eta_\tau$ 是 Weierstrass zeta 沿 $1,\tau$ 的 quasi-period。
定义
$$
e_{(c,d)}(\tau)=\frac1{2\pi i}
\left(\zeta_W\!\left(\frac{c\tau+d}{47}\right)
-\frac{c\eta_\tau+d\eta_1}{47}\right),\qquad (c,d)\ne(0,0).
\tag{1090.1}
$$
这是代数的权一 Eisenstein 形式，满足 $e_{-x}=-e_x$。
对 $a\in\mathbf F_{47}$、$\rho\in O^\times$，使用完整 Reynolds 来源
$$
F_{a,\rho}
 =\sum_{x\in O^\times}
 \left(\zeta^{aN(x)}e_xe_{\rho x}
       +\zeta^{-aN(x)}e_xe_{\bar\rho x}\right).
\tag{1090.2}
$$
**第二项的共轭只作用于 $\rho$，同时系数的指数取负。**
先前可考虑的对称候选
$\sum_x(\zeta^{aNx}+\zeta^{-aNx})e_x(e_{\rho x}+e_{\bar\rho x})$
恰为 $F_{a,\rho}+F_{-a,\rho}$。本篇不假设这个对称子族单独张成；
有限消费者始终保留 (1090.2) 的两个不同相位。

对 $\gamma\in\mathrm{SL}_2(\mathbf Z)$，
$e_v|_1\gamma=e_{v\gamma}$。
把 full-level 的作用扩到 $\mathrm{GL}_2(\mathbf F_{47})$ 时，
$\operatorname{diag}(1,b)$ 在系数上给
$\sigma_b(\zeta)=\zeta^b$，仍有 $e_v^g=e_{vg}$；
因此系数函数同时按 $\sigma_{\det g}$ 变化。

对 $u\in O^\times$，乘法矩阵 $m_u$ 的行作用为 $x\mapsto xu$，
且 $\det m_u=N(u)$。故 (1090.2) 的两个系数变为
$\zeta^{\pm aN(x)N(u)}$，torsion 标签同时变为
$xu,\rho xu,\bar\rho xu$。换元 $y=xu$ 即恢复 (1090.2)。

正规化子的另一生成元 $\operatorname{diag}(1,-1)$
把 $x$ 送到 $-\bar x$，并使 $\zeta$ 变为 $\zeta^{-1}$。
换元 $y=-\bar x$ 后，第一项变成
$\zeta^{-aNy}e_ye_{\bar\rho y}$，第二项变成
$\zeta^{aNy}e_ye_{\rho y}$，恰好交换。
所以 (1090.2) 是完整 $N_{\rm ns}(47)$-不变量，
包括行列式的 Galois 下降，给原 $X/\mathbf Q$ 上的有理权二形式。

为确认保留了完整 characteristic-zero 来源，取任意 seed
$\zeta^j e_\alpha e_\beta$，令
$\rho=\beta/\alpha$、$a=j/N(\alpha)$。
正规化子中 Cartan 的半个群和，以 $x=\alpha u$ 换元后给
(1090.2) 的第一项；另一个 coset 给第二项。因此这些 $F_{a,\rho}$
正是完整的原 Reynolds product 族。
Khuri–Makdisi 的 weight-one product 张成定理及 Zywina
Corollaries4.10–4.11 给它们在 characteristic zero 张成
$H^0(X,\Omega^1(C_\infty))$。
这一来源说明不代替模4513的实际整秩认证。

有准确重排
$F_{a,-\rho}=-F_{a,\rho}$、
$F_{a,\bar\rho}=F_{-a,\rho}$，
以及 $F_{0,\rho}=-\sum_{a=1}^{46}F_{a,\rho}$。
故可以取 $a=1,\ldots,46$ 及
$\rho=d+ci$、$0\le c,d\le23$、$(c,d)\ne(0,0)$。
一般纯虚 $\rho=ci$ **仍保留**；不能把对称子族的逐项消失
移到完整 (1090.2)。
令 $q_\tau=\exp(2\pi i\tau)$，原微分为
$$
\omega_{a,\rho}=F_{a,\rho}\frac{dq_\tau}{q_\tau}.
\tag{1090.3}
$$
在 characteristic zero 的 full-level 曲线上它只可能在尖点有简单极；
沿非尖点有限商下降时，不变的正则微分在粗参数上仍正则。
所以 $\omega_{a,\rho}\in H^0(X,\Omega^1(C_\infty))$。

### 1.1 不依赖复近似的代数读取

在 $Y^2=4X^3-g_2X-g_3$、$\omega=dX/Y$ 的规范下，
这里复 Tate 实现取 $X=(2\pi i)^{-2}\wp$、$Y=(2\pi i)^{-3}\wp'$，
故 $\omega=2\pi i\,dz$，与 (1090.1) 的 $e$ 规范相同。
对不同的非零47挠点 $P,Q$、$P+Q\ne0$，
Weierstrass 加法式给
$$
e(P+Q)-e(P)-e(Q)
 =\frac12\frac{Y(P)-Y(Q)}{X(P)-X(Q)}.
\tag{1090.4}
$$
$Q=P$ 时取实际切线斜率。令 $\lambda(P,kP)$ 为这一 $Y/X$ 斜率，
对 $k=1,\ldots,45$ 相加、用 $e(-P)=-e(P)$，得
$$
e(P)=-\frac1{94}\sum_{k=1}^{45}\lambda(P,kP).
\tag{1090.5}
$$
所以所有 e 值都可以由原47挠点和原 invariant differential
在有限域或整数环中精确读取。这里没有额外可任选的加性常数：
两个满足加法式的差给 $E[47]\to\mathbf G_a$ 的同态，
而47可逆，故差为零。
(1090.4)–(1090.5) 也固定了与 (1090.1) 相同的尺度。
若使用短模型 $y^2=x^3+A x+b$、$\omega=dx/(2y)$，
则 $Y=2y$，所以同一式准确变为
$47e(P)=-\sum_{k=1}^{45}m_y(P,kP)$，
$m_y=(y(P)-y(kP))/(x(P)-x(kP))$；
此短模型斜率前没有 $1/2$。
这与 Khuri–Makdisi Corollary3.13、Remark3.14 的代数表达一致。

## 2. 原 q 展开与良素整性

取 $t=q_\tau^{1/47}$，并用 $0\le c<47$。
由 Jacobi product 的 logarithmic derivative，
令 $w=\zeta^dt^c$，有
$$
e_{(c,d)}
 =\frac c{47}-\frac12
 -\sum_{n\ge0}\frac{q_\tau^n w}{1-q_\tau^n w}
 +\sum_{n\ge1}\frac{q_\tau^n w^{-1}}{1-q_\tau^n w^{-1}}.
\tag{1090.6}
$$
$c=0$ 时把第一和的 $n=0$ 项作为常数读取。
因此常数项为
$$
C(c,d)=
\begin{cases}
c/47-1/2,&c\ne0,\\
(\zeta^d+1)/(2(\zeta^d-1)),&c=0,\ d\ne0,
\end{cases}
$$
其余系数为完整有限除数和
$$
[t^n]e_{(c,d)}
=-\!\sum_{\substack{kr=n\\r\equiv c\ (47)}}\zeta^{dk}
+\!\sum_{\substack{kr=n\\r\equiv-c\ (47)}}\zeta^{-dk},
\qquad n\ge1.
\tag{1090.7}
$$
(1090.6) 直接由
$\theta_1(z)=\mathrm{constant}\cdot w^{-1/2}(1-w)
\prod_{n\ge1}(1-q_\tau^n)(1-q_\tau^nw)(1-q_\tau^nw^{-1})$
求导得到；Legendre 关系
$\eta_1\tau-\eta_\tau=2\pi i$ 正好给 $c/47$。
所以这里没有引用某个未刊平方水平的计算结果。

令 $\ell>3$、$\ell\ne47$。
$\zeta^d-1$ 的范数只含47，故 (1090.7) 的所有系数在
$\mathbf Z_{(\ell)}[\zeta]$ 中。
由 R1067，原 $X$ 有 smooth proper 的良模型；
尖点在未分歧扩张后给互不相交的光滑截面。
原 cusp stabilizer 在 $N_{\rm ns}\cap\mathrm{SL}_2$ 中只有
$\{\pm I\}$，所以该 cusp 的真实参数为 $t$，width恰47。

为明确整性不依赖猜测的整基：
设某个原有理 $\omega_{a,\rho}$ 有负垂直赋值，
取最小 $r>0$ 使 $\ell^r\omega_{a,\rho}$ 为原良模型的整截面。
由整 q 展开，其约化在一个 cusp 的整个形式邻域为零。
特殊纤维几何连通且光滑，故该约化截面恒零，
与 $r$ 的最小性矛盾。
这在一个包含该 cusp 的未分歧扩张上证明，
再由忠实平坦下降得到原整性。因此
$$
\omega_{a,\rho}\in
L^c_\ell:=H^0(\mathcal X/\mathbf Z_\ell,\Omega^1(C_\infty)).
\tag{1090.8}
$$
对于本次 $\ell=4513$（也适用于283），全部23个 cusp 已在基域有理。

## 3. 全部23个留数与恰好的有限 jet 范围

由 Riemann–Roch 及相对 Serre duality，
$$
\deg\Omega^1(C_\infty)=2\cdot73-2+23=167,\qquad
\operatorname{rank}L^c_\ell=95.
$$
又 $H^1(\Omega^1(C_\infty))=H^0(O(-C_\infty))^\vee=0$，
故在23个 cusp 都有理时，原整数环上有正合列
$$
0\longrightarrow L_\ell
\longrightarrow L^c_\ell
\xrightarrow{\operatorname{Res}}
\left\{(r_b)_{b\in\mathbf F_{47}^\times/\{\pm1\}}:
             \sum_b r_b=0\right\}
\longrightarrow0,
\tag{1090.9}
$$
其中 $L_\ell=H^0(\mathcal X,\Omega^1)$ 的秩为73。

对同一个有理形式 $F$，全部 cusp 的常数项由
$\zeta\mapsto\zeta^b$ 读取，$b$ 遍历 $\mathbf F_{47}^\times/\{\pm1\}$。
由于
$$
\omega_F=47F(t)\frac{dt}{t},
$$
真实 residue 是 **$47c_0(F;\zeta^b)$**。
即使47在模4513中是单位，也保留这一原尺度。
单个 $c_0$ 在 $\mathbf F_{4513}$ 只给一个线性条件，
不能用它替代 (1090.9) 的全部22个独立条件。

另一方面，映射
$$
L^c_\ell/\ell \longrightarrow\mathbf F_\ell^{168},
\qquad
\omega_F\longmapsto(c_0(F),\ldots,c_{167}(F))
\tag{1090.10}
$$
在指定 cusp 的原参数 $t$ 下单射：
若这些系数全零，作为 $\Omega^1(C_\infty)$ 的截面，
它在该点的零阶至少168，大于这条线丛的degree167，
所以截面为零。
这说明168个系数足够认证候选的完整秩，不需要无限展开或未付 Sturm 猜测。

因此，若某个明确有限候选集的 (1090.10) 矩阵模 $\ell$ 秩95，
则它在原 $L^c_\ell$ 中的整张成就是全部 $L^c_\ell$（Nakayama）。
其完整23 residue矩阵必有秩22，核恰为原73维 Hodge 格的约化。
消费者必须实际验证这两个秩，不能从候选定义预设成立。

这里模 $\ell$ 的 kernel 向量不必按任意整数系数提升后就没有 cusp 极。
真正的整 lift 由 (1090.9) 构造：从 residue 矩阵删去总和关系的一行，
选一个 $22\times22$ 的单位 minor，在 $\mathbf Z_\ell$ 上精确解掉
其余73个基向量的全部 residues。
这给原 $L_\ell$ 的整基，并可经一个整可逆换基提升指定的有限域 kernel 基。
所以后继模 $\ell$ 的 CM jet 可直接用 kernel 向量计算，
但不把其任意整数代表冒称 characteristic-zero holomorphic form。

## 4. 真正的原 Hecke 坐标桥

设 $n\ne47$ 为素数，$\sigma_n(\zeta)=\zeta^n$。
对同一标准 Tate 标记，实际 Hecke 对应的两个类型给
$$
c_r(T_nF)=\sigma_n^{-1}(c_{nr}(F))
+n\,\sigma_n(c_{r/n}(F)),
\tag{1090.11}
$$
其中 $c_{r/n}=0$ 除非 $n\mid r$。
可以从原 Tate 标记直接核准两个 Galois 方向。
$\mu_n$ 核的商 $u\mapsto u^n$、$q'\!=q^n$，
把原标记 $(P,Q)=(\zeta,t)$ 送到 $(\zeta^n,t^n)$；
$d\log t'=n\,d\log t$ 给第二项。
其余 $n$ 个商取 $q'_j=\zeta_n^j q^{1/n}$。
若 $an=1+47m$，将两个像标记同时乘 $a$ 不改变原 necklace，
因为中心标量属于原 normalizer。
标记可写成 $(\zeta^a,Q'_jP^{-aj})$；
后一个量随 $j$ 遍历 $t$ 的全部 $n$ 次根，
因为 $-47m\equiv1\pmod n$。
故常数系数受到 $\sigma_a=\sigma_n^{-1}$，
而 $d\log t'=d\log t/n$ 与根求和恰给第一项。
这支付了完整配对、中心标量与 Hecke normalization，
没有从 $X_0$ 的矩阵猜一个 diamond character。

用 (1090.10) 的完整基，(1090.11) 到 $r=167$ 只需要原展开到degree835，
以及 $\zeta\mapsto\zeta^{n}$ 和 $\zeta^{n^{-1}}$。
所以 $T_2,T_3,T_5$、以及 $H_2=T_2+2T_3+4T_5$，
可以在同一个原整格约化上精确重建。
它们必须保持 (1090.9) 的73维核。

这是为了原 CM 读数得到一个实际坐标基，
不把 R1081 的平方水平矩阵当成本曲线的整微分基。
R1081 已证明的完整 mod4513 因式次数
$1^{16},2^6,3^4,11,22$ 及线性根可用作原来源一致性检查；
新的矩阵来源仍完全是 (1090.1)–(1090.11)。

## 5. ordinary CM 的实际 Serre–Tate 高矩

这一节始终读取
$$
\lambda_{u_y}(\omega)=
q^{-1}\log_J\bigl((q+1-T_q)u_y\bigr)(\omega)\pmod q,
\qquad u_y=23[y]-C_\infty,
\tag{1090.12}
$$
而不是未经除实际 $(q+1-T_q)$ eigenvalue 的 $\log u_y$。
R1089 的整可逆性允许比较非零和深度，不允许删去这个精确算子。

取 R1085 所用的原 ordinary CM 点、physical 双 Tate basis、
Serre–Tate 参数 $s$，以及实际 canonical invariant differential
$\omega_{\rm can}$。Katz Main Theorems3.7.1–2、4.3.1–2 给
$$
\operatorname{KS}(\omega_{\rm can}^{\otimes2})=d\log s,\qquad
\nabla\omega_{\rm can}=u_{\rm can}\otimes d\log s,\qquad
\nabla u_{\rm can}=0.
\tag{1090.13}
$$
常数为 $+1$。这里不用另一个文献中 reciprocal 的 Kummer 参数。

把原 $\omega_F$ 写成 $f(s)d\log s$。
R1085 已连同全部 Hecke 根、Mahler 尾项及粗点重数证明
$$
\lambda_{u_y}(\omega_F)=
23[t^{q-2}]f(e^t)\pmod q,
\tag{1090.14}
$$
其中 $t$ 仅是 formal $\log s$ 的系数变量。
由 (1090.13)，这个读数等于
$23(q-2)!^{-1}\theta^{q-2}f(1)$，$\theta=s\partial_s$。
没有把 $s-1$ 的最高系数误当成 $\log s$ 的最高系数。

设原代数模型的微分为 $\omega_{\rm alg}$，
$\omega_{\rm can}=\Omega\omega_{\rm alg}$。
对 Hasse invariant $H_q$，
$\operatorname{Cartier}(\omega_{\rm can})=\omega_{\rm can}$
给 $H_q(E,\omega_{\rm can})=1$，因此
$$
\Omega^{q-1}=H_q(E,\omega_{\rm alg})\pmod q.
$$
CM 的非 Hodge 特征线同时是 ordinary unit-root 线
和复实现的 antiholomorphic 特征线。
在一个 CM 点，它们定义相同的代数直和补线。
两种连接比较都沿这个水平补线迭代，故其全部 CM jets
由同一个 algebraic Gauss–Manin/CM operator $\delta_{\rm CM}$ 读取。
更明确地，复反 Hodge 线在平坦基中由 $\bar\tau e_1+e_2$ 生成，
只沿 holomorphic 的 $\partial/\partial\tau$ 方向水平；
p-adic unit-root 线则对 Gauss–Manin 连接水平。
相同初始 CM 特征线的唯一水平形式延拓给全部迭代，
不能在每次求导后重新任取一个补线。
到阶 $q-2$ 的递推分母 $1,\ldots,q-2$ 全为单位。

最终 $\delta_{\rm CM}^{q-2}F$ 的权为 $2q-2$；
又 $(q-2)!\equiv1\pmod q$，所以准确得到
$$
\boxed{\quad
\lambda_{u_y}(\omega_F)
=23\,H_q(E,\omega_{\rm alg})^{-2}\,
  (\delta_{\rm CM}^{q-2}F)(E,\omega_{\rm alg})
 \pmod q.
\quad}
\tag{1090.15}
$$
只判断单位性时可保留非零 period 因子；
(1090.15) 给它在此最终权下的原有限读法。
$q=4513$、$j=1728$ 的原模型 $y^2=x^3+343x$
有基域内完整47挠点，是后继实际 finite-jet 的一个输入。
必须用真实47配对选择 CM Cartan 标记。

即使在 $j=0,1728$ 初值 $E_2^*=0$，
完整迭代仍有 $\delta E_2^*=-E_4/12$ 等非零导数；
不得把普通 Serre 导数在这个初值上反复应用而删去这些项。
R1085 已保留细根到粗点的2/3重数，(1090.15) 不另除它们。


### 5.1 完整 CM 导数的有限代数系统

令 $A_2=E_2^*$、$A_4=E_4$、$A_6=E_6$，在同一原微分下用模型
$$
Y^2=4X^3-\frac{A_4}{12}X+\frac{A_6}{216}.
$$
因此若原短 Weierstrass 模型为 $y^2=x^3+a x+b$、$\omega_{\rm alg}=dx/(2y)$，
则 $X=x,Y=2y,A_4=-48a,A_6=864b$。
每个原47挠点的 $e,X,Y$ 满足
$$
\begin{aligned}
\delta A_2&=(A_2^2-A_4)/12,\\
\delta A_4&=(A_2A_4-A_6)/3,&
\delta A_6&=(A_2A_6-A_4^2)/2,\\
\delta e&=A_2e/12-Xe-Y/2,\\
\delta X&=A_2X/6+eY+2X^2-A_4/36,\\
\delta Y&=A_2Y/4+3XY+e(6X^2-A_4/24).
\end{aligned}
\tag{1090.16}
$$
这里的 $A_2$ 是完整变化的变量，不在初值为零时删掉。

为核符号及来源，设 $h=\log\theta_1$，$D_z=(2\pi i)^{-1}\partial_z$。
Jacobi heat equation $4\pi i\,\partial_\tau\theta_1=\partial_z^2\theta_1$、
$\eta_1/(2\pi i)^2=-E_2/12$ 及 $z=(c\tau+d)/47$ 给
$$
D_\tau e=(E_2/12-X)e-Y/2,\quad
D_z e=E_2/12-X,\quad
D_zX=Y,\quad D_zY=6X^2-E_4/24.
$$
对第一式作 $D_z$、用 Ramanujan 的 $D_\tau E_2$，得到 (1090.16) 的 $X$ 行；
再微分椭圆方程得到 $Y$ 行。
把 holomorphic derivative 换成相同水平 CM 补线的
Shimura–Maass derivative，正好把 $E_2$ 换成 $E_2^*$，
并给前三个完整 Ramanujan 行。
所以 (1090.16) 是由原 theta/Weierstrass 恒等式逐项得到，
不是从未刊表格搬来的一串数值规则。

对 $j=1728$ 的 canonical CM 初值，$A_2=0$：
CM 单位 $i$ 保持补线，而权二特征值是 $-1$，故该值必须为零。
$A_6=0$，$A_4=-48a$。
各 $e(P)$ 的原值由 (1090.5) 给出。
在特征 $q$ 中，以同一形式变量 $v$ 解
$d/dv=(1090.16)$ 到degree $q-2$，每一步只除以
$1,\ldots,q-2$ 和2、3的幂，均为单位。
于是 (1090.2) 的 $[v^{q-2}]$ 连同 (1090.15) 给有限、完全原尺度的 CM 高矩算法。
这一步尚未执行；首个 Hodge 请求只认证 (1090.10)、(1090.9)，不暗中运行4511阶系统。

## 6. 可复核的有限消费者设计

第一请求可固定 $q=4513$，不执行 CM 高矩：

1. 以同一 $\zeta_0=2$ 和 (1090.7) 建立全部非零47标签的 e 展开。
2. 按固定有限前缀取 $\rho=c i+d$，
   $0\le c,d\le23$、$(c,d)\ne(0,0)$，包括纯虚代表；
   $a=1,\ldots,46$。每个 $\rho$ 先按完整
   $N(x)=n\in\mathbf F_{47}^\times$ 的46组分别求两项。
   每组有24个半向量，完整 $x\ne0$ 和是半向量和的2倍。
   两个相位 $\zeta^{an}$、$\zeta^{-an}$ 分别相乘后再相加；
   不把它们合成一个未证明足够的 cosine 子族。
3. 用 (1090.10) 累计实际秩，达到95后停止增加候选。
   若预算内或指定前缀没有达到95，只报告实际完成的秩与范围。
4. 对选出的95个真实候选读取全部23 cusp residues，
   核和为零、秩22及73维核。
5. 初次请求明确不运行835阶 Hecke 坐标桥或4511阶 CM 系统。
   后继新请求可按 (1090.11) 构造原 $T_2,T_3,T_5$ 与 $H_2$，
   或按 (1090.16) 读取实际 CM 高矩；它们各自有明确预算和范围。

任何数值步骤只能在审过的专用公开 Actions 请求执行；
本文件没有报告这些步骤已执行。
后继 CM 高矩、实际 Mordell–Weil 饱和和高度仍有各自输入，
原八盘唯一性及全素数主目标继续开放。

## 7. 原始来源

- K. Khuri–Makdisi, *Moduli interpretation of Eisenstein series*,
  Int. J. Number Theory **8** (2012), 715–748；
  Corollary3.13、Remark3.14、Theorem5.1；
  [作者预印本 v6](https://arxiv.org/pdf/0903.1439)。
  Theorem5.1 只用于解释 complex 来源，不用它冒充模4513的整张成证明。
- D. Zywina, *Explicit open images for elliptic curves over Q*，
  §4.7, Theorem4.9、Corollaries4.10–4.11 及式(4.8)；
  [作者全文](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)。
  该 Reynolds 恒等式的本题两 coset 形式已在 §1 直接核准。
- N. Katz, *Serre–Tate local moduli*, LNM **868** (1981), 138–202；
  Main Theorems3.7.1–2（印刷166–167页）、4.3.1–2；
  [作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)。
- R1067 原 good model；R1078/R1080 原 genus及完整空间；
  R1081 原整 Hecke 代数；R1085 原 ordinary CM 完整高矩；
  R1089 原 $(B)_{283},(B)_{4513}$。
- R1091 后继已把 Gaussian 情形的 (1090.14) 化为一个实际短模型的
  系数式，保留相同 $B_q$、KS、原 e 值与 period。
- Jaswal 的未刊平方水平构造仅提示寻找候选的方向。
  本文使用完整原 Reynolds 族，而不依赖那个公式的排版或数值结论；
  full47 下降、整性、全23 residues、168 jet 及 (1090.15)
  均已分别给出原来源证明。
