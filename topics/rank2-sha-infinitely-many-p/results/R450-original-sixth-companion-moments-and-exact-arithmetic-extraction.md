# R450 — 原第六阶伴随矩的满秩与含 U 的算术来源准确抽回

日期：2026-11-14。**状态：已证明。** 在 R445、R448 保留原独立
sigma 输入的同一个三变量来源中，六条真正含 $U$ 的六次矩
$X^{6-j}U^j$、$1\le j\le6$，准确张成第一输出的整个六维型零
theta 空间。本文给全部七列、完整特征零证明、三个固定提取多项式
以及整性常数；不是仅在原点检查有限阶的来源猜测。

其中一个由 $U$ 整除的固定六次测试，完整返回原算术来源 $S$。
它在原目标斜线 $U=280X$ 上不消失，且在当前每个普通素数处为
单位倍的 $X^6$。对 R441 的同一真实同深管，此测试的中央仍准确
具有赋值 $5n$；全部法向贡献已计入，不能仅用斜线取值推出此结论。
另外两条测试分别准确返回 R307 已识别的两个秩零参考。

经 R448 的整逆，原 $J'_S$ 还可写成保 $U$ 的完整 carry 行。
本文不将完整算术中央的零分配给目标斜管或删除其补域；主目标未完成。

## 1. 原完整来源、周期和矩规范

保持 R439、R445、R448 的同一固定 ray、$b=17$ 和原周期 $\Omega$：
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\quad v_p(\kappa)=1,
\qquad p>19,\quad p\equiv7\pmod{64}.
\tag{1}
$$
所有输入、输出都保持 R448 的原定义：
$$
Y=c+Z,\quad X=-c+H,\quad
W=Z+H,\quad Q=9Z-17H,\quad U=Q-280c.
\tag{2}
$$
其同一个完整生成函数为
$$
\boxed{\begin{aligned}
\Phi_0(y,v,u)
 &=\sigma(y-v-280u)\mathcal L^{\rm phys}(y+9u,v-17u)\\
 &=\frac{\sigma(y-v-280u)}{\sigma(y-v+26u)}
                          \mathcal K_0(y+9u,v-17u).
\end{aligned}}
\tag{3}
$$
第二行只用于局部计算；第一行是已付的完整全纯整来源。
R448 已证明
$\Phi_0\in\mathcal S_{34}\boxtimes\mathcal S_{18}
\boxtimes\mathcal S_{85680}$，无平坦 twist。

以下 $x=x(y)$ 是椭圆函数，$X$ 始终是 (2) 的物理输出。
对 $0\le j\le6$，定义一个完整第一输出来源 $T_{j,b}$：
$$
\boxed{
\nu_{T_{j,b}}=(Y)_*\left(
  (X/\Omega)^{6-j}(U/\Omega)^j\,\nu_{\Phi_0}\right).}
\tag{4}
$$
所以来源计算必须乘 $(6-j)!j!$。除以 $\Omega^6$ 是同一个原
周期下的矩规范，没有重选周期或输入测度。

## 2. 七列完整 theta 来源

写 $M=(M_{aj})_{0\le a\le5,\,0\le j\le6}$。全部来源准确是
$$
\boxed{
T_{j,b}(y)=\sigma(y)^{34}
       \sum_{a=0}^5 M_{aj}\,b^{5-a}x(y)^{2+3a}.}
\tag{5}
$$
为避免分数遮蔽系数，以下列出整数矩阵 $N=7M$，分成两块：
$$
N_{[:,0:4]}=
\begin{pmatrix}
-1916928&-12533760&-1136590848&62616158208\\
-1198080&-219340800&-3767353344&360524519424\\
-179712&-207394560&-2900897280&319930960896\\
-793728&2741760&-423714816&26223641856\\
104832&3329280&-34519104&-3167868672\\
0&0&18144&3238704
\end{pmatrix},
\tag{6}
$$
$$
N_{[:,4:7]}=
\begin{pmatrix}
-5259536695296&-850457378488320&-214570333232824320\\
-17231254069248&-192496870195200&-148416735012618240\\
-12917843601408&588924520611840&126743553779834880\\
-747641369088&21854791434240&87447430221557760\\
9209180160&-57769992829440&-39424626143285760\\
-201724992&8019648000&-225566208000
\end{pmatrix}.
\tag{7}
$$
这里第一个块的列是 $j=0,1,2,3$，第二个块是 $j=4,5,6$；
每块的行均按 $x^2,x^5,x^8,x^{11},x^{14},x^{17}$ 排列。

