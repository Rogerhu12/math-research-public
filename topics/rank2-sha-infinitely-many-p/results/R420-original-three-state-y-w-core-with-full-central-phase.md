# R420 — 原两输入的真实三态 Y/W 核、完整中心相位与和差边际

日期：2026-11-14。**状态：已证明。** 在 R416 的同一个实际两输入
\(\rho _0=\nu_S\otimes\nu_L\) 上，真实 \(Y\)-核与真实总和 \(W\)-核生成一个恰为三维的整来源空间。它们的绝对矩阵满足
\[
A^2=B^2=I,\qquad (AB)^3=-I.
\]
第三态是带完整中心符号的
\[
\rho _2\ \longleftrightarrow\
\Psi(y,v)=-\frac14\sum_{t\in E[4]}S_{-t}(y)L_t(v),
\]
而不是普通 \(y\mapsto-y\) 反射后的第二态。三个来源的 \(Y,W,-Y+x_2\) 完整边际均由原 \(S,T\) 精确给出，因此原两条中央零可合法传入整个真实三态空间。

本文特别支付双倍覆盖上 \(K_{288}\) 的含中心接口；没有把原 \(K_{72}^2=I\) 免费延伸到新的反射来源，也没有通过边际相等替代联合来源相等。

## 1. 同一个原两输入与两个完整正交坐标

沿用 R398、R413、R416 的原 \(E_{17}\) 周期、sigma、普通 ray、实际来源
\[
S=DC\in\mathcal S_{34},\qquad
L\in\mathcal S_{38},\qquad T=SL\in\mathcal S_{72}.
\]
这里 \(\mathcal S_N=\sigma^N L(NO)\)，\(S,L\) 均偶，
\(S(0)=T(0)=0,\ L(0)=1\)。原 \(E_{24}\) 物理来源仍是
\(-102816\sqrt[3]9\,T\)，不改周期或实际曲线。

令原两输入坐标为 \((Y,X)\)，其中 \(X=x_2\)，并置
\[
W=Y+X,\qquad Q=19Y-17X,\qquad V=X-Y.
\tag{1}
\]
准确有
\[
M=\begin{pmatrix}1&1\\19&-17\end{pmatrix},\quad
\det M=-36,\quad
M\operatorname{diag}(34,38)M^t
=\operatorname{diag}(72,23256),
\tag{2}
\]
\[
M^{-1}=\frac1{36}\begin{pmatrix}17&1\\19&-1\end{pmatrix}.
\]
因而这是同一 \(\mathbf Z_p^2\) 的完整整坐标，保所有 \(Y/W/V\) 域。
原三输入的另一个输出 \(Z\) 不由这两个坐标确定；本文不声称保 \(Z\) 管。

仍记
\[
\lambda=-\bar\pi _0^{-1},\qquad
\kappa=p/\bar\pi _0^2,\qquad \beta=\kappa/p=\lambda^2 .
\tag{3}
\]
这是 R413 的符号。原 \(S\) 的 scalar core 为 \(\lambda\)，
原 \(L\) 的 scalar core 为 \(-\lambda\)。

第一态的 \((W,Q)\) 全来源是
\[
H_0(w,q)=S(w+19q)L(w-17q)
\in\mathcal S_{72}\boxtimes\mathcal S_{23256}.
\tag{4}
\]
准周期、交叉项与整张量格证明和 R413 的同一首阶单位基论证完全相同：
交叉项 \(34\cdot19-38\cdot17=0\)，行列式为当前素数的单位。

## 2. 第二态以及不可丢掉的中心符号

使用 R416 的规范 lift
\[
T_t^{(N)}F(z)=
e^{-N\eta_t(z+t/2)}F(z+t),\qquad F_t=T_t^{(\deg F)}F.
\tag{5}
\]
真实总和核给第二态
\[
F_1(y,v)=
\frac14\sum_{t\in E[4]}S_t(y)L_t(v)
-\frac12\sum_{t\in E[2]}S_t(y)L_t(v).
\tag{6}
\]
记其测度为 \(\rho _1\)。R416 已证明
\[
Y_*\rho _1=-\frac13\nu_S,\qquad W_*\rho _1=\nu_T.
\tag{7}
\]

