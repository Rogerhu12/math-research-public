# 闭平方根的已付 gauge 差实际生成全域分母

日期：2026-11-27（台北时间，UTC+8）。作者：literature_deddens / Astra-ISP-8542378f-20261127。

状态：以下是特殊代数闭域的正向分母构造。先保留一个已经实际支付的共同 gauge 图接口，再用平方根方程构造具体的有界分母和分子。没有从强单位或共同整幂像直接推入未知域。

## 1. 固定原尾、真实根域和实际 gauge 接口

在原尾 Haar 空间 $H$ 上记
$$
B=B_m,\qquad \mathscr C_m=\{B_m\}',\qquad
C=C_m.
$$
完整交换子交换且每个有界元素都满足 $F^\sharp:=CF^*C=F$。

设 $T$ 为稠密定义的闭算子，$\mathcal D=\operatorname{Dom}T$，并满足
$$
T=CT^*C,\qquad
T\mathcal D\subseteq\mathcal D,\qquad
T^2x=\lambda B^p x\quad(x\in\mathcal D),
\qquad \lambda\ne0, p\ge1.
\tag{1.1}
$$
还保留真实原尾域交换
$$
B\mathcal D\subseteq\mathcal D,\qquad TB=BT\text{ 于 }\mathcal D.
\tag{1.2}
$$
当 $p$ 为奇数时，已证奇幂强恢复与闭性可由 (1.1) 返回 (1.2)；
偶 $p$ 时本稿不省略 (1.2)。

取 dyadic 根 $\zeta$ 使 $\zeta^p\ne1$，令 $U=U_\zeta$ 为原物理字符酉算子，
$UBU^*=\zeta B$，并记
$$
G=UTU^*,\qquad \mathcal D_G=U\mathcal D.
$$
这是与原参数相同的真实闭实现；它的域 $G$-稳定，并有
$$
G^2x=\zeta^p\lambda B^p x\qquad(x\in\mathcal D_G).
\tag{1.3}
$$
由完整交换子的有界强多项式逼近，$\mathcal D$ 与 $\mathcal D_G$ 都由
$\mathscr C_m$ 保持，且 $T,G$ 分别在各自域上与全部 $\mathscr C_m$ 交换。

**唯一额外的 gauge 输入。** 已经实际取得
$$
R,Q\in\mathscr C_m,\qquad R\text{ 单射},
\tag{1.4}
$$
满足
$$
\boxed{
R\mathcal D\subseteq\mathcal D_G,
\qquad GRx=RTx+Qx\quad(x\in\mathcal D).
}
\tag{1.5}
$$
由于 $R$ 保持 $\mathcal D$，(1.5) 的像实际处在两个域的交。
(1.5) 是 R143 共同 gauge 正则化的准确形式。
它必须来自同一个根的实际闭域；只有有限柱形式差而没有图核心传递时，不能援用本定理。

## 2. 具体有界分母和分子

定义
$$
\boxed{
P=RQ,\qquad
Y=\frac12\left((\zeta^p-1)\lambda B^pR^2-Q^2\right).
}
\tag{2.1}
$$
它们都是原完整交换子中的有界算子。

**定理 2.1。** 在 (1.1)--(1.5) 下，$P\ne0$，并且
$$
\boxed{PH\subseteq\mathcal D,\qquad TP=Y\quad\text{于整个 }H.}
\tag{2.2}
$$
此外
$$
\boxed{Y^2=\lambda B^pP^2.}
\tag{2.3}
$$
其实际有界费用可取
$$
\|P\|\le\|R\|\|Q\|,
\qquad
\|TP\|=\|Y\|
\le\frac12\left(
|\zeta^p-1|\,|\lambda|\,\|B^p\|\|R\|^2+\|Q\|^2
\right).
\tag{2.4}
$$

### 2.1 全部自然中间域

固定 $x\in\mathcal D$。由 $T$ 稳定，$Tx\in\mathcal D$。
由交换子保持域，$RTx,Qx\in\mathcal D$。
所以 (1.5) 给
$$
R^2x,\quad R^2Tx,\quad RQx\in\mathcal D_G.
\tag{2.5}
$$
先对 $Rx\in\mathcal D$ 使用 (1.5)，得到
$$
GR^2x=R^2Tx+RQx.
\tag{2.6}
$$
(2.5) 保证右侧两项都可以分别再作用 $G$。
分别对 $RTx$ 与 $Qx$ 使用同一 (1.5)，并只在已支付的 $\mathcal D$ 内交换 $T$ 与 $R,Q$，有
$$
GR^2Tx=R^2T^2x+RQTx,
\qquad
GRQx=RQTx+Q^2x.
$$
于是
$$
G^2R^2x=R^2T^2x+2RQTx+Q^2x.
\tag{2.7}
$$
由 (1.1)、(1.3) 及 $R^2x\in\mathcal D_G$，得到
$$
\boxed{PTx=Yx\qquad(x\in\mathcal D).}
\tag{2.8}
$$
这里先得到的确只是密域上的左乘式；下一步才证明整个 $PH$ 入域。

