# R841 — 原三阶平移的完整 Chow 纯性与端点的有限角色提取

日期：2026-11-16。**状态：下述群、曲线及 Chow 恒等式已证明。**

本篇保持 R831 的唯一原二退化端点，给出其最高 CM 纯性的
直接几何证明。它不使用 R832 中混合因子的 rank-zero 论证，
也不证明这个端点非零。原 $q/q^4$、三个有序角色、所有
$X_0/X_1$ 次数和系数域均保留。

## 1. 固定实际来源和目标

沿 [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)，取
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
N=10404,\quad M=2601,\quad
X=X_0(N),\quad C=X_0(M).
$$
原第一形式和后两个形式为
$$
f=\theta(\psi_{17}),\qquad
g=g_j=\theta(\eta_j^{-2}\psi_0),\qquad
h=g_k=\theta(\eta_k^{-2}\psi_0),
$$
有序对仍为
$$
(j,k)=(10,16),(16,4),(4,10).
\tag{1}
$$
对应的最高角色分别是
$\lambda_4,\lambda_{10},\lambda_{16}$，其中
$\lambda_\nu=\eta_\nu^{-1}\psi_0^3$。

取原 cusp $\infty$ 为基点，令 $\Delta_X$ 为 modified diagonal。
原实际映射为
$$
q_0:X\to C,\quad z\mapsto z,\qquad
q_2:X\to C,\quad z\mapsto4z,\qquad \deg q_0=\deg q_2=6.
$$
这里 $z$ 是上半平面变量。共同目标中的原类准确为
$$
Z=Z_{02}:=
(e_f\otimes e_g\otimes e_h)_*
(\mathrm{id}\times q_0\times q_2)_*\Delta_X.
\tag{2}
$$
所有投影均先包含原 $h^1$ Chow–Künneth 投影。
所需固定系数域 $\mathcal E$ 包含 $K$ 及三个原 Hecke
系数域；几何数据可在一个先于研究素数 $p$ 固定的有限扩域上解释。

本篇证明
$$
\boxed{Z=\operatorname{pr}_{\lambda_\nu}Z}
\tag{3}
$$
以及第6节的两个完整有限角色公式。
式(3)是实际 Chow 等式，不只是某个实现或某一个 AJ 槽的等式。

## 2. 两个原层级上的真实三阶自同构

对 $L=N,M$，令
$$
r=\begin{pmatrix}1&1/3\\0&1\end{pmatrix},\qquad
R_L:X_0(L)\to X_0(L),\quad z\mapsto z+1/3.
\tag{4}
$$
若 $\gamma=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)
\in\Gamma_0(L)$，则
$$
r\gamma r^{-1}
=
\begin{pmatrix}
A+C/3&B+(D-A)/3-C/9\\
C&D-C/3
\end{pmatrix}.
\tag{5}
$$
因为 $9\mid L$，有 $9\mid C$；又 $AD\equiv1\bmod3$，
所以 $D\equiv A\bmod3$。右侧是行列式1的整数矩阵，
其下左项仍被 $L$ 整除。对 $r^{-1}$ 同样成立，
故 $r$ 正规化 $\Gamma_0(L)$。
$r^3$ 是整数平移，而 $r$ 本身不在该群中，
所以 (4) 的阶准确为3。

它固定 cusp $\infty$；对原 $Q=e^{2\pi iz}$，
$$
R_L^*Q=\omega Q.
\tag{6}
$$
有理矩阵对应先给在有限数域上定义的代数 modular correspondence；
正规化使其成为自同构。
对任意固定 $\omega$ 的绝对 Galois 元素，共轭自同构在
原 cusp 的展开仍为(6)，由 q-expansion 原理与曲线态射的
唯一性，它等于原自同构。因此 $R_L$ 定义于 $K$。
这里没有把 $\Gamma_0(L)$ 的正规化错误延到整个
$\Gamma_1(L)$；原 $X_1$ 返回将在第7节通过真实遗忘映射支付。

原两个退化映射满足
$$
\boxed{
q_0R_N=R_Mq_0,\qquad
q_2R_N=R_Mq_2.
}
\tag{7}
$$
第二式在上半平面是 $4z+4/3$ 与 $4z+1/3$，
相差一个真正整数平移，故在 $C$ 上相同。
式(7)明确使用原 $q^4$ 位置，未换成同一退化副本。

## 3. 原三份 CM 因子的绝对三阶特征

原 CM 整理想展开的三处均被排除。
每个素于3的 $K$-理想，其范数模3为1：
split 素理想的范数为 $1\bmod3$，
inert 素理想的范数是有理素数的平方。
因此三个原 normalized forms 及其全部 Hecke 系数域嵌入
都满足
$$
F(Q)=\sum_{n\equiv1\ (3)}a_n(F)Q^n,
\qquad F=f,g,h.
\tag{8}
$$
这不是从前若干 Fourier 系数猜测支撑，而是原完整
Hecke-character ideal formula。

