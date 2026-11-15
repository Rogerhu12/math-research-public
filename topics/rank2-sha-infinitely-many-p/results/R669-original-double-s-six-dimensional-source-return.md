# R669 — 两个原 S 共同来源的完整六维返回与双深度递推

日期：2026-11-15。**状态：已证明。**

本篇把 R666 的七条完整条件 A 来源和 R667 的完整 S5 矩核
重新合回同一个 standard even degree34 theta 空间。
结果是原两个 S 共同域各自只需六个准确系数；
它们对两个深度参数分别为至多六次多项式。
本文给直接合成公式、一个无 zeta 残项的曲线多项式算子，
以及只用原总次数至多36矩的整恢复。

所有公式都是原固定 q、真实共同门和原单位观察的公式。
外部与浅补域的完整和也因此得到同一个六维表示；
没有将它们单独赋零，也没有给新增 theta 基赋算术中央零。

## 1. 原来源、两个深度参数与全部周期

保持 R664–R668 的同一个 p、固定原 ray、b=17、lambda/kappa/Omega
及原 R594 整右逆。仍取
$$
N\in4\mathbf Z_{\ge1},\qquad n\ge N,\qquad
u=\kappa^N,\quad t=\kappa^{n-N}.
\tag{1}
$$
本文 Mellin 变量另用 w；u,t 是独立形式参数被代入 (1)，
不是重新选择多项式或新的算术来源。

原两个 S 观察为 Y0=A+Q、Y1=A+L，
N(A)=29、N(Q)=N(L)=5，三轴互相正交。
原 pair 的整个 Fourier 函数是
$$
\sigma(q+2l)\sigma(2q-l).
$$
仍令
$$
\mathcal H(A,q)=5A-29q,
$$
$$
e_0=-(170+117\omega)/9135,\qquad
e_1=-(170+291\omega)/9135,
$$
$$
h_0=-5-9\omega,\quad h_1=-5-3\omega,\quad
\epsilon_i=(-1)^i,
$$
$$
a_i(t)=e_i+h_it/315,\qquad
b_i(t)=-29e_i+34h_it/315 .
\tag{2}
$$
b_i(t) 是本篇方向系数，不是曲线常数 b。

R666 的完整归一条件来源写为
$$
F_{k,p}(u;Z)
=\sum_{h=0}^6 u^hF_{k,h,p}(Z),\qquad0\le k\le6,
$$
$$
F_{k,p}(\kappa^N;Z)
=\kappa^{kN}\lambda^{-N}\Omega^k
                   \mathcal A_{\Lambda_{k,N}}(Z).
\tag{3}
$$
全部 C 单位减深域项、两个 eta 符号、原 lambda/kappa 右逆
都已经在 F 中；不作模 p 替换。
F_k 属 whole odd S29，角型 k−2。

以 \(\mathfrak C_{i;N,n}\) 表示 R664 原 S 共同域的实际
Y_i 输出测度；其 unit Mellin 是 \(\mathcal C_{i,n}^S(w)\)。
本篇不把 T 的移动观察改成这个 Y_i。

## 2. 一个直接保整条来源的合成算子

对 whole S29 的截面 F，定义
$$
\boxed{
\mathcal J_k(F;a,b)(Z)
=\left.\partial_s^k
 \left[
 F(Z+5as)\,
 \sigma\bigl(Z+(2b-29a)s\bigr)\,
 \sigma\bigl(2Z-(b+58a)s\bigr)
 \right]\right|_{s=0}.
}
\tag{4}
$$
所有 sigma 都是原 sigma17；s 是独立微分变量。
没有截断其 Z 级数。

**定理1。** 原两个共同来源准确满足
$$
\boxed{
\mathcal A_{\mathfrak C_{i;N,n}}(Z)
=\epsilon_i\lambda^{2n+2N}
 \sum_{k=0}^6
 \mathcal J_k\bigl(F_{k,p}(\kappa^N;\cdot);
                  a_i(\kappa^{n-N}),\epsilon_i b_i(\kappa^{n-N})\bigr)(Z).
}
\tag{5}
$$

证明。R667 的有限 n S 核使用
$$
\alpha_i=e_i\kappa^N+h_i\kappa^n/315=u\,a_i(t),\qquad
\gamma_i=-29e_i\kappa^N+34h_i\kappa^n/315=u\,b_i(t).
$$
i=0 的实际多项式是
\((\alpha_i\mathcal H(A,Q)+\gamma_iL)^k\)；
i=1 在完整原 quarter 转置后给全局负号和
\(\gamma_i\mapsto-\gamma_i\)。这两个符号的来源不同，全部保留。

