# R551 — 原 Norm5 两态核心、保 Y 的完整单位逆与两步混合返回

日期：2026-11-14。**状态：已证明。** 在 R544 的同一个
\((\rho_0,\eta)\) 两态上，原 \(R=c+2d_0,\ Q=2c-d_0\)
两轴具有完整核心 \(\chi_{65}\lambda\mathsf B\)，
其中 \(\mathsf B=-\mathsf R_0\)。
这个结论保全部四个共有 σ 与另一输出，不仅作用于原第一边际。
现有射线已经足够，没有新增模 \(25\) 条件。

因为 \(Q\) 正交于原 \(Y\)，这给一个保原 \(Y\) 权的、作用于
全部连续两态测试的整单位逆；不是只对有限个多项式矩有效。
原 \(c\) 核与该 \(Q\) 核两步就返回原两态的共同标量，
但物理矩阵和逐步归一域完整保留。原 \(W\) 的变化不被删除。

## 1. 原来源与 Norm5 的真正联合

使用 R539、R541、R544 的原六输入及同一普通周期：
\[
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\eta=\omega^2H_*\rho_0,\quad
\lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad\kappa=p\lambda^2.
\]
\(H\) 只作用于 \((c,d_0)\)，是 R541/R544 的同一个酉矩阵。
令
\[
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,
\quad Y=A+c+2d_0,\quad W=A+3\delta c+4d_0.
\]
定义
\[
\boxed{R=c+2d_0,\qquad Q=2c-d_0.}
\tag{1}
\]
两行正交、范数五、行列式 \(-5\)，且
\[
c=(R+2Q)/5,\qquad d_0=(2R-Q)/5.
\tag{2}
\]
它是当前普通处的整自同构。四个共有 σ 始终独立保留。

原双 σ 的整个生成来源是
\[
F_5(r,q)=\sigma(r+2q)\sigma(2r-q)
\in\mathcal S_5\otimes\mathcal S_5.
\tag{3}
\]
交叉 Gaussian 为零；每轴一个奇 CM 系数、一个偶系数，
所以两轴均为标准 odd 半特征，而非标准 even 格。

