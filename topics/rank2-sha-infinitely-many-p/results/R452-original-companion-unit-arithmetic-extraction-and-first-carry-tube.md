# R452 — 真 U 单位域中的算术抽回与第一层 carry 非零管

日期：2026-11-14。**状态：已证明。** R450 的六条正 $U$ 次数来源
在真正的 $U$ 单位域上仍整满秩。由此得到三个完全指定、可计算且
整的测试：它们支持于 $U$ 单位，完整抽回同一原 $S$ 和两个已识别
的秩零参考。原 $S$ 测试与 R450 的测试只差 $p\mathcal O$，
但新的 $\log c$ 质量修正并未被省略。

在 R441、R448 的原同深域上，新的原 $S$ 测试仍对每个正偶数
$n$ 给准确赋值 $5n$。用保原 sigma 的完整核心，这个非零值可以
送到反射来源 $\Psi_0$ 的第一层单位 carry 中；该整个 carry 的
同一个中央恰为 $\lambda J'_S$。本文始终保留其内部斜管补域，
不从一个非零管推出完整算术中央非零。

## 1. 同一个来源格和两组完整六列

保持 R439、R445、R448、R450 的原固定 ray、$b=17$、原周期
$\Omega$、$\lambda=-\bar\pi_0^{-1}$、$\kappa=p/\bar\pi_0^2$、
$\eta=\eta_{5,p}\in\{\pm1\}$。仍有 $p>19$、$p\equiv7\pmod{64}$。
所有测试使用原物理输出
$$
Y=c+Z,\quad X=-c+H,\quad Q=9Z-17H,\quad
W=Z+H,\quad A=Q+26c,\quad U=Q-280c.
\tag{1}
$$

R448 的两个实际三变量来源为
$$
\boxed{\Phi_i(y,v,u)=
\sigma(y-v-280u)\sigma(y+v-8u)
 A_i(y+9u,v-17u),\qquad i=0,1.}
\tag{2}
$$
这里 $A_0=G_{16}R_{16,16}$，而
$$
A_1=\frac18\sum_{t\in E[4]}
          (T_t^{(32)}\otimes T_{-t}^{(16)})A_0
\tag{3}
$$
是 R443 的完整固定来源；它的全部有理多项式、偶偶与奇奇项均已
指定。没有另选一个只具相同边际的第二来源。

对于 $1\le j\le6$，定义整条第一输出来源
$$
\nu_{T_{i,j,b}}=(Y)_*
  \{(X/\Omega)^{6-j}(U/\Omega)^j\nu_{\Phi_i}\}.
\tag{4}
$$
两个原来源在同时 $\mu_6$ 旋转下的型为零，测试总次数为六，
所以 (4) **整个**属于第一轴的型零空间，而不混入另一个 tame 型。
写其完整系数为
$$
\boxed{T_{i,j,b}(y)=\sigma(y)^{34}
 \sum_{a=0}^5 M^{(i)}_{aj}\,b^{5-a}x(y)^{2+3a}.}
\tag{5}
$$
令 $M_i=(M^{(i)}_{aj})_{0\le a\le5,1\le j\le6}$。
$M_0$ 就是 R450 的显式 $M_+$。

为使 $M_1$ 的定义无任何未定常数，在 $b=1$ 时，它的第 $j$ 列
准确为
$$
\boxed{M^{(1)}_{aj}=
[x^{2+3a}]\left\{\sigma(y)^{-34}(6-j)!j!
              [v^{6-j}u^j]\Phi_1(y,v,u)\right\}.}
\tag{6}
$$
将 R443 的 (3) 完整来源代入 (2)，即可用有限椭圆函数环计算
(6)；两个矩阶乘和原周期规范均在式中。它是不依赖 $p$ 的明确
有理矩阵，不是待选择的六条向量。
R448 的整三张量格和 $p>19$ 保证 (5) 的全部矩与原 theta 基
系数都整。因此 $M_1\in M_6(\mathcal O)$，没有为满秩论证
偷加未知的分母假设。

## 2. 限制 U 单位后的准确来源矩阵

