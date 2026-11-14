# R150 附录：秩一物理均值的泛参数完整分类与有限例外集合

## 1. 结论

对原六维物理核以及**全部**原匹配临界条件，不限制 $H,V$ 的秩、共同支持维数或 $T_3$ 的本质变量数。存在一个由原整数方程明确确定的有限代数集合 $\Sigma\subset\mathbb C$，使得每个

$$
y=a\,v(s),\qquad a\ne0,\quad s\in\mathbb C\setminus\Sigma
$$

的完整临界点恰为

$$
\boxed{H=h y^2,\qquad V=\frac{6h-1}{4}y^3,\qquad h\in\mathbb C.}
$$

故这些均值上的全部临界点均有 $T_3=0$。

本条同时证明一个对**每个有限复源点**有效的统一上界：在第 4 节定义的 $224\times155$ 原多项式投影矩阵 $P(s)$ 中，

$$
\boxed{\operatorname{rank}_{\mathbb C}P(s)\le142.}
$$

该上界包括 $A_y$ 秩为 $8$ 的源点，不能把它误读成只在 $A_y$ 满泛秩处可用。它的证明先在 $\mathbb Q(s)$ 构造十三个独立右核，再用多项式子式恒等式专门化；从未将参数依赖的 primitive 行除数在其零点使用。

$\Sigma$ 的精确定义见第 6 节。本文没有完成其枚举或排除，不把“有限例外”写成“无例外”，也不把泛参数结论当作原 ISP 已完成。

## 2. 原中心方程、投影与记号

依[完整中心归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)，可先按权重齐次性取 $y=v(s)$，令

$$
M=H-\frac12y^2,\quad p=Ky,\quad
L_y=J_3^{-1}B_yJ_2,\quad A_yM=(L_yM)_p.
$$

最高方程唯一给出 $V=\frac32L_yM+\frac12y^3$。剩余原十七式为

$$
N(Kv(z),Kv(z))=0,\qquad
N=4MKM+6A_yM,
$$

以及

$$
\Gamma(M)=2\operatorname{tr}((KM)^2)y+
8MKMp-12(L_yM):(KMK)=0.
$$

记 $\mathcal H_2$ 为十一维 Hankel 对称矩阵空间。双线性型

$$
\langle X,Z\rangle_K=\operatorname{tr}(KXKZ)
$$

在 $\mathcal H_2$ 上非退化，其 Gram 矩阵为可逆的原 $J_2$。令 $\Pi$ 将任意对称矩阵投影为具有相同物理极线多项式的唯一 Hankel 矩阵。因此

$$
\langle X,\Pi Z\rangle_K=\langle X,Z\rangle_K
\quad(X\in\mathcal H_2).
$$

这一步只重新表示原十一条极线条件；它没有将 $N$ 擅自当成 Hankel 矩阵，也没有额外添加完整矩阵方程 $N=0$。

$A_y$ 对该双线性型自伴随，因为

$$
J_2A_y=J_2B_y^TJ_3^{-1}B_yJ_2
$$

对称。由[全复参数精确秩定理](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)，在函数域 $\mathbb Q(s)$ 上

$$
\operatorname{rank}A_y=9,\qquad
\ker A_y=\operatorname{span}(Y,T),
$$

其中

$$
Y=yy^T,\quad u=v'(s),\quad T=yu^T+uy^T,\quad q=Ku,
$$

$$
y^TKy=y^TKu=0,\qquad
g=u^TKu=-2s^2(s-2)(s+6)\ne0
$$

作为函数域元素非零。$L_yY=y^3$，$L_yT=yT$，所以 $A_yY=A_yT=0$。

以 Hankel 序列平移

$$
m_i=\sum_{j=0}^i\binom ij s^{i-j}z_j
$$

作为坐标，写 $c=z_0,d=z_1$，其余九坐标组成横向矩阵 $Z$。即 $M=cY+dT+Z$。横向理想记为 $I=(z_2,\ldots,z_{10})$。

## 3. 三个必要的形式解系数

本节在 $\mathbb Q(s)$ 上工作。由于 $\langle Y,Y\rangle_K=\langle T,Y\rangle_K=0$，自伴随性保证存在唯一取在横向补空间中的 $r\in\mathcal H_2$，使

$$
6A_yr=-4gY. \tag{3.1}
$$

定义 $b=p^Trp$。我们首先证明

$$
b=0. \tag{3.2}
$$

