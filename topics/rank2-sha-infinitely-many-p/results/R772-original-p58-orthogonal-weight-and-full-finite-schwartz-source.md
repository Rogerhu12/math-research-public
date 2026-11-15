# R772 — 原 P58 轴的完整正交权、三倍覆盖与有限 p 门来源

日期：2026-11-15。**状态：第1—7节的来源、整格、周期和有限化结论已证明。第8节所列的全点公式尚未付清。**

本篇处理 R764 的同一个实际条件首行
$$
\mathcal L_P(\mathcal D)
 =\int_{\mathcal D}\frac{\mathfrak t}{P}\,q_N^*\,de_0.
\tag{1}
$$
全部 CD、失败门、E 门及单位条件保持原样。这里分母是 P，不把它换成 Y，也不把未切割的纯 $D_\omega$ 来源代入。

新增的完整事实是：**原最终权 $q_N^*$ 不但与 Y 正交，也与 P 正交。** 清掉 P 的真实三处分母后，(1) 是标准 degree174 theta 空间的有限 p-primary 平移的负一单位矩；原伙伴正矩只改变代数系数。这个覆盖只增加三处，不产生十七处的 lattice/gluing。它并不使所有相关 Hecke 分量自动落入已经证明的点公式范围。

## 1. 同一物理来源和实际域

沿 R764 的原规范，置
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
\omega^2+\omega+1=0,\qquad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad N\in4\mathbf Z_{>0}.
\tag{2}
$$
$p$ 是原普通射线的合格素数；特别 $p\nmid2\cdot3\cdot17\cdot29$。
原六输入为
$$
\xi=(\xi_1,\xi_2,\xi_3,x,c,d)^t,\qquad
e_0=-\nu_\sigma^{\boxtimes6}/84 .
$$
记
$$
\begin{aligned}
\mathfrak r&=(\xi_1-\omega^2\xi_3+\omega x)/\delta,\\
\mathfrak s&=\mathfrak r+c,\qquad
\mathfrak t=\mathfrak r-c,\\
\mathfrak B&=-\xi_1+\omega\xi_3-\omega^2x,\\
\mathfrak A_0&=2\delta\xi_2-\frac{4\delta}{3}\mathfrak B,\\
Y&=\mathfrak A_0+\mathfrak s+2d,\qquad a=1+3\omega.
\end{aligned}
\tag{3}
$$
采用行 Gram 约定 $\langle L,M\rangle=L\bar M^t$。
R764 的完整整框架给
$$
(\mathfrak s,\mathfrak t,C,\mathfrak B,\xi_2,d)
\quad\text{两两正交，范数为}\quad (2,2,1,3,1,1).
\tag{4}
$$
最终 $q=q_N^*$ 是 R734 的实际测试，含全部原逆矩阵、两条核修正、有限门和各混次周期归一；它仅使用
$$
F=\mathfrak s-\mathfrak B+\omega^2\xi_2+(2+3\omega)d,\qquad
G=13\mathfrak B+26\xi_2+(3-2\omega)F
\tag{5}
$$
及 C。这里始终不是 cd 返回后的 $\Phi_N$。

令
$$
\widehat{\mathfrak s}=\mathfrak s-Y/17,\qquad
\widehat d=d-Y/17,\qquad
b_Y=(20+3\omega)/17.
$$
对 $m\ge n\ge N$，R764 的共同实际域为
$$
\mathcal D^\infty_{n,N}
 =\{Y\text{ unit},\
       \widehat{\mathfrak s},\widehat d\in p^N,\
       \widehat{\mathfrak s}/2-3\widehat d\notin p^n\}.
\tag{6}
$$
可以附已经准确运输的 $E_\perp$ 深、浅或环带门，以及 $\mathfrak t$-unit；下面以 $\mathcal D$ 表示整个有限域。

同一观察为
$$
\boxed{
P=b_YY+a\widehat{\mathfrak s}+2\widehat d
 =Y+a\mathfrak s+2d
 =\mathfrak A_0+(2+3\omega)\mathfrak s+4d .
}
\tag{7}
$$
第二个等号使用 $17b_Y-a-2=17$，因此物理 P 的系数没有十七分母。
在 (6) 上，$P-b_YY\in p^N$，故 P 是单位。

三个原 W 观察准确为
$$
W_j=P-a\omega^{2j}\mathfrak t,\qquad j=0,1,2;
\tag{8}
$$
它们在 R764 返回后成为 $P-a\omega^{2j}\kappa^m\mathfrak t$。
(1) 是这些完整观察差的首行，尚非一个完整原中央。

