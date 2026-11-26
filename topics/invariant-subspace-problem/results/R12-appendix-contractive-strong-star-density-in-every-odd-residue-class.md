# 任意奇数剩余类中的收缩强*多项式密度

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。日期：2026-11-27（台北）。

**状态：完整证明的正向逼近结论。** 固定任意原尾 $B_m$、正奇数 $p$、剩余类 $r\bmod p$。对每个完整交换子 $X\in\mathscr C_m=\{B_m\}'$，存在多项式 $q_n$，使其每个非零次数均属于 $r\bmod p$、最低次数趋无穷，并且
$$
\boxed{
\|q_n(B_m)\|\le\|X\|,\qquad
q_n(B_m)\longrightarrow X\quad\text{强*}.
}
$$
因此从一个指定的模奇数剩余类中，仍能保同一实际输入、普通算子范数与全部完整交换子。$r=0$ 给出 $B_m^p$ 多项式单位球在完整交换子单位球中的强*密度，实质加强此前的有界奇幂恢复。

这个结论不表示任意闭根已经获得全域有界正则化；它仅使用实际有界多项式，在原空间及已经存在的闭图上取强极限。

## 1. 原尾位估计与一个准确收缩平均

沿用[奇幂强恢复稿](R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)的实际归一化位：
$$
N_j=\frac{B_m^{2^j}}{d_j},\qquad d_j=\|B_m^{2^j}\|>0,
\qquad \|N_j\|=1,
$$
$$
\|N_j-E_j\|=\eta_j,\qquad
\eta_j=\frac{\alpha_{m+j+1}}{\alpha_{m+j}}
\le e^{-770\,16^{m+j}}.
\tag{1.1}
$$
特别
$$
C_m:=\sum_{j\ge0}\eta_j
\le\frac{e^{-770\,16^m}}{1-e^{-11550}}
<\frac12.
\tag{1.2}
$$

若 $F$ 含 $L$ 个互异位，则
$$
\left\|\sum_{j\in F}E_j\right\|\le\frac{L+1}{2}.
\tag{1.3}
$$
这里给出有限维证明。按 $F$ 内物理一位数分层，$\sum E_j$ 把第 $a$ 层送到第 $a+1$ 层。这一零一 incidence 矩阵的每个列和为 $L-a$、每个行和为 $a+1$，Schur 不等式给该块的范数至多
$\sqrt{(a+1)(L-a)}\le(L+1)/2$。不同输入层的输出层正交，故全算子范数为这些层块范数的最大值，得到 (1.3)。其他位上张量恒等不改变范数。

定义
$$
T_F=\frac{2}{L+2}\sum_{j\in F}N_j.
\tag{1.4}
$$
全部真实进位同时计入，给
$$
\|T_F\|
\le\frac{L+1}{L+2}
+\frac{2}{L+2}\sum_{j\in F}\eta_j
\le\frac{L+1+2C_m}{L+2}<1.
\tag{1.5}
$$
所以每个 $T_F$ 都是原算子的实际收缩，不只是其独立位近似为收缩。

## 2. 单一次数剩余类中的收缩强单位

固定正奇数 $p$。取 $d\ge1$ 使 $2^d\equiv1\pmod p$；$p=1$ 时取 $d=1$。给任意头深度 $b$，选择严格递增的位
$$
j_\nu\ge b,\qquad j_\nu\equiv0\pmod d,\qquad \nu\ge1.
$$
置
$$
T_{b,L}=\frac{2}{L+2}\sum_{\nu=1}^L N_{j_\nu}.
\tag{2.1}
$$
每个单项式的次数 $2^{j_\nu}$ 都满足
$$
2^{j_\nu}\equiv1\pmod p,
\tag{2.2}
$$
而 $\|T_{b,L}\|\le1$。此外，它在前 $b$ 位上准确为恒等张量一个尾算子：
$$
T_{b,L}=I_{2^b}\otimes S_{b,L},\qquad \|S_{b,L}\|\le1.
\tag{2.3}
$$
这是由 $N_j=I_{2^j}\otimes(B_{m+j}/\alpha_{m+j})$ 得到的准确位置关系。

