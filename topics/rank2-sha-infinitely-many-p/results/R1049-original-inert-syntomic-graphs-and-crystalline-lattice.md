# R1049. 原固定54图在惰性目标素数处的 finite-polynomial 公式与新增除子的晶体整格

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明的范围。** 本篇把 R1011 的同一个、未 depletion 的固定最高循环放到目标素数 $p$ 本身惰性的情形。给出保全部54图、全部 $\eta_j$ 权及完整 corestriction 的 proper finite-polynomial AJ 公式，准确保留因子 $p/(p+1)$。另由原完整 NS 格证明：新增最短截面的两个 CM 分量在原晶体格中的指数分别为 $1,p$；全纯分量的晶体 Chern 类是原二形式的一个 $p$-adic 单位倍。

§§8–12进一步在同一整扩张格中支付全Chern–Miller/PD比较与真实限制，将原残余参数 $\overline h_{j,p}$ 准确写为全部54图的 $d_i^pX_iP_p(X_i^3)$ 加权和，再识别为原 weight $p$ CM theta form 的同一 toric 值。全权和的非零以及它到通常全 $\Sha$ 的全球比较仍未付；非零二形式本身不替代这两步。

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
(6)给 $P_S(F)[\Omega_S]=0$ 与 $P_A(F)[\omega_A]=0$。在原光滑模型的 functorial Čech–rigid/de Rham mapping fibre 中，明确取 $H^2_{\rm fp}(S,2)$ 的 lift（因为 $\Omega_S\in\operatorname{Fil}^2$）
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

在曲线因子上取 $H^1_{\rm fp}(A,0)$ 的唯一 lift $\widetilde\omega_A$，使用 Besser 2016(2.3)的 $H^1_{\rm fp}(A,0)\simeq H^1_{\rm dR}(A)$。于是两因子的 Hodge 参数为 $2+0=2$，直接进入原 AJ 的测试次数。因 $H^1_{\rm fp}(\operatorname{Spec}W,0)=0$，$O_A^*\widetilde\omega_A=0$ 自动成立；无需另选一个常数。一个 cochain 代表仍可写成
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

两项 Chow 修正的贡献确为零。对 $S_{b_i}\times O_A$，采用上述 $n=0$ lift 的 $O_A^*\widetilde\omega_A=0$。对 $O_{b_i}\times A$，$\widetilde\Omega_S$ 向点的 degree2 proper finite-polynomial 限制为零。原系数34保留在修正图定义中；并非先丢修正项才算图。

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

可以将 $u_p\widetilde\Omega_S$ 称为 $c_1^{\rm cris}(D_p^+)$ 的一个 finite-polynomial lift；这只是一种精确的上同调 lift。这里先在 $H^2_{\rm fp}(S,2)$ 使用(31)已给的全纯 Chern 分量；与通常 twist1 的 Chern 类比较时使用自然的 $H^2_{\rm fp}(S,2)\to H^2_{\rm fp}(S,1)$。不把这条 forget 映射当作特殊纤维除子已经提升。其图限制满足
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

## 8. 原局部扩张的积分正规形及唯一残余参数

以下仍取(1)–(8)的同一个惰性目标素数，另取 $p\ge5$ 并排除固定图、有限系数与投影分母。令 $\mathcal O$ 为原系数域 $E$ 在所选素位的整数环。因 $p\ne3$，$\mathcal O/\mathbf Z_p$ 未分歧，且含有原 $W=\mathbf Z_p[\omega]$。在包含原 Artin 下降基的一个固定有限系数扩张内工作也不改变下述证明；只需继续排除其固定分歧及基变换分母。

本节给出比(21)更精确的整格结论：
**同一个加权读数在原整 BK 格中的唯一参数，以及它模 $p$ 检测的确切扩张。**
没有声称该参数已非零。

### 8.1 原整实现及两个标记嵌入

取原固定几何的 $p$-adic 整上同调、原最高 projector 及 Artin projector 所给的格 $T_{j,p}\subset V_{j,p}$。所有 projector 的固定分母在当前 $p$ 均为单位。原模型的整比较、Hodge 分次自由及完美杯积沿§1的有限删集使用。

为使全部 filtration 次数在 Fontaine–Laffaille 范围内，取
$$
M=D_{\mathrm{FL}}\bigl(T_{j,p}(-2)\bigr).
\tag{33}
$$
这里使用与 $D_{\mathrm{cris}}$ 同向的约定：有理化的 $M$ 是原最高 $H^3$，商 $\mathcal O(-2)$ 的过滤次数为2；不是把(7)的算术角色改成其对偶。若从 Fontaine–Laffaille 原文的反变实现出发，先对实现作对偶就得到这一同向约定。

分裂
$$
W\otimes_{\mathbf Z_p}\mathcal O=\mathcal O\oplus\mathcal O.
$$
以 $1,2$ 标记两个嵌入，使 $M_1$ 的 filtration 次数为3，$M_2$ 的为0。**标记2是(7)的 $D_{\rm dR}/\operatorname{Fil}^0$ 所在的嵌入**；最高测试 $\Omega_S\omega_A$ 在原对偶线上，不能把它当作 $M_1$ 在同一个嵌入中的向量。

晶体 $\varphi$ 在两标记之间交换，且对系数环 $\mathcal O$ 线性。选各自的本原基 $e_1,e_2$。强可除性与(6)给
$$
\begin{split}
M_1&=\mathcal O e_1,\quad \operatorname{Fil}^3M_1=M_1,
   \quad\operatorname{Fil}^4M_1=0,\\
M_2&=\mathcal O e_2,\quad \operatorname{Fil}^0M_2=M_2,
   \quad\operatorname{Fil}^1M_2=0,\\
\varphi e_1&=p^3u e_2,\qquad
\varphi e_2=-u^{-1}e_1,\qquad u\in\mathcal O^\times .
\end{split}
\tag{34}
$$
最后两式相乘恰为 $\varphi^2=-p^3$。若不先分裂两个嵌入，$\varphi$ 对 $W$ 半线性；(34)绝不把它当作在单个 $W$ 分量上随意线性化。式中 $u$ 也不是§5的 $u_p$，两者的定义和所在格不同。

在标记2选择 $e_2$，使其与原积分测试基的配对为1；杯积次序沿(16)。在模型测试 $\Omega_S\omega_A$ 与下降后的测试之间，保留(21)后已固定的 $a_{j,p}^{-1}$。该 Artin 基在删去固定有限素数后为本原整基；没有为不同 $p$ 另选任意本原周期。

Fontaine–Laffaille 适用的范围在这里是 $[0,3]\subset[0,p-2]$。原文§7.14、Proposition7.15及Theorem8.4给精确、全忠实的实现和晶体比较；带系数的表述也可见 Gee–Herzig–Liu–Savitt 2017§2.3，印刷第414页。其 essential image 包含该范围内的每个晶体稳定格，且与模 $p$、子商相容。因此下文是原 Galois 整扩张的分类，不仅是某个有理过滤模的形式计算。

### 8.2 逐式分类原 $H_f^1$ 的整扩张

设 $\mathcal E$ 表示一个属于 $H_f^1(K_p,T_{j,p})$ 的整扩张
$$
0\longrightarrow T_{j,p}\longrightarrow\mathcal E
 \longrightarrow\mathcal O\longrightarrow0.
$$
先扭曲 $(-2)$，再用上述同向 Fontaine–Laffaille 实现。其商有两个标准基 $\bar f_1,\bar f_2$，均在 $\operatorname{Fil}^2$，且
$\varphi\bar f_1=p^2\bar f_2$、
$\varphi\bar f_2=p^2\bar f_1$。过滤严格性使我们可以选取
$\operatorname{Fil}^2$ 中的提升 $f_1,f_2$。

相对于(34)，强可除性准确地给
$$
\varphi f_1=p^2f_2-p^2x e_2,\qquad
\varphi f_2=p^2f_1-p^2y e_1,\qquad x,y\in\mathcal O.
\tag{35}
$$
这里故意按 $1-\varphi/p^2$ 写**负号**，以和下文的 Bloch–Kato 连接映射对齐。不能只用未除 $p^2$ 的 Frobenius 矩阵判定残余扩张。

保持子对象与商标准基的全部 Hodge gauge 只有
$f_1\mapsto f_1+z e_1$，$z\in\mathcal O$；
$f_2$ 不能加 $e_2$，因为 $e_2\notin\operatorname{Fil}^2$。
把这个替换代入(35)得
$$
(x,y)\longmapsto(x-puz,\ y+z).
\tag{36}
$$
于是
$$
\boxed{h(\mathcal E)=x+puy}
\tag{37}
$$
是完整 gauge 不变量。取 $z=-y$ 后，正规形为 $y=0,x=h$。

