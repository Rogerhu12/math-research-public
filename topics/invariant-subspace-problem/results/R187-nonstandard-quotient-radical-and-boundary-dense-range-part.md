# R187：具体非标准商的稠密根理想与边界的稠密像部分

日期：2026-11-12（UTC）。作者：l2_moments。根代理预留 R187。
状态：完整证明。使用 R185 的具体慢符号，不另外假定任何未知限制的稠密像。

## 1. 固定的具体商与结论

令
$$
S=\sum_{j\ge0}\frac{N_j}{(j+1)^2},\qquad
J=\overline{S\mathcal A}^{\|\cdot\|},
\qquad
\mathcal Q=\mathcal A/J,\qquad b=A+J.
$$
R185 已证明 $J\ne0$、$J\subsetneq I_1$，并且 $A^n\notin J$ 对全部 $n\ge0$ 成立。记商映射为 $q$，置
$$
\mathcal R=I_1/J\subseteq\mathcal Q.
$$

本文证明：

1. 对每个 $n\ge1$，有真代数和等式 $I_1=J+I_n$。
2. $\mathcal Q$ 只有一个字符，$\mathcal R$ 是其无限维根理想，并且
   $$
   \overline{b^n\mathcal Q}=\mathcal R,\qquad
   \overline{\mathcal R^n}=\mathcal R\quad(n\ge1).
   $$
   各闭包均为商范数闭包；$\mathcal R$ 不是零代数，也非幂零代数。
3. 任意连续有限维含幺表示 $\mathcal Q\to M_d(\mathbb C)$ 都等于唯一字符乘 $I_d$。因此 $\mathcal R$ 是 $\mathcal Q$ 唯一的真有限余维闭理想，且唯一字符处没有非零连续点导子。
4. 对 R185 的具体边界核 $M_-=\ker\pi_-(S)$，令
   $$
   N_-=\overline{BM_-}.
   $$
   则
   $$
   \overline{B^nM_-}=N_-\quad(n\ge1),\qquad
   \overline{BN_-}=N_-.
   $$
   $N_-$ 无限维，而且附录 A 证明
   $
   e_0\in N_-\setminus B^nM_-\quad(n\ge1).
   $
   因而每个正阶像均不闭；删去准确的一维根核 $\mathbb C e_0$ 后，得到一个明确的无限维、单射且稠密像的拟幂零边界子商。
5. 这个新子商的归一化 dyadic 幂强趋零，与原 Haar 不变子商的弱极限 $I/2$ 不同；两者之间仍无非零有界交织。
6. 附录 B 给每个固定有限头的有界线性核延拓，并证明 $M_-$、$BM_-$、$N_-$ 的全部有限头投影均满射；延拓常数不一致，不据此推出 $N_-=M_-$。

没有证明 $N_-=M_-$；也没有由原 $H$ 上 $S$ 单射推断所有抽象 $\mathcal Q$ 表示为零。

## 2. 有限 jet 理想与真代数和

先记录不涉及有界除法的准确事实：
$$
I_n=\overline{A^n\mathcal A}^{\|\cdot\|}
=
\{T\in\mathcal A:[z^k]\iota(T)=0,\ 0\le k<n\}.
\tag{2.1}
$$
右边的系数泛函由 R32 连续。

为自含说明反向包含，设 $T$ 的前 $n$ 个系数为零。
取多项式 $p_\ell(A)\to T$ 按范数。
其前 $n$ 个系数各趋零，故从 $p_\ell$ 中删去这些有限项，所得多项式仍按范数趋于 $T$，且每个都含因子 $A^n$。
正向包含直接由系数连续性。这个证明不声称 $T/A^n$ 有界。

$S$ 的形式首项为
$$
\iota(S)(z)=s_1z+\cdots,\qquad s_1=1/d_0\ne0.
$$
给定 $T\in I_1$ 和 $n\ge2$，有限三角递推唯一确定一个次数至多 $n-2$ 的多项式 $p$，使
$$
[z^k]\bigl(\iota(T)-\iota(S)p\bigr)=0
\qquad(0\le k<n).
$$
这里只对有限 jet 作除法，分母是非零标量 $s_1$。
于是
$$
T-Sp(A)\in I_n,\qquad Sp(A)\in J.
$$
结合 $J\subseteq I_1$，得到
$$
\boxed{I_1=J+I_n\qquad(n\ge1).}
\tag{2.2}
$$
$n=1$ 显然成立。
(2.2) 没有在右侧再取闭包，也没有构造 $S$ 的有界形式逆。

