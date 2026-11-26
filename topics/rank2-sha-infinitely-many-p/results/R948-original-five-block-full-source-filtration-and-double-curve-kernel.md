# R948 — 原五块全来源的五层限制、二重曲线核界与真实单位秩

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列同一原完整矩阵的全来源核界已证明。** 本篇不再只考察平方子源。它把整个首核沿同一条 \(C\) 过滤，支付五个真实限制深度，因而控制所有原有限类及非平方偏移。较宽窗口不要求 \(h+\ell\ge N\)：第三层使用 \(\min(N,h+\ell)\)，第四层准确使用 \(\max(\ell,N-h)\)。所有维数都来自一个嵌套过滤，不把不同子块的单位秩相加。

## 1. 原完整格、物理长度与曲线

保 [R938](R938-original-full-source-finite-offsets-and-affine-carry.md)、
[R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)、
[R944](R944-original-five-block-full-square-source-injectivity.md) 的同一十九角光滑射影曲面 \(X\)、同一几何整 Cartier 曲线 \(C=(F)\)、同一完整原格及其约化
\[
 \mathcal W=H^0(X,\mathcal O_X(B_D)),\qquad
 n_D=\dim_k\mathcal W,\qquad
 \kappa=C^2>0,\qquad d_D=B_D\cdot C.
 \tag{1}
\]
全部固定分母、\(P_{134}\)、charge 四十、角帽和原整来源保持不变。

物理点 \(P=(0,1)\) 是 \(C\) 的光滑点；原坐标 \(t\) 是 \(C\) 在 \(P\) 的参数。置
\[
 \mathcal E=Y\partial_Y,\qquad
 e=(\mathcal EF)|_C,\qquad e(P)\ne0,\qquad
 C:\ Y=\psi(t).
\]
同一实际低轴 \(g(t)\) 为单位，且
\[
 \operatorname{ord}_t(g-\psi)
 =\operatorname{ord}_t F(t,g)=h.
 \tag{2}
\]
在需要形式级数时任取给定原低轴的延拓；下列结论只使用显示的有限精度，不延长原 ODE 的授权窗口。

R943 原五块物理评价的四个长窗和末短窗，经已付公共单位及可逆 charge 三角运输后，其准确首核为
\[
 \mathcal K=
 \left\{R\in\mathcal W:
 \begin{array}{ll}
  (\mathcal E^iR)(t,g)\in t^Nk[[t]],&0\le i\le3,\\
  (\mathcal E^4R)(t,g)\in t^\ell k[[t]]
 \end{array}\right\},
 \qquad N=s-13,\quad p=6s-1.
 \tag{3}
\]
这里的 \(N\) 是实际除十三前缀之后的长度；没有给原矩阵补行。四条十三行跨界带的总成本五十二及较高页的所有原 carry 继续按 R943 保留。

本篇只要求
\[
 p>211,\qquad h>21,\qquad
 h<N\le2h+2,\qquad
 1\le\ell<N,\qquad \ell\le h+2.
 \tag{4}
\]
仍须保 R943 的其余有限坏素数门。与 R944 的应用窗口相比，这里不另要求 \(h+\ell\ge N\)。

定义完整子源
\[
 \mathscr D_i
 =F^iH^0(X,\mathcal O_X(B_D-iC)),\qquad
 \mathscr D_0=\mathcal W,\qquad 0\le i\le5,
\]
及同一首核中的嵌套子空间
\[
 \mathcal K^{[i]}=\mathcal K\cap\mathscr D_i.
 \tag{5}
\]
这是在整个 \(X\) 上被 \(F^i\) 整除并支付全部角帽的子源，绝非只在物理支上整除的 germ。

## 2. 有限 Taylor、原零角与全部误差