反过来，对任意 $h\in\mathcal O$，(34)及(35)中 $x=h,y=0$
定义一个强可除模。确实，标记1的目标由
$\varphi_0e_2=-u^{-1}e_1$ 与 $\varphi_2f_2=f_1$ 生成，
标记2由 $\varphi_3e_1=u e_2$ 与
$\varphi_2f_1=f_2-h e_2$ 生成；所以强可除性没有额外限制。
Baer 加法直接相加 $x,y$。因此
$$
H_f^1(K_p,T_{j,p})\ \simeq\ \mathcal O,\qquad
[\mathcal E]\longmapsto h(\mathcal E).
\tag{38}
$$
这里 $H_f^1$ 指整上同调中晶体有理子空间的原像。任一这样的整扩张，其有理化为晶体表示，Hodge 权就是上述子商的并集，所以正好在已经核准的 Fontaine–Laffaille essential image 内。

同一计算可模 $p^n$ 进行，使用全部除 Frobenius $\varphi_i$。全忠实性于是给
$$
\mathcal E/p^n\text{ 分裂}
\quad\Longleftrightarrow\quad
h(\mathcal E)\equiv0\pmod {p^n}.
\tag{39}
$$
特别模 $p$ 的唯一参数是 $x\bmod p$。这是原**局部 Galois 扩张**
的参数，不是将特殊纤维上一点的阶或无权 Picard 类取模 $p$。

### 8.3 Bloch–Kato 对数的准确整格与符号

在有理化后，唯一 Frobenius splitting 写作
$f_i+a_i e_i$。它应满足
$\varphi(f_1+a_1e_1)=p^2(f_2+a_2e_2)$ 及反向等式。
由(34)–(35)逐式得到
$$
a_2=-x+pu a_1,\qquad
a_1=-y-p^{-2}u^{-1}a_2.
$$
消去 $a_1$，即
$$
a_2=-\frac p{p+1}(x+puy)=-\frac p{p+1}h.
\tag{40}
$$

采用标准 Galois cocycle $g\mapsto g\tilde1-\tilde1$，
Bloch–Kato 对数是 Hodge splitting 减去 Frobenius splitting。
这个符号可以直接从
$0\to V\to B_{\rm cris}^{\varphi=1}\otimes V
 \to(B_{\rm dR}/B_{\rm dR}^+)\otimes V\to0$
的连接映射核出：若 $b$ 提升 de Rham 类 $v$，连接 cocycle 是
$gb-b$；扩张中的 Frobenius 不变提升为 $\tilde1-b$，Hodge 提升与它之差正是 $v$。因此在(40)的标记2中对数坐标是 $-a_2$，不是 $a_2$。由原测试基的配对规范，
$$
\boxed{
\log_{\rm BK}[\mathcal E]
 =\frac p{p+1}h(\mathcal E)e_2
 \quad\bmod\operatorname{Fil}^0,
\qquad
\log_{\rm BK}H_f^1(K_p,T_{j,p})
 =p\mathcal O e_2 .
}
\tag{41}
$$
最后等式用 $p+1\in\mathcal O^\times$。它给真实整格上的一个 $p$，
而非在有理一维空间中任意重标度造成的 $p$。

现在把 $\mathcal E$ 取为同一个 $Y_{j,0}$ 的原局部整 AJ 扩张，记
$h_{j,p}=h(\mathcal E_{Y_{j,0}})$。与(20)–(21)逐项比较得到
$$
\boxed{
h_{j,p}=a_{j,p}^{-1}\mathcal I_{j,p}\in\mathcal O,\qquad
\operatorname{AJ}_p(Y_{j,0})(\text{原下降测试})
 =\frac p{p+1}h_{j,p}.
}
\tag{42}
$$
因两个等式均用同一原周期、同一杯积次序和同一 Artin 基，
(42)没有未定的依赖 $p$ 的非零比例。若坚持在 $H$ 上的模型测试基书写，
则等价地 $a_{j,p}h_{j,p}=\mathcal I_{j,p}$。

由(39)及(42)，$a_{j,p}^{-1}\mathcal I_{j,p}\not\equiv0\bmod p$
是一个足以证明原局部 AJ 非零的具体有限精度条件。
反向只能说
$\mathcal I_{j,p}=0$ 等价于整个局部扩张分裂；
模 $p$ 为零本身仍允许更深的非零扩张。

### 8.4 下一原输入确实是一阶 normal function

对原任一图，把特殊纤维的 $D_p^+$ 限制并拉回 $A$，
其无权 degree0 类来自 $A(\mathbf F_{p^2})$。
因 $F_{p^2}=[-p]$，该点群被 $p+1$ 杀。
对每个实际整点，$p+1$ 与 $p$ 互素，故它有唯一同阶的未分歧挠提升；
该提升的 $p$-adic logarithm 为零。
原固定系数线性组合和所有 $\eta_j$/Cor 操作也不改变这个事实。

因此(42)所需的 $h_{j,p}$ 不能由这些单独挠提升的日志取得。
它记录的是(12)的**全局** Čech/Frobenius 数据在原图上的限制，
亦即与实际全局除子不提升相联系的 secondary 项。
(31b)证明全局障碍非零，(39)准确指出残余读数必须检测哪个局部扩张；
但它们没有把全局障碍到原54项加权和的映射宣布为非零。

后继可在同一覆盖中选择 $D_p^+$ 的 transition functions，
用 Frobenius 的线丛同构及对数 cochain 构造(12)，再加入
$c_1(D_p^+)=u_p\Omega_S$ 的 exact 比较项。
由于(14)，只要保完整比较同伦与原图，此计算代表给出的(42)唯一。
目前仍需真正计算该限制；不把特征 $p$ 的空间 Manin 函数
$\mu(Q_p)$ 自动当成这一算术一阶项。

本节来源补充：
Fontaine–Laffaille, *Construction de représentations p-adiques*,
Ann. Sci. ENS15(1982),547–608，§7.14、Proposition7.15、Theorem8.4：
<https://www.numdam.org/item/10.24033/asens.1437.pdf>。
Gee–Herzig–Liu–Savitt,
*Potentially crystalline lifts of certain prescribed types*,
Documenta Math.22(2017),397–422，§2.3，p.414：
<https://www.emis.de/ft/10184>。
所引定理仅支付整实现、精确性及全忠实性；(34)–(42)的扩张分类和全部比例已在本文直接计算。

## 9. 完整 Čech–Miller 公式：把原读数写成唯一的 normal function

本节在同一个曲面、同一特殊纤维新增类及同一54个图上，
把§8的 $h_{j,p}$ 改写成可由 transition functions 计算的式子。
不引入新的图或新的普通投影。新增内容是：给出特殊纤维
Miller 函数的完整 Frobenius null-homotopy，保留 degree0
同伦项，并逐式锁住 normal function 的常数。

### 9.1 一个同时保所有图的 crystalline 复形

可把固定光滑模型 $\mathcal S,\mathcal A$ 分别嵌入射影空间，
用标准仿射覆盖与其交叠上的完备 PD envelope 计算晶体上同调。
对每一个原图，在两射影空间的乘积中使用其实际图嵌入；
到两因子的映射都是投影。坐标的 $p^2$ 次幂定义环境空间的
Frobenius lift。由于§2.1已经证明所有特殊图在
$\mathbf F_{p^2}$ 上，这个 lift 保持其特殊纤维理想，
因而作用在相应 PD envelope 上，且与环境投影严格交换。

这是环境空间的 Frobenius，**不是**声称原特征零曲面或图有
全局 Frobenius lift。由 PD 复形到实际模型 de Rham 复形的
比较同伦仍须保留。以下用 $C_S,C_b$ 表示这一 Čech–de Rham
总复形，$I_b:C_S\to C_b$ 为纤维限制；实际图拉回亦在这个
同一系统中进行。换用其它 embedding system 时，所有公式
沿其 functorial 比较和同伦运输。

总微分约定为
$d_{\rm tot}=\check\delta+(-1)^{\text{Čech degree}}d_{\rm dR}$。
在 PD 理想 $J$ 上使用
$$
\log(1+z)=\sum_{m\ge1}(-1)^{m+1}(m-1)!\,\gamma_m(z),
\qquad z\in J.
$$
这在完备 PD 环中收敛；其微分是 $d\log(1+z)$。
因此下列对数只对模 $J$ 等于1的单位取值，
不对任意有零极的 Miller 函数直接写一个全局对数。

先对一个实际整线丛写公式，再对原 Shioda 校正及
$D_p^+=(1+\omega^2\tau^*+\omega\tau^{2*})D(Q_p)/3$
线性组合。所有分母是 $p$ 单位，$F=\varphi^2$ 固定这些系数。

