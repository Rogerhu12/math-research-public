# 原惰性 p² CM 全范数、旧项抵消及同一 syntomic 整参数

日期：2026-11-27。状态：全式手证；没有新增数学执行。

本篇处理原 R1006/R1011/R1049 的同一个 full9 来源和全部 54 条图。结论是：

* 原 $p^2$ cyclic CM 轨道的**未剔除**图和，乘 $p^{-2}$ 后，准确给 R1049 的 $\mathcal I_{j,p}$；在原下降基中准确给 $h_{j,p}$。
* 对 Andreatta–Iovita 的实际 primitive $G^{[p]}=G-V^2G$，同一个 imprimitive 完整范数为零。两个旧项逐项保留后抵消，不能用其 primitive-character 定理把这份零和换成未剔除和。
* 所有 $p$ 的幂均是固定整数次数同源的真实归一。本文不定义、更不微分一个 $p^{\text{非整数权}}$。

## 1. 原对象、完整级结构与适用素数

取
$$
K=\mathbf Q(\omega),\qquad
\delta=1+2\omega,\qquad
A=E_{27}:y^2+y=x^3,\qquad
\omega_A=\frac{dx}{2y+1}.
\tag{1}
$$
原曲面 $S/B$、三条 $\eta_j$（$j=4,10,16$）、系数域、完整
$P_-$、外部 $e_A^-$ 及下降基都沿 R1049。原模形式是
$$
f_{27}=\theta(\psi_{27}^2),\qquad k=3,\qquad
\epsilon=\chi_K,\qquad f_{\Omega_S}=-\delta h_\Gamma,
\quad h_\Gamma(\tau)=f_{27}(\tau/3).
\tag{2}
$$
最后一个常数已经包含在本篇所选 primitive 中，不另在图和外乘
$-\delta$、$34$ 或一个新周期。

原 full9 有序级为
$$
\ell_9=((1+\omega)u_9,(\omega-1)u_9),
\tag{3}
$$
即 R1006(13)–(14) 的 $Ph$ 和 row/adjugate 规范；原
243 项 $e_{\theta^{-1}}$ 亦保留。令
$\varphi_i:A\longrightarrow E_i=S_{b_i}$ 为原全部 54 条
degree34 图，系数仍为 $c_i$。所有级点沿实际商同源运输。

以下 $p\ge5$ 惰性于 $K$，且排除原固定模型、图、系数与 projector
的有限坏集，特别 $p\nmid 2\cdot3\cdot17$。于是
$$
a_p(f_{27})=0,\qquad \epsilon(p)=-1.
\tag{4}
$$
在必要的有限局部扩域上评价全部同源；完整有限和的下降不依赖对某一
分支的任选标号。

一个商 $\lambda:E\to E'$ 的级结构始终是 $\lambda\ell_9$。
单个 degree $p$ 商可能移动 determinant 分量，故先在 full9 的完整
对应上操作，再取原 $3$ 型和 $K$ 分量。不能把每一中间商都提前认作
原同一个 CM 标记点。

## 2. full9 的真实 diamond 与 Coleman 唯一性

令 $\mathcal H=R^1\pi_*\Omega^\bullet_{S/B}$。对(2)的实际
$\mathcal H$-值模形式取 Coleman primitive
$$
\nabla G=f_{\Omega_S}.
\tag{5}
$$
采用 Andreatta–Iovita §7.1（印刷页 696）的 Frobenius-rigid 规范：
若 $P(F)$ 杀掉原形式的上同调类，要求 $P(F)G$ 在相应严格邻域上解析。
这是一个 $\operatorname{Sym}^{k-2}\mathcal H=\mathcal H$ 的 primitive。
因为 $k-2=1>0$，它没有可任加的全局 horizontal analytic section；
不能只用逐圆盘的局部原函数而漏掉这个条件。

本文出现的有限 Hecke 组合仍满足同一个 Coleman 刚性规范。
其差若连接为零，便是全局 horizontal analytic section，故为零。
这也与原曲面的另一检查一致：R1049(14)给
$H^1_{\rm dR}(S)\simeq H^1_{\rm dR}(B)$，这一类限制到任一原纤维为零。
后者支付原 proper primitive 的选择不影响图读数，不能反过来准许任加
一个纤维 horizontal 常数。