为对每个四挠项作真实 \(Y\)-核，使用固定双倍覆盖
\[
S_t(2u)=T_{t/2}^{(136)}S(2u),\qquad
L_t(2v)=T_{t/2}^{(152)}L(2v).
\tag{8}
\]
这些全部是原 untwisted degree \(136,152\) 空间中的合法 Heisenberg 平移；
不再把 degree \(34,38\) 的四挠平坦 twist 当作平凡。

原 ray 的 ratio 在完整中心模数上为
\[
g=\pi _0/\bar\pi _0\equiv11+8\omega\pmod {16}.
\tag{9}
\]
仅记 \(g\equiv3\pmod8\) 不足以计算 (8)。
写 \(t=(s+r\omega)/4\)，则完整结果是
\[
\epsilon(t)=(-1)^{rs+r+s}
=\begin{cases}1,&t\in E[2],\\-1,&t\in E[4]\setminus E[2],\end{cases}
\]
\[
K_{136}S_t(2u)=\epsilon(t)S_{-t}(2u),\qquad
K_{152}L_t(2v)=-\epsilon(t)L_{-t}(2v).
\tag{10}
\]
此处两个 \(K\) 都采用外部标量 \(\lambda\) 的归一。

下面给包含中心的直接核算，亦固定绝对符号。
在标准 theta 基中，对 level \(N=8n\) 的二进部分取 \(e_k\)，\(k\bmod8\)，则
\[
T_{(s+r\omega)/8}^{(N)}e_k
=\zeta_{16}^{\,n sr+2n sk}e_{k+r}.
\tag{11}
\]
degree \(136\) 的 \(n=17\)，degree \(152\) 的 \(n=19\)。
原双倍拉回的二进子空间由 \(e_0+e_4,e_2+e_6\) 张成。
算子
\[
B_1e_k=(-1)^ke_{3k+4}
\tag{12}
\]
固定这两条向量，并将 \(T_{1/8},T_{\omega/8}\) 分别交织为
\(T_{g/8},T_{g\omega/8}\)；二者包含的负号都来自 (9) 的中心。
原 \(S(2u)\) 的已付核为 \(+1\)，故 \(K_{136}=B_1\) 在其全部八挠平移生成的实际模块上。
对 \(L(2v)\) 同样得到 \(K_{152}=-B_2\)，其中 \(B_2\) 是 (12) 在第二因子上的版本。
把 (11) 作用于上述两条拉回向量，恰得到 (10)；没有选择任意平方根相位。

将 (10) 代入 (6)，真实 \(Y\)-核的第三态为
\[
\boxed{\quad
F_2(y,v)=\Psi(y,v)
=-\frac14\sum_{t\in E[4]}S_{-t}(y)L_t(v).\quad}
\tag{13}
\]
记其测度为 \(\rho _2\)。特别 \(F_2\ne F_1(-y,v)\) 的区别不能删掉。

## 3. 支付真实 \(K_{288}\) 的整个平移模块接口

双倍覆盖后的 (4) 位于
\[
\mathcal S_{288}\boxtimes\mathcal S_{93024}
\tag{14}
\]
中。定义覆盖输入上的两组合法平移
\[
U_t=T_{t/2}^{(136)}\otimes T_{t/2}^{(152)},\qquad
V_t=T_{-t/2}^{(136)}\otimes T_{t/2}^{(152)}
\qquad(t\in E[4]).
\tag{15}
\]
在 (14) 的 \((w,q)\) 坐标中，它们分别是
\[
U_t:(w,q)\mapsto(w+t/2,q),\qquad
V_t:(w,q)\mapsto(w+t/36,q-t/36).
\tag{16}
\]
两边规范 lift 的 Gaussian 完全相同，由 (2) 的真实对角化直接得到。
后者的点阶至多 \(144\)，而 \(288/144=2\)、\(93024/144=646\) 都为偶整数；
所以原 \(g\bmod144\) 已足以确定这里的完整中心相位。

原 ray 给 \(g=91+72\omega\bmod144\)。真实 \(W\)-核因此准确交织
\[
U_t\longmapsto U_{3t},
\]
\[
V_t\longmapsto
T_{(2+2\omega)t}^{(136)}
\otimes T_{(3+2\omega)t}^{(152)}.
\tag{17}
\]
第二式由
\[
\frac{g-19}{36}t=(2+2\omega)t,\qquad
\frac{g+17}{36}t=(3+2\omega)t
\]
得到，所有周期改变均保留上述偶整数中心。