### 9.2 Chern cocycle 与真实 Frobenius 同伦

设原特殊纤维线丛在所选覆盖上有 transition functions
$g_{ab}^{(0)}$，并选 PD 环中的单位提升 $g_{ab}$。
用 $g_{ba}=g_{ab}^{-1}$，记
$q_{abc}=g_{ab}g_{bc}g_{ca}$。它模 $J$ 为1。
取完整 degree2 cocycle
$$
c=\bigl(0,\ d\log g_{ab},\ -\log q_{abc}\bigr)
\in C_S^2.
\tag{43}
$$
按上述总微分，$\check\delta(d\log g)=d\log q$，
与第三项的微分抵消，所以 $dc=0$。这就是同一
$c_1^{\rm cris}$ 的 Čech 代表，不删三重交叠函数。

因为模 $J$ 的 $F$ 是 $p^2$ 次幂，定义
$$
b_{ab}=-\log\!\left(\frac{F g_{ab}}{g_{ab}^{p^2}}\right),
\qquad b\in C_S^1.
$$
两项逐个计算给
$$
\boxed{(F-p^2)c=db.}
\tag{44}
$$
在(43)的 Čech1微分项，右侧为
$d\log(Fg/g^{p^2})$；在 Čech2函数项，右侧为
$-\check\delta\log(Fg/g^{p^2})$，恰等于左侧。
若用局部 Frobenius 而非上述同一 PD 系统，
$b$ 必须同时包含比较同伦；式(44)仍在总复形中成立。

对 $D_p^+$ 用同一记号 $c,b$。由(31)，存在 degree1 cochain
$a$ 使
$$
c=u_p\Omega_S+da.
\tag{45}
$$
这里 $\Omega_S$ 指其在该复形中的原 Hodge lift，
不是任意替换过的二形式。于是一个准确的(12)代表为
$$
\boxed{
\Xi_p=u_p^{-1}
 \left(\frac{Fa-b}{p^2}-a\right).
}
\tag{46}
$$
直接对(46)取微分并代入(44)–(45)，得到
$d\Xi_p=(1-F/p^2)\Omega_S$。这同时固定了所有 $p^2$ 分母和符号。

### 9.3 原特殊纤维 Miller 函数给完整 null-homotopy

每一个原 $S_b$ 都与 $A$ 经次数34的实际同源相连，
且同源定义于 $\mathbf F_{p^2}$。由源上
$\operatorname{Frob}_{p^2}=[-p]$ 及同源自然性，
靶上亦有此端同态等式。因此
$S_b(\mathbf F_{p^2})$ 被 $N=p+1$ 杀。

原 Shioda 线丛限制在这些好纤维上就是一个 degree0 类；
旧垂直及基类的限制是平凡类。先对每个实际整限制
$\mathcal L_b$ 取一个 $\mathbf F_{p^2}$-有理 Miller 函数，
平凡化 $\mathcal L_b^{\,N}$。它存在于原剩余域上：
对应主除子的函数空间为一维，Galois 下降只用 Hilbert90。
可用原 $O_b$ 的局部首项把比例固定为1；若该类已为零，
直接取平凡化。最后再作同一个 $D_p^+$ 的线性组合。

具体地，这个平凡化给每个覆盖块上的单位 $k_a^{(0)}$，满足
$$
(g_{ab}^{(0)})^N=k_b^{(0)}/k_a^{(0)}.
$$
选择任意单位提升 $k_a$，定义
$$
H_{ab}=\frac1N\log\!\left(g_{ab}^{\,N}\frac{k_a}{k_b}\right),
\qquad
t_b=\left(\frac1N\,d\log k_a,\ -H_{ab}\right)\in C_b^1.
\tag{47}
$$
这里的 $g_{ab}$ 已沿同一 $I_b$ 限制。括号内模 $J$ 为1，
所以全部 PD logarithm 合法。由
$$
dH_{ab}=d\log g_{ab}
       +N^{-1}(d\log k_a-d\log k_b),\qquad
\check\delta H=\log q
$$
逐项得到 $dt_b=I_b c$，包括全部三重交叠项。

再定义实际 degree0 cochain
$$
\ell_a=\frac1N\log\!\left(\frac{Fk_a}{k_a^{p^2}}\right).
$$
代入(47)，在 Čech0的一形式分量得到 $d\ell_a$；
在 Čech1的函数分量得到
$\ell_b-\ell_a$。所以完整等式为
$$
\boxed{
dt_b=I_b c,\qquad
(F-p^2)t_b=I_b b+d\ell.
}
\tag{48}
$$
尤其不能在计算时把 $d\ell$ 无说明删掉，
也不能以某个 Teichmüller 挠提升的点日志0代替整个(47)。

### 9.4 原 Hodge 限制的同伦必须一并入式

在实际 de Rham 模型上，二维全纯形式限制到曲线为零。
在一个任意 PD/Čech 代表中，其对应说法是指定比较同伦
$\zeta_b\in C_b^1$，使
$$
I_b\Omega_S=d\zeta_b.
$$
它来自实际零限制，而非任意选一个原函数。
若复形把这个限制严格化为零，则可取 $\zeta_b=0$。
一般情形必须使用
$$
\begin{split}
\xi_{b,p}
 &=\left[I_b\Xi_p-(1-F/p^2)\zeta_b\right],\\
\mathfrak n_{b,p}
 &=\left[t_b-I_ba-u_p\zeta_b\right]\in H^1_{\rm dR}(S_b).
\end{split}
\tag{49}
$$
第二行由(45)、(48)确实闭合。将(46)、(48)代入，得到
$$
(F-p^2)\mathfrak n_{b,p}
 =-u_p p^2\,\xi_{b,p}.
$$
而原纤维 $H^1$ 上 $F=-p$，故
$$
\boxed{
\mathfrak n_{b,p}
 =u_p\frac p{p+1}\xi_{b,p}.
}
\tag{50}
$$
这才是同一个 normal function；它是
Miller–Frobenius 平凡化与全局 holomorphic 比较的差，
不是其任一部分的日志。

所有选择变化都可核回(48)–(50)。例如改变 $k_a$ 的提升或
Miller 函数的常数时，$t_b$ 的改变为闭 cochain，
且由(48)其类被 $F-p^2$ 杀；这个算子在 $H^1(S_b)$ 上为
$-p(p+1)$，可逆，故类不变。改变 $a$ 的闭部分来自
$H^1(S)$，其限制由(14)为零。改变 transition 提升或
embedding system 时，$c$ 改为 $c+dr$，
$b$ 同时改为 $b+(F-p^2)r$ 加 exact cochain；
$a$ 与 $t_b$ 中对应的 $r$ 正好抵消，余项仍由上述两种
唯一性消去。改变 $\zeta_b$ 时，必须同时改变该复形的
restriction comparison；(49)整体沿相同比较运输。
因此并不存在另一个可以自由调整原54个值的水平常数。

### 9.5 同一个全权读数与积分费用

保持(20)中的所有标号及系数，定义
$$
\mathcal N_{j,p}
=\frac1{18}\sum_\sigma\eta_j(\sigma)^{-1}
 \sum_\gamma\sum_{i=1}^{54}c_i
 \left\langle
   (\sigma\gamma\varphi_i)^*\mathfrak n_{\sigma\gamma b_i,p},
   \omega_A
 \right\rangle_A .
\tag{51}
$$
每一项的 $c,b,a$ 来自同一个固定 $D_p^+$，
而 $t_b$ 是该类在该实际图靶上的(47)。
这里不把系数 Galois 共轭同几何作用混同，也不重新选择
不同图所用的 $u_p$。degree34 留在真正 pullback 内。

由(20)、(42)、(50)，得到
$$
\boxed{
\operatorname{AJ}_p(Y_{j,0})(\Omega_S\omega_A)
 =u_p^{-1}\mathcal N_{j,p},\qquad
h_{j,p}=\frac{p+1}{p\,u_p}\,
        a_{j,p}^{-1}\mathcal N_{j,p}.
}
\tag{52}
$$
特别
$a_{j,p}^{-1}\mathcal N_{j,p}\in p\mathcal O$
来自§8的原 Fontaine–Laffaille 整格。
它不是由单项特殊点的阶 $p+1$ 推出的整除性，
更不能在未计算(51)前把除 $p$ 后的数预记为单位。

(43)、(44)、(47)、(48)已给可直接计算的 Chern 与 Miller
共链。仍需实际求出的全局部分是(45)中的 $a$，
以及原实际 Hodge 比较的 $\zeta_b$；
必须连同它们计算(51)，才能证明某个 $h_{j,p}$ 非零。
本节既不把空间微分 $\mu(Q_p)$ 当作 $h_{j,p}$，
也不以全局新增格的本原性替代该有限加权和。

