# R239 — 第三条实际秩二曲线、十六格 dyadic 线与原四项 theta 运输

日期：2026-11-13。**状态：以下精确秩、实际有限向量、四项原 theta 群运输、共同整行及完整中央半因子接口已证明。尚未证明三条秩二曲线的完整中央导数在无穷多个素数上不同时消失。**

本篇把 [R112](R112-e34-dyadic-theta-and-two-rank-two-rows.md) 的实际有限池扩大为
$$
E_{17}:y^2=x^3-17x,\qquad E_{34}:y^2=x^3-1156x,\qquad
\boxed{E_{136}:y^2=x^3-136x.}
$$
下标 $136$ 在本篇表示方程中的四次扭曲参数；不表示二次扭曲 $136^2$。
新曲线在同一个原 theta 图中的像由四个准确十六挠平移给出，
并非仅因 theta 空间维数相同而作的识别。

## 1. 不依赖数表的精确秩二证书

令 $E^+:y^2=x^3+34x$。核为 $(0,0)$ 的实际二同源是
$$
\phi:E^+\longrightarrow E_{136},\qquad
(x,y)\longmapsto\left(x+\frac{34}{x},
 y\left(1-\frac{34}{x^2}\right)\right).
\tag{1}
$$
取
$$
P=(-8,24)\in E_{136}(\mathbb Q),\qquad Q=(8,28)\in E^+(\mathbb Q),
\quad \phi(Q)=(49/4,105/8).
$$
对 $E_b:y^2=x^3+bx$，二同源下降的同态为
$\alpha_b(O)=1$、$\alpha_b((0,0))=b$、其余点 $\alpha_b(x,y)=x$
于 $\mathbb Q^\times/\mathbb Q^{\times2}$。其核是对偶同源的像。
由两个二同源和 $[2]$ 的正合列，
$$
2^{\operatorname{rank}E_b(\mathbb Q)}
   =|\alpha_b(E_b(\mathbb Q))|
    |\alpha_{-4b}(E_{-4b}(\mathbb Q))|/4.
\tag{2}
$$
把对偶曲线 $y^2=x^3+544x$ 经 $(x,y)=(4X,8Y)$ 化为 $E^+$
不改变平方类。

在 $E_{136}$ 上，$P$ 和 $(0,0)$ 给出独立的 $-2,-34$，
故 $\{1,-2,17,-34\}$ 全部出现。候选平方类只支撑于 $-1,2,17$。
剩下的四个类构成上述子群的另一个陪集，所以只需排除类 $2$。
该类出现当且仅当相应覆盖有非平凡有理点；清分母并取互素整数后必有
$$
N^2=2U^4-68V^4,\qquad \gcd(U,V)=1.
\tag{3}
$$
当 $(U,V)$ 的奇偶为 $(1,0),(0,1),(1,1)$ 时，右端模 $16$
分别为 $2,12,14$，全部不是平方。因此
$$
\alpha_{-136}(E_{136}(\mathbb Q))=\{1,-2,17,-34\}.
$$
在 $E^+$ 上 $x(x^2+34)\ge0$ 强制 $x\ge0$。
候选类因而只有 $1,2,17,34$；$Q$ 与 $(0,0)$ 已生成全部四类。
(2) 给
$$
\boxed{\operatorname{rank}E_{136}(\mathbb Q)
       =\operatorname{rank}E^+(\mathbb Q)=2.}
\tag{4}
$$
数表身份仅作定位：它们分别为 LMFDB $73984.d1,d2$，
Cremona $73984m2,m1$。证明 (4) 没有使用数表秩。

## 2. 实际局部特征；新 splitting 的相位

仍以 $E_0:y^2=x^3-x$、$[i](x,y)=(-x,iy)$ 为参考。
在 $2$ 处 $17$ 是四次幂，故新局部改变正是 $E_8/E_0$ 的四次扭曲。
记该有限 Hecke 特征为 $\chi_8$。这里不是 R112 的二次 Dirichlet 特征。

