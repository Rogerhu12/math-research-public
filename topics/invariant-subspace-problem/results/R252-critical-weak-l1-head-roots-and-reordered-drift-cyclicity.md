# R252：临界弱 $\ell^1$ 行的有界全柱幂根、排序漂移与大幅往返循环性

日期：2026-11-12（UTC）。作者：kernel。
状态：以下定理已证明。它处理幅度重排允许 $r_n\asymp1/n$ 的临界类；规范逐项交替调和行的活动根 $+1$ 仍未排除。

## 1. 结论

沿用 [R251：任意有限位集的真实进位预算与按幅度排序的 first 分支中心](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) 的实际设置。
固定
$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad a\in\ell^2,
$$
将非零系数按幅度非增排列为 $a_{\iota(k)}$，记
$$
r_k=|a_{\iota(k)}|,\qquad
\tau_n=a_*+\sum_{k=1}^n a_{\iota(k)}.
$$
本稿只要求
$$
\boxed{0<b:=\sup_{k\ge1}kr_k<\infty.}
\tag{1.1}
$$
不再假定 $kr_k\to0$。有限支撑行按有限和处理；以下证明针对无限支撑。

置
$$
I(v)=(1+v)\log(1+v)-v\log v,\qquad
K=1+I(2)
=1+3\log3-2\log2<3.
\tag{1.2}
$$

**定理 1.1。** 若 $M\ne0$ 是实际闭子空间，
$M\subseteq\operatorname{Dom}X$、$XM\subset M$，令 $B=X|_M\in B(M)$，则：

1. 幅度排序部分和 $(\tau_n)$ 必有界。
2. 若 $\sigma(B)$ 有限，则对 $(\tau_n)$ 的每个聚点 $s$ 及每个
   $\lambda\in\sigma(B)$，
   $$
   \boxed{|\lambda-s|\le Kb.}
   \tag{1.3}
   $$

因此，如果排序部分和无界，原 $X$ 没有任何非零有界闭限制分支。
如果排序部分和有两个聚点 $s,t$ 满足
$$
|s-t|>2Kb,
\tag{1.4}
$$
则原 $X$ 没有非零有限谱有界闭限制分支。

**多项式推论。** 在上述任一排除条件下，任意非零多项式 $q$ 和任意复
$\ell^2$ first 指数 $w$ 都满足
$$
\boxed{q(u)e^w\text{ 是实际 }A\text{ 的循环向量},\qquad
u=a_*+\sum_j a_j\chi_j.}
\tag{1.5}
$$
更一般地，若 $(\tau_n)$ 有界，令其聚点集为 $\mathcal C$，置
$$
\mathcal D_b=\bigcap_{s\in\mathcal C}\overline{D(s,Kb)}.
\tag{1.6}
$$
只要 $q$ 的根集与 $\mathcal D_b$ 不交，(1.5) 仍成立。

其中 (1.3) 的有限谱条件不可省；本稿没有把一般 $B$ 的每个谱点都置于每个圆盘。
R251 次临界定理的圆盘半径趋零，本稿则给固定的、与未知分支无关的半径。

## 2. 任意头集的既有真实输入

以下四项已由R251完整证明，且均不依赖有限头的最大位号。

对有限集 $F$，记
$$
H_F=\sum_{j\in F}a_j(V_j-I),\quad
s_F=a_*+\sum_{j\in F}a_j,\quad
Z_{F^c}=X_{\sum_{j\notin F}a_j\chi_j}.
$$
$Q_F$ 保留全部以 $F$ 为支撑的 Walsh 柱；补集次数算子记作
$\mathcal N_{F^c}$。

1. 精确的有界去项及完整自然域给
   $$
   X-s_FI=H_F+Z_{F^c},\qquad
   \operatorname{Dom}(X-s_FI)^p=\operatorname{Dom}Z_{F^c}^p.
   \tag{2.1}
   $$
   这里只减有限个系数，原 $a_*$ 不变，不进行条件收敛无穷标量和的拆分。