第一列准确还原 R441：
$$
\boxed{T_{0,b}=14976bS_b.}
\tag{8}
$$
另一方面，$T_{6,b}(0)=-32223744000$。因此含 $U$ 的完整行
确实不全是 $S$ 的倍数；不能把原中央零无条件扩张到全部这些行。

## 3. 为什么有限计算支付整个第一输出函数

记 $\mathcal K_0=-2(S\otimes G_{18}-C_{34}\otimes F_{18})/3$，
并写
$$
S=\sigma^{34}P_S(x),\quad C_{34}=\sigma^{34}P_C(x),
$$
$$
\begin{aligned}
P_S(x)&=x^2\left(x^{12}-\frac{53b}{7}x^9-
 \frac{12b^2}{7}x^6-\frac{80b^3}{7}x^3-\frac{128b^4}{7}\right),\\
P_C(x)&=x(x^3+b)(x^3-8b)
                (x^9-30bx^6-144b^2x^3-32b^3).
\end{aligned}
\tag{9}
$$
在椭圆函数环
$\mathbf Q(b)[x,\mathfrak y]/(\mathfrak y^2-x^3-b)$ 上用真实导子
$$
\partial x=2\mathfrak y,\qquad \partial\mathfrak y=3x^2.
\tag{10}
$$
暂令 $v,u$ 同时乘一个形式参数 $t$。将 (3) 中的
$\sigma(y+9tu)^{34}$ 提出 $\sigma(y)^{34}$，它与 sigma 比的
一次 $\zeta(y)$ 项准确抵消：$34\cdot9-280-26=0$。
余下的完整六阶 frame 是
$$
\exp\left(\sum_{k=2}^6 e_kt^k+O(t^7)\right),\qquad
e_k=\frac{\zeta^{(k-1)}(y)}{k!}
       \{34(9u)^k+(-v-280u)^k-(-v+26u)^k\},
\tag{11}
$$
其中按 $k=2,\ldots,6$，真实导数依次为
$$
-x,\quad-2\mathfrak y,\quad-6x^2,\quad-24x\mathfrak y,
\quad-24(5x^3+2b).
\tag{12}
$$
令该指数的 $t^k$ 系数为 $E_k$。实际用到的全部系数是
$$
\begin{gathered}
E_0=1,\ E_1=0,\ E_2=e_2,\ E_3=e_3,\
E_4=e_4+e_2^2/2,\quad E_5=e_5+e_2e_3,\\
E_6=e_6+e_2e_4+e_3^2/2+e_2^3/6.
\end{gathered}
\tag{13}
$$
原 $F_{18}(z)=z^4+O(z^{10})$、
$G_{18}(z)=1-156bz^6/5+O(z^{12})$。所以 (3) 除去
$\sigma(y)^{34}$ 后的全部 $t^6$ 系数，准确为
$$
\boxed{\begin{aligned}
-\frac23\Bigg[&\sum_{k=0}^6
 E_{6-k}\frac{(9u)^k}{k!}\partial^kP_S
 -\frac{156b}{5}(v-17u)^6P_S\\
 &-(v-17u)^4\left\{E_2P_C+
                         \frac{(9u)^2}{2}\partial^2P_C\right\}\Bigg].
\end{aligned}}
\tag{14}
$$
由 (10) 约化后，所有 $\mathfrak y$ 项消失，只有
$x^{2+3a}$、$0\le a\le5$。读取 $v^{6-j}u^j$ 并乘两个矩阶乘，
逐项就是 (5)–(7)。这整个计算把 $y$ 保留为椭圆变量，因而证明
的是完整函数 (5)，不是先截断 $y$ 再认定来源。

脚本在 $b=1$ 完成有理环运算。对 $\beta^6=b$，原完整来源的
齐次式为 $\Phi_{0,b}(y,v,u)=\beta^{-6}
\Phi_{0,1}(\beta y,\beta v,\beta u)$。取另两轴六次导数后，
第 $a$ 个 theta 基向量的系数恰乘 $b^{5-a}$，证明 (5) 对原
$b=17$ 的全部系数；辅助六次根已消除。

## 4. 六条正 U 次数的整满秩

取 $M_+=M_{[:,1:7]}$。精确行列式是
$$
\boxed{
\det M_+=-
\frac{2^{59}3^{53}5^3 17^4\cdot4357\cdot501843101759}{7^5}.}
\tag{15}
$$
所以这六列在特征零满秩。除 $2,3,5,7,17,4357,501843101759$
之外，它还是整个六维 theta 格的整基（另有 (5) 的单位 $b$ 行缩放）。

