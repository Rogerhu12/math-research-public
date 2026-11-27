# R1049. 原固定54图在惰性目标素数处的 finite-polynomial 公式与新增除子的晶体整格

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明的范围。** 本篇把 R1011 的同一个、未 depletion 的固定最高循环放到目标素数 $p$ 本身惰性的情形。给出保全部54图、全部 $\eta_j$ 权及完整 corestriction 的 proper finite-polynomial AJ 公式，准确保留因子 $p/(p+1)$。另由原完整 NS 格证明：新增最短截面的两个 CM 分量在原晶体格中的指数分别为 $1,p$；全纯分量的晶体 Chern 类是原二形式的一个 $p$-adic 单位倍。

这两个结论尚不把特征 $p$ 的新增截面或其 Manin 函数认作固定特征零循环的调节子。最后一节明确两者之间仍要计算的原函数限制；本文不据一个非零二形式给加权 AJ 非零。

## 1. 固定循环、系数与有限删集

始终取
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
A=E_{27}:y^2+y=x^3,\qquad E=\mathbf Q(\zeta_9).
\tag{1}
$$
曲面与原微分为
$$
B:v^3=t(1-27t),\qquad
S:y^2+xy+ty=x^3,\qquad
\Omega_S=\frac{dt}{v^2}\wedge\frac{dx}{2y+x+t}.
\tag{2}
$$
$S$ 总指 R991、R1014 的实际光滑射影相对极小模型；无穷处的好模型及二形式的一阶零均保留。

完全沿 R1011(2)–(5) 固定
$$
\ell_9=((1+\omega)u_9,(\omega-1)u_9),\qquad
C_i=C_{2,t}+C_{17,s},\qquad i=(t,s),\quad 3\cdot18=54.
$$
商及实际模问题同源记作
$$
q_i:A\longrightarrow A/C_i,\qquad
\varphi_i:A\longrightarrow S_{b_i}.
$$
两者次数都是34；$\varphi_i$ 包括同一 full9 到原 $\Gamma$ 模型的运输。令
$$
\begin{split}
\Delta_i&=\Gamma_{\varphi_i}
 -34(S_{b_i}\times O_A)-(O_{b_i}\times A),\\
Z_{j,0,L}&=\sum_i c_i\Delta_i,\qquad
Y_{j,0}=P_-e_{\eta_j}\operatorname{Cor}_{L/H}Z_{j,0,L}.
\end{split}
\tag{3}
$$
$c_i=c_{2,t}c_{17,s}$、$P_-$、$e_{\eta_j}=18^{-1}\sum_\sigma
\eta_j(\sigma)^{-1}\sigma$、$L/H/K$ 全是 R1006/R1011 已固定的数据。Galois 作用于几何而固定系数 $E$。重复图仍按原重数保留。

取目标素数 $p\equiv2\bmod3$，排除 $2,3,17$、原有限模型与图表达的坏素数以及下列一个固定有限集合。将 $S$ 的特征零 Hodge 格及原旧 NS 格扩散后，可以删去有限多个素数，使：

* 所用 de Rham 整格、Hodge 分次与杯积对偶自由且与约化相容；
* 晶体—de Rham 比较为整比较，杯积为完美配对；
* $\Omega_S$ 生成原秩二部分的全纯整线。

这是对固定光滑射影模型的有限生成模及固定杯积行列式作局部化；并未要求随 $p$ 选择新的特征零曲面。涉及新增 NS 格时，再取 $p>q_0$，其中 $q_0$ 是 R1014§8 已支付的充分大界。

选定 $\omega$ 的原 $p$-adic 嵌入，记
$$
K_p=\mathbf Q_{p^2},\qquad W=\mathcal O_{K_p}.
$$
必要的系数扩张只在同一已固定 $E$ 的素位进行。以下的晶体 $F$ 是**未 Tate 扭曲的** $p^2$-Frobenius $\varphi^2$；不要将它与作用在几何点上的算术 Frobenius 混同。

## 2. 原图的局部定义域与准确 Frobenius

### 2.1 全部图确实可在 $K_p$ 上比较

对 $A$ 的原 CM 角色 $\psi_{27}$，惰性时
$$
\psi_{27}((p))=-p.
\tag{4}
$$
这是原 $A$ 的好约化 Frobenius 平方，不以别条三次扭曲曲线的 primary 生成元代替。CM 主定理因此给算术 $\operatorname{Frob}_{(p)}$ 在 $A[N]$ 上为 $[-p]$，对所有 $N\mid306$ 同时成立。

