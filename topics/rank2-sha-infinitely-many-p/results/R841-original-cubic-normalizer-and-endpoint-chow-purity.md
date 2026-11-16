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


## 附录 A. 原实际曲线像的最低亏格与 genus-four 分支型

本附录加强 R839 §7 的**这份原端点表达**。它不对任意
三条曲线态射强加对称性，而是先在真实 Jacobian 同态上
逐项平均，使原完整权一对应保持不变。

### A.1. 对原整个权一对应作等变平均

取 R839 §7 的固定有限定义域 $F$、系数域 $\mathcal E$
和原三个对应 $\Gamma_i$。仍以各原 cusp $\infty$ 为基点，
令
$$
J_i=J(C_i),\qquad C_f=X,\quad C_g=C_h=C,
$$
令 $r_i$ 是 $R_{C_i}$ 在 $J_i$ 上诱导的真实群自同构。
在 $E_0$ 上固定 $u=[\omega]$，规范为
$u^*\omega_{E_0}=\omega\,\omega_{E_0}$。

R839 的 CM 相容权一同构，以及本篇 §3 的完整特征，给
$$
\Gamma_i r_i=u\Gamma_i
\quad\text{于 }\operatorname{Hom}(J_i,E_0)\otimes\mathcal E .
\tag{A1}
$$
这里用的是 Jacobian 的协变同态；等价的微分式为
$r_i^*\Gamma_i^*=\Gamma_i^*u^*$。
原 $\Gamma_i$ 经整个 $e_i$，而非只经最高三重张量分量；
在该权一因子的全纯与反全纯两线上，(A1)都成立。
权一同态的实现忠实，故 (A1) 是实际同态等式。
这不改变正文(9)对 Chow 推前特征的约定。

把原展开写为
$$
\Gamma_i=\sum_\alpha c_{i,\alpha}\varphi_{i,\alpha},
\qquad \varphi_{i,\alpha}\in\operatorname{Hom}(J_i,E_0).
$$
原有理分母已吸收进 $c_{i,\alpha}$。定义实际整数和同态
$$
\varphi^\circ_{i,\alpha}
=\sum_{a=0}^2u^{-a}\varphi_{i,\alpha}r_i^a .
\tag{A2}
$$
于是逐项有
$$
\varphi^\circ_{i,\alpha}r_i=u\varphi^\circ_{i,\alpha},
\qquad
\boxed{\Gamma_i=\frac13
 \sum_\alpha c_{i,\alpha}\varphi^\circ_{i,\alpha}.}
\tag{A3}
$$
第二式直接由 (A1) 得到；它保持**原整个 $\Gamma_i$**，
不是只保持其最高投影。所有 $\varphi^\circ$ 仍定义于同一个
固定有限域上；(A2)只使用已定义的 $R$ 与 $[\omega]$，
未加入随 $p$ 变化的对象。

置
$a^\circ_{i,\alpha}=\varphi^\circ_{i,\alpha}\circ
\operatorname{AJ}_{C_i,\infty}$。
因为 $R_{C_i}\infty=\infty$，它们满足真实曲线态射恒等式
$$
a^\circ_{i,\alpha}R_{C_i}=u\,a^\circ_{i,\alpha}.
\tag{A4}
$$
用这些态射和 (A3) 的系数重新展开 R839(18)，得到同一
$\widetilde Z$ 的有限曲线表达；每个实际三元态射
$$
\Phi:X\longrightarrow E_0^3,\qquad
\Phi=(a_f^\circ,\ a_g^\circ q_0,\ a_h^\circ q_2)
$$
都严格满足
$$
\boxed{\Phi R_N=u_A\Phi,\qquad u_A=[\omega]^{\times3}.}
\tag{A5}
$$
这里使用正文(7)的两条原退化等式。三个 $1/3$ 只在展开
$\Gamma_f\otimes\Gamma_g\otimes\Gamma_h$ 的系数中出现；
它们不改变原 Chow 类，不引入新的 $q/q^4$ 次数。
正文(21)–(23)的全部 $X_0/X_1$ 倍率保持不变。

### A.2. 生成整个 $E_0^3$ 的原像必须有亏格至少四