原固定 \(d=1+8t\) 分母在 \(t=0\) 为单位。原完整多项式来源的 \(Y\) 次数非负，且
\[
 v_0(F)=-3,\qquad v_0(R)\ge-2,\qquad
 v_0\!\left(\sum_{n\ge0}H_n(t)Y^n\right)
 =\min_n\bigl(4\operatorname{ord}_tH_n-n\bigr).
 \tag{6}
\]
特别每个 \(R\in\mathcal W\) 在此二维邻域逐系数正则。若 \(R=F^iH\in\mathscr D_i\)，则 \(v_0(H)\ge3i-2\)，故
\[
 \begin{array}{c|c}
 i&\text{整个乘子的逐系数结论}\\ \hline
 2&H=t c+O(t^2),\quad c\in k\\
 3&H\in t^2k[[t]][Y]\\
 4&H\in t^3k[[t]][Y]\\
 5&H\in t^4k[[t]][Y].
 \end{array}
 \tag{7}
\]
第一行 \(t^1\) 的系数只能是常数，因为 \(4-n\ge4\) 迫 \(n=0\)。这些是原零角的必要结论；其它十八角仍由 (5) 保留，没有被删除。

若 \(R=F^2H\in\mathcal K^{[2]}\)，第二 Euler 长行在 \(t^1\) 的系数为
\(2e(P)^2c\)。所有含 \(F(t,g)\) 的其它项至少深 \(h+1\)；故
\[
 R=F^2H\in\mathcal K^{[2]}
 \quad\Longrightarrow\quad H\in t^2k[[t]][Y].
 \tag{8}
\]
因 \(\mathcal E(t)=0\)，逐系数的 \(t^a\) 因子被所有有限 Euler 导数保留。

为精确控制曲线与实际轴之间的移动，令
\[
 \delta=g-\psi,\qquad \eta=\delta/\psi,\qquad
 \operatorname{ord}_t\eta=h.
\]
若 \(S\) 逐系数含 \(t^a\)，一次普通有限 Taylor 给
\[
 \begin{aligned}
 S(t,g)&=S|_C+\eta(\mathcal ES)|_C+O(t^{2h+a}),\\
 S|_C&=S(t,g)-\eta(\mathcal ES)(t,g)+O(t^{2h+a}).
 \end{aligned}
 \tag{9}
\]
第二式可以直接由普通导数证明：在
\(S(\psi)=S(g)-\delta S_Y(g)+O(t^{2h+a})\)
中，\(\delta/g\) 与 \(\delta/\psi\) 的差深 \(2h\)。
因此 (9) 没有把普通坐标差误当作精确 Euler 位移，也未使用特征 \(p\) 下的无限对数或无限指数。

还需整个来源的前两个限制。由于 \(g\) 为单位，
原四个 Euler 长行与 \(R,R_Y,R_{YY},R_{YYY}\) 在 \(g\) 处都深 \(N\) 等价。普通有限 Taylor 因而给
\[
 \begin{aligned}
 R|_C
 &=\sum_{j=0}^{3}\frac{(-\delta)^j}{j!}
       (\partial_Y^jR)(t,g)+O(t^{4h}),\\
 R_Y|_C
 &=\sum_{j=0}^{2}\frac{(-\delta)^j}{j!}
       (\partial_Y^{j+1}R)(t,g)+O(t^{3h}).
 \end{aligned}
 \tag{10}
\]
由 \(h>21\)、\(N\le2h+2<3h\)，两式都深 \(N\)。
\(2,6,24\) 在当前剩余域可逆；所有余项只用原二维正则性。

## 3. 同一首核的五层真实限制

置
\[
 n_0=n_1=n_2=N,\qquad
 n_3=\min(N,h+\ell),\qquad
 n_4=\max(\ell,N-h).
 \tag{11}
\]

**定理 1。** 对 \(0\le i\le4\)，映射
\[
 \mu_i:\mathcal K^{[i]}\longrightarrow
 H^0\!\left(C,\mathcal O_C(B_D-iC)(-n_iP)\right),
 \qquad
 F^iH\longmapsto H|_C
 \tag{12}
\]
有定义，且
\[
 \ker\mu_i=\mathcal K^{[i+1]},\qquad
 \mathcal K^{[5]}=\mathscr D_5.
 \tag{13}
\]
因此
\[
 \boxed{\displaystyle
 \dim\mathcal K
 =\dim\mathscr D_5+\sum_{i=0}^{4}\dim\operatorname{im}\mu_i
 \le\dim\mathscr D_5+
 \sum_{i=0}^{4}
 h^0\!\left(C,\mathcal O_C(B_D-iC)(-n_iP)\right).}
 \tag{14}
\]
各右侧空间只是实际限制像的容器，不在此宣称限制满射。