2. 对 $d=|F|$、$B_F=\sum_{j\in F}|a_j|$，
   $$
   \|H_F^k\|\le(6B_F)^k e^{-\gamma k^4}
   \quad(k\ge\max(2d,16)),
   \qquad\gamma=770/16^4.
   \tag{2.2}
   $$
   所以当 $d\le\sqrt R+1$ 时，
   $$
   \sup_{|z|\le R}\log\|e^{zH_F}\|=o(R)
   \tag{2.3}
   $$
   一致于所有这样的 $F$。进位计数使用
   $\sum c_j\ge\sum\lfloor k_j/2\rfloor\ge(k-|F|)/2$，而非最大位号。

3. 令 $g=\|a_{F^c}\|_2$。在只数补集位的指数次数空间上，
   $$
   \|Z_{F^c}:\mathcal H_t\to\mathcal H_{t-\delta}\|
   \le Cg\delta^{-1/2}\quad(0<\delta\le t\le1).
   \tag{2.4}
   $$
   纯算子 $Z^0_{F^c}=\sum_{j\notin F}a_jS_j$ 满足同样估计。
   可以取固定 $C=17$，但本稿的主导常数不含这个 $17$。

4. 每个单独真实 Cayley 指数满足
   $$
   \|e^{za_j(V_j-I)}\|
   \le(1+2|za_j|)
   \exp[|za_j|(2\sqrt{\eta_j}+6\eta_j)].
   \tag{2.5}
   $$
   其中
   $$
   \kappa_J:=\sum_{j\ge J}|a_j|(2\sqrt{\eta_j}+6\eta_j)\to0.
   \tag{2.6}
   $$

在 $Q_FH$ 上，真实自然整轨道为
$$
\mathcal E_F(z)
=\sum_{p\ge0}\frac{z^p}{p!}(X-s_FI)^pQ_F
=e^{zH_F}\mathcal E_{Z_{F^c}}(z)Q_F.
\tag{2.7}
$$
这不是全空间上的有界 $e^{zX}$。下节把 (2.4) 给出的粗 Gaussian 常数，
在本稿的具体尺度上换成纯尾的准确常数 $1$，并付清实际 carry 的差。

## 3. 补集 carry 从增长的物理前缀之后才开始

令
$$
\ell_n=\lfloor\sqrt n\rfloor,\qquad
F_n=\{\iota(1),\ldots,\iota(n)\}\cup[0,\ell_n),
$$
$$
g_n=\|a_{F_n^c}\|_2,\qquad s_n=s_{F_n},\qquad N_n=|F_n|.
\tag{3.1}
$$
这些集合递增，$n\le N_n\le n+\sqrt n$，并有 $Q_{F_n}\to I$ 强。
由 $r_k\le b/k$，
$$
g_n^2\le\sum_{k>n}r_k^2\le b^2/n,
\tag{3.2}
$$
且
$$
\boxed{|s_n-\tau_n|\le\sqrt{\ell_n}\,
       \left(\sum_{k>n}r_k^2\right)^{1/2}
       \le b n^{-1/4}\to0.}
\tag{3.3}
$$
缩小追加的物理前缀仍使所有固定有限柱最终被保留，同时让临界情形的标量误差也趋零。

令 $J=F_n^c$，$Z=Z_J$、$Z^0=Z_J^0$。
在 $\mathcal H_t=\operatorname{Dom}e^{t\mathcal N_J}$ 上，真实差为
$$
K_n=Z-Z^0=\sum_{j\in J}\sum_{L\ge1}a_jB_{j,j+L},
\qquad
\|B_{j,j+L}\|\le18\eta_j\eta_*^{L-1}.
$$
每一局部项只改变至多 $L+1$ 个补集位。因此对 $0\le t\le1$，
$$
\|K_n:\mathcal H_t\to\mathcal H_t\|
\le C_\eta\sum_{j\in J}|a_j|\eta_j
\le C_\eta g_n\bar\eta_{\ell_n}
=:\delta_n,
\tag{3.4}
$$
其中
$$
C_\eta=\frac{18e^2}{1-e\eta_*},\qquad
\bar\eta_\ell=\left(\sum_{j\ge\ell}\eta_j^2\right)^{1/2}
\le2e^{-770\,16^\ell}.
\tag{3.5}
$$
$j\notin F_n$ 迫 $j\ge\ell_n$，这是本节不能遗漏的实际物理起点。