对 (A5) 中一个非恒定 $\Phi$，取其像的正规化 $D$，
写
$$
X\xrightarrow{\vartheta}D\xrightarrow{\iota}A=E_0^3.
$$
保留有限推前次数：
$\Phi_*[X]=\deg(\vartheta)\,\iota_*[D]$。
若像落在一个真阿贝尔子簇的平移中，R839 §6 已给其
最高投影为零。因此以下只考虑像生成整个 $A$ 的项。

(A5)使 $u_A$ 在 $D$ 上唯一提升为自同构 $v$，且
$v^3=1$。它的阶确为3：若 $v=1$，整个像逐点被 $u_A$
固定，便落在有限群 $A[u_A-1]$ 中，与像为曲线矛盾。
取 $\vartheta(\infty)$ 作基点；它由 $v$ 固定。
于是原 $\iota$ 给满同态
$$
q:J(D)\longrightarrow A,\qquad qv_J=u_Aq .
\tag{A6}
$$
其微分拉回是三维单射，故
$$
\dim H^0(D,\Omega^1)_{\omega}\ge3.
\tag{A7}
$$

若 $g(D)=3$，(A7)使 $v^*$ 在全部全纯微分上都是标量
$\omega$，因而在 canonical projective space 上恒等。
非超椭圆曲线的 canonical map 是嵌入，所以迫 $v=1$；
超椭圆曲线的 canonical map 为二次映射，其自同构核
至多为阶2，仍不含这个阶3的 $v$。两种情况均矛盾。
故
$$
\boxed{g(D)\ge4.}
\tag{A8}
$$
这比 R839 对任意曲线表达得到的亏格至少三更强，
但准确范围是本附录保持原 $\Gamma_i$ 后得到的等变表达。
它不证明任一曲线项或它们的指定线性组合非零。

### A.3. 最小亏格四时的完整 Riemann–Hurwitz 与特征计算

设 $g(D)=4$，记 $B=D/\langle v\rangle$，$g_0=g(B)$。
除 (A7) 的三条 $\omega$ 线外，仅有一个剩余特征。
若它也是 $\omega$，canonical map 的同一论证再次排除。
若它是1，则 $g_0=1$；若是 $\omega^2$，则 $g_0=0$。

下面给出所需 cyclic-cover 维数式，包含可能的未分歧
线丛扭曲。设分支点局部 monodromy 分别为 $v$、$v^2$，
数目为 $r_1,r_2$；$r=r_1+r_2$。特征零下每个非平凡
稳定子均为整个三阶群，故
$$
2g(D)-2=3(2g_0-2)+2r.
\tag{A9}
$$
取循环覆盖线丛 $\mathscr L$，使
$\mathscr L^3\simeq\mathcal O_B(D_1+2D_2)$，
其中 $D_i$ 为相应的约化分支除子。局部正规化给
$$
\pi_*\mathcal O_D
=\mathcal O_B\oplus\mathscr L^{-1}
 \oplus\mathscr L^{-2}(D_2),
\quad
\deg\mathscr L=(r_1+2r_2)/3.
\tag{A10}
$$
按 $v(y)=\omega y$ 规范，后两项的特征依次为
$\omega,\omega^2$。对 (A10) 作相对 duality，再用
Riemann–Roch，得到
$$
\begin{aligned}
d_\omega&:=\dim H^0(D,\Omega^1)_\omega
 =g_0-1+\frac{2r_1+r_2}{3},\\
d_{\omega^2}&:=\dim H^0(D,\Omega^1)_{\omega^2}
 =g_0-1+\frac{r_1+2r_2}{3}.
\end{aligned}
\tag{A11}
$$
此处后两条 line-bundle correction 的次数均严格为正，
因为本段 (A9) 的 $r$ 为3或6；故相应的 $H^1$ 项为零。
这也说明 (A11) 不依赖未分歧的 degree-zero 扭曲。

在剩余特征为1的假设下，$g_0=1$，(A9)给 $r=3$。
又 $r_1+2r_2$ 被3整除，所以 $(r_1,r_2)$ 只能为
$(3,0)$ 或 $(0,3)$。由 (A11)，非平凡特征维数为
$(2,1)$ 或 $(1,2)$，与 (A7)要求 $(3,0)$ 矛盾。
故该假设也不成立。