为显示这个完整联合，设
\[
D=-xy\sigma^5,\quad U_1=x^2\sigma^5,\quad
U_2=-y\sigma^5,\quad U_3=x\sigma^5,\quad U_5=\sigma^5,
\]
其中 \(y=\wp'/2\)，这些 \(U_j\) 不与 R533 的六度 \(f_j\) 混用。
它们的 \(\mu_6\) 型分别是 \(0,1,2,3,5\)，首项依次为
\(1,z,z^2,z^3,z^5\)。
整个型二张量空间只容许以下五项，准确为
\[
\boxed{
F_5=2U_2\otimes D-2D\otimes U_2+3U_1\otimes U_1
+6b(U_3\otimes U_5+U_5\otimes U_3).
}
\tag{4}
\]
证明：总二阶是 \(2r^2+3rq-2q^2\)；
\(\sigma(z)=z+bz^7/210+\cdots\) 给总八阶的
\(r^3q^5,r^5q^3\) 系数均为 \(6b\)，\(r^4q^4\) 系数零。
型与完整五维空间已经排除了其他项，故这确定全函数。
等价地，\(0\le i,j\le5\) 的完整矩形 jet 中只有总阶二和八；
degree5 截面不能有六阶零。附证书保全部这些系数。

只对 \(Q\) 作 principal 平均，(4) 退化为
\[
\Pi_{0,Q}F_5=\sigma(r)\sigma(2r)\,D(q),\qquad D(0)=1.
\tag{5}
\]
这是 R370 的原 pair 身份在 (1) 的符号下的准确重写。

## 2. whole degree20 核的绝对定标

现有射线给
\[
g_\pi=\pi_0/\bar\pi_0\equiv3\pmod8,\qquad
g_\pi\equiv1\pmod5,
\]
所以
\[
\boxed{g_\pi\equiv11\pmod{40}.}
\tag{6}
\]
没有将模五提升为模二十五。

R370 已付整个 odd \(\mathcal S_5\) 的标量核心；
R504/R513 通过非零固定拉回
\([\gamma_{13}]^*\mathcal S_5\subset\mathcal S_{65}\)
绝对识别了同一个符号：
\[
K_5=\chi_{65}I,\qquad \chi_{65}\in\{\pm1\}.
\tag{7}
\]
实际深限制另带外部因子 \(\lambda\)。
不需要知道这个真实符号在所有素数上是否相同。

在标准 even \(\mathcal S_{20}\) 的 canonical Schrödinger 基
\(e_j,\ j\in\mathbb Z/20\)，完整二挠平移是
\[
\mathsf T_{(s+r\omega)/2}^{(20)}e_j
=(-1)^{s(j+5r)}e_{j+10r},\qquad s,r\in\{0,1\}.
\tag{8}
\]
这是含中心的 Weyl lift；来自半周期的指数和标准 even 半特征，
不是只指定 projective 交换子。
令
\[
\epsilon(t)=\chi_\sigma(2t)=
\begin{cases}1&t=0,\\-1&t\ne0,\end{cases}
\quad
P_\epsilon=\frac14\sum_{t\in E[2]}\epsilon(t)\mathsf T_t^{(20)}.
\]
写 \(De_j=(-1)^je_j\)、\(Xe_j=e_{j+10}\)，(8) 给
\[
P_\epsilon=\frac14(I-D)(I-X),\quad
\boxed{B_{20}=2P_\epsilon-I,\qquad B_{20}e_j=-e_{11j}.}
\tag{9}
\]
\(P_\epsilon\) 的像为五维，恰是原
\([2]^*\mathcal S_5\)；非零二挠上的特征是 \(\epsilon(t)\)。
特别 \(B_{20}\) 在这个真实子空间上为 \(+I\)。

排列 \(j\mapsto11j\) 把完整 Heisenberg 两生成元都送到其
第十一幂。中心没有残余相位，因为
\[
11^2=121\equiv1\pmod{40}.
\]
所以 (6)、(8)–(9) 与实际普通 core 实现同一个**完整**交织，
Schur 引理使二者仅差标量。在非零的
\([2]^*\mathcal S_5\) 上，core 与普通单位倍点严格交换，
(7) 确定该标量恰为 \(\chi_{65}\)。于是
\[
\boxed{K_{20}=\chi_{65}B_{20}\quad\text{于整个 }\mathcal S_{20}.}
\tag{10}
\]
这同时支付绝对符号、整个空间和全部 tame，而非从一条边际猜矩阵。

## 3. 二挠平均在原整个两态上的准确作用

R544 的原两态在共同 raw \([2]\) 覆盖后位于
\(\mathcal S_4\otimes\mathcal S_4\)。将 (1) 的整个生成框架代入，
两轴都位于 \(\mathcal S_{20}\)，交叉仍为零；
(10) 因而可保另一轴及四个共有 σ 使用。

在共同覆盖中沿 \(Q\) 平移 \(t\in E[2]\)，原 \(c,d_0\)
生成变量分别平移 \(2t,-t\)。
标准 even \(\mathcal S_4\) 的完整整周期平移为一，
而二挠的 \(-t\) 与 \(t\) 是同一个 canonical lift。
所以 (9) 的 \(P_\epsilon\) 沿 \(Q\) 准确等于原 \(d_0\) 轴的
\(\epsilon\)-加权平均。沿 \(R\) 则等于原 \(c\) 轴的同一平均。

在原 \(\mathcal S_4\) 中，(8) 的四维版本给
\[
\frac14\sum_{t\in E[2]}\epsilon(t)\mathsf T_t^{(4)}
=\frac{I-\mathcal R}{2}.
\tag{11}
\]
R544 已付
\[
(R_c)_*\rho_0=-\rho_0,\qquad
(R_c)_*\eta=\rho_0+\eta.
\tag{12}
\]
两个来源在 \(c,d_0\) 同时变号下固定，所以
\(R_{d_0}\) 与 \(R_c\) 在整个两态上相同。
由 (11)–(12)，两个轴分别都满足
\[
P_{\epsilon,Q}\rho_0=P_{\epsilon,R}\rho_0=\rho_0,\qquad
P_{\epsilon,Q}\eta=P_{\epsilon,R}\eta=-\rho_0/2.
\tag{13}
\]
结合 (9)–(10)，在有序来源基 \((\rho_0,\eta)\) 中置
\[
\boxed{
\mathsf B=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}
=-\mathsf R_0,\qquad \mathsf B^2=I.
}
\tag{14}
\]
这里矩阵的列表示每个来源的像。若
\(P_{Q,t}=I+(t-1)\bar Q^{\,t}Q/5\)，\(P_{R,t}\) 同理，
对 \(r,s\ge0\) 的完整测度式为
\[
\boxed{
\mu|_{\{Q\in p^r,\ R\in p^s\}}
=(\chi_{65}\lambda)^{r+s}
(P_{Q,\kappa^r}P_{R,\kappa^s})_*\mathsf B^{r+s}\mu,
\quad\mu\in\langle\rho_0,\eta\rangle .
}
\tag{15}
\]
尤其
\[
\rho_0|_{Q\in p}=\chi_{65}\lambda(P_{Q,\kappa})_*\rho_0,
\]
\[
\eta|_{Q\in p}
=-\chi_{65}\lambda(P_{Q,\kappa})_*(\rho_0+\eta).
\tag{16}
\]
\(R\) 轴同样成立。双轴共同深系数是 \(\lambda^{2n}\)，
与原两个独立 σ 同深完全相容。

