# 原两边界模型的五坐标联合图反例及平方来源域的严格边界

日期：2026-11-27（台北时间 UTC+8）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return、literature_deddens；AI-assisted GPT-6 Astra Pro。

**状态：以下原 N/Y 算子的有限支撑反例和实际联合图来源已证明。它们排除无条件的联合图 carry 估计，并不属于未解决的非零 $W$ 来源，不排除对同一真实 $w\in W$ 的额外估计，未证明 $N=M$。**

两条独立推导在同一个五坐标构造上合并：先用两个单缺位向量消去纯创建顶行，再用三个双缺位向量准确消去实际 carry 的主行。所有剩余真实 carry 与 Cayley 逆都保留。输入的物理孔数趋于无穷，绝不以固定低孔模型代替原空间。

## 1. 准确结论和已付输入

沿用原 $S=B^*$、$a_j=(j+1)^{-2}$、$D^*=\sum_j a_jE_j^*$、$K_\bullet=T_\bullet^*-D^*$，以及
$$
\eta_j=\alpha_{j+1}/\alpha_j,
\qquad b_0=\eta_0,\qquad b_q=a_{q-1}\eta_{q-1}\quad(q\ge1),
$$
$$
\|h\|_{\mathcal C_2}^2=\sum_{q\ge0}b_q^2\|P_qh\|^2.
$$
$P_q$ 是整个首零位块；$\mathsf P_p$ 是整个总物理孔层。原权满足
$$
\eta_{j+1}\le\eta_j/4,\qquad \eta_{j+1}\le\eta_j^2,
\qquad \eta_j\longrightarrow0.
\tag{1.1}
$$

使用以下已有完整结果：

- [规范来源 carry 范数及总孔核心](../results/R271-appendix-canonical-source-carry-norm-total-hole-core.md)给出
  $$
  \|K_N h\|\le3\sqrt2\,\|h\|_{\mathcal C_2},
  \qquad
  N_i^*P_q=(\alpha_q/\alpha_i)V_{iq}\quad(i<q),
  \tag{1.2}
  $$
  其中全部降首零位列正交；$i>q$ 的保首零位余项范数总和至多 $s_q=\sum_{i>q}a_i\eta_i$。
- [Y carry 首缺位行和及整个平方源图核心](R271-appendix-y-carry-first-gap-row-domain-and-common-square-source-core.md)给出准确分解
  $$
  K_Y=-V_b+R_b,\qquad V_b=\sum_{q\ge1}b_qE_q^*P_q,
  \qquad\|R_b\|_{\mathcal C_2\to\mathcal H}\le12.
  \tag{1.3}
  $$
  本稿 §5 还由同一完整 Cayley 账本证明所需的渐近细化。

**定理 1.1。** 对每个 $\bullet=N,Y$，存在每个仅含五个原坐标的有限支撑向量 $h_q^\bullet$，使
$$
\frac{\|h_q^\bullet\|_{\mathcal C_2}}{b_q}\longrightarrow1,
\qquad
\frac{\|T_\bullet^*h_q^\bullet\|+\|Sh_q^\bullet\|}{b_q}
\longrightarrow0,
\tag{1.4}
$$
而
$$
\frac{\|K_Nh_q^N\|}{b_q}\longrightarrow1,
\qquad
\frac{\|K_Yh_q^Y\|}{b_q}\longrightarrow\sqrt2.
\tag{1.5}
$$
因而不存在有限常数 $C$，使对全部有限支撑 $h$ 有
$$
\|K_\bullet h\|\le C\bigl(\|T_\bullet^*h\|+\|Sh\|\bigr),
\tag{1.6}
$$
也不存在以同一个右端控制 $\|h\|_{\mathcal C_2}$ 的无条件估计。

这与旧的单独纯 $D^*$ 相对反例不同：(1.4) 的两个小输出都是**实际** $T_\bullet^*$ 与原 $S$ 的输出。