唯一可能是
$$
\boxed{
g_0=0,\qquad
(d_1,d_\omega,d_{\omega^2})=(0,3,1),\qquad r=6.
}
\tag{A12}
$$
将 $d_\omega=3,d_{\omega^2}=1$ 代回 (A11)，得
$$
\boxed{r_1=6,\qquad r_2=0.}
\tag{A13}
$$
即六个分支点的 monodromy **全部相同**。
若同时反转生成元及 $\omega$ 的标签，则变成六个 $v^2$；
这只是同一结论的整体共轭，不能逐点任意改号。

在一个仍先于 $p$ 固定的有限扩域上，把一个未分歧点移到
$\mathbf P^1$ 的无穷远，便可写成
$$
D:\quad y^3=c\prod_{a=1}^6(x-b_a),
\qquad b_a\ne b_b\ (a\ne b),\quad c\ne0,\quad v(y)=\omega y.
\tag{A14}
$$
无穷远不分歧。全纯微分基可取
$$
\frac{dx}{y^2},\quad\frac{x\,dx}{y^2},\quad
\frac{x^2\,dx}{y^2},\quad\frac{dx}{y}.
\tag{A15}
$$
前三条的特征为 $\omega$，最后一条为 $\omega^2$，
与 (A12) 完全一致。

### A.4. 最小情形还保原 $E_0^3$ 的同源约束

在 $g(D)=4$ 时，(A6)的连通核是一个椭圆曲线 $B_1$。
它由 $v_J$ 保持；由全纯微分的正合列及 (A12)，
$v_J|_{B_1}$ 在其微分上的特征是 $\omega^2$。
因此 $B_1$ 有原点保持的阶3自同构，几何 $j$-不变量为0。
完全可约性遂给
$$
\boxed{J(D)\sim E_0^4}
\tag{A16}
$$
（在某个固定有限扩域上），其中 $v_J$ 的全纯
特征 signature 为 $(3,1)$。它不是在整个 $J(D)$ 上的
标量 $[\omega]$；这个区别正是 (A8) 的要点。

(A14) 的一般六点覆盖不满足 (A16)。因此不能任取一个
六点三重覆盖来替换原 $\Phi$，也不能由本附录的必要条件
推断它具有原17处 Artin 数据或等于 R814 的 canonical 类。
原实际同态、三个完整角色、$q_0/q_2$ 与完整临界 period
仍须保持。这里没有任何新的数值计算或目标素数扫描。


## 附录 B. 原端点的对称双线性、同一实际映射与最小属四模型

本附录先在原 Jacobian 对应上保留完整 Hecke 投影，再作
polarization。结论是：R839 的原端点可以准确写成
$\Pi(F,a q_0,a q_2)_*[X]$ 的固定有限线性组合。
这些实际曲线同时具有原三阶作用和一条二阶作用。
当其像的正规化达到附录 A 的最低亏格四时，六分支模型
因而进一步受到下面 (B17) 的严格限制。

### B.1. 原有理 Hecke packet 中的实际 Hom

令 $e_{\mathcal G}\in\operatorname{End}^0J(C)$ 是原
$g_4,g_{10},g_{16}$ 全部 Galois 共轭所成的有理 Hecke 因子
的幂等元。原两份 $\Gamma_g,\Gamma_h$ 均满足
$\Gamma_i e_{\mathcal G}=\Gamma_i$。第一份则满足
$\Gamma_f e_f=\Gamma_f$，其中原 $f$ 为有理新形式。
这里保留整个有理 packet，不能把带非有理系数的单个
Hecke 幂等元误作一个实际曲线态射。

在附录 A 的有限 Hom 展开中，先将每个同态右复合
$e_f$ 或 $e_{\mathcal G}$。清除固定整数分母，并将分母
吸收进原代数系数后，各项仍为实际 Jacobian 同态，而且
每项都经所需有理 Hecke 因子。再作 (A2) 的整数和平均。
这些有理 Hecke 因子与原 $R$ 交换，故这两步相容，并保持
原整个 $\Gamma_i$，不只是它的某个三重张量投影。