若 $a^4=8$，同构 $(x,y)\mapsto(a^2x,a^3y)$ 在
$a\mapsto\epsilon a$ 下改变为 $[\epsilon^{-1}]$ 倍，
所以在奇素理想 $\mathfrak l$ 上
$$
\chi_8(\mathfrak l)=(8/\mathfrak l)_4^{-1}.
\tag{5}
$$
这是 Tate 表示的实际扭曲方向，不能将四次符号取反。
令 $\lambda_2=1+i$、$\pi_5=1+2i$。
$\chi_8$ 只在 $2$ 分歧且无穷型为零。主 idèle 关系给
$$
\chi_{8,2}(\lambda_2)=\chi_{8,2}(i)=1.
$$
模 $\pi_5$ 有 $i=2$、$8=3=-i$，所以
$\chi_8((\pi_5))=i$，再由主 idèle 关系得
$$
\chi_{8,2}(1+2i)=-i.
\tag{6}
$$
共轭素位给相反的值，故 $\chi_{8,2}(5)=1$；同时
$2=-i\lambda_2^2$ 给 $\chi_{8,2}(2)=1$。
因为 $-1,2,5$ 拓扑生成 $\mathbb Q_2^\times$，该特征在整个
$\mathbb Q_2^\times$ 上平凡。

沿用 R112 的
$$
g_*=\frac{-3+4i}{5}=\frac{1+2i}{1-2i}.
$$
Yang 的原 splitting 改变为
$$
\omega_{136,2}(g)=\eta(g)\omega_{0,2}(g),\qquad
\eta(g)=\chi_{8,2}(i(g-1)).
$$
由于 $i(i-1)=-(1+i)$、$i(g_*-1)=-4(1+2i)/5$，准确得到
$$
\boxed{\eta(i)=1,\qquad\eta(g_*)=-i.}
\tag{7}
$$
$i,g_*$ 拓扑生成整个 $K_2^1$，见 R49/R112 的原生成性证明。

也可直接认定导子。在 $1+8\mathcal O_{K,2}$ 中，
用 $\sqrt{N(u)}\in1+8\mathbb Z_2$ 除去有理部分后，
所得 norm-one 元素属于 $g_*^{2\mathbb Z_2}$，故 $\chi_{8,2}$ 平凡。
另一方面 $(1+2i)^2=-3+4i\in1+\lambda_2^5\mathcal O_{K,2}$，
而其 $\chi_{8,2}$ 值为 $-1$。原 $E_0$ 特征在这个元素上为一，
故新 Hecke 特征的二处导子恰为 $\lambda_2^6$。
十七处仍在两个分裂素位各一阶分歧；可取原始导子
$$
f_{136}=136,\qquad Nf_{136}=18496,
\quad N(E_{136})=4Nf_{136}=73984.
\tag{8}
$$

## 3. 十六格空间及准确 Rao 矩阵

取
$$
\mathcal V_{16}=\{f:\operatorname{supp}f\subset\tfrac14\mathbb Z_2,
                       \ f(x+4)=f(x)\},\qquad
e_a=\mathbf1_{a/4+4\mathbb Z_2},\quad a\bmod16.
$$
Haar 测度为 $\operatorname{vol}(\mathbb Z_2)=1$，故每格测度 $1/4$。
令 $\zeta=\zeta_{16}=e^{2\pi i/16}$。原 $i$ 的矩阵是
$$
I_{ab}=\tfrac14\zeta^{-ab}.
\tag{9}
$$
原 $g_*$ 的 Rao 核及 splitting 常数仍准确为
$$
2\int\psi_2\!\left(\frac{3u^2-10uv+3v^2}{8}\right)f(v)\,dv,
\qquad \mu_0(g_*)=-\zeta_8^{-1}.
$$
代入 $u=a/4,v=b/4+4s$，相位的非常数部分为
$(3b-5a)s/4+6s^2$。对 $s\in\mathbb Z_2$ 的积分非零恰当
$b\equiv3a\pmod4$。写 $b=3a+4k$，便得到
$$
\boxed{
G_{ab}=\begin{cases}
-\dfrac12\zeta_8^{-1-2ak-3k^2},&b=3a+4k,\\
0,&b\not\equiv3a\pmod4.
\end{cases}}
\tag{10}
$$
同一平移积分在 $u\notin\tfrac14\mathbb Z_2$ 时为零；
在非零位置把 $u$ 加 $4$ 不改变值。因此 (9)–(10)
确实是稳定子空间上的完整矩阵，不是只在十六个采样点的值。

置
$$
t=\tan(\pi/16)=-i\frac{\zeta-1}{\zeta+1}
=-1+\zeta-\zeta^2+\zeta^3-\zeta^5+\zeta^6-\zeta^7.
\tag{11}
$$
它满足 $t^4+4t^3-6t^2-4t+1=0$。以下列向量为原未归一取值：
$$
\boxed{
v=(0,1,0,t,0,-t,0,-1,0,-1,0,-t,0,t,0,1).
}
\tag{12}
$$
在 $\mathbb Z[\zeta]$ 内逐项相乘给
$$
Iv=v,\qquad Gv=iv.
\tag{13}
$$
由 (7)，新表示下两生成元均固定 $v$。
共同特征空间一维：文末精确脚本给
$[4I-4;4G-4i]$ 在 $\zeta\mapsto8\in\mathbb F_{97}$ 下秩十五；
$8$ 的阶准确为十六。这个固定非零 minor 证明特征零秩至少十五，
而 (12) 给非零核，所以恰为十五。
这是一个固定代数恒等式证书，不是对变化目标素数的数值样本。