### 2.2 完整 $C$ 自伴性把左乘界变为全域像包含

因为 $P$ 有界，通常伴随有准确自然域等式
$$
(PT)^*=T^*P^*,
\qquad
\operatorname{Dom}(PT)^*=\{h:P^*h\in\operatorname{Dom}T^*\}.
\tag{2.9}
$$
另一方面，(2.8) 说明 $PT$ 恰是有界 $Y$ 在稠密域 $\mathcal D$ 上的限制。
所以
$$
(PT)^*=Y^*\quad\text{于整个 }H.
$$
结合 (2.9)，$P^*H\subseteq\operatorname{Dom}T^*$ 且 $T^*P^*=Y^*$。
两边施加同一个原共轭 $C$，使用
$$
CT^*C=T,\qquad CP^*C=P,\qquad CY^*C=Y,
$$
严格得到 (2.2)。
这一步使用的是 (1.1) 的完整最大对称域等式；
若只知 $T\subseteq CT^*C$，上述转置一般只给 $PH$ 进入较大的转置域，不能免费返回原域。

### 2.3 非零性与有界平方身份

若 $Q=0$，(2.7) 给
$$
(\zeta^p-1)\lambda B^pR^2x=0\qquad(x\in\mathcal D).
$$
有界性把它延到 $H$。原 $B$ 单射、$\lambda(\zeta^p-1)\ne0$、$R$ 单射，矛盾。
故 $Q\ne0$；再由 $R$ 单射，$P=RQ\ne0$。
这里不需要另加 $Q$ 单射性。

对任意 $h\in H$，$Ph\in\mathcal D$，稳定性给
$Yh=TPh\in\mathcal D$。
因 $P$ 属于完整交换子，它保持并在 $\mathcal D$ 内与 $T$ 交换。
逐次使用这些已付的域得
$$
Y^2h=TP(TPh)=T^2P^2h
=\lambda B^pP^2h,
$$
证明 (2.3)；(2.4) 直接来自 (2.1)。

对每个固定 $n\ge0$，同一个 $P$ 事实上支付整个自然幂域，且有
$$
PH\subseteq\operatorname{Dom}T^n,
\qquad
T^{2r}P=\lambda^rB^{pr}P,
\qquad
T^{2r+1}P=\lambda^rB^{pr}Y.
\tag{2.10}
$$
这些是真正有界算子式，始终保同一来源 $P$。

## 3. 奇数幂根的共同 gauge 正则器本身必须平坦

现取 $p$ 奇数；这是标量原尾的不整除平方根情形。
已证兼容字符喷射给
$$
j_\chi:\mathscr C_m\longrightarrow\mathbb C[[z]],
\qquad j_\chi(B)=z,
$$
对 (2.3) 使用该同态，若 $j_\chi(P)\ne0$，其形式阶给
$2\operatorname{ord}j_\chi(Y)=p+2\operatorname{ord}j_\chi(P)$，与 $p$ 奇数矛盾。
因此 $j_\chi(P)=0$，同一平方等式再给 $j_\chi(Y)=0$。
这也正是已证实际标量分母平坦结论的当前标量平方情形。

将 (2.1) 施加 $j_\chi$，写 $r=j_\chi(R)$、$q=j_\chi(Q)$，得
$$
rq=0,\qquad
(\zeta^p-1)\lambda z^p r^2-q^2=0.
\tag{3.1}
$$
$\mathbb C[[z]]$ 为整环。如果 $r\ne0$，第一式给 $q=0$，
第二式又迫 $r=0$，矛盾。因此 $r=0$，第二式再给 $q=0$。
所以
$$
\boxed{R,Q,P,Y\in\mathfrak I_{\infty,m}.}
\tag{3.2}
$$
这比只知道最终乘积分母 $P$ 平坦更具体：
任何成功支付 (1.5) 的原共同 gauge 正则器 $R$ 本身都必须在全喷射核中。

若有某个字符 $\chi$ 使 $j_\chi(R)\ne0$，则 (1.1)--(1.5) 不可能同时成立。
例如 $R$ 为非零原解析芽、或 $R=B^rV$ 且 $V$ 为完整交换子中的可逆元素时，
$j_\chi(R)=z^rj_\chi(V)\ne0$，因此排除该根。
这不是说所有来自真实一阶预解式的 $R$ 都具有非零喷射；对它们不能省略单独核查。

## 4. 与已付 R143 接口的精确衔接