本节的等式是上述 PD/Čech 复形中的直接计算；
proper AJ、投影及 trace 所需的来源范围仍严格是§7所列。
没有使用尚未取得全文的 normal-function 文献，也没有新增数学执行。

## 10. 原全局连接的曲率与明确的模 $p$ 定标

本节证明同一个 $u_p$ 与 R1043 的实际 Manin 常数之间的准确关系：
$$
\boxed{\ \overline u_p=-c_{Q_p}\ \in\mathbf F_{p^2}^{\times}. \ }
\tag{53}
$$
横线是原 $W$ 的模 $p$ 约化。式(53)用原
$\Omega_S,\omega_B,\mu$ 的规范，包含原三次基覆盖的倍率，
不只给一个未定非零比例。

以下记 $k=\mathbf F_{p^2}$、$K_0=k(B)$；
这里 $K_0$ 是函数域，不是前面的局部数域 $K_p$。

### 10.1 先构造真正 Shioda 线丛的全局连接

选一个仅含2、3因子的整数 $m>0$，清掉原 Shioda 校正的分母，
使 $mD(Q_p)$ 是 $S_k$ 上的实际整除子，并令
$\mathcal L=\mathcal O_{S_k}(mD(Q_p))$。
在泛纤维上准确有
$$
\mathcal L|_{S_{K_0}}=\mathcal O\bigl(m(Q_p)-m(O)\bigr).
\tag{54}
$$
式中右侧指除子的整数倍。旧垂直类和基类在泛纤维上平凡；
它们已经在左侧先作了正确校正。本文不对未校正的
$\mathcal O([Q_p]-[O])$ 直接声称全局 Atiyah 类为零。

由(31)，
$$
c_{1,\rm dR}(\mathcal L)=m\overline u_p\,\overline\Omega_S
 \in\operatorname{Fil}^2H^2_{\rm dR}(S_k).
\tag{55}
$$
因为 $c_1(D_p^-)$ 整除 $p$，故这里确实是**实际整**
$D(Q_p)$ 的 Chern 类，不是只对带系数 $D_p^+$ 作一个形式推断。

原固定好模型的 Hodge 分次自由及基变保证 Hodge–de Rham
谱序列在当前有限删集外于 $E_1$ 退化：
各个 Hodge 维数及 de Rham 总维数等于特征零的相应维数，
故没有余地容纳非零微分。
因此
$H^2(\Omega_{S_k}^{\ge1})\to H^2_{\rm dR}(S_k)$
为单射，像是 $\operatorname{Fil}^1$；
而其向 $H^1(\Omega_{S_k}^1)$ 的映射在
$\operatorname{Fil}^2$ 上为零。
Chern cocycle $d\log g_{ab}$ 的这个像就是 $\mathcal L$ 的
Atiyah 类。由(55)它为零，故 $\mathcal L$ 有全局代数绝对连接。

按§9的 Chern 符号，取局部一形式 $\vartheta_a$ 满足
$$
\check\delta\vartheta=d\log g.
$$
连接写作 $d-\vartheta$；其曲率为 $-d\vartheta$。
因为 $c_1-d_{\rm tot}\vartheta$ 只剩这个全局二形式，
且 $H^0(\Omega_{S_k}^2)\to H^2_{\rm dR}(S_k)$ 为单射，
得到准确的形式等式
$$
-d\vartheta=m\overline u_p\,\overline\Omega_S.
\tag{56}
$$
这不是只在一个穿孔邻域里比较两个 exact 的上同调类。

### 10.2 非零 KS 使泛纤维的连接曲率唯一

记泛纤维为 $\mathscr E/K_0$。绝对微分的序列给
$$
0\longrightarrow\Omega^1_{K_0/k}
 \longrightarrow H^0(\mathscr E,\Omega^1_{\mathscr E/k})
 \longrightarrow H^0(\mathscr E,\Omega^1_{\mathscr E/K_0})
 \xrightarrow{\rm KS}
 H^1(\mathscr E,\mathcal O_{\mathscr E})
       \otimes\Omega^1_{K_0/k}.
\tag{57}
$$
后三个相关空间各为一维，原 KS 由 R1043(97)为
$3dt/[t(1-27t)]$，非零；故最后箭头同构。
于是所有全局正则绝对一形式都来自基：
$$
H^0(\mathscr E,\Omega^1_{\mathscr E/k})=\Omega^1_{K_0/k}.
$$
任意两个定义在同一个 degree0 线丛上的绝对连接之差，
因此是一条基一形式，其外微分在一维函数域上为零。
**所以该线丛的连接曲率唯一。**

这个论证也说明此后完成到一个乘法 cusp 时不会留下能改变曲率
的额外选择。准确地说，我们将原有限秩空间
$\Omega^1_{K_0/k}$ 基变到 $k((s))$，并使用由原基导数延伸的
连续微分；不引入 $k((s))/k$ 的全部非连续 Kähler 微分。
在这个意义下，(57)继续是同一个一维 KS 序列。

### 10.3 在实际 Tate 线丛上计算曲率

在原 $I_9$ 或 $I_3$ cusp 取局部参数 $s$。
记真实 Tate period 为 $T=T(s)$，原点 $Q_p$ 的 Tate 参数为
$U=U(s)$。一般 $T=s^n$ 乘单位，$n=9$ 或3；以下始终使用
$d\log T$，不把 $T$ 偷换成 $s$。
在 Tate 均匀化的纤维坐标 $Z$ 上，
$$
\omega_T=d\log Z,\qquad
\lambda_T=d\log T,\qquad A_T=1,\qquad
z=\frac{d\log U}{d\log T}.
$$

为固定真正的线丛及其符号，可取
$$
\Theta_T(Z)=(1-Z)\prod_{r\ge1}(1-T^rZ)(1-T^r/Z),
\qquad \Theta_T(TZ)=-Z^{-1}\Theta_T(Z).
$$
比值 $\Theta_T(Z/U)/\Theta_T(Z)$ 的除子是 $(Q_p)-(O)$，
其 automorphy multiplier 是 $U$。
在§9使用的 transition 约定下，令
$$
\vartheta_T=z\,d\log Z.
$$
则
$\vartheta_T(TZ)-\vartheta_T(Z)=z\,d\log T=d\log U$。
所以它确实给**同一** $\mathcal O((Q_p)-(O))$ 的绝对连接。
这是 proper Tate 泛纤维上的正则线丛连接；
对该有限秩 connection 扩张使用 proper rigid GAGA，
可与(57)中的代数连接比较。

其 Chern 曲率为
$$
-d\vartheta_T=-dz\wedge d\log Z.
$$
R1043§19已在这个相同 Tate 规范支付
$\mu(Q_p)=z^p-z$。故
$$
-d\vartheta_T=d\mu(Q_p)\wedge\omega_T.
\tag{58}
$$
原模型变换
$\mu_{\rm new}=u^p\mu$、
$A_{\rm new}=u^{p-1}A$、
$\omega_{\rm new}=u^{-1}\omega$
给
$$
\Phi(Q_p):=\frac{d\mu(Q_p)}{A_p}\wedge\omega_t
$$
为模型无关的二形式；因为 $d(u^p)=0$，这里没有遗漏一个导数项。
在 Tate 模型中它就是(58)。
泛纤维连接曲率的唯一性因此将(58)运输到原曲面。
先对(54)的整数倍得到曲率 $m\Phi(Q_p)$，再除以当前
$p$ 单位 $m$，由(56)得到
$$
\overline u_p\,\overline\Omega_S=\Phi(Q_p).
\tag{59}
$$

最后，R1043§20给
$d\mu(Q_p)=c_{Q_p}A_p\omega_B$。
原坐标 $X=-3v$ 与 KS 的准确等式为
$$
\frac{dt}{v^2}=\frac v3\,\lambda=-\omega_B.
$$
所以
$\Phi(Q_p)=c_{Q_p}\omega_B\wedge\omega_t
          =-c_{Q_p}\overline\Omega_S$。
代入(59)即得(53)。该步骤保留原基覆盖和微分的全部倍率，
没有使用 cusp width 为1的替代模型。

### 10.4 同一个连接的相对 $p$-curvature

还有一个后继可直接使用的规范。
在 proper 泛纤维上，(57)说明绝对连接的**相对部分**唯一：
改变连接只加基一形式，不改变沿纤维的协变导数。
设 $D_{\mathscr E}$ 是与 $\omega_t$ 对偶的相对不变向量场，
故 $D_{\mathscr E}^{\,p}=A_pD_{\mathscr E}$。
对 $\mathcal O((Q_p)-(O))$ 的上述规范连接，定义相对
$p$-curvature 标量
$$
\Psi_Q=\nabla_{D_{\mathscr E}}^{\,p}
       -A_p\nabla_{D_{\mathscr E}}\in K_0.
