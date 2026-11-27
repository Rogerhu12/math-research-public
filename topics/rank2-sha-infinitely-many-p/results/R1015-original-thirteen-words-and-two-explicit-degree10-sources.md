# R1015 — 原十三字的两条明确 degree10 来源与完整同点乘法关系

日期：2026-11-27 UTC。**已证明。** R1012 将全部十三字返回固定的
十维 degree10 空间；对于原两条 canonical 来源，这十维输入实际各只用
一条明确的向量。第一条是原 $\Psi_{125}$，第二条准确为
$\sigma^{10}(X+1)=\sigma(z)^2\sigma(2z)^2/4$。
下面给出所有十二个非零字的完整规范常数，原两支的相位，以及一个
不依赖 $p$ 的明确有理乘子。该乘子在同一 Miller/平移后的整个输入上
联系两条原来源，保留全部 $G_j$、$P_{10}$、$Z$ 和二挠权。

本篇不把字、平移或该有理乘子另赋 canonical 中央零。新的内容是
将原来可能任意的十维来源和其相对位置完全确定；它可直接代入
R1013 的全字长窗与 R1016 的同一个特征零平坦 trace。

## 1. 原相位、两条来源和实际质量

沿 R987、R993、R1012，固定

$$
E:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\pi=(7+\delta)/2,\quad \bar\pi=(7-\delta)/2.
\tag{1}
$$

两条完整来源记为 $\Phi_*,\Phi_{260}$。它们的全部有限标签分别为
$(0,0,0)$ 与 $(1,4,4)$，质量均零，$z^6$ 系数均一。
这些是 R970、R973 的原算术向量，不从好位本征值重新任选来源。
令

$$
\Psi=\Psi_{125}=\sigma^{10}x^2(X-8),\qquad
q=\sigma^{10}(X+1).
\tag{2}
$$

本篇要证明 $q$ 正是第二条来源在十三分解后的实际标准向量。

取原 degree130 canonical Heisenberg 提升。以下把对偶生成元
$v\in E[\bar\pi]$ 的符号规定为

$$
T_{u_\pi}T_v=\zeta T_vT_{u_\pi},
\qquad B=\pi v\in E[\bar\pi]\setminus\{O\}.
\tag{3}
$$

这是由 R1012 已定的 $\zeta$ 唯一确定的对偶生成元；若将通常
Schrödinger translation 写成相反的坐标移位，便同时使用 $-v$。
这只是 (3) 的明确约定，不更换原提升的相位。
本篇涉及的 $x(iB),X(iB)$ 和全部偶角色均不受这个记号符号影响。

沿 R1012 记

$$
\varepsilon(i)=(i/13),\qquad
g=\sum_{a\bmod13}\varepsilon(a)\zeta^a,\qquad
\nu_\pi=\frac{g\,m_\pi}{13},
\qquad
m_\pi=\frac{(3-\delta)\sqrt\pi}{332640},
$$

$$
\rho_\pi=-\frac{11(1+\delta)}{40}.
\tag{4}
$$

其中 $g$ 和 $\sqrt\pi$ 都是 R987 原规范的根。
原完整核计算给出的不是单个点的比例，而是整个二次核代数上的比例。
故对全部 $i\ne0$，原加性投影满足

$$
\boxed{
m_0(\mathcal P_{\pi,i}\Phi_*)=\varepsilon(i)\nu_\pi,
\qquad
m_0(\mathcal P_{\pi,i}\Phi_{260})
=\varepsilon(i)\rho_\pi\nu_\pi.
}
\tag{5}
$$

两来源的 $i=0$ 字整条为零。式 (5) 使用实际 Heisenberg lift，
没有在质量计算之后另乘一个未登记的 theta 常数。

## 2. 分解中的标准向量不随非零字变化

原完整 theta 空间的有限分解为

$$
\mathcal S_{130}\simeq(W_2\otimes W_5)\otimes W_{13}.
\tag{6}
$$