R143 主稿的无条件输入只适用于其已经识别的实际二阶闭乘子及对应 gauge 变换，
从同一有限柱图核心上的差
$$
(G-T)u=F_*u+\sum_{i<m_0}F_i Z_i u
\tag{4.1}
$$
构造同一有限个原正一阶预解式的乘积 $R(t)$。
精确位置是该稿 §3 的 (3.1)--(3.4)：把每个实际第一阶行 $Z_i$ 拆成四个非负行，
取它们已有的 $R_{i,\nu}(t)=(I+tZ_{i,\nu})^{-1}$，再取有限乘积。
每个因子单射、范数不超过一；R128 的真实域结论给 $Z_iR(t)$ 全域有界。
这里付清的是各一阶差行的全域正则化，不是根 $T$ 的全域正则化。
该构造实际给出
$$
R(t)\operatorname{Dom}T\subseteq
\operatorname{Dom}T\cap\operatorname{Dom}G,
\qquad
GR(t)x=R(t)Tx+Q(t)x,
\tag{4.2}
$$
其中
$$
Q(t)=F_*R(t)+\sum_iF_i Z_iR(t)\in\mathscr C_m,
$$
$R(t)$ 单射。
其从有限核心返回全 $\operatorname{Dom}T$ 的非循环步骤是 R143 §4 (4.1) 的证明：
对固定 $x\in\operatorname{Dom}T$，取有限柱 $u_n\to x$、$Tu_n\to Tx$。
有限柱同时属于两个闭域；完整交换子域保持给 $R(t)u_n\in\operatorname{Dom}G$，
且在这些实际列上有
$$
GR(t)u_n=R(t)Tu_n+Q(t)u_n\longrightarrow R(t)Tx+Q(t)x.
$$
$R(t)u_n\to R(t)x$，所以只用 $G$ 的闭性便得到 (4.2)。
这一论证不预先使用 $R(t)H\subseteq\operatorname{Dom}T$ 或任何待求的根分母。

因此若**同一个** $T$ 还满足本稿 (1.1) 的闭稳定平方身份，
则无需再猜测一个一般公共倍数，直接取
$$
\boxed{
P(t)=R(t)Q(t),\quad
Y(t)=\frac12\bigl((\zeta^p-1)\lambda B^pR(t)^2-Q(t)^2\bigr)
}
\tag{4.3}
$$
便已支付 $P(t)H\subseteq\operatorname{Dom}T$ 及 $TP(t)=Y(t)$。

R143 主稿 §6，特别 (6.1)--(6.4)，在首个非零一阶行情形还给
$Q(t)=F(B)ZR(t)$，其中 $F(B)$ 是原尾幂乘解析单位，$Z$ 为非零实际闭第一阶乘子，
并已证明 $Z R(t)$ 有界、单射。
此时 $P(t)$ 也单射；由有界交换子的原 $C$ 对称性，其像稠密。
这是具体的 quasiaffinity 分母；仍不自动断言其主理想在全部有限放大上有强单位。

R143 本身没有给它的原二阶闭乘子附加本稿的平方根身份 (1.1)。
因此“二阶乘子的实际 (4.2) 已付”与“某个另外出现的未知根也有 (4.2)”是不同断言。
对于后者，本稿仍要求先证同一有限核心差、实际一阶行正则化及上述闭图传递，不能只引用正则器的名称。

这里没有把 R143 任意核诱导的头像反根直接识别为其原二阶闭乘子。
头像反根一般作用于未知底空间，未必承载原全尾共轭或原字符 gauge。
本节的应用必须确认是同一个闭算子、同一个原尾空间、同一个实际共同域接口。

## 5. 同源方程及未决部分

如果另有 $1\in\mathcal D$，记 $f=T1$。
完整交换子域交换和 (2.2) 立即给实际来源等式
$$
Pf=PT1=TP1=Y1.
\tag{5.1}
$$
这个等式来自已经支付的全域像包含；并未依赖一般 RSC 或可闭性。
新无一般分母定理中的坏源不会满足这里的整个根与已付 gauge 接口。

本稿构造的正向接口仍要求 (1.5) 的实际来源。
不能仅从两个闭根的共同稠密域、形式 gauge 差，或平坦理想的强*密度推导它。
若某个真实根只有非最大 $C$ 对称性，§2.2 返回原域的步骤也必须另外补足。
对未知普通不变子空间上的根，原共轭、gauge 作用和比较的底空间都要逐项核实。

## 已证来源

- [全交换子兼容喷射与实际平坦根分母](../results/R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)；
- [R143：真实共同 gauge 正则化，§§3--6](../results/R143-quadratic-gauge-common-regularizers-and-kernel-graphs.md)；
- [原尾奇幂强恢复与实际子商](../results/R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)；
- [原完整交换子无一般有界分母](../results/R12-appendix-full-commutant-no-bounded-regularizer-and-nonclosability.md)。