这个标量固定每个 $C_i$，所以固定商映射 $q_i$。在完整9基上，它乘以 $s=-p$。因为 $s\equiv1\bmod3$，矩阵 $sI$ 属于 R1006 的完整 $G_\Gamma$：
其 $b=c=0$，$a=d=1\bmod3$，行列式为 $s^2$，也保留原 $K$ 分量。9级 Weil pairing 的变化正是 $s^2$，已经包含在该完整 GL 模问题中，不另施一个 $h$ 或复共轭。

因此忘到原 fine $\Gamma$ 族后，同一个商及同一个同源被固定。原级结构的刚性排除额外的模型自同构。这个证明也逐个适用于全部几何 Galois 共轭：$[-p]$ 是中心标量。故(3)中的全部实际图，在所选惰性局部完成上定义于 $K_p$；不必把 $F=\varphi^2$ 非法地当作在任意更大常数域上仍自然的线性 Frobenius。

原有限角色也满足
$$
\eta_j((p))=1.
\tag{5}
$$
可直接用 R806/R1019 的全主理想公式核对：选 primary 生成元 $-p\equiv1\bmod3$；它在2处是标量1，在17处属于 $\mathbf F_{17}^{\times}$ 的标量子群，两个原有限商角色均取1。这里保的是全角色，不是单个普通位的旧值。

### 2.2 原最高实现与 Bloch–Kato 局部条件

R991 的原 $H^2_{\rm tr}(S)$ 对应 $\theta(\psi_{27}^2)$。在惰性 $p$，其 Hecke 多项式为 $X^2-p^2$。源曲线 $A$ 的多项式为 $X^2+p$。所以
$$
F|H^2_{\rm tr}(S)=p^2,\qquad
F|H^1(A)=-p,\qquad
F|H^2_{\rm tr}(S)\otimes H^1(A)=-p^3.
\tag{6}
$$
最高 projector 与(5)的 Artin 扭曲均保持这个等式。对原
$$
V_{j,p}=\eta_j^{-1}\chi_{27,p}^{\,3}\varepsilon_p^{-1}
\subset H^3(S\times A)(2)
\tag{7}
$$
的对应晶体模，归一化算子准确为
$$
\Phi=\varphi^2=-p^{-1}.
\tag{8}
$$
式(7)采用 R1006/R1009 的算术 Tate-module 角色约定；式(8)是晶体算子，不能直接写成惯性处某个未经定义的算术 Frobenius 值。

$V_{j,p}$ 的两个标记 Tate 指数为 $(2,-1)$。相应 de Rham 过滤在两个 $K_p$ 嵌入中的次数为 $(-2,1)$；商 $D_{\rm dR}/\operatorname{Fil}^0$ 在系数域上为一维。因为(8)排除 $\varphi=1$，Bloch–Kato 的基本正合列给
$$
\exp_{\rm BK}:D_{\rm dR}(V_{j,p})/\operatorname{Fil}^0
 \xrightarrow{\ \sim\ }H^1_f(K_p,V_{j,p}).
\tag{9}
$$
原光滑整模型上的图循环给 crystalline AJ 类，故其局部值确实在这个 $H^1_f$ 中。最高测试线是 $V_{j,p}^{*}(1)$ 的原全纯线，按 $P_-^t=P_+$ 用 $\Omega_S\omega_A$ 测试；并不把一个 $G_{K_p}$ 上的 CM 单线误称为自身 Tate 对偶。

(9)只说明**这一个**局部调节子非零等价于其原标量非零。它没有把此标量等同于某条秩二椭圆曲线的中央首导数。

## 3. Proper finite-polynomial lift 与 Čech 原函数

这里使用 Besser 的 good-reduction proper finite-polynomial 上同调。其 proper 正合列为
$$
0\longrightarrow H^{r-1}_{\rm dR}/\operatorname{Fil}^n
 \xrightarrow{\boldsymbol i}H^r_{\rm fp}(\mathcal X,n)
 \longrightarrow\operatorname{Fil}^nH^r_{\rm dR}
 \longrightarrow0.