## 2. q 的 P 正交性是逐项等式

由 (3)—(5)，
$$
P=(2+3\omega)\mathfrak s-\frac{4\delta}{3}\mathfrak B
  +2\delta\xi_2+4d .
$$
因此
$$
\begin{aligned}
\langle P,F\rangle
 &=2(2+3\omega)+4\delta+2\delta\omega
       -4(1+3\omega)=0,\\
\langle P,C\rangle&=0,\\
\langle P,\mathfrak B\rangle&=-4\delta,\qquad
\langle P,\xi_2\rangle=2\delta,\\
\langle P,G\rangle&=13(-4\delta)+26(2\delta)=0,\\
\langle P,\mathfrak t\rangle&=0 .
\end{aligned}
\tag{9}
$$
第一行还使用 $4\delta+2\delta\omega=6\omega$。
这些是原行的 Hermitian 正交等式，不是从某条边际的质量推测。

对非零 z，记
$$
P_{P,z}=I+\frac{z-1}{N(P)}\bar P^tP .
$$
它逐点固定 $P^\perp$。由 q 的全部实际变量范围，得到
$$
\boxed{
q_N^*\circ P_{P,z}=q_N^*,\qquad
\mathfrak t\circ P_{P,z}=\mathfrak t .
}
\tag{10}
$$
q 内的所有指示函数和正多项式也逐项成立。没有新增 P 方向的多项式导数。

但 (6) 的各门一般不是 P 正交门；它们在 (10) 下仍需完整转置。
同样，本篇没有证明 $\Phi_N\circ P_{P,z}=\Phi_N$。原 q 与 cd 返回权的区别在这里是实质性的。

由 (4)、(7)，
$$
N(P)=2N(2+3\omega)+\frac{16N(\delta)}9\cdot3
       +4N(\delta)+16=14+16+12+16=58 .
\tag{11}
$$
这也与 $N(W)=72$、$N(a\mathfrak t)=14$ 和 $P\perp\mathfrak t$ 相符。

## 3. 实际清分母及全标准半特征

P 的原系数在 $\delta^{-1}\mathcal O_K$ 中。取真正的整行
$$
\boxed{
P_0=\delta P
=(-2+3\omega,\,-6,\,-1+6\omega,\,
  1+3\omega,\,-4+\omega,\,4\delta)\,\xi .
}
\tag{12}
$$
各系数范数依次为
$$
19,\quad36,\quad43,\quad7,\quad21,\quad48,
\qquad N(P_0)=174 .
\tag{13}
$$
所以原 P58 的标准整实现是 degree174 的三倍覆盖，不能直接将整个实际来源称作未覆盖的 $\mathcal S_{58}$。

在生成变量中，P0 嵌入是 $P_0^t z$，不是 $\bar P_0^t z$。
原 product sigma 的极化拉回度数等于 (13)。其半特征也完整确定：
模二恰四个系数非零，另外两个为 $-6$、$4\delta$。
等价地，四个奇范数 isogeny 的 kernel 点和为零；
两个偶范数 isogeny 都含完整 $E[2]$，其 kernel 点和也为零。
因此刚性化线丛准确为
$$
\boxed{
\mathcal L_{P_0}\simeq
  \mathcal O_{E_{17}}(174[0]).
}
\tag{14}
$$
没有一个未记的二挠 flat twist。

取 $B_P$ 为生成嵌入 $z\mapsto P_0^t z$ 的连通 Hermitian 正交补
（在生成坐标列上为 $\ker(\bar P_0)$ 的连通分量）。
由于 $p\nmid174$，原 p 整格的投影
$$
e_P=\bar P_0^tP_0/174
\tag{15}
$$
整且幂等，原格在 p 处分成 P0 轴和正交伙伴格。
在代数 isogeny
$$
E_{17}\times B_P\longrightarrow E_{17}^6,\qquad
(z,w)\longmapsto P_0^t z+j(w)
$$
下，交叉极化为零，原 rigidification 给外张量分裂
$$
\mathcal L\longmapsto
   \mathcal L_{P_0}\boxtimes\mathcal L_{B_P}.
\tag{16}
$$
(9) 说明 C、F、G、$\mathfrak t$ 全在第二因子方向。