**证明。**

对于 \(i=0\)，(10) 直接给 \(R|_C\) 深 \(N\)。对于 \(i=1\)，写 \(R=FH\)；同一个精确乘积式
\[
 (\mathcal ER)|_C=eH|_C
\]
与 (10) 的 \(R_Y|_C\) 深 \(N\) 给 \(H|_C\) 深 \(N\)。这里没有把一般 \(R\) 分解成两个各自入核的分量。

对于 \(i=2\)，先用原长行得到 (8)。把 (9) 用于
\(S=\mathcal E^2R\)，其逐系数含 \(t^2\)；第二、第三 Euler 长行均深 \(N\)，二次误差深 \(2h+2\ge N\)。故
\[
 (\mathcal E^2R)|_C\in t^N,\qquad
 (\mathcal E^2(F^2H))|_C=2e^2H|_C,
 \tag{15}
\]
给 \(n_2=N\)。

对于 \(i=3\)，(7) 给整个乘子逐系数含 \(t^2\)。将 (9) 用于 \(S=\mathcal E^3R\)，得到
\[
 (\mathcal E^3R)|_C
 =(\mathcal E^3R)(t,g)
 -\eta(\mathcal E^4R)(t,g)+O(t^{2h+2}).
\]
三个项的保证深度分别为 \(N,h+\ell,2h+2\)，故
\[
 (\mathcal E^3R)|_C\in t^{n_3},\qquad
 (\mathcal E^3(F^3H))|_C=6e^3H|_C.
 \tag{16}
\]
这正是较宽窗口需要保留的 \(\min(N,h+\ell)\)；没有借用旧 \(\ell\ge N-h\)。

对于 \(i=4\)，写 \(R=F^4L\)。由 (7)，\(L\) 逐系数含 \(t^3\)。准确有
\[
 (\mathcal E^jR)|_C=0\ (0\le j\le3),\qquad
 (\mathcal E^4R)|_C=24e^4L|_C.
\]
有限 Taylor 给
\[
 \begin{aligned}
 (\mathcal E^jR)(t,g)&\in t^{2h+3}\quad(0\le j\le2),\\
 (\mathcal E^3R)(t,g)
  &=24e^4\eta L|_C+O(t^{2h+3}),\\
 (\mathcal E^4R)(t,g)
  &=24e^4L|_C+O(t^{h+3}).
 \end{aligned}
 \tag{17}
\]
第一行也可直接由乘积中至少两个 \(F\) 因子读出。
因 \(N\le2h+2\)、\(\ell\le h+2\)，第三 Euler 长行准确要求 \(L|_C\) 深 \(N-h\)，第四 Euler 短行准确要求其深 \(\ell\)。于是
\[
 \boxed{\displaystyle
 \mathcal K^{[4]}=
 \{F^4L:L\in H^0(X,\mathcal O_X(B_D-4C)),
                \ \operatorname{ord}_P L|_C\ge n_4\}.}
 \tag{18}
\]
特别 \(n_4\) 是两行共同给的最大值，不应在较宽窗口仍只写成 \(\ell\)。

若 \(R=F^5H\in\mathscr D_5\)，(7) 给乘子及其所有有限导数逐系数含 \(t^4\)。沿 \(g\)，第 \(i\) 个 Euler 值至少深
\((5-i)h+4\)（\(0\le i\le4\)）。
对 \(i\le3\)，其最小值 \(2h+4>N\)；对 \(i=4\)，其值 \(h+4>\ell\)。
故 \(\mathscr D_5\subset\mathcal K\)，即 (13) 的最后等式。