\tag{10}
$$
在固定多项式 $P$ 的 mapping-fibre 表示中，$\boldsymbol i$ 是 $P(F)$，不是裸的闭形式识别；这一归一见 Besser 2016(2.7)。本篇用其 proper 版本，不把 BLZ§3 的 affine 假设直接套到整个 $S\times A$。

取
$$
P_S(T)=1-\frac{T}{p^2},\qquad
P_A(T)=1+\frac{T}{p}.
\tag{11}
$$
(6)给 $P_S(F)[\Omega_S]=0$ 与 $P_A(F)[\omega_A]=0$。在原光滑模型的 functorial Čech–rigid/de Rham mapping fibre 中选 lift
$$
\widetilde\Omega_S=(\Omega_S,\Xi_p),\qquad
d\Xi_p=(1-p^{-2}F)\Omega_S.
\tag{12}
$$
$\Xi_p$ 是总次数1的 Čech cochain：包括各仿射块的1形式、交叠函数及 Frobenius 比较同伦。式(12)不主张 $S$ 有一个全局 Frobenius lift，也不将这些交叠项删成某一仿射模型上的单一有理1形式。

对一个原光滑纤维 $S_b$，记
$$
\xi_{b,p}\in H^1_{\rm dR}(S_b/K_p)
\tag{13}
$$
为(12)的**实际导出限制**的闭 cochain 类。由于 $\Omega_S|_{S_b}=0$，这个限制是闭的。若改用局部 Frobenius lift，限制中同时使用新的比较同伦；(13)是对应 proper finite-polynomial 类的原 restriction 数据，不能只把一个不相容的局部 $F$ 代入。

这里无未定的纤维常数。原 $\pi:S\to B$ 诱导
$$
H^1_{\rm dR}(B)\xrightarrow{\sim}H^1_{\rm dR}(S).
\tag{14}
$$
可由原 $q(S)=g(B)=1$、零截面与 Hodge 分解直接得到；沿固定好模型扩散后仍成立。两种(12)的差是一个来自 $H^1_{\rm dR}(S)$ 的闭类，而(14)在常值纤维上的限制为零。因此(13)与 lift 的选择无关；exact cochain 与 Frobenius 同伦的替换也只改其代表。

每个 $S_b$ 与 $A$ 是次数34的好同源，故 $F=-p$ 在其 $H^1_{\rm dR}$ 上。由(10)及归一 $\boldsymbol i=P_S(F)$，真正的限制为
$$
\boldsymbol i^{-1}(\widetilde\Omega_S|_{S_b})
 =\left(1+\frac1p\right)^{-1}\xi_{b,p}
 =\frac{p}{p+1}\xi_{b,p}
 \quad\bmod\operatorname{Fil}^1.
\tag{15}
$$
这一步已解释所需 $p$ 因子；$p+1$ 是单位，$p/(p+1)$ 本身不是单位。

严格说，此处有限多项式次数的 Hodge 参数是 $n=2$，而 $\operatorname{Fil}^2H^1_{\rm dR}(S_b)=0$；所以(15)的等式实际在整个 $H^1_{\rm dR}$ 中成立。写模 $\operatorname{Fil}^1$ 仅表示随后与全纯 $\omega_A$ 杯积时所需的商，不改变归一。

取 $\omega_A$ 的 proper finite-polynomial lift $\widetilde\omega_A$，并用 $O_A^*\widetilde\omega_A=0$ 固定其唯一常数。它可由
$$
\widetilde\omega_A=(\omega_A,G_p),\qquad
dG_p=(1+p^{-1}F)\omega_A
$$
在同一总复形表示。

## 4. 原图的公式及完整54项

### 4.1 单图，保源/靶方向

记 $\langle u,v\rangle_C=\operatorname{tr}_C(u\cup v)$ 为 proper de Rham 杯积，按书写的次序取符号。原 $\varphi_i$ 的方向是 $A\to S_{b_i}$。由(15)、杯积相容与 Besser 的 proper AJ 公式，
$$
\boxed{
\operatorname{AJ}_p(\Delta_i)(\Omega_S\omega_A)
 =\frac{p}{p+1}
  \left\langle\varphi_i^*\xi_{b_i,p},\omega_A\right\rangle_A.
}
\tag{16}
$$
等价地，投影公式把分子写成
$\langle\xi_{b_i,p},\widehat\varphi_i^{\,*}\omega_A\rangle_{S_{b_i}}$。
因此 degree34 及真实微分 multiplier 留在实际 pullback 中；没有把 $\varphi_i$ 错当成反向同源，也没有省去一个34因子。