对于 q 中原 C 角平均，逐个有理 CM 变换固定 P0 并保其正交补；
其三处分母和原中心相位均保留。它不改变 (14) 的第一线丛。
原 $\mathcal T$ 也固定 P，故同一论证可用于 R764 的
$h_W=\omega^2\mathcal T_*e_0$，但各常数须按原来源保留。

## 4. 所有实际有限门的有限化，不穿过门作边际替换

固定 p、N、n 及所附有限门。将 q 写为其实际有限混次和
$$
q(\xi)
 =\sum_\rho
   a_\rho\,b^{-h_\rho}\Omega_p^{-d_\rho}
   Q_\rho(C,F,G)\,1_{\mathcal E_\rho}(\xi),
\qquad d_\rho=\deg Q_\rho=6h_\rho.
\tag{17}
$$
零次数块同样允许；原整逆系数 $a_\rho$ 含完整
$\lambda,\kappa,\kappa^N$，固定参数后均为代数数。
若原写法进一步分块，就逐个使用它自己的 (17)，不统一删去周期。

对每一项，$\mathcal E_\rho\cap\mathcal D$ 是模某个实际有限 $p^M$ 的集合。
保完整六变量 Fourier 公式
$$
1_{\mathcal E_\rho\cap\mathcal D}(\xi)
 =p^{-6M}\sum_{a,v\bmod p^M}
  1_{\mathcal E_\rho\cap\mathcal D}(v)\,
  \zeta_{p^M}^{\,a\cdot(\xi-v)} .
\tag{18}
$$
这不将 (6) 分解成独立的 Y/P 边际。
P0 与其正交补的 p 整分裂 (15) 将每个加性角色分为第一轴和伙伴部分。
第一轴是实际 formal p-power torsion 平移，伙伴部分保持所有剩余变量和 gate 系数。

应用 R745 第3节的 Bannai–Kobayashi 第一式，保所有 Mumford 配对、
quarter-safe 半提升和中心相位。因为这里的原第一线丛是 (14)，
每一项都是它的实际 p-primary 平移及正交伙伴的有限 Taylor jet。
沿伙伴取 $Q_\rho$ 的 $d_\rho$ 阶 jet，再取 $\mathfrak t$ 的一阶 jet，
不会改变第一轴 automorphy factor。由 (17) 的 $\Omega_p^{-d_\rho}$，
只有分子 $\mathfrak t$ 贡献的一个 $\Omega_p$ 尚需单独除去。

准确地，定义
$$
\nu_{\mathcal D}
 =\Omega_p^{-1}(P_0)_*
    \bigl(1_{\mathcal D}\,\mathfrak t q_N^*e_0\bigr).
\tag{19}
$$
它在固定有限门层上是**有限个代数系数的标准 $\mathcal S_{174}$ 截面及其实际 p-primary Mumford 平移**。
没有任意未知的 $\mathbf C_p$ 伙伴系数。

标准未平移空间的完整代数基可取
$$
F_{j,b}=\sigma_b^{174}x_b^j\quad(0\le j\le87),\qquad
G_{j,b}=\sigma_b^{174}y_bx_b^j\quad(0\le j\le85).
\tag{20}
$$
共 $88+86=174$ 个。所用极帽准确为 $2j\le174$、
$3+2j\le174$。取足够多的代数 Taylor 系数即可恢复每个 jet 的全部坐标；
非零 degree174 截面在一点的零阶不超过174，故此恢复有限且唯一。
这只是一般代数证明，没有新增数值计算。

在所选 ordinary CM 型中，p-primary Mumford 平移的原测度作用是
$\nu_F\mapsto\zeta_{p^M}^{ax}\nu_F$。
因此 (19) 可准确写成
$$
\boxed{
\nu_{\mathcal D}
 =\sum_{j=0}^{87}\Phi_j(x)\nu_{F_{j,b}}(x)
  +\sum_{j=0}^{85}\Psi_j(x)\nu_{G_{j,b}}(x),
}
\tag{21}
$$
其中 $\Phi_j,\Psi_j$ 是模 $p^M$ 的代数值函数，全部 Fourier 系数和原 lift 相位保留。
一个统一的有限 M 可取覆盖所有真实门层；不把伙伴的高层门擅降为模 p。

即使原总来源的 $\mu_6$ 型为5，(21) 的单个未平移基向量仍可有其它角型，
由对应 $\Phi_j,\Psi_j$ 补偿。不能先只保裸 type5 基。
在单位群上再作有限乘法角色展开，
$$
\Phi_j|_{\mathbf Z_p^\times}
 =\sum_{\chi\bmod p^M}\widehat\Phi_j(\chi)\chi ,