十三 torsion Heisenberg 群只作用于末因子。
$\mathcal P_{\pi,0}$ 的像准确为 $D_\pi\mathcal S_{10}$，其中
$D_\pi f(z)=f(\pi z)$，不另乘 Hecke 标量。
由 (3)，$T_{iv}D_\pi$ 将标准 $\mathcal S_{10}$ 同构到
$\mathcal P_{\pi,i}$ 的像。因而可以用

$$
F\otimes\delta_i\longmapsto T_{iv}D_\pi F
\tag{7}
$$

固定整个十三因子的 Schrödinger 分解。
式 (7) 对其余两个有限因子是同一个交织；没有逐字改变二、五处来源。

R970 的自然十三极化给完整有限环面作用

$$
W(t)\phi(a)=\varepsilon(t)\phi(ta).
\tag{8}
$$

所以有限标签 $b$ 的非 quadratic 向量准确为
$\chi_{b-6}(a)$，在 $a=0$ 取零；这里
$\chi_j(2)=\zeta_{12}^j$、$\zeta_{12}^4=\omega^2$。
这保留了 quadratic splitting，与 R973 的算术单位角色的指数相反。
对原两条来源，十三 profile 分别是

$$
\chi_6=\varepsilon,\qquad \chi_{10}.
\tag{9}
$$

由于每条原来源在 (6) 中是已指定的纯张量，存在同一个非零
$q_0\in\mathcal S_{10}$ 和固定非零常数 $c_*,c_{260}$，使

$$
\mathcal P_{\pi,i}\Phi_*
=c_*\chi_6(i)T_{iv}D_\pi\Psi,
\qquad
\mathcal P_{\pi,i}\Phi_{260}
=c_{260}\chi_{10}(i)T_{iv}D_\pi q_0.
\tag{10}
$$

第一条的标准向量是 $\Psi$，因为 R978/R987 已完整确定同一
二、五因子的 $\delta_0$ old 向量就是 $D_\pi\Psi$。
这里的 $c_*,c_{260}$ 只用于证明方向；第4节会消去它们，给出
所有字的明确规范，不以“存在某个比例常数”作为最终身份。

### 2.1 第二条标准向量的几何型

令 $R_\lambda F(z)=F(\lambda z)$。canonical lift 逐式给
$R_\lambda T_vR_\lambda^{-1}=T_{\lambda^{-1}v}$。
在 $E[\bar\pi]$ 上，$\omega$ 作用为 $3\bmod13$，故
$\omega^{-1}$ 作用为9。将 (10) 在 $i$ 上重编号，十三 profile
对 $R_\omega$ 的贡献是

$$
\chi_{10}(3)=\zeta_{12}^{40}=\omega^2.
$$

原 $\Phi_{260}$ 是整个几何主型，故 $R_\omega q_0=\omega q_0$。
此外 $\chi_{10}(-1)=1$，故 $q_0$ 是偶函数。
标准全 $\mathcal S_{10}$ 的该型恰为

$$
\boxed{q_0=\sigma^{10}(aX+b),\qquad (a,b)\ne(0,0).}
\tag{11}
$$

这一步在完整十维空间内作；没有预先把第二条来源投到原主型两列。

## 3. 实际质量唯一迫出 $a=b$

在 (10) 的质量比中，相同的 canonical 平移指数完全相消。
结合 (5)，对每个 $i\ne0$ 有

$$
\rho_\pi
=\frac{c_{260}}{c_*}\chi_4(i)
\frac{aX(iB)+b}{x(iB)^2(X(iB)-8)}.
\tag{12}
$$

所以记

$$
r_{a,b}(P)=\frac{aX(P)+b}{x(P)^2(X(P)-8)},
$$

全部实际十三核点都满足

$$
\frac{r_{a,b}(2P)}{r_{a,b}(P)}
=\chi_4(2)^{-1}=\omega,
\qquad P\in E[\bar\pi]\setminus\{O\}.
\tag{13}
$$

各分母非零；非零十三挠点不能同时为二挠或三挠。
以下在完整二次代数内核 (13)，不选择某个根拟合。

原共轭核多项式为