## 3. 根理想、各幂稠密与字符 hull

$\mathcal A$ 是由拟幂零 $A$ 生成的交换含幺 Banach 代数，只有一个字符 $\chi$。
因 $J\subseteq I_1=\ker\chi$，它下降为 $\mathcal Q$ 的字符 $\bar\chi$。
任意 $\mathcal Q$ 字符与 $q$ 复合都给 $\mathcal A$ 字符，因此
$$
\boxed{
\Delta(\mathcal Q)=\{\bar\chi\},\qquad
\operatorname{rad}\mathcal Q=\ker\bar\chi=\mathcal R.
}
\tag{3.1}
$$
换言之，$J$ 的 Gelfand hull 只有原代数的那一个点；
这个 hull 不能区分 $J$ 与标准理想。

R185 已证明 $\mathcal A/J$ 无限维，而 $\mathcal R$ 在其中余维1，
所以 $\mathcal R$ 无限维。
另外 $b^n\ne0$ 对所有 $n$，故 $\mathcal R$ 非幂零。

由 (2.2)，
$$
q(I_n)=q(I_1)=\mathcal R.
\tag{3.2}
$$
用 $I_n=\overline{A^n\mathbb C[A]}$：
每个 $\mathcal R$ 元素都可选择一个属于 $I_n$ 的代表，并由 $A^n$ 乘多项式逼近。
所以
$$
\boxed{\overline{b^n\mathcal Q}=\mathcal R\qquad(n\ge1).}
\tag{3.3}
$$
由于 $b^n\mathcal Q\subseteq\mathcal R^n\subseteq\mathcal R$，有
$$
\boxed{\overline{\mathcal R^n}=\mathcal R\qquad(n\ge1).}
\tag{3.4}
$$
这里 $\mathcal R^n$ 表示 $n$ 个根理想元素乘积的有限线性组合。
特别 $\mathcal R=\overline{\mathcal R^2}$，但 $\mathcal R\ne0$。
所有逐有限 jet 可见的正阶信息都已在商中消去，
剩下的范数结构不能由有限阶幂零商检测。

## 4. 所有连续有限维表示都只有字符

设
$$
\rho:\mathcal Q\to M_d(\mathbb C)
$$
连续、含幺，记 $C=\rho(b)$。
$\rho\circ q$ 连续，且 $A$ 拟幂零，所以
$$
r(C)\le r(A)=0.
$$
有限维中 $C$ 因而幂零。

把范数收敛的 $S$ 送入表示，得到
$$
0=\rho(q(S))
=\sum_{j\ge0}\frac{C^{2^j}}{(j+1)^2d_j}.
\tag{4.1}
$$
因 $C$ 幂零，右边实际只有有限项。
它可写成
$$
0=C\left[
d_0^{-1}I+
\sum_{j\ge1}\frac{C^{2^j-1}}{(j+1)^2d_j}
\right].
$$
括号为非零标量 $d_0^{-1}I$ 加一个幂零多项式，故可逆。
所以 $C=0$。

$q(\mathbb C[A])$ 在 $\mathcal Q$ 中范数稠密，
因此
$$
\boxed{\rho(x)=\bar\chi(x)I_d\qquad(x\in\mathcal Q).}
\tag{4.2}
$$

对于非含幺表示，只能在非退化像上作同一陈述。
具体地，$\rho(1)$ 是一个幂等矩阵；
在它的像上表示含幺，故 (4.2) 适用；
在其核上表示为零。
不把一个任意非含幺表示误称为全空间上的字符乘恒等。

### 4.1. 真有限余维闭理想

若 $K$ 是 $\mathcal Q$ 的真有限余维闭理想，则
$\mathcal Q/K$ 的左正则表示有限维、含幺且忠实。
由 (4.2)，这个商只能是一维标量代数。
因此
$$
\boxed{
\mathcal R\text{ 是 }\mathcal Q\text{ 唯一的真有限余维闭理想。}
}
\tag{4.3}
$$
这不是全部闭理想的分类。

### 4.2. 没有非零连续点导子