因此可将原表达写为有限和，其各项的实际映射
$$
F:X\longrightarrow E_0,\qquad a,b:C\longrightarrow E_0
\tag{B1}
$$
都在 cusp $\infty$ 取零，$F$ 经原 $e_f$，
$a,b$ 经 $e_{\mathcal G}$，并且
$$
FR_N=[\omega]F,\qquad aR_M=[\omega]a,\qquad
bR_M=[\omega]b .
\tag{B2}
$$
这里及下文，加法和负号均是 $E_0$ 上的真实群运算。
特别 $a+b$ 仍是同一个有理 packet 中的实际映射，仍满足 (B2)。

### B.2. 最高投影后的真实 Chow 双线性

对 (B1) 定义
$$
\mathcal B(F;a,b)
=\Pi\,(F,a q_0,b q_2)_*[X]
\quad\in CH^2(E_0^3)_{\mathcal E}.
\tag{B3}
$$
$\Pi$ 是 R839 的最高 CM Chow 幂等元；
特别 $\Pi=\Pi(\pi_1^{E_0})^{\otimes3}$。

先支付 (B3) 对 Hom 的加性，而不借一般高余维实现忠实性。
在 $E_0\times E_0$ 上取以原点规范化的 Poincaré 线丛
$$
\mathscr P=\mathcal O(\Delta-E_0\times\{0\}-\{0\}\times E_0).
$$
对实际 $a:C\to E_0$，其图形除子满足
$$
[\Gamma_a]
=c_1((a,\mathrm{id})^*\mathscr P)
+[C\times\{0\}]
+\operatorname{pr}_C^*c_1(a^*\mathcal O_{E_0}(0)).
\tag{B4}
$$
最后两项在目标 $E_0$ 上施 $\pi_1$ 后消失。
Poincaré 线丛对第一群变量的 biadditivity 给
$$
(\pi_1)_*[\Gamma_{a+b}]
=(\pi_1)_*[\Gamma_a]+(\pi_1)_*[\Gamma_b]
\quad\text{于 }CH^1(C\times E_0)_{\mathbf Q}.
\tag{B5}
$$
把 (B5) 与原小对角、另两个图形对应复合，再施 $\Pi$，
得到 $\mathcal B$ 对 $F,a,b$ 各自的加性和有理线性。
基点项被相应 $\pi_1$ 杀掉，所以这里的小对角写法与
R839 中的 modified diagonal 完全相同。

### B.3. 两因子交换在最高 Chow 因子上的准确负号

令 $\sigma_{23}$ 交换 $E_0^3$ 的第二、第三坐标。
它与 $\Pi$ 交换。在 Betti 实现中，$\Pi$ 的像只有
三份同一 CM 线的全正、全负张量；几何交换在两条线上
都为 $-1$，因为交换的两个上同调因子均为次数1。
这一步的负号是几何 Künneth 交换号，不能写成无号的
普通一维向量张量交换。

为将它提升为实际 Chow 等式，考虑
$$
P=\Pi\,\frac{1+\sigma_{23,*}}2.
$$
这是一个 Chow 幂等元，且全部 Betti 实现为零。
$h(E_0^3)$ 是 Kimura finite-dimensional motive；
其数值平凡自对应为幂零。因此 $P$ 同时幂等、幂零，
故 $P=0$。于是完整对应环中有
$$
\boxed{\Pi\sigma_{23,*}=-\Pi.}
\tag{B6}
$$
此处只对这个已显示的幂等元使用幂零定理，
并未假定 Chow realization 对所有对应忠实。
同样，由 $\Pi\subset(\pi_1)^{\otimes3}$，直接有
$$
\Pi([-1]\times\mathrm{id}\times\mathrm{id})_*=-\Pi.
\tag{B7}
$$
所用有限维与幂零结论为 Kimura，
*Chow groups are finite dimensional, in some sense*,
Math. Ann. 331 (2005), 173–201，Corollary 4.4、
tensor-product 稳定性及 Proposition 7.5；
<https://doi.org/10.1007/s00208-004-0577-3>。
这里只需三条椭圆曲线的乘积这一已知范围。

### B.4. 原 $W_4$ 将反对称端点变成对称 Hom 形式