R445、R448 的真实 $U$ 核心，保另外两个物理输出，给
$$
\nu_{\Phi_0}|_{U\in p}
=-\eta\lambda[1,1,\kappa]_*\nu_{\Psi_1},
\qquad \Psi_1=R_Y\Phi_1.
\tag{7}
$$
对 (4) 的六次测试，$U$ 缩放贡献 $\kappa^j$。每条
$T_{1,j,b}$ 都是型零、特别为偶函数，所以第一输出反射严格固定
它。由 (7) 从全域减去深域，完整得到
$$
\boxed{
(Y)_*\{\mathbf1_{U\ {\rm unit}}
 (X/\Omega)^{6-j}(U/\Omega)^j\nu_{\Phi_0}\}
=\nu_{\,T_{0,j,b}+\eta\lambda\kappa^jT_{1,j,b}}.}
\tag{8}
$$
这首先是整个第一输出测度的等式，不只是某个 principal 中央值。

置
$$
\boxed{
\Delta_\kappa=\operatorname{diag}(\kappa,\kappa^2,\ldots,\kappa^6),
\qquad B_p=M_0+\eta\lambda M_1\Delta_\kappa.}
\tag{9}
$$
R450 已在当前全部素数处付 $M_0\in\operatorname{GL}_6(\mathcal O)$。
因为 $\Delta_\kappa\in pM_6(\mathcal O)$，严格有
$$
\boxed{B_p\in\operatorname{GL}_6(\mathcal O),\qquad
B_p^{-1}\equiv M_0^{-1}\pmod p.}
\tag{10}
$$
例如将 $M_0^{-1}B_p=I+E_p$，其中 $E_p\in pM_6(\mathcal O)$，
则 $(I+E_p)^{-1}=\sum_{r\ge0}(-E_p)^r$ 整收敛。
实际测试也可直接使用有限的
$\operatorname{adj}(B_p)/\det B_p$；(2)、(3)、(6)、(9) 完整
指定全部输入。因此 (10) 是一个确定的可计算矩阵逆，不依赖
存在性选择或对新增目标素数的数值扫描。

## 3. 支持于 U 单位的三个原算术测试

采用 R450 的三个目标列
$$
s=(-128/7,-80/7,-12/7,-53/7,1,0)^{\mathsf t},
$$
$$
r_3=(-2048,12032,8128,400,-208,1)^{\mathsf t},
\quad r_5=(1024,-6784,-14912,-272,272,1)^{\mathsf t}.
$$
用同一个真实 $\eta,\lambda,\kappa$ 定义
$$
\boxed{
c_{S,p}=B_p^{-1}(s/b),\qquad
c_{3,p}=B_p^{-1}r_3,\qquad c_{5,p}=B_p^{-1}r_5.}
\tag{11}
$$
每个列向量均整，且分别模 $p$ 等于 R450 的相应六项系数。
令
$$
\begin{aligned}
P_{k,p}(\xi,\upsilon)
 &=\sum_{j=1}^6 c_{k,p,j}\xi^{6-j}\upsilon^j,\\
\mathfrak h^\times_{k,p}(X,U)
 &=\mathbf1_{U\ {\rm unit}}
                P_{k,p}(X/\Omega,U/\Omega),\quad k=S,3,5.
\end{aligned}
\tag{12}
$$
这是连续整测试，支持是真正的原 $U$ 单位域。
式 (5)、(8)–(11) 准确给
$$
\boxed{\begin{aligned}
(Y)_*(\mathfrak h^\times_{S,p}\nu_{\Phi_0})&=\nu_S,\\
(Y)_*(\mathfrak h^\times_{3,p}\nu_{\Phi_0})&=\nu_{H_{3,17}},\\
(Y)_*(\mathfrak h^\times_{5,p}\nu_{\Phi_0})&=\nu_{H_{5,17}}.
\end{aligned}}
\tag{13}
$$
故原整条 principal 行以及中央导数分别是
$$
\boxed{\Gamma_0(z;\mathfrak h^\times_{S,p})=J_S(z),
\qquad\Gamma'_0(0;\mathfrak h^\times_{S,p})=J'_S(0),}
\tag{14}
$$
另两条是同一个共周期 $J_{H_{3,17}},J_{H_{5,17}}$。
这给的是三个指定测试的真算术返回；没有把任意 $U$ 测试都赋
相同中央，也没有把两个参考的非零质量当作其导数已知。

## 4. 同一目标深管上的首项稳定，保新的 log 质量