设连续线性泛函 $d:\mathcal Q\to\mathbb C$ 满足
$$
d(xy)=\bar\chi(x)d(y)+d(x)\bar\chi(y).
$$
则 $d(1)=0$，且 $d$ 在 $\mathcal R^2$ 上为零。
由 (3.4) 和连续性，$d|_{\mathcal R}=0$。
因 $\mathcal Q=\mathbb C1+\mathcal R$，
$$
\boxed{d=0.}
\tag{4.4}
$$
同样，任何把有限 jet 具体实现为有限维矩阵的连续表示都无法看到这个非零根理想。

## 5. 具体边界核上的模结构

沿用 R185：
$$
M_-=\ker T,\qquad T=\pi_-(S),\qquad
B=\pi_-(A).
$$
$M_-$ 是真无限维闭 $B$ 不变空间。
全部 $\pi_-(\mathcal A)$ 保持 $M_-$，且 $J$ 杀掉 $M_-$。
因此
$$
\rho_-:\mathcal Q\to B(M_-),\qquad
\rho_-(q(F))=\pi_-(F)|_{M_-}
\tag{5.1}
$$
是良定义的连续含幺表示。

对每个 $n\ge1$，由 (3.3) 以及 $\rho_-$ 的连续性，
$$
\overline{\rho_-(\mathcal R)M_-}
=\overline{B^nM_-}.
\tag{5.2}
$$
其中左侧取所有像向量线性张成的闭包。
证明两个包含分别如下：

- $b^n\in\mathcal R$，所以 $B^nM_-$ 包含于左边；
- 对任意 $r\in\mathcal R$，取 $b^nq_k\to r$ 按商范数；
  则 $\rho_-(r)x=\lim B^n\rho_-(q_k)x$，属于右边。

令
$$
N_-=\overline{BM_-}.
$$
于是
$$
\boxed{
\overline{B^nM_-}=N_-\quad(n\ge1),\qquad
\overline{BN_-}=N_-.
}
\tag{5.3}
$$
后一式由有界性给
$\overline{B\overline{BM_-}}=\overline{B^2M_-}$。

$N_-$ 无限维。
否则 $B|_{M_-}$ 的像有限维，而其核至多为
$\ker B=\mathbb Ce_0$；第一同构原理会使 $M_-$ 有限维，矛盾。

这已经抽出一个真实的稠密像部分。
仍未证明 $N_-=M_-$，不能把这一步缺口藏在符号里。

## 6. 有限维边界子模与商模的准确限制

R185 的有限头核等式给
$$
M_-\cap\ker B^k=\mathbb Ce_0
\qquad(k\ge1).
\tag{6.1}
$$
所以 $M_-$ 中唯一的非零有限维 $B$ 不变子空间是 $\mathbb Ce_0$：
任何有限维限制拟幂零，最终被某个幂杀掉，再用 (6.1)。

有限维商不同。若 $L\subseteq M_-$ 闭、$B$ 不变且 $M_-/L$ 有限维，
则范数多项式逼近使 $L$ 对全部 $\pi_-(\mathcal A)$ 不变，
从而商上有 (5.1) 的有限维表示。
由 §4，诱导 $B$ 为零，即
$$
\boxed{BM_-\subseteq L,\qquad N_-\subseteq L.}
\tag{6.2}
$$

反向，任何闭 $L$ 满足 $N_-\subseteq L\subseteq M_-$，
都自动为 $B$ 不变；商上的整个 $\mathcal Q$ 作用只是 $\bar\chi$ 乘恒等。
因为 $\mathcal R=\overline{b\mathcal Q}$，根理想的像都落在 $N_-$。

因此 $M_-$ 的有限维连续商模，准确等于 Hilbert 商
$M_-/N_-$ 的有限维商，均为字符模的有限重数。
没有证明这个缺陷空间为零，也没有理由把有限维商的维数限制为1。
§4 的“一维”指有限维**代数商**，与此处的模重数不同。

等价地，任意连续模映射
$M_-\to\mathbb C^d_{\bar\chi}$ 都恰好是一个杀掉 $N_-$ 的有界线性映射。附录 A 的 $e_0\in N_-$ 还说明：所有这些商模都杀掉唯一非零有限维子模 $\mathbb C e_0$。

## 7. 删去唯一根向量后的真实 quasiaffine 子商