R831(12)、(16)在原曲线上准确给
$$
q_0w_4=q_2,\qquad q_2w_4=q_0,\qquad e_f(w_4)_*=-e_f.
\tag{B8}
$$
故对经 $e_f$ 的实际 $F$，
$$
Fw_4=-F+c_F,\qquad c_F=F(w_4\infty).
$$
这个常值不能在曲线层面无理由删掉；
R839 的最高投影对所有平移不变，恰好允许在 (B3) 中删去它。
将 $w_4$ 作用于源曲线，再用 (B6)、(B7)，得
$$
\begin{aligned}
\mathcal B(F;a,b)
&=\Pi\,(-F,a q_2,b q_0)_*[X]\\
&=\Pi([-1]\times\mathrm{id}\times\mathrm{id})_*
       \sigma_{23,*}(F,b q_0,a q_2)_*[X]\\
&=\mathcal B(F;b,a).
\end{aligned}
\tag{B9}
$$
两个负号分别来自原 $f$ 的 partial $W_4$ 和目标的
最高 CM 交换，均在实际 Chow 群中支付。

结合双线性，得到准确的 polarization：
$$
\boxed{
\mathcal B(F;a,b)=
\frac12\left(
\mathcal B(F;a+b,a+b)
-\mathcal B(F;a,a)-\mathcal B(F;b,b)
\right).
}
\tag{B10}
$$
因此原 $\widetilde Z$ 是有限个
$$
\Pi\,\Phi_{F,a,*}[X],
\qquad
\Phi_{F,a}=(F,a q_0,a q_2),
\tag{B11}
$$
的固定代数系数线性组合，且每个 $a$ 均为 B.1 中的真实
有理 packet 映射。原 $\Gamma_f,\Gamma_g,\Gamma_h$、
其系数及整个有限 Artin 投影都保留在这个组合中。
不要求每一个单独的 (B11) 都已具有原指定 $\lambda_\nu$；
不能把这种逐项强化冒认为 (B10) 的结论。

### B.5. 同一实际映射的原二阶平移

在 $X=X_0(N)$ 上令
$$
S:z\longmapsto z+\tfrac12.
\tag{B12}
$$
因为 $4\mid N$，对
$\gamma=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)
\in\Gamma_0(N)$，
$$
\begin{pmatrix}1&1/2\\0&1\end{pmatrix}
\gamma
\begin{pmatrix}1&-1/2\\0&1\end{pmatrix}
=
\begin{pmatrix}
A+C/2&B+(D-A)/2-C/4\\ C&D-C/2
\end{pmatrix}
$$
仍为原整数群元素；逆共轭亦然。
$S^2$ 为整数平移，故 $S$ 是阶2自同构，固定 $\infty$，
且在其参数上 $Q\mapsto-Q$。它定义于 $\mathbf Q$，
并与正文的 $R_N$ 交换。

原 rational packet 的每个形式 $G$ 在2处均未分歧、
中心特征平凡，且因2在 $K$ 惰性而 $T_2G=0$。
以标准权二归一 $T_2=U_2+2V_2$，它的全部偶数 Fourier
项准确为 $-2G(Q^4)$，从而
$$
\boxed{G(-Q)=-G(Q)-4G(Q^4).}
\tag{B13}
$$
这对整个 packet 的线性组合同时成立。
原 $f$ 在2处的新 conductor exponent 为2，
其 $U_2$ 特征为零，所以全部偶数项为零：
$f(-Q)=-f(Q)$。

实际 $q_2$ 微分为 $4G(Q^4)dQ/Q$，不是裸 $G(Q^4)dQ/Q$。
用 (B13) 和 $q_2S=q_2$，因此有
$$
FS=-F,\qquad
a q_0S=-a q_0-a q_2,\qquad
a q_2S=a q_2.
\tag{B14}
$$
这是实际曲线映射恒等式：微分式先给 Jacobian 同态等式，
而全部映射在 $S$ 固定的 cusp $\infty$ 取零，故常值项为零。
这里没有使用 $S$ 在奇数层 $C$ 上的正规化；
所用 $S$ 始终作用于 $X$。

于是每个 (B11) 都同时满足
$$
\boxed{
\Phi_{F,a}S=L\Phi_{F,a},\qquad
L=
\begin{pmatrix}
-1&0&0\\
0&-1&-1\\
0&0&1
\end{pmatrix},
\qquad
\Phi_{F,a}R_N=[\omega]^{\times3}\Phi_{F,a}.
}
\tag{B15}
$$
$L$ 是实际 $E_0^3$ 群自同构，$L^2=1$、$\det L=1$，
且与标量 $[\omega]^{\times3}$ 交换。
$\det L=1$ 也说明它没有给一个额外的最高投影反号，
不能由 (B15) 再推出原类为零。