$$
R_{\bar\pi}(X)
=X^2+(2-6\delta)X+(40-24\delta)/13.
\tag{14}
$$

倍2交换两个 $\mu_6$ 轨道：$2\notin(\mathbf F_{13}^\times)^2$，
而这两个轨道恰是 (14) 的两个根。因此置

$$
X'=X(2P)=-(2-6\delta)-X.
\tag{15}
$$

原 duplication 恒等式给

$$
x(2P)=\frac{x(P)(X-8)}{4(X+1)}.
\tag{16}
$$

完整两个范数准确是

$$
N_{R_{\bar\pi}}(X+1)=\frac{27(1+2\delta)}{13},
\qquad
N_{R_{\bar\pi}}(X-8)=\frac{216(5-3\delta)}{13},
$$

$$
\boxed{16N_{R_{\bar\pi}}(X+1)
=\omega N_{R_{\bar\pi}}(X-8).}
\tag{17}
$$

由 (16)，(13) 左边为

$$
\frac{16(X+1)^2(aX'+b)}
     {(X-8)(X'-8)(aX+b)}.
\tag{18}
$$

将 (17) 代入，(13) 精确等价于

$$
(aX'+b)(X+1)=(aX+b)(X'+1),
\quad\hbox{即}\quad (b-a)(X-X')=0.
\tag{19}
$$

因为 (14) 可分且 $X\ne X'$，有 $a=b\ne0$。
吸收原统一常数后，(10) 中的标准向量因此准确为

$$
\boxed{q=\sigma^{10}(X+1).}
\tag{20}
$$

由 $\sigma(2z)^2=4\sigma(z)^8y(z)^2$，同一来源另有完整公式

$$
\boxed{q(z)=\frac14\sigma(z)^2\sigma(2z)^2.}
\tag{21}
$$

它从 $z^4$ 起，首项一；它不是原 principal 算术中央的另一个零输入。
式 (19) 唯一确定的是原固定二、五向量的方向，完整有限角色由
(6)–(10) 保持，并未反过来凭该四 sigma 形状任选角色。

## 4. R1012 的全部 Miller 字规范

R1012 的 $S$ 是 $\kappa$ 的实际 deck 角色在 $u_\pi$ 上等于
$\zeta$ 的唯一点。由 (3) 和原 theta 除子，准确有

$$
\boxed{S=-10B,\qquad R_i=4iS=-iB.}
\tag{22}
$$

证明如下。在 $T_vD_\pi F/\sigma(\pi z)^{10}$ 中，
平移的 theta 线丛相对于未平移线丛的 degree0 类是
$-10B$。其在 $[\pi]$ 上拉回为 principal，deck 角色由 (3)
恰为 $\zeta$。R1012 的字符—点同构的单射性遂给 $S=-10B$。
乘 $4i$ 后使用 $40\equiv1\bmod13$ 得第二式。
这也说明标准返回的平移 $R_i$ 与原 Heisenberg 平移完全配准，
不是另外挑一个满足 $10R_i=iS$ 的点。

保持 R1012 原规范

$$
\operatorname{div}h_i=(10-i)(O)+i(S)-10(R_i),
\qquad h_i(z)=z^{10-i}+\cdots\quad\hbox{at }O,
$$

$$
\kappa^if_i
=\frac{\pi^{10}\mathcal P_{\pi,i}\Phi}{\sigma(\pi z)^{10}},
\quad \kappa(z)=\pi^{-1}z^{-1}+\cdots,
\quad Q_i(P)=h_i(P+R_i)f_i(P+R_i).
\tag{23}
$$

设 $w=\pi z$ 是目标的原形式参数。若
$m_i=m_0(\mathcal P_{\pi,i}\Phi)$，则在原点

$$
f_i(w)=\pi^{10}m_i w^{i-10}+\cdots.
$$

故无论 $i<10$、$i=10$ 或 $i>10$，原 Laurent 规范都给

$$
\boxed{Q_i(iB)=\pi^{10}m_i.}
\tag{24}
$$

标准返回 (23) 与 (7) 都是同一个固定平移后的线丛同构，
二者之比是完整椭圆曲线上的无零无极函数，故为常数。
因此 (20) 所确定的方向在 R1012 的 $Q_i$ 规范中也保持。
用 (5)、(24) 确定该常数，得到全部十二个字的完整公式

$$
\boxed{
Q_{i,*}(P)=
\frac{\pi^{10}\varepsilon(i)\nu_\pi}
     {x(iB)^2(X(iB)-8)}\,x(P)^2(X(P)-8),
\qquad 1\le i\le12,
}
\tag{25}
$$

$$
\boxed{
Q_{i,260}(P)=
\frac{\pi^{10}\varepsilon(i)\rho_\pi\nu_\pi}
     {X(iB)+1}\,(X(P)+1),
\qquad 1\le i\le12.
}
\tag{26}
$$

这两式没有未定的 proportionality 标量。$\pi^{10}$ 来自
R1012 原有理化规范，而不是新的 Hecke 归一。
式 (25)、(26) 的第零字均为零。

对 $\bar\pi$ 支重复相同构造，使用与其原中心根相容的对偶生成元，
$\bar B=\bar\pi u_\pi$，并替换

$$
\pi\longmapsto\bar\pi,\quad
\rho_\pi\longmapsto\rho_{\bar\pi}
=-11(1-\delta)/40,\quad
\nu_\pi\longmapsto\nu_{\bar\pi},
$$

$$
\nu_{\bar\pi}=g m_{\bar\pi}/13,
\qquad m_{\bar\pi}=-(3+\delta)\sqrt{\bar\pi}/332640.
\tag{27}
$$

这里保留原 Weyl-dual 负号；不能把 (27) 换成任意选定的正平方根。
两条标准多项式 $x^2(X-8)$ 和 $X+1$ 在双支完全相同。

### 4.1 好位单位范围

$x(iB)$、$X(iB)+1$、$X(iB)-8$ 在 $2,3,13$ 外均为单位。
这可直接由 (14)、(17) 以及 $N(X)=8(5-3\delta)/13$ 核得；
也可用十三挠与二、三挠在好约化上的不交。
$\nu_\pi$ 的显示分母与 $\rho_\pi$ 只涉及
$2,3,5,7,11,13$。故在原固定数域的每个 $p>211$ 好位，
(25)、(26) 的全部显示规范常数都是单位。
全部 Miller 函数仍按 R1012 的原整模型使用；不新增数值求解的分母。

## 5. 一个固定有理乘子给完整同点关系

定义原曲线上的固定函数

$$
\boxed{r(P)=\frac{X(P)+1}{x(P)^2(X(P)-8)}
=\frac1{4x(P)x(2P)}.}
\tag{28}
$$

第二式是 (16)，不是仅在十三核上的同余。
由 (13)、(19)，对所有 $i\ne0$，

$$
\boxed{r(iB)=\chi_8(i)r(B),\qquad
r(B)^3=\frac{5+3\delta}{2048}.}
\tag{29}
$$

第一式因为2生成整个 $\mathbf F_{13}^\times$ 且倍2比为 $\omega$。
第二式用 $r(P)^3=(64X(P)X(2P))^{-1}$，再代入
$XX'=(40-24\delta)/13$。所以所有字的相对系数只取三个
明确的三次角色值；原 $r(B)$ 的根仍由实际点 $B$ 决定，不能另挑。
共轭支的相应立方值为 $(5-3\delta)/2048$。

由 (25)、(26) 得完整标准字关系

$$
\boxed{Q_{i,260}(P)=
\frac{\rho_\pi}{r(iB)}\,r(P)Q_{i,*}(P).}
\tag{30}
$$

回到上游原来源，而不是仅留在标准字方向上，又有

$$
\boxed{
\mathcal P_{\pi,i}\Phi_{260}(P)
=\rho_\pi\frac{r(\pi P+iB)}{r(iB)}
              \mathcal P_{\pi,i}\Phi_*(P),
\qquad i\ne0.
}
\tag{31}
$$

这是整个函数的身份。右边有理乘子的 apparent 极由相应完整
字来源的零抵消；不能只在避开这些点的开集解释它。
对全部 $i$ 求和，得到明确的原 source-to-source 算子

$$
\boxed{
\Phi_{260}(P)=\frac{\rho_\pi}{r(B)}
\sum_{i=1}^{12}\chi_4(i)
 r(\pi P+iB)\,\mathcal P_{\pi,i}\Phi_*(P).
}
\tag{32}
$$

式 (32) 的 domain 是这些指定完整字的直和；它不宣称有理乘子
在任意全 $\mathcal S_{130}$ 截面上无极。
逆向用同一字上的 $r(iB)/r(\pi P+iB)$，也保完整零极抵消。

## 6. 全权、全部 Cartier 层和单一 trace 中的准确消费

先取 R1010/R1013 的任意完整权字
$i\equiv-pj\pmod{13}$、$e_j=(i+pj)/13$。沿 R1012，记

$$
\mathcal W_{i,j,p}(P)=
(g_j(P+R_i))^p(h(P+R_i))^{e_j}
\frac{Z(P+R_i)^{-7}P_{10}(P+R_i)}{h_i(P+R_i)}.
\tag{33}
$$

则两条完整原字在同一个平移后的输入准确为

$$
\tau_{R_i}^*\eta_{j,*,p}
=\mathcal W_{i,j,p}Q_{i,*}\omega_E,
\qquad
\tau_{R_i}^*\eta_{j,260,p}
=\mathcal W_{i,j,p}Q_{i,260}\omega_E,
$$

$$
\boxed{
\tau_{R_i}^*\eta_{j,260,p}
=\frac{\rho_\pi}{r(iB)}\,r(P)
       \tau_{R_i}^*\eta_{j,*,p}.
}
\tag{34}
$$

因此后续对第一 Cartier、两个 exact 层或全部长前缀的联立，
可使用一个固定乘子 $r$ 与三个明确角色标量；不再需要给每个字
保留任意十维输入。式 (34) 保留整个 $\mathcal W_{i,j,p}$。
不能把 $r$ 移过 Cartier、把 $G_j$ 移过几何投影，或在乘法后
丢掉 $h_i$、原 $P_{10}/Z$ 与二挠极。

对 R1016 的单一特征零权 $V_{N,\pi}$，同样保留其全部 Fourier
字，先对完整乘积作几何投影，再使用 (31)。于是全部前缀及模
$p^{H+1}$ 的原中央比较仍落在 R1016 的同一个实际 target，
不是逐行更换来源。该 trace 对两个来源都线性，但它不与 (31)
中的非恒定有理乘子交换。

在同时坏的 canonical 假设下，式 (32) 提供两个准确的同源
测试：原 $\Phi_*$ 的中央测试和该显示算子的转置测试都为零。
此处的转置只能用 R985/R987 的完整有限 theta 配对，或直接用
(33)–(34) 的实际源读取；不能将它改成变量的普通加法平移。
后续须从这两个真实约束及原 old 对数取得不相容，不能预先给
$q$、每个字或每个加权 $\Psi$ 的中央导数赋零。

## 7. 证明来源与固定输入

本篇只消费以下已完整支付的输入，没有新运行数值数学：

- R970 §3、R973 §§1、4：原自然十三极化、quadratic splitting、
  两条实际纯张量及全部二、五、十三有限类型。
- R978、R987：原 $D_\pi\Psi_{125}$、两个 canonical 提升及绝对相位。
- R993、R1012：整个十三核质量比 $\rho_\pi$、全部字质量及原 Miller 规范。
- R1012：完整十三次 Kummer 分解、固定标准返回、完整乘积后三轨道式。
- R1013、R1016：保全权的长前缀与同一特征零平坦 trace。

核心唯一性步骤 (17)–(19) 在完整二次核代数中进行；
(24) 逐式确定全部规范常数；(31)–(34) 是完整函数及微分身份。
它们不以有限素数扫描、两个好位特征值或来源乘积传播中央零。