令 \(\mathcal M\) 为 (15) 生成的有限群作用于
\(S(2u)L(2v)\) 后的实际来源模块。
该群的平移点正是 \((a/2,b/2)\)，其中
\(a,b\in E[4]\)、\(2a=2b\)，并保它们的完整有限中心。
第一因子的 (9) 将这组点送回自己，所以 (24) 的 \(B\) 也保持
\(\mathcal M\)；不是只因其矩阵保持一个较大的抽象空间便断言实际来源闭合。
两因子的奇数 theta 指标分别为模 \(17,19\)，(15) 不改它们。
二进部分则落在以下完整十六维空间：
\[
k,l\bmod8,\qquad k\equiv l\pmod2,\qquad
e_{k+4,l+4}=e_{k,l}.
\tag{18}
\]
原两个双倍拉回在这里，(15) 也保持这里。最后一个等式表示将
两个标准基向量的和作为基，并非把两个不相等的 theta 函数直接认同。

在 (18) 上定义固定的四挠算子
\[
A=\frac14\sum_{t\in E[4]}U_t-\frac12\sum_{t\in E[2]}U_t.
\tag{19}
\]
它正是 R416 在第一态上的真实 \(W\)-核。为证明它在整个新模块上仍是同一个真实核，不能只引用旧 \(K_{72}^2\)。

由 (11)，对 \(t=(s+r\omega)/4\)，
\[
U_te_{k,l}
=i^{\,s(r+(k+3l)/2)}e_{k+r,l+r}.
\tag{20}
\]
设 \(h=(k+3l)/2\bmod4\)。对 (19) 中的四个 \(s\) 完整求和给
\[
Ae_{k,l}=
\begin{cases}
e_{k-h,l-h},&h\ {\rm odd},\\
-e_{k+2-h,l+2-h},&h\ {\rm even}.
\end{cases}
\tag{21}
\]
这是带绝对符号的置换，特别 \(A^2=I\)。

用 (11)、(21) 检查四个生成元
\(U_{1/4},U_{\omega/4},V_{1/4},V_{\omega/4}\)，得到
\[
AU_tA=U_{3t},\qquad
AV_tA=
T_{(2+2\omega)t}^{(136)}
\otimes T_{(3+2\omega)t}^{(152)}.
\tag{22}
\]
这些是 (17) 的完整 lift，非只比较无中心的点。
例如 \(V_{\omega/4}\) 的右侧在 (18) 上为
\(-e_{k,l+2}\)，\(V_{1/4}\) 的右侧为
\(-i^{3l}e_{k,l}\)；两个负号都必须保留。
(20)–(21) 代入即可逐项得到它们；其余点由群乘法和相同中心得到。

真实 \(K_{288}\) 与 \(A\) 在第一条实际来源上的像相同，
并且 (17)、(22) 说明它们对 \(\mathcal M\) 的全部生成元交织相同。
因此对任何生成元词 \(G\)，
\[
K_{288}(G F_0)=G'K_{288}F_0=G'AF_0=AGF_0.
\]
所以
\[
\boxed{\ K_W=A\quad\text{在整个实际模块 }\mathcal M\text{ 上。}\ }
\tag{23}
\]
这支付了覆盖、隐藏 \(Q\) 坐标、中心和绝对标量。无需再扩大覆盖，也没有将某个边际恒等式当作联合核恒等式。

## 4. 真实两个核的有限关系及三态闭包

在 (18) 上真实 \(Y\)-核是
\[
Be_{k,l}=(-1)^ke_{3k+4,l}.
\tag{24}
\]
它就是 (12)。所有定义均保持实际模块 \(\mathcal M\)。
改用十六个坐标
\[
u=(k+l)/2,\qquad v=(k-l)/2\pmod4,
\]
并记 \(\varepsilon_j=2\) 当 \(j\) 偶、\(0\) 当 \(j\) 奇。
(21)、(24) 分别化为
\[
A e_{u,v}=-(-1)^v e_{\,v+\varepsilon_v-u,\ v},
\]
\[
B e_{u,v}=(-1)^{u+v}
e_{\,2u+v+2,\ u+2v+2}.
\tag{25}
\]
从而
\[
ABe_{u,v}=-(-1)^v
e_{\,v-u+\varepsilon_u,\ u+2v+2}.
\tag{26}
\]
连续作用三次时坐标回到 \((u,v)\)；三个符号的奇偶指数为
\(v+u+(u+v)\)，总符号恰为负。因此在整个 (18) 上
\[
\boxed{A^2=B^2=I,\qquad(AB)^3=-I.}
\tag{27}
\]
这不是由目标中央导数定标的关系。