还可用原实际 \(H\) 共轭。对
\(Q_j=QH^{-j}, R_j=RH^{-j}\)，来源矩阵准确为
\(\mathsf B_j=-\mathsf R_j\)，其中 \(\mathsf R_j\) 是 R544 的
三个真实反射矩阵。这个结论从已付 whole 身份共轭得到，
无需另在更大覆盖上猜一个 scalar 核。

## 4. 保原 Y 的全部连续两态测试整逆

以下在真正整坐标
\((\xi_1,\xi_2,\xi_3,x,R,Q)\in\mathbb Z_p^6\) 上工作。
令
\[
a=\chi_{65}\lambda,\qquad
(\mathcal S f)(\xi,R,Q)=f(\xi,R,\kappa Q).
\]
对两分量测试列 \(f=(f_0,f_\eta)^t\)，约定
\[
\langle f,\boldsymbol\rho\rangle
=\int f_0\,d\rho_0+\int f_\eta\,d\eta .
\]
由 (16) 逐项展开，而不省略非齐次项，准确有
\[
\boxed{
\langle g,\boldsymbol\rho|_{Q\ {\rm unit}}\rangle
=\langle (I-a\mathsf B\mathcal S)g,\boldsymbol\rho\rangle.
}
\tag{17}
\]
例如深域上两分量变为
\(a(g_0\circ P_Q-g_\eta\circ P_Q,\,-g_\eta\circ P_Q)\)，
这固定了 (17) 的转置约定。

**引理。** \(1-a\)、\(1+a\)、\(1-a^2\) 都是当前处的单位。

若其中一个一次因子非单位，则
\(\bar\pi_0\equiv\pm1\pmod{\mathfrak p}\)。
因 \(\pi_0\equiv0\bmod\mathfrak p\)，实际整数迹
\(A_0=\pi_0+\bar\pi_0\) 也满足 \(A_0\equiv\pm1\bmod p\)。
原 primary 条件给 \(A_0\) 偶，且 \(|A_0|\le2\sqrt p<p-1\)，
迫 \(A_0=\pm1\)，矛盾。该论证同时处理两个实际 \(\chi_{65}\) 号。