对自然幂作望远镜展开，把 $1\to0$ 分成 $p$ 个尺度步长。
$K_n$ 的一步只需 (3.4) 的同权范数；其余 $p-1$ 个因子使用 (2.4)。
所有中间输入都在下一个因子的真实域中，故
$$
\boxed{
\|(Z^p-(Z^0)^p)Q_{F_n}\|
\le p\delta_n(Cg_n\sqrt p)^{p-1}.
}
\tag{3.6}
$$
于是，若 $|z|\le R$，
$$
\begin{aligned}
\|(\mathcal E_Z(z)-\mathcal E_{Z^0}(z))Q_{F_n}\|
&\le\delta_n R\sum_{q\ge0}
  \frac{(Cg_nR\sqrt{q+1})^q}{q!}\\
&\le\sqrt2\,\delta_n R
  \exp(2e^2C^2g_n^2R^2).
\end{aligned}
\tag{3.7}
$$
最后一式可由 $q!\ge(q/e)^q$、$\sqrt{q+1}\le\sqrt{2q}$（$q\ge1$），
再对 $\sum v^q/\sqrt{q!}$ 用 Cauchy–Schwarz 得出；$q=0$ 项单独保留。

本稿固定
$$
\boxed{R_n=n/b.}
\tag{3.8}
$$
由 (3.2)，$g_n^2R_n^2\le n$；而 (3.5) 的负指数远大于 $n^2$。
因此 (3.7) 在整个 $|z|\le R_n$ 上最终至多 $e^{-n^2}$：
$$
\boxed{
\sup_{|z|\le R_n}
\|(\mathcal E_Z(z)-\mathcal E_{Z^0}(z))Q_{F_n}\|
\le e^{-n^2}.
}
\tag{3.9}
$$
固定的 $C=17$ 只进入被双指数 carry 压倒的误差，不进入下面的主导圆盘半径。

## 4. 纯尾的准确整轨道上界

在单个位的 Walsh 基上，
$$
e^{zaS_j}\Omega
=e^{za}[(1-za)\Omega+za\chi_j].
$$
对任意复 $z,a$，
$$
\|e^{zaS_j}\Omega\|^2
=e^{2\operatorname{Re}(za)}
 \left(1-2\operatorname{Re}(za)+2|za|^2\right)
\le e^{2|za|^2}.
\tag{4.1}
$$
这里括号始终至少为 $1/2$，所以可直接用 $\log(1+t)\le t$。

纯 $Z^0_J$ 只作用于补集位，而 $Q_{F_n}$ 在这些位上保留参考真空。
先对有限个补集位作张量积，再由 $\ell^2$ 系数取极限，得到
$$
\boxed{
\|\mathcal E_{Z^0_J}(z)Q_{F_n}\|
\le e^{g_n^2|z|^2}.
}
\tag{4.2}
$$
此极限确实等于纯自然幂的整级数：
有限系数截断在每个正指数次数尺度之间由 (2.4) 收敛，
从而对每个固定自然幂收敛；同一 Gaussian 级数给复紧集上一致收敛。
也可直接使用不完全张量积判据，因为每个局部真空系数为
$e^{za}(1-za)=1+O(|a|^2)$，而非真空分量为 $O(|a|)$。
整个头维数只作恒等放大。

由 (3.9)、(4.2)，对 $|z|\le R_n$，最终有
$$
\boxed{\|\mathcal E_Z(z)Q_{F_n}\|
\le2e^{g_n^2R_n^2}.}
\tag{4.3}
$$

## 5. 有界而不必趋零的全柱自然幂根

将选中的头分成低物理部分
$$
F_n^{\rm low}=F_n\cap[0,J_n),\qquad
J_n=\lfloor\sqrt{R_n}\rfloor
$$
和其余部分。低物理部分由 (2.3) 只付 $o(R_n)$。
其余部分用 (2.5)、(2.6)，以及按幅度的积分估计
$$
\begin{aligned}
\sum_{j\in F_n}\log(1+2R_n|a_j|)
&\le\sum_{k=1}^{N_n}\log(1+2bR_n/k)\\
&\le N_n I(2bR_n/N_n).
\end{aligned}
\tag{5.1}
$$
结合 (2.7)、(4.3)，可取 $\Lambda_n\ge0$ 使
$$
\sup_{|z|\le R_n}\|\mathcal E_{F_n}(z)\|\le e^{\Lambda_n},
$$
并有
$$
\begin{aligned}
\limsup_n\frac{\Lambda_n}{R_n}
&\le
\lim_n\frac{N_n}{R_n}I(2bR_n/N_n)
+\limsup_n g_n^2R_n\\
&\le bI(2)+b=:d_b.
\end{aligned}
\tag{5.2}
$$
固定小 carry 仍不能直接乘 $R_n$ 后丢掉；是增长的 $J_n$ 使
$\kappa_{J_n}\to0$，低物理部分另外由四次进位预算支付。

