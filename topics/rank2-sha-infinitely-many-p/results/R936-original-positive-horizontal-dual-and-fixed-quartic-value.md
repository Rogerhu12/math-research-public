# R936：原正水平真左行对固定 quartic 短尾的非零评价

日期：2026-11-20。状态：以下为完整符号证明，未执行数学计算。

R934 已把原固定 P 的双 jet forcing 写成一个准确短尾，
但没有从短尾非零推出全局兼容类非零。本注在一个显示的
正水平次数门内，构造真正杀掉全部原兼容对的左行，
并对该同一 forcing 算出原单位 −11U_*(0)/a。
使用的是 R903 已付的完整正水平截面条件，不是任意选择的
局部 dual 数据，也不是 R935 的来源 nef 预算。

结论首先针对已经指定、且实际满足 B∈H3 的原返回陪集；
一般固定 B 的真实偏移始终保留，见 §5。

## 1. 同一原对象和待判固定类

沿用 R928、R934 的原十九角曲面 X、几何整 Cartier 曲线 C、
原光滑点 P₀=(0,1) 和同一线束

\[
C=(F),\quad N=\mathcal O_C(C),\quad
\kappa=C^2,\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
V=H^0(C,N^3).
\tag{1}
\]

仍用 \(\mathcal E=Y\partial_Y\)、\(b=\deg_YF\)、
\(e=\mathcal EF\)，保 \(3b<p\)、\(e(P_0)\ne0\)、
\(F(t,0)\ne0\)、原完整返回
\(\jmath(G)=qt^2G\in\overline{\mathcal W}_D\)。
完整 P134、总 charge 四十、原 q 的全部 Euler 项和十九角
均已按 R928 的同一单位三角逆运输；不更换原格。

保持 R934 的全部负 fringe 与长度：

\[
s=2h+d_0+2,\quad1\le d_0\le13,\quad
r_{\rm src}=\tau+d_0+2,\quad J=s-2=2h+d_0,
\tag{2}
\]
\[
T=J-13,\quad L=\ell-2,\quad
h<T\le2h,\quad T-h>\kappa,\quad
T-h\le L\le h,\quad2h+L>J.
\tag{3}
\]

r_src 是原 P 的来源指数；返回指数仍为 2。
本注处理 R934 尚有非零短尾的范围

\[
\boxed{2\le\tau\le d_0+1.}
\tag{4}
\]

固定的原整 P 与给定基点 R_b 按 R934 同预算 factor lift 定义

\[
\Delta=(P-P^{\rm fact})/p,\qquad
B=\frac{\overline{R_b+\Delta}}{qt^2}.
\tag{5}
\]

不改变这个给定的陪集 \(\bar R_b+\jmath\mathcal H_3\)。
先按原矩阵核 R928 的四个实际 t² 低行门；失败则该陪集已不可解。
通过后，R934 的固定全 J 对是

\[
j_0=-B|_C,\qquad
j_1=\mathcal T_P-(\mathcal EB)|_C
\pmod{t^J},
\tag{6}
\]
\[
\mathcal T_P=-\frac{11}{a}t^K\mathcal U_*(t),\qquad
K=2h+\tau-2,\qquad
\mathcal U_*(0)\ne0.
\tag{7}
\]

这里

\[
\mathcal U_*(t)
 =\left(\frac{w(t)}t\right)^{-s}
  \left(t^{-h}F(t,\bar g(t))\right)^4
\tag{8}
\]

仍是同一原实际轴；没有丢掉其已付规范。
(4) 给 \(K<J\)，且 \(J-K=d_0+2-\tau\) 为 1 至 13。

用完整 \(Z=(e|_C)\) 和

\[
\mathscr Z=H^0(Z,N^3|_Z),\qquad
D_3:V\longrightarrow\mathscr Z
\tag{9}
\]

表示 R836 的真实 Euler 兼容映射。R928 的固定类是

\[
[(j_0,j_1,0)]\in\operatorname{coker}\mathcal T_J,\qquad
\mathcal T_J(V_0,V_1)
=(\operatorname{ev}_JV_0,\operatorname{ev}_JV_1,
D_3V_0-\operatorname{res}_ZV_1).
\tag{10}
\]

下文给这一个类的一条真实左行及其准确值。

## 2. 原正水平上的完整值空间

令 \(H_+\) 是原严格正水平，

\[
Z_+=C\cap H_+,\qquad e_+=C\cdot H_+,\qquad
\mathcal M_+=N^3(-Z_+).
\tag{11}
\]

Z₊ 使用完整 Cartier 交概形，包括重数、固定角端点、
原曲线奇点和剩余域；不只取互异几何点。
P₀ 不在 Z₊ 上。因而 \(\mathcal M_+\) 在 P₀ 的 jet
通过原包含 \(\mathcal M_+\hookrightarrow N^3\) 读取，
不引入一个新选的局部 frame。

R903(17) 在原正水平坐标 x=Y^(−1) 中是

\[
x^{3b}(\mathcal E-3b)G
 =-x\,\partial_x(x^{3b}G).
\]

原十九角框与这一式相容，所以对于每个真正的
\(G\in\mathcal H_3\)，都有