$$
它是线丛的正则端同态；proper 纤维上的正则函数来自基，
故确为这个标量。

在 Tate 模型上，
$\nabla_{Z\partial_Z}=Z\partial_Z-z$，$A_T=1$，
所以
$$
\Psi_Q=-(z^p-z)=-\mu(Q_p).
\tag{60}
$$
与曲率一样，原相对部分的唯一性和 Tate 完成的单射将该式
给到原函数域；模型变换两侧同乘 $u^p$。
它也在每个原好纤维以极小模型延拓。
清掉 Shioda 分母时两侧同乘 $m$，再除回不会改变(60)。

例如在一个原超奇异好纤维 $S_b$，
用(47)的 $N=p+1$ Miller 平凡化给其 degree0 限制取
$p$-curvature 为零的挠连接。规范全局连接与它之差写作
$\lambda_b\omega_b$。
相对 $p$-curvature 的差为
$\lambda_b^p-A_p(b)\lambda_b$；因 $A_p(b)=0$，
$$
\boxed{\lambda_b^p=-\mu(Q_p)(b).}
\tag{61}
$$
这里的 $\lambda_b$ 只是这个实际特殊纤维连接差的全纯系数。
要读(52)中的除 $p$ 后 anti-Hodge 坐标，还须保留整
Frobenius/Čech 比较，不能仅凭(61)就称其等于原 AJ。

最后，绝对晶体 Frobenius 的约定也必须保留：
对一个实际特殊纤维线丛有
$\varphi c_1(\mathcal L)=p\,c_1(\mathcal L)$。
原 $Q_p$ 的**系数算术** Frobenius 为负并不将此式改成
$-p\,c_1(\mathcal L)$。
在内部 $W$ 标量的两 CM 投影中，半线性
$\varphi(\omega)=\omega^2$ 给
$$
\varphi c_1(D_p^+)=p\,c_1(D_p^-).
\tag{62}
$$
其平方才是本篇一直使用的 $F=p^2$。
本节未改变任何原最高投影或 Artin 下降方向。

## 11. 一次 Frobenius 给原54图的准确残余公式

本节将(52)中的除 $p$ 后读数真正接到原 Manin 多项式。
所用输入仍是同一个 $Y_{j,0}$、同一个 $D_p^+$ 和所有原图。
不更换循环，也不删去 $\eta_j$ 或 corestriction。

令 $p=6r-1$。为避免与原权 $c_i$ 混淆，把实际图的微分倍率记为
$$
\varphi_i^*\omega_{b_i}=d_i\omega_A.
\tag{63}
$$
对每个 $\sigma,\gamma$ 共轭均用相同定义。
在原固定有限删集外，这些图、有限基点和微分都在同一好模型上，
$d_i$ 为单位。式(63)包含完整 full9 运输；它不是只记一个
抽象 degree34 同源的倍率。

定义 R1043§20 已证明的多项式
$$
\begin{split}
H_p(U)&=\sum_{\nu=0}^{r-1}h_\nu U^\nu,\qquad
h_\nu=\frac{(-4)^\nu(5/6)_\nu(2/3)_\nu}{(\nu!)^2},\\
P_p(U)&=\sum_{\nu=0}^{r-1}\frac{h_\nu}{3\nu+1}U^\nu .
\end{split}
\tag{64}
$$
系数在 $\mathbf F_p$ 中；所有分母都是 $p$ 单位。
原坐标 $X=-3v$、$V=2Y+1$ 中
$$
A_p=V H_p(X^3),\qquad
\mu(Q_p)=c_{Q_p}X P_p(X^3),\qquad c_{Q_p}\ne0.
\tag{65}
$$

选源曲线的整 CM 基 $\omega_A,\epsilon_A$，使
$\langle\epsilon_A,\omega_A\rangle=1$，且 $\epsilon_A$ 在
与 $\omega_A$ 相反的 CM 线上。令 $\alpha_p$ 由
$$
\varphi\omega_A=p\alpha_p\epsilon_A,\qquad
\varphi\epsilon_A=-\alpha_p^{-1}\omega_A
\tag{66}
$$
定义。下文证明 $\alpha_p\in\mathbf Z_p^\times$。
它是这个固定源微分的明确晶体单位，不是可自由改变的周期。

本节结论为
$$
\boxed{
\begin{aligned}
\overline h_{j,p}
={}&-\overline a_{j,p}^{-1}\,\overline\alpha_p\,
\frac1{18}\sum_\sigma\eta_j(\sigma)^{-1}
 \sum_\gamma\sum_{i=1}^{54}c_i\,
 d_{\sigma\gamma i}^{\,p}\,
 X_{\sigma\gamma b_i}\,
 P_p\!\left(X_{\sigma\gamma b_i}^{\,3}\right).
\end{aligned}}
\tag{67}
$$
各几何量在原指定剩余域中约化。式中仅几何倍率
$d_{\sigma\gamma i}$ 取 $p$ 次幂；
$\eta_j(\sigma)^{-1}$ 和 $c_i$ 始终是原**外系数**，
不在这里额外作 Frobenius 共轭。

### 11.1 两个 PD 理想与同一原图的 filtered 比较

本节用 $\varphi$ 表示一次、对 $W$ 半线性的晶体 Frobenius；
其平方仍是前文 $F$。环境坐标取 $p$ 次幂，系数取 $W$ 的
Frobenius。模 $p$ 这就是绝对 Frobenius，所以它保持每个
特殊纤维的理想，即使该纤维或图只定义于 $\mathbf F_{p^2}$。
在乘积环境中它与投影严格交换。于是§9.1的整个有限图表
可以同时使用这个一次 Frobenius。

必须区分两个理想。记 $\mathscr D$ 为这些环境中的完备
PD envelope，令
$$
I=\ker(\mathscr D\longrightarrow\mathcal O_{\mathcal X}),\qquad
J=\ker(\mathscr D\longrightarrow\mathcal O_{X_k}).
$$
$I$ 是**实际 $W$ 模型**的法向 PD 理想，$J$ 是特殊纤维理想；
$J$ 还包含 $p$。每个实际模型、纤维及图都用自己的 $I,J$。
由于实际图映射定义在 $W$ 上，其环境投影把源模型的 $I$
送到图模型的 $I$，所以所有原 pullback 都保持下面的 filtration：
$$
\operatorname{Fil}^a_I(\mathscr D\Omega^\bullet)^b
   =I^{[a-b]}\mathscr D\Omega^b
\quad(b<a),
\qquad
=\mathscr D\Omega^b\quad(b\ge a).
\tag{68}
$$
这里 $I^{[n]}$ 表示由至少第 $n$ 阶 divided powers 生成的理想。

这个 filtration 的比较是原 Hodge filtration，不能把 $I$
换成 $J$ 后再直接声称同一事。其积分 Poincaré 比较可局部核实：
光滑模型在光滑环境中的嵌入是正则嵌入；在形式局部法向参数
$z_1,\ldots,z_e$ 中，PD de Rham 复形的每个法向变量有
$$
d\gamma_{n+1}(z)=\gamma_n(z)\,dz .
$$
收缩同伦把含 $\gamma_n(z)\,dz$ 的项送到
$\gamma_{n+1}(z)$，不引入分母。
它降低一阶形式次数、提高一阶法向 PD 次数，因而保持(68)。
逐个法向变量收缩，再在标准 Čech 覆盖上作同样的总复形比较，
给与实际 $\Omega_{\mathcal X/W}^{\ge a}$ 的 filtered
quasi-isomorphism。构造对这些环境投影的比较同伦也保持(68)。
这里用的是完备 PD 复形；不假定原曲面有 Frobenius lift。

据此，原全纯二形式可选一个积分代表，其总次数2的三个部分在
$$
\Omega^2,\qquad I\Omega^1,\qquad I^{[2]}\mathcal O
$$
中。仍把它记为 $\Omega_S$。
实际图上 $\Omega_S$ 的 de Rham 限制严格为零。
在曲线上 $\Omega^{\ge2}$ 整个复形为零，因此(68)的
$\operatorname{Fil}^2_I$ 比较复形无上同调。
故原限制有一个积分的、filtered 的原函数
$$
I_b\Omega_S=d\zeta_b,\qquad
\zeta_b\in
 \check C^0(I\Omega^1)\oplus
 \check C^1(I^{[2]}\mathcal O).
