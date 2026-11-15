# R271 附录：真实 joined 商的创建源同余、共同 coherent Gram 与固定源上界

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文识别原 left+bare joined 商的固定低端来源。即使 joined 最小代表不是真正的 $\ker(C+D)$ 向量，其原残量也全部落在指定高旗中；这足以在同一个完整 forcing 空间上证明
$$
P_{\mathcal M_q}p(D^*)i_0=P_{\mathcal M_q}i_0p(-C^*).
\tag{0.1}
$$
由真正平方自由创建列的正交性，得到整个 joined forcing Gram 的上界
$$
i_0^*P_{\mathcal M_q}i_0\le
\left[\sum_{j=0}^{h-1}
\frac{(C^*)^jC^j}{(j!)^2e_j(b^2)}\right]^{-1}.
\tag{0.2}
$$
同一结论同时适用于真正有限核、完整核以及同一个 joined／完整物理 gap。全部高旗和全部零源均保留；没有先假设 forcing Gram 可逆，也没有把 (0.2) 反向用作原返回逆的上界。

依据：
[真实 joined 递减闭空间](../notes/2026-11-14-physical-joined-decreasing-projections-and-fixed-test-bare-budget-789f-next.md) §§1–3；
[物理夹逼及同一增量三费](../notes/2026-11-14-physical-joined-sandwich-and-same-increment-three-fee-fixed-test-budget-789f-next.md) §§1–4；
[强位并头及同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
[实际固定源正删除 Gram](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md)。

## 1. 原物理空间、残量高旗及闭和

令 $\mathfrak h$ 为有限维原物理头空间，$C\in\mathcal B(\mathfrak h)$ 且 $C^h=0$，其中整数 $h\ge1$。原模型可取
$$
C=A_m,\quad h=2^m,
$$
或取真正强位并头
$$
C=A_m+D_<,\qquad h=2^m+R,\qquad x=m+R.
$$
后者的 $R$ 个强平方自由位全部仍在 $\mathfrak h$，不被删成标量权或对称试探源。

在远尾平方自由 Fock 空间
$\mathcal F_{\rm hc}=\bigoplus_{p\ge0}\mathcal H_p$ 上取
$$
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2}.
$$
写
$$
\mathcal H=\mathfrak h\otimes\mathcal F_{\rm hc},\quad
\mathcal L=C+D,\quad
\mathcal K=\ker\mathcal L,\quad
\mathcal K_t=\mathcal K\cap\mathcal H_{\le t}.
$$
头和尾上的单位张量省略。$\sum b_i<\infty$，所以 $D,C,\mathcal L$ 在整个 $\mathcal H$ 上有界。

对整数 $q\ge0$，置
$$
\mathcal H_{{\rm hi},q}
=\mathfrak h\otimes\bigoplus_{p\ge q+2}
\bigl(\ker D^{p-q-1}\cap\mathcal H_p\bigr),\quad
Q_q=P_{\mathcal H_{{\rm hi},q}^{\perp}}.
\tag{1.1}
$$
若 $y_p\in\ker D^{p-q-1}$，则
$Dy_p\in\ker D^{p-q-2}$；在 $p=q+2$ 的最底端，$Dy_p=0$。因此高旗在 $D$ 下不变；它张量全部头，所以在 $C,C^*$ 下均不变。

原 joined 闭空间准确为
$$
\boxed{\mathcal M_q=\mathcal K+\mathcal H_{{\rm hi},q}
=\ker(Q_q\mathcal L).}
\tag{1.2}
$$
这里第一个加号是已经闭合的代数和，不是未经证明的闭包约定。为明确多 Jordan 块的强头也适用，复述闭和证明：在正交商上令
$\delta_q=Q_qD|_{\mathcal H_{{\rm hi},q}^{\perp}}$。其幂满足
$\delta_q^j=Q_qD^j|_{\mathcal H_{{\rm hi},q}^{\perp}}$。
对 $C$ 的任一长度 $\ell\le h$ Jordan 块，商核由首头
$f\in\ker\delta_q^\ell$ 唯一给出。若 $f_p$ 的孔数 $p>q+\ell$，商最小代表条件和
$\delta_q^\ell f_p=0$ 一起迫使
$f_p\in\ker D^{p-q-1}$ 且与该空间正交，因此 $f_p=0$；在其余层有 $D^\ell f_p=0$。所以这个首头本身属于完整 $\ker D^\ell$，用完整 $D$ 的有限 Jordan 链给出 $\mathcal K$ 中的提升。逐块相加得到 (1.2)，右边是有界算子的核，故和闭合。