当前素数已满足 $p>19$、$p\equiv7\pmod{64}$；而两个额外素数
分别为 $5,63\pmod{64}$。故**在当前每个素数处六列都整满秩**，
不用进一步缩小原 ray，也不引入随 $p$ 变化的矩次数。

## 5. 三个由 U 整除的固定提取多项式

用独立变量 $\xi,\upsilon$ 表示测试的两个参数。对于下表的三行，
定义
$$
\widehat h_k(\xi,\upsilon)=\frac1{D_k}
       \sum_{j=1}^6 n_{k,j}\xi^{6-j}\upsilon^j.
\tag{16}
$$
准确整数如下；每个六元组按 $j=1,\ldots,6$ 排列：

$$
\begin{aligned}
D_S={}&6851361798915816222720,\\
(n_{S,j})={}&(-2356384735107984,-69135664184520,
 -4247484553360,-674343960,1753978614,-3583957),\\[2pt]
D_3={}&330527829137401987038720,\\
(n_{3,j})={}&(486398961296147196848,-134871942541360977640,
 -5434379967790044880,-96540113818516160,
 361509955872958,55756639231),\\[2pt]
D_5={}&2809486547667916889829120,\\
(n_{5,j})={}&(5568058069140943116080,-1371591423898677910120,
 -56265692937514802560,-985587506970570080,
 3506162283999094,688639936231).
\end{aligned}
\tag{17}
$$
分母的全部分解为
$$
\begin{aligned}
D_S&=2^{12}3^2 5\cdot17\cdot4357\cdot501843101759,\\
D_3&=2^9 3^{10}5\cdot4357\cdot501843101759,\\
D_5&=2^8 3^{10}5\cdot17\cdot4357\cdot501843101759.
\end{aligned}
\tag{18}
$$
所有测试在当前普通处都整。定义最终原测试为
$$
\boxed{
h_S=b^{-1}\widehat h_S,
\qquad h_3=\widehat h_3,
\qquad h_5=\widehat h_5.}
\tag{19}
$$
它们均由 $\upsilon$ 整除。把 (17) 直接乘入 $M_+$，分别得到
$$
\begin{gathered}
(-128/7,-80/7,-12/7,-53/7,1,0)^{\mathsf t},\\
(-2048,12032,8128,400,-208,1)^{\mathsf t},\\
(1024,-6784,-14912,-272,272,1)^{\mathsf t}.
\end{gathered}
\tag{20}
$$
由 (5) 的 $b$ 权，第一行正好多一个 $b$，已由 (19) 除掉。
因此完整测度身份是
$$
\boxed{\begin{aligned}
(Y)_*\{h_S(X/\Omega,U/\Omega)\nu_{\Phi_0}\}&=\nu_S,\\
(Y)_*\{h_3(X/\Omega,U/\Omega)\nu_{\Phi_0}\}&=\nu_{H_{3,17}},\\
(Y)_*\{h_5(X/\Omega,U/\Omega)\nu_{\Phi_0}\}&=\nu_{H_{5,17}}.
\end{aligned}}
\tag{21}
$$
后两条是 R307 的原共周期参考，分别对应 $E_{17^3}$、$E_{17^5}$；
不是按质量或原点型新猜的算术来源。

特别，对整条原 principal 参数 $z$，
$$
\boxed{\Gamma_0(z;h_S(X/\Omega,U/\Omega))=J_S(z),}
\tag{22}
$$
另两行分别为 $J_{H_{3,17}}(z),J_{H_{5,17}}(z)$。它们的质量
分别为 $0,1-\lambda,1-\lambda$；两个参考的中央导数仍未被
其非零质量确定。式 (21) 比只在中央的一条线性关系更强：任何
连续的第一输出测试都可使用。

## 6. 目标斜线上的准确值与法向阶

对原斜线，直接从 (17) 得
$$
\boxed{
h_S(\xi,280\xi)=
\frac{1856440488328178557}{10705252810805962848\,b}\,\xi^6.}
\tag{23}
$$
分子的准确分解是
$$
1856440488328178557=7^3\cdot181\cdot42131\cdot92863\cdot7643;
$$
分母（未计 $b$）为
$2^5 3^2 17\cdot4357\cdot501843101759$。
四个新分子素数模 $64$ 依次为 $53,19,63,27$，均不等于七。
所以 (23) 的比例在当前全部素数处都是单位。