取 R441、R448 的同一域
$$
\mathscr D_n=
\{Z,H\in p^n,c\text{ 单位}\}
=\{X\text{ 单位},W\in p^n,U-280X\in p^n\}.
\tag{15}
$$
这里 $U\equiv-280c\pmod p$，所以 $U$ 自动为单位。
在 $\mathscr D_n$ 上，(12) 的指标函数恒为一。

为保留全部法向项，记以下两个准确整数行：
$$
\boxed{\begin{aligned}
\alpha={}&(-29272,-5132872,-898806472,-171811015456,
                -38394575430400,-8989226826496000),\\
\beta={}&(0,2592,462672,-28817856,1145664000,-32223744000).
\end{aligned}}
\tag{16}
$$
它们由 R450 的同一个 $\mathfrak m_5$ 完整给出：对
$$
q_j(T)=(-1+TH)^{6-j}(-280+T(9Z-17H))^j,
$$
准确有
$$
\alpha_j=\mathfrak m_5([T^5]\log(1+TZ)q_j),\qquad
\beta_j=\mathfrak m_5([T^5]q_j).
\tag{17}
$$
因此它们已经包括每个法向 Taylor 项及其阶乘。
特别 $\beta$ 就是 R450 的 $M_0$ 的原点质量行。

对 (12) 的 $S$ 测试，令 $\mathcal A_{S,p}^{\times}(T)$ 为
R450 式 (26) 中将 $h_S$ 换成多项式 $P_{S,p}$ 的同一完整函数。
在 $T\in p\mathcal O$、$c$ 单位时，$U=-280c+T(9Z-17H)$
始终为单位，所以这个函数准确读取 (15) 的实际测试。

写
$$
I_1=\int_{c\ {\rm unit}}c\,d\nu_\sigma,
\qquad I_{1,\log}=\int_{c\ {\rm unit}}
                         c\log_p\langle c\rangle\,d\nu_\sigma.
$$
原 $I_1=(1-\lambda_\sigma\kappa)\Omega$，而
$I_{1,\log}\in p\mathcal O$。完整五阶系数为
$$
\boxed{[T^5]\mathcal A_{S,p}^{\times}
=\frac d\Omega\{(\alpha c_{S,p})I_1+
                         (\beta c_{S,p})I_{1,\log}\}.}
\tag{18}
$$
这里不能沿用 R450 的 $\log c$ 项整条为零。
实际质量由 (9)、(11) 准确给出
$$
\boxed{
\beta c_{S,p}=-\eta\lambda\,
 e_6^{\mathsf t}M_1\Delta_\kappa c_{S,p}\in p\mathcal O.}
\tag{19}
$$
它一般未被赋为零，只因 (19) 和 $I_{1,\log}\in p\mathcal O$
而在 (18) 中属于 $p^2\mathcal O$。

另一方面，由 (10)、(11) 以及 R450 的全首项，
$$
\alpha c_{S,p}\equiv\frac{\alpha_S}{b}\pmod p,
\qquad
\alpha_S=-\frac{480763982085139011763}{107052528108059628480}
\in\mathcal O^\times.
\tag{20}
$$
所以 (18) 是单位。原残余的总次数低于五的矩仍全部为零；
测试仍为六次、系数整，R450 的完整高尾估计
$v_p([T^k]\mathcal A)\ge-\lfloor\log_pk\rfloor$ 原样适用。
于是对每个正偶数 $n$，同一真实域的值严格满足
$$
\boxed{\begin{aligned}
\mathcal C^{\times}_{S,n}
&:=\int_{\mathscr D_n}d\log_p\langle Y\rangle
                  \mathfrak h^\times_{S,p}(X,U)\,d\nu_{\Phi_0}\\
&=\lambda^{2n}\mathcal A_{S,p}^{\times}(\kappa^n),\qquad
v_p(\mathcal C^{\times}_{S,n})=5n.
\end{aligned}}
\tag{21}
$$
此外 $P_{S,p}(\xi,280\xi)\equiv h_S(\xi,280\xi)\pmod p$，
所以 R450 的斜线单位也保留。式 (18) 才是 (21) 的充分证明；
仅知道斜线上的值不足以支付同阶法向贡献。

## 5. 真第一层单位 carry 的同一个算术测试

