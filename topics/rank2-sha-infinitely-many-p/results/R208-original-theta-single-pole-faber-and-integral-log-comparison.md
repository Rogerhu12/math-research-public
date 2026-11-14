# R208 — 原 theta 两权的单固定极点模型、整 Faber 留数与除 p 后继式

日期：2026-11-12。**状态：下述原有限 jet、单固定极点、整 exact/log 分解及原目标格比较均已证明。没有证明无穷多个目标素数处的非零。**

本篇支付 [R202](R202-rational-elliptic-parameter-and-unit-cartier-obstruction.md) 之后的原点单分支问题：不用整个 $Z=0$ 纤维的迹，不要求全局有理椭圆对数提升到模 $p^2$。保留 [R197](R197-actual-two-weight-determinant-and-common-theta-gauge.md) 的同一个 theta gauge、原两列及原两权，给极点次数 $O(p)$、在 $\mathbf Z_p$ 上成立的固定曲线模型。它与 R197 的有限系数证书等价，并没有凭重写取得新的非零定理。

## 1. 原对象与准确窗口

固定原曲线、微分及形式参数
$$
 E_0:y^2=x^3-x,\qquad \omega=\frac{dx}{2y}=dz,\qquad
 u=x^{-1/2},\quad s=u^4=x^{-2},\quad w=z^4.
$$
$u$ 可在 R202 的固定二同源覆盖上读取；$s$ 是原 $E_0$ 上的全局有理函数。以下所有全局函数都在 $E_0$ 上。

令
$$
 F(s)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}s^j,\qquad
 W(s)=sF(s)^4,\qquad z=uF(s),\quad w=W(s).
 \tag{1}
$$
保留 R197 的原次数十六多项式
$$
\begin{aligned}
 J(s)&=s(1-2s+5s^2)(5-2s+s^2)/5,\\
 H_1(s)&=1+4s+70s^2+4s^3+s^4,\\
 H_2(s)&=1+20s-26s^2+20s^3+s^4,\\
 Q_8(s)&=1+364s^2-1088s^3+1190s^4-1088s^5+364s^6+s^8,\\
 P(s)&=J(s)(1-s)^2(1+s)H_1(s)H_2(s),\\
 Q(s)&=J(s)(1-s)(1+s)^2Q_8(s).
\end{aligned}
 \tag{2}
$$
于是原两截面为
$$
 A_2=\vartheta(z)^{68}P(s),\qquad B=\vartheta(z)^{68}Q(s),
 \qquad P(s)=s+\cdots,\quad Q(s)=s+\cdots.
$$

取惰性素数 $p=4r-1\ge31$，$O=\mathbf Z_p$。写
$$
 \log\vartheta(z)=\sum_{j\ge1}k_jw^j,\qquad
 \widehat K_p(w)=
 \sum_{\substack{1\le j\le2r-1\\j\ne r}}k_jw^j.
 \tag{3}
$$
R197 已证明这些保留的 $k_j$ 均在 $O$ 中，唯一删去项是原 $k_r$，$v_p(k_r)=-1$；所有相关尺度、原第一行和第二行的整消去均已确定。

定义一个实际有限多项式
$$
 \boxed{\quad
 \Gamma_p(s)=
 \left[\exp\!\bigl(68\widehat K_p(W(s))\bigr)\right]_{\deg_s\le2r-1}
 \in O[s].
 \quad}
 \tag{4}
$$
这里 $W(s)$ 只读至相应有限次数。(1) 的分母在该窗口内素于 $p$，指数的阶乘也小于 $p$，所以 (4) 的整性直接成立。置
$$
 f_{p,A}(s)=\Gamma_p(s)P(s),\qquad
 f_{p,B}(s)=\Gamma_p(s)Q(s).
 \tag{5}
$$
两个多项式都从 $s$ 开始，且
$$
 \deg f_{p,F}\le L:=2r+15=\frac{p+31}{2}\le p.
 \tag{6}
$$

**有限 jet 的准确性。** (4) 的截断误差在 $s^{2r}$ 中；乘上 $P$ 或 $Q$ 后在 $s^{2r+1}$ 中。$W(s)$ 首系数为一，因此对 $n=r,2r$，
$$
 \widehat R_{n,F}
 :=[w^n]f_{p,F}(s(w))
 =[w^n]e^{68\widehat K_p(w)}
       \begin{cases}P(s(w)),&F=A,\\Q(s(w)),&F=B.\end{cases}
 \tag{7}