向量为实值，并且
$\|v\|^2=\tfrac14(4+4t^2)=1+t^2$。
归一的实际不变向量为 $\phi_{136,2}=\cos(\pi/16)\,v$。
从这里以下保留未归一向量 $v$；省去的正代数常数始终固定且非零。

## 4. 原十七处向量与三条共同的实际有限行

固定原规范 $\lambda(3)=-i$、$i\equiv4\pmod {17}$、
模 $289$ 的 lift 为 $38$。
在十七处，$E_{136}/E_{17}$ 的四次扭曲只造成未分歧特征，
因为 $8$ 是 $17$ 进单位。其紧单位限制及紧平均向量因而不变：
$$
\frac{\sqrt{17}}{16}\lambda^{-1}(y)
                       \mathbf1_{\mathbb Z_{17}^{\times}}(y).
$$
R48 的实际 Fourier 核仍给 $x=s/17$ 上的
$\lambda(s)\zeta_{289}^{19s^2}$，乘一个共同非零代数常数。
未分歧特征在 $17$ 本身的值不改变这个单位区间的向量。

全局支撑为 $x=n/68$。二处 $17^{-1}\equiv1\pmod {16}$；
十七处 $s=n/4$，且 $\lambda(4)=1$、$19/16\equiv236\pmod {289}$。
所以新的原 raw 权准确为
$$
\boxed{
a_n^{136}=\begin{cases}
v_{n\bmod16}\lambda(n)\zeta_{289}^{236n^2},&17\nmid n,\\
0,&17\mid n,
\end{cases}
\qquad F_{136}(\tau)=\sum_n a_n^{136}q^{n^2/9248}.}
\tag{14}
$$
这些向量在全部中央权 $4\mid m$ 不变：$2m+1\equiv1\pmod8$
同时保持原有限 CM 型和新的四次扭曲。二处已经构造 Hermitian
参数 $1$ 的真实不变线，十七处是原紧平均向量；故 Yang 的实际
全局平方公式应用于 (14)，没有换成另一个同维表示。

在 $\mathcal D=\mathbb Z/4624$、$Q(r)=r^2/9248$ 上，取
$$
\boldsymbol\Theta=\sum_{r\bmod4624}\sum_{n\equiv r(4624)}
                          q^{n^2/9248}\mathbf e_r.
$$
三个实际行都使用同一二次相位 $\zeta_{289}^{236r^2}$，分别为
$$
\begin{array}{c|c|c}
\text{行}&\text{二处权}&\text{十七处单位权}\\\hline
\ell_{17}&v_0(r)=\mathbf1_{4\mid r}&\lambda(r)\\
\ell_{34}&v_+(r)=\mathbf1_{2\mid r}\varepsilon_{r/2}
                         &(\lambda(r))^2\\
\ell_{136}&v(r)&\lambda(r)
\end{array}
\tag{15}
$$
其中 $(\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3)=(1,1,-1,1)$，
各行在 $17\mid r$ 时为零。于是
$\ell_j\boldsymbol\Theta=F_j$ 对三个实际 raw 形式全部成立。
在 $r=4,2,1$ 的三列上所得矩阵为三角形，三个对角元都是单位根。
所以这些原有限行在所有奇素位均整线性无关。
这不是关于它们的中央导数秩的声明。

## 5. 不是抽象识别：四项原 Heisenberg 运输

在十六格上定义
$$
(Xw)_a=w_{a-1},\qquad (Zw)_a=\zeta^a w_a,
\qquad ZX=\zeta XZ.
$$
原第一条曲线的 dyadic 向量是
$v_0=(1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0)$。
准确的四项恒等式是
$$
\boxed{
v=\mathcal Rv_0,\qquad
\mathcal R=\frac{ZX+\zeta Z^{-1}X+\zeta ZX^{-1}+Z^{-1}X^{-1}}
                   {1+\zeta}.}
\tag{16}
$$
例如在 $a=1+4k$ 上，右端等于
$((1+it)i^k+(1-it)(-i)^k)/2$，
给 $(1,-t,-1,t)$；在 $a=3+4k$ 上给 $(t,-1,-t,1)$。
其余位置为零。文末脚本在 $\mathbb Z[\zeta]$ 内直接验证
乘去 $1+\zeta$ 后的恒等式。

