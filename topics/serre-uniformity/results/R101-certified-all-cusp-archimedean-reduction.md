# R101：四个小层的全部尖点严格阿基米德约化

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，含独立复算的区间证书。** 本文从有限轨道、圆分单位和整数逼近见证重新实现第一阶段约化，不使用 BBM 的整点分类结论，也不沿用公开程序的浮点转区间例程。§9 进一步把四层的统一界降到 $246,282,354,508$。全部剩余实分支的完整覆盖和最终候选识别现已由[R109](R109-four-small-level-integral-points-by-complete-real-covers.md)完成。

## 1. 完整结论

设 $P\in X_{\rm ns}^+(p)(\mathbb Q)$ 非尖点，$j(P)\in\mathbb Z$。在最近尖点 $c$ 的标准基本域中写
$$q_c(P)=e^{2\pi i\tau},\qquad \tau\in\mathcal F,\qquad
s=\log|q_c(P)|^{-1}.$$
则有以下**无条件**界：

| $p$ | 全部尖点数 | 通过的整数见证数 | $s$ 的统一上界 $S_p$ | 随之得到的 $\log\max(1,|j(P)|)$ 上界 |
|---:|---:|---:|---:|---:|
| 41 | 20 | 57 | 896 | $<897$ |
| 47 | 23 | 69 | 1100 | $<1101$ |
| 59 | 29 | 87 | 1419 | $<1420$ |
| 83 | 41 | 115 | 2127 | $<2128$ |

每个尖点的更细界、有限轨道系数、全部整数见证都保存在证书中。此界适用于全部整点，包括 $0\le j\le1728$，不要求 $q_c$ 为实数，也不假设 CM、特定商二次域或小惯性。它将无穷尖点尾部严格移除，但不把有限高度界当作已完成有限枚举。

## 2. 固定坐标和全部尖点

记 $d=(p-1)/2$，$g$ 为下表的本原根，$\xi$ 为非平方：

| $p$ | $g$ | $\xi$ |
|---:|---:|---:|
| 41 | 6 | 3 |
| 47 | 5 | 5 |
| 59 | 2 | 2 |
| 83 | 2 | 2 |

使用非分裂 Cartan 及其正规化子
$$
C=\left\{\begin{pmatrix}a&\xi b\\b&a\end{pmatrix}:(a,b)\ne(0,0)\right\},
\qquad
G=C\cup\left\{\begin{pmatrix}a&\xi b\\-b&-a\end{pmatrix}:(a,b)\ne(0,0)\right\}.
$$
取 $H=\{\pm1\}$，$G_H=\det^{-1}(H)$。行向量上的右 $G_H$ 轨道取为
$$\mathcal O=\{(x,y):\xi x^2-y^2\in\{1,-1\}\}.$$
其大小为 $2(p+1)$。对 $0\le k<d$，选 $M_k\in C$ 满足 $\det M_k=g^k$；则
$$\mathcal O_k=\mathcal O M_k
=\{(x,y):\xi x^2-y^2\in\{g^k,-g^k\}\}.$$
这些轨道分割全部非零向量。

尖点由列向量上的 $G\cap\operatorname{SL}_2$ 轨道给出；其不变量是 $u^2-\xi v^2$ 模正负号。对每个 $t=1,\ldots,d$，取一组
$$u_t^2-\xi v_t^2=t\pmod p,$$
再补成
$$\sigma_t=\begin{pmatrix}u_t&b_t\\v_t&w_t\end{pmatrix}\in\operatorname{SL}_2(\mathbb F_p).$$
每个矩阵均保存到证书，故不是只抽查部分尖点。它可提升到 $\operatorname{SL}_2(\mathbb Z)$；以下常数只依赖这个模 $p$ 矩阵。

同一尖点上的另外 $p$ 个标准域代表可写成 $\sigma_tT^r$。右乘 $T^r$ 不改变行向量的第一坐标；在第一坐标为零时也不改变第二坐标。因此下面的斜率和常数项同时适用于该尖点的全部标准域分支，第一阶段不遗漏其中的相位。

## 3. 真正的模单位与整数指数