完整级上的标量 diamond 必须实际计算。在 R1006§2 的原
$\pi_3$ 中，$1+3\mathbf Z_3$ 的中心作用平凡，而 $-I$ 对
weight3 作用为 $-1$。因 $p\equiv-1\pmod3$，
$$
pI=(-I)((-p)I),\qquad -p\in1+3\mathbf Z_3,
$$
从而
$$
\langle p\rangle G=-G,\qquad
\langle p^2\rangle G=G.
\tag{6}
$$
标量矩阵的 adjugate 仍是同一个标量矩阵，因此(3)不会把这个符号翻回。
$Ph$、原 243 项投影及原 $2,17$ 处有限作用均与中心交换。
这里的 $\epsilon(p)$ 是完整原表示的 nebentype；不是对某个
CM 邻点临时选择的负号。若在不同经典 level 坐标中把 $V$ 的 level
用 $p^{-1}$ 重标号，必须同时带上相应 diamond；本篇的两步式只用
实际 $\langle p^2\rangle=1$，所以没有隐藏的 level 修正。

## 3. 完整邻点和与非回返的 p² 和

对 degree $p$ 商
$\phi_C:E\to E_C=E/C$，定义作用于 $\mathcal H$ 的归一
$$
\mathsf V_C=\frac{\phi_C^*}{p}.
\tag{7}
$$
这正是 Andreatta–Iovita Appendix A 的
$(\widehat\phi_C^*)^{-1}=\phi_C^*/p$，不是按形式权随意除以 $p$。

先在完整 level 对应上定义
$$
\mathsf B_1G(E,\ell)
=\sum_{\substack{C\subset E[p]\\|C|=p}}
 \frac{\phi_C^*}{p}\,G(E_C,\phi_C\ell).
\tag{8}
$$
和中有 $p+1$ 项，没有除以 $p+1$。
weight $k$ 的完整几何商算子为 $pT_p$：先在标准 newvector 的经典分量核 Tate 式，再与原 prime-to-$p$ 有限算子交换。一个商给
$p^k\epsilon(p)f(q^p)$，其它 $p$ 个给
$\sum_{a\bmod p}f(\zeta_p^a q^{1/p})$；
二者之和为 $p(U+\epsilon(p)p^{k-1}V)f=pT_pf$。
在 full9 上这就是同一个完整 correspondence 的等式，且保(6)。

Kodaira–Spencer 的同源自然性给
$\nabla\mathsf V_C=p\,\mathsf V_C^{\otimes3}\nabla$。
故
$$
\nabla\mathsf B_1G
=p\sum_C\mathsf V_C^{\otimes3}f_{\Omega_S}
=p^{-1}T_pf_{\Omega_S}.
$$
由§2的唯一性，
$$
\mathsf B_1G=\frac{a_p}{p}G=0.
\tag{9}
$$

令 $\mathscr C_2(E)$ 是 $E[p^2]$ 中所有 cyclic order $p^2$
子群。其大小为 $p(p+1)$。对 $D\in\mathscr C_2(E)$ 写
$\lambda_D:E\to E_D$，并定义
$$
\mathsf B_2G(E,\ell)
=\sum_{D\in\mathscr C_2(E)}
 \frac{\lambda_D^*}{p^2}\,G(E_D,\lambda_D\ell).
\tag{10}
$$
每条不回返的两步 $p$-同源路径准确给一个这样的 $D$，其
order $p$ 子群 $D[p]$ 唯一，故没有额外路径重数。

$\mathsf B_1^2$ 的其它路径是 $p+1$ 条回返路径。
每条复合为 $[p]$，归一后在 $\mathcal H$ 上为
$[p]^*/p^2=p^{-1}$，而末端 level 是 $p\ell$。
因此完整 operator 等式为
$$
\mathsf B_1^2
=\mathsf B_2+\frac{p+1}{p}\langle p\rangle.
\tag{11}
$$
结合(6)、(9)，得到
$$
\boxed{\mathsf B_2G=\frac{p+1}{p}G.}
\tag{12}
$$
(11)保留了所有回返路径及其真实 diamond。若漏掉(6)，(12)会得到错误符号。