\tag{22}
$$
以及同样的 $\Psi_j$ 展开，得到真正的有限 physical-character 矩。
这里不把一般 p-local Weil 向量与一变量 $\chi$ 测试混同；
(22) 来自 (18)—(21) 已付的原测度平移。

因为 $P_0=\delta P$ 且 $\delta$ 为原 p-unit，完整原行 (1) 等于
$$
\boxed{
\mathcal L_P(\mathcal D)
 =\delta\Omega_p
   \int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{\mathcal D}(x).
}
\tag{23}
$$
(6) 已确保 P-unit；(23) 不增删任何原域。

## 5. 基曲线和原周期的准确返回

令
$$
\theta=17^{1/6},\qquad
E_0:y^2=x^3+1,\qquad
\Omega_{p,0}=\theta\Omega_p .
$$
原微分给出精确缩放
$$
\sigma_b(z)=\theta^{-1}\sigma_1(\theta z),\quad
x_b(z)=\theta^2x_1(\theta z),\quad
y_b(z)=\theta^3y_1(\theta z).
\tag{24}
$$
于是 (20) 的每一个实际基向量满足
$$
F_{j,b}(z)=\theta^{-(174-2j)}F_{j,1}(\theta z),\qquad
G_{j,b}(z)=\theta^{-(171-2j)}G_{j,1}(\theta z).
\tag{25}
$$
它们的 Amice 测度在同一个物理 x 上相应缩放；没有把
$x\mapsto\theta x$，单位域和有限 $\chi$ 都保持原样。

将 (21)—(25) 合并，完整系数为
$$
\begin{aligned}
\mathcal L_P(\mathcal D)
=\delta\Omega_{p,0}\bigg(
 &\sum_{j=0}^{87}\theta^{-(175-2j)}
  \int_{\mathbf Z_p^\times}x^{-1}\Phi_j(x)d\nu_{F_{j,1}}\\
+&\sum_{j=0}^{85}\theta^{-(172-2j)}
  \int_{\mathbf Z_p^\times}x^{-1}\Psi_j(x)d\nu_{G_{j,1}}
 \bigg).
\end{aligned}
\tag{26}
$$
所以 $b=17$ 的原微分缩放在这里确实是显示的代数系数和共同周期。
这不等于已经证明负一值是点对数，也不把代数系数所在域冒充点坐标域。

## 6. 十七处的真实整格范围

先按 (24) 回到 $E_0$。此时原 product sigma 模型在17处为原未分歧球；
其已有非平凡有限 level 在2、3，P0 还引入29。
原 p-primary 门不在17处分歧。

更具体地，(12) 的系数在 $\mathcal O_{K,17}$ 中，$174$ 是单位，
故 (15) 在17处同样是整幂等元。原 Hermitian 自对偶格准确分成
$$
\mathcal O_{K,17}^{\,6}
 =\mathcal O_{K,17}\bar P_0^{\,t}
    \ \perp\ 
       \ker(P_0:\mathcal O_{K,17}^{\,6}\to\mathcal O_{K,17}),
\tag{27}
$$
第一因子的 Gram 是单位174，正交补也是 unimodular。
原 C 平均的分母只含3，其每个算子在17处为整 unitary；
原 $p^M$ Fourier 参数也在17处整。故它们都保这个第一轴的未分歧 lattice model。

(27) 是原六维格上的分裂，不是根据“度数不含17”猜测整个来源。
因此，本篇有限来源在17处没有新的 theta gluing、非平凡惯性字符或额外 torsion level。
用任何原全 CM/Weil 分解继续处理 (21) 时，第一轴17处必须保这个未分歧球。
伙伴 jets 和 (25) 的代数系数可以属于更大的数域；
它们不是改变第一轴17-local Schwartz 的操作。

此结论仅为真实有限来源的 local statement。
若后来建立相应全负一 Katz/点公式，还须通过真实 finite-twist descent
才能将它变为点坐标域在17处不分歧的结论；本篇不倒置这一步。

## 7. 原算术身份和补域全部保持

R767 的未切割完整来源是
$$
\Omega_p^{-1}Y_*(\mathfrak t q_N^*e_0)
 =-\frac{22}{21}\beta^N D_\omega .