$$
右边就是 R197 的两条原 gauged 行。这个等式在 $\mathbf Q_p$ 中准确成立，因而同时保留模 $p^N$ 的任意精度；不是只保留模 $p$ 的代理。

(4) 不宣称原 theta 截面本身是全局有理函数，也不改动其正次数线丛。它只是原指定有限 jet 的一个有理代表，所有系数均由同一个原 theta 和同一个已付 gauge 给出。

## 2. 只在原点有极点的整 Faber 函数

记
$$
 T=x^2=s^{-1}.
$$
对 $n=r,2r$ 定义
$$
 \boxed{\quad
 \mathcal F_n(T)
 =\sum_{j=0}^{n}
     [s^j]F(s)^{-4n}\,T^{n-j}
 =\bigl[z(T)^{-4n}\bigr]_{\text{在 }T=\infty\text{ 的非负幂}}.
 \quad}
 \tag{8}
$$
最后一式表示 Laurent 展开的多项式部分，不要求 $z$ 在全局成为有理函数。

(1) 至 $s^{2r}$ 的分母仍素于 $p$：此范围中 $4j+1<3p$，不可能等于 $p$ 或 $2p$。因此
$$
 \mathcal F_n\in O[T],\qquad \deg\mathcal F_n=n,\qquad
 \text{首系数}=1.
 \tag{9}
$$
在原点 $O_E$ 处，$T^{-1}=s=z^4+\cdots$，故
$$
 \mathcal F_n(T(z))=z^{-4n}+O(z^4).
 \tag{10}
$$

令 $D=d/\omega$。原曲线给
$$
 Dx=2y,\qquad DT=4xy.
$$
定义
$$
 \boxed{\quad
 \mathcal H_n
 =-\frac1{4n}D\mathcal F_n
 =-\frac{xy}{n}\mathcal F_n'(T).
 \quad}
 \tag{11}
$$
由于 $n<p$，(11) 仍是整函数。它只在 $O_E$ 有极点，准确主部为
$$
 \mathcal H_n=z^{-4n-1}+O(z^3).
 \tag{12}
$$
这已隔离原点所需的完整主部，极点阶只有 $4n+1\le2p+3$。没有为 $Z=0$ 的其他分支逐点制造高阶零，也没有 $O(p^2)$ 的分支投影代价。

## 3. 原留数移到一个固定极点

固定 $T_0=(0,0)\in E_0$。$s=x^{-2}$ 只在 $T_0$ 有极点；$T=x^2$ 在 $T_0$ 有四阶零，在 $O_E$ 有四阶极点。定义原微分
$$
 \Omega_{n,F}=f_{p,F}(s)\,\mathcal H_n\,\omega.
 \tag{13}
$$
它只可能在 $O_E,T_0$ 有极点。由 (7)、(12)，
$$
 \operatorname{Res}_{O_E}\Omega_{n,F}=\widehat R_{n,F}.
 \tag{14}
$$
这里原 theta 的有限 jet、原 $P/Q$、权 $4n$ 以及原 $\omega=dz$ 都已保留。

由 (11)，这个微分准确从 $\mathbf P^1_T$ 拉回：
$$
 \Omega_{n,F}=\pi_T^*\eta_{n,F},\qquad
 \eta_{n,F}
 =-\frac1{4n}f_{p,F}(T^{-1})\mathcal F_n'(T)\,dT.
 \tag{15}
$$
在 $T_0$ 的分歧指数是 $4$，且 $p\ne2$；留数拉回因此乘 $4$。全局留数定理给
$$
 \boxed{\quad
 \widehat R_{n,F}
 =\frac1n\operatorname{Res}_{T=0}
       f_{p,F}(T^{-1})\mathcal F_n'(T)\,dT.
 \quad}
 \tag{16}
$$
该式是单个固定有理点的留数，没有剩余的移动零纤维和未读分支。