## 4. canonical 上行 V² 的每条微分费用

在 $p$ 惰性且原 CM conductor 与 $p$ 互素时，$E_D$ 有
conductor 乘 $p^2$ 的 CM，原 $p^2$ canonical 上行核为
$$
H_D=E[p^2]/D=\ker\widehat\lambda_D.
\tag{13}
$$
这正是 Andreatta–Iovita §5.1 及 Proposition 5.9 使用的
$E^{(2)}\to E^{(0)}$；$\widehat\lambda_D:E_D\to E$ 的次数仍是
$p^2$，不是 $p$。

为把源、靶 CM 微分全部写出，选
$\langle\omega_E,\eta_E\rangle=1$，并令
$$
\lambda_D^*\omega_D=\omega_E,\qquad
\langle\omega_D,\eta_D\rangle=1.
$$
同源保持 CM 两线，且杯积乘次数，所以
$$
\lambda_D^*\eta_D=p^2\eta_E,\quad
\widehat\lambda_D^*\omega_E=p^2\omega_D,\quad
\widehat\lambda_D^*\eta_E=\eta_D.
\tag{14}
$$
故在 $E_D$ 的两步旧项是
$$
(V^2G)(E_D)=\frac{\widehat\lambda_D^*}{p^2}
 G(E,[p^2]\ell).
\tag{15}
$$
末端的 actual full9 level 为 $[p^2]\ell$；用(6)才把其值写回
$G(E,\ell)$。对(15)施加同一个下降归一，
$$
\boxed{
\frac{\lambda_D^*}{p^2}(V^2G)(E_D)
=\frac{[p^2]^*}{p^4}G(E)
=p^{-2}G(E).
}
\tag{16}
$$
这里 $[p^2]^*$ 在 $H^1_{\rm dR}$ 上为 $p^2$，不是
在 $H^2$ 上的 $p^4$。式(14)分别核定了两条 CM 微分方向，
所以(16)没有省去原 $\Omega_{p,2}$ 或把某个 target 生成元偷换成
source 生成元。若改用整数环上的本原微分，两个实际缩放须同时带入；
把(14)写回去仍得到(16)。

因此
$$
\sum_D\frac{\lambda_D^*}{p^2}(V^2G)(E_D)
=\frac{p(p+1)}{p^2}G
=\frac{p+1}{p}G.
\tag{17}
$$
Andreatta–Iovita 印刷页 705 的 primitive 剔除式在当前
$k=3,a_p=0,\epsilon(p)=-1$ 准确为
$$
G^{[p]}=G-\frac{a_p}{p}VG+\epsilon(p)p^{k-3}V^2G
       =G-V^2G.
$$
由(12)、(17)，
$$
\boxed{
\sum_D\frac{\lambda_D^*}{p^2}G^{[p]}(E_D)=0.
}
\tag{18}
$$

这里用的是完整 oriented cyclic correspondence 的和。若将它写成
CM 局部范数，原 full9 和原 $2,17$ 标记保持不变；其相对轨道为
$$
\mathcal O_{K,p}^{\times}/
 \bigl(\mathbf Z_p^{\times}(1+p^2\mathcal O_{K,p})\bigr),
$$
阶为 $p(p+1)$。不能再把这份 fine-level 范数除以 CM 的六个单位。
若选择更大的含全部 $p^2$ 挠点的域，则按该完整 torsion 域作
corestriction 会另有 stabilizer 重数；本篇(10)、(18)始终使用
cyclic subgroup 轨道的有限 étale trace。

原 $\eta_j$ 在这条新的 $p$-局部相对轨道上不分歧且平凡，
故它正是这里的 imprimitive 情形。A–I Proposition 5.9 的
primitive-character 消旧项使用一个非平凡 $p$-角色和为零；
当前不能使用那一步，也没有使用 Theorem 7.1 的 primitive-conductor
结论。公式(18)是把原两个旧项保留后的实际答案。

## 5. 原54项、full9、Artin和最高投影逐项交换