给任意整连续测试 \(f\)，定义
\[
f^{(0)}(\xi,R,Q)=f(\xi,R,0),\qquad f^+=f-f^{(0)}.
\]
完整逆为
\[
\boxed{
\mathcal U_Q f=
\frac{I+a\mathsf B}{1-a^2}f^{(0)}
+\sum_{n=0}^{\infty}a^n\mathsf B^n\mathcal S^n f^+.
}
\tag{18}
\]
因为 \(\kappa\in p\mathcal O^\times\)，连续函数的一致连续性给
\(\|\mathcal S^n f^+\|_\infty\to0\)。
故该级数在**测试函数一致范数**中收敛，所有系数整，
\(\|\mathcal U_Q f\|_\infty\le\|f\|_\infty\)。
不声称测度范数收敛，也不要求 \(a\) 的绝对值小于一。

有限部分和的望远镜与常数项直接证明
\[
(I-a\mathsf B\mathcal S)\mathcal U_Qf=f.
\]
代入 (17)，得到整个两态的真实单位返回
\[
\boxed{
\langle\mathcal U_Qf,\boldsymbol\rho|_{Q\ {\rm unit}}\rangle
=\langle f,\boldsymbol\rho\rangle
\quad\text{对所有整连续 }f.
}
\tag{19}
\]
这包含任意紧开测试和全部隐藏输入。
若 \(f=\sum_{j=0}^m f_j(\xi,R)Q^j\) 是有限多项式，(18) 直接成为
\[
\boxed{
\mathcal U_Qf
=\sum_{j=0}^m
\frac{I+a\kappa^j\mathsf B}{1-a^2\kappa^{2j}}f_jQ^j.
}
\tag{20}
\]
所有分母均为单位，\(j=0\) 由引理，\(j>0\) 因 \(\kappa\) 为深。

关键是 \(Y=A+R\) 不依赖 \(Q\)。
因此 (18) 与原 \(1_{Y\ {\rm unit}}\langle Y\rangle^{du}\)
严格交换，原中央的尺度和单位观察不移动。
对 R536 的原完整 \(q_n\)，取
\(f=(q_n,0)^t\)，(19) 给一个只在 \(Q\)-unit 上积分的、
依旧准确返回 \(\beta^nJ_S(u)\) 的整连续测试。
这里真实替换的是 \(q_n\)，并没有断言它原来被 \(Q\) 缩放固定。
同一构造可保 R546 允许的其他独立伴随测试；
混合 CM 投影若要交换，仍须其完整分支证明。

对仅 \(\eta\) 分量、且不依赖 \(Q\) 的测试 \(h\)，(18) 特别是
\[
\mathcal U_Q(0,h)^t
=\left(-\frac{a}{1-a^2}h,\frac1{1+a}h\right)^t.
\tag{21}
\]
原 \(\rho_0\) 补偿项在这里不可丢掉。

## 5. 原 W 的准确移动和全部 log 项

(1)–(2) 给
\[
\boxed{
W=A+\frac{8+3\delta}{5}R+\frac{6\delta-4}{5}Q.
}
\tag{22}
\]
所以 \(Q\) 缩放下 \(Y\) 固定，但
\[
W\circ P_{Q,t}
=W+\frac{6\delta-4}{5}(t-1)Q.
\tag{23}
\]
例如每个 \(n\) 在 (18) 中的真实单位条件必须是
\[
A+\frac{8+3\delta}{5}R+
 \frac{6\delta-4}{5}\kappa^nQ\in\mathbb Z_p^\times,
\tag{24}
\]
其 logarithm 也用同一个表达。
(19) 对包括 \(W\)-unit、log \(W\) 或 R544 \(\Phi_j\) 的连续测试
仍完全成立，但它生成的是 (24) 的全部实际测试族，
不能把它们改回未移动的原 \(W\)。

对 \(u\)-依赖测试，(18) 按完整测试施加；
求导须同时保测试本身的质量、log 和 \(\rho_0/\eta\) 混合项。
尤其不能从 (19) 的整逆推断 R544 的唯一余域或 \(\eta\) 行已为零。

## 6. 两步就返回整个两态的真实混合词