两项 Chow 修正的贡献确为零。对 $S_{b_i}\times O_A$，采用上面已固定的 $O_A^*\widetilde\omega_A=0$。对 $O_{b_i}\times A$，$\widetilde\Omega_S$ 向点的 degree2 proper finite-polynomial 限制为零。原系数34保留在修正图定义中；并非先丢修正项才算图。

### 4.2 用完整卷积独立核归一和符号

卷积多项式是
$$
R(T)=P_S*P_A(T)=1+\frac{T}{p^3},
$$
且有精确恒等式
$$
R(T_1T_2)=-\frac{T_2}{p}P_S(T_1)+P_A(T_2).
\tag{17}
$$
在 degree2 与 degree1的杯积中，这给未归一 cochain
$$
-\frac1p\,\Xi_p\wedge F\omega_A+\Omega_S\wedge G_p.
\tag{18}
$$
直接取微分即为 $(1+p^{-3}F)(\Omega_S\wedge\omega_A)$，故(18)的正负号已在总复形中固定。限制到图，第二项为零；第一项因 $F[\omega_A]=-p[\omega_A]$，其 proper degree2 类恰为
$\varphi_i^*\xi_{b_i,p}\wedge\omega_A$。源曲线的 $H^2$ 上 $F=p^2$，所以 trace 前仍须除以
$$
R(p^2)=1+\frac1p.
$$
这重新给出(16)，不能以未归一杯积分子冒充 AJ。

若改用 BLZ 的 Tate 归一变量，则原 $H^3(2)$ 上的测试多项式为
$$
P(T)=1+pT,\quad
P(1)=p+1,\quad P(p^{-2})=\frac{p+1}{p}.
\tag{19}
$$
两值均非零，恰与(15)–(18)一致。

### 4.3 原有限角色、corestriction 与最高转置

取 $\sigma\in\operatorname{Gal}(H/K)$ 的任意提升，$\gamma$ 遍历
$\operatorname{Gal}(L/H)$；把 $\sigma\gamma\varphi_i$ 的靶点记成
$\sigma\gamma b_i$。定义**同一个原有限和**
$$
\mathcal I_{j,p}
=\frac1{18}\sum_\sigma\eta_j(\sigma)^{-1}
 \sum_\gamma\sum_{i=1}^{54}c_i
 \left\langle
   (\sigma\gamma\varphi_i)^*\xi_{\sigma\gamma b_i,p},
   \omega_A
 \right\rangle_A .
\tag{20}
$$
每一项都是(13)的实际 restriction。$c_i$ 不随几何 $\sigma$ 共轭；所有 full9 标号及重数按(3)保留。改换提升只是完整 $\gamma$ 和的重标记。

因为 $P_-^t=P_+$ 且 $P_+(\Omega_S\omega_A)=\Omega_S\omega_A$，移去测试侧已经作用为恒等的 projector 后，准确得到
$$
\boxed{
\operatorname{AJ}_{p}(Y_{j,0})(\Omega_S\omega_A)
 =\frac{p}{p+1}\mathcal I_{j,p}.
}
\tag{21}
$$
它先按 $H$ 上的原 $\eta_j$ 投影写。若下降为(7)并选择原 Artin de Rham 基，再乘 R1006(57)的同一个非零基变换因子 $a_{j,p}^{-1}$。这不是一个新本原周期，也不影响(21)中的 $p/(p+1)$。

本文没有以原 R826 的 diagonal cycle 代换(3)；R829 已证明那份旧来源为零。式(21)从实际原54图逐项导出。

## 5. 新增最短截面的完整晶体指数

本节取 $p>q_0$，仍用同一个 $S$。R1014 已给
$$
\det\operatorname{NS}(S_{\mathbf F_{p^2}})=-p^2,\qquad
MW_{\rm free}=(p/3)A_2.
\tag{22}
$$
取原规范的反算术 Frobenius 最短整生成元 $Q_p$。其 torsion 校正及倒6约定沿 R1027；以下用 Shioda 校正类 $D(Q_p)$，校正仅含旧垂直类与零截面，分母整除2、3的幂，在当前 $p$ 均为单位。