附录 A 用可控远块近似预像证明 $e_0\in N_-$。因此准确地置
$
E=N_-\cap\mathbb Ce_0=\mathbb Ce_0,\qquad
\mathscr K=N_-/\mathbb Ce_0.
$
$E$ 恰为一维，故 $\mathscr K$ 仍是无限维 Hilbert 空间。
$B$ 保持 $N_-$ 和 $E$，诱导有界算子
$$
C(x+E)=Bx+E.
\tag{7.1}
$$

**单射性。** 若 $Bx\in E$，则 $B^2x=0$。
又 $x\in N_-\subseteq M_-$，由 (6.1) 有 $x\in\mathbb Ce_0$，
故 $x\in E$。因此 $\ker C=0$。

**稠密像。** 由 (5.3) 的 $\overline{BN_-}=N_-$，取商后得到
$\overline{C\mathscr K}=\mathscr K$。

**拟幂零。** 商范数给
$\|C^n\|\le\|B^n\|=W_n$，故 $r(C)=0$。

综上，
$$
\boxed{
\mathscr K\text{ 无限维},\qquad
C\text{ 单射、值域稠密且拟幂零}.
}
\tag{7.2}
$$
整个 $\mathcal Q$ 也在 $\mathscr K$ 上诱导连续含幺表示，
且 $b$ 的像就是 $C$。这是一条从具体边界无限核中得到的实际子商构造，而非任意存在性模型。

## 8. 归一化幂的强零极限仍阻止 Haar 传输

在整个边界 $\mathscr H_-$ 上，
$$
\frac{B^{2^j}}{d_j}\longrightarrow0\quad\text{强}.
\tag{8.1}
$$
因为这些算子范数均为1，并且对每个有限支持向量最终严格为零。
限制到 $N_-$ 再取 Hilbert 商，给
$$
\boxed{
\frac{C^{2^j}}{d_j}\longrightarrow0\quad\text{强},
\qquad
\left\|\frac{C^{2^j}}{d_j}\right\|\le1.
}
\tag{8.2}
$$

另一方面，R140 的任意非零原 Haar 不变子商 $Q_0$ 上，
其诱导算子 $A_{Q_0}$ 满足
$$
\frac{A_{Q_0}^{2^j}}{d_j}\longrightarrow\frac12I_{Q_0}
\quad\text{弱}.
\tag{8.3}
$$
这可用 $M\ominus N$ 代表子商并压缩原来的弱极限得到；
不要求代表空间本身在全部原算子下不变。

若有有界交织 $K:Q_0\to\mathscr K$，则
$$
K\frac{A_{Q_0}^{2^j}}{d_j}
=\frac{C^{2^j}}{d_j}K.
$$
左边弱趋 $K/2$，右边强趋零，故 $K=0$。
逆方向的有界交织同样为零：
左边由 (8.2) 强趋零，右边由 (8.3) 弱趋 $K/2$。

所以
$$
\boxed{
\operatorname{Int}(A_{Q_0},C)
=\operatorname{Int}(C,A_{Q_0})=\{0\}.
}
\tag{8.4}
$$
同一证明适用于有限放大。
即使边界已抽出与原模型一样单射稠密的部分，
归一化幂的拓扑行为仍阻止这类有界传输。

## 9. 对原 Haar 空间能够及不能够说什么

若指定某个非零闭 $A$ 不变 $M\subseteq H$，
并要求其实际限制表示
$$
F\longmapsto F|_M
$$
经 $\mathcal Q=\mathcal A/J$ 分解，则必有 $S|_M=0$。
R185/R122 的原全空间单射性迫 $M=0$，矛盾。
因此这种**指定的实际限制表示**不能经过 $\mathcal Q$。

这不意味着所有抽象 $\mathcal Q\to B(H)$ 表示都为零；
字符表示已经是非零例子，§7 还给无限维表示。
也不自动排除某个原 Haar 不变子商让 $S$ 的诱导作用为零：
那会涉及未知限制上的稠密像或饱和性，不能由全空间单射直接推出。

本稿保留的具体问题是：
$$
\text{对 }M_-=\ker\pi_-(S)，\quad
\overline{BM_-}\overset{?}=M_-.
$$
已经严格完成的替代是 (5.3)、(7.2)：
所有正次幂有同一闭像，并可从中抽出单射稠密的无限维边界子商。

原 $H$ 的一般不变子空间及完整 ISP 仍未解决。