同一证明还给
$$
\operatorname{supp}\bigl(P_{\mathcal M_q}i_0g\bigr)
\subseteq[0,q+h],
\tag{1.3}
$$
其中 $i_0g=g\otimes\Omega$ 为远尾真空嵌入。原因是 $i_0g\perp\mathcal H_{{\rm hi},q}$，且高旗包含于 $\mathcal M_q$，所以其投影就是商核的物理最小代表。该代表准确保原右侧头旗、短核旗、两个端点以及全部内部零源。

$\mathcal M_q$ 在 $C,D$ 下不变：例如
$Q_q\mathcal L Dz=0$ 来自 $\mathcal Lz\in\mathcal H_{{\rm hi},q}$、
$D\mathcal H_{{\rm hi},q}\subseteq\mathcal H_{{\rm hi},q}$，$C$ 同理。每个 $\mathcal K_t$ 也在 $C,D$ 下不变，因为 $D$ 降孔、$C$ 保孔，二者均与 $\mathcal L$ 交换。

## 2. joined 残量被同一个低端 forcing 准确杀掉

设
$$
P_{\rm M}=P_{\mathcal M_q},\qquad Z_{\rm M}=P_{\rm M}i_0.
$$
对任意 $z\in\mathcal M_q$，有 $\mathcal Lz\in\mathcal H_{{\rm hi},q}$，因此
$$
\langle\mathcal Lz,i_0g\rangle=0,\qquad
P_{\rm M}(C^*+D^*)i_0=0.
\tag{2.1}
$$
这不是声称 $\mathcal Lz=0$。在原 joined 商中必须保留的高返回，恰由这个低端 forcing 的正交性处理。

因 $\mathcal M_q$ 在 $D,C$ 下不变，
$$
P_{\rm M}D^*=P_{\rm M}D^*P_{\rm M},\qquad
P_{\rm M}C^*=P_{\rm M}C^*P_{\rm M}.
\tag{2.2}
$$
再用 $C^*i_0=i_0C^*$，(2.1)–(2.2) 给
$$
(P_{\rm M}D^*|_{\mathcal M_q})Z_{\rm M}
=-Z_{\rm M}C^*.
$$
迭代得到对每个整数 $j\ge0$ 的准确恒等式
$$
\boxed{P_{\rm M}(D^*)^ji_0
=(-1)^jZ_{\rm M}(C^*)^j.}
\tag{2.3}
$$
所以 (0.1) 对所有多项式成立。这里没有把 $C^*$ 换成 $C$；它作用的是同一个原头 forcing。因 $C^h=0$，$j\ge h$ 时两边都为零。此处没有 $j\le q$ 的限制。

真正有限核 $\mathcal K_t$ 以及完整核 $\mathcal K$ 的残量为零，且均保持 $C,D$，因此同一证明给
$$
\boxed{P_{\mathcal K_t}(D^*)^ji_0
=(-1)^j(P_{\mathcal K_t}i_0)(C^*)^j,}
\tag{2.4}
$$
完整核也同样成立。

令
$$
P_{\rm g}=P_{\mathcal M_q}-P_{\mathcal K_{q+h}},\quad
Z_{\rm g}=P_{\rm g}i_0.
$$
因 $\mathcal K_{q+h}\subseteq\mathcal M_q$，$P_{\rm g}$ 是真实正交投影。将 (2.3) 与 (2.4) 相减，得到
$$
\boxed{P_{\rm g}(D^*)^ji_0=(-1)^jZ_{\rm g}(C^*)^j.}
\tag{2.5}
$$
这个结论是同一个物理 forcing 的投影恒等式，不需要假设 gap 空间在 $D$ 下不变。尤其不能由它删掉原 $K/{\rm gap}$ 交叉；准确的一阶式是
$$
P_{\rm g}D^*Z_{\rm g}
=-Z_{\rm g}C^*-P_{\rm g}D^*(P_{\mathcal K_{q+h}}i_0).
\tag{2.6}
$$
最后一项仍是实际核反馈。

## 3. 全部 coherent 创建列同时给出正交行预算

定义
$$
\sigma_j^2=\|(D^*)^j\Omega\|^2
=(j!)^2e_j(b^2),\qquad \sigma_0=1.
\tag{3.1}
$$
这里
$$
(D^*)^j\Omega
=j!\sum_{|I|=j}\Bigl(\prod_{i\in I}b_i\Bigr)e_I
$$
是在原平方自由尾空间中的真正创建列。因为原无限尾每个 $b_i>0$ 且 $b\in\ell^2$，每个有限 $j$ 的 $\sigma_j$ 有限且严格为正。