旧 rank12 NS 格由零截面、纤维、两奇异纤维分量和原3挠的饱和给出；其判别式为 $-3$。故其晶体像 $\mathcal M_0$ 在 $W$ 上为幺模直接加项。记
$$
\mathcal T=\mathcal M_0^\perp
 \subset H^2_{\rm cris}(S_{\mathbf F_{p^2}}/W).
\tag{23}
$$
$\mathcal T$ 是杯积完美的 rank2 整格。由 Chern 类与交数相容，原新增 Shioda 格的像 $\mathcal N\subset\mathcal T$ 的 Gram 矩阵为
$$
-\frac p3
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}
\quad\text{在 }D(Q_p),D(\tau Q_p)\text{ 上}.
\tag{24}
$$
它的行列式为 $p^2/3$。因此
$$
\operatorname{length}_W(\mathcal T/\mathcal N)=1.
\tag{25}
$$
这里没有使用晶体 Tate 猜想：原已证明的整 NS 格、Chern 杯积与非零行列式已给注入及这个精确指数。

甲板变换取原
$$
\tau(t,v,x,y)=(t,\omega v,x,y),\qquad \tau^*\Omega_S=\omega\Omega_S.
$$
在新增格及原 rank2 晶体格上均有 $\tau^2+\tau+1=0$。以 $W$ 中已选的 $\omega$ 作标量，令
$$
e_\omega=\frac{1+\omega^2\tau^*+\omega(\tau^*)^2}{3},\qquad
e_{\omega^2}=\frac{1+\omega\tau^*+\omega^2(\tau^*)^2}{3}.
\tag{26}
$$
这些分母是 $p$ 单位，并给
$\mathcal T=\mathcal T_\omega\oplus\mathcal T_{\omega^2}$、各 rank1。
$e_\omega$ 是原全纯测试分量；本篇不把算术的 $P_-$ AJ 线与这条转置测试线交换。

把(23)经整晶体—de Rham 比较后，原 Hodge 数为 $(1,0,1)$，所以
$$
\operatorname{Fil}^1\mathcal T/p
 =\operatorname{Fil}^2\mathcal T/p
 =\mathbf F_{p^2}\,\overline{\Omega_S}
 =\mathcal T_\omega/p.
\tag{27}
$$
任意特征 $p$ 线丛的晶体 Chern 类模 $p$ 是其 de Rham Chern 类。用 transition functions 写 $d\log g_{ab}$，便见它属于
$\operatorname{Fil}^1H^2_{\rm dR}$。因此
$$
\mathcal N\bmod p\subset\mathcal T_\omega/p.
\tag{28}
$$
(25)说明该像是一维且非零。于是其两个 CM 加项的指数没有选择余地：
$$
\boxed{
\mathcal N_\omega=\mathcal T_\omega,\qquad
\mathcal N_{\omega^2}=p\mathcal T_{\omega^2}.
}
\tag{29}
$$
特别，不能仅由(24)中两个高度皆含 $p$ 就说两个晶体方向都多一个 $p$；那会与总指数(25)矛盾。

令
$$
D_p^+=e_\omega D(Q_p),\qquad
D_p^-=e_{\omega^2}D(Q_p).
$$
由于 $D(Q_p)=D_p^++D_p^-$，同号 eigenspace 的杯积为零，(24)给
$$
c_1(D_p^+)\cup c_1(D_p^-)=-p/3.
\tag{30}
$$
$\Omega_S$ 是 $\mathcal T_\omega$ 的原本原整生成元。选
$\Omega_S^-\in\mathcal T_{\omega^2}$ 使
$\Omega_S\cup\Omega_S^-=1$。则(29)–(30)给**准确整式**
$$
\boxed{
c_1^{\rm cris}(D_p^+)=u_p\Omega_S,\qquad
c_1^{\rm cris}(D_p^-)
 =-\frac{p}{3u_p}\Omega_S^-,
\qquad u_p\in W^\times.
}
\tag{31}
$$
这个 $u_p$ 的单位性来自原全 NS 饱和与 Hodge 约化，不是将特征零非零自动当作模 $p$ 非零。取反 $Q_p$ 会同时取反 $u_p$，不改任何分母或投影。