特别，$h_S$ 沿 $\upsilon-280\xi=0$ 的法向消失阶为零。
“由 $U$ 整除”并不使它在这个非零单位斜线上消失。
对真实物理参数，(23) 是
$h_S(X/\Omega,280X/\Omega)=r_SX^6/(b\Omega^6)$，
其中 $r_S$ 为显示的有理数。

## 7. 同一真实深管中，全部五阶贡献仍给单位

只用 (23) 不能计算深管中央，因为法向 Taylor 项也可能在同一
五阶参与。以下保留全部项。

令
$$
\mathscr D_n=\{Z,H\in p^n,\ c\text{ 单位}\}
=\{X\text{ 单位},W\in p^n,U-280X\in p^n\}.
\tag{24}
$$
第二个等式是 R448 的同一个真实输入域。对于正偶数 $n$，R439
给残余双输出的整个同深返回 $\lambda^{2n}[\kappa^n,\kappa^n]_*$。
故在 (24) 测试第一中央与本篇 $h_S$，其值为
$$
\mathcal C_{S,n}=\lambda^{2n}\mathcal A_S(\kappa^n),
\tag{25}
$$
其中
$$
\begin{aligned}
\mathcal A_S(T)=d\int_{c\ {\rm unit}}\int
 &\log_p\langle c+TZ\rangle\\
 &\cdot h_S\left(\frac{-c+TH}{\Omega},
       \frac{-280c+T(9Z-17H)}{\Omega}\right)
                        d\nu_{\mathcal L}^{\rm phys}d\nu_\sigma(c),
\qquad d=p-1.
\end{aligned}
\tag{26}
$$

原残余的完整首项为
$$
\mathcal L^{\rm phys}(y,v)
=-\frac23(y^5+y^4v+y^3v^2+y^2v^3)+O_{\rm total}(11).
\tag{27}
$$
只有总次数 $5\pmod6$ 的矩可能非零。特别总次数不超过六时，
仅有 (27) 显示的四个五次矩。

为把所有法向项明确列入，定义一个完全有限的泛函
$$
\mathfrak m_5(P)=
-\frac23\sum_{j=0}^3(5-j)!j!\,[Z^{5-j}H^j]P.
\tag{28}
$$
记
$q_S(T)=\widehat h_S(-1+TH,-280+T(9Z-17H))$。精确有理计算给
$$
\boxed{
\mathfrak m_5([T^5]q_S)=0,\qquad
\mathfrak m_5([T^5]\log(1+TZ)q_S)
=\alpha_S:=-\frac{480763982085139011763}{107052528108059628480}.}
\tag{29}
$$
这里第二个式子只使用 $\log(1+TZ)$ 的一至五次项，已经包含
测试的每一个法向 Taylor 项。

第一式还可由完整来源质量直接解释：$h_S$ 的六次矩抽回 $S$，
质量为零；sigma 的质量为零、首非零矩是一次，而残余首非零矩
为五次，所以全部六次质量只能来自该五次式。因测试次数只有六，
(27) 还说明 (26) 的整个 $\log_p\langle c\rangle$ 项准确为零，
不是仅模 $p$ 删除它。

由 $I_1^\times(\sigma)=(1-\lambda_\sigma\kappa)\Omega$，现在得到
$$
\boxed{
[T^5]\mathcal A_S
=\frac{d\alpha_S}{b\Omega}I_1^\times(\sigma)
=\frac{d\alpha_S}{b}(1-\lambda_\sigma\kappa).}
\tag{30}
$$
分子的绝对值准确分解为
$$
480763982085139011763=7\cdot1093\cdot1431421\cdot43898162053;
$$
分母为 $2^6 3^2 5\cdot17\cdot4357\cdot501843101759$。
三个额外分子素数模 $64$ 为 $5,61,5$。所以 (30) 在当前每个
素数处都是单位。

作为完整质量核对，同一计算对 $\widehat h_3,\widehat h_5$ 给
(29) 第一式的值均为一；其原 $\log c$ 项必须保留。
全部系数和另两条非 log 五阶值保存在精确 JSON 中。