令 $R=L_yr$，则 $R_p=A_yr$ 是 $Y$ 的倍数，且原最高恒等式为

$$
R(Kv(t),Kv(t),Kv(t))
=p_y(t)\,r(Kv(t),Kv(t)),\qquad p_y(t)=y^TKv(t).
$$

在 $t=s$ 展开。$p_y$ 的二次系数为 $-g/2$，非零。左侧二次项只含 $R(p,p,Kv''(s)/2)$ 和 $R(p,q,q)$；它们均为零，因为 $R_p$ 是 $Y$ 的倍数、$y^Tp=y^Tq=0$。右侧二次项因此给出 $(-g/2)b=0$，即 (3.2)。

再令

$$
S_c=YKr+rKY,\qquad S_d=TKr+rKT .
$$

直接用 $YKY=YKT=TKY=0$、$(KT)^2=gpy^T$ 得

$$
\langle Y,S_c\rangle_K=\langle T,S_c\rangle_K=
\langle Y,S_d\rangle_K=0,\qquad
\langle T,S_d\rangle_K=2gb=0.
$$

所以 $\Pi S_c,\Pi S_d$ 均正交于 $\ker A_y$。自伴随性再次给出横向矩阵 $r_c,r_d$，满足

$$
6A_yr_c=-4\Pi S_c,\qquad
6A_yr_d=-4\Pi S_d. \tag{3.3}
$$

这里的投影 $\Pi$ 不可省略：$S_c,S_d$ 一般并非 Hankel。

对任意 Hankel $Z$，记二次映射 $\Gamma$ 的交叉项为

$$
\mathcal B_\Gamma(X,Z)=\Gamma(X+Z)-\Gamma(X)-\Gamma(Z).
$$

由原张量式直接展开，得到两个完整向量恒等式：

$$
\boxed{\mathcal B_\Gamma(Y,Z)=-12(A_yZ)_p,\qquad
\mathcal B_\Gamma(T,Z)=-24(A_yZ)_q.} \tag{3.4}
$$

例如第一式中，$\tau_2$、$MKMp$、$L_yY:(KZK)$ 三部分的 $p^TZp\,y$ 项分别为 $4,8,-12$ 倍，完全抵消；余下正是 $-12(L_yZ)_{pp}$。第二式中，$p^TZq\,y$ 及 $p^TZp\,u$ 项同样抵消。由于 (3.1)，两式在 $Z=r$ 时均为零。这里使用全部六条 $\Gamma$，没有只用受限均值方向导数。

## 4. 十三个统一右核

取十一变量中总次数 $1$ 至 $5$ 的单项式空间，删掉至少含两个横向变量的列。余下 $155$ 列为二十个纯 $c,d$ 单项式，以及

$$
z_jc^\alpha d^\beta,\quad 2\le j\le10,\quad \alpha+\beta\le4 .
$$

对原十七式乘次数至多三的所有单项式，投影后的完整行空间由以下 $224$ 行生成：

1. 原十七式乘十个次数至多三的纯 $c,d$ 单项式；
2. 五十四个 $z_jd^2c^\alpha d^\beta$，其中 $\alpha+\beta\le2$，各作为单位坐标行。

第二组在 $g\ne0$ 时确实来自原行空间，因为原方程的纯切向部分为 $N=4gd^2Y,\ \Gamma=0$。若 $g=0$，第二组仍可用于定义一个多项式矩阵，但可能额外扩大投影行空间；这只会保留我们需要的上界方向。

定义 $P(s)$ 时，原十七式**统一乘固定非零整数 $D=\det J_3$**，然后做上述整系数平移。未逐源点除以内容。第二组是固定单位行。因此 $P(s)$ 的全部条目属于 $\mathbb Q[s]$，实际上第一组可取整系数。

前十个右核是取出 $c^\alpha$（$1\le\alpha\le5$）和 $c^\alpha d$（$0\le\alpha\le4$）系数的泛函。另定义三个泛函，未列出的单项式取值均为零：

| 泛函 | 纯切向值 | 横向一次值 |
|---|---|---|
| $\varphi_2$ | $\varphi_2(d^2)=1$ | $\varphi_2(z_j)=r_j$ |
| $\varphi_c$ | $\varphi_c(cd^2)=1$ | $\varphi_c(cz_j)=r_j,\ \varphi_c(z_j)=(r_c)_j$ |
| $\varphi_d$ | $\varphi_d(d^3)=1$ | $\varphi_d(dz_j)=r_j,\ \varphi_d(z_j)=(r_d)_j$ |