最后，任意线束的完整 Cartier 限制列
\[
 0\longrightarrow\mathcal O_X(B_D-(i+1)C)
 \xrightarrow{\ \cdot F\ }
 \mathcal O_X(B_D-iC)
 \longrightarrow\mathcal O_C(B_D-iC)
 \longrightarrow0
 \tag{19}
\]
在全球截面处的核恒准确；无须任何 \(H^1\) 消失或限制满射。
故 \(\ker\mu_i=\mathcal K^{[i+1]}\)。沿同一嵌套链取维数即得 (14)。证毕。

## 4. 适用于可能奇曲线的明确 \(h^0\) 界

置
\[
 g_C=p_a(C)=1+\frac{\kappa+K_X\cdot C}{2},\qquad
 \chi_C=-K_X\cdot C.
 \tag{20}
\]
这是算术亏格。\(C\) 是光滑曲面上的 Cartier 曲线，因而 Gorenstein；\(\omega_C\) 可逆且次数 \(2g_C-2\)。不把可能奇的 \(C\) 换成其正规化后忽略差额。

对整数 \(d\)，定义
\[
 \mathsf H_g(d)=
 \begin{cases}
 0,&d<0,\\
 \lfloor d/2\rfloor+1,&0\le d\le2g-2,\\
 d+1-g,&d\ge0,\ d>2g-2.
 \end{cases}
 \tag{21}
\]
中间区间在 \(g=0\) 时为空；该定义也涵盖 \(g=0,1\)。

对任意 \(C\) 上次数为 \(d\) 的线束 \(L\)，有
\[
 h^0(C,L)\le\mathsf H_{g_C}(d).
 \tag{22}
\]
这里给出所需特殊区间的证明，避免假设曲线光滑或引用未核的特殊版本。延标量到代数闭包不改截面维数。负次数无非零正则截面；\(d>2g_C-2\) 时，由 Serre 对偶及负次数给 \(H^1(C,L)=0\)，Riemann–Roch 给等号 \(h^0=d+1-g_C\)。

剩下 \(0\le d\le2g_C-2\)。若 \(h^0=0\)，结论显然。若 \(h^1=0\)，Riemann–Roch 已给
\(h^0=d+1-g_C\le d/2+1\)。
否则记
\[
 a=h^0(C,L)>0,\qquad
 b=h^0(C,\omega_C L^{-1})=h^1(C,L)>0.
\]
乘法映射到 \(H^0(C,\omega_C)\) 的像至少有维数 \(a+b-1\)。
为直接证明这一点，在任一光滑点选两组按消失阶递增的基
\(v_1,\ldots,v_a\) 与 \(w_1,\ldots,w_b\)。
每个有限维截面空间在一个光滑点的消失阶过滤，每一层商至多一维，故可以选成各阶互异。
积
\[
 v_1w_1,\ldots,v_aw_1,\quad v_aw_2,\ldots,v_aw_b
\]
具有严格递增的消失阶，因 \(C\) 整而均非零，故线性无关。
所以 \(a+b-1\le g_C\)。结合
\(a-b=d+1-g_C\)，得 \(2a\le d+2\)，即 (22)。
该证明在当前特征下不需要额外可分性或光滑曲线 Clifford 假设。

于是定理 1 给全有限参数的明确界
\[
 \boxed{\displaystyle
 \dim\mathcal K\le
 h^0(X,\mathcal O_X(B_D-5C))
 +\sum_{i=0}^{4}
 \mathsf H_{g_C}(d_D-i\kappa-n_i).}
 \tag{23}
\]
这里第一项就是完整 \(\mathscr D_5\) 的维数，未把实际五次来源删去。

## 5. 完整平方首核消失与真正二重曲线

若满足四个明确次数门
\[
 \begin{aligned}
 d_D-2\kappa&<N,\\
 d_D-3\kappa&<n_3,\\
 d_D-4\kappa&<n_4,\\
 d_D&<5\kappa,
 \end{aligned}
 \tag{24}
\]
则
\[
 \mathcal K^{[2]}=0.
 \tag{25}
\]
证明：前三门依次使定理 1 的第 \(2,3,4\) 层实际限制像为零。
又因 \(C\) 几何整且 \(\kappa>0\)，它和其它整曲线的交数非负、和自身交数为正，故 \(C\) nef。
若 \(H^0(B_D-5C)\ne0\)，其有效零除子与 \(C\) 的交数应非负，却等于 \(d_D-5\kappa<0\)，矛盾。
所以最后一层也为零。