\tag{69}
$$
它表示的是实际零限制。
沿实际图拉回(69)仍是同一个 filtered 原函数；
若在图的另一个 embedding 中用局部收缩构造，
两者之差在同一个 $\operatorname{Fil}^2_I$ 复形中 exact。
所以可以同时保留全部54图的 pullback、实际零限制和(69)；
没有为不同图另加一个闭的常数类。

现在核一次 Frobenius 的整除性。
在 PD envelope 上，$\varphi\bmod p$ 是其绝对 Frobenius。
对 $z\in J$，$z^p=p!\gamma_p(z)$，故
$$
\varphi(J)\subset p\mathscr D,\qquad
\varphi(\mathscr D\Omega^1)\subset p\mathscr D\Omega^1.
$$
对 divided powers，若 $\varphi(z)\in p\mathscr D$，则
$\varphi(\gamma_n(z))=\gamma_n(\varphi z)$ 的 $p$ 赋值至少
$n-v_p(n!)$。在 $p\ge5,n\ge2$ 时此数至少2。
因 $I\subset J$，逐个分量得到
$$
\varphi(\Omega_S)\in p^2 C_S^2,\qquad
\varphi(\zeta_b)\in p^2 C_b^1.
\tag{70}
$$
特别(70)对于 degree1 的两个部分分别使用
$\varphi(I\Omega^1)\subset p^2\Omega^1$ 和
$\varphi(I^{[2]})\subset p^2\mathscr D$。
这里只需 $\varphi(I)\subset p\mathscr D$；
没有误用一般不成立的 $\varphi(I)\subset I$。

### 11.2 使全局原函数真的可作一次除 $p$

以下所有 $+$、$-$ 是内部 $W$ 标量的两个 CM projector。
先对真正的 $mD(Q_p)$ 构造 Chern cocycle、连接及 Miller
平凡化，最后除以 $p$ 单位 $m$ 并作投影。

取(45)的积分共链
$$
c_+=u_p\Omega_S+d a_+.
\tag{71}
$$
它存在于积分复形，因为两边在同一积分晶体格中有相同的类。
令 $\vartheta_+$ 是§10真实连接的 $+$ 投影。
将(71)映到实际特殊纤维的 de Rham 复形，得到
$d\overline a_+=d\vartheta_+$。
原 $H^1_{\rm cris}$、$H^2_{\rm cris}$ 自由及 de Rham 基变
使每个这样的闭差的类可由一个积分闭共链提升。
减去这个全局闭提升，再减去一个 exact 提升，可使
$\overline a_+=\vartheta_+$ 在这个实际 de Rham 复形中逐项相等。
若需保 CM 分量，最后应用同一分母3为单位的 projector。

这里 $\vartheta_+$ 只有 Čech0的一形式部分。
故调整后 $a_+$ 的 Čech1函数部分属于 $J$。
结合上节的整除性，
$$
\varphi a_+\in pC_S^1 .
\tag{72}
$$
这些调整都是全局闭类或 exact 类；原 $H^1(S)=H^1(B)$
限制纤维为零，所以它们不改变(49)的任一原读数。

对每个真正线丛仍取同一单位提升 $g_{ab}$，现在定义
$$
b_p=-\log\!\left(\frac{\varphi g_{ab}}{g_{ab}^{p}}\right).
$$
由于分式属于 $1+p\mathscr D$，$b_p\in pC_S^1$。
和(44)完全相同的两分量计算给
$\varphi c-pc=db_p$。
对内部 CM projector，$\varphi(\omega)=\omega^2$，故准确地是
$$
\varphi c_+-p c_-=d b_+,\qquad b_+\in pC_S^1.
\tag{73}
$$
这里 $b_+$ 是同一个 $b_p$ 的相应共轭 projector，
不是重新猜一个 Frobenius 同伦。

记 $\sigma_W$ 为 $W$ 的非平凡 Frobenius。定义
$$
\Omega_-^{\,\mathrm{F}}=\frac{\varphi\Omega_S}{p^2},\qquad
a_-=\frac{\varphi a_+-b_+}{p},\qquad
\zeta_{b,-}=\frac{\varphi\zeta_b}{p^2}.
$$
(70)、(72)、(73)证明三者都积分。
逐式代入(71)、(73)得到
$$
c_-=p\,\sigma_W(u_p)\Omega_-^{\,\mathrm{F}}+da_-,
\qquad
I_b\Omega_-^{\,\mathrm{F}}=d\zeta_{b,-}.
\tag{74}
$$
$\Omega_-^{\,\mathrm{F}}$ 只表示这个准确的 Frobenius 除式，
不冒充一个全纯形式，也不把它与(31)中任选的对偶基混同。

### 11.3 Miller 同伦给 $\varphi\mathfrak n_+=p\mathfrak n_-$

对同一批 Miller 单位使用一次 Frobenius。
以(47)的逐分量计算，精确有
$$
\varphi t_{b,+}-p t_{b,-}
   =I_b b_++d\ell_{b,+}.
$$
$\ell_{b,+}$ 来自
$(p+1)^{-1}\log(\varphi k/k^p)$ 及同一内部 projector。
不删这个 degree0 同伦。定义
$$
\begin{split}
\mathfrak n_{b,+}
 &=\left[t_{b,+}-I_ba_+-u_p\zeta_b\right],\\
\mathfrak n_{b,-}
 &=\left[t_{b,-}-I_ba_-
             -p\,\sigma_W(u_p)\zeta_{b,-}\right].
\end{split}
$$
由(71)、(74)两者都是积分闭类。
第一行恰是(49)已经定义的原 $\mathfrak n_{b,p}$。
把上述 Miller 等式和(74)代入，得到
$$
\boxed{\ \varphi\mathfrak n_{b,+}=p\,\mathfrak n_{b,-}.\ }
\tag{75}
$$
这是全 Čech 复形中的恒等式模 exact cochain。
其成立同时使用了 $\varphi\zeta_b/p^2$；
不能只在忽略实际限制同伦后写这个式子。

一次晶体 Frobenius 对所有原几何映射自然。
因此沿任一实际 $\varphi_i$ 拉回(75)仍成立。
这包括只定义于 $K_p$ 的图：半线性作用在其几何系数上，
不需要错误地要求每个图先定义于 $\mathbf Q_p$。

### 11.4 特殊纤维两个 CM 连接差的准确方向

先对实际 $Q_p,\tau Q_p,\tau^2Q_p$ 分别使用§10.4。
在每个原超奇异好纤维，令 $\lambda_s\omega_b$ 为
由(49)的 $t-\vartheta$ 指定的实际联络差（连接算子取 $d-\vartheta$）。
式(61)给
$$
\lambda_s^p=-\mu(\tau^sQ_p)(b).
$$
由原坐标 $\tau^*X=\omega X$ 及(65)，
$\mu(\tau^sQ_p)=\omega^s\mu(Q_p)$。

现在才形成内部系数的两投影：
$$
\lambda_+=\frac{\lambda_0+\omega^2\lambda_1+\omega\lambda_2}{3},
\qquad
\lambda_-=\frac{\lambda_0+\omega\lambda_1+\omega^2\lambda_2}{3}.
$$
因 $p\equiv-1\bmod3$，取 $p$ 次幂会交换两组系数。
所以
$$
\lambda_+^p=0,\qquad
\lambda_-^p=-\mu(Q_p)(b).
\tag{76}
$$
这一步不能把 $p$-curvature 当成对内部 $W$ 标量线性的映射。

由$a_+$的选择及$\zeta_b$的 filtered 性质，
$\overline{\mathfrak n}_{b,+}=\lambda_+\omega_b=0$。
对负分量，(74)模$p$给$d\overline a_-=c_-$。
而$\vartheta_-$的曲率为零，亦有$d\vartheta_-=c_-$。
故$\overline a_--\vartheta_-$是来自全局
$H^1_{\rm dR}(S_k)$的闭类，限制纤维为零。
因此
$$
\overline{\mathfrak n}_{b,-}=\lambda_-\omega_b,\qquad
\lambda_-^p=-\mu(Q_p)(b).
\tag{77}
$$
没有对形式的带系数 $D_p^-$ 宣称它本身是一条真正线丛；
上述等式始终由三条真正连接逐项组合得到。

### 11.5 源 CM 格逐式读出除 $p$ 后的杯积

源 $A$ 的积分 Hodge 线和相反的 CM 线均为直和因子。
强可除性给
$\varphi\omega_A=p\alpha_p\epsilon_A$，
$\varphi\epsilon_A=\beta_p\omega_A$，
其中 $\alpha_p,\beta_p$ 为单位。
完美杯积在 $\varphi$ 下乘$p$，所以
$\alpha_p\beta_p=-1$。
再用原$\varphi^2=-p$，得到
$\sigma_W(\alpha_p)=\alpha_p$。
这证明(66)及$\alpha_p\in\mathbf Z_p^\times$，同时固定全部符号。