(3.1) 使 $\varphi_2$ 消去 $N$ 的投影。(3.3) 分别消去 $\varphi_c,\varphi_d$ 在未乘子的 $N$ 上的值；在一次乘子的 $N$ 上，则再次使用 (3.1)。所有更高纯乘子项均因支撑次数而消失。(3.4) 使三个泛函也消去全部六个 $\Gamma$ 及其允许乘子。五十四个附加单位行不在这些泛函的支撑中，故同样被消去。

这十三个泛函在十三个不同纯切向单项式上的值组成单位矩阵，因此线性无关。故

$$
\operatorname{rank}_{\mathbb Q(s)}P(s)\le155-13=142. \tag{4.1}
$$

每个 $143$ 阶子式于是是恒零多项式。将这些多项式直接专门化可得

$$
\operatorname{rank}_{\mathbb C}P(s_0)\le142
\quad\text{对每个 }s_0\in\mathbb C. \tag{4.2}
$$

这包括 $A_y$ 降秩、(3.1)–(3.3) 的某个选定有理表达式有极点、或 $g=0$ 的参数。我们专门化的是多项式子式恒等式，并不在这些点代入带极点的核向量。

## 5. 原大矩阵的泛秩及理想包含

令 $\mathcal M_5(s)$ 为原十七式统一乘 $D$ 后，再乘全部次数至多三的单项式所得 $6188\times4367$ 多项式矩阵。记其行空间为 $\mathcal L_5(s)$，记 $W=(I^2)_{\le5}$，则 $\dim W=4212$。

由 (4.2)，对每个有限源点

$$
\dim\mathcal L_5(s)\le4212+142=4354. \tag{5.1}
$$

[源点 $s=4$ 的完整证书](R150-appendix-rank-one-mean-source-four-complete-critical-classification.md)已经给出

$$
\operatorname{rank}_{\mathbb Q}\mathcal M_5(4)=4354.
$$

那里的 primitive 整数行与这里的固定 $D$ 倍行在该固定点只差非零有理比例，故有理秩相同。因此 $\mathcal M_5(s)$ 在 $\mathbb Q(s)$ 上的秩恰为 $4354$。

若某一具体源点满足 $g(s)\ne0$ 且 $\operatorname{rank}\mathcal M_5(s)=4354$，则 (5.1) 中所有维数不等式均取等，特别有

$$
\dim\pi(\mathcal L_5(s))=142,\qquad
W\subseteq\mathcal L_5(s).
$$

故九个横向坐标的平方均在原十七式的特征零理想中。每个复数临界点因此有 $Z=0$，随后 $N=4gd^2Y$ 的原物理极线迫使 $d=0$。于是 $M=cY$，并得到第 1 节的完整必要充分分类。

## 6. 有限例外的精确定义与后续接口

令 $\Delta(s)$ 为 $\mathcal M_5(s)$ 的全部非零 $4354$ 阶子式在 $\mathbb Q[s]$ 中的首一最大公因式。至少有一个这样的非零子式，因为 $s=4$ 的秩为 $4354$。定义

$$
\boxed{\Sigma=\{s:g(s)\Delta(s)=0\}.} \tag{6.1}
$$

这是由原十七式、原变量平移和确定的次数截断给出的精确有限代数集合。本文没有计算 $\Delta$ 的系数或根。该定义不依赖任一抽样素数，也不以扫描有限域作为例外集合。

原矩阵条目作为 $s$ 的多项式次数至多 $25$：$N$ 的条目次数至多 $20$，$\Gamma$ 的条目至多 $25$。因此任一非零最大子式的次数至多 $25\cdot4354=108850$；这给出一个明确但很粗的有限性界。该界并不声称例外实际有这么多，也没有将所有可能例外排除。

对于满足某个不可约有理多项式的非接触源点，(4.2) 已提供数域上的小投影统一上界 $142$。若在一个良好素数的简单剩余根上，原大矩阵有秩 $4354$，且行系数及该素数的整模型已正确处理，则某个最大子式在该数域非零，因不可约性对全部复共轭根非零。此时可直接使用第 5 节夹逼，无需重新在数域做 $224\times155$ 精确 Gaussian 消元。若模素数大秩较小，该论证不提供相反结论，仍须更换良好素数或另取更锐上界。

本文将尚未处理的非接触物理均值收紧为有限集合中的问题；它不关闭该有限集合，也不证明其他均值类别或自然幂/实际逆。本课题仍未完成。