展开 (8)，也可写为
$$
 \widehat R_{n,F}
 =\frac1n\sum_{k=1}^n k\,[s^k]f_{p,F}(s)
           [s^{n-k}]F(s)^{-4n}
 =\frac1n[s^{n-1}]f'_{p,F}(s)F(s)^{-4n}.
 \tag{17}
$$
这准确恢复 R162/R197 的 Lagrange 系数式。新增的是其单固定极点的整全局实现和下面的单位分母控制；(17) 本身不提供非零。

## 4. 整 exact/log 分解与真正的下一 p 位

写
$$
 \eta_{n,F}=\sum_j a_{n,F,j}T^j\,dT.
$$
由 (6)、(9) 及 $f_{p,F}(0)=0$，
$$
 a_{n,F,j}\in O,\qquad -L\le j\le n-2.
 \tag{18}
$$
如果 $j\ne-1$，则
$$
 -p<j+1<p,
$$
所以所有非零 $j+1$ 都是 $O$ 的单位。于是可显式定义
$$
 \mathcal U_{n,F}(T)=
 \sum_{\substack{-L\le j\le n-2\\j\ne-1}}
          \frac{a_{n,F,j}}{j+1}T^{j+1}
 \in O[T,T^{-1}].
 \tag{19}
$$
由 (16)，$a_{n,F,-1}=-\widehat R_{n,F}/4$。因此
$$
 \eta_{n,F}
 =d\mathcal U_{n,F}
       -\frac{\widehat R_{n,F}}4\,d\log T,
$$
拉回原曲线得到本篇的整比较：
$$
 \boxed{\quad
 \Omega_{n,F}
 =d\mathcal U_{n,F}(x^2)
       -\frac{\widehat R_{n,F}}2\,d\log x.
 \quad}
 \tag{20}
$$
所有原函数系数都整，$\pm2$ 是单位；这不是先在 $\mathbf Q_p$ 上分解后忽略一个未知的整指数。

尤其若原第一行已经在 $pO^2$ 中，则对其每个实际原列都有
$$
 \frac{\Omega_{r,F}-d\mathcal U_{r,F}(x^2)}p
 =-\frac{\widehat R_{r,F}/p}{2}\,d\log x.
 \tag{21}
$$
左边先减去已明确给出的整 exact 项后才除 $p$，所以 (21) 是合法的整后继式。它保留 R197 真正需要的 $\widehat R_{r,F}/p\bmod p$；没有从自动为零的未除 $p$ 第一行重复提取信息。

这里控制的是 (18) 这个实际有界 Laurent 格。没有声称整个仿射曲线在特征 $p$ 的所有微分都能用同样的单位分母积分。

### 4.1. 再截一次有限代表，可覆盖全部 $p\ge7$

若只需原两权及其任意 $p$-adic 精度，可以取
$$
 f_{p,F}^{\mathrm{short}}(s)=[\Gamma_p(s)P_F(s)]_{\deg_s\le2r},
 \qquad P_A=P,\quad P_B=Q.
 \tag{21a}
$$
被删的尾从 $s^{2r+1}$ 开始，所以 (7) 的两个原系数完全不变。对这个代表，(18) 的实际范围缩为
$$
 -2r\le j\le n-2,\qquad n=r,2r,\qquad 2r<p.
$$
因此所有非零的 $j+1$ 对每个 $p=4r-1\ge7$ 都是单位。(19)–(25) 的同一整原函数、原第一行除 $p$ 及一次 Cartier 比较全部成立，无须排除 $7,19$。

这里仍用原 $P/Q$ 的实际有限 jet；不是换成任意可选择的多项式。新代表只在 $T_0$ 有至多 $8r=2p+2$ 阶极点。若要比较 R207 的完整有理函数迹，则必须保留相应尾项：有限 jet 的相等不等于完整函数域迹相等。正文保留不截 $P/Q$ 的版本，正是为了明确这个区别。

## 5. Cartier 读取和原 Hurwitz 行列式

约化到 $\mathbf F_p$ 后，(20) 及
$\operatorname{Car}(dH)=0$、
$\operatorname{Car}(d\log x)=d\log x$ 给
$$
 \boxed{\quad
 \operatorname{Car}(\overline\Omega_{n,F})
 =-\frac{\overline{\widehat R}_{n,F}}2\,d\log x.
 \quad}
 \tag{22}