## 附录 A：真空属于各阶闭像，但不属于任何实际正阶像

以下统一处理 R185 的 $\sum a_j\mathsf N_j$ 与 R188 的 $\sum a_j\mathsf Y_j$，给出 §1、§7 所用的精确加强。

### A.1. 同时处理两个已经完整构造的算子

沿用负整数边界表示的记号

$$
B e_0=0,\qquad B e_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),
$$

$$
\mathsf N_j=\frac{B^{2^j}}{d_j},\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},
\qquad a_j=(j+1)^{-2}.
$$

分别取

$$
T=\sum_{j\ge0}a_j\mathsf N_j
\quad\text{或}\quad
T=\sum_{j\ge0}a_j\mathsf Y_j,
\qquad M=\ker T.
\tag{A.1.1}
$$

两个级数均按算子范数绝对收敛。R185、R188 已对每一种情形证明：

- $M$ 为无限维闭 $B$ 不变空间；
- 对每个 $k\ge1$，$M\cap\ker B^k=\mathbb C e_0$；
- 有限头近核向量可用后续远块递归改造成真核向量，同时永久保留其已有全部有限头坐标；
- 对 $N=\overline{BM}$，R187 给
  $$
  \overline{B^kM}=N,\qquad \overline{BN}=N
  \quad(k\ge1).
  \tag{A.1.2}
  $$

这里证明额外的具体信息：

$$
\boxed{
e_0\in N,\qquad e_0\notin B^kM\quad(k\ge1).
}
\tag{A.1.3}
$$

因而 $B|_M$ 的值域确实不闭；R187 中的
$E=N\cap\mathbb C e_0$ 在这两个具体例子里准确等于 $\mathbb C e_0$。

### A.2. 一个可直接控制 B 像的初始模型核

取大整数 $L\ge256$，使用块 $[L,2L)$。记

$$
\sigma_L^2=\sum_{i=L}^{2L-1}a_i^2,\qquad
h_L=\frac1{\sigma_L^2}
       \sum_{i=L}^{2L-1}a_i e_{2^i}.
\tag{A.2.1}
$$

块中的纯消去算子
$D_L=\sum_{i=L}^{2L-1}a_i\mathsf E_i$
满足

$$
D_Lh_L=e_0,\qquad \|h_L\|=\sigma_L^{-1}.
$$

因为该块有 $L$ 个指标，且
$(2L)^{-2}\le a_i\le(L+1)^{-2}$，

$$
\frac1{16L^3}\le\sigma_L^2\le\frac1{L^3},
\qquad
L^{3/2}\le\sigma_L^{-1}\le4L^{3/2}.
\tag{A.2.2}
$$

置

$$
V_L=e_1-h_L,\qquad
Q_L=1+4L^{3/2}.
\tag{A.2.3}
$$

最低有限头上，两种 $T$ 都满足

$$
T_{\rm head}e_1=e_0,\qquad T_{\rm head}e_0=0,
$$

因为 $a_0=1$、$\mathsf N_0e_1=e_0$，
而 $\mathsf N_0^2e_1=0$ 也给
$\mathsf Y_0e_1=e_0$。
因此低头与远块之间放空 gap 后，

$$
(T_{\rm head}\otimes I+I\otimes D_L)V_L=0.
\tag{A.2.4}
$$

这只是两项有限模型恒等式；尚未把实际进位误差忽略。

R185 的空 gap 估计及 R188 的 Cayley 逆差估计分别给
$4\eta_{L-1}$、$26\eta_{L-1}$ 的模型误差上界。
统一使用较大的常数，得到

$$
\|TV_L\|\le26\eta_{L-1}\|V_L\|,
\qquad \|V_L\|\le Q_L.
\tag{A.2.5}
$$

### A.3. 从近核到真核：归一化后调用已经证明的递归

令

$$
v_L=V_L/Q_L,\qquad m=2L.
$$

则 $v_L$ 属于有限头 $\mathscr F_m$，范数不超过1，并且

$$
\|Tv_L\|\le26\eta_{L-1}
\le26\exp\!\left(-\frac{770}{16}16^L\right)
\le\exp(-40\,4^m).
\tag{A.3.1}
$$

最后一步对 $L\ge256$ 有充分余量；其比较是
$770/16=48.125>40$，没有把多项式因子藏入同阶指数。