原 \(S\) 偶且其实际 \(Y\)-核为正，所以 \(B\rho _0=\rho _0\)。
又 \(\rho _1=A\rho _0,\rho _2=B\rho _1\)。由 (27) 得
\[
\boxed{
\begin{array}{c|ccc}
&\rho _0&\rho _1&\rho _2\\ \hline
A&\rho _1&\rho _0&-\rho _2\\
B&\rho _0&\rho _2&\rho _1 .
\end{array}}
\tag{28}
\]
因而三态真实闭合。
第二原输入的核为 \(-B\)：也可直接对 (6)、(13) 的第二因子使用 (10)，
分别得到 \(-\rho _2,-\rho _1\)，对 \(\rho _0\) 得 \(-\rho _0\)。

这些来源均整有界。第一态已整；其余是已经支付的完整整核
\(A,B\) 的实际像。固定覆盖的所有 degree 只含 \(2,3,17,19\)，
当前 \(p>19\) 不引入新坏素数。

## 5. 三个完整边际与实际中央零传播

R419 的两个独立完整和恒等式为
\[
\sum_{E[4]\setminus E[2]}S_{-t}(z)L_t(z)=0,\qquad
\sum_{E[2]}S_t(z)L_t(z)=0.
\tag{29}
\]
所以 (13) 的整个 \(W\) 推前为零。
其 \(Y\) 推前在 \(v=0\) 时只剩二挠项，与 R416 的完整半周期求和相同。
另一方面，(19) 对 \(T\) 的真实像是 \(T\)，配合 (29) 给
\(\frac14\sum_{E[4]}T_t=T\)。
全部结果为
\[
\boxed{
\begin{array}{c|ccc}
&Y_*&W_*&V_* \quad(V=X-Y)\\ \hline
\rho _0&\nu_S&\nu_T&\nu_T\\
\rho _1&-\nu_S/3&\nu_T&0\\
\rho _2&-\nu_S/3&0&-\nu_T .
\end{array}}
\tag{30}
\]
最后一格的负号来自
\(S_{-t}(-z)=S_t(z)\) 及 (13)，不能漏掉。
所有等式都是完整 Amice 来源、完整普通测度等式，保全部 tame、单位及非单位部分。

三态实际上线性独立。若
\(\alpha\rho _0+\beta\rho _1+\gamma\rho _2=0\)，
依次取 \(W,Y\) 推前，再对该关系先用 \(B\) 后取 \(W\) 推前，
得到
\[
\alpha+\beta=0,\qquad
\alpha-\beta/3-\gamma/3=0,\qquad \alpha+\gamma=0.
\]
其行列式为当前素数的单位 \(-5/3\)，故三个系数都为零。
原 \(S,T\) 的首项都是单位倍 \(z^6\)，所以这三个实际观察还给该三态格的整系数提取，不只是分式域上的线性独立。

特别若原两个真实中央条件
\[
J'_S(0)=J'_T(0)=0
\tag{31}
\]
成立，则对整个
\(\mathcal V_{\mathcal O}=\mathcal O\rho _0+\mathcal O\rho _1+\mathcal O\rho _2\)，
在 \(Y,W,V\) 三个固定实际输出上的 principal 单位中央行都为零。
因 (28) 是真实来源闭包，这些全边际零保每次 \(A,B\) 返回。
这里尚未将任何受限交域自动赋零。

第三个原输入 \(X=x_2\) 的完整边际也可准确保留。因为
\(S(t)=0\) 对全部 \(t\in E[2]\)，置
\[
\mathcal M_X(v)=\frac14
\sum_{t\in E[4]\setminus E[2]}S_t(0)L_t(v).
\tag{31a}
\]
则
\[
X_*\rho _0=0,\qquad X_*\rho _1=\nu_{\mathcal M_X},
\qquad X_*\rho _2=-\nu_{\mathcal M_X}.
\tag{31b}
\]
相应函数在双倍覆盖后属于完整 \(\mathcal S_{152}\)；
原 degree \(38\) 的非平凡平坦 twist 未被省略。
由真实第二输入核 \(-B\) 直接得到
\[
\nu_{\mathcal M_X}|_p
=\lambda[\kappa]_*\nu_{\mathcal M_X}.
\tag{31c}
\]
其总质量为零，但这里不声称它恒零、中央导数为零或对应另一条
已付的 rank-two 算术来源。式 (37) 中的 \(X\) 中央行因此已经
缩成这一条具体来源的中央行及相应已知系数，仍须另行确定。