令 $D\subset E_i[p^2]$。因 $\deg\varphi_i=34$ 与 $p$ 互素，
它唯一对应 $A[p^2]$ 中的 cyclic 子群 $D_A$。
有保全部级结构的商方块
$$
\lambda_D\varphi_i=\varphi_{i,D_A}\lambda_{D_A}.
\tag{19}
$$
它是相同的有限平坦商，而非只到一个未定 CM 单位的同构。
在每个角中均用实际拉回相等的微分。故 $p$-correspondence 与原
$2$ 和 $17$ 处的全有限算子交换，不删其任何 torus 字，也不把
$c_i$ 改为其共轭。

同样，$p$-correspondence 在原 $3$ 处有限向量上为恒等张量因子，
因而与 $Ph$、243项 projector、完整 $P_-$ 和测试侧的
$P_-^t=P_+$ 相容。每条 degree $p$ 分支改变 determinant 分量的
费用仍由§2–4支付，不能在此借“交换”将其忽略。

所有有限 Galois 作用只重标记 $(i,D)$ 及其 full9 标号。
因此原
$$
\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
 \eta_j(\sigma)^{-1}
 \sum_{\gamma\in\operatorname{Gal}(L/H)}
 \sum_{i=1}^{54}c_i
\tag{20}
$$
可逐项施于(12)、(17)、(18)。$c_i$ 始终为原外系数。
这里不添加新的 $1/54$、$1/18$、$[L:H]$ 或一个 p²-level
平均：原有的每项和其重数均由(20)原样保留。

## 6. 未剔除完整范数准确返回原 h

为固定 primitive 与图的配对，若 $\varphi:A\to E$ 有次数 $c$，
取 $\varphi^*\omega_E=\omega_A$ 及单位杯积对偶基，则
$\varphi^*\eta_E=c\eta_A$。将 $G=G_0\omega_E-G_1\eta_E$ 代入：
$$
\langle\varphi^*G,\omega_A\rangle_A=cG_1.
\tag{21}
$$
这正是 A–I Lemma 7.3 在 $r=j=1$ 的图公式；亦可直接由原
R1049 的 Leray/Čech restriction 与杯积得到。它是任意实际同源图的
局部 AJ 自然性，不使用 Theorem 7.1 的 Heegner-character 插值假设。
若在 full9 覆盖上写证明，完整 finite projector 后仍为(21)。

对 $\lambda_D\varphi_i$ 使用未除以 $p^2$ 的
$\lambda_D^*$。故(12)逐项给
$$
\sum_D
 \operatorname{AJ}_p(\Delta_{\lambda_D\varphi_i})
       (\Omega_S\omega_A)
=p^2\left\langle
 \varphi_i^*\mathsf B_2G,\omega_A
 \right\rangle
=p(p+1)\operatorname{AJ}_p(\Delta_{\varphi_i})
       (\Omega_S\omega_A).
\tag{22}
$$
每条修正图在这里仍是
$$
\Delta_{\lambda_D\varphi_i}
=\Gamma_{\lambda_D\varphi_i}
 -34p^2(E_{i,D}\times O_A)-(O_{b_{i,D}}\times A).
\tag{23}
$$
固定 degree0 修正没有被换成旧 degree34 的修正。

令 $\mathcal Z_{j,p^2}$ 表示对(23)作完整 $D$ 和，再作原
54项、$\eta_j$、Cor、最高投影的循环；这是新的 p²-level 图范数。
以下只断言其**实际 AJ 读数**，不从此声称一个未付的 Chow 类等式。
由(20)、(22)，
$$
\boxed{
\operatorname{AJ}_p(\mathcal Z_{j,p^2})(\Omega_S\omega_A)
=p(p+1)\operatorname{AJ}_p(Y_{j,0})(\Omega_S\omega_A).
}
\tag{24}
$$
R1049(21)、(42)在同一个杯积次序和基下已付
$$
\operatorname{AJ}_p(Y_{j,0})(\Omega_S\omega_A)
=\frac p{p+1}\mathcal I_{j,p},\qquad
h_{j,p}=a_{j,p}^{-1}\mathcal I_{j,p}\in\mathcal O.
$$
所以实际旧项回收为
$$
\boxed{
p^{-2}\operatorname{AJ}_p(\mathcal Z_{j,p^2})(\Omega_S\omega_A)
=\mathcal I_{j,p},\qquad
a_{j,p}^{-1}p^{-2}\operatorname{AJ}_p(\mathcal Z_{j,p^2})
=h_{j,p}.
}
\tag{25}
$$
第二式的测试采用原下降基。它没有未定的依赖 $p$ 的比例；
$p/(p+1)$ 与 $(p+1)/p$ 在同一图读数上精确相消。