R185、R188 的递归引理现在可以直接从 $m=2L$ 开始。
每一步实际修正的范数不超过
$\exp(-20\,4^{m_n})$，而 $m_{n+1}=128\,2^{m_n}$。
所以全部后续修正的和不超过

$$
2\exp(-20\,4^m)=2\exp(-20\,16^L).
$$

得到 $z_L\in M$，满足

$$
\|z_L-v_L\|\le2e^{-20\,16^L},
\qquad
P_{\mathscr F_{2L}}z_L=v_L.
\tag{A.3.2}
$$

这里的投影等式来自每一步正阶修正都有至少一个新远块孔，
故全部新增坐标位于旧有限头之外。

放回尺度，令

$$
y_L=Q_Lz_L\in M.
$$

于是

$$
P_{\mathscr F_{2L}}y_L=V_L,\qquad
\|y_L-V_L\|\le2Q_Le^{-20\,16^L}.
\tag{A.3.3}
$$

尤其 $(y_L)_1=1$、$(y_L)_0=0$，而且
$\|y_L\|\asymp L^{3/2}$。这个构造没有给出一致有界的近似逆。

### A.4. B 像趋于真空

边界移位的实际一孔公式是

$$
Be_{2^i}=\alpha_i e_{2^i-1}.
$$

这些输出互相正交。因此

$$
\|Bh_L\|^2
=\frac1{\sigma_L^4}\sum_{i=L}^{2L-1}a_i^2\alpha_i^2
\le\frac{\alpha_L^2}{\sigma_L^2}
\le16L^3\alpha_L^2.
\tag{A.4.1}
$$

由 $Be_1=\alpha_0e_0$、$\|B\|=\alpha_0$ 及 (A.3.3)，

$$
\boxed{
\|By_L-\alpha_0e_0\|
\le4L^{3/2}\alpha_L
  +2\alpha_0Q_Le^{-20\,16^L}
\longrightarrow0.
}
\tag{A.4.2}
$$

所以 $e_0\in\overline{BM}=N$。
再结合 (A.1.2)，得到

$$
\boxed{
e_0\in\overline{B^kM}\quad\text{对每个 }k\ge1.
}
\tag{A.4.3}
$$

这是关于各个固定 $k$ 的闭像结论，不把同一个近似序列声称为全部阶数的统一预像。

### A.5. 没有任何实际正阶预像

若 $B^kx=e_0$ 且 $x\in M$，则

$$
B^{k+1}x=0.
$$

由 $M\cap\ker B^{k+1}=\mathbb C e_0$，有 $x\in\mathbb C e_0$，
但此时 $B^kx=0$，矛盾。因此

$$
\boxed{e_0\notin B^kM\quad(k\ge1).}
\tag{A.5.1}
$$

特别 $BM$ 不闭。对 $k=1$，也可直接检查：
$Bx=\alpha_0e_0$ 迫使 $x=e_1+ce_0$，
而两种 $T$ 都有 $Tx=e_0\ne0$。

这还排除任何一致有界的真核预像序列：
若 $x_n\in M$ 一致有界且 $Bx_n\to e_0$，Hilbert 空间的弱紧性给弱收敛子列，
闭空间 $M$ 中的弱极限 $x$ 将满足 $Bx=e_0$，与 (A.5.1) 矛盾。

### A.6. 对 R187 的准确加强与保留缺口

对两种具体慢算子，R187 的稳定部分现在准确为

$$
N=\overline{BM}\supset\mathbb C e_0,\qquad
\overline{BN}=N.
$$

商空间

$$
\mathcal K=N/\mathbb C e_0
$$

是无限维 Hilbert 空间。$B$ 在其上的诱导算子单射、稠密像、拟幂零；
其归一化高位幂强趋于0。R187 已证明的原 Haar 子商归一化幂弱趋于
$I/2$ 因而继续排除两方向的非零有界交织。

此外，任何连续有限维边界模商都杀掉 $N$，于是必杀掉唯一有限维子模
$\mathbb C e_0$。这不把有限维模商的字符重数误写成1。

仍未证明 $N=M$，也未确定 $M/N$ 是否为零。
这里得到的是具体真空的可控近似预像和所有正阶像不闭；
没有假设一般核向量的尾速率，没有证明一般尾向量的同类近似预像，
也没有在原 Haar 表示中构造不变子空间。


## 附录 B：全部有限头都有统一选择的有界线性核延拓