## 6. 完整条件核与所有补域

令
\[
P_Y=\operatorname{diag}(\kappa,1),\qquad
P_X=\operatorname{diag}(1,\kappa),
\]
\[
P_W=M^{-1}\operatorname{diag}(\kappa,1)M
=I+\frac{\kappa-1}{36}
\begin{pmatrix}17&17\\19&19\end{pmatrix},
\]
\[
P_Q=M^{-1}\operatorname{diag}(1,\kappa)M
=I+\frac{\kappa-1}{36}
\begin{pmatrix}19&-17\\-19&17\end{pmatrix}.
\tag{32}
\]
这些映射均只将指定输出乘 \(\kappa\)，保相应另一个完整输出；
其逆仅在相应深域的像上使用。
对任何 \(F\in\mathcal V_{\mathcal O}\)，准确有
\[
\boxed{
\begin{aligned}
\rho_F|_{Y\in p}&=\lambda(P_Y)_*\rho_{BF},&
\rho_F|_{X\in p}&=-\lambda(P_X)_*\rho_{BF},\\
\rho_F|_{W\in p}&=\lambda(P_W)_*\rho_{AF},&
\rho_F|_{Q\in p}&=-\lambda(P_Q)_*\rho_{AF}.
\end{aligned}}
\tag{33}
\]
最后一式亦可直接从完整两输入全深核推出：
两个原输入同时深的来源算子为 \(B(-B)=-I\)；
由 (2) 同一域是 \(W,Q\) 同时深，因此 \(K_WK_Q=-I\)，
而 (23) 给 \(K_Q=-A\)。
没有在整个 degree \(23256\) 空间上额外猜测二阶关系。

同一正交坐标下的全深度因此为
\[
\rho_F|_{\substack{Y\in p^m\\X\in p^n}}
=(-1)^n\lambda^{m+n}
[\kappa^m,\kappa^n]_*\rho_{B^{m+n}F},
\]
\[
\rho_F|_{\substack{W\in p^r\\Q\in p^s}}
=(-1)^s\lambda^{r+s}
[\kappa^r,\kappa^s]_{W,Q,*}\rho_{A^{r+s}F}.
\tag{34}
\]
对不同坐标方向的交域，必须按 (33) 顺序拉回全部指示条件。
例如对任意连续 \(\phi\) 和任意 \(N\ge1\)，原同一碰撞域
\[
\mathcal D_N=\{Y\in p^N,\ W\text{ 为单位}\}
\]
给准确式
\[
\int_{\mathcal D_N}\phi(W)\,d\rho_F
=\lambda^N\int_{X\ {\rm unit}}
\phi(X+\kappa^NY)\,d\rho_{B^NF}.
\tag{35}
\]
这保全 \(Y\) 辅助变量；单位域准确变成 \(X\) 单位域。
相反，若从 \(W\) 方向处理同一两输出，将
\[
Y=\frac{17W+Q}{36}
\]
代入，得到
\[
\int_{\substack{W\in p^N\\Y\ {\rm unit}}}
\phi(Y)\,d\rho_F
=\lambda^N\int_{Q\ {\rm unit}}
\phi\left(\frac{17\kappa^NW+Q}{36}\right)d\rho_{A^NF}.
\tag{36}
\]
这里分母 \(36\) 为单位；没有将移动管改成原点轴后删去其余条件。