(26)、(31)是在选定 CM 系数/基域嵌入下的 $W$-线性陈述。$D_p^+$ 是特殊纤维上的带系数除子；不能由其某个 de Rham 分量落在 $\operatorname{Fil}^2$，声称一个特征零整除子已经提升。另一 CM 分量及半线性 Frobenius 都仍存在。

### 5.1 同一实际线丛的非零 $W_2$ 提升障碍

(31)还给一个明确的一阶结果。这里 $W_2=W/p^2$。令
$\operatorname{ob}_2(\mathcal D)\in H^2(S_{\mathbf F_{p^2}},\mathcal O)$
是将实际特殊纤维线丛 $\mathcal D$ 提升到原模型模 $p^2$ 的障碍。

为固定符号，在一个仿射覆盖上写 transition functions $g_{ab}$，
选单位提升 $\widetilde g_{ab}$，并记
$$
\widetilde g_{ab}\widetilde g_{bc}\widetilde g_{ca}
 =1+p h_{abc}\pmod {p^2}.
$$
定义 $\operatorname{ob}_2(\mathcal D)=[h_{abc}]$。改变单位提升只加
Čech coboundary，且障碍为零恰等价于可以修正这些提升使它们成为
$W_2$ 上的线丛 cocycle。

在同一覆盖的晶体—de Rham 总复形中，Chern 类由
$$
\left(d\log\widetilde g_{ab},
 -\log(\widetilde g_{ab}\widetilde g_{bc}\widetilde g_{ca})\right)
$$
表示。总微分为零，因为第一项的 Čech 微分是三重积的 $d\log$，
而第二项的 de Rham 微分正好抵消它；三重积的下一 Čech 微分为1。
$p>2$ 时模 $p^2$ 的 PD logarithm 就是 $p h_{abc}$。故其向
$H^2(\mathcal O)$ 的 Hodge 商投影满足
$$
\operatorname{pr}_{0,2}c_1^{\rm cris}(\mathcal D)
 =-p\,\operatorname{ob}_2(\mathcal D)\pmod {p^2}.
\tag{31a}
$$
这也说明这里用的是实际线丛的一阶 cocycle 障碍，不是仅凭某个
特征零 period 非零推断不能提升。

所有 Shioda 旧修正类已经在原模型上提升，故在(31a)的右侧为零。
如需清除垂直修正的分母，先乘一个2、3幂即可；该数在 $p$ 处为
单位，再除回不会改零/非零。以 $\Omega_S^-$ 在 $H^2(\mathcal O)$
的原像作为单位生成元，(31)于是给
$$
\boxed{
\operatorname{ob}_2(Q_p)
 =\frac{1}{3\overline u_p}\,\overline{\Omega_S^-}\ne0,\qquad
\operatorname{ob}_2(aQ_p+b\tau Q_p)
 =\frac{\overline a+\omega^2\overline b}
        {3\overline u_p}\,\overline{\Omega_S^-}.
}
\tag{31b}
$$
此处 $a,b$ 是整自由坐标，横线取模 $p$；若以 $[Q_p]-[O]$
代替 Shioda 类，障碍相同。因为 $p$ 惰性，$1,\omega^2$ 在
$\mathbf F_p$ 上线性无关。因此原新增整自由格的
$\operatorname{ob}_2$ 给一个 $\mathbf F_p$-线性同构
$$
MW_{\rm free}/pMW_{\rm free}
 \xrightarrow{\sim} H^2(S_{\mathbf F_{p^2}},\mathcal O)
 \quad\text{（右侧按 }\mathbf F_p\text{ 向量空间看）}.
\tag{31c}
$$
等价地，实际整 NS 类在去掉原旧类及 torsion 后，能提升到
$W_2$ 当且仅当其两个新增 MW 自由坐标都被 $p$ 整除。

(31c)不与带 $W$ 系数的 $D_p^+$ 的(31)混淆：前者的坐标在
$\mathbf Z$ 或 $\mathbf Z_p$，后者允许 $\omega\in W$ 的系数。
将系数先扩到 $W$ 会使(31c)出现一条核线，恰是(26)的全纯分量；
这不产生一个新的整特征零截面。

## 6. 与原 Manin 函数和通常全 Sha 入口的准确连接