\[
\boxed{
(\mathcal EG-3bG)|_C\in H^0(C,\mathcal M_+).
}
\tag{12}
\]

这里不用 R903 关于齐次核单射的任何额外结论。
(12) 对全部原 H3 成立，不仅对齐次四块核成立。

每一个满足 \(D_3V_0=\operatorname{res}_ZV_1\) 的真实全局对
都由同一 \(G\in\mathcal H_3\) 实现，这是 R836 的全局提升定理。
故 (12) 等价地给

\[
\boxed{
V_1-3bV_0\in H^0(C,\mathcal M_+)
\quad\text{对全部真实兼容对。}
}
\tag{13}
\]

这不是说右边每个截面都可由兼容对实现；以下只使用该必要包含。

## 3. 由实际截面列构造一个确定的局部行

本注的正水平门是

\[
\boxed{K+e_+>3\kappa.}
\tag{14}
\]

因 \(\deg\mathcal M_+=3\kappa-e_+\)，(14) 使实际映射

\[
\operatorname{ev}_K:
H^0(C,\mathcal M_+)\longrightarrow k[t]/t^K
\tag{15}
\]

单射。确实，一个非零截面在 P₀ 消失到 K 阶，
其有效零除子的次数至少 K，不能大于所属线束次数。
该论证在原可能奇异的整曲线上仍成立：线束可逆、P₀ 光滑，
全零除子长度与线束次数相等；没有先正规化并删 conductor。

为避免把一个自由局部行冒充全局行，给出明确的完整列构造。
取 (15) 来源的任一真实 k 基 \(m_1,\ldots,m_n\)，在原 N³ frame
展开到 t^K；令

\[
A_{ij}=[t^j]m_i,\quad
0\le j<K,\qquad
c_i=[t^K]m_i.
\tag{16}
\]

A 为 n×K，因 (15) 单射而有全行秩 n。
取按列序的首组独立列 I，\(A_I\) 是 n×n 可逆矩阵。
定义对原全 J jet 的行

\[
\boxed{
\lambda_+(v)
 =[t^K]v-v_I A_I^{-1}c.
}
\tag{17}
\]

n=0 时，第二项定义为零。
I 只从真正的全部截面列选出，不从 forcing 中选择。
K<J 保 (17) 完全在原已付 J 窗口内。

对任意 \(m=\sum_i a_i m_i\)，其前缀满足
\(m_I=aA_I\)、\([t^K]m=ac\)，故

\[
\boxed{
\lambda_+(\operatorname{ev}_Jm)=0
\quad\text{对每个 }m\in H^0(C,\mathcal M_+).
}
\tag{18}
\]

同时

\[
\lambda_+(t^K u(t))=u(0)
\tag{19}
\]

对任意原单位 u 成立，因为其 t^K 以下的全部项为零。
(18) 是完整来源恒等式；不是随机测试、维数预测或任意局部 h₀。
换实际基不改变 (17) 的含义；即便换合法的前缀关系延拓，
(19) 也保持不变。

## 4. 同一个完整 Z 上的真实第三分量

置

\[
\lambda_0=-3b\lambda_+,\qquad\lambda_1=\lambda_+.
\tag{20}
\]

还必须构造同一 \(\nu\in\mathscr Z^\vee\)，满足 R928(26)，
不能只说 (17) 杀掉一部分局部数据。

原 R836 的完整商

\[
\mathscr Z=\mathcal H_3/(F\mathcal H_2+e\mathcal H_2)
\]

及 \(\mathcal H_3\twoheadrightarrow V\) 说明
\(\operatorname{res}_Z:V\to\mathscr Z\) 满射，且

\[
\ker(\operatorname{res}_Z)=e|_C\,H^0(C,N^2).
\tag{21}
\]

对于任意 \(U\in H^0(C,N^2)\)，取原全局提升 H∈H2。
将 (12) 用在 G=FH 上，可得

\[
e|_C\,U=(\mathcal E(FH)-3bFH)|_C
\in H^0(C,\mathcal M_+).
\]

所以由 (18)，\(\lambda_+\circ\operatorname{ev}_J\)
在 (21) 的全部核上为零。
于是唯一的完整 Z 行可直接定义为

\[
\boxed{
\nu(z)=\lambda_+(\operatorname{ev}_JV_z),
\qquad \operatorname{res}_ZV_z=z.
}
\tag{22}
\]

不同真实提升之差在 (21)，故该式选择无关；
Z 的非约化与边界分量没有被省略。
由定义即有

\[
\operatorname{res}_Z^\vee\nu
 =\operatorname{ev}_J^\vee\lambda_1.
\tag{23}
\]

再取任意 \(V_0\in V\) 的原 H3 提升 G，置 V₁=(EG)|C。
它们是真正兼容对，所以由 (13)、(18)，

\[
\nu(D_3V_0)
=\lambda_+(\operatorname{ev}_JV_1)
=3b\,\lambda_+(\operatorname{ev}_JV_0).
\]

因此