在全局 $n$ 指标中，$X$ 是 $n\mapsto n-289$ 的权平移，
因为 $289\equiv1\pmod {16}$ 且不改变十七处的完整模 $289$ 权；
$Z$ 是乘 $\zeta^n$。故 (16) 确实保留原十七处坐标。

### 5.1 在同一原 sigma 截面上的明确算子

以下全在 $E_0$ 微分 $dx/(2y)$ 的变量 $z$ 上工作。
令 $\Omega_0$ 为其正实周期、$\alpha=4-i$、$L=68$，并置
$$
h=\frac{\sqrt{\pi/2}\,L}{\Omega_0\alpha},\qquad
\mathscr S_w(z)=e^{-h^2z^2}\sum_n
w_{n\bmod16}\lambda(n)\zeta_{289}^{236n^2}
e^{-\pi(n/L)^2+2\pi nz/(\Omega_0\alpha)}.
\tag{17}
$$
仍令 $\lambda(n)=0$ 当 $17\mid n$。
把 $n=4m$ 代入，$\mathscr S_{v_0}$ 正是原 E17 Hermite 函数
在四倍变量的值。因此除一个固定共同非零常数外，
$$
\mathscr S_{v_0}(z)=A_{17}(4z),\quad
A_{17}(z)=\tfrac15\vartheta(z)\sigma(z)^{16}
                (x(z)^2+1)(5x(z)^4-2x(z)^2+1).
\tag{18}
$$
这里 $A_{17}$ 是 R51/R54 的原 $E_0$ 尺度，首项为 $z^4$。
以下对全部 $\mathscr S_w$ 同除这个共同常数，使 (18) 成为准确等式。

置
$$
P=\frac{(4-i)\Omega_0}{16},\qquad Q=-iP,\qquad N=272,
$$
并定义完整 theta 平移
$$
\mathcal T_R f(z)=
\exp\!\left(\frac{N\pi\bar R}{\Omega_0^2}z
        -\frac{N\pi|R|^2}{2\Omega_0^2}\right)f(z-R).
\tag{19}
$$
在 (17) 中把 $n$ 改为 $n+289$，或乘 $\zeta^n$，直接配方得到
$$
\boxed{X\longleftrightarrow\mathcal T_P,\qquad
       Z\longleftrightarrow\mathcal T_Q.}
\tag{20}
$$
例如第一式的完整补偿是
$\exp(\pi289z/(\Omega_0\alpha)-\pi289/32)$，
准确等于 (19)，没有丢掉线性或常数 Gaussian 因子。
并且
$$
\mathcal T_Q\mathcal T_P=\zeta\mathcal T_P\mathcal T_Q,
\qquad \mathcal T_P^{16}=\mathcal T_Q^{16}=1.
\tag{21}
$$
第一式中的指数是 $2\pi i\cdot289/16$；$289\equiv1\pmod {16}$
核对了原有限 commutator 的方向。

因此新实际截面在原坐标中完整给为
$$
\boxed{
C_{136}=\frac{\mathcal T_Q\mathcal T_P
 +\zeta\mathcal T_Q^{-1}\mathcal T_P
 +\zeta\mathcal T_Q\mathcal T_P^{-1}
 +\mathcal T_Q^{-1}\mathcal T_P^{-1}}{1+\zeta}
                      A_{17}(4z).}
\tag{22}
$$
它和原 $A_{17}(4z)$、$A_{34}(2z)$ 都是同一 degree-272 线丛
$\mathcal O(272O)$ 的截面。$P,Q$ 为真实十六挠点，且 $16\mid272$，
所以这些平移是该线丛的真实 theta 群作用。

### 5.2 固定代数性、整性及中心零

(19) 在解析式中写有 $\pi,\Omega_0$，并不意味着运输矩阵含任意
超越标量。先在代数线丛上选任一覆盖 $P$ 的代数同构 $U_P$。
其十六次幂为某个代数数 $a$ 倍恒等；若
$\mathcal T_P=cU_P$，(21) 强制 $c^{16}a=1$，故 $c$ 代数。
$Q$ 同理。这证明 (22) 是一个固定数域中的准确代数运输。