## 2. 五个原坐标和三个双缺位列

取整数 $q\ge2$、$m\ge q+3$，置 $A=2^m-1$，并记
$$
e^j=e_{A-2^j},\qquad
 e^{i,j}=e_{A-2^i-2^j}\quad(i\ne j).
\tag{2.1}
$$
它们分别在前 $m$ 位中只有一个、两个缺位；物理孔数分别是 $m-1,m-2$。令 $k=q-1$、$r=q+1$，以及
$$
\boxed{
 v_q=\frac{e^{k,q}}{2a_q}
      +\frac{e^{k,r}}{2a_r}
      -\frac{a_k}{2a_qa_r}e^{q,r}.
}
\tag{2.2}
$$
用 $D_{<m}^*=\sum_{j<m}a_jE_j^*$ 表示纯创建的前 $m$ 位部分。直接逐列计算给
$$
D_{<m}^* e^{i,j}=a_ie^j+a_je^i,
\qquad
\boxed{D_{<m}^*v_q=e^k.}
\tag{2.3}
$$
两个非目标单缺位行的系数分别准确相消，目标行的两项各为 $1/2$。

置 $C_q=3(q+2)^2$。三个来源坐标两两正交，(2.2) 的显式系数立即给
$$
\|v_q\|\le C_q,
\qquad
\|v_q\|_{\mathcal C_2}\le b_{q-1}C_q,
\qquad
\|Sv_q\|\le\alpha_{q-1}C_q.
\tag{2.4}
$$
这里三个来源的首零位均不小于 $q-1$，只出现 $q-1,q$ 两个首零位块。

对任何支撑于 $\{0,\ldots,2^m-1\}$ 的 $z$，尾创建的不同最高位输出彼此正交，因此
$$
\left\|\sum_{j\ge m}a_jE_j^*z\right\|
=\sigma_m\|z\|,
\qquad
\sigma_m^2=\sum_{j\ge m}(j+1)^{-4}
\le\frac1{3m^3}.
\tag{2.5}
$$
这是整个真实无限纯尾的范数，没有将它置零。

## 3. N 型准确主 carry 和全部余项

由于 $e^q$ 的首零位为 $q$，(1.2) 中 $i=q-1$ 的准确输出是
$$
a_{q-1}N_{q-1}^*e^q=b_qe^{q-1}.
\tag{3.1}
$$
更低的 $i<q-1$ 输出、以及所有 $i>q$ 的保首零位 carry 均保留。它们给与 $m$ 无关的估计
$$
\left\|b_q^{-1}K_Ne^q-e^{q-1}\right\|
\le \frac{\alpha_q}{b_q}\sum_{i<q-1}\frac{a_i}{\alpha_i}
    +\frac{s_q}{b_q}
\longrightarrow0.
\tag{3.2}
$$
确实，$\alpha_q/b_q=q^2\alpha_{q-1}$，故第一项至多
$$
\frac{\pi^2}{6}q^2\eta_{q-2}\longrightarrow0.
$$
第二项至多
$$
\frac{\pi^2}{6}q^2\frac{\eta_{q+1}}{\eta_{q-1}}
\le\frac{\pi^2}{6}q^2\eta_{q-1}^{3}\longrightarrow0.
$$
另外
$$
\|K_Ne^{q+1}\|\le3\sqrt2\,b_{q+1},
\qquad
\frac{b_{q+1}}{b_q}\le\eta_{q-1}\longrightarrow0.
\tag{3.3}
$$
所以，对任何有界标量族 $c_q$，准确有
$$
\left\|b_q^{-1}K_N(e^q-c_qe^{q+1})-e^{q-1}\right\|
\longrightarrow0
\tag{3.4}
$$
且收敛对全部 $m\ge q+3$ 一致。由 (1.2)、(2.4)，
$$
\|K_Nv_q\|\le3\sqrt2\,b_{q-1}C_q\longrightarrow0.
\tag{3.5}
$$

