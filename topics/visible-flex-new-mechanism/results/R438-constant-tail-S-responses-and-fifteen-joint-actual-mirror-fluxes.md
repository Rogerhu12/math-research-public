# R438：S 常尾支路与同一实际镜对库的十五个内部通量

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、积分、求根、符号程序、秩或科学测试。**

[R436](R436-fifteen-self-directions-and-fourteen-joint-actual-degenerate-fluxes.md) 给十五个 formal self 方向，并在原完整复制库中实际联合支付十一左镜点和三个右镜点。其另一个 jet 比值条件可以支付第十五点，但不由既有母简单性自动成立。

本稿改用原 $S=s_0$ 的常数右尾，得到一个不需额外母假设的方向。它在全部左对应点为零，在右对应点准确给三次多项式。因此同一个已经固定的实际镜对库可联合支付 **十一左点加四个不同右点**；原 $J^+$ 保持，整个消-self 向量 $C$ 不被这些新增响应改变。对其它 C 的实际联合支付仍保 R435/R436 的原前提。

此外，原 K 轨道加 P、S 两支路在 universal 退化 jets 上恰给十八个 self current 方向。十八不是实际任意十八点的秩；本稿同时给出固定镜对全部对应副本上这个模块的准确十五维像。

## 1. S 的原 self、右尾与全圆两通道

采用与 [R432](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md) 相同的原右锚：
$$
p=u',\quad r=u'',\quad t=u''',\quad A_u=6pt-2r^2,
$$
$$
S(u,u)=J(xr^2).
\tag{1}
$$
这里 S 是原 E8 的 $s_0$，不是另一个自由 primitive。