在任何奇剩余特征的好模型上，十六挠点 étale，平移和线丛同构
可在严格 Hensel 基变换后整地选取；其十六次幂常数是单位。
归一到 (21) 只需取这个单位的十六次根，仍为单位。
又 $N_{\mathbb Q(\zeta)/\mathbb Q}(1+\zeta)=2$。
故运输算子在每个奇素位保持实际截面整格。
把原固定有理 frame 和固定平方常数也纳入后，仅需排除一个固定有限集合，
不会出现随目标 $p$ 增长的运输分母。

四个平移项的中心值本身均为零。确实对应的原点参数为
$R=4(\pm P\pm Q)$，而 $[2]R=T_0=(1+i)\Omega_0/2$；
这些四挠点的 $x^2=-1$，所以 (18) 的因子 $x^2+1$ 为零。
由原全局 $i$ 对称，(13) 及十七处 $\lambda(i)=\lambda(4)=1$ 给
$$
C_{136}(iz)=C_{136}(z),\qquad C_{136}(z)\in z^4\overline{\mathbb Q}[[z^4]].
\tag{23}
$$
它不是零截面：在 (17) 的 Laurent/Fourier 展开中 $n=1$ 的系数非零。
因此还可唯一写成
$$
\boxed{C_{136}=\sigma^{272}P_{136}(x^2),\qquad
               P_{136}\in\overline{\mathbb Q}[X],\quad\deg P_{136}\le67.}
\tag{24}
$$
(22) 是对 (24) 全部系数的固定、无歧义代数构造；
不需要以有限 Gaussian 样本拟合该多项式。

## 6. 保留全部补偿的实际中央接口

### 6.1 同一 gauge 上的完整线性恒等式

对 $p\equiv3\pmod4$、$p>19$，令 $d=p+1$，
$c_0$ 为 R54 原 sigma 对数的临界系数，$v_p(c_0)=-1$，并取
$c=272c_0$。对本节的实际截面统一使用
$$
\mathcal J_c(F;u)=\sum_{h\ge0}
c^{-h}(u)_h[z^{dh}](e^{-cz^d}F),\qquad
(u)_h=u(u-1)\cdots(u-h+1).
\tag{25}
$$
令 $F_{\epsilon,\delta}=\mathcal T_Q^\epsilon
\mathcal T_P^\delta A_{17}(4z)$。则 (22) 给整条解析函数的准确式
$$
\boxed{
J_{136}(u)=\frac{\mathcal J_c(F_{+,+};u)
 +\zeta\mathcal J_c(F_{-,+};u)
 +\zeta\mathcal J_c(F_{+,-};u)
 +\mathcal J_c(F_{-,-};u)}{1+\zeta}.}
\tag{26}
$$
同一式可完整求 $u$ 导数，尤其适用于 $u=0$。
每个 $F_{\epsilon,\delta}$ 包含 (19) 的全部补偿。
这里没有把平移、乘法或协变微分移过 Mellin 变换，也没有删除任何
$W$ 项或 $u-1,u-2$ 的移权值。

原第一行在这个共同 gauge 中也准确定位。
若 $J_{17}$ 采用 R54 的 $17c_0$，整数插值后再用解析唯一性给
$$
\mathcal J_c(A_{17}(4z);u)
          =(4^{p-1})^uJ_{17}(u).
\tag{27}
$$
因 $4^{p-1}\in1+p\mathbb Z_p$，右侧是准确解析单位扭转。
其中心值为零，故中央导数与原 $J_{17}'(0)$ 完全相同。

### 6.2 新行仍是实际初级有限性的充分输入

存在固定有限素数集合 $S$，使对 $p\notin S$、$p\equiv3\pmod4$，
$$
\boxed{J_{136}'(0)\ne0\quad\Longrightarrow\quad
       \Sha(E_{136}/\mathbb Q)[p^\infty]\text{ 有限}.}
\tag{28}
$$
下面逐项核对 R50/R54 的原比较为何仍适用。

首先，$136$ 在 $\mathbb Q_{p^2}$ 中有单位四次根，给 $E_0$ 与
$E_{136}$ 的光滑整模型、形式群和完整 Tate 格的实际同构。
它保持同一局部 signed Rubin 两个直和因子。$E_0$ 的原 rank-zero
椭圆单位仍是其中的原始基，所以新椭圆单位有唯一的整系数
$\mathcal A_{136,p}(T)$。秩 (4) 与已发表的 CM parity 定理给正根数；
BKO 的同一个正号控制给
$$
2\le s_{136,p}\le\operatorname{ord}_0\mathcal A_{136,p}.
\tag{29}
$$
这里 $s_{136,p}$ 是原 $\mathbb Q$ 上的 $p^\infty$-Selmer 余秩。
与 R50 一样，$-1$ 二次扭曲与原曲线同构，所以从 $K$ 的控制下降
没有多添一个未知秩。