由(6)，$R^*$ 在各全纯微分 $F(Q)dQ/Q$ 上的特征为
$\omega$。由于它是曲线自同构，其 Hodge 共轭线上
特征为 $\omega^2$。这两条正是原 CM 因子的两个
rank-one 分量。

还须把该判断送回真正的 $h^1$ 对应。
在各原二维 CM Hecke 因子上，$R^*$ 保全纯线及其共轭，
因而保该因子。对其正交补，使用 $R$ 的有限阶和
极化相容性得到同样稳定性。
所以 $R$ 与 $e_f,e_g,e_h$ 在 $h^1$ 实现中交换。
曲线 $h^1$ 的有理对应由 Jacobian 同态给出，
该实现忠实；故这些交换式及两条特征式均在
$h^1$ Chow 对应环中成立。

为避免 push/pull 的标签混淆，后文用**推前**定义精确投影。
在第 $i$ 个原 CM 因子上，对 $\zeta=\omega,\omega^2$ 置
$$
e_i[\zeta]
=
e_i\,\frac13\sum_{a=0}^2\zeta^{-a}(R_i)_*^a,
\qquad i=f,g,h.
\tag{9}
$$
这里 $R_f=R_N$，$R_g=R_h=R_M$。
有
$$
e_i[\omega]+e_i[\omega^2]=e_i,\qquad
(R_i)_*e_i[\zeta]=\zeta e_i[\zeta].
\tag{10}
$$
推前在全纯拉回线上的特征与拉回相反；
(9)已把这一点固定，后续不偷换两个标签。

沿 R826/R832 已付的八维 CM 张量分解，
$$
\boxed{
\operatorname{pr}_{\lambda_\nu}
=
e_f[\omega]\otimes e_g[\omega]\otimes e_h[\omega]
+
e_f[\omega^2]\otimes e_g[\omega^2]\otimes e_h[\omega^2].
}
\tag{11}
$$
两项是同一个原 $AI(\lambda_\nu)$ 的互为共轭的两条线。
这里只用原完整 Hecke 角色的乘法：
$\psi_{17}\beta_j\beta_k=\lambda_\nu$；
不由三阶特征独自猜出有限 $\eta_\nu$。
另外六条线仍是 R826 的原三个混合因子。

## 4. Modified diagonal 的原基点与完整不变性

由于 $R_N\infty=\infty$，小对角及每一个 modified
diagonal 基点项都逐式保持，故
$$
(R_N\times R_N\times R_N)_*\Delta_X=\Delta_X.
\tag{12}
$$
此处没有任意基点的隐含改换，也无需仅在 cohomology 中
消去基点项。

用(7)推前，再用第3节的真实 Hecke 投影交换式，得到
$$
\boxed{
(R_N\times R_M\times R_M)_*Z=Z.
}
\tag{13}
$$
这个作用在(11)两条线上均为1。
对其它六种选择，三个特征中恰有一种与另两种不同，
其乘积为 $\omega$ 或 $\omega^2$。将相应完整 CM
幂等元施于(13)，有
$$
(\omega-1)Z_{\rm mixed}=0
\quad\text{或}\quad
(\omega^2-1)Z_{\rm mixed}=0.
$$
系数域为特征零，故所有混合项为零，得到(3)。

这份证明直接作用原 $Z$；
它不依赖混合 motive 的全部 $CH^2$ 是否为零。
R832 对那些混合因子的 rank-zero/Chow 结论仍保持，
但在本篇原端点的纯性证明中不再是必要输入。

## 5. 精确的循环商与同一端点的交换图

写 $L=9L_0$，令 $d_3=\operatorname{diag}(3,1)$。
直接共轭得到
$$
d_3\Gamma_0(9L_0)d_3^{-1}
=\Gamma_0(3L_0)\cap\Gamma^0(3).
\tag{14}
$$
右侧模3是上三角群的对角子群。
上三角矩阵的两个对角元在 $\mathbf F_3^\times$ 中相等，
所以该对角子群为中心；商是阶3的上 unipotent 群。
故右侧是 $\Gamma_0(3L_0)$ 的 normal index-three 子群。

得到原代数曲线上的 degree3 循环商
$$
\boxed{
\pi_L:X_0(L)\longrightarrow X_0(L/3),
\quad z\longmapsto3z,\quad
\operatorname{Deck}(\pi_L)=\langle R_L\rangle.
}
\tag{15}
$$
在 cusp $\infty$，参数为 $Q\mapsto Q^3$；
泛型次数为3，故该 cusp 的完全分歧不添别的泛型 multiplicity。

令
$$
\bar X=X_0(3468),\qquad \bar C=X_0(867),
$$
并在这两层保持 $z\mapsto z$、$z\mapsto4z$ 的两个
退化映射 $\bar q_0,\bar q_2$。则
$$
\pi_Mq_0=\bar q_0\pi_N,\qquad
\pi_Mq_2=\bar q_2\pi_N.
\tag{16}
$$
式(16)是原端点的真实交换图。
它没有将某条 nontrivial deck-character 线识别为下层
平凡局部系；也没有将这个循环商本身当成 R814
canonical cycle 的比较。