对原 $c=0$ 第三核 $\tau$，R432(25)—(27)给
$$
\mathcal B_S\tau(u^2,0)=2K_u^\tau(S(u,u)),
$$
$$
\int_{\ell_u}^x p[\mathcal B_S\tau(u^2,0)]''
=2a_\tau\{pS''-rS'\}.
\tag{2}
$$
原 $S'=-xr^2,\ S''=-r^2-2xrt$，所以
$$
pS''-rS'=-pr^2+xr(r^2-2pt).
$$
在真实 $A_u=0$ 点，
$$
\boxed{\mathcal F_x(\mathcal B_S\tau;u)
=\frac23a_\tau r^2(xr-3p).}
\tag{3}
$$
式(2)的左常数由平零 jets 确定；没有把单包 S 的左尾删掉。
当 $r\ne0$ 时，(3)等于 $(x-3p/r)$ 乘 R436 的 P 支路 current；一般点直接使用(3)，不作除 r。

原 S 的右包左尾是常数
$$
p_S(n)=n_1.
\tag{4}
$$
对 $c=0$ 的局部第三算子，常数被完整 $\mathscr A_{\tau,u}$ 杀掉，原三重右积分的常数也为零。因此全部真正 suffix 项在此支路准确消失，而不是被当作可自由改选的平台。

沿原圆记
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
R_i=a_i^2-b_i^2,\quad T_i=a_i b_i.
$$
在任意包任意实际 A 根上，完整两通道为
$$
\boxed{
H_{d,i}(\mathcal B_S\tau)=a_i^3R_i\mathcal F_x(\mathcal B_S\tau;u_i),
\qquad
H_{e,i}(\mathcal B_S\tau)=-a_i^3T_i\mathcal F_x(\mathcal B_S\tau;u_i).
}
\tag{5}
$$
本列的外 collar 第二导数零，故(5)同时保留 R435 的真实 raw 平台规范。它不宣整个 self 输出左紧。

特别
$$
C_i:=R_iH_{e,i}+T_iH_{d,i}=0
\tag{6}
$$
对同一原圆全部包、全部点成立。
由 R432 的 whole-E 身份及全响应自然零，
$$
\boxed{\mathcal B_SZ_{c0}\subset\mathcal R\cap\ker E
\cap\ker J^+,\qquad C(\mathcal B_SZ_{c0})=0.}
\tag{7}
$$
这里 $J^+=(E,\mathcal A,\mathcal O)$ 使用 R433 的同一个实际共同观察。
(7)只陈述这些原 signed 响应，不将 universal 自然全零说成实际可建背景。

## 2. 七个 P/S self 方向与十八个 formal 方向

沿用 R432 的原基
$$
\begin{array}{c|c}
\tau&a_\tau\\ \hline
\sigma&p^2\\
\tau_0&A_u\\
\tau_1&xA_u+2pr\\
\tau_2&x^2A_u+4xpr-4p^2\\
\tau_3&x^3A_u+6x^2pr-4xp^2 .
\end{array}
\tag{8}
$$
置 $J_\tau=\mathcal B_P\tau$、$W_\tau=\mathcal B_S\tau$，并简写 $J_j,W_j$。R436 的四条 P 列为
$$
\begin{aligned}
\mathcal F(J_\sigma)&=\tfrac23p^2r^3,&
\mathcal F(J_1)&=\tfrac43pr^4,\\
\mathcal F(J_2)&=\tfrac83(xpr^4-p^2r^3),&
\mathcal F(J_3)&=4x^2pr^4-\tfrac83xp^2r^3.
\end{aligned}
\tag{9}
$$
由(3)，全部非盲 S 列准确为
$$
\boxed{
\begin{aligned}
\mathcal F(W_\sigma)&=\tfrac23xp^2r^3-2p^3r^2,\\
\mathcal F(W_1)&=\tfrac43xpr^4-4p^2r^3,\\
\mathcal F(W_2)&=\tfrac83(x^2pr^4-4xp^2r^3+3p^3r^2),\\
\mathcal F(W_3)&=4x^3pr^4-\tfrac{44}{3}x^2p^2r^3+8xp^3r^2 .
\end{aligned}}
\tag{10}
$$
$J_0,W_0$ 在 A 根上均盲；并且在这个 current 层面
$$
\mathcal F(W_1)=\tfrac12\mathcal F(J_2)-4\mathcal F(J_\sigma).
\tag{11}
$$
(11)不是成本算子的全函数身份。

取明确的十八列
$$
\mathscr M_{18}
=\operatorname{span}\{K_0,\ldots,K_{10},
J_\sigma,J_1,J_2,J_3,W_\sigma,W_2,W_3\}.
\tag{12}
$$
它们的 universal A 根 current 线性独立。R435 完整生成式的纯 $r^5$ 部分为
$-8(1-zx)^{10}r^5/45$；比较 $x^nr^5$ 先迫十一 K 系数全部为零。
余七列中，$pr^4$ 单独付 J1，$xpr^4,p^2r^3$ 付 J2/Jσ，最高 $x^3pr^4$ 付 W3。剩 J3、Wσ、W2 在
$(x^2pr^4,xp^2r^3,p^3r^2)$ 上，提出非零常数后是
$$
(3,-2,0),\qquad(0,1,-3),\qquad(1,-4,3),
$$
行列式为 $-21\ne0$。

这些多项式比较有与 R436 相同的真实有限 jet 见证：取 $p\ne0$、$t=r^2/(3p)$，再选四阶 jet 令 A 根简单。没有在不可实现的 $p=0,r\ne0$ 点求值。

因此(12)是十八个独立原成本，给十八个 formal self 方向。全部 P/S、$Z_{c0}$ 标签加 K 的 A 根 current 像也恰为这十八维，因为(11)及两个盲列已经列全。
这不判断这些标签之间除 current 之外是否还有别的完整响应信息。

如实际原型需真仿射闭包，使用
$$
\operatorname{span}\{K_0,\ldots,K_{10}\}
+\mathcal B_{\operatorname{span}(P,S)}Z_{c0}.
\tag{13}
$$
$NP=0,\ NS=P$ 和 R432 的完整 N 表使(13)平移稳定；原正伸缩按真权作用。增入的盲列不会改变本文的 A 根评价像。整个(13)仍保持(7)与全部 C 零。

## 3. 固定真实镜点、物理宽度和完整 K3

使用 R436 已固定的一组同宽对应副本，不另改母或移动实际根。
把共同物理宽度收入参考偶 u，选其原镜点 $\pm b$：
$$
u(-b)=u(b)=u_*,\quad
u'(-b)=p_*>0,\quad u'(b)=-p_*,
\quad u''(\pm b)=r_*>0.
\tag{14}
$$
这两个是 R431 最后母库中实际存在并被共同外区保持的 A 根；不假设母只有这一对根。

每个已有完整副本写作
$$
f=\rho_j a\,u(x-\xi_j),\quad
g=\rho_j\epsilon_j b_0\,u(x-\xi_j),\quad
x_j^\pm=\xi_j\pm b,
\tag{15}
$$
$\rho_j\ne0,\ a\ne0,\ R=a^2-b_0^2\ne0$。$\xi_j$ 是已经存在的真实中心。
如果原包是 $U((x-\xi)/w_0)$，则(14)里的 $p_*,r_*,b$ 分别是 $U'/w_0,U''/w_0^2,w_0b_{\rm ref}$。下面不能改用未经输运的母 jets。

简写
$$
s=\frac{p_*}{r_*},\quad h_*=\frac{u_*}{r_*},\quad
q_*=\frac43p_*r_*^4,\quad \kappa_*=-2q_*.
\tag{16}
$$
所有参数都由同一基点预先固定。

由 R435 原生成式取真实系数，前四条完整 current 是
$$
\begin{aligned}
F_0&=-\tfrac8{45}r^5,\\
F_1&=\tfrac{16}{9}xr^5,\\
F_2&=-16x^2r^5+\tfrac{32}{3}p^2r^3-\tfrac43ur^4,\\
F_3&=128x^3r^5-256xp^2r^3+\tfrac{320}{3}p^3r^2
+32upr^3+32xur^4.
\end{aligned}
\tag{17}
$$
这里 $F_n=\mathcal F_x(K_n)$。特别 K3 的两条含 u 项都保留。
在两侧镜点，F0/F1/F2 作为物理 x 的多项式相同，而
$$
F_3^-(x)=128r_*^5x^3+B_*x+C_*,
\quad F_3^+(x)=128r_*^5x^3+B_*x-C_*,
$$
$$
B_*=-256p_*^2r_*^3+32u_*r_*^4,\qquad
C_*=\tfrac{320}{3}p_*^3r_*^2+32u_*p_*r_*^3.
\tag{18}
$$
此处上标是镜点侧，不是把原 $\xi_j$ 误写成 x。

## 4. 新列在左族全零、在右族准确为三次

由(10)，W3 在左、右对应族分别为
$$
F_{W_3}^-(x)=q_*(3x^3-11sx^2+6s^2x),
$$
$$
F_{W_3}^+(x)=-q_*(3x^3+11sx^2+6s^2x).
\tag{19}
$$
定义一个完整原成本
$$
\boxed{
Q_3=\frac{s}{32}K_3+\frac{11s^2}{12}K_2+
\left(9s^3-\frac{9h_*s}{16}\right)K_1+
\left(\frac{295s^4}{4}-\frac{5h_*s^2}{4}\right)K_0.}
\tag{20}
$$
将(17)的四项逐次代入，得到
$$
F^-_{Q_3}(x)=F^-_{W_3}(x)
\tag{21}
$$
作为整个物理 x 多项式恒等，包括原常项。不是只匹配三次首项。

右侧只有 K3 常项变号，因此
$$
F^+_{W_3-Q_3}(x)
=\kappa_*\left(3x^3+6s^2x-\frac52s^3-\frac34h_*s\right).
\tag{22}
$$
取 R436 的三个原列
$$
\begin{aligned}
L_0&=J_1+\tfrac{15}{2}sK_0,\\
L_1&=J_2-\tfrac32sK_1-15s^2K_0,\\
L_2&=J_3+\tfrac14sK_2+\tfrac32s^2K_1+
(15s^3-\tfrac{15}{8}h_*s)K_0.
\end{aligned}
$$
其真实左 current 全零，右 current 是 $\kappa_*(1,2x,3x^2)$。
最后定义
$$
\boxed{
L_3=W_3-Q_3-3s^2L_1+
\left(\frac52s^3+\frac34h_*s\right)L_0.}
\tag{23}
$$
于是对全部已有对应副本，
$$
\boxed{
F^-_{L_j}=0\ (0\le j\le3),\qquad
(F^+_{L_0},F^+_{L_1},F^+_{L_2},F^+_{L_3})
=\kappa_*(1,2x,3x^2,3x^3).}
\tag{24}
$$
所有系数只选一次；没有为四个右点分别更换成本。
这些列在整个原圆上均保持 $J^+$ 与全部 C。

## 5. 同一库的真实十五行

从原已有完整 cell 的首包或末包对应组中，选十一个不同左点；在其中四个不同副本中再取其右镜点。原十二 cell 库已足够，不添加新的复制、宽度或中心。

这里完整 cell 是 R397/R435 已核的整个 R/T 编码圆经八包装得到的块；不是八个孤立同轴包。原编码在八包装以前已有
$\sum_iR_i\mu_i=\sum_iT_i\mu_i=0$，
每个复制的平方幅只乘这个零向量；三次差分另负责第三层。其后真实母纤维、宽度与所有后续完整块仍保这些原三矩身份。

按十一左行、四右行排列，取十五列
$$
K_0,\ldots,K_{10},L_0,L_1,L_2,L_3.
$$
完整原矩阵是
$$
\begin{pmatrix}
M_-&0\\
*&M_+
\end{pmatrix}.
\tag{25}
$$
$M_-$ 是 R435/R436 已付的真实同基点十一行矩阵，仍使用它的全部非最高项；不重算该旧 rank。
令四个右点的实际幅因子
$$
d_j=\rho_j^5a^3R\ne0.
$$
则(24)给
$$
M_+=\kappa_*\operatorname{diag}(d_j)
\begin{pmatrix}
1&2x_1^+&3(x_1^+)^2&3(x_1^+)^3\\
1&2x_2^+&3(x_2^+)^2&3(x_2^+)^3\\
1&2x_3^+&3(x_3^+)^2&3(x_3^+)^3\\
1&2x_4^+&3(x_4^+)^2&3(x_4^+)^3
\end{pmatrix},
$$
$$
\boxed{\det M_+
=18\kappa_*^4\left(\prod_{j=1}^4d_j\right)
\prod_{i<j}(x_j^+-x_i^+)\ne0.}
\tag{26}
$$
不同右位置是实际同宽副本的不同中心加同一个 b；不把不同 cap 点、不同宽度或任意可移动点混成同一矩阵。

由此原十五条 H 观察在同一个明确响应模块上满射。
R436 另外的比值条件(24)不再是这十五行结论的前提；它仍是该旧模块在另一个不同根上增加一行的独立准确条件，不被本文撤销。

## 6. 完整实际联合截面与全部基准

令 $\mathbf H_{15}$ 为(25)的十五个真实 raw 观察。由(7)、(25)，
$$
(J^+,\mathbf H_{15})(U)=J^+(U)\times\mathbb R^{15},
\quad
(J^+,\mathbf H_{15})(\mathcal R)=J^+(\mathcal R)\times\mathbb R^{15}.
\tag{27}
$$
这是同一个有限 profile 库、同一个右锚和同一个合法窗口的共同像。

R435 的原实际增强构造可用(25)替换末响应矩阵：原 J⁺ 响应基与十五列形成一个固定块三角基；S 支路的全部成本来自原 E8/Z 有限真原型。共享倒行、桥、闭 frame、保护芽和成本基准按原字一起安装，不把 signed 相加冒称实际路径可直接相加。

原型的完整 $J^+$ 商基准先校正；第二次商校正引起的全部十五 H 代价也原样保留。内部有限整数和所有原型先固定，最后对同一个
$$
n(a+Mt)+F(t,y)=y_{\rm resp}
$$
选一个有限 n 作紧目标 $C^1$ 收缩。Klein 仍对 $V_{\rm base}+4V_B$ 先减真实基准再除4。因此获得同一固定有限字的实际截面
$$
\boxed{J^+=y,\qquad\mathbf H_{15}=h.}
\tag{28}
$$
这不继承旧冻结几何的 whole-E、Morse 或其它未计目标。

对原圆全部其它 C，准确范围是：若已有同一库的 $(J^+,C)$ 实际截面，或 R435§5.1 的共同响应等像入口，则可从起点把它加入(27)—(28)，所有 prototype 的 C 基准继续保留，本文新增十五列不改任何 C。没有此前提时，(28)不单凭 C 对新增列零就宣所有 actual C 已付。

对本稿选取的完整 cell 首/末包，C 本来由原 E 因子化。因此 $J^+=0,\mathbf H_{15}=0$ 时，所选十五个点的两条 period 内部通量均零。其余包根、整包目标、平台仿射连接和同相位十三行仍不免费支付。

## 7. 同一有限组的 λ⁺ 核见证

原 $H_*$ 满足 $J^+(H_*)=0,\lambda_+(H_*)=1$。
取其十五条完整真实查询值，通过(25)减去唯一的十五列线性组合。
因为这些列都在原响应空间，
$$
J^+(\widetilde H_*)=0,\quad
\mathbf H_{15}(\widetilde H_*)=0,\quad
\lambda_+(\widetilde H_*)=1.
\tag{29}
$$
这里使用 H* 的原 self/history 真值，不把它们预置为零。
若还要其它 C 零，必须先按既有完整 C 响应像消 $C(H_*)$，再施上述不改 C 的修正。
(29)是同一有限组不能承载新 λ 障碍的 signed 见证；实际存在由(28)另行给出。

## 8. 固定镜对全部副本上的准确十五维像

记 R436 中 K 轨道的原左、右多项式为 $p_n^-(\xi),p_n^+(\xi)$。
左侧的十一个多项式定义唯一线性输运
$$
\mathsf T:\operatorname{Pol}_{\le10}\longrightarrow\operatorname{Pol}_{\le10},
\qquad\mathsf Tp_n^-=p_n^+ .
$$
它保真实 $x^\pm=\xi\pm b$、全部 u/p/r 常数及 K3 镜差。

对(12)及完整(13)，全部 normalized 镜对像恰为
$$
\boxed{
h^-(\xi)=P(\xi),\qquad
h^+(\xi)=\mathsf TP(\xi)+Q(\xi+b),\qquad
\deg P\le10,\quad\deg Q\le3.}
\tag{30}
$$
证明中 P/S 新列的 left 都至多三次；用 K0…K3 的完整左基消掉后，右残差仍至多三次。反过来(24)取得全部三次以下 Q，所以(30)既必要又充分。
实际读出乘回各个真实第五幅 $\rho_j^5a^3R$。

因此这个具体固定镜对族一旦含(25)的十五点，其 current rank 恰15；十八个 formal 方向中有三个在该整族上不可见。更多目标的准确条件是同一个 P 与同一个 Q 的评价，不是每个点独立十五维。
该限制只针对本文明确模块，不扩为整个 $\mathcal R\cap\ker E$ 或实际成本锥的障碍。

本稿完成了 S 原常尾的全 self 公式、十八个 formal 方向，以及同一实际镜对库十五个内部点的完整联合支付。全部不同根的 self/ordered 目标像和完整同规范 period，仍沿同一真实库继续。