旧窗口 \(h+\ell\ge N\) 给 \(n_3=N,n_4=\ell\)，于是 (24) 退回 R944 的门，第二门由第一门自动推出。较宽窗口则按 (11) 支付两层不同深度。

为将整个来源的剩余核准确放在二重曲线上，置
\[
 Z=2C.
\]
它是 \(X\) 上的非约化有效 Cartier 曲线。在 \(P\) 处，
\[
 \widehat{\mathcal O}_{Z,P}\simeq k[[t,F]]/(F^2).
\]
定义 \(Z\) 上的有效 Cartier 除子 \(\Delta_P\)：在一个只含 \(t=0\) 与 \(C\) 的该次交点 \(P\) 的邻域内用方程 \(t\)，在 \(Z\setminus\{P\}\) 用方程 \(1\) 粘合。
交叠处 \(t\) 为单位；在 \(P\) 的上式环中 \(t\) 不是零因子，故这是确切的 Cartier 除子，而非任意选取的厚点延拓。
其在 \(C\) 上的限制为 \(P\)，在 \(Z\) 上的长度为二。

在原局部线束框中，模 \(F^2\) 的展开为
\[
 R=R|_C+
 F\,\frac{R_Y|_C}{F_Y|_C}\pmod{F^2}.
 \tag{26}
\]
\(F_Y|_C=e/\psi\) 为单位。
由 (10)，对于每个 \(R\in\mathcal K\)，(26) 两个系数都含 \(t^N\)，故实际限制满足
\[
 R|_Z\in
 H^0\!\left(Z,\mathcal O_Z(B_D)(-N\Delta_P)\right).
 \tag{27}
\]
改变局部线束框只作单位三角变换，不改变两个系数共同含 \(t^N\) 这一条件。

\(R|_Z=0\) 的完整全球核正是 \(\mathscr D_2\)。
因此在 (24) 下，(27) 给整个原首核的注入
\[
 \boxed{\displaystyle
 \mathcal K\hookrightarrow
 H^0\!\left(2C,\mathcal O_{2C}(B_D)(-N\Delta_P)\right).}
 \tag{28}
\]
这里没有把原有限类挑成某个自然陪集。

二重曲线的准确列
\[
 0\longrightarrow\mathcal O_C(-C)
 \longrightarrow\mathcal O_{2C}
 \longrightarrow\mathcal O_C
 \longrightarrow0
\]
张量可逆层
\(\mathcal O_{2C}(B_D)(-N\Delta_P)\) 后得到
\[
 0\longrightarrow
 \mathcal O_C(B_D-C)(-NP)
 \longrightarrow
 \mathcal O_{2C}(B_D)(-N\Delta_P)
 \longrightarrow
 \mathcal O_C(B_D)(-NP)
 \longrightarrow0.
 \tag{29}
\]
左右两个 \(-NP\) 都来自同一个真正 Cartier \(\Delta_P\) 的限制；没有把二重曲线截面空间未经证明拆成直和，也没有假设右侧截面均可提升。
故在 (24) 下，
\[
 \boxed{\displaystyle
 \dim\mathcal K\le
 h^0\!\left(C,\mathcal O_C(B_D)(-NP)\right)
 +h^0\!\left(C,\mathcal O_C(B_D-C)(-NP)\right)
 \le
 \mathsf H_{g_C}(d_D-N)
 +\mathsf H_{g_C}(d_D-\kappa-N).}
 \tag{30}
\]
这也是 (23) 在后三层消失时的同一界；(28) 说明它控制的是完整非约化限制，包括全部非平方、有限交及远离物理点的来源偏移。

## 6. 条件尺度、同一原矩阵的单位秩与仍待支付的强迫项