现在令
$$
c_q^N=\frac{a_q}{a_{q+1}},
\qquad
\boxed{h_q^N=e^q-c_q^Ne^{q+1}-b_qv_q.}
\tag{3.6}
$$
这些标量有界，且
$$
D_{<m}^*(e^q-c_q^Ne^{q+1})=0,
\qquad
D_{<m}^*h_q^N=-b_qe^{q-1}.
\tag{3.7}
$$
式 (3.4)--(3.5) 因而证明
$$
\left\|b_q^{-1}K_Nh_q^N-e^{q-1}\right\|\longrightarrow0.
\tag{3.8}
$$
实际 $T_N^*$ 的主项正与 (3.7) 相消；全部余项的范数为 $o(b_q)+\sigma_m\|h_q^N\|$。

## 4. 真实 $S$ 输出、平方源范数和头长的选择

对任一有界 $c_q$，令 $h_q=e^q-c_qe^{q+1}-b_qv_q$。原 $S$ 的基向量权就是其首零位权，因此
$$
\frac{\|Sh_q\|}{b_q}
\le (1+|c_q|)\frac{\alpha_q}{b_q}+\alpha_{q-1}C_q
=\bigl[(1+|c_q|)q^2+C_q\bigr]\alpha_{q-1}
\longrightarrow0.
\tag{4.1}
$$
前两个单缺位向量和三个双缺位向量处于不同的总孔层。故它们也在 $\mathcal C_2$ 度量下正交，且
$$
\frac{\|h_q\|_{\mathcal C_2}^2}{b_q^2}
=1+|c_q|^2\left(\frac{b_{q+1}}{b_q}\right)^2
  +\|v_q\|_{\mathcal C_2}^2
\longrightarrow1.
\tag{4.2}
$$
选择
$$
\boxed{m(q)\ge\max\{q+3,\lceil b_q^{-2}\rceil\}.}
\tag{4.3}
$$
实际孔数 $m(q)$ 很大，但每个 $h_q$ 始终只有上述五个有限坐标。$\sigma_{m(q)}/b_q\le b_q^2/\sqrt3\to0$，且 $\|h_q\|$ 一致有界。结合 (3.7)--(3.8)，已完整证明 (1.4)--(1.5) 的 N 型部分。允许进一步增大每个 $m(q)$，因为所有其余上界都对头长一致。

## 5. Y 型保留全 Cayley 后的渐近主项

本节只细化 (1.3) 的已付完整分解，不截掉任何逆。记
$$
\mathcal E=K_Y-K_N+V_b=-(L_1-V_b)+L_2-L_3,
\tag{5.1}
$$
其中
$$
L_1=\sum_{j\ge1}b_jN_j^*,\quad
L_2=\sum_{i\ge0}a_i\eta_iN_i^*N_{i+1}^*,
$$
$$
L_3=\sum_{i\ge0}t_i(I+N_i^*)^{-1}N_{i+2}^*,
\qquad t_i=a_i\eta_i^2\eta_{i+1}.
\tag{5.2}
$$

**引理 5.1。** 整个首零位块上有
$$
\boxed{\varepsilon_q^Y:=\|\mathcal EP_q\|/b_q\longrightarrow0.}
\tag{5.3}
$$

证明分三项进行。

首先，$L_1-V_b$ 的 $j>q$ 部分除以 $b_q$ 至多
$\sum_{j>q}b_j/b_q\to0$。$j<q$ 的部分即使用三角不等式也满足
$$
\frac{\alpha_q}{b_q}\sum_{1\le j<q}\frac{b_j}{\alpha_j}
=q^2\alpha_{q-1}\sum_{1\le j<q}\frac1{j^2\alpha_{j-1}}
\le\frac{\pi^2}{6}q^2\eta_{q-2}\longrightarrow0.
\tag{5.4}
$$