## 6. 保持全来源的九项有限角色提取

对 $a,b\in\mathbf Z/3$，仍在同一共同目标中定义
$$
Z_{a,b}^{R}
=
(e_f\otimes e_g\otimes e_h)_*
(\mathrm{id}\times R_M^a q_0\times R_M^b q_2)_*\Delta_X.
\tag{17}
$$
于是
$$
Z_{a,b}^{R}
=(\mathrm{id}\times R_M^a\times R_M^b)_*Z.
\tag{18}
$$
每一项都保原 modified diagonal、原两个 degree6
退化和同一 Hecke 投影；不是另挑一个局部向量后认作原类。

记
$$
Z^{[\zeta]}
=(e_f[\zeta]\otimes e_g[\zeta]\otimes e_h[\zeta])_*Z,
\qquad \zeta=\omega,\omega^2.
$$
由(3)、(9)有准确的两个分量式
$$
Z_{a,b}^{R}
=\omega^{a+b}Z^{[\omega]}
 +\omega^{2(a+b)}Z^{[\omega^2]}.
\tag{19}
$$
有限 Fourier 正交遂给
$$
\boxed{
Z^{[\zeta]}
=\frac19\sum_{a,b=0}^2\zeta^{-(a+b)}Z_{a,b}^{R},
\qquad Z=Z^{[\omega]}+Z^{[\omega^2]}.
}
\tag{20}
$$
$1/9$ 是九项完整角色提取的实际归一；
没有任何未指定的 Gauss sum、period 或平方根。
这一公式给两条原 $K$-CM 线的真实有限几何代表。
它与 R838 的临界读数相容，但不证明其中任一条非零。

## 7. 全部 $X_0/X_1$ 与 old 副本次数仍原样保持

式(2)、(3)、(17)–(20)均先在 R831 的共同
$X_0$ 目标上建立，所以没有新增 degree6 乘子。
返回原 $X_0(N)^3$ 的选定 old 副本仍准确为
$$
\Delta_X^{(0,2)}
=6^{-2}(\mathrm{id}\times q_0^*\times q_2^*)Z.
\tag{21}
$$

令 $a:X_1(N)\to X_0(N)$、$b:X_1(M)\to X_0(M)$
为原遗忘生成元映射，并令 $A=a\times b\times b$。
R831 的实际次数与来源身份为
$$
D_X=1632,\qquad D_C=816,\qquad
12D_C=6D_X,
$$
$$
\boxed{
A_*Z_{02}^{(1)}=D_XZ,\qquad
Z_{02}^{(1)}=D_C^{-2}A^*Z.
}
\tag{22}
$$
原 $X_1$ 三因子上的单副本类则是
$$
\Delta_{X_1(N)}^{(0,2)}
=
12^{-2}
(\mathrm{id}\times(q_0^{(1)})^*
                \times(q_2^{(1)})^*)Z_{02}^{(1)}.
\tag{23}
$$
所有对应和 CM 投影沿(22)实际运输，故(3)同样成立于
原 $Z_{02}^{(1)}$ 及(23)。
无需也没有声称 $r$ 直接正规化 $\Gamma_1(N)$。
同一 $X_0$ de Rham 测试的拉回在 $X_1$ 上仍带原
projection-formula 倍率 $D_X$；(20)的 $1/9$ 不改变它。

这里所有次数仅含2、3、17因子，原 $p>17$ 范围不变。
本篇没有重新选 ray、端点、finite conductor 或 period。

## 8. 与原几何表达及后继问题的关系

R839 已给原 $Z$ 在 $E_0^3$ 上的固定有限曲线像与最高
Ceresa 表达。本篇说明该原 modified diagonal 来源本身
已由实际三阶平移精确落到最高 CM 因子，并给(20)的两个
完整有限 character representatives。
这使最高纯性不再依赖一个 mixed rank-zero 推导，
但不产生第二个原端点类或额外中央零。

尚未支付的仍是这个指定类的非零，或到 R814
canonical cycle 的实际非零对应。
同一 motive、同一有限角色、同一 Frobenius 根和同一
三阶特征均不足以代替这条比较。
R838 的完整临界 Hecke projector、最高主极项、
原 Euler 和 period 继续保留。

本篇无新增数值计算，无目标素数扫描，也不生成可重算数据。

## 9. 已用来源

- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)：
  原三份 CM Hecke 角色、完整八维分解及全部有限导子。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原共同目标 $Z_{02}$、两个端点、全 old 与 $X_1$ 次数。
- [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)：
  只在本篇(11)用其已识别的原八维 CM motives；
  本篇纯性证明未使用其中的 rank-zero 输入。
- [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原权一对应的真实曲线展开与 Jacobian 同态忠实性；
  本篇没有以高余维实现忠实性代替 Chow 恒等式。
- [R838](R838-original-critical-hecke-reader-and-three-endpoint-periods.md)
  附录 C：同一三阶平移在完整变权 packet 的 self-twist、
  $e$ 偶及原三条临界系数的奇性。