测试系数整，所有单位输入矩和残余矩有界。对 $k>5$，(26) 中的
唯一可能非单位分母来自 $\log(1+TZ/c)$ 的 $1/(k-j)$，其中
$0\le j\le6$。因此
$$
v_p([T^k]\mathcal A_S)\ge-\lfloor\log_p k\rfloor.
\tag{31}
$$
对 $p>19,n\ge1,k>5$，有
$kn-\lfloor\log_p k\rfloor>5n$。结合 (30)，严格得到
$$
\boxed{v_p(\mathcal C_{S,n})=5n
\quad\text{对每个正偶数 }n.}
\tag{32}
$$
这是同一个原 $S$ 完整提取测试在真实目标管上的非零。
原完整中央仍是
$$
\boxed{J'_S(0)=\mathcal C_{S,n}+\mathcal C_{S,n}^{\rm outside}.}
\tag{33}
$$
补域没有删去；(32) 本身不证明左侧非零。

## 8. 保 U 的算术 carry 返回，可写成有限显式测试

在以下公式中把 $h_S$ 理解为物理测试
$h_S(X/\Omega,U/\Omega)$。R448 的算子
$\mathcal Sh=h(X,\kappa U)$ 给本篇测试的整逆为有限多项式：
$$
\boxed{
\mathcal Rh_S=
\frac1{bD_S}\sum_{j=1}^6
 \frac{n_{S,j}}{1-\lambda^2\kappa^{2j}}
       (X/\Omega)^{6-j}(U/\Omega)^j.}
\tag{34}
$$
全部分母是单位；没有 $U^0$ 项，也不必在这里求无限级数。
原两条第一层 carry 的完整中央准确给
$$
\boxed{
B'_0(0;\mathcal Rh_S)
-\eta\lambda B'_1(0;\mathcal S\mathcal Rh_S)
=\lambda J'_S(0).}
\tag{35}
$$
保 $U$ 的另一种写法只需同一原来源的两层 carry。令
$$
\mathfrak g^U_{0,2}
=(W,A/\kappa^2,U)_*
 \left(\mathbf1_{\{A\in p^2,\,(Q,c)\notin p^2\mathbf Z_p^2\}}
                 \nu_{\Phi_0}\right).
$$
R445 的完整三轴公式给
$$
\mathfrak g^U_{0,2}
=\lambda^2\nu_{\Phi_0}-
                  \lambda^4[1,1,\kappa^2]_*\nu_{\Phi_0}.
\tag{36}
$$
在推前坐标中写 $\widetilde A=A/\kappa^2$，并用
$Y'=(17W+\widetilde A)/26$、$X'=(9W-\widetilde A)/26$
测试第一 principal 中央和
$\mathcal Rh_S(X',U)$，(34)–(36) 准确给
$$
\boxed{\mathfrak g^U_{0,2}
 [\mathbf1_{Y'\ {\rm unit}}d\log_p\langle Y'\rangle
                            \mathcal Rh_S(X',U)]
=\lambda^2J'_S(0).}
\tag{37}
$$
这是一条保原 $U$ 的完整算术 carry 行，没有额外未知来源中央。

此外，$\mathcal Rh_S-h_S$ 的所有系数在 $p^2\mathcal O$ 中。
按 (27)–(31) 重新读取同深域，五阶单位不变、此前仍无低阶项，
所以本篇 (32) 对 $\mathcal Rh_S$ 同样成立。R445 的真实两层
运输将它送进 (36) 内的明确斜管，值另乘 $\lambda^2$，赋值仍为
$5n$。该内部斜管条件是
$$
W\in p^n,\qquad
140A/\kappa^2+13U\in p^n,\qquad
A/\kappa^2-U\text{ 单位}.
\tag{38}
$$
原 $Q,c$ 在这里都为单位、$v_p(A)=2$。
完整 (37) 仍包含 (38) 的真实补域；不能从其算术返回免费推出
每条内部斜管零。

## 复核文件与依赖

[精确脚本](../scripts/check-r450-original-sixth-companion-moments.py)
从 (9)–(14) 重建全部来源，准确核验七列、行列式、三条提取、
斜线值和完整五阶式；不读取缓存矩阵或作点值插值。
[全部有理系数](../scripts/check-r450-original-sixth-companion-moments.json)
包含矩阵、分解、三个多项式及每条五阶常数。

- [R445：同一原 sigma 保留、完整三轴及真实两层运输](R445-original-sigma-retained-three-coordinate-core-and-four-state-carry.md)。
- [R448：物理三张量、保 U 反射与联合 principal carry](R448-original-retained-companion-reflection-and-joint-principal-carry.md)。
- [R441：原残余首五阶、全部同深返回及高尾估计](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
- [R424：原 F/G、小核及完整 Bezout 因子](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R307：原 S 与两个已识别的共周期秩零参考](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
- [R447：另一组固定 degree18 参考测试及其完整算术返回](R447-original-two-reference-intersection-and-fixed-degree18-tests.md)。