其次，将 $L_2P_q$ 按 $i<q-1$、$i=q-1$、$i=q$、$i>q$ 分开。已付的真实二进位列公式给这四部分除以 $b_q$ 的上界依次为
$$
\frac{\pi^2}{6}q^2\eta_0\eta_{q-2},
\qquad \eta_{q-1}\eta_q,
\qquad \frac{b_{q+1}}{b_q},
\qquad\frac{s_q}{b_q}.
\tag{5.5}
$$
它们全部趋零。这里 $i=q-1$ 使用 $N_q^*$ 先填首缺位、$N_{q-1}^*$ 随后至少跨两道边界的原范数界；$i<q-1$ 使用准确系数 $\alpha_q/\alpha_i$。

最后，对 $L_3$ 的每个固定 $i$，当 $q>i+2$ 时，其规范化块范数至多
$$
\frac{3t_i\alpha_q}{\alpha_{i+2}b_q}
=\frac{3t_i}{\alpha_{i+2}}q^2\alpha_{q-1}\longrightarrow0.
\tag{5.6}
$$
整个 $q$ 族同时由可求和的原账本控制：当 $q\le i+1$、$q=i+2$、$q>i+2$ 时，依次不超过
$$
3\eta_i\eta_{i+1},\qquad
12\eta_i^2,\qquad
27\eta_i^2\eta_{i+1}.
\tag{5.7}
$$
因此按 $i$ 的算子范数级数作支配收敛，$\|L_3P_q\|/b_q\to0$。全部逆仍付原范数 $3$。三部分合并证明 (5.3)。

## 6. Y 型的五坐标修正

原权给 $b_q/a_q\le4\eta_0<1$（$q\ge1$），且 $b_q/a_q\to0$，故以下分母为正，比例一致有界：
$$
c_q^Y=\frac{a_q-b_q}{a_{q+1}-b_{q+1}},
\qquad
\boxed{h_q^Y=e^q-c_q^Ye^{q+1}-b_qv_q.}
\tag{6.1}
$$
对 $u_q=e^q-c_q^Ye^{q+1}$，纯创建顶行与 $V_b$ 顶行准确相等：
$$
D_{<m}^*u_q
=(b_q-c_q^Yb_{q+1})e_A=V_bu_q.
\tag{6.2}
$$
因此从原身份 $T_Y^*=D^*+K_N-V_b+\mathcal E$ 得
$$
T_Y^*u_q
=K_Nu_q+\mathcal Eu_q+\sum_{j\ge m}a_jE_j^*u_q.
\tag{6.3}
$$
(3.4)、(5.3) 给
$$
\left\|b_q^{-1}(K_Nu_q+\mathcal Eu_q)-e^{q-1}\right\|
\longrightarrow0.
\tag{6.4}
$$

对 (2.2) 的三个坐标，$V_b$ 的每个输出纤维至多有两列，故
$$
\|V_bv_q\|\le\sqrt2\,\|v_q\|_{\mathcal C_2}.
$$
连同完整有界余项 (1.3)，
$$
\|K_Yv_q\|\le(12+\sqrt2)b_{q-1}C_q\longrightarrow0.
\tag{6.5}
$$
于是减去 $b_qv_q$ 的真实输出后，(2.3) 正好取消 (6.4) 的主行。配合与 N 型同一个头长选择 (4.3)，
$$
\|T_Y^*h_q^Y\|/b_q\longrightarrow0.
\tag{6.6}
$$
$S$ 输出和 $\mathcal C_2$ 范数已由 (4.1)--(4.2) 统一支付。

另一方面，(5.1)、(6.2)、(6.4)--(6.5) 给
$$
\left\|
 b_q^{-1}K_Yh_q^Y-(e^{q-1}-e_A)
\right\|\longrightarrow0.
\tag{6.7}
$$
两个基向量正交，故极限范数为 $\sqrt2$。这证明定理的 Y 型部分；没有把 $K_Y$ 替为 $K_N$，其额外顶行正是第二个非零极限方向。

