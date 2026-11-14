# 饱和 primitive 固定线的双侧权数最优相邻常数

- 日期：2026-11-13。
- 作者：Astra-ISP-0c；central_review 已独立核验实际 MP 积分、全部正混合、严格性与极限最优性，并与旧稿 §8–10 去重。
- 状态：完整证明；只处理指定饱和固定一维线。
- 输入：[任意独立头权的饱和完整最小逆](../results/R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §8。旧结果给单侧出生常数 $(q+n)/(q+n+1)$；本稿利用头权相对池权的强弱个数给更小且在对应类别内最优的双侧常数。

## 1. 模型与结论

取 $q\ge0$ 个独立正权头位及 $L=q+h$ 个等权池位，其中 $h\ge2$。整体缩放后令池权为一，头权为 $a_i>0$，并置

$$
A_i=a_i^2,\qquad
p=\#\{i:A_i>1\},\qquad
r=\#\{i:A_i<1\}.
\tag{1.1}
$$

单位头权不计入 $p,r$。算子为

$$
D=\sum_{i=1}^q a_iE_i+D_{\rm w}.
$$

考虑出生 $s=q$、池置换固定的饱和 primitive 线。按完整层先取逆、再压 primitive 的约定，

$$
F_n=\frac{D^n(D^*)^n}{(n!)^2},\qquad
\Gamma_n=P_{K_q}F_n^{-1}|_{K_q},\qquad 0\le n\le h.
$$

该固定线约化各 $\Gamma_n$，本征值记为 $\gamma_n$，且 $\gamma_0=1$。

**定理。** 对每个 $1\le n<h$，

$$
\boxed{
\gamma_n^2\le
C_{p,r,h,n}\,\gamma_{n-1}\gamma_{n+1},
\qquad
C_{p,r,h,n}
=\frac{n+p}{n+p+1}
 \frac{h-n+r}{h-n+r+1}.
}
\tag{1.2}
$$

若 $p+r>0$，每个固定有限正头权组的 (1.2) 都严格。若所有头权等于池权，则等号成立，常数为

$$
\frac{n(h-n)}{(n+1)(h-n+1)}.
$$

在指定哪些头权大于、等于、小于池权的整个类别内，(1.2) 的常数最优：强头权平方趋于无穷、弱头权平方趋于零即可逼近它。

## 2. 实际 MP 的标量范数

为保持真实源和完整逆，先重述所用的有限公式。池内未归一对称向量为

$$
w_j=\sum_{|J|=j}e_J,\qquad \|w_j\|^2=\binom Lj.
$$

对头集合 $F\subseteq[q]$，写 $R=[q]\setminus F$、$u=|R|$、
$a_R=\prod_{i\in R}a_i$。饱和 primitive 源及其 $n$ 阶原像为

$$
g=\sum_{F\subseteq[q]}
 (-1)^u\frac{u!a_R}{L^{\underline u}}e_Fw_u,
$$

$$
v_n=\sum_{F\subseteq[q]}
 (-1)^u\frac{(n+u)!a_R}{L^{\underline{n+u}}}e_Fw_{n+u}.
\tag{2.1}
$$

全部池占据数合法，因为 $n\le L-q$。有限差分给

$$
Dg=0,\qquad \frac{D^n}{n!}v_n=g.
$$

完整核正交并非额外假设：在池固定空间中，输入与输出都以全部头集合索引，映射按头集合大小为三角，非零对角使原像唯一。对完整核作池置换平均得到零；固定向量 $v_n$ 因而正交于完整核。它正是真正 Moore–Penrose 最小解。完整层满射由正权对角去权只作秩比较得到，未改变范数。

因此

$$
H_n:=\|v_n\|^2
=\sum_{u=0}^q
 \frac{(n+u)!\,e_u(A_1,\ldots,A_q)}
 {L^{\underline{n+u}}},
\qquad
\gamma_n=\frac{H_n}{H_0}.
\tag{2.2}
$$

$q=0$ 时上述式子是池真空的直接公式，同样成立。源归一化消去后，

$$
\frac{\gamma_n^2}{\gamma_{n-1}\gamma_{n+1}}
=\frac{H_n^2}{H_{n-1}H_{n+1}}.
\tag{2.3}
$$

## 3. 准确 Beta 积分及固定正混合

对每项使用有限 Beta 积分：

$$
\frac{(n+u)!}{L^{\underline{n+u}}}
=(L+1)\int_0^1t^{n+u}(1-t)^{L-n-u}\,dt.
$$

求和并用 $L=q+h$，得到

$$
\boxed{
H_n=(L+1)\int_0^1
 t^n(1-t)^{h-n}
 \prod_{i=1}^q(1-t+A_it)\,dt.
}
\tag{3.1}
$$

这一步只重写 (2.2) 的真正最小逆。

分别按头权相对一的位置展开：

$$
1-t+A_it=
\begin{cases}
1+(A_i-1)t,&A_i>1,\\
A_i+(1-A_i)(1-t),&A_i<1,\\
1,&A_i=1.
\end{cases}
$$

故有与 $n$ 无关的正系数 $d_{ij}$，使

$$
\prod_i(1-t+A_it)
=\sum_{i=0}^p\sum_{j=0}^r d_{ij}t^i(1-t)^j,
\qquad d_{ij}>0.
\tag{3.2}
$$

例如

$$
d_{ij}=
e_i\bigl((A_\ell-1)_{A_\ell>1}\bigr)
\left(\prod_{A_\ell<1}A_\ell\right)
e_j\bigl((A_\ell^{-1}-1)_{A_\ell<1}\bigr).
$$

空集合的零阶基本对称多项式为一。于是

$$
\boxed{
H_n=(L+1)\sum_{i=0}^p\sum_{j=0}^r
d_{ij}\,\mathrm B(n+i+1,h-n+j+1).
}
\tag{3.3}
$$

所有 Beta 参数都严格正，且此同一混合同时给出全部 $0\le n\le h$。

## 4. 每个分量的精确相邻比及混合后的界

记

$$
b_{ij}(n)=\mathrm B(n+i+1,h-n+j+1).
$$

两参数之和 $h+i+j+2$ 不随 $n$ 变化，故直接用阶乘得

$$
\frac{b_{ij}(n)^2}{b_{ij}(n-1)b_{ij}(n+1)}
=
\frac{n+i}{n+i+1}
\frac{h-n+j}{h-n+j+1}.
\tag{4.1}
$$

右侧分别随 $i,j$ 严格递增，因此不超过 $C_{p,r,h,n}$。使用固定正系数以及 Cauchy–Schwarz，

$$
\begin{aligned}
\sum_{i,j}d_{ij}b_{ij}(n)
&\le\sqrt{C_{p,r,h,n}}
 \sum_{i,j}d_{ij}
 \sqrt{b_{ij}(n-1)b_{ij}(n+1)}\\
&\le\sqrt{C_{p,r,h,n}}
 \left(\sum_{i,j}d_{ij}b_{ij}(n-1)\right)^{1/2}
 \left(\sum_{i,j}d_{ij}b_{ij}(n+1)\right)^{1/2}.
\end{aligned}
$$

乘上共同的 $L+1$ 并平方，得到 (1.2)。

若 $p+r>0$，(3.2) 的 $d_{00}>0$，而 (4.1) 在 $(0,0)$ 处严格小于 $C_{p,r,h,n}$，所以第一步已严格。若 $p=r=0$，只有 $(0,0)$ 一个分量，全部式子都是等式。

## 5. 在指定强弱类别内的最优性

固定强头、弱头和单位头的位置。令全部强头 $A_i=T$、全部弱头 $A_i=T^{-1}$，单位头保持一，并令 $T\to\infty$。准确有

$$
T^{-p}\prod_i(1-t+A_it)
\longrightarrow t^p(1-t)^r
$$

作为有限次多项式逐系数收敛。因而对每个合法 $k$，

$$
T^{-p}H_k\longrightarrow
(L+1)\mathrm B(k+p+1,h-k+r+1).
$$

在 (2.3) 中取极限，再用 (4.1)，得到恰为
$C_{p,r,h,n}$ 的极限相邻比。这证明对应强弱类别的统一常数不能减小。

实际头权是 $\sqrt{A_i}$，每个有限 $T$ 仍严格正。这里仅以有限模型的参数极限证明常数最优，没有构造零权或无穷权算子。

## 6. 共同头权、任意高度的推论

本节取 $q\ge1$。若这 $q$ 个头权相同且平方为 $z$，则在整个合法高度区间，

$$
\frac{\gamma_n^2}{\gamma_{n-1}\gamma_{n+1}}
\le
\begin{cases}
\dfrac{n}{n+1}\dfrac{q+h-n}{q+h-n+1},&0<z<1,\\[6pt]
\dfrac{n}{n+1}\dfrac{h-n}{h-n+1},&z=1,\\[6pt]
\dfrac{q+n}{q+n+1}\dfrac{h-n}{h-n+1},&z>1.
\end{cases}
\tag{6.1}
$$

第一、三行对有限 $z$ 严格，并分别在 $z\downarrow0$、
$z\uparrow\infty$ 达到极限常数。因此在全部 $z>0$ 上，最优统一常数是第一、三行常数的较大者。

$h=2,n=1$ 时两者相同，得到

$$
\frac{q+1}{2(q+2)}.
$$

这与[两组整个高度二定理](../results/R239-appendix-two-weight-groups-full-height-two-sharp-primitive-gram-bound.md)的差二饱和串常数一致；后者的回文系数证明是另一个完整核验。

## 7. 结论的使用范围

本稿加强了任意独立头权的饱和固定一维线，不只限于共同头权。新常数在所有合法相邻阶都比旧单侧出生常数小，并准确区分高于、等于、低于池权的头数。

它没有把其他 primitive 线或多维块识别为同一 Beta 混合。尤其，共同两组在一般出生的非饱和双串仍需独立处理；普通有限异权全 primitive、原无限尾及真实 Schur 返回费用不由本稿完成。