\tag{28}
$$
所以其完整 Y-unit 负一值为
$$
\int_{Y\ {\rm unit}}\frac{\mathfrak t}{Y}q_N^*\,de_0
 =-\frac{22}{21}\beta^N\Omega_p I_{D_\omega}\ne0 .
\tag{29}
$$
这与 (1) 有两项准确区别：分母 P/Y 以及全部真实门。
在同一 $\mathcal D$ 上，始终有有限的精确关系
$$
\boxed{
\frac{\mathfrak t}{P}
 -\frac{\mathfrak t}{b_YY}
 =-\frac{\mathfrak t(a\widehat{\mathfrak s}+2\widehat d)}
         {b_YY\,P}.
}
\tag{30}
$$
把 (29) 限到 $\mathcal D$ 时，还须保
$\{Y\ {\rm unit}\}\setminus\mathcal D$ 的完整积分。
(30) 不是一个已经为零的残差，也没有从 $p^N$ 的范数界推其点惯性投影为零。

R764 的两 W 首差仍准确为
$$
-a(\omega^{2j}-\omega^{2k})\lambda^n\beta^m
 d_p\kappa^m\,\mathcal L_P(\mathcal D)
 +p^{4m}\mathcal O ,
\tag{31}
$$
并保 R764 的整个高阶级数与所有浅层/外部。
原 $J'_S=J'_T=0$ 没有在本篇产生 $\mathcal L_P(\mathcal D)=0$。

固定 p、N、n 和门层时，(21) 是一个真正有限来源池。
但沿 n 或 N 的任意极限，该池及系数可以变化。
R753 的限制继续适用：点因子幂等元不能据 (26) 对任意无限 p-adic 和或原整 log 展开交换极限。

## 8. 尚须支付的全角色与点域门

(12)—(27) 给了一个具体且有限的后续任务：
将实际 degree174 模型的全部有限 torus 分量及 (22) 的角色，
在原周期下识别为它们自己的 negative-one Katz 值，再付同一嵌入中的 point-factor 公式。

三倍覆盖有真实代价。未覆盖 degree58 对应的29-local模型以外，
$\mathcal S_{174}$ 还可含额外的3-local方向。
不能把整个174维空间当作 $[\delta]^*\mathcal S_{58}$ 的58维像，
也不能仅凭范数将所有分量套进 R748/R751 的原 $(\delta)$ 恰一次导子表。

BDP 2012 Proposition3.28 的原 good-pair 构造使用了其第3D节的
$\mathfrak d_K\Vert\mathfrak f_\nu$ 条件。
LZZ 的 Waldspurger 定理允许更一般的有限分歧，
但将其用于这里，仍须支付实际辅助 pair、全部局部 period、
精确 CM factorization 和两个点因子同一嵌入的下降；
不能只由其“无分歧限制”描述略过这些步骤。
本篇没有据此宣布所有 (26) 都已经属于17不分歧的椭圆点 logarithm 空间。

如果这项点公式完成，(27) 将给一个具体的17-local输入，
而 (25)—(26) 保证原 $b=17$ 缩放只作为代数系数留在 point-factor 之外。
目前已证明的是全部来源和规范，不是这个尚未付清的算术结论。

## 依赖与计算范围

- [R764](R764-y-preserving-six-axis-and-three-cd-exterior-domains.md)：原全部行、同域返回、完整 q 范围和 E 移动。
- [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：未切割纯 $D_\omega$ 身份及完整五伙伴首边界。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：原最终测试及其实际混次系数。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：有限 Fourier、完整 Mumford 平移和正交伙伴正矩代数性。
- [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)、
  [R751](R751-second-dyadic-character-point-fields-and-inertia-extraction.md)：
  原已付角色范围及精确点公式；本篇不扩大它们的假设。
- [R752](R752-native-mod-p-two-source-closure-and-point-inertia-extraction.md)：
  原 ordinary p-torsion 平移与 physical finite-character 展开。
- R753：有限 point-carrier 与极限的区别。
- Bannai–Kobayashi, *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*, Duke Math. J.153 (2010)；原预印本 v4 Theorems2.9、2.12 与 Proposition2.19。
- Bertolini–Darmon–Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*, Pacific J. Math.260 (2012)，第3D节与 Proposition3.28。
- Liu–Zhang–Zhang, *A p-adic Waldspurger formula*, Duke Math. J.167 (2018)，完整局部 period 与 Proposition4.3.6。

本篇为显示行、原整格与已付代数 theta 定理的直接证明；没有新增数值计算、辅助素数扫描或生成数据文件。