例如，考虑实际满足 (4) 且
\[
 \kappa\longrightarrow\infty,\qquad
 \chi_C=o(\kappa),\qquad
 d_D=4\kappa+o(\kappa),\qquad
 \frac h\kappa\longrightarrow\frac98,\qquad
 \frac N\kappa\longrightarrow\frac94
 \tag{31}
\]
的一族同一原来源。无需再要求 \(\ell/\kappa\) 有正下界：
\[
 n_3\ge\min(N,h+1)=h+1,\qquad
 n_4\ge N-h.
\]
所以 (24) 的四个门均有严格正比例余量。
又由 (20)，\(g_C=\kappa/2+o(\kappa)\)。
在 (30) 中，两个次数分别为
\[
 d_D-N=\frac74\kappa+o(\kappa),\qquad
 d_D-\kappa-N=\frac34\kappa+o(\kappa).
\]
第一项超过典范次数，第二项在特殊区间；(21) 因而给
\[
 \boxed{\dim\mathcal K\le\frac{13}{8}\kappa+o(\kappa).}
 \tag{32}
\]
这是从整个原来源得到的界，不是只对某个预选陪集的估计。

对于 (3) 所指的同一原整物理矩阵 \(M_5^{\rm orig}\)，原自由 canonical 格的约化核就是 \(\mathcal K\)，故其单位 Smith 因子数准确为
\[
 \operatorname{rank}_k\overline M_5^{\rm orig}
 =n_D-\dim\mathcal K.
\]
因此 (23) 或 (30) 各自直接给同一个原矩阵的单位秩下界；在 (24) 下明确有
\[
 \boxed{\displaystyle
 \operatorname{rank}_{\rm unit}M_5^{\rm orig}
 \ge\max\!\left(0,\,
 n_D-\mathsf H_{g_C}(d_D-N)
     -\mathsf H_{g_C}(d_D-\kappa-N)\right).}
 \tag{33}
\]
不需要把曲线上某个抽象截面另加成来源列：非零约化子式本来就是原矩阵的单位子式。与任何旧单位秩比较时应取较强界，不能将两界相加。

如果在 (31) 外**另已证明** \(n_D=8\kappa+o(\kappa)\)，则 (32) 给
\[
 \operatorname{rank}_{\rm unit}M_5^{\rm orig}
 \ge\frac{51}{8}\kappa+o(\kappa),
 \qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}M_5^{\rm orig}}{n_D}
 \ge\frac{51}{64}.
 \tag{34}
\]
\(n_D=8\kappa+o(\kappa)\) 不能只由 \(d_D=4\kappa+o(\kappa)\) 推出：
例如用曲面 Riemann–Roch 付这一维数时，还须实际有
\(B_D^2=16\kappa+o(\kappa)\)、\(-K_X\cdot B_D=o(\kappa)\) 及所需原 \(H^1\) 消失。
本文不把这些条件免费加到一般五块预算上。

对同一个已固定整源 \(P\) 和同一个指定一次修正目标，若修正方程可解，其全部模 \(p\) 解的差位于 \(\mathcal K\)。
所以 (23)/(30) 同时界定这些差的所有实际有限类，以及任何确实定义在该首核上的线性 carry 读取的像维数。
这不宣称各有限分量独立，也不把右侧 \(h^0\) 当作原限制像的实际维数。

本篇仍未判定给定仿射强迫项是否落入这些实际像；
较高页仍须通过原完整 \(P/R/S\)、所选整提升的下一位及 R943 的真实折回。
特别，单有五个中央零或五轴低 jet 可逆，不自动给任何 primitive \(p^2\) 或更深右核。
若实际候选已经含 \(F^5\) 并迫其预算 \(d_D\ge5\kappa\)，应使用 (23) 保留 \(\mathscr D_5\)，不能套用 (24) 的末门。

## 依赖与证明范围

- R938：同一十九角曲面、完整来源及有限交；完整 Cartier 子源的含义。
- R943：真实第五算术输入、原五块实际评价与全部五十二跨界成本。
- R944：原零角和平方乘子 \(t^1\) 的真实消去；本篇重新写明所需有限 Taylor，并放宽短窗范围。
- (22) 的曲线截面界、全部五层限制以及 \(2C\) 上真正 Cartier \(\Delta_P\) 和两层序列均在本文证明。

本篇为统一代数证明；无新增数学执行、素数扫描、硬编码证书或可重算输出。