$$
也可直接在 (18) 读取：区间 $[-L,n-2]$ 中唯一满足
$j\equiv-1\pmod p$ 的指数就是 $-1$。因此没有隐藏的第二个 Cartier 分量。
$d\log x$ 在原点的留数是 $-2$，是本题范围内固定非零的参考微分。

令 $\ell_{n,F}$ 为 (20) 的 $d\log x$ 系数。则在原目标整格中准确有
$$
 \widehat R_{n,F}=-2\ell_{n,F},\qquad n=r,2r,\quad F=A,B.
 \tag{23}
$$
若 $\mathcal L$ 为这两个原权和原两列组成的矩阵，R197 给
$$
 \frac{\Delta_p}{p^3}\equiv-16\det\mathcal L\pmod p.
 \tag{24}
$$
在原第一行属于 $pO^2$ 后，其下一位检测准确为
$$
 \det(p^{-1}\widehat R_r,\widehat R_{2r})
 =4\det(p^{-1}\mathcal L_r,\mathcal L_{2r}).
 \tag{25}
$$
没有删原第一行的除 $p$，也没有引入一个额外周期或不同的 theta 规范。

固定参考 $d\log x$ 非零，并不证明 (23) 的任一目标系数非零。当前仍须对真正的 $\Gamma_p$、原 $P,Q$ 和原 Faber 核证明相应系数或除 $p$ 后继式在无穷多个 $p$ 非零。

## 6. 与 R202 的全局不可提升结论相容

R202 排除的是在固定曲线上把原全局有理椭圆原函数提升到模 $p^2$，其误差满足非零的二次 Cartier 障碍。本篇不要求这样的全局函数：

- (8) 只用原形式对数的有限主部，直接产出整多项式；
- (4) 只用原指定 theta 的有限 jet，直接产出整多项式；
- (15) 是原有限目标的准确全局微分，全部极点和整分母已列出；
- (21) 在减去实际整原函数后除 $p$，并没有声称 $dZ=\omega$ 在全局模 $p^2$ 成立。

本篇因而关闭“必须隔离整个 $Z=0$ 纤维才能读取原点”的障碍，也付清此两权窗口中的整留数比较。它没有自动扩展到原完整中央导数的全部无界权，也未证明 R197 的必要失败条件会在无穷素数处被违反。

## 7. 原对象的精确校准

[check-original-theta-faber-residues.js](../scripts/check-original-theta-faber-residues.js)
仅用 JavaScript BigInt 有理运算；[完整输出](../scripts/check-original-theta-faber-residues.json) 与脚本一同保存。没有外部依赖。

校准仍用已经出现过的 $p=43,r=11$。第一算法直接反演原 $w=sF(s)^4$，合成原 theta 的有理级数，再作 R197 指定 gauge。第二算法先把同一 gauge 运输到 $s$，构造 (8)、(15)、(19) 并取固定极点留数。所有等式在有理数中逐项相等，整 primitive 的最低 $43$-赋值为 $0$。

| 原权 | 原 $A_2$ 行模 $43^2$ | 原 $B$ 行模 $43^2$ | 对应模 $43$ |
| --- | ---: | ---: | --- |
| $44$ | $899$ | $1683$ | $(39,6)$ |
| $88$ | $882$ | $1206$ | $(22,2)$ |

原共同 gauge 系数的 $43$-赋值准确为 $-1$，两种构造均保留了它。$\deg\Gamma=21$、$\deg f\le37<43$，因此所有非留数项的积分分母确是单位。
这个样本本身的第一行不为零；它校准原单位与下一精度，不是双完整中央失败的实例，也不是无穷性证明。

## 8. 接着要解决的实际问题

当前新对象已经是同一固定曲线、同一固定极点和同一固定对数方向。具体待付的是
$$
 (\ell_{r,A},\ell_{r,B})\not\equiv(0,0)\pmod p,
$$
在无穷 $p$ 上成立；或在该行可除 $p$ 时，证明 (25) 的真实后继式不为零；也可利用完整更深证书。

R207 的特殊有理迹单位若要进入这里，须证明它与本篇实际的 $\Gamma_p P/Q$ 及 Faber 核之间的整比较。仅有同一个 $d\log x$ 参考方向、一个非零裸有理迹或一个形式维数计数，均不提供这项比较。