取
$$
p_n=\lceil d_b R_n\rceil=\lceil[1+I(2)]n\rceil.
\tag{5.3}
$$
由积分夹逼有 $\log(p!)=p\log p-p+O(\log p)$，故
$p!^{1/p}=(p/e)(1+o(1))$。在此保留这个因子；只用 $p!\le p^p$ 会无谓多付一个 $e$。
算子值 Cauchy 估计给
$$
\limsup_n
\|(X-s_nI)^{p_n}Q_{F_n}\|^{1/p_n}
\le \frac{d_b}{e}\exp(1)=d_b=Kb.
$$
实际共轭 $C$ 保持所有 $Q_F$，把已经付清域的自然幂逐次送到伴随幂，故
$$
\boxed{
\limsup_n
\|(X^*-\overline{s_n}I)^{p_n}Q_{F_n}\|^{1/p_n}
\le Kb.
}
\tag{5.4}
$$
$Q_{F_n}\to I$ 强，$p_n\to\infty$。
这是真实同一算子的全柱估计，不是仅在一个参考向量上的形式幂计算。

## 6. 预解式的幂需要使用谱半径，不能只用一次预解范数

设 $M,B$ 如定理 1.1。真实域上的
$$
P_MX^*=B^*P_M
$$
可在 (5.4) 的具体向量上逐次使用。因此只要 $s_n\in\rho(B)$，
$$
P_MQ_{F_n}
=(B^*-\overline{s_n}I)^{-p_n}
 P_M(X^*-\overline{s_n}I)^{p_n}Q_{F_n}.
\tag{6.1}
$$

若 $\tau_n$ 无界，(3.3) 给某子列 $|s_n|\to\infty$，且
$$
\|(B-s_nI)^{-p_n}\|
\le(|s_n|-\|B\|)^{-p_n}.
$$
与 (5.4) 合并即得 $\|P_MQ_{F_n}\|\to0$，违 $M\ne0$。
这证明定理第 1 项。

现在假设 $\sigma(B)$ 有限。取任一谱点 $\lambda$，其非零 Riesz 子空间记为
$M_\lambda$；这仍是原 $H$ 中的真实闭 $X$ 不变空间。
令 $B_\lambda=X|_{M_\lambda}$，$Q=B_\lambda-\lambda I$ 拟幂零。
对任意 $\rho>0$，存在有限 $C_\rho$ 使
$$
\|Q^k\|\le C_\rho\rho^k\quad(k\ge0).
\tag{6.2}
$$
若 $|s_n-\lambda|>\rho$，对逆的自然正整数幂作范数收敛展开，
$$
(B_\lambda-s_nI)^{-p}
=(\lambda-s_n)^{-p}
\sum_{k\ge0}(-1)^k\binom{p+k-1}{k}
 \frac{Q^k}{(\lambda-s_n)^k},
$$
从而
$$
\boxed{
\|(B_\lambda-s_nI)^{-p}\|
\le C_\rho(|s_n-\lambda|-\rho)^{-p}.
}
\tag{6.3}
$$
这是统一于 $n,p$ 的估计。不能用
$\|(B_\lambda-s_nI)^{-1}\|^p$ 代替后再无证地把范数改成谱距离。

沿任一聚点子列 $\tau_n\to s$，由 (3.3) 也有 $s_n\to s$。
若 $|\lambda-s|>Kb$，选 $\rho>0$ 足够小，使
$|\lambda-s|-2\rho>Kb$。
把 (6.3) 代入此 $M_\lambda$ 的 (6.1)，再用 (5.4)，
得到 $\|P_{M_\lambda}Q_{F_n}\|\to0$，迫 $M_\lambda=0$，矛盾。
因此 (1.3) 成立。