对一个原图，记
$$
\begin{split}
\varphi_i^*\mathfrak n_{b_i,+}&=A_i\omega_A+B_i\epsilon_A,\\
\varphi_i^*\mathfrak n_{b_i,-}&=A_i^-\omega_A+B_i^-\epsilon_A.
\end{split}
$$
全部系数属于$W$。
(75)、(66)的$\omega_A$系数给
$$
-\alpha_p^{-1}\sigma_W(B_i)=pA_i^-.
$$
故$B_i$整除$p$，且
$B_i/p=-\alpha_p\sigma_W(A_i^-)$。
由(63)、(77)，
$\overline A_i^-=d_i\lambda_-$，
所以
$$
\boxed{
\overline{\frac1p
 \left\langle\varphi_i^*\mathfrak n_{b_i,+},\omega_A\right\rangle}
 =\overline\alpha_p\,d_i^p\,\mu(Q_p)(b_i).
}
\tag{78}
$$
杯积方向使用$\langle\epsilon_A,\omega_A\rangle=1$；
两个负号分别来自 Frobenius 矩阵与(77)，在这里抵消。
特别(78)支付了每个实际图的除$p$，不只是对最终加权和
引用§8的抽象整除性。

degree34仍在(78)内。若在靶上取相同的杯积规范，
写$\varphi\omega_b=p\alpha_b\epsilon_b$，
则实际同源的对偶性给
$\varphi_i^*\epsilon_b=(34/d_i)\epsilon_A$。
Frobenius自然性因而给
$$
\alpha_p\,\sigma_W(d_i)=\frac{34}{d_i}\alpha_b .
\tag{79}
$$
其模$p$形式正是(78)中的$\alpha_p d_i^p$。
所以本计算没有省掉34，也没有把实际几何倍率改成无权
Hecke 算子的规范。

### 11.6 全部原权、下降基及结论的范围

最后对(78)按(51)逐项施加原$e_{\eta_j}$和
$\operatorname{Cor}_{L/H}$。
各图的几何数据仍按$\sigma\gamma$作用；
原外系数$E$保持不动。
由(52)，$p+1\equiv1\bmod p$，
再用(53)、(65)，
$$
\overline u_p^{-1}\mu(Q_p)(b)
   =-X_bP_p(X_b^3).
$$
这就逐项得到(67)。

式(67)中不存在未定的$c_{Q_p}$、未定的曲率比例或新的
horizontal 常数。原$\alpha_p$和$a_{j,p}$都是已指定的非零单位；
全部可能的零仍准确保留在原54项、其共轭和角色权构成的和中。
该等式给原局部扩张的模$p$参数：
如果这个完整有限和非零，(39)、(42)即给同一原局部 AJ 非零。
若有限和为零，只能说明该扩张参数至少整除$p$，
不能据此判定整个$p$-adic AJ为零。

本节没有从$\mu(Q_p)\ne0$推出这个加权和非零，
也没有把所得局部最高 AJ 自动等同于 R970/R973/R1038
通常 Selmer 入口所需的椭圆曲线 canonical 中央首导数。
后继须分别支付全权非零及该原算术入口的真实比较。

## 12. 原全迹、三列以及准确的 weight $p$ CM companion

本节对(67)的有限和继续作实际计算。
首先消去的是已经支付的原 Galois 重标记；
随后把同一个有限多项式识别为一个规范 CM theta form。
后一识别包含原 $\Gamma$、宽度3及常数 $3\delta$。

### 12.1 全部 $\eta$/Cor 恰给原 $[L:H]$

令
$$
m_p(b)=X_bP_p(X_b^3),\qquad
z^{(p)}_{i,t}=d_{i,t}^{\,p}m_p(b_{i,t}),
\qquad
\mathcal T_{j,p}^{\,m}
 =\sum_{i=0}^2\sum_{t\in C_{18}}
      \omega^i\vartheta_{l_j}(t)^{-1}z^{(p)}_{i,t}.
\tag{80}
$$
这里 $l_j=-5,1,7$，$j=4,10,16$。
式(80)始终在原 $A=E_{27}$、原 full9 级点及指定的
$\mathbf F_{p^2}$ 嵌入上评价。

R1043(75)已在特征零完整模问题中逐图证明
$$
\gamma\varphi_{i,t}
 =\varphi_{i-r_\gamma,h_\gamma^{-1}t},
$$
包括靶的完整9级、原微分及零截面。
同一处(76)给**实际带系数循环**的等式
$\gamma Z_j=\eta_j(\gamma)Z_j$。
这里的系数作用仍是$\gamma\otimes1$。
所以对(67)的同一个线性读者，这些严格图等式逐项相加，得到
$$
\frac1{18}\sum_\sigma\eta_j(\sigma)^{-1}
 \sum_\gamma\sum_{i,t}c_{i,t}\,
 d_{\sigma\gamma(i,t)}^p m_p(b_{\sigma\gamma(i,t)})
 =[L:H]\,\mathcal T_{j,p}^{\,m}.
\tag{81}
$$
这不需要把 weight $p$ 放进 R1006 的某个经典权分支；
所用的是 R1043 在 Chow 层已经核完的完整置换。
若使用其最小原级域$L_0=K(E_{27}[306])$，
$[L_0:H]=432$；更大的实际$L$仍保它自己的倍数。

于是(67)准确简化为
$$
\boxed{\;
\overline h_{j,p}
 =-\overline a_{j,p}^{-1}\overline\alpha_p
    [L:H]\,\mathcal T_{j,p}^{\,m}.
\;}
\tag{82}
$$
原 Artin 基$a_{j,p}$并未被这个重标记删除。

### 12.2 原三列依旧相加，且有单个多项式表达

这里可以直接核(80)中的相位，不借一个未经证明的
“Manin 值是点值”断言。
R1043(23)的实际图给
$$
X_{i,t}=\omega^iX_{0,\omega^{-i}t},\qquad
d_{i,t}=\omega^i d_{0,\omega^{-i}t}.
$$
在当前固定有限删集外所有这些目标均在原有限好模型上。
因$p\equiv-1\bmod3$，$d^p$和$X$的两个相位相消：
$z^{(p)}_{i,t}=z^{(p)}_{0,\omega^{-i}t}$。

另一方面，R1027(30)的**原实际**交换图为
$F_b\varphi_C=\varphi_{\delta C}[-\delta]_A$。
其微分等式是$\delta d_C=-\delta d_{\delta C}$，
所以$d_{\delta C}=-d_C$。
基点变成$-b=(X,-1-Y)$，其$X$不变。
故
$z^{(p)}_{\delta C}=-z^{(p)}_C$。
原角色在同一 order2 类上的值也为$-1$，所以仍是正重数2，
没有因一次 Frobenius 改成消零。

沿 R1043(29)固定$s$及$\zeta_9$的方向，置
$$
\mathcal B_{a,p}
 =\sum_{i=0}^2\omega^i z^{(p)}_{i,s^{2a}},
 \qquad a=0,1,2 .
$$
和 R1043(30)、(34)同样的逐标号求和给
$$
\boxed{\;
\mathcal T_{j,p}^{\,m}
 =6\sum_{a=0}^2\zeta_9^{-l_ja}\mathcal B_{a,p}.
\;}
\tag{83}
$$
按$j=10,4,16$的顺序，这是三个指数$1,4,7$的三阶 Fourier
矩阵。其行列式只含3的单位因子。
因而在所有原固定次数亦为$p$单位的范围内，
三个$\overline h_{j,p}$同时为零，等价于
$\mathcal B_{0,p}=\mathcal B_{1,p}=\mathcal B_{2,p}=0$。
这次等价已经是原局部扩张的残余读数，不再只是无权 Picard 类。