令 $K^+=\mathbb Q(\zeta_p+\zeta_p^{-1})$。对非零 $(x,y)\in\mathbb F_p^2$，取第一坐标在 $[0,1)$、第二坐标在 $(-1/2,1/2)$ 的 $p^{-1}\mathbb Z^2$ 提升，记相应 Siegel 函数为 $g_{(x,y)}$。这个提升保持 $(x,y)\mapsto(x,-y)$ 的复共轭。

对四个层数都有
$$m=2,\qquad 12\mid m|\mathcal O|,$$
以及精确的模 $p$ 关系
$$\sum_{\mathcal O}x^2=\sum_{\mathcal O}xy=\sum_{\mathcal O}y^2=0.$$
独立复核器逐项验证这些有限和。Siegel 函数变换律的二次关系判据因而使
$$U=\prod_{a\in\mathcal O}g_a^2$$
成为层 $p$ 的模函数。对 $G_H$ 的作用，其商因子至多为 $p$ 次单位根；由于 $p\nmid|G_H|$，Kummer 理论消去这一余因子，而上述复共轭相容性使需要的根单位本身为一。故
$$U\in K^+(X_{\rm ns}^+(p)),\qquad U^{\varphi_k}=U_{\mathcal O_k},
\quad\varphi_k(\zeta_p)=\zeta_p^{g^k}.$$
这里用的是通常的模单位变换律及 BBM §§5–6 对该判据的证明，不使用其最终整点计算。

这些单位在非尖点处无零极点，并在整 $j$ 点取代数整数值。乘遍全部轨道得到
$$\prod_{k=0}^{d-1}U^{\varphi_k}=\pm p^2.$$
也可以直接从全部非零 Siegel 因子的乘积核对：其除子为零，首项由 $x=0$ 的因子给 $\prod_{y=1}^{p-1}(1-\zeta_p^y)^2=p^2$，根单位只影响符号。因此 $U(P)$ 的主理想是 $K^+$ 中唯一的 $p$ 上方素理想的平方。

取
$$\eta_0=(1-\zeta_p)(1-\zeta_p^{-1}),\qquad
\eta_{j-1}=\zeta_p^{(1-j)/2}\frac{1-\zeta_p^j}{1-\zeta_p}\quad(2\le j\le d),$$
其中半整数指数按模 $p$ 解释；不同符号不影响绝对值。圆分单位的指数公式及 Miller 的无条件类数一定理说明 $\eta_1,\ldots,\eta_{d-1}$ 是模正负号的完整单位基。故存在真正整数 $b_i$，且 $b_0=2$，使
$$U(P)=\pm\prod_{i=0}^{d-1}\eta_i^{b_i}.                 \tag{101.1}$$
这一步的整数性是后面逼近见证的依据，不能只取一个未证明饱和的单位子格。

## 4. 区间中从零构造正确的矩阵

定义精确实数
$$L(a)=\log\bigl(2\sin(\pi a/p)\bigr),\qquad 1\le a<p.$$
其对数矩阵以**嵌入为行、单位为列**：
$$E_{k0}=2L(g^k),\qquad E_{k,j-1}=L(jg^k)-L(g^k),       \tag{101.2}$$
参数均先取 $1,\ldots,p-1$ 的剩余类。令 $A=E^{-1}$，则 (101.1) 给 $b=A\lambda$。

对尖点 $t$ 和嵌入 $k$，遍历 $(x,y)\in\mathcal O_k\sigma_t$，取 $0\le x,y<p$，令
$$
V_{t,k}=-m\sum\frac{6x^2-6px+p^2}{12p^2},\qquad
W_{t,k}=m\sum_{x=0}L(y).                               \tag{101.3}
$$
于是斜率和常数项是
$$\delta_t=AV_t,\qquad\theta_t=AW_t.                    \tag{101.4}$$
它们没有转置 $A$。范数恒等式给 $\delta_{t,0}=0$、$\theta_{t,0}=2$；程序同时核对这两个恒等式。逼近所用分母只从 $\delta_{t,i}\ne0$ 的 $i>0$ 选取，从不除以零坐标。