用 Fourier 规范
\(\mathcal A_\mu(Z)=\int e^{xZ/\Omega}d\mu\)，
这个 k 次物理矩恰给 \(\Omega^k u^k\) 乘 (4)。
代 (3) 后，\(u^k,\Omega^k\) 分别准确消掉
\(\kappa^{-kN},\Omega^{-k}\)，留下 lambda^N。
共同 Gamma_n 与 E 深 N 的完整核系数另为
\(\lambda^{2n}(\eta_A\lambda)^N\)。
由于 \(4\mid N,\eta_A^2=1\)，总系数就是
\(\lambda^{2n+2N}\)，得到 (5)。

原 S 逆观察中的 \((-1)^nY_i\) 不改变本式：
每一项的整体角型为零，特别输出测度是偶的。
这一点也由 (4) 中 F 的 k−2 型、pair 的型二和 k 次微分直接得出。
所以 (5) 是整条实际测度的身份，不只是 principal log 的身份。
证毕。

## 3. 准确 degree34、完整角型和六个基

(4) 的 z 向量范数为 29+1+4=34。
更关键的完整交叉项准确为
$$
29\cdot5a+(2b-29a)+2(-b-58a)=0 .
\tag{6}
$$
所以沿 Z 的任意原周期平移，sigma 准周期因子不含 s。
F 的 odd29 半特征与两个原 sigma 的完整半特征相乘，
恰为 standard even34；没有留下额外 flat twist。
因此对任意 k 次 s 微分，(4) 都是整个 S34 的真实截面。

F 的型为 k−2，而两个 sigma 的总型为二，
故 (4) 的型为零。设
$$
\boxed{
\Xi_j(Z)=\sigma(Z)^{34}x(Z)^{17-3j},
\qquad0\le j\le5.
}
\tag{7}
$$
它们的首项为
$$
\Xi_j(Z)=Z^{6j}(1+O(Z^6)).
\tag{8}
$$
这些恰是 S34 的整个型零子空间的一组基。
事实上截面除以 sigma34 后是仅在 O 有至多34阶极的椭圆函数，
唯一写为 P(x)+yQ(x)。
型零不容许 y 项，x 指数只能为
17,14,11,8,5,2；恰给 (7)。
这证明的是完整 theta 空间中的等式，不以有限 Taylor 相合代整个来源。