R544 的原 \(c\) 核是 \(\lambda\mathsf R_0\)。
(14) 使它与 \(Q\) 核的来源矩阵乘积为
\[
\mathsf B\mathsf R_0=-I.
\]
先要求 \(c\in p\)，将实际坐标按 \(P_{c,\kappa^{-1}}\) 归一，
再要求新坐标的 \(Q\in p\)。对应实际域为
\(\mathcal A\mathbb Z_p^6\)，其中前四输入固定，后两输入矩阵为
\[
\boxed{
\mathcal A=P_{c,\kappa}P_{Q,\kappa}
=\frac15
\begin{pmatrix}
\kappa+4\kappa^2&2\kappa-2\kappa^2\\
2-2\kappa&4+\kappa
\end{pmatrix}.
}
\tag{25}
\]
所以对原整个两态，
\[
\boxed{
\mu|_{\mathcal A\mathbb Z_p^6}
=-\chi_{65}\lambda^2\,\mathcal A_*\mu.
}
\tag{26}
\]
同样可迭代任意 \(m\)：
域是 \(\mathcal A^m\mathbb Z_p^6\)，系数
\((-\chi_{65}\lambda^2)^m\)。
这不是 raw \(c,Q\) 独立深的矩形。

真实矩阵满足
\[
\det\mathcal A=\kappa^2,\qquad
\operatorname{tr}\mathcal A=(4+2\kappa+4\kappa^2)/5
\equiv4/5\pmod p.
\tag{27}
\]
因而它绝不是共同深一层的标量缩放。

令 \(q_{\mathcal A}=q_n\circ\mathcal A^{-1}\)、
\(Y_{\mathcal A}=Y\circ\mathcal A^{-1}\)、
\(W_{\mathcal A}=W\circ\mathcal A^{-1}\)，都只在实际像格上使用。
原两条完整函数精确返回
\[
\int_{\mathcal A\mathbb Z_p^6,\ Y_{\mathcal A}\ {\rm unit}}
\langle Y_{\mathcal A}\rangle^{du}q_{\mathcal A}\,d\rho_0
=-\chi_{65}\lambda^2\beta^nJ_S(u),
\]
\[
\int_{\mathcal A\mathbb Z_p^6,\ W_{\mathcal A}\ {\rm unit}}
\langle W_{\mathcal A}\rangle^{du}q_{\mathcal A}\,d\rho_0
=-6\delta\chi_{65}\lambda^2\beta^nJ_T(u).
\tag{28}
\]
所有原输入条件和补域均按同一 \(\mathcal A\) 运输。
(26) 对 \(\eta\) 也成立，但若调用其算术投影，
仍保 R546 的 CM 操作及其真实转置域。

## 7. 当前连接范围

本篇给了原同一两态中的新完整 Norm5 核、保原 \(Y\) 的全部
连续测试整逆，以及比原六步词更短的两步来源返回。
核心符号与旧 \(\chi_{65}\) 严格相同，未新增射线或算术来源。

原三条秩二曲线中央只通过已付的实际行使用。
R544 的唯一全单位余域、\(\eta(\Phi_1-\Phi_2)\)、
R546 的参考和十二外谱仍须完整联立。
(18) 可合法重写这些测试，却不凭整逆本身赋其中央零。
固定曲线和无穷不同 \(p\) 的主目标尚未完成。

## 依赖与证书

- [R370：原 degree5 完整核心与真实 pair](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)。
- [R513：同一个 odd5/65 绝对符号](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R544：原两态 S3、whole degree4 和真实词域](R544-original-s3-and-exact-mixed-unit-complement.md)。
- [R546：原第三支的完整五伴随算术行](R546-original-third-sigma-full-five-companion-cm-transfer.md)。
- [精确证书脚本](../scripts/check-r551-norm5-two-state-unit-inverse.mjs)。
- [完整有限输出](../scripts/check-r551-norm5-two-state-unit-inverse.json)。

有限证书已在当前 JavaScript 环境执行，逐项支付 degree20
canonical 二挠矩阵、\(B=-U_{11}\)、全部中心、原 odd5 锚及
五项联合的完整矩形系数。连续逆与实际域由正文证明；
没有另加独立复跑或数值非消失推断。