所有超越量使用 Arb 严格球运算计算到 4096 比特；第一份实现使用精确有理参数的 $\sin(\pi a/p)$，独立复核器使用严格区间的 $\pi a/p$ 再求正弦。没有先用浮点求代数数嵌入、再人为加末位误差的步骤。矩阵逆的误差由 Arb 传播，证书另将
$$\kappa=\max_i\sum_k|A_{ik}|$$
向上包在一个分母为 $2^{64}$ 的有理数内。下文用这个有理上界，仍记为 $\kappa$。

## 5. 自含的余项界及初始界

在标准基本域有 $r=|q|\le e^{-\pi\sqrt3}<1/200$。置 $z=r^{1/p}$。Siegel 乘积中，第一坐标非零时，除去 Bernoulli 首项后的绝对对数之和至多
$$\frac{2z}{(1-z)(1-r)}.$$
因为 $r<e^{-5}$，且 $1-e^{-5/p}\ge5/(p+5)$，对 $p\ge7$ 有
$$\frac{2}{(1-z)(1-r)}\le\frac{400(p+5)}{995}<p.$$
第一坐标为零时先取出 $1-\zeta_p^y$，其余项至多 $2r/(1-r)^2<pz$。根单位不影响绝对值，所以每个因子的余项都被 $p r^{1/p}$ 控制。

乘以 $m|\mathcal O|$，再作用 $A$，得到对**全部**坐标成立的界
$$b_i=\delta_{t,i}s+\theta_{t,i}+e_i,\qquad
|e_i|\le\Theta e^{-s/p},\qquad
\boxed{\Theta=\kappa mp\,2(p+1).}                       \tag{101.5}$$
这里保留了安全界中的因子 $p$。

为明确初始界只依赖已发表的有效高度定理，设 $d_0\ge3$ 是 $(p-1)/2$ 的最小约数。Bajolet–Sha 的 Theorem 1.1 给
$$\log|j(P)|<\Omega_p,
\qquad\Omega_p=30^{d_0+5}d_0^{-2d_0+9/2}p^{6d_0+5}(\log p)^2.$$
$j=0$ 单独按零值处理，不影响以下估计。

我们还直接给一个宽松的 $j$ 级数界，避免依赖旧程序的数值 $j$ 函数。由
$$j(q)=\frac{E_4(q)^3}{q\prod_{n\ge1}(1-q^n)^{24}}$$
及非负级数系数，在 $0<r\le1/200$ 上有
$$
|j(q)-q^{-1}|
\le\frac1r\left[
\frac{\left(1+\frac{240r(1+4r+r^2)}{(1-r)^5}\right)^3}
 {1-\frac{24r}{(1-r)^2}}-1\right]<10000.                \tag{101.6}
$$
其中 $\sum n^3r^n=r(1+4r+r^2)/(1-r)^4$；乘积用
$-\log(1-r^n)\le r^n/(1-r^n)$ 和 $e^x\le(1-x)^{-1}$ 控制。右边除以 $r$ 后仍有非负系数，故只需代入 $r=1/200$；所得有理数小于 $2410$，复核器作精确有理比较。

由 (101.6)，$e^s\le|j(P)|+10000\le e^{\Omega_p}+10000$，从而可取
$$S_0=\left\lceil\Omega_p+10000\right\rceil,\qquad s\le S_0. \tag{101.7}$$
这里的初始上界来自 Bajolet–Sha，不引用 BBM 的有限层整点分类。

## 6. 单个整数见证为什么能严格缩小界

假设已经知道 $s\le S$。选 $i,j>0$、$i\ne j$、$\delta_i\ne0$，置
$$a=\delta_j/\delta_i,\qquad \ell=a\theta_i-\theta_j.$$
由 (101.5)，
$$|b_j-a b_i+\ell|\le(1+|a|)\Theta e^{-s/p},\qquad
|b_i|\le B:=\left\lceil|\delta_i|S+|\theta_i|+\Theta\right\rceil.$$