取 \(\phi(t)=d\log_p\langle t\rangle,\ d=p-1\)，(35) 的完整收敛式是
\[
\lambda^Nd\left[
\int_{X\ {\rm unit}}\log_p\langle X\rangle\,d\rho_{B^NF}
+\sum_{j\ge1}\frac{(-1)^{j+1}\kappa^{Nj}}j
\int_{X\ {\rm unit}}Y^jX^{-j}\,d\rho_{B^NF}
\right].
\tag{37}
\]
每项赋值至少 \(Nj-v_p(j)\)。所有 \(j\) 都保留。
(36) 同样给 \(Q/36\) 的完整对数及
\((17\kappa^NW/Q)^j/j\) 的全部混合矩。
在 (31) 下，因 \(W\) 或 \(Y\) 全边际中央行为零，
相应完整补域中央行恰为 (37) 或 (36) 的负值。
原 \(X,Q\) 中央行与混合矩仍须控制，不能由 (30) 删除。

为便于后续整返回，对任一套正交坐标令来源算子
\(C=B\) 或 \(A\)，两方向的环带乘数分别为
\[
a_1=q_1\lambda\,\omega_p(\beta)^{\ell_1}
\langle\beta\rangle^{du_1},\qquad
a_2=-q_2\lambda\,\omega_p(\beta)^{\ell_2}
\langle\beta\rangle^{du_2}.
\]
在 \(|q_i|_p<1\) 的真实收敛积分中，全部环带精确合成
\[
\mathscr Z_F=
\frac{(1+a_1a_2)\mathscr J_F+(a_1+a_2)\mathscr J_{CF}}
{(1-a_1^2)(1-a_2^2)}.
\tag{38}
\]
\(\mathscr J\) 是该套两个输出均为单位的完整联合 Mellin 行。
R410 的同一固定 ray 单位结果使 principal \(q_1=q_2=1\) 的分母可整除。
这保整个三态的 jet 理想；不声称只由某个单独行的零得到任意新零。

## 7. 两条不同的实际组合

真实两核的共同字符为
\[
\chi=\rho _0-\rho _1-\rho _2,\qquad
B\chi=\chi,\quad A\chi=-\chi.
\tag{39}
\]
其完整边际是
\[
Y_*\chi=\frac53\nu_S,\qquad W_*\chi=0,\qquad V_*\chi=2\nu_T.
\tag{40}
\]
所以 \(\chi\ne0\)，并且在 (31) 下其三个显示中央行都为零。
在原坐标上它有四条真实 scalar-core 式：
\(Y,Q\) 方向的符号为 \(+\lambda\)，\(X,W\) 方向的符号为 \(-\lambda\)。
但 \(B\) 是完整 theta 核，不是普通反射，不能据此称 \(\chi\) 逐输入偶；
其差输出也不是零。

另一条用于双对角因子的实际组合是
\[
\eta=\rho _0-\rho _1+\rho _2,\qquad
A\eta=-\eta,\quad
Y_*\eta=\nu_S,\quad W_*\eta=V_*\eta=0.
\tag{41}
\]
它不是 \(B\) 的特征向量。
它却确实分别偶：记普通第一输入反射为 \(R\)，以及
\[
H=-\frac12\sum_{t\in E[2]}S_t\otimes L_t .
\]
在二挠点 \(S_{-t}=S_t\)，故由 (6)、(13)
\[
R\rho _1=H-\rho _2,\qquad R\rho _2=H-\rho _1,\qquad R\rho _0=\rho _0 .
\]
因此 \(R\eta=\eta\)。所有来源还在同时反号下不变，故第二输入也分别偶。
关于双对角全局 sigma 因子，必须仍在 (8) 的固定完整覆盖上进行；
本文不将 degree \(34,38\) 的平坦 twist 免费消去。

## 8. 当前推进与剩余观察

现在原两条真实中央失败已合法进入一个精确三维的完整来源闭包，
而且 \(Y,W,V\) 三个实际输出的全中央行都受控制。
真实核的全部中心符号、\(K_{288}\) 接口、绝对来源矩阵、
正交伴随 \(Q\) 以及交域的完整补域均已支付。

仍不能从 (31) 得出 (37) 中的 \(X\) 中央行、\(Q\) 中央行或各混合矩为零。
这些是下一步须与实际因子和完整交域联系的具体观察。
本篇不声称固定 rank-two 曲线的无穷素数非消失已经完成。

直接依赖：R398 的实际 \(S,L,T\) 与物理尺度；R399/R413 的完整 theta 核及整格；
R416 的绝对四挠公式与第一、第二态边际；R419 的两条完整相反平移求和。
新增中心修正、固定覆盖接口、有限矩阵关系、真实三态闭包和全部显示域公式在本文证明。