本附录继续同时适用于附录 A 的两个具体算子 $T$。令
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathscr F_m=\operatorname{span}\{e_n:0\le n<2^m\}.
$$
$P_m$ 为到 $\mathscr F_m$ 的正交投影。

证明对每个固定 $m$ 都存在有界线性映射
$$
J_m:\mathscr F_m\longrightarrow M,\qquad P_mJ_m=I_{\mathscr F_m}.
\tag{B.1}
$$
选择过程全部只依赖 $m$，不依赖输入向量。对 $m\ge2$ 可取
$$
\boxed{\|J_m\|\le2\exp(8m2^m).}
\tag{B.2}
$$
常数允许随头长度迅速增长；不据此作无穷头极限。

### B.1. 固定的线性模型延拓

固定 $m\ge2$，置
$$
d=2^m,\qquad L=64d,\qquad m_0=2L,\qquad
\delta=(32L^3)^{-1/2}.
$$
使用 R185/R188 已构造的同一纯块右逆链
$$
h_0=e_\varnothing,\qquad
D_Lh_k=h_{k-1},\qquad
\|h_k\|\le\delta^{-k}\quad(0\le k<d).
$$
每个 $h_k$ 在块 $[L,2L)$ 上具有准确孔次数 $k$。
右逆和全部 $h_k$ 现在一次固定。

低头实际算子 $T_m=T|_{\mathscr F_m}$ 满足
$$
T_m^d=0,\qquad \|T_m\|\le6.
$$
定义线性映射
$$
\mathcal E_m v
=\sum_{k=0}^{d-1}(-1)^kT_m^kv\otimes h_k
\in\mathscr F_{m_0},
\tag{B.3}
$$
中间 gap 放真空。不同 $k$ 的块次数正交，所以
$$
\|\mathcal E_mv\|^2
\le\sum_{k=0}^{d-1}(6/\delta)^{2k}\|v\|^2.
$$
因此
$$
\|\mathcal E_m\|\le
Q_m:=\sqrt d\,(6/\delta)^{d-1}.
\tag{B.4}
$$
由于 $\delta^{-1}=2^{23/2}d^{3/2}$，取对数得
$$
Q_m\le\exp(8m2^m)\qquad(m\ge2).
\tag{B.5}
$$
例如用 $6\delta^{-1}<2^{15}d^{3/2}$，
右侧对数不超过
$[\tfrac12m+d(15+\tfrac32m)]\log2\le8md$。

$k\ge1$ 的项都有一个新高位孔，故
$$
P_m\mathcal E_m=I_{\mathscr F_m}.
\tag{B.6}
$$
有限模型精确抵消，真实空 gap 误差给
$$
\|T\mathcal E_m v\|
\le26\eta_{L-1}\|\mathcal E_m v\|.
\tag{B.7}
$$

### B.2. 在算子范数中同时改正全部输入

归一化仅用于固定算子的估计：
$$
F_0=\mathcal E_m/Q_m:
\mathscr F_m\longrightarrow\mathscr F_{m_0}.
$$
它不是按输入 $v$ 的范数重新选择参数。由上式，
$$
\|F_0\|\le1,\qquad
\|TF_0\|\le26\eta_{L-1}
\le\varepsilon_{m_0},\qquad
\varepsilon_q=e^{-40\,4^q}.
\tag{B.8}
$$

现在固定全部后续头长度
$$
m_{n+1}=128\,2^{m_n}
$$
及其对应块右逆，并递推
$$
F_{n+1}=\mathcal E_{m_n}F_n.
\tag{B.9}
$$
每一个 $F_n$ 都是同一有限维输入空间 $\mathscr F_m$ 上的线性算子。

R185/R188 的近核修正界对每个输入成立，
因此可以直接取单位球上确界，得到算子范数估计：
若
$\|TF_n\|\le\varepsilon_{m_n}$，则
$$
\|F_{n+1}-F_n\|
\le e^{8m_n2^{m_n}}\varepsilon_{m_n}
\le e^{-20\,4^{m_n}}.
\tag{B.10}
$$
若暂用 $\|F_n\|\le2$，此式先给 $\|F_{n+1}\|\le3$；
真实进位误差再给
$$
\|TF_{n+1}\|
\le78\eta_{64\cdot2^{m_n}-1}
\le\varepsilon_{m_{n+1}}.
\tag{B.11}
$$
另一方面，对 (B.10) 从 $F_0$ 求和，
$$
\|F_{n+1}\|
\le1+\sum_{\ell=0}^n e^{-20\,4^{m_\ell}}<2.
$$
所以临时的范数3只用于证明下一步残差，
全局的范数2又恢复了归纳假设，没有循环估计。