证书给出整数 $R>0,n,h$，并用区间检查
$$|R\ell-h|<1/2,\qquad
|R\ell-h|-B|Ra-n|\ge\frac{G}{2^{64}}>0,                \tag{101.8}$$
其中 $G$ 是证书中的正整数。因为 $Rb_j-nb_i$ 为整数，三角不等式给
$$R(1+|a|)\Theta e^{-s/p}
\ge\|R\ell\|-|b_i|\,|Ra-n|
\ge G/2^{64}.$$
于是
$$\boxed{s\le p\log\frac{R(1+|a|)\Theta\,2^{64}}{G}.}  \tag{101.9}$$
把右端向上取整便得到下一步整数 $S'$。复核器只检查 (101.8)–(101.9) 和 $S'<S$，无需相信搜索器的连分数选择，也不要求一个启发式搜索循环必定终止。保存的 328 个见证已经构成实际完成的有限链。

对全部 113 个尖点分别应用这些链，得到 §1 的统一界。由 (101.6)，
$|j(P)|\le e^{S_p}+10000<e^{S_p+1}$，给出表中的高度推论。

## 7. 独立复算覆盖了什么

生成器先选实际 Cartan 矩阵 $M_k$，逐向量计算 $\mathcal O M_k\sigma_t$。复核器使用不同的有限枚举：对每个非零目标向量 $(x,y)$，先乘 $\sigma_t^{-1}$，再按
$$\xi x_0^2-y_0^2\in\{g^k,-g^k\}$$
直接分桶。它不调用生成器的轨道函数，也不使用保存的近似斜率；所有 Bernoulli 和、首项计数及矩阵 $A$ 都重新计算。

复核覆盖每个尖点、每个嵌入、每个整数见证；每次约化的输入上界与上一条输出严格衔接，最后检查最大值。初始有效定理、圆分单位饱和性以及 Siegel 变换律是明确列出的数学输入，其余有限与数值步骤均可重新执行。

- [生成器](../scripts/small_levels_archimedean_reduction.py)。
- [独立复核器](../scripts/verify_small_levels_archimedean_reduction.py)。
- [完整证书](../scripts/data/small_levels_archimedean_reduction.json)：301629 字节；SHA256 `0b4d761752b07f3410a18d2e16eeb7f6bde98add4214bf889c0188fd410ba159`。

~~~sh
python3 -B topics/serre-uniformity/scripts/small_levels_archimedean_reduction.py
python3 -B topics/serre-uniformity/scripts/verify_small_levels_archimedean_reduction.py
~~~

依赖为 `python-flint` 的 Arb；本轮使用 0.9.0。全部生成及独立复核均已实际通过，不含 GRH 选项。数据并未包含剩余紧区间的完整覆盖树、格点排除或最终候选识别；它们是继续计算的对象。

## 8. 原始来源与用途边界