对每个固定 $b$，
$$
\boxed{T_{b,L}\longrightarrow I\quad\text{强*},\qquad L\to\infty.}
\tag{2.4}
$$
证明先取有限柱 $f$。除了有限个初始位以外，$E_{j_\nu}f=\mathbf1_{\{y_{j_\nu}=1\}}f$，这些 Bernoulli 变量互相独立且独立于 $f$。其平均趋于 $f/2$ 于 $L^2$；系数 $2L/(L+2)\to2$。当全部位都高于 $f$ 支持时，准确有
$$
\left\|
\left(\frac{2}{L+2}\sum_{\nu=1}^L E_{j_\nu}-I\right)f
\right\|^2
=\frac{L+4}{(L+2)^2}\|f\|^2.
\tag{2.5}
$$
有限初始位只给 $O_f(L^{-1})$ 误差，而真实 carry 的范数误差至多 $2C_m/(L+2)$。柱函数稠密及 (1.5) 给全空间强收敛。由于这些算子是收缩且强趋 $I$，
$$
\|(T_{b,L}^*-I)x\|^2
\le2\|x\|^2-2\operatorname{Re}\langle T_{b,L}^*x,x\rangle
\longrightarrow0,
$$
故也强*收敛。

特别，$B_mT_{b,L}^{p-1}$ 是 $B_m^p$ 的实际多项式，并且
$$
\boxed{
B_mT_{b,L}^{p-1}\longrightarrow B_m\quad\text{强*},
\qquad
\|B_mT_{b,L}^{p-1}\|\le\|B_m\|.
}
\tag{2.6}
$$
$p=1$ 时直接取 $B_m$。对于任意剩余类 $r$，取一个正整数 $a\equiv r\pmod p$，则 $T_{b,L}^a$ 是该单一剩余类中的收缩强单位。

## 3. 所需的矩阵多项式收缩不等式

为保持整个有限多项式的范数，不把其各系数范数分别相加，需要下面的标准不等式及其证明。

**引理 3.1。** 设 $S$ 为 Hilbert 空间上的收缩，$C_0,\ldots,C_n$ 为同一个有限维空间上的矩阵，则
$$
\left\|\sum_{a=0}^n C_a\otimes S^a\right\|
\le\max_{|z|=1}\left\|\sum_{a=0}^n C_a z^a\right\|.
\tag{3.1}
$$

**证明。** 先假设 $\|S\|<1$，令 $D=(I-S^*S)^{1/2}$。映射
$$
Vx=\sum_{\nu\ge0}z^\nu DS^\nu x
$$
从原 Hilbert 空间到其向量值 Hardy 空间是等距的，因为
$$
\sum_{\nu\ge0}\|DS^\nu x\|^2
=\sum_{\nu\ge0}
\bigl(\|S^\nu x\|^2-\|S^{\nu+1}x\|^2\bigr)=\|x\|^2.
$$
若 $L$ 为 Hardy 空间的前向移位，则 $VS=L^*V$。张量有限维头后，左边的矩阵多项式与 $\sum C_a\otimes(L^*)^a$ 交织，故其范数不大于后者。后者的伴随是矩阵解析多项式
$\sum C_a^*z^a$ 的乘法算子；由圆周 Parseval 身份，其范数不超过该矩阵多项式在圆周的最大范数。这与右边相等。一般收缩用 $\theta S$、$0<\theta<1$ 并令 $\theta\uparrow1$，有限多项式按范数收敛，得到 (3.1)。证毕。

## 4. 一个固定多项式的同范数剩余类逼近

固定
$$
f(z)=\sum_{j=0}^{D}a_jz^j
$$
和剩余类 $r\bmod p$。取整数
$$
n>D,\qquad n\equiv r\pmod p.
\tag{4.1}
$$
定义实际多项式
$$
Q_{b,L}(B_m)
=\sum_{j=0}^{D}a_jB_m^jT_{b,L}^{\,n-j}.
\tag{4.2}
$$
式 (2.2) 保证每个非零单项式的次数均为 $r\bmod p$。因为 $n-j\ge1$ 且 $T_{b,L}$ 的最低次数至少为 $2^b$，$Q_{b,L}$ 的最低次数也至少为 $2^b$。

对每个固定 $b$，由 (2.4)，
$$
Q_{b,L}(B_m)\longrightarrow f(B_m)\quad\text{强*}.
\tag{4.3}
$$