虽然定义中写了 $p^{-2}$，(25)证明这份**完整和**在原下降整基中为整。
不能据此断言每条 p² 图分别可除以 $p^2$。

## 7. 哪个端点值已经支付，哪个尚未支付

(18)经过(20)及同一图配对后为零；(25)是未剔除和的准确值。
因此在原 imprimitive 角色上，A–I 的被剔除有限和不会直接检测
$h_{j,p}$。具体丢失的项就是(17)，其原归一值准确为 $h_{j,p}$，
不是一个可凭 primitivity 删去的零。

可以仅在固定的两个实际对应之间引入形式系数 $T$：
$$
\mathscr N_j(T)
=\frac1{18}\sum_{\sigma,\gamma,i,D}
 \eta_j(\sigma)^{-1}c_i
 \left\langle
  (\sigma\gamma\varphi_i)^*
  \frac{\lambda_D^*}{p^2}
  (G-T V^2G)(E_{i,D}),\omega_A
 \right\rangle .
$$
全部原标号和外系数沿(20)。由已证式，
$$
\boxed{\mathscr N_j(T)=(1-T)\mathcal I_{j,p}.}
\tag{26}
$$
于是这个固定两项 polynomial 的系数导数为
$-\mathcal I_{j,p}$，下降后为 $-h_{j,p}$。
这只是一个已经完全定义的 finite correspondence 系数导数；
它不被称作某条 p-adic L 函数的权导数。把(26)与实际 analytic weight
family 连接，还必须识别该 family 的算子、CM period 与 character
变量；尤其不能将 $\epsilon(p)p^{k-3}$ 中的 $p^{k-3}$ 当作
$k\in\mathbf Z_p$ 的解析函数。

本篇没有给 $h_{j,p}$ 赋非零，也没有把原 $H^3(2)$ 的局部 AJ
改名为某条 rank2 椭圆曲线的中央首导数。已完成的是同一个原来源的
p² 端点零、完整旧项和以及原整参数的准确回收；后续任何非零或通常全
Sha 消费须使用这个真实回收式。

## 8. 精确来源

* F. Andreatta–A. Iovita, *Katz type p-adic L-functions for primes p non-split
  in the CM field*, Comment. Math. Helv. 99 (2024), 641–716,
  DOI [10.4171/CMH/577](https://doi.org/10.4171/CMH/577)；
  [作者出版全文](https://ems.press/content/serial-article-files/48931)。
  本篇实际使用 §4.2/Corollary4.23（pp680–681）的 full V/diamond，
  §5.1及Proposition5.9（pp682、689–690）的 CM 上行核及旧项，
  §7.1（p696）的 Coleman 唯一性、Lemma7.3（pp698–699）的图公式、
  pp705–706的完整 primitive 剔除，以及AppendixA（pp708–709）的
  $\phi^*/p$ 和连接关系。没有套用其 primitive-character Theorem7.1
  到当前未分歧 p 角色。
* [R1006](../results/R1006-actual-full-nine-trace-and-original-katz-square.md)，
  §§2–5：原 full9、243项、真实3型、54图及外系数规范。
* [R1011](../results/R1011-fixed-undepleted-highest-cycle-and-chow-euler-factors.md)：
  原未剔除 $Y_{j,0}$、修正图及原最高 projector。
* [R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md)，
  (14)、(20)–(21)、(41)–(42)：原 proper primitive 的不歧义、
  完整54/η/Cor读数、$p/(p+1)$及原整参数 $h_{j,p}$。

以上是固定整数同源及全有限和的证明；没有新素数扫描或数值拟合。