1. A. Bajolet、M. Sha，*Bounding the j-invariant of integral points on X_ns^+(p)*，Proc. Amer. Math. Soc. **142** (2014), 3395–3410，[作者全文](https://arxiv.org/pdf/1203.1187)，Theorem 1.1；用于唯一的初始高度界。其 §4.1 同时明确圆分单位生成元及单位指数等于实类数。
2. J. C. Miller，*Real cyclotomic fields of prime conductor and their class numbers*，[作者全文](https://arxiv.org/html/1407.2373v1)，Theorem 1.1 的无条件部分：实圆分域在素数导子不超过 151 时类数一。本文不用同定理后半的 GRH 结果。
3. A. Bajolet、Y. Bilu、B. Matschke，*Computing integral points on X_ns^+(p)*，Algebra & Number Theory **15** (2021), 569–608，[作者 v4](https://arxiv.org/html/1212.0665v4)，§§5–7 的 Siegel 单位变换、整数指数关系及尖点描述。本文自行给余项和单见证证明，并重写全部数值入口，不引用其 Theorem 1.1 的整点分类。
4. [先前公开代码审计](../notes/2026-11-12-bbm-public-code-audit-and-p47-boundary-resume2.md)：记录矩阵方向、误差盒及浮点转换的具体边界。本文的证书修复了第一阶段所需的入口；尚未据此声称整个旧整点证明已修复。

## 9. 逐整数坐标包围给出的更强尾部界

本节继续使用同一套精确模单位，没有施加实数 $q$ 或小惯性等附加条件。新的完整结论是
$$
\boxed{s\le246,282,354,508\quad\text{分别对应 }p=41,47,59,83.}
\tag{101.10}
$$
相应的 $\log\max(1,|j|)$ 分别小于 $247,283,355,509$。

### 9.1 利用每个第一坐标至多四点

固定尖点矩阵 $\sigma=\left(\begin{smallmatrix}u&b\\v&w\end{smallmatrix}\right)$，其尖点标号为 $c=u^2-\xi v^2\ne0$。目标向量 $(x,y)\in\mathcal O_k\sigma$ 满足
$$
\xi(wx-vy)^2-(-bx+uy)^2\in\{g^k,-g^k\}.
$$
固定 $x$ 后，这是两条关于 $y$ 的二次方程，二次项系数恒为 $-c\ne0$。所以每个 $x$ 至多出现四个 $y$，不需要使用整个轨道大小作粗略乘数。

置 $t=e^{-s/p}$、$r=t^p$。对 $x=1,\ldots,p-1$，Siegel 乘积两侧余项的绝对值之和，使用 $|\log|1-z||\le |z|/(1-|z|)$，至多为
$$
8\sum_{x=1}^{p-1}\sum_{n\ge0}\frac{t^{x+np}}{1-t^{x+np}}
\le \frac{8t}{(1-t)^2(1-r)}.
$$
$x=0$ 时已在 $W$ 中取出 $1-\zeta_p^y$，剩余部分至多
$$8\sum_{n\ge1}\frac{r^n}{1-r^n}\le\frac{8r}{(1-r)^2}.$$
乘模单位指数 $m=2$ 并作用 $A$，得到全部坐标同时成立的严格界
$$
\left|b_j-\delta_js-\theta_j\right|\le\varepsilon_p(s),
\qquad
\boxed{\varepsilon_p(s)=16\kappa\left(
\frac{t}{(1-t)^2(1-t^p)}+\frac{t^p}{(1-t^p)^2}\right).}
\tag{101.11}
$$
其右边正且严格递减。这一证明只使用绝对值，覆盖全部复相位及每个 $\sigma T^r$ 分支。

### 9.2 有限整数枚举和包围步骤

对每个尖点，从已认证的 $s\le S_c$ 出发，令 $L=6p$，只考察 $[L,S_c]$。选一个 $i>0$ 且 $\delta_i\ne0$。所有可能的整数 $n=b_i$ 均在
$$
\delta_i[L,S_c]+\theta_i+[-\varepsilon_p(L),\varepsilon_p(L)]
\tag{101.12}
$$
中，因而形成一段完整的有限整数范围。搜索器选最大斜率仅为效率；证书检查不依赖其最大性。

固定其中一个 $n$。若目前已知 $s\in[a,b]$，则由 (101.11) 和单调性，所有可能值仍位于
$$
[a,b]\cap\left(
\frac{n-\theta_i}{\delta_i}
+\left[-\frac{\varepsilon_p(a)}{|\delta_i|},
\frac{\varepsilon_p(a)}{|\delta_i|}\right]\right).
\tag{101.13}
$$
将上下端分别向下、向上取到分母 $2^{64}$ 的有理数后，再和原区间相交。重复三次始终保留全部真实解；不要求收缩收敛、坐标单调或导数非零。

区间为空即排除这个 $n$。否则对另一个 $j>0$ 检查
$$
\delta_j[a,b]+\theta_j+[-\varepsilon_p(a),\varepsilon_p(a)].
\tag{101.14}
$$
若此区间没有整数，则该 $n$ 也被排除。一个仍通过的区间只登记为**候选带**；不声称其中存在整点，也不要求它通过所有其余几何条件。

对所有尖点和 (101.12) 中的每个整数实际完成此过程，结果为：

| $p$ | 尾部起点 $L$ | 检查的整数总数 | 未被本测试排除的带数 | 全局上界 |
|---:|---:|---:|---:|---:|
| 41 | 246 | 7626 | 0 | 246 |
| 47 | 282 | 12044 | 0 | 282 |
| 59 | 354 | 21340 | 0 | 354 |
| 83 | 498 | 45225 | 7 | 508 |

最后七条带的全部有理端点存于证书，其上端均小于 $508$。因此 (101.12) 以下的 $s<L$ 与所有保留带合在一起，严格给出 (101.10)。

### 9.3 新证书及独立复核

- [尾部生成器](../scripts/small_levels_archimedean_tail.py)。
- [独立尾部复核器](../scripts/verify_small_levels_archimedean_tail.py)。
- [逐整数排除证书](../scripts/data/small_levels_archimedean_tail.json)：185148 字节，SHA256 `83da73c7083ea6197478a91c4a766d93ebea88af07bf667b4c926e75a564e69a`。

生成使用 256 比特 Arb；独立复核以 384 比特重新构造对数矩阵和精确斜率，并以 $\pi a/p$ 的严格正弦替代生成器的有理参数正弦。它核对已发布初始证书的哈希和每个尖点的非零二次项；逐一检查整数范围覆盖、三次向外收缩、保存的排除坐标及七条保留带的有理包含关系。保存的坐标只指定检查哪一条不等式，不能直接决定通过。

~~~sh
python3 -B topics/serre-uniformity/scripts/small_levels_archimedean_tail.py
python3 -B topics/serre-uniformity/scripts/verify_small_levels_archimedean_tail.py
~~~

本节只给高度界；界以下的完整实相位覆盖和最终整数识别见已完成的 R109。

## 10. 中间的全部1727个整数 $j$ 已独立排除

对四个层数均有
$$\boxed{j(X_{\rm ns}^+(p)(\mathbb Q))\cap\{1,\ldots,1727\}=\varnothing.}\tag{101.15}$$
此步骤直接使用精确有限域点数，不要求继续模单位数值计算。

给定其中一个整数 $j$，取
$$k=\frac{j}{1728-j},\qquad E_j:y^2=x^3+3kx+2k.$$
其 $j$ 不变量确为指定整数。对每个保存的素数 $q\ge5$，证书检查
$$q\ne p,\qquad q\nmid j(1728-j),$$
所以显示模型在 $q$ 好约化。准确计数得到 $a=a_q(E_j)$，并验证
$$a\not\equiv0\pmod p,\qquad a^2-4q\text{ 为模 }p\text{ 的非零平方}.\tag{101.16}$$

非分裂 Cartan 中的元素，要么为标量，要么其特征多项式在 $\mathbb F_p$ 不可约；正规化子外陪集的元素迹为零。(101.16) 给出两个互异的 $\mathbb F_p$ 本征值且迹非零，因此这个 Frobenius 不在任何共轭的非分裂 Cartan 正规化子中。

因 $j\notin\{0,1728\}$，任意同 $j$ 的有理椭圆曲线都是 $E_j$ 的二次扭曲。二次扭曲对整个模 $p$ 表示只乘标量 $\pm I$；所有这些标量已在正规化子中，故表示是否包含于其某个共轭与扭曲无关。因此上述反证适用于**所有**同 $j$ 曲线，包括在所选 $q$ 处分歧的扭曲；没有给原曲线另加好约化假设。

完整证书为每层保存全部 $j=1,\ldots,1727$ 的一条三元组 $(j,q,a)$。四层实际使用的最大见证素数依次为 $61,59,53,47$。生成时按 Legendre 符号求迹；复核时重新枚举平方值的重数，直接计算整个有限群的点数，并在 $\mathbb F_p$ 枚举判别式平方根。

- [生成及独立点数复核](../scripts/small_levels_middle_j.py)。
- [完整6908条见证](../scripts/data/small_levels_middle_j.json)：准确记录数为 $4\cdot1727=6908$，79333 字节；SHA256 `2ba3b061b51fd0206857c3bd5c159c78c9df58b4b321a4ac9605f265fa2a4fb7`。

~~~sh
python3 -B topics/serre-uniformity/scripts/small_levels_middle_j.py --check
~~~

这一有限区间已完成；$j<0$、$j>1728$ 两段及对应 CM 端点的完整识别由 R109 完成。