现在完整支付其普通范数。将 $B_m$ 的前 $b$ 位分开，令 $J_b$ 是该头上的加权 nilpotent 链，提升时记作 $J_b\otimes I$。原进位式给
$$
\|B_m-J_b\otimes I\|=\alpha_{m+b},
\qquad
\|B_m\|=\|J_b\|=\alpha_m\quad(b\ge1).
\tag{4.4}
$$
置
$$
\varepsilon_b(f)
=\alpha_{m+b}\sum_{j=1}^D j|a_j|\alpha_m^{j-1}
\longrightarrow0.
\tag{4.5}
$$
由逐幂 telescoping 和 $\|T_{b,L}\|\le1$，
$$
\left\|
Q_{b,L}(B_m)
-\sum_{j=0}^D a_jJ_b^j\otimes S_{b,L}^{\,n-j}
\right\|
\le\varepsilon_b(f).
\tag{4.6}
$$
给矩阵多项式
$$
F(z)=\sum_{j=0}^D a_jJ_b^j z^{\,n-j}.
$$
在 $|z|=1$ 上，$J_b/z$ 与 $J_b$ 通过有限头对角酉相似，所以
$$
\|F(z)\|=\|z^n f(J_b/z)\|=\|f(J_b)\|.
\tag{4.7}
$$
引理 3.1 及 (2.3) 遂给
$$
\left\|\sum_{j=0}^D a_jJ_b^j\otimes S_{b,L}^{\,n-j}\right\|
\le\|f(J_b)\|.
$$
再由 (4.4)—(4.5)，
$$
\boxed{
\|Q_{b,L}(B_m)\|
\le\|f(B_m)\|+2\varepsilon_b(f),
}
\tag{4.8}
$$
一致于 $L$。这项界保留整个实际 $f(B_m)$ 的范数，没有用 $\sum|a_j|\|B_m^j\|$ 取代它。

### 4.1 最低次数趋无穷时仍保留统一预算

式 (4.8) 的 carry 费用只含 $f$ 的原次数 $j\le D$，不含辅助指数 $n$；因为所有 $T_{b,L}^{n-j}$ 都是收缩。故之后让 $b,n$ 同时增大，不会向这一范数界偷偷加入 $n\alpha_{m+b}$。

强逼近的速度则确实依赖 $n$。令
$$
H(f,n)=\sum_{j=0}^D |a_j|\alpha_m^j(n-j).
$$
若一个单位柱向量 $x$ 的全部位低于 $b$，由 (2.5)、carry 界及收缩性可取
$$
\|(T_{b,L}-I)x\|\le\frac4{\sqrt L},
\qquad
\|(T_{b,L}^*-I)x\|\le\frac4{\sqrt L}.
$$
第二式例如由
$\operatorname{Re}\langle T_{b,L}x,x\rangle
\ge L/(L+2)-2C_m/(L+2)$
代入第 2 节的收缩伴随不等式得到。
对收缩 $T$，
$$
\|(T^a-I)x\|\le a\|(T-I)x\|,
$$
伴随也同理。由于 $T_{b,L}$ 与 $B_m$ 交换，其伴随也与 $B_m^*$ 交换，故
$$
\boxed{
\begin{aligned}
\|(Q_{b,L}(B_m)-f(B_m))x\|
&\le \frac{4H(f,n)}{\sqrt L},\\
\|(Q_{b,L}(B_m)^*-f(B_m)^*)x\|
&\le \frac{4H(f,n)}{\sqrt L}.
\end{aligned}}
\tag{4.9}
$$
因此增加 $n$ 所需的同一实际来源费用可以明确由增加 $L$ 支付；未使用对随阶段变化的 $f,n$ 自动一致的强收敛。

## 5. 完整交换子的单位球密度

[原尾有界根正文 §2](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)的有限头压缩证明给每个 $X\in\mathscr C_m$ 一列多项式 $f_\ell$，满足
$$
f_\ell(B_m)\longrightarrow X\quad\text{强},
\qquad
\|f_\ell(B_m)\|\le\|X\|.
\tag{5.1}
$$
确切地，该处多项式与收缩有限头压缩的范数误差为 $o(1)\|X\|$；除以相应的 $1+o(1)$ 即得 (5.1)。

此处强收敛自动加强为强*。令
$$
(\mathcal J_mf)(z)=\overline{f(-1-z)}.
$$
原径向权给 $B_m=\mathcal J_mB_m^*\mathcal J_m$，故每个多项式满足
$f_\ell(B_m)^*=\mathcal J_m f_\ell(B_m)\mathcal J_m$。其伴随于是强收敛到 $\mathcal J_mX\mathcal J_m$；由内积极限，这个极限就是 $X^*$。所以完整交换子的每个元素也对同一个 $\mathcal J_m$ 复对称。

现在设 $X\ne0$。对第 $\ell$ 个固定多项式 $f_\ell$，在第 4 节中选择：