其次，比较始终用 $f_{136}=136$ 和 $f_0=2(1+i)$ 的原始导子。
它们之比只含 $2,17$，在目标 $p$ 处是单位；四次扭曲在 $d\mid m$
的反圆分分支上平凡。R50 的完整二变量 specialization、两个相同
$m!$、两个相同 Euler 因子 $1+1/p$ 和整微分比较遂逐项保留，给
$$
v_p\mathcal A_{136,p}(x_m)
  =v_pd_m^{(136)}-v_pd_m^{(0)},\qquad d\mid m.
\tag{30}
$$
没有把参考导子人为增大，也没有使用未证的高权单位周期。

第三，(14) 是实际 Yang 向量。R48 的 Fourier 实结构证明只用
非平凡 tame 单位型及实的 dyadic 不变向量，故对 (12) 同样成立；
十七处未分歧改变量只改变一个固定非零代数相位。
在 (17) 的 $\alpha$ 尺度上，这意味着 $C_{136}$ 的系数共轭
是固定非零代数数倍自身。实际中央平方公式因而给
$$
v_pd_m^{(136)}=2v_p[z^m]C_{136},\qquad 4\mid m,
\tag{31}
$$
在除去全部固定归一常数的有限素因子后成立。
这一步没有先声称单个平方根系数有理。

最后，(24) 的有限代数系数在除去固定分母后整；R54 的原半径
$R=p^{-1/(2p)}$ 上，$e^{-272c_0z^d}C_{136}$ 的 Gauss 范数至多 $R^4$。
因此 (25) 收敛，并有
$$
J_{136}\in pu\mathcal O_p\langle u\rangle,\qquad
J_{136}(k)=k!(272c_0)^{-k}[z^{dk}]C_{136}.
\tag{32}
$$
参考值仍为 $v_pd_{dk}^{(0)}=-2k-2v_p(k!)$。
把 (31)–(32) 代入 (30)，准确得到
$$
v_p\mathcal A_{136,p}(x_{dk})=2v_pJ_{136}(k).
\tag{33}
$$
BKO torsion 定理保证左侧函数非恒零。沿 $k=p^a$ 比较零阶如 R54，
$$
\operatorname{ord}_0\mathcal A_{136,p}
                         =2\operatorname{ord}_0J_{136}.
$$
所以 $J_{136}'(0)\ne0$ 将 (29) 的两端同时压到二，证明 (28)。

同一 Gauss 界也给出保留原行的首层
$$
J_{136}(u)\equiv\frac{[z^{p+1}]C_{136}}{272c_0}\,u\pmod {p^2},
$$
及 R54 的完整高精度尾界。
这提供一个新的合法固定候选行，没有以首层消失代替完整导数消失。

## 7. 回到同一个 charge；明确二次来源及三条原中央行

这里的 $w$ 是加法参数，**不是** R203 中另用字母 $w$ 表示的四次参数。
置
$$
D_{136}(w)=C_{136}(w/4),\qquad \Theta_1(w)=\vartheta(w)^{17},
\qquad h(w)=D_{136}(w)/\Theta_1(w).
\tag{34}
$$
这个变量改变是四倍同源的实际局部坐标改变。
它使新来源仍是 $\Theta_1$ 乘一个固定代数函数；不能将新来源
当成原变量中一个未经补偿的 charge-16 多项式。

### 7.1 完整参数和单位扭转

令 $\mathcal J_{17c_0}$ 用 (25) 的同一 $d=p+1$、同一下降阶乘，
只是将变量改为 $w$、gauge 改为 $17c_0$。
在每个非负整数 $k$，准确系数插值给
$$
\begin{aligned}
\mathcal J_{272c_0}(C_{136};k)
 &=k!(272c_0)^{-k}4^{dk}[w^{dk}]D_{136}\\
 &=(4^{p-1})^k\mathcal J_{17c_0}(D_{136};k).
\end{aligned}
$$
两边都解析：将新 gauge 拉回 $w$ 后，差为
$17c_0(16/4^d-1)w^d$，其系数整，且在 R54 的同一余项盘上
严格落入指数的收敛域。因此解析唯一性给
$$
\boxed{
\mathcal J_{272c_0}(C_{136};u)
    =(4^{p-1})^u\mathcal J_{17c_0}(D_{136};u).}
\tag{35}
$$
这里 $4^{p-1}\in1+p\mathbb Z_p$，故右边是完整的解析单位扭转，
并非把一个不收敛的混合 charge Newton 和形式重排。
中心值为零，所以 (35) 两侧的中央导数相等。