## 7. 实际联合图核心中仍有 $\mathcal C_2$ 外的规范来源

反例还给出一个严格的来源域事实，且可以明确辨认其所属子空间。固定任一模型，取趋于无穷的子列 $q_n$，使首零位集合
$$
\{q_n-1,q_n,q_n+1\}
$$
两两不交，并使
$$
x_n=h_{q_n}^\bullet/b_{q_n},\qquad
\|Sx_n\|+\|T_\bullet^*x_n\|\le2^{-n}.
\tag{7.1}
$$
每次仍可加大 $m(q_n)$，令各对物理孔层
$$
\{m(q_n)-2,m(q_n)-1\}
$$
及其升一后的层对也两两不交。相应有限坐标支撑向无穷移出。

在形式坐标层定义
$$
h=\sum_{n\ge1}x_n,
\qquad
y=\sum_{n\ge1}Sx_n,
\qquad f=\sum_{n\ge1}T_\bullet^*x_n.
\tag{7.2}
$$
后两级数在 $\mathcal H$ 中绝对收敛。原 $T_\bullet^*$ 严格向前的逐行三角形式，以及来源支撑向无穷移出，给
$$
Sh=y\in\mathcal H,\qquad
T_\bullet^*h=f\in\mathcal H.
\tag{7.3}
$$
由首零位块的分离和 (4.2)，
$$
\boxed{h\notin\mathcal C_2.}
\tag{7.4}
$$
每个固定 $P_qh$ 此处甚至只有有限坐标。有限部分和 $h^{(n)}=\sum_{j\le n}x_j$ 则满足
$$
Sh^{(n)}\longrightarrow y,
\qquad T_\bullet^*h^{(n)}\longrightarrow f.
\tag{7.5}
$$
所以这个来源已经位于有限来源生成的**实际联合图核心的闭包**中，并非由未付最大域边界凭空产生。原形式除法单射，故 $h$ 正是 $f$ 的唯一规范来源。

由 (7.5)，
$$
\boxed{f\in\overline{\operatorname{Ran}T_\bullet^*}=M^\perp.}
\tag{7.6}
$$
$f\ne0$，因为形式 $T_\bullet^*$ 单射而 $h\ne0$。这明确排除了把 (7.2) 当成未知非零 $W\subset M$ 的来源。

还可看到此图来源中的真实抵消：$D^*$ 严格升一个总孔，而各个 $x_n$ 的两层及升一后的两层互不相交；由 (1.4)--(1.5)，$\|D^*x_n\|$ 分别趋于 $1$ 或 $\sqrt2$。因此形式 $D^*h\notin\mathcal H$，进而
$$
K_\bullet h=f-D^*h\notin\mathcal H.
\tag{7.7}
$$
这里完整 $T_\bullet^*h\in\mathcal H$，但纯项与实际 carry 分别不在 $\mathcal H$，并且有限来源仍已在整个原图中逼近。

## 8. 对真实缺陷路线的准确限制

本稿排除了以下无条件升级：

- 用整个实际联合图范数 $\|T_\bullet^*h\|+\|Sh\|$ 统一控制单独 carry 或 $\mathcal C_2$ 来源；
- 从 $Sh,T_\bullet^*h\in\mathcal H$，甚至从有限来源联合图逼近，自动得到 $h\in\mathcal C_2$；
- 在这些一般来源上，分别要求纯创建和 carry 输出属于 $\mathcal H$。

本稿没有给 $W=M\ominus\overline{BM}$ 的非零向量。对同一 $w\in W$ 的 $u\in\ker K$、$H^*G_{\rm env}u$、$\Gamma(u)$ 以及规范 $h(w)$ 的额外正交性，所有待付费用继续保留。特别，(7.6) 表明此处已经构造的规范输出位于与 $W$ 正交的已知范围中；不得将这一反例用于否定真实 $W$ 专属的来源估计。