- $n_\ell>\deg f_\ell$ 且 $n_\ell\equiv r\pmod p$；
- $b_\ell\ge\ell$ 高于前 $\ell$ 个 Walsh 基向量的位支持，且使 $2\varepsilon_{b_\ell}(f_\ell)\le\ell^{-1}$；
- 取 $L_\ell>16\ell^2H(f_\ell,n_\ell)^2$，由 (4.9) 使同一列真实强*逼近在这些单位检验向量及伴随上都小于 $\ell^{-1}$。

由 (4.8)，所得 $Q_\ell$ 满足
$$
\|Q_\ell(B_m)\|\le\|X\|+\ell^{-1},
\qquad
Q_\ell(B_m)\longrightarrow X\quad\text{强*}.
$$
最后乘标量
$$
\frac{\|X\|}{\|X\|+\ell^{-1}}
$$
得到所需的 $q_\ell$，不改变任何次数及剩余类条件。$X=0$ 时取零多项式。综上，
$$
\boxed{
\begin{gathered}
\|q_\ell(B_m)\|\le\|X\|,\qquad
q_\ell(B_m)\to X\quad\text{强*},\\
[z^j]q_\ell\ne0\ \Longrightarrow\
j\equiv r\pmod p,\quad j\ge2^{b_\ell}\longrightarrow\infty.
\end{gathered}}
\tag{5.2}
$$

## 6. 单一奇数剩余类的实际循环空间和正常配对

**推论 6.1。** 任给 $f\in K$、正奇数 $p$、$0\le r<p$ 和 $N\ge0$，
$$
\boxed{
\overline{\operatorname{span}}\{B_m^{pn+r}f:n\ge N\}
=[f]_{B_m}.
}
\tag{6.1}
$$
这里 $[f]_{B_m}$ 是 $f$ 的普通闭循环子空间。

证明：左边显然包含于右边。对每个 $j\ge0$，将 (5.2) 用于 $X=B_m^j$；其多项式的最低次数趋无穷，所以充分大阶段的每项都在左边所选的同一剩余类尾部中。强极限给 $B_m^jf$ 属于左边。取闭包即得等式。

**推论 6.2。** 设 $\varphi$ 是 $B(K)$ 上正常线性泛函。若对某个正奇数 $p$、某剩余类 $r$ 及全部充分大的 $n\equiv r\pmod p$ 都有
$$
\varphi(B_m^n)=0,
$$
则
$$
\boxed{\varphi(X)=0\quad\text{对全部 }X\in\mathscr C_m.}
\tag{6.2}
$$

证明：对固定 $X$ 使用 (5.2)，充分大的多项式各项均被 $\varphi$ 湮灭。正常泛函由 trace-class 算子表示；先用有限秩在 trace norm 中逼近该表示，再用多项式的统一算子范数界，可将其值通过强*极限传递。因此 $\varphi(X)=0$。

此推论覆盖任意已经定义好的有限向量配对、有限秩或 trace-class 正见证。若配对中还含一个未支付域的无界算子，则不能先把它称为正常泛函再套用本结论。

## 7. 对同一实际不变空间与闭域的可用范围

每个 $q_\ell(B_m)$ 都是原算子的实际多项式，故保持每个闭 $B_m$-不变空间。式 (5.2) 的强极限仍保持该空间；全过程没有另换来源向量，也没有调用 Deddens 对未知普通不变空间的保持。

若 $T$ 是闭算子，$\operatorname{Dom}T$ 被 $B_m$ 保持且在该域上交换，则对每个固定 $x\in\operatorname{Dom}T$，
$$
q_\ell(B_m)x\to Xx,\qquad
Tq_\ell(B_m)x=q_\ell(B_m)Tx\to XTx.
$$
闭性给 $Xx\in\operatorname{Dom}T$ 以及 $TXx=XTx$。当 $X=I$ 时，任何指定奇数剩余类、任意高的最低次数，都能给同一实际域上的图范数近似单位。

这里仍没有得到 $q_\ell(B_m)H\subseteq\operatorname{Dom}T$，更没有从强近似推出某个非零全域有界 $P$ 使 $PH\subseteq\operatorname{Dom}T$。闭根和平坦共同倍数路线需要的这个额外像包含保持为明确未付条件。

全部强*密度与图核心结论只在原纯 Haar 表示、其真实尾及实际有界交织所支付的空间中使用；不能只凭 UHF 的等距抽象表示搬到负整数 boundary。后者的高次正幂杀掉每个固定有限支撑向量，因而本文最低次数趋无穷的多项式不可能在那里强趋 $I$。
