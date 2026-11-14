# R239 附录：固定矩形的精确 Turán 端点与更强曲率上界

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：以下固定宽高的上界及端点常数已证明。它们是实际矩形族的额外必要约束，不单独宣称异常位的全高度比较。
- 输入：仓库自足重证的单 Schur Toda 身份；本文 §5 进一步完整重证所需 Turán 比单调性。单调性的原出处为 Suvrit Sra, *Monotonicity of Turán-ratios of symmetric polynomials*, v1 (2026-10-07), §2；[作者官方页](https://suvrit.github.io/papers/sym-turan/)。

## 1. 结论

固定整数 $N\ge2$、$1\le D<N$、$t\ge1$。令
$$
S_j(z)=s_{(t^D)}(z^{[j]},1^{[N-j]}),\quad
f_j(\theta)=\log S_j(e^\theta),\quad
\kappa(z)=\frac{z}{(z-1)^2},\quad z>1.
$$
对 $1\le j<N$，置 $U_j=S_j^2/(S_{j-1}S_{j+1})$。

**定理。** 若 $j<D$，
$$
1\le U_j(z)\le
\frac{(N-j)(t+D-j)}{(D-j)(t+N-j)}.
\tag{1.1}
$$
若 $j>D$，
$$
1\le U_j(z)\le
\frac{j(t+j-D)}{(j-D)(t+j)}.
\tag{1.2}
$$
上界是 $z\to\infty$ 的准确极限。$j=D$ 时 $U_D(z)\to\infty$。

因此所有 $1\le j<N$ 的对数曲率满足
$$
\boxed{
0<f_j''(\theta)\le
\kappa(z)\,
\frac{t\,\min(j,D)\,[N-\max(j,D)]}{t+|j-D|}.
}
\tag{1.3}
$$
特别地，舍弃宽度 $t$ 后仍有更强于一般 Schur 界的
$$
\boxed{f_j''(\theta)\le
\kappa(z)\min(j,D)[N-\max(j,D)].}
\tag{1.4}
$$
(1.3) 的系数对固定 $N,D,t,j$ 是最优的：$f_j''/\kappa$ 在 $z\to\infty$ 时趋向所列系数。$0<z<1$ 的对应界由 $j\mapsto N-j$、$z\mapsto1/z$ 得到；$z=1$ 无需使用奇异的 $\kappa$ 表达。

## 2. 最高项的完整计算

记
$$
d_m^{(k)}(t)=s_{(t^k)}(1^{[m]}),\qquad m\ge k.
$$
Weyl/钩长积给
$$
d_m^{(k)}(t)=\prod_{i=1}^k\prod_{r=1}^t
\frac{m+r-i}{t-r+k-i+1}.
\tag{2.1}
$$
当 $m>k$ 时逐列相消，准确得到
$$
\frac{(d_m^{(k)}(t))^2}
{d_{m-1}^{(k)}(t)d_{m+1}^{(k)}(t)}
=\frac{m(m+t-k)}{(m-k)(m+t)}.
\tag{2.2}
$$

若 $j\ge D$，Schur 表中能使用 $z$ 变量填满全部 $tD$ 个格，最高项为
$$
S_j(z)=d_j^{(D)}(t)z^{tD}+\text{较低次项}.
\tag{2.3}
$$
若 $j<D$，每列至多使用 $j$ 个 $z$ 变量，最高次数为 $tj$。最高项对应唯一的 $z$ 子形 $(t^j)$，其在 $j$ 个一变量上的 Schur 值为一；剩余形为 $(t^{D-j})$，故
$$
S_j(z)=d_{N-j}^{(D-j)}(t)z^{tj}+\text{较低次项}.
\tag{2.4}
$$
有限矩形的补秩维数对称性给
$$
d_{N-j}^{(D-j)}(t)=d_{N-j}^{(N-D)}(t).
\tag{2.5}
$$
它可从 (2.1) 直接消积，或由 $\det^t$ 张量对偶得到。

$j>D$ 时将 (2.3) 代入 $U_j$，最高次数相消，(2.2) 取 $m=j,k=D$ 得 (1.2) 的极限。$j<D$ 时用 (2.4)–(2.5)，取 $m=N-j,k=N-D$，同样得到 (1.1) 的极限。$j=D$ 时最高次数之差为 $t>0$，所以 $U_D\to\infty$。

## 3. 单调性与曲率

已有单 Schur 定理给 $U_j(z)$ 在 $z>1$ 单调非减，且 $U_j(1)=1$；因此其准确无穷端点给 (1.1)、(1.2)。这一步明确使用实际矩形 Schur 族，任意正底测度不具备该单调性。

已证明的 Toda 身份为
$$
f_j''=\kappa(z)\,j(N-j)\left(1-U_j^{-1}\right).
\tag{3.1}
$$
若 $j>D$，用 (1.2) 得
$$
\frac{f_j''}{\kappa}\le
j(N-j)-\frac{(j-D)(t+j)(N-j)}{t+j-D}
=\frac{Dt(N-j)}{t+j-D}.
$$
若 $j<D$，同样得到
$$
\frac{f_j''}{\kappa}\le
j(N-j)-\frac{j(D-j)(t+N-j)}{t+D-j}
=\frac{jt(N-D)}{t+D-j}.
$$
$j=D$ 时用 $U_D>0$ 得 $f_D''<\kappa D(N-D)$。这正是 (1.3)，且 (1.4) 直接跟随。准确极限由 (3.1) 和 §2 给出。

## 4. 对真实异常位问题的用法与限度

真实中矩形的参数是 $N=h+1$、$D=\delta+1\le(h+1)/2$，宽为 $t=q-\delta\ge1$，而
$$
f_j''=a_j/b_{j-1}.
$$
因此在四次式涉及的 $j=n-1,n,n+1,n+2$ 上，可以把一般的 $\kappa j(N-j)$ 上界替换成 (1.3)。它们保留相同的矩形高度 $D$ 和宽度 $t$，不能为四个位置分别任意选择。

例如 $h=10,n=8,z=21/20$ 时，$N=11$、$D\le5$、$\kappa=420$。真实范数比 $a_8/b_7$ 必满足
$$
a_8/b_7\le15\kappa=6300,
$$
所以仅满足一般 Schur 曲率界的松弛取值 $a_8/b_7=7900$ 不属于实际矩形族。

这些约束尚不足以无条件宣称四次式各系数非负。即使所有实际模型中各系数都非负，扩大到只保若干标量必要条件的松弛域，也可能出现负系数而整条四次式仍为正。完整相邻目标是所有正 $w$ 上的四次式正性，后续应保整个 $w$ 多项式及三族的联立结构。


## 5. 所用单 Schur 单调性的自足证明及来源

本节是 Suvrit Sra, *Monotonicity of Turán-ratios of symmetric polynomials*, v1 (2026-10-07), Lemma 2.2 / Theorem 1.1（pp. 3–4）的负部和最大原理证明，明确保留署名，不登记为本稿的新定理。仓库 notes/2026-11-13-three-weight-interior-quartic-shear-and-rational-evidence-0c.md §2 已写出此短证；这里为完整性重述并补齐严格性与半无限区间的极限论证。唯一输入是两权全高度稿 §8 从有限 Schur 行列式完整推导的 Toda 身份。

取任意长度补零到 $N$ 的分区 $\lambda$，定义
$$
S_i=s_\lambda(e^{\theta[i]},1^{[N-i]}),\quad f_i=\log S_i,
\quad u_i=2f_i-f_{i-1}-f_{i+1},\quad 1\le i<N.
$$
在 $\theta>0$ 上置
$$
\kappa=(4\sinh^2(\theta/2))^{-1},\qquad
B_i=i(N-i)e^{-u_i},\qquad B_0=B_N=0.
$$
已自足证明的 Toda 身份是
$$
f_i''=\kappa[i(N-i)-B_i],\qquad
u_i''=\kappa[2-2B_i+B_{i-1}+B_{i+1}].
\tag{5.1}
$$
令 $v_i=u_i'$。因为 $B_i'=-B_iv_i$，对 (5.1) 微分得闭合线性系统
$$
\boxed{v_i''-\frac{\kappa'}\kappa v_i'
=\kappa[2B_iv_i-B_{i-1}v_{i-1}-B_{i+1}v_{i+1}],}
\qquad B_0v_0=B_Nv_N=0.
\tag{5.2}
$$

置 $q_i=-v_i$ 和 $W=\sum_{i=1}^{N-1}(q_i)_+$。在任意紧子区间，全部函数光滑；正部的凸链式法则给分布不等式
$$
W''-(\kappa'/\kappa)W'
\ge\kappa\sum_{i\in I}(2B_iq_i-B_{i-1}q_{i-1}-B_{i+1}q_{i+1}),
\quad I=\{i:q_i>0\}.
$$
右侧重新按 $j$ 求和，其 $B_jq_j$ 的系数是
$$
2\mathbf1_I(j)-\mathbf1_I(j-1)-\mathbf1_I(j+1).
$$
若 $j\in I$，该系数非负且 $q_j>0$；若 $j\notin I$，该系数非正且 $q_j\le0$。边界 $B_0,B_N$ 为零。故
$$
W''-(\kappa'/\kappa)W'\ge0.
\tag{5.3}
$$
正部在零点处的分布二阶导数只增加非负测度，已经包含在此不等式内。

作坐标变换
$$
s=-\tfrac12\coth(\theta/2),\qquad ds/d\theta=\kappa.
$$
它把 $0<\theta<\infty$ 映为 $-\infty<s<-1/2$，且
$$
\frac{d^2W}{ds^2}=\frac{W''-(\kappa'/\kappa)W'}{\kappa^2}\ge0
$$
按分布成立。因此 $W$ 是该半无限区间上的凸函数。

变量对称性及次数齐次性给 $f_i'(0)=i|\lambda|/N$，故 $v_i(0)=0$。另一方面，Schur 多项式关于前 $i$ 个等于 $z$ 的变量的最大总次数是 $\lambda_1+\cdots+\lambda_i$，而该最高项系数严格正。因此
$$
v_i(+\infty)=\lambda_i-\lambda_{i+1}\ge0.
$$
于是 $W$ 在 $s\to-\infty$ 和 $s\uparrow-1/2$ 时均趋零。对任意有限 $s$，先取凸性弦端点 $s_0<s<s_1$，令 $s_0\to-\infty$，再令 $s_1\uparrow-1/2$，得到 $W(s)\le0$。因 $W\ge0$，必有 $W\equiv0$。这证明
$$
u_i'(\theta)\ge0\quad(\theta>0).
\tag{5.4}
$$

若补零分区 $\lambda$ 不为常数向量，则上式实际上对每个 $1\le i<N$ 严格为正。否则在某个内部点 $v_i=0$，非负性给 $v_i'=0,v_i''\ge0$，而 (5.2) 给 $v_i''=-\kappa(B_{i-1}v_{i-1}+B_{i+1}v_{i+1})\le0$；相邻内部的正 $B$ 强制所有 $v_j=0$。它们均在非负最小点，故所有 $v_j'=0$。光滑线性 ODE 的唯一性迫整条向量解为零，违背至少一个端点差 $\lambda_j-\lambda_{j+1}>0$。矩形 $(t^D)$、$1\le D<N,t\ge1$ 正是非恒定情形。

因为 $U_i=e^{u_i}$ 且 $u_i(0)=0$，所以 $U_i$ 在 $z>1$ 非减（此矩形情形严格递增），且 $U_i(1)=1$。这完全支付了 §3 使用的单调性。$0<z<1$ 由 $S_i(z)=z^{|\lambda|}S_{N-i}(1/z)$ 的变量倒数对偶处理。