\[
\boxed{
\operatorname{ev}_J^\vee\lambda_0+D_3^\vee\nu=0,
\qquad
\operatorname{ev}_J^\vee\lambda_1-
\operatorname{res}_Z^\vee\nu=0.
}
\tag{24}
\]

这就是同一个完整原 \(\mathcal T_J\) 的真实左行。
没有替换 D3、没有挑选自由的 Z 值，也不需要先假有一个解。

## 5. 对固定 P 的准确值

把原 (6)、(7) 代入同一 (20)、(24)，准确得到

\[
\begin{aligned}
\lambda_0(j_0)+\lambda_1(j_1)
&=\lambda_+\bigl(\mathcal T_P
  -(\mathcal EB-3bB)|_C\bigr)\\
&=\boxed{-\frac{11}{a}\mathcal U_*(0)
   -\lambda_+\bigl((\mathcal EB-3bB)|_C\bigr).}
\end{aligned}
\tag{25}
\]

这是一般给定基点的完整 affine 值。
B 仍由原 P、R_b 的真除 p 分支读数确定；
不因为第一项为单位就删除第二项。

现在明确假定已经指定的原陪集满足

\[
\boxed{B\in\mathcal H_3.}
\tag{26}
\]

该条件可按原来源身份
\(\overline{R_b+\Delta}\in qt^2\mathcal H_3\)
核定；不能为通过本门临时改选其它陪集。
(26) 下，(12) 与 (18) 杀掉 (25) 的第二项，故

\[
\boxed{
\lambda_0(j_0)+\lambda_1(j_1)
=-\frac{11}{a}\mathcal U_*(0)\ne0.
}
\tag{27}
\]

p>211，且原 a、\(\mathcal U_*(0)\) 都是单位。
因此在 (1)–(4)、(14)、(26) 的准确范围中，

\[
\boxed{
[(j_0,j_1,0)]\ne0\quad\text{于原 }\operatorname{coker}\mathcal T_J.
}
\tag{28}
\]

从而这一既定原返回陪集没有 R928 的选定四行解，
更没有原完整 p³ 解，允许的 S 无论是全格还是受限格都不能修复。
这一步发生在同 H1 的剩余 normal 门之前；
不是以局部目标非零代替全局非零，而是已有 (24) 和实际 (27)。

若 (26) 未核定，则只保 (25) 的真实检验：
其值非零仍排这个给定陪集；值零仅表示这一行未排，
并不证明固定类为零，也不证明同 H1 或受限 S 可解。

## 6. 当前范围、去重和边界

R903 已给原齐次核的必要门 T+e₊≤3κ。
本注没有重复该核结论，而是对固定非齐次 P 给真正的左行和值。
由原负 fringe，

\[
\boxed{
K-T=11+\tau-d_0=13-(J-K)\in[0,12].
}
\tag{29}
\]

所以显示的条件可能落在

\[
\boxed{
T+e_+\le3\kappa<K+e_+,
}
\tag{30}
\]

其宽度至多 12。该条带并未被 R903 的旧齐次反门排掉；
也不要求 T>3κ。这里没有断言当前某个未经识别的 F 一定落入
(30)，而是精确给出同 P 可直接套用的实际参数门。

在 K+e₊=3κ 的等号处，(15) 可能出现零次数线束截面；
不能自动声称单射。本注保严格不等号。
当 τ≥d₀+2，K≥J，自然双 jet forcing 已退出；
此时不能继续使用 (17) 读取第 K 项。
τ=0、1 的自然陪集低行失败已由 R934 支付，不重复登记。

Z₊ 不与负水平消失除子直接相加。两端来自同一个 V₀、V₁，
R903(25) 的共同关系仍在；本注只使用正侧的一条真实来源包含。
原全 WD 的其它 R_b 陪集仍可能有抵消 (25) 的实际偏移，
故 (28) 不排全 K1 或所有原 R，亦不证明 ordinary / 无穷 p 主门。

依赖：R495/R836 原全截面、D3 与两值提升；R903(17) 原完整正水平；
R928(23)、(26) 同一全局兼容映射；R934 原固定双 jet 和真基点。
全部运算仍在原十九角与完整 Cartier 曲线上进行。


审阅：deep完整推导；root全文核并回查R903完整水平框、R836真实全商与两值提升、R928原左行符号。所有全局来源与一般B偏移均保，没有数学执行。原定稿SHA256 `51c283cdeca6a77798af786f0aab7756f55f0da6793e7bffcd58f624536f91fb`。

## 附A：完整原尾方向及全 J 仿射补门

[R937附A–B](R937-original-quadratic-horizontal-dual-and-same-H1-obstruction.md)
与所链完整证明已付同 q 的全部合法 Y_j（1≤j≤d₀−1）对本注
全 J 双 jet 行的零响应。故已实际核定的
B∈H3+span{t^{d₀−j}F⁴} 仍有本注原单位评价；不把这些 β₁ 非零
方向放进 K′。另在 J>3κ 时，用完整 ker(res_Z)=eH⁰(N²)
与 ev_J 的转置，直接构造真正 (λ₀,λ₁,ν) 行并付低 τ 的同一
非零 forcing，覆盖 T 截止后的至多十三位。所有一般 B 偏移与其它 WD 陪集保留。