若两个聚点相距大于 $2Kb$，其两个闭圆盘不交，有限谱非空便产生矛盾。
最后对 R176/R147 的实际 $P(X)$ 核使用该有限谱结论：
非零核上 $X$ 有界、谱属于 $q$ 的根集；核零由 $C$ 自伴性给值域稠密，
再由真实图循环性和指数权外单位得到 (1.5)–(1.6)。

## 7. 任意物理置换的不等振幅调和行

固定 $\kappa>0$、$\kappa\ne1$，原系数列为
$$
c_{2k}=\frac1{2k+1},\qquad
c_{2k+1}=-\frac{\kappa}{2k+2}.
\tag{7.1}
$$
它满足弱 $\ell^1$ 幅度条件；例如可取 $b\le\max(1,\kappa)$。

幅度阈值 $t\downarrow0$ 时，正、负项的计数分别是
$$
\frac1{2t}+O(1),\qquad \frac{\kappa}{2t}+O(1).
$$
所以按幅度排序前 $n$ 项中的两类项数为
$$
n_+(n)=\frac{n}{1+\kappa}+O(1),\qquad
n_-(n)=\frac{\kappa n}{1+\kappa}+O(1).
$$
同模并列最多有两项，不影响这些估计。调和级数的渐近给
$$
\boxed{\tau_n=\frac{1-\kappa}{2}\log n+O(1).}
\tag{7.2}
$$
故排序和无界。

令 $a_j=c_{\pi(j)}$，其中 $\pi$ 是任意物理位置置换。
排序漂移 (7.2) 保持，定理给：这个实际 first 没有任何非零有界闭限制分支，
且全部非零 $q(u)e^w$ 循环。

这比依赖原物理部分和漂移的 R241 更强：
由于两类系数都不可和，物理顺序可以用条件重排改成收敛到任意指定实数，
或保持有界振荡；(7.2) 与本定理仍完全有效。
并未把置换视作原 $A$ 的酉共轭，而是对每个置换后的实际系数行各自应用完整域证明。

## 8. 幅度仍为 $1/(j+1)$、物理部分和有界的新临界例

取 $a_*=0$，$a_0=1$。从 $j=1$ 开始，依次给 $1/(j+1)$ 选择符号：
连续取正号，直到当前部分和严格大于 $6$；然后连续取负号，
直到严格小于 $0$；反复执行。

调和尾不可和，故每个块有限结束。每次过冲至多等于最后一项的幅度，
它趋零；块内部分和单调。因此 $(\tau_n)$ 有界，且有聚点 $0$ 和 $6$
（事实上聚点集为 $[0,6]$）。

这里严格有
$$
r_n=1/n,\qquad b=1,\qquad
n\sum_{k>n}r_k^2\to1.
$$
所以它不属于 $nr_n\to0$ 的次临界类，也没有部分和漂移到无穷。
但
$$
6>2K,
$$
两个聚点的 $K$ 圆盘不交。定理遂给
$$
\boxed{\text{此临界行的全部非零 }q(u)e^w\text{ 都循环。}}
\tag{8.1}
$$
任意物理位置置换仍保留幅度排序后的这条符号行，故同样成立。
正、负两类质量均无穷，R138 仍把这些 first 归于全平面连续谱类。

## 9. 规范交替行仍留下什么

对规范 $a_j=(-1)^j/(j+1)$，幅度排序和只收敛到 $\log2$。
本稿只给有限谱分支落在 $\overline{D(\log2,K)}$，
比 R246 已得的精确椭圆更弱，因此不替换 R246。
特别，活动根 $+1$ 仍在允许区域内。

本稿的新增正结果是：

- 临界弱 $\ell^1$ 的排序和只要无界，就排除全部有界闭分支；
- 排序和即使有界，只要其聚点分离超过一个明确固定阈值，
  也排除全部有限谱闭分支；
- 这两类均对任意物理系数置换有效，并给完整的实际多项式循环性。

它没有从这些新类免费取参数极限来排规范 $+1$，
也没有把这些全空间分支结果写成所有未知限制／子商上的普遍稠密像。

依赖：R251 §§2–7；
R207 指数次数权附录；R176/R147 的真实 Bell 核与指数权图循环接口；
R138 的非 $\ell^1$ first 谱分类。

