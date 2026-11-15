# R356：原第四成本最低两整权的完整 self 结构与总通量恒零

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、原根恢复、符号消元、秩计算、人工测试或科学运行。**

[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 已把总通量的真实 Green 修正写成原 $U/\mathcal R$ 上不依赖辅助右包的读出 $\Lambda_u$。[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 支付了三个加速度平方正规族，但没有支付其余正规生成元。

本稿直接消费 [R203](R203-general-pure-lowest-two-weights-vanish.md) 从原 R56 推得的一般动态双线性式，完整计算 self 通道的最低两层。与 R203 的 pure 消去不同，这里保留非零的 self 左尾。得到
$$
\boxed{\Sigma(U_{-9})=0,\qquad
\Omega_u(U_{-8})=0,\qquad
\Lambda_u(U_{-9}+U_{-8})=0.}
\tag{1}
$$
这里 $\Sigma_V(u)=V(u^2,0)$，$\Omega_u(V)=\int u'''\Sigma_V(u)$。更精确地，权 $-8$ 的整个 self 输出落在下文两个明确模板的跨度内。本文不声称这个跨度就是实际像，也不声称 $U_{-8}=0$ 或 $U_{-8}\subseteq\mathcal R$。

## 1. 原对象、共同锚与两个模板

$U$ 是 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 定义的真实完整 canonical 第四成本线性空间。所有输入、原函数和沿 $s$ 的 histories 保持原共同锚。对
$$
u\in C_c^\infty((\ell,r_*)),\qquad
J(F)(x)=\int_x^{r_*}F(t)\,dt,
$$
写
$$
v=u',\qquad r=u'',\qquad t=u'''=r'.
\tag{2}
$$
中间输出允许有真实左尾；$J^2$ 是同一个 $J$ 的两次组成。

定义
$$
\mathcal T_R(u)
=4J^2(r^2t^2)-4J(vrt^2)-r^4,\qquad
\mathcal C(u)=r^4.
\tag{3}
$$
它们都是原 universal profile 代数中的四次齐次函数。两者的真仿射权均为 $-8$：每次 profile 微分降一权，每个右原函数升一权。没有给它们额外的左端积分常数。

本稿的完整 self 结构结论是
$$
\boxed{
\Sigma(U_{-8})
\subseteq\operatorname{span}_{\mathbb R}
\{\mathcal T_R,\mathcal C\}.}
\tag{4}
$$
式 (4) 是整个输出函数的包含关系，不是有限节点、单个 profile 或仅左尾的结论。

## 2. 从完整原恢复中取最低两层

固定一条真实有限路径 $B$，同 scalar 常值端口、frame $I\to I$，并满足原二阶矩阵 $M_B=0$。不要求先把第三算子 $T_B$ 置零；R105 第 5 节已证明这类成本的线性跨度仍是 $U$。

先取真实合法的右端 $c$，使整条路径上 $c+\omega(s)>0$ 有正间隙；置
$$
\xi=c+\epsilon x,\qquad \epsilon>0,\qquad x\le0.
$$
在固定的右零 profile 区间上计算。最后才按第 7 节从局部窄化转回真整权。下列几何系数均先在原 $\xi$ 变量求导，再在 $\xi=c$ 取值：
$$
z=\xi+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad\lambda=e_s/h^2,
$$
$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad K=K_0+\lambda_s,
$$
$$
f_g=\frac{Q}{8h^2},\qquad
C_g=\frac{KQ}{8h},\qquad D_g=\frac{Ke}{4}.
\tag{5}
$$
始终使用原水平关系 $\omega_s=k_s/(2h)$。

沿 R203 的原双线性算子
$$
P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xP(a,b),\qquad
S(a,b)=J(xa''b''),
\tag{6}
$$
记
$$
\mathscr Q_s=(\partial_\xi C_g-D_g)R+D_gS.
\tag{7}
$$
这里下标 $s$ 表示随真实路径变化的系数，不是对整个算子再求一次导数。

对一般动态、共同右零输入 $\phi,\chi$，R203(11)–(13) 已从 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的完整分子公式证明
$$
\psi_s
=\epsilon^{-3}C_gP(\phi,\chi)
+\epsilon^{-2}\{\mathscr Q_s(\phi,\chi)+\mathscr L(\phi,\chi)\}
+O(\epsilon^{-1}),
\tag{8}
$$
其中
$$
\mathscr L(\phi,\chi)=
J^2\!\left[
2f_g\phi_s''\chi_s''
-\bigl((f_g\phi_s)_s\bigr)'\chi'''
-\phi'''\bigl((f_g\chi_s)_s\bigr)'
\right].
\tag{9}
$$
正交 scalar $\psi$ 与原 scalar $W$ 的次层规范差是
$$
\mathscr E(\phi,\chi)=
-\frac{(f_g)_s}{2}\phi'\chi'
-f_gJ^2(\phi_s'\chi'''+\phi'''\chi_s').
\tag{10}
$$
R203 第 4 节同时证明，真实恢复场的正交余分子对下一 forcing 的贡献比这里两层再高一阶。因此下面可以在准确截断内使用 $-Y_\psi$，并没有把完整余场从原理论删除。

## 3. self 通道必须保留二阶 history 的真实导数

令 $Z_u$ 是原 forcing $H(Y_u,Y_u)$ 的 canonical 第二场。其实际正交 scalar 展开为
$$
\psi_2=\epsilon^{-3}bA+\epsilon^{-2}d+O(\epsilon^{-1}),
\qquad A=P(u,u)=J(r^2).
\tag{11}
$$
R203 的原递推给
$$
b_s=C_g,\qquad d_s=\mathscr Q_s(u,u),\qquad
b(0)=0,\quad d(0)=0.
\tag{12}
$$
特别，不能因为初始 $b=0$ 就把 $b_s=C_g$ 设为零。

原二阶矩阵 $M_B=0$ 使整个第二 scalar 的末值为零；R203(33) 因而准确给
$$
b(L)=0.
\tag{13}
$$
下文不需要假设 $d(L)=0$，也不需要删除第三 history。self 通道本身是
$$
\Sigma_{V_B}(u)=-\int_B\mathcal R_{H(Z_u,Z_u)}\,ds.
\tag{14}
$$
它没有 pure 规范中的 $1/16$ 系数，也没有 $Y$–第三场交叉项。

由 (8)，其最低层是
$$
[\epsilon^{-9}]\Sigma_{V_B}
=-P(A,A)\int_0^L C_gb^2\,ds
=-\frac13P(A,A)[b^3]_0^L=0.
\tag{15}
$$
次层完整等于
$$
\begin{aligned}
[\epsilon^{-8}]\Sigma_{V_B}
=-\int_0^L\bigl\{
2C_gbP(A,d)+b^2\mathscr Q_s(A,A)
+\mathscr L(bA,bA)
\bigr\}\,ds.
\end{aligned}
\tag{16}
$$
这里保留了 (9) 对动态输入 $bA$ 的全部项。

还须核原规范差。对 self forcing，(10) 的相应次层为
$$
-\mathscr E(bA,bA)
=\frac{(f_g)_s b^2}{2}(A')^2
+2f_gbC_gJ^2(A'A''').
\tag{17}
$$
它在初、末端都由 $b=0$ 准确消去。原 scalar 与 $\widetilde W=W+\lambda P$ 的差在同 scalar 常值端口也有 $\lambda=0$。故 (15)–(16) 确实是原始 self 成本的两层，而不只是一个重新锚定的正交变量。

## 4. 动态部分留下一个局部四次项

置
$$
M=J^2((A'')^2),\qquad N=J^2(A'A''').
$$
因为 $A'=-r^2$ 且这些原函数在同右 collar 为零，
$$
M+N=\frac{(A')^2}{2}=\frac{r^4}{2}.
\tag{18}
$$
直接把 (12) 代入 (9)，得到
$$
\mathscr L(bA,bA)
=2f_gC_g^2M-2b(f_gC_g)_sN.
\tag{19}
$$
对第二项作真实 $s$ 分部积分。其端项 $[2bf_gC_gN]_0^L$ 由 (12)–(13) 为零，而不是把 $C_g$ 或 $N$ 的端值删掉。因此
$$
\begin{aligned}
-\int_0^L\mathscr L(bA,bA)\,ds
&=-2\int_0^L f_gC_g^2(M+N)\,ds\\
&=-r^4\int_0^L f_gC_g^2\,ds.
\end{aligned}
\tag{20}
$$
这个项通常不为零。R203 在 pure 通道中由第三场的另一个真实端势抵消它；self 通道没有那个交叉项，所以本稿必须保留 (20)。

## 5. 静态部分的完整原函数化简

利用 $d_s=\mathscr Q_s(u,u)$，
$$
\partial_s\{b^2P(A,d)\}
=2bC_gP(A,d)+b^2P(A,\mathscr Q_s(u,u)).
$$
两端 $b=0$，故 (16) 的静态部分为
$$
\int_0^Lb^2
\{P(A,\mathscr Q_s(u,u))-\mathscr Q_s(A,A)\}\,ds.
\tag{21}
$$
这是保留 full outer slot 的真实算子差，不是用纯对角交换子替换它。

现在从原 (6) 直接计算。已有
$$
A'=-r^2,\qquad A''=-2rt,
$$
以及
$$
R(u,u)''=2(v-xr)t,\qquad
S(u,u)''=-r^2-2xrt.
\tag{22}
$$
因此
$$
\begin{aligned}
P(A,R(u,u))-R(A,A)
&=4J(xr^2t^2)-4J(vrt^2)-r^4-4xJ(r^2t^2)\\
&=4J^2(r^2t^2)-4J(vrt^2)-r^4\\
&=\mathcal T_R(u).
\end{aligned}
\tag{23}
$$
这里用的是同锚的准确式 $J(xF)=xJF+J^2F$，没有丢弃左常数。

同样，
$$
\begin{aligned}
P(A,S(u,u))-S(A,A)
&=J(2r^3t+4xr^2t^2)-4J(xr^2t^2)\\
&=2J(r^3t)=-\frac12r^4.
\end{aligned}
\tag{24}
$$
最后一步来自右 collar 上 $r=0$。

将 (7)、(20)、(23)、(24) 合并，得到整个次层公式
$$
\boxed{
[\epsilon^{-8}]\Sigma_{V_B}(u)
=a_B(c)\mathcal T_R(u)+b_B(c)r^4,}
\tag{25}
$$
其中真实路径系数为
$$
a_B(c)=\int_0^Lb^2(\partial_\xi C_g-D_g)\,ds,
$$
$$
b_B(c)=-\int_0^L
\left(\frac12b^2D_g+f_gC_g^2\right)\,ds.
\tag{26}
$$
式 (25) 是整个 $x$ 函数身份，包含其左尾。只要给定原实际路径，(26) 的所有 histories 都由 (12) 唯一决定。

## 6. 总通量零与不能删除的左尾

先对 $\mathcal C=r^4$，
$$
\int r'\mathcal C=\frac15[r^5]_\ell^{r_*}=0.
\tag{27}
$$
对 (23) 的两个原函数项，紧输入的 $r,v$ 在两端均为零，逐次保留边项后给
$$
\int r'J^2(F)=\int rJ(F)=\int vF,
\qquad
\int r'J(G)=\int rG.
\tag{28}
$$
这些式子不要求 $J(F)$ 或 $J^2(F)$ 左紧；真正消边项的是外因子 $r,v$。

取 $F=r^2t^2$、$G=vrt^2$，(27)–(28) 得
$$
\boxed{
\int u'''\mathcal T_R(u)
=4\int vr^2t^2-4\int vr^2t^2-\int tr^4=0.}
\tag{29}
$$
因此 (25) 对每条实际路径、每个合法 $c$ 都有准确零总通量。

零配对不能升级为输出零。例如在 $u$ 支撑的左方，
$$
\mathcal T_R(u)(x)
=4\int (y-x)r(y)^2t(y)^2\,dy
-4\int v(y)r(y)t(y)^2\,dy.
\tag{30}
$$
其 $x$ 系数是 $-4\int r^2t^2$。对非零实紧 $u$，该积分严格正：若 $rt\equiv0$，则 $(r^2)'=0$，紧支撑迫 $r=0$，再迫 $u=0$。所以模板 $\mathcal T_R$ 有真实非零的仿射左尾。

本稿没有证明某个实际路径的 $a_B$ 必非零；(30) 只说明不能为了得到 (29) 而把模板的左尾预先置零。

## 7. 从合法局部系数到原 U 的真权

局部窄化阶与未经平移的真权不同，不能跳过这一步。按 R105 与 R203 第 8 节的完整仿射输运，
$$
V(C_{\epsilon,c}u)(c+\epsilon x)
=(D_\epsilon T_cV)(u)(x),\qquad
D_\epsilon|_{U_\sigma}=\epsilon^\sigma.
\tag{31}
$$
self 通道 $\Sigma_V(u)=V(u^2,0)$ 与上述输运及整权投影交换。

原完整成本有有限 Laurent 权支撑，$T_c$ 在同一个 finite profile 函数空间上为 $c$ 的有限多项式。第 2–6 节对每个足够大的合法 $c$、任意共同右 collar 的紧输入，已经证明
$$
\Sigma_{\Pi_{-9}T_cV_B}=0,\qquad
\Sigma_{\Pi_{-8}T_cV_B}
\in\operatorname{span}\{\mathcal T_R,\mathcal C\}.
\tag{32}
$$
R203 第 8 节已逐项说明：在任意预留右零开区间上的全部紧输入可以忠实分离这里的有限仿射 Volterra 函数空间。该论证同样适用于 self 输出及其模掉两个固定模板后的线性商。因此 (32) 是有限函数空间中的多项式身份，不是只在一个输入上观察的值。

对 $c$ 的有限多项式在一个合法开放半轴上成立，遂在 $c=0$ 的 universal 延拓中也成立。这里没有声称 $\xi=0$ 在每条原几何上物理合法。由实际成本取 span，再作其真权投影，得到
$$
\boxed{
\Sigma(U_{-9})=0,\qquad
\Sigma(U_{-8})\subseteq
\operatorname{span}\{\mathcal T_R,\mathcal C\}.}
\tag{33}
$$
(27)、(29) 随即给
$$
\boxed{\Omega_u(U_{-9}+U_{-8})=0.}
\tag{34}
$$
整个证明没有使用任何新的 faithful 查询数值、旧原根重编译或研究消元。

## 8. 对自然商读出的后果与尚欠范围

R203 已证明原正式 pure 投影
$$
\pi(U_{-9}+U_{-8})=0.
$$
R352 的有序三矩尾映射 $\mathscr G_{V,u}$ 只依赖 $\pi V$，所以在这两个真权上同样为零。其自然读出
$$
\Lambda_u(V)=
\Omega_u(V)-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u))
$$
因此在这里恰为 $\Omega_u(V)$。由 (34)，
$$
\boxed{\Lambda_u(U_{-9}+U_{-8})=0.}
\tag{35}
$$

这是整个原 $U$ 的两个完整权层的新值判定。它不只覆盖三个加速度平方族，也不以某个有限参数 profile 族的零值作外推。另一方面，(33) 并未证明完整 mixed 成本空间 $U_{-8}$ 为零，更未证明它等于已有响应像。

权 $-6$ 的原 pure-zero 目标、$H_1,H_2$ 的完整正规密度、其余 normal 生成元及 $\Lambda|_U$ 的一般值仍未由本稿决定。总通量本身也不能代替各活动包的平台、内部退化通量、真实端芽或同一个二阶 gauge 的完整 period 条件。