对第二条原曲线同样逐整数插值，准确有
$$
\mathcal J_{17c_0}(A_{34}(w/2);u)
       =(2^{-(p-1)})^u\mathcal J_{68c_0}(A_{34};u).
\tag{36}
$$
其中心值也为零，中央导数仍相等。
因此三个真正的完整中央条件可同时写成
$$
\boxed{
\left.\partial_u\mathcal J_{17c_0}
 \bigl(A_{17}(w),\ A_{34}(w/2),\ D_{136}(w);u\bigr)
\right|_{u=0}=0.}
\tag{37}
$$
(35)–(37) 保留原分支 $d=p+1$、原 Euler 比较和完整补偿；
没有对高次多项式源使用混合 charge 笔记中未经支付的 $m\not\equiv1\pmod p$ 核。

### 7.2 新来源所在的最小二次扩张

令 $\Gamma=\Omega_0\mathbb Z[i]$。
由同一 theta 乘子，$h$ 是 $4\Gamma$ 上的椭圆函数。
原向量 (12) 还准确满足
$$
X^8v=-v,\qquad Z^8v=-v,
$$
而原 $v_0$ 和 R112 嵌入的 $v_+$ 在这两算子下均取正号。
在 (19) 的完整规范中，$\mathcal T_Q^8=\mathcal T_{\Omega_0/2}$，
$\mathcal T_P^8=\mathcal T_{-i\Omega_0/2}$：相差的格向量所产生的
常数相位是 $e^{272\pi i}$ 的整数次幂，等于一。
把 theta 乘子同时除去后，得到
$$
\boxed{h(w+2\Omega_0)=-h(w),\qquad
       h(w+2i\Omega_0)=-h(w).}
\tag{38}
$$
所以 $h$ 的周期与旧 $2\Gamma$ 相交的格准确为
$$
\Lambda=\{2\Omega_0(m+ni):m+n\equiv0\pmod2\}
        =2(1+i)\Gamma.
\tag{39}
$$
这在旧 $2\Gamma$ 中指数二；只写“某个固定有限覆盖”会丢掉此准确方向。

写
$$
X=x_0(w/2),\qquad Y=y_0(w/2),\qquad
\mathscr K_2=\overline{\mathbb Q}(X,Y),\quad Y^2=X^3-X.
$$
取 $u=w/(2(1+i))$、$x=x_0(u)$。
原 $[1+i]$ 加法式准确给
$$
X=-\frac i2(x-x^{-1}),\qquad
R=\frac12(x+x^{-1}),\qquad R^2=1-X^2.
$$
核的非平凡平移把 $x$ 变成 $-1/x$，因而把 $R$ 变成 $-R$。
由 (38)–(39)，
$$
\boxed{h\in\mathscr K_2(R)\setminus\mathscr K_2,
\qquad R^2=1-X^2.}
\tag{40}
$$
特别 $h^2\in\mathscr K_2$。
因为 $h\ne0$ 且取负号，这个扩张和来源方向都确实非平凡。

旧 $A_{17}(w)/\Theta_1$、$A_{34}(w/2)/\Theta_1$ 以及 R235 的七个
伴随商都属于 $\mathscr K_2$。它们加上原 $W$ 补偿后的固定有理
微分闭包仍包含在
$\mathscr K_2(w,V)$ 中，其中 $V=(\log\Theta_1)'$。
这里 $w,V$ 在 $\mathscr K_2$ 上代数独立：沿两个旧周期继续时，
它们的增量分别为
$$
(2\Omega_0,34\pi/\Omega_0),\qquad
(2i\Omega_0,-34\pi i/\Omega_0).
$$
两向量的行列式为 $-136\pi i\ne0$。
若存在代数关系，在任一非极点固定系数后，沿所有整数周期平移
会得到一个在 $\mathbb Z^2$ 上恒零的二元多项式；可逆的上述线性变换
迫它的所有系数为零。这证明代数独立。
纯超越扩张中原系数域相对代数闭，故由 (40)
$$
h\notin\mathscr K_2(w,V).
\tag{41}
$$
因此新来源不在旧七维来源及其原 $W$、微分有理闭包内。
这项来源结论不将任何 Mellin 核或中央零空间冒充为该微分闭包。

### 7.3 一个有限的原多项式接口