R1043§20 已对同一 $Q_p$ 证明
$$
D_B\mu(Q_p)=c_{Q_p}A_p,\qquad c_{Q_p}\ne0,
$$
以及两 cusp、canonical fiber 和有限 supersingular 点的准确接触阶。本篇(31)进一步支付了其新增除子在**原晶体整格**里的本原 CM 位置。但是，$\mu(Q_p)$ 是特征 $p$ 函数；$\Xi_p$ 是固定特征零 $\Omega_S$ 的含 Frobenius 同伦的 primitive。它们尚未被本文识别。

可以将 $u_p\widetilde\Omega_S$ 称为 $c_1^{\rm cris}(D_p^+)$ 的一个 finite-polynomial lift；这只是一种精确的上同调 lift。其图限制满足
$$
\boldsymbol i^{-1}\!\left(
 u_p\widetilde\Omega_S|_{S_b}\right)
 =u_p\frac p{p+1}\xi_{b,p}
 \quad\bmod\operatorname{Fil}^1.
\tag{32}
$$
要从新增截面消费原固定循环，真正需要计算的是(32)的限制，并以(20)的全部 $\eta_j$/Cor 权求和。不能把特殊纤维点 $Q_p(b)$、其非零 Manin 值、或 $u_p$ 的单位性直接代入(21)赋非零。

局部 $H_f^1$ 已由(9)定位；signed 或通常 Selmer 的全球消费另有固定来源要求。R1038§12.2(62)–(67)、R970§6、R973§6 的通常全群桥，要求其**实际**中央首导数 $J_p'(0)\ne0$，才得到秩2时通常全 $\Sha[p^\infty]$ 有限。那些定理没有声称任意新 syntomic 标量非零都等于该 $J_p'(0)$。本篇保留这项全球连接，不把 $H^3(2)$ 的一维局部目标当成已经完成的秩二结论。

## 7. 原始来源与逐项适用范围

1. A. Besser, *A generalization of Coleman's p-adic integration theory*, Invent. Math.142(2000),397–434，Theorem1.2、Proposition2.5、Remark4.3。作者原稿入口：
   <https://www.math.bgu.ac.il/~bessera/padic/coleman.html>。
   此处使用的是 proper good-reduction AJ 与 finite-polynomial 杯积。
2. A. Besser, *On the regulator formulas of Bertolini, Darmon and Rotger*, Research in the Mathematical Sciences3(2016),26，(2.1)、(2.5)–(2.7)、Proposition2.2及Definition2.3：
   <https://link.springer.com/article/10.1186/s40687-016-0073-x>。
   (2.7)的 $P(F)$ 归一正是(15)、(18)中不能省掉的因子。
3. H. Darmon–V. Rotger, *Diagonal cycles and Euler systems I*, Ann. Sci. ENS47(2014),779–832，§3.3(76)–(79)逐字给出前述 proper AJ 公式：
   <https://www.math.mcgill.ca/darmon/pub/Articles/Research/62.DR-Diagonal1/paper.pdf>。
   本篇只用这段 general proper formalism，不使用其 ordinary diagonal 插值定理，更不更换(3)的来源。
4. A. Besser–D. Loeffler–S. L. Zerbes, *Finite polynomial cohomology for general varieties*, Ann. Math. Québec40(2016),203–220，§1.2–1.4、Proposition2.17、Theorem3.2、Proposition3.3：
   <https://arxiv.org/pdf/1405.7527>；
   <https://link.springer.com/article/10.1007/s40316-015-0041-7>。
   (19)与其 Tate 归一约定吻合；proper 论证本身已由前3项支付。
5. D. Ulmer, *A construction of local points on elliptic curves over modular curves*, Int. Math. Res. Notices1995(1995),349–363，§6 Proposition6、§7 Proposition7：
   <https://dlulmer.github.io/research/papers/1995b.pdf>。
   §6的 crystalline cycle map 是 Shioda 正交校正并保高度杯积；§7保 Hecke 自然性。其 Theorem5 与§8并未给本文 $\Xi_p$ 在原54个 CM 图上的积分值，所以未据该定理省去(32)。
6. 仓库的 R991、R995、R997、R1006、R1009、R1011、R1014、R1027、R1043：分别支付原纯角色、严格对应、原图来源、最高转置/Artin下降、固定非零锚、未depletion固定循环、充分大完整NS格、真实最短截面规范及实际Manin函数。

本文没有新增数学执行或素数扫描。