### B.6. 最小 genus-four 来源的两个固定分支点

若 (B11) 的像不生成 $E_0^3$，它的最高投影由 R839 消失。
否则令 $D$ 为像的正规化；附录 A 已给 $g(D)\ge4$。
假定 $g(D)=4$。在 $D$ 上，(B15)诱导相互交换的
$v$、$s$，分别为阶3、阶2，并共同固定
$\vartheta(\infty)$。阶数不能降低：否则像逐点落在
$[\omega]-1$ 或 $L-1$ 的真固定子群中，不能生成 $E_0^3$。

由 (A12)–(A13)，$D/\langle v\rangle\simeq\mathbf P^1$，
六个分支点的 monodromy 全部为 $v$。
$s$ 在此 $\mathbf P^1$ 上诱导非平凡对合 $\bar s$；
若 $\bar s$ 平凡，$s$ 将属于三阶 deck 群，与其阶2矛盾。
$\vartheta(\infty)$ 是 $v$ 固定点，故其像是一个
由 $\bar s$ 固定的分支点。

$\mathbf P^1$ 上的非平凡对合有两个固定点。
六点分支集由它保持，非固定点成对出现，
故固定分支点数为偶数。它已至少为1，因而准确为2。
在固定有限扩域上令这两点为 $0,\infty$，
其余四点写作 $\{\alpha,-\alpha,\beta,-\beta\}$，
则
$$
\bar s(x)=-x,\qquad
\alpha\beta(\alpha^2-\beta^2)\ne0.
\tag{B16}
$$
结合全部相同的 monodromy，并吸收固定的非零 cube 常数，
实际 $D$ 因而有模型
$$
\boxed{
D:\quad y^3=x(x^4+A x^2+B),\qquad
B\ne0,\quad A^2-4B\ne0,
}
\tag{B17}
$$
$$
v(x,y)=(x,\omega y),\qquad
s(x,y)=(-x,-y).
\tag{B18}
$$
无穷远的分支指数为 $-5\equiv1\bmod3$，与另外五点同号。
在这个模型上，$x\mapsto-x$ 的三个与 $v$ 交换的 lift
依次为 $y\mapsto-\omega^i y$；只有 $i=0$ 的阶为2，
故 (B18) 没有未定的 cubic 相位。

### B.7. 原二阶商的准确 genus-two 模型

(B17) 的全纯微分仍可取
$$
\frac{dx}{y^2},\quad\frac{x\,dx}{y^2},\quad
\frac{x^2\,dx}{y^2},\quad\frac{dx}{y}.
$$
$s^*$ 的特征依次为 $-1,+1,-1,+1$，
所以 $D/\langle s\rangle$ 的亏格为2。
准确的不变量为
$$
z=\frac yx,\qquad
w=x^2-\frac B{x^2}=2x^2-z^3+A.
$$
它们满足
$$
\boxed{
H=D/\langle s\rangle:\quad
w^2=z^6-2Az^3+(A^2-4B).
}
\tag{B19}
$$
并且 $x^2=(z^3-A+w)/2$，故得到的函数子域指数确为2，
不是只构造了一条到某个 genus-two 曲线的非最小映射。
(B17) 的两个不等式使 (B19) 右侧无重根。

由 (A16)，$J(D)\sim E_0^4$；
$J(H)$ 是其由实际 degree2 商给出的二维同源因子，
因而在一个先于 $p$ 固定的有限扩域上
$$
\boxed{J(H)\sim E_0^2.}
\tag{B20}
$$
一般参数 $A,B$ 不满足 (B20)。
(B17)–(B20)只是原实际 Hom 表达在最低亏格时的必要限制，
没有辨认其具体 CM order、原17处 Artin 角色或 R814 类。

所有操作都从原共同目标的 $Z_{02}$ 出发。
(B10) 的 $1/2$、A.1 的 $1/3$ 及清分母系数均明确留在
有限组合中；正文 (21)–(23) 的 $6^{-2}$、$D_X,D_C$、
原 $X_1$ 的 $12^{-2}$ 一律不变。
本附录不证明 $Z$ 或其 AJ 非零，也没有执行数值计算。