这些基确实给原 p 处的有界测度。
令
$$
D_\sigma=(\sigma')^2-\sigma\sigma''=\sigma^2x .
$$
则
$$
\boxed{\Xi_j=\sigma^{6j}D_\sigma^{17-3j}.}
\tag{9}
$$
sigma 及其有限阶导数按原周期规范对应有界测度及有界坐标矩；
乘积对应卷积。Omega 是单位，故 (9) 直接给其整有界性。
无需另加一个未经构造的 theta 测度。

由定理1，存在唯一六个系数多项式
$$
\boxed{
C_{i,j,p}(u,t)\in K[u,t],\qquad
\deg_u C_{i,j,p}\le6,\quad\deg_t C_{i,j,p}\le6,
}
\tag{10}
$$
使
$$
\boxed{
\mathcal A_{\mathfrak C_{i;N,n}}
=\epsilon_i\lambda^{2n+2N}
 \sum_{j=0}^5 C_{i,j,p}(\kappa^N,\kappa^{n-N})\Xi_j .
}
\tag{11}
$$
这里 K 为原 CM 系数域；系数仍依当前 p 的原 lambda/kappa。
它们不是跨 p 任意免费的全局列。

u 次数界来自 (3)。算子 (4) 的 k 次微分对 a,b 齐次 k 次，
而 (2) 对 t 一次，所以 t 次数至多 k≤6。
全部差测试同样适用；没有利用额外的中央零假设。

## 4. 不含 zeta 的准确曲线多项式计算

下面给 (10) 的有限直接算式。
在曲线坐标环
$$
\mathscr R=K[x,y]/(y^2-x^3-b)
$$
上使用原椭圆导数
$$
\partial_E=2y\partial_x+3x^2\partial_y.
$$
它和 sigma 的 logarithmic derivative 满足
\(\zeta'=-x\)，因此所有二阶以上的 sigma 对数导数
均是 \(\mathscr R\) 中的多项式。

由 R666 的完整基，将
$$
F_{k,p}(u;Z)=\sigma(Z)^{29}f_{k,p}(u;x(Z),y(Z)).
$$
f_k 的全部系数就是 R666 已给的准确33系数，
不是新未知的任意函数。

R667 的完整 S5 总矩除以其相应 Omega^ell 后为
\(\sigma^5B_\ell(x,y)\)，其中准确表是：

| ell | \(B_\ell(x,y)\) |
|---:|---|
| 0 | \(-2y\) |
| 1 | \(3x^2\) |
| 2 | \(4xy\) |
| 3 | \(36b\) |
| 4 | \(0\) |
| 5 | \(720bx\) |
| 6 | \(-240by\) |

特别 ell=6 项保留；它是整个 F12 行，不能删去。

对整数 h≥0 定义一个完全有限的双线性算子
$$
\boxed{
\begin{aligned}
\mathcal D_h(f,g)
=h![s^h]\Bigg\{&
 \exp\left(
 -\sum_{\nu=2}^{h}
 \frac{29\cdot5^\nu+5(-29)^\nu}{\nu!}
           (\partial_E^{\nu-2}x)s^\nu\right)\\
&\cdot\left(\sum_{a=0}^{h}\frac{5^a s^a}{a!}\partial_E^a f\right)
 \left(\sum_{b=0}^{h}\frac{(-29)^b s^b}{b!}\partial_E^b g\right)
 \Bigg\}\pmod{y^2-x^3-b}.
\end{aligned}
}
\tag{12}
$$
在 (12) 中指数只需展开到 s^h，不存在未保的无限尾。
其完整意义为
$$
\sigma(Z)^{34}\mathcal D_h(f,g)(x(Z),y(Z))
=
\left.\partial_s^h
 \left[
 \sigma(Z+5s)^{29}f(Z+5s)
 \sigma(Z-29s)^5g(Z-29s)
 \right]\right|_{s=0}.
\tag{13}
$$
这里 \(f(Z+5s)\) 表示沿原 x,y 函数代入，不是另一个独立曲线点。

证明 (13) 时，两块 sigma 的一次对数项因
29·5+5·(−29)=0 准确消失；
第 nu≥2 项则是
\(-[29·5^\nu+5(-29)^\nu]\partial_E^{\nu-2}x/\nu!\)。
其余两块是沿 \(\partial_E\) 的 Taylor 展开。
因此 (12) 保留全部 Gaussian 修正，并未令 zeta 为零。

例如
$$
\mathcal D_0(f,g)=fg,\qquad
\mathcal D_1(f,g)=5(\partial_Ef)g-29f(\partial_Eg),
$$
$$
\mathcal D_2(f,g)=25(\partial_E^2f)g
 -290(\partial_Ef)(\partial_Eg)+841f(\partial_E^2g)-4930xfg .
\tag{14}
$$
最后的 \(-4930xfg\) 正是不能删除的二阶交叉 Gaussian。

于是定义
$$
\boxed{
H_{i,p}(u,t;x,y)
=\sum_{k=0}^6\sum_{\ell=0}^{k}{k\choose\ell}
 a_i(t)^{k-\ell}(\epsilon_i b_i(t))^\ell\,
 \mathcal D_{k-\ell}(f_{k,p}(u),B_\ell).
}
\tag{15}
$$
完整角型及极帽已在第3节证明，因此把 (15) 在 \(\mathscr R\)
中约简后，准确只有
$$
\boxed{
H_{i,p}(u,t;x,y)
=\sum_{j=0}^5C_{i,j,p}(u,t)x^{17-3j}.
}
\tag{16}
$$
所有 y 项及其它 x 次数必须准确抵消；它们不是另加的约束。
(15)–(16) 是从原33系数到六系数的完整显式线性映射。
本篇不声称这张映射有某个未经计算的秩。

## 5. 原总次数至多36矩与整三角恢复

也可不用 (12)，直接在 (5) 右端读取低 Taylor 系数。
若已经恢复 j'<j 的 C 系数，则由 (8)
$$
\boxed{
C_{i,j,p}(u,t)
=[Z^{6j}]\sum_{k=0}^6
 \mathcal J_k(F_{k,p}(u);a_i(t),\epsilon_i b_i(t))
-\sum_{j'<j}C_{i,j',p}(u,t)[Z^{6j}]\Xi_{j'} .
}
\tag{17}
$$
每个三角对角都是一，故没有小除数问题。

恢复只用 Z 次数至多30。
原共同来源的 carry 总次数仍为六；物理总矩因此至多
$$
30+6=36.
$$
等价地，R666 的 F_k 已用四输入次数6−k的矩，
(4) 另读 k 次伴随矩及至多30次 Y 矩，合计不超过36。
它们全部由同一个原六 sigma 及 C 平均给出。
全 C 单位补域通过 (3) 原样进入，未作有限阶替换。

原整多项式流给这些低 jet 的 Hurwitz 系数整，
所以只增加至多36!的分母；本题 p>101 以及原固定坏集
已经排除它们及所有显示几何分母。
因此 C 的所有 u,t 系数在原 \(\mathcal O\) 中。
本篇使用这个单位三角恢复，不把在不同深度采样的 Vandermonde
逆误称为整单位。

## 6. 同一实际来源的两个深度递推

固定 N，令 \(\mathsf S_n\) 表示 n→n+1。
由 (10)–(11) 的 t 次数界，整条来源准确满足
$$
\boxed{
\prod_{a=0}^{6}(\mathsf S_n-\lambda^2\kappa^a)
              \mathfrak C_{i;N,n}=0,\qquad n\ge N.
}
\tag{18}
$$
这是来源身份，所以可对同一个固定 unit Mellin 测试、
其质量和中央导数使用。
它可用于对真正双 Y 共同来源作准确七步过滤；
这不删除任何实际外部。

另一方向，固定整数 ell≥0，写
$$
N=4r,\qquad n=4r+\ell,\qquad r\ge1 .
$$
此时 t=kappa^ell 固定，而 u=kappa^(4r)。
令 \(\mathsf S_r\) 表示 r→r+1，则
$$
\boxed{
\prod_{h=0}^{6}(\mathsf S_r-\lambda^{16}\kappa^{4h})
              \mathfrak C_{i;4r,4r+\ell}=0 .
}
\tag{19}
$$
(19) 是与 R668 正浅层同型的真实七阶递推；
两者的域不同，不能仅因特征根相同就相减或互换。

形式来源等式也是有界测度等式：全部 Fourier 系数为零时，
全部多项式矩为零，继而由多项式在 \(\mathbf Z_p\) 连续函数中的稠密性
得差测度为零。这里都是有限组合，不用未经一致控制的测度极限。

T 的实际观察含 \(w_i\kappa^N\mathcal E\) 等移动项。
(18)–(19) 没有把那些项冻结，因而没有直接赋给 T 同一个有限递推。

## 7. 回到原 S 中央行和完整外部补偿

令 \(\nu_{\Xi_j}\) 是 (9) 的实际有界测度，并定义六个固定 p 的观察
$$
M_{j,p}(w)=
\int_{\mathbf Z_p^\times}\langle x\rangle^{d_pw}\,d\nu_{\Xi_j}(x).
\tag{20}
$$
原 S 截面是同一个
$$
S=\sigma^{34}x^2P_4(x^3)
=\sum_{j=1}^5s_j\Xi_j ,
\tag{21}
$$
s_j 由原 P4 唯一给出，并保原 Fourier/period 的整体规范。
所以
$$
\boxed{J_S(w)=\sum_{j=1}^5s_jM_{j,p}(w).}
\tag{22}
$$
s0=0；没有将另外五个独立 M_j 的中央导数赋零。

由 (11)，两个实际共同 Mellin 行为
$$
\boxed{
\mathcal C_{i,n}^S(w)
=\epsilon_i\lambda^{2n+2N}
 \sum_{j=0}^5C_{i,j,p}(\kappa^N,\kappa^{n-N})M_{j,p}(w).
}
\tag{23}
$$
设 \(\mathcal L_{i,n}^S\) 是 R664 的完整浅域之和
（包括 R668 的第零层），\(\mathcal O_{i,n}^S\) 是原 Y 外部。
原总行准确为 \(\epsilon_i\lambda^n\beta^N J_S\)，
而 \(4\mid N\) 给 beta^N=lambda^N。
因此同一完整外部与浅域之和准确满足
$$
\boxed{
\mathcal O_{i,n}^S(w)+\mathcal L_{i,n}^S(w)
=\epsilon_i\lambda^{n+N}
 \sum_{j=0}^5
 \left[s_j-\lambda^{n+N}
 C_{i,j,p}(\kappa^N,\kappa^{n-N})\right]M_{j,p}(w).
}
\tag{24}
$$
这是完整补域的实际返回，保 w=0 质量和其全部 log 导数。
只有这个完整和由 (24) 表示；它不分别给每个浅层或每条外部
一个可互换的常系数表示。

特别若原 \(J'_S(0)=0\)，只知道
$$
\sum_{j=1}^5s_jM'_{j,p}(0)=0.
$$
(23)–(24) 仍可非零并准确互补。
对 R667 的完整 pi4 零差测试，s 向量本来就是零；
(24) 相应是全补域等于负的共同域。
这解释了该差测试为何可有非零条件来源而无新的算术零。

本篇新增的是同一原 S34 上的实际六维系数、全周期消去、
无 zeta 的有限合成以及两个准确深度递推。
下一步若要用它证明中央非零，必须再付这些六个原观察之间的
真实算术关系，或在完全相同测试上控制 (24) 的完整补域；
不能用六维来源本身当作六条中央零。
固定曲线的无穷不同 p 结论仍未完成。

主要依赖：
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R666](R666-original-conditional-a-sources-and-exact-depth-recurrence.md)；
[R667](R667-original-kernel-visible-mass-and-seven-source-contraction.md)；
[R668](R668-original-double-s-shallow-annuli-and-exterior-words.md)。