由 $h(iw)=h(w)$、$X(iw)=-X(w)$、$R(iw)=-R(w)$，
$h/(XR)$ 属于 $\mathscr K_2$ 的 $i$-不变子域，即
$\overline{\mathbb Q}(X^2)$。
其可能极点只在 $X^2=-1$；那里 $\vartheta(w)$ 有简单零，
所以极点阶至多十七。
在 $X^2=0,1$，$XR$ 的零阶分别为二、一，低于该参数的分歧阶四、二，
故商不能藏有额外极点。
在无穷处 $XR$ 有四阶极点，而 $h$ 至少四阶零。
因此存在唯一固定多项式 $P_{15}$，满足
$$
\boxed{
h(w)=\frac{XR\,P_{15}(X^2)}{(X^2+1)^{17}},\qquad
P_{15}\in\overline{\mathbb Q}[U],\quad\deg P_{15}\le15.}
\tag{42}
$$
它由 (22) 唯一且代数地构造。
原点处分支为 $R\sim iX$；由于 $R=-iY/\sqrt X$，也可准确写为
$$
\boxed{
D_{136}(w)=-i\,y_0(w/2)\vartheta(w/2)\sigma_0(w/2)^{67}
                      P_{15}(x_0(w/2)^2).}
\tag{43}
$$
这把需要后续计算的新源压到十六个固定代数系数，
没有增加随 $p$ 改变的源维数。

更具体地，置 $U=X^2$、$Z=XR$，则
$Z^2=U(1-U)$。
(37) 的三个源统一是 $\Theta_1$ 乘
$$
\begin{aligned}
f_1(U)&=Q\!\left(\frac{16U(U-1)^2}{(U+1)^4}\right),
  &Q(s)&=s+\tfrac35s^2-\tfrac15s^3+\tfrac15s^4,\\
f_2(U)&=\frac{P_{34}(U)}{(U+1)^{17}},\\
f_3(U,Z)&=\frac{ZP_{15}(U)}{(U+1)^{17}}.
\end{aligned}
\tag{44}
$$
其中 $P_{34}$ 是 R115 的原次数十六多项式。
这是同一个 charge、一条固定代数二次覆盖及三条完整原中央行。
新源使原线性来源空间增加一个非平凡二次方向，整个函数域的
超越维数仍为二。

## 8. 当前新增的约束与仍需证明的覆盖

现在三个固定 rank-two 来源都在 (15) 的同一原 Weil 向量和
(22) 的真实 theta 群图中。若能证明它们的完整导数不同时为零的
惰性素数集合无穷，固定三元池的抽屉原理即给本课题所需的某一条曲线。

新行给出 (26)、(37) 的额外真实线性约束；它在中央泛函层面是否
独立于旧两行条件尚未证明，也不能把它自动传播到四个平移项分别为零。
尤其 (15) 的有限行独立、(16) 的源运输以及
rank-zero 分量的非零中心值，都不单独证明这个中央导数覆盖。
后续可在 (26) 中计算准确的连接补偿和函数方程单位扭转；
任何 $\log(\text{单位})J(0)$ 项必须随原规范保留。

## 9. 可重复证书与来源

- [精确脚本](../scripts/check-e136-dyadic-rank2-and-original-transport.js)
  只用 Node 整数算术，核对二下降模 $16$ 阻碍、所有原矩阵特征式、
  共同特征线的固定非零 minor、四项实际运输、CRT 相位和三行 minor。
  [输出](../scripts/check-e136-dyadic-rank2-and-original-transport.json) 为 PASS。
- R48/R49/R51：原 Fourier 实结构、degree-17 下降和准确 $A_{17}$。
  R112/R115：第二条原 rank-two dyadic 线及其规范。
- R50/R54：实际 signed 整格比较、全权值与完整半因子的零阶比较。
  这些论证在 §6.2 中已逐项核对新导子和新局部型，而非凭名称套用。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. 485 (1997), 25–53，
  Corollaries 2.4、2.10 及 (2.28)；原 Rao/Kudla 规范沿用 R48/R112。
- A. Burungale, S. Kobayashi, K. Ota, *Rubin's conjecture on local units in
  the anticyclotomic tower at inert primes*, Annals 194 (2021), 943–966，
  [原文](https://par.nsf.gov/servlets/purl/10336626)，Theorems 2.1、6.1、6.2。
- 同三位作者，*p-adic L-functions and rational points on CM elliptic curves
  at inert primes*, JIMJ 23 (2024), 1417–1460，
  [原文](https://doi.org/10.1017/S147474802300021X)，Corollary 4.11(i)。
- 曲线数据定位：[73984.d1](https://www.lmfdb.org/EllipticCurve/Q/73984/d/1)、
  [73984.d2](https://www.lmfdb.org/EllipticCurve/Q/73984/d/2)。