因为 (12) 支持于 $U$ 单位，R448 的缩放转置
$\mathcal S h(X,U)=h(X,\kappa U)$ 在这些测试上为零。
故对于 $\Phi_0$ 的真实第一层单位 carry，完整有
$$
\boxed{B_0(z;\mathfrak h^\times_{S,p})=\lambda J_S(z).}
\tag{22}
$$
这不再需要用第二条未知来源的中央行消元。

为让已知非零管也进入同一层，保 R445 的真实反射来源
$\Psi_i=K_A\Phi_i=R_Y\Phi_i$。在同一个 $(W,Q,c)$ 坐标域
$$
\mathscr B=\{A\in p,Q,c\text{ 都单位}\}
=\{A\in p,U\text{ 单位}\}
$$
中，令 $\widetilde{\mathfrak b}_i^U$ 是 $\nu_{\Psi_i}$ 限制后的
$(W,A/\kappa,U)$ 推前。R445 的四态完整核心给
$$
\boxed{\widetilde{\mathfrak b}_i^U
=\lambda\nu_{\Phi_i}
   +\eta\lambda^2[1,1,\kappa]_*\nu_{\Psi_{1-i}}.}
\tag{23}
$$
这由 $A$ 深减去 $A,U$ 同深得到，不要求 $\Psi_i$ 另有原
$\sigma\otimes\mathcal L_i$ 的乘积分解。
在任何 $U$ 单位测试下，(23) 的第二项准确为零，因而
$$
\boxed{\widetilde B_0(z;\mathfrak h^\times_{S,p})
=\lambda J_S(z).}
\tag{24}
$$

现在将 (15) 用 $A\mapsto\kappa A$ 的真实 $A$ 核心送入
$\Psi_0$。所得的实际域是
$$
\boxed{\mathscr E_n=
\left\{W\in p^n,\ A\in p,\
 140A/\kappa+13U\in p^n,\
 A/\kappa-U\text{ 单位}\right\}.}
\tag{25}
$$
在此处 $U,Q,c$ 都为单位，而且 $v_p(A)=1$，故
$\mathscr E_n\subset\mathscr B$。只在确实深的 $A$ 上使用
$\widetilde A=A/\kappa$，规范物理输出是
$$
Y'=(17W+\widetilde A)/26,\qquad
X'=(9W-\widetilde A)/26.
$$
真实核心限制式准确为
$$
\nu_{\Psi_0}|_{\mathscr E_n}
=\lambda[1,\kappa,1]_*\left(\nu_{\Phi_0}|_{\mathscr D_n}\right).
\tag{26}
$$
同一个规范测试在 (25) 的中央值因此是
$$
\boxed{
\lambda\mathcal C^{\times}_{S,n},\qquad
v_p(\lambda\mathcal C^{\times}_{S,n})=5n.}
\tag{27}
$$
整个 (24) 的中央却仍必须保精确分拆
$$
\boxed{\lambda J'_S(0)
=\lambda\mathcal C^{\times}_{S,n}
 +\widetilde B'_{0,\,\mathscr B\setminus\mathscr E_n}
                      (\mathfrak h^\times_{S,p}).}
\tag{28}
$$
这已把原算术行与非零深管放在同一个保 $U$ 的第一层实际 carry
测试中。剩余缺口就是 (28) 的真实内部补域；不是另一个未识别
来源，也不能由“测试合法”改写成该补域或子域已知为零。

## 依赖与完整输入

- [R450：七列、整满秩、三条原算术测试与全部同深首项](R450-original-sixth-companion-moments-and-exact-arithmetic-extraction.md)。
- [R443：第二来源 A1 的全部精确 theta 多项式](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R445：同一保 sigma 的四态与所有独立深度](R445-original-sigma-retained-three-coordinate-core-and-four-state-carry.md)。
- [R448：保 U 的物理反射、完整 principal 行与真实目标管](R448-original-retained-companion-reflection-and-joint-principal-carry.md)。
- [R441：原残余的真实五阶矩与严格高尾估计](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。

(6) 的实际有理矩阵也见
[三态六次矩的完整数据](../scripts/check-three-state-fixed-u-degree-six.json)
中的 `M1` 六条正 $U$ 次数列；本篇满秩证明只用该已确定来源的
整性，不依赖新跑一次有限秩计算。