对 $0\le j<h$ 令
$$
I_j=\sigma_j^{-1}(D^*)^ji_0:\mathfrak h\longrightarrow\mathcal H.
$$
每个 $I_j$ 是等距映射，其像位于不同孔层，故这些像彼此正交。于是
$$
I_{\rm coh}=(I_0,\ldots,I_{h-1}):
\mathfrak h^{\oplus h}\longrightarrow\mathcal H
$$
是一个等距映射，$P_{\rm coh}=I_{\rm coh}I_{\rm coh}^*$ 为真正物理正交投影。

取 $P$ 为 $P_{\rm M},P_{\mathcal K_t},P_{\mathcal K}$ 或 $P_{\rm g}$ 中任一个，记
$$
Z=Pi_0,\qquad G=Z^*Z=i_0^*Pi_0.
$$
由 (2.3)–(2.5)，
$$
PI_j=(-1)^j Z(C^*)^j/\sigma_j.
$$
置头空间上的严格正算子
$$
\boxed{H_{\rm coh}
=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{\sigma_j^2}
=I+\sum_{j=1}^{h-1}\frac{(C^*)^jC^j}{(j!)^2e_j(b^2)}.}
\tag{3.2}
$$
完整正交行给
$$
\boxed{Z H_{\rm coh}Z^*
=PP_{\rm coh}P\le P\le I.}
\tag{3.3}
$$
因此 $\|ZH_{\rm coh}^{1/2}\|\le1$，等价于
$$
H_{\rm coh}^{1/2}G H_{\rm coh}^{1/2}\le I.
$$
只对本来严格正的 $H_{\rm coh}$ 作合同，得到
$$
\boxed{0\le G\le H_{\rm coh}^{-1}.}
\tag{3.4}
$$
这个方向不需要 $G$ 可逆；其真实核和全部 source nuisance 没有被剔除后假作单位。

另一个保完整残余的精确式为
$$
\boxed{G-GH_{\rm coh}G=Z^*(I-P_{\rm coh})Z\succeq0.}
\tag{3.5}
$$
它表明 coherent 列之外的横向物理分量仍然保留，本文没有把 (3.4) 升为等式或双侧比较。

由 $j!e_j(b^2)\le(\sum_i b_i^2)^j$，若 $S=\sum_i b_i^2$，则
$$
H_{\rm coh}\succeq
H_{\rm bos}:=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{j!S^j},
$$
从而
$$
G\le H_{\rm coh}^{-1}\le H_{\rm bos}^{-1}.
\tag{3.6}
$$
新增适用对象是完整 joined／gap forcing Gram；推导始终在原硬核空间进行，没有将 joined 向量冒充完整 bosonic 真核。

## 4. joined 与完整核的共同交叉也保留

在同一个 $q$ 上置
$$
G_{\rm M}=i_0^*P_{\mathcal M_q}i_0,\quad
G_{\rm K}=i_0^*P_{\mathcal K_{q+h}}i_0,\quad
G_{\rm g}=G_{\rm M}-G_{\rm K}.
$$
由于两个物理投影嵌套，
$$
(Z_{\rm M},Z_{\rm K})^*(Z_{\rm M},Z_{\rm K})
=\begin{pmatrix}G_{\rm M}&G_{\rm K}\\G_{\rm K}&G_{\rm K}\end{pmatrix}.
$$
将同一个 $I-P_{\rm coh}$ 置于两列之间，得到实际正块
$$
\boxed{
\begin{pmatrix}G_{\rm M}&G_{\rm K}\\G_{\rm K}&G_{\rm K}\end{pmatrix}
-
\begin{pmatrix}G_{\rm M}\\G_{\rm K}\end{pmatrix}
H_{\rm coh}
\begin{pmatrix}G_{\rm M}&G_{\rm K}\end{pmatrix}
\succeq0.}
\tag{4.1}
$$
对共同差列作合同给
$G_{\rm g}-G_{\rm g}H_{\rm coh}G_{\rm g}\succeq0$，与 (3.4) 的 gap 版本一致。这没有用两个分别比较的 Gram 做不可交换乘法，也没有从两条 Loewner 上界相减。

这些投影空间均被原加权交换保持。因此固定源正删除 Gram 定理也真实适用于 $Z_{\rm M}$、$Z_{\rm K}$、$(I-P_{\rm M})i_0$。对 gap 使用两正交缺陷
$$
i_0-Z_{\rm g}=(I-P_{\rm M})i_0+P_{\mathcal K_{q+h}}i_0,
\quad G_{\Delta,{\rm g}}=I-G_{\rm g},
$$
同一已付完整行给
$$
\sum_{i\ge x}\frac1{i+1}
E_iZ_{\rm g}G_{\Delta,{\rm g}}^\dagger Z_{\rm g}^*E_i^*
\le\frac83I.
\tag{4.2}
$$
(2.5) 允许在这个确切固定源家族中作 $p(-C^*)$ 的共同右合同；度量必须同时变为
$p(-C^*)^*G_{\Delta,{\rm g}}p(-C^*)$。不能另取一个未经支付的环境头逆范数。