还可用 R1043§§13、21、22 的同一真实二商写出各列。
记$t_a=s^{2a}$，$\psi_{t_a}$为原 degree17 图，
$e_a$由$\psi_{t_a}^*\omega=e_a\omega_A$定义。
令$(X'_a,Y'_a)=q_-d_{t_a}$为原有序全二谱 lift 所给的点，
$V'_a=2Y'_a+1$，并令$N_p$为 R1043(127)–(130)的完整多项式。
组合图$\varphi_{i,t_a}=\phi_{2,i}\psi_{t_a}$的微分给
$d_{i,t_a}=e_a c_{2,i}$；代入那里的三项函数恒等式便得
$$
\boxed{\;
\mathcal B_{a,p}
 =e_a^p\,\frac{X'_a}{(V'_a)^{\,2r-1}}\,
        N_p\!\left((V'_a)^2\right).
\;}
\tag{84}
$$
(84)不把外系数$\omega$变成邻近纤维的几何端同态。
它只是(80)这三个**函数**的完整代数化简，
所有分母按已付原模型延拓；若使用有限坐标，仍排其固定坏集。
本式也未声称这三个指定代数点中的某一点已不在$N_p$的零集。

### 12.3 一个真正属于原 $\Gamma$ 的 CM theta form

令$\psi=\psi_{27}$，定义规范新形式
$$
f_{p-1}(\tau)
 =\theta(\psi^{\,p-1})(\tau)
 =\sum_{\substack{\mathfrak a\subset\mathcal O_K\\(\mathfrak a,3)=1}}
      \psi(\mathfrak a)^{p-1}q^{\mathrm N\mathfrak a},
\qquad
g_p(\tau)=f_{p-1}(\tau/3).
\tag{85}
$$
这里是 Hecke theta series；不是微分算子$\theta$。
因为$p-1\equiv4\bmod6$，$\psi^{p-1}$在$\mu_3$上的有限型仍
非平凡，且原模$(3)=\delta^2$的型保持。
它的精确导子仍为$(3)$，不是较小的$\delta$。
Hecke theta 构造因而给 weight $p$、level27、
nebentypus$\chi_K$的原始 cusp newform。
同 R991 使用的 CM 构造，系数按共轭理想配对为有理代数整数。

需要核的是它确实进入**原**$\Gamma$。
每个出现的范数都为$1\bmod3$，所以
$g_p(\tau+1)=\omega g_p(\tau)$。
另一方面，$f_{p-1}$的系数为实数，newform 的 Fricke 关系
使它为$W_{27}$的本征形式；
因此$g_p$为
$D_3=\left(\begin{smallmatrix}0&-1\\3&0\end{smallmatrix}\right)$
的本征形式。这里不需要把这个本征值冒充 weight3 时的值。
由准确的矩阵等式
$$
D_3T^{-1}D_3^{-1}
 =\begin{pmatrix}1&0\\3&1\end{pmatrix}=U_3
$$
可知$g_p|U_3=\omega^{-1}g_p$。
$T,U_3$生成$\Gamma_1(3)$；
这两个值正是原角色
$\left(\begin{smallmatrix}a&b\\3c&d\end{smallmatrix}\right)
\mapsto\omega^{b-c}$。
所以$g_p$对其核$\Gamma$为真正的 weight $p$ cusp form。
这个证明保留了两个生成元，不只从$T$的$q$展开猜级别。

完整 determinant 下降也保持。
在原 full9 的 Tate 模型上，$g_p$的展开仅含$q^{n/3}$，
系数为有理整数。R1043(14)、(74)中的 determinant 部分
$d\equiv1\bmod3$固定原$\zeta_3$和该展开。
$q$-expansion principle 故将它下降到同一个完整
$G_\Gamma$模型和原$K$分量。
没有再用$h$翻转这个分量，也没有重选一套 full9 基。

这些形式在$p\nmid6$时为整形式。
可直接从 tame 光滑模型的$q$-expansion principle 看出：
若一个形式在整格中有负$p$赋值，其最小分母清掉后的非零
特殊纤维截面，不可能在这个 cusp 的整个形式邻域上为零。
所以(85)的整$q$系数不容许这里出现额外$p$分母。

### 12.4 惰性 Frobenius 逐系数给完整导数等式

记原$f_2=\theta(\psi^2)=\sum A_nq^n$，
$h_\Gamma=f_2(\tau/3)$。
对$p\nmid n$，每个$\mathrm N\mathfrak a=n$满足
$$
\psi(\mathfrak a)^p
 \equiv\overline{\psi(\mathfrak a)}\pmod p,\qquad
\psi(\mathfrak a)\overline{\psi(\mathfrak a)}=n .
$$
因此
$n\psi(\mathfrak a)^{p-1}
 \equiv\overline{\psi(\mathfrak a)}^{\,2}$；
把$\mathfrak a$与其共轭重新标号，得
$n\,a_n(f_{p-1})\equiv A_n$。
若$p\mid n$，惰性$p$的理想范数含$p$只能以偶数指数出现；
存在这样的理想时，$\psi^2$的相应项至少含$p^2$。
所以$A_n\equiv0$；左侧也为零。
这核了全部$p$倍指数，不只prime-to-$p$部分。
于是原宽度3的展开准确满足
$$
\boxed{\quad
q\frac d{dq}g_p=\frac13h_\Gamma\pmod p .
\quad}
\tag{86}
$$

因 weight 正是$p$，$L^p$有 Frobenius 拉回的规范连接：
在局部框架$e^p$中，$\nabla(fe^p)=df\,e^p$。
用原 KS 同构把
$L^p\otimes\Omega_B^1(\log\{T,-T\})$
识别为$L^{p+2}$，得到这里的几何导数$\Theta_p$；
其 Tate 展开就是$q\,d/dq$。
这不是在普通 locus 上除以 Hasse 后留下的一个有极算子。

R1043(111)给原 raw 形式
$D_Bm_p=A_p$，
而$\lambda=9\omega_B/X$，故
$D m_p=A_pX/9$。
再保 R997(23)的实际 split Tate 微分
$\omega_t=r(q)\omega_{\rm can}$，$r(0)=\delta$。
同篇(24)等价于
$$
r(q)^3\,\frac X9=\delta\,h_\Gamma(q).
$$
因为$A_{\rm can}=r^{p-1}A_p=1$、$d(r^p)=0$，
在原同一个 Tate 参数中得到
$\Theta_p(m_p)=\delta h_\Gamma$。
与(86)比较，
$\Theta_p(m_p-3\delta g_p)=0$。

这个核没有隐藏的$q^p$ cusp 项。
若$G\in H^0(B,L^p(-T-(-T)))$且$\Theta_pG=0$，
局部框架下其函数的导数为零，故为一个$p$次幂。
过渡函数也为$p$次幂，这些根拼成 Frobenius 共轭曲线上的
weight1 截面；在两个 cusp 的正零阶保证其亦 cuspidal。
但原$L=\mathcal O_B(O)$，所以
$$
\deg L(-T-(-T))=1-2=-1,
$$
该 weight1 cusp 空间为零。因而$G=0$。
这里$m_p$确为 cusp 形式：原多项式的唯一极在$O$，
阶$p-3$，并在两个$X=0$的 cusp 都为零。
遂得到原规范下的严格等式
$$
\boxed{\qquad
m_p=X P_p(X^3)=3\delta\,g_p
 \quad\text{作为原 }\Gamma\text{ 上的 weight }p
 \text{ 模形式，模 }p .
\qquad}
\tag{87}
$$
比例$3\delta$来自原非裂 cusp 的真实微分和宽度3，
不是一个随后可忽略的未知比例。

### 12.5 回到同一有限 toric 值

若$\omega_b/d_i$是由实际商规定的微分，
$\varphi_i^*(\omega_b/d_i)=\omega_A$，
weight $p$ 的定义给
$$
g_p(S_{b_i},\ell_{b_i},\omega_b/d_i)
 =d_i^p g_p(S_{b_i},\ell_{b_i},\omega_b).
$$
所以(80)、(87)准确是同一个原有限向量的评价：
$$
\begin{split}
\mathcal T_{j,p}^{\,g}
 &:=\sum_{i,t}c_{i,t}
      g_p(S_{b_{i,t}},\ell_{b_{i,t}},\omega_b/d_{i,t}),\\
\mathcal T_{j,p}^{\,m}
 &=3\delta\,\mathcal T_{j,p}^{\,g},\\
\boxed{\quad
\overline h_{j,p}
 &=-3\delta\,\overline\alpha_p\,
   \overline a_{j,p}^{-1}[L:H]\,
   \mathcal T_{j,p}^{\,g}.
\quad}
\end{split}
\tag{88}
$$
该有限向量仍在2、17处使用原非平凡 torus 角色，
原degree34/full9微分全部保留；不换成球向量或无权 Hecke 和。

(87)本身以及(80)–(84)的有限函数恒等式不需要新增 NS 格存在的
$p>q_0$前提。只有把它们称作(88)的原局部扩张参数时，
仍保留§1–11的全部晶体整格及几何前提。
所以单个较小$p$的有限和计算若没有另外支付该$p$的整格，
只能报告这个完整有限和，不能先给它标成原$h_{j,p}$。

本节已经把下一非零问题准确转成一个原 CM theta form 的
完整 toric 值。其经典 CM 分解、原 type4 Taylor 源及周期的比较
若要用于模$p$，仍须逐项支付阶乘和所有$p$赋值。
这里没有从一个复临界值非零推出(88)的模$p$非零。