(B.10) 的级数收敛，故 $F_n$ 在算子范数中趋于
$$
F_\infty:\mathscr F_m\longrightarrow H,\qquad
\|F_\infty\|\le2.
$$
由 (B.11) 及 $T$ 有界，$TF_\infty=0$。
后续修正全部在当前头外，因而
$$
P_mF_\infty=P_mF_0=Q_m^{-1}I.
$$
最后令
$$
J_m=Q_mF_\infty.
$$
即得到 (B.1)—(B.2)。$m=0,1$ 可限制 $J_2$，无需另一套递归。

### B.3. B M 的有限头也全部满射

定义有限的精确右移
$$
R_m\left(\sum_{n<2^m}v_ne_n\right)
=\sum_{n<2^m}
\frac{v_n}{\alpha_{v_2(n+1)}}e_{n+1}.
\tag{B.12}
$$
它的像属于 $\mathscr F_{m+1}$，并且
$$
BR_m=I_{\mathscr F_m},\qquad
\|R_m\|\le\alpha_m^{-1}.
\tag{B.13}
$$

置
$$
K_m=BJ_{m+1}R_m:\mathscr F_m\longrightarrow BM.
$$
计算 $P_mB$ 只用输入的第1至第 $2^m$ 个坐标，
都包含于 $\mathscr F_{m+1}$。
因此 $P_{m+1}J_{m+1}=I$ 给
$$
\boxed{
P_mK_m=I_{\mathscr F_m},\qquad
\|K_m\|\le
\frac{2\alpha_0}{\alpha_m}
 \exp\bigl(8(m+1)2^{m+1}\bigr).
}
\tag{B.14}
$$
$m\ge2$ 时按上式，较小 $m$ 仍可由有限限制处理。

于是
$$
\boxed{P_mM=P_m(BM)=P_mN=\mathscr F_m\quad(m\ge0).}
\tag{B.15}
$$

### B.4. 对偶 forward 子模与剩余除法缺口

由 (B.15)，
$$
\boxed{
M^\perp\cap\mathscr F_m
=N^\perp\cap\mathscr F_m=\{0\}
\quad(m\ge0).
}
\tag{B.16}
$$
甚至有量化的严格正有限角：
对 $h\in\mathscr F_m$，
$$
\|P_Mh\|\ge\|J_m\|^{-1}\|h\|,
\qquad
\|P_Nh\|\ge\|K_m\|^{-1}\|h\|.
\tag{B.17}
$$
例如第一式由
$\|h\|^2=\langle J_mh,h\rangle
=\langle J_mh,P_Mh\rangle$
及 Cauchy–Schwarz 得到。

令
$$
\mathcal I=M^\perp=\overline{\operatorname{Ran}T^*}.
$$
因为 $e_0$ 对 $B^*$ 循环且 $T^*$ 与 $B^*$ 交换，
$$
\mathcal I
=\overline{\operatorname{span}\{(B^*)^nT^*e_0:n\ge0\}}.
\tag{B.18}
$$
这是单个真实 forward Hilbert 子模；(B.16) 说明它没有非零有限多项式向量。

另一方面，
$$
N^\perp=(B^*)^{-1}\mathcal I
:=\{h\in H_-:B^*h\in\mathcal I\}.
\tag{B.19}
$$
所以未知问题准确化为
$$
\boxed{
N=M
\ \Longleftrightarrow\
(B^*)^{-1}\mathcal I=\mathcal I.
}
\tag{B.20}
$$
已证明的只是两边都没有非零有限支持向量，
以及全部有限头投影满射；没有证明这个 forward 子模对除以 $B^*$ 饱和。

尤其 (B.2)、(B.14) 的常数随 $m$ 急剧增长。
不能把所有有限 jet 的延拓拼成一个有界全空间延拓，
不能由 (B.15) 得到 $N=M$，
也不能从 $B^*$ 的循环性推出这里的除法核至多一维。
这些是本附录保留的准确无限维缺口。