## 5. 原两个右端 Riesz 源的具体含义

沿原完整源定义，记 $U_q$ 为真实左最小列，
$L_q=U_q^*U_q$，$B_q=J_{b,q}^*J_{b,q}$，
$H_q=J_{f,q}^*J_{f,q}$。此处 $H_q$ 是普通完整右费，与 (3.2) 的 $H_{\rm coh}$ 不同。

对支持于孔层 $\le q$ 的物理 forcing $F$，原两端源为
$$
s_b[F]=(L_q+B_q)^{-1}U_q^*F,\qquad
s_f[F]=(L_q+H_q)^{-1}U_q^*F.
\tag{5.1}
$$
所有逆按已付的原共同源与自然闭形式解释。为区分非零源链和完整投影，令
$$
\mathcal T_b s=(U_qs,-J_{b,q}s),\qquad
\mathcal T_f s=(U_qs,-J_{f,q}s),
$$
左右分块分别是 $\le q$ 与 $>q$ 的物理孔层。完整 Riesz 代表准确为
$$
\boxed{
P_{\mathcal M_q}F=P_{\mathcal K_q}F+\mathcal T_b s_b[F],\qquad
P_{\mathcal K_{q+h}}F=P_{\mathcal K_q}F+\mathcal T_f s_f[F].}
\tag{5.1a}
$$
因此两者保留同一个完整左零源分量；$\mathcal T_b s_b$ 或 $\mathcal T_f s_f$ 单独不等于完整物理投影。其余右零源已由各自真正右最小列的物理正交性处理。

若多项式 $p$ 的次数 $\le q$，那么 $p(D^*)i_0g$ 仍是一个合法低端 forcing；(2.3)–(2.5) 以及 $\mathcal K_q$ 的同式同时给
$$
\boxed{
s_b[p(D^*)i_0g]=s_b[i_0p(-C^*)g],\qquad
s_f[p(D^*)i_0g]=s_f[i_0p(-C^*)g].}
\tag{5.2}
$$
故原差源 $s_b-s_f$、原 bare 链和原完整右链，都是在各自不变的真实映射后接同一个 forcing 右合同。这里没有重新挑选一个便宜右原像。

(2.3) 本身没有次数限制，但若 $\deg p>q$，输入可能落到右侧，此时不能继续把其 Riesz 功能写成仅 $U_q^*F$ 的 (5.1)。这是 source 同余与原低端 source 公式之间必须保留的限定。若将本稿放回原总孔截止 $Q$ 的强位并头流，还须保持原 $q+h+R\le Q$ 等实际内部窗口条件；本稿没有放宽它们。

## 6. 无限尾、有限尾及尚未支付的返回

原连续尾下 $D$ 在全孔空间有界；高旗、所有核、joined 和以及本文全部正交投影都在同一物理 Hilbert 空间中。每个多项式和 $j<h$ 的创建列均处于整个自然域，本文没有调用全孔 $D^\dagger$ 的有界性。$\sigma_j$ 的级数是非负平方和，有限位置截断后单调收敛到 (3.1)；无需假定不同截断的核投影范数收敛来证明 (2.3)–(3.5)。

对于有限尾，若位数至少 $h-1$，全部公式原样成立。位数较少时，只将 (3.2) 求和于 $\sigma_j>0$ 的项；其余创建列为零，而 (2.3) 仍给相应 $Z(C^*)^j=0$。零次项始终是 $I$。这里只断言这些原有界模型；不把仅有 $b\in\ell^2$ 的全孔无界删除当作同一个有界设定。

本稿已经为真实 joined／gap 的低端创建 forcing 支付共同源身份和 Gram 上界。然而实际帽返回仍包含
$$
P_{\widehat{\mathscr E}}K_{\rm amb}^{-*}
P_{\mathscr E}q_h(-\mathbb T)^*P_{\mathscr E}Y_f.
$$
其中完整 $\mathscr E$ 上的最小化不能由 (3.4) 替换；一般不能把它当作 $Z_{\rm g}$ 后接一个头源矩阵，也不能用 (2.6) 删掉核反馈。因此 (0.2) 不提供 $G_{\rm g}^{-1}$、完整返回 Schur 逆或 ordinary 右费的上界。原同一个实际来源的混合返回和两端部分和仍须继续支付。
