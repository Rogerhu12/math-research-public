# R907 — 原四块核的真实二步后继、同源末尾与六维零纤维反馈

日期：2026-11-16。**状态：下列原来源二步链、完整末尾条件和真正稳定部分的六维限制已证明。未证明整个四块核稳定，未判定指定 forcing；主目标仍未完成。**

[R902](R902-original-four-block-kernel-and-first-normal-injectivity.md)
和 [R903](R903-original-positive-horizontal-endpoint-and-joint-normal-values.md)
给同一来源的两个端点值单射。本篇继续它们的联合像：
第一法向值若确实能作为另一个原四块核来源的值，则这个后继来源由一个确定的
$F^3$ 修正唯一给出。修正的全部二、三层尾必须同时通过，不能只解首常数。

在原 $r=2$、$C.f_0=3$ 的范围，零纤维给一个明确六维算子。
它只控制真正能够一直续接的实际核部分，不把 $W_T$ 或整个原核认成 Euler 稳定。

## 1. 同一来源与准确窗口

保持 R836/R840/R902/R903 的原十九角曲面、几何整曲线
$C=(F=0)$、光滑点 $P=(0,1)$ 及
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad
\kappa=C^2,\quad
\mathcal E=Y\partial_Y,\quad e=\mathcal EF.
\tag{1}
$$
记
$$
b=\deg_YF,\qquad 3b<p,\qquad p>211,\qquad
\gamma=e(P)\ne0,\qquad F(t,0)\ne0.
$$
只使用已经整返回同一原来源的
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D}.
\tag{2}
$$
$q_{\rm src}$、charge 四十、原 $P_{134}/U_0$ 及全部 Euler 项
仍按 R836 的完整单位下三角运输；本篇 $\mathcal E$ 是运输后的相对算子。

写 $g=\psi\exp\eta$、$\operatorname{ord}\eta=h$。设
$$
\boxed{
h<T\le2h,\quad T-h>\kappa,\quad
L:=\ell_{\rm eff}\ge T-h,\quad 0<L<T,
}
\tag{3}
$$
其中原物理长度仍是
$$
T=s-r-13,\qquad L=\max(\ell-r,0).
\tag{4}
$$
相对 $J$ 另取自己的长度，不代换 (4)。
令 $K=K_{4,T,L}$ 为同一原四块核：
$$
G,\ \mathcal EG,\ \mathcal E^2G
\text{ 在 }Y=g(t)\text{ 上消到 }T,\qquad
\mathcal E^3G(t,g)\in(t^L).
\tag{5}
$$
对同一个 $G$ 记 $V_i(G)=(\mathcal E^iG)|_C$。
由原有限 Taylor 及 (3)，
$$
V_0(G),V_1(G),V_2(G)\in
V_T:=H^0(C,N^3(-TP)).
\tag{6}
$$
$V_T\to H^0(Z,N^3|_Z)$ 单射，其中 $Z=(e|_C)$，因为 $T>2\kappa$。
原全局限制序列和十九角 Euler 保格均保持。

## 2. 实际二步链唯一是一个确定的校正 Euler

定义原线性泛函及真正保格的算子
$$
a(G)=\frac{(\mathcal E^4G)(P)}{6\gamma^3},\qquad
\boxed{\mathcal T G=\mathcal EG-a(G)F^3.}
\tag{7}
$$
$\mathcal T\mathcal H_3\subset\mathcal H_3$，因为 $\mathcal E$ 保原格且
$F^3\in\mathcal H_3$。没有增加来源次数或自由的第四中央条件。

**定理 1。** 对 $G,H\in K$，若作为整个 $C$ 上的限制截面有
$$
V_0(H)=V_1(G),
\tag{8}
$$
则准确有
$$
\boxed{H=\mathcal TG.}
\tag{9}
$$
反之，对给定 $G\in K$，其 $V_1(G)$ 可成为某个原 $H\in K$ 的完整值，
当且仅当 $\mathcal TG\in K$；后继唯一。

**证明。** 对 (8) 作用原有限 Euler 值映射 $D_3$，
$$
V_1(H)|_Z=D_3(V_0(H))
=D_3(V_1(G))=V_2(G)|_Z.
$$
两侧都来自 (6)，故限制单射给 $V_1(H)=V_2(G)$。
于是 $\mathcal EG-H$ 的值和第一法向值同时为零。
原全局限制序列逐次除 $F$，给
$$
\mathcal EG-H=F^2A,\qquad A\in\mathcal H_1.
\tag{10}
$$
不是仅在 $k(t)[Y]$ 中取商。

两来源的第三、第二长行给
$\mathcal E(F^2A)(t,g)\in(t^T)$。
在同一轴上，
$$
\mathcal E(F^2A)(t,g)
=2e(t,\psi)^2\eta\,A|_C\pmod{t^T}.
$$
因此 $\operatorname{ord}_P A|_C\ge T-h>\kappa$，所以
$A|_C=0$，即 $A=cF$、$c\in k$。
得到 $H=\mathcal EG-cF^3$。

最后使用 $H$ 的原第四短行，而非任取 $c$。
因 $L>0$，
$$
0=(\mathcal E^3H)(P)
=(\mathcal E^4G)(P)-6c\gamma^3,
$$
故 $c=a(G)$。反向由 (7) 和 $F^3|_C=0$ 直接成立。证毕。

## 3. 不能省略的两个真实末尾

对 $G\in K$，$\mathcal TG$ 的前两长行自动通过：
$F^3(t,g)$ 的阶为 $3h$，$\mathcal E(F^3)(t,g)$ 的阶为 $2h\ge T$。
其余条件准确为
$$
\boxed{
\begin{aligned}
\mathcal E^3G(t,g)-a(G)\mathcal E^2(F^3)(t,g)&\in(t^T),\\
\mathcal E^4G(t,g)-a(G)\mathcal E^3(F^3)(t,g)&\in(t^L).
\end{aligned}}
\tag{11}
$$
(11) 使用同一个 $a(G)$、同一个 $G$ 和完整轴函数。
首常数已由 (7) 消去，并不代表这两段尾已消失。

在实际较短的范围 $T-h\le L\le h$，(11) 可等价写成
$$
\boxed{
V_3(G)\in V_T,\qquad
V_4(G)-6a(G)e|_C^3\in t^L N^3_P.
}
\tag{12}
$$
确实，
$$
\mathcal E^2(F^3)(t,g)=6e|_C^3\eta\pmod{t^T},
\qquad
\mathcal E^3(F^3)(t,g)=6e|_C^3\pmod{t^L},
$$
且 $\mathcal E^3G(t,g)=V_3+\eta V_4\bmod t^T$、
$\mathcal E^4G(t,g)=V_4\bmod t^L$。
第二式乘 $\eta$ 后全部消到 $T$，这正使用 $h+L\ge T$。
所有被略去的二次 $\eta$ 项在 $T\le2h$ 内合法。

若 $L>h$，则 (11) 的第一行与
$\mathcal E^3G(t,g)\in(t^L)$ 先迫 $a(G)=0$：
$\mathcal E^2(F^3)(t,g)$ 的首项恰在阶 $h$ 且系数为单位。
此时后继存在的条件是原同源的
$$
\mathcal E^3G(t,g)\in(t^T),\qquad
\mathcal E^4G(t,g)\in(t^L),
\tag{13}
$$
仍不是可以免费添加的两条零行。

对已经存在的后继，三值准确为
$$
V_0(H)=V_1(G),\quad V_1(H)=V_2(G),\quad
V_2(H)=V_3(G).
\tag{14}
$$
同时 $H-3bG\in K$ 的值是原 $U_+=V_1(G)-3bV_0(G)$。
这把正、负端点放在同一条链上；没有分别选择端点或把两个单射相加。

## 4. 全部纯 charge 的实际统一原点帽

以下另取 R903 的原 $r=2$、$C.f_0=3$ 范围。
设原类和四条负权链为
$$
C=bS_0+(u+4b)f-\sum\mu_{i,j}E_{i,j}^*,\qquad
e_+=C.H_+=u+4b-\sum_{i\in\mathcal N}\mu_{i,1}.
\tag{15}
$$
$\mathcal N$ 包括 $0$、$h_7$ 的两个几何根和 $1$。

**引理 2。** 对任意原纯 charge 截面
$G=a(t)Y^n\in\mathcal H_3\setminus\{0\}$、$0\le n\le3b$，有
$$
\boxed{\operatorname{ord}_0a\le3(e_++\mu_{0,1}).}
\tag{16}
$$

**证明。** 原全截面帽给 $\deg a\le3u+4n$。
在每个非零有限负权底点 $i\ne0$，第一吹起框为
$a(t)x^{3b-n}$，所以实际重数要求
$$
\operatorname{ord}_{t_i}a\ge
\max\{0,n-3(b-\mu_{i,1})\}.
$$
故
$$
\operatorname{ord}_0a\le
B(n):=3u+4n-
\sum_{i\in\mathcal N,\ i\ne0}
\max\{0,n-3(b-\mu_{i,1})\}.
\tag{17}
$$
有三项扣除，且 $0\le\mu_{i,1}\le b$。
$n$ 每增加一，$B(n)$ 至少增加一。
因此 $B(n)\le B(3b)=3(e_++\mu_{0,1})$。
所有其它中间角和两条正权链仍是原来源条件；
这里只取必要条件作统一上界。非分裂角按剩余域次数等价计数。证毕。

所以只要
$$
\boxed{T>3(e_++\mu_{0,1}),}
\tag{18}
$$
$K$ 中没有非零纯 charge。
这不是从 R903 的最高 charge 单独推断中间 charge；(17) 支付了每一个。

原 $b\ge5$ 强窗自动满足 (18)：
R819 给 $\kappa\ge(b-3)e_++3b$，而
$\mu_{0,1}\le b-3$，故
$$
2\kappa-3(e_++\mu_{0,1})
\ge(2b-9)e_++3b+9>0,
$$
再用 $T>2\kappa$。

## 5. 零纤维上的明确六维算子

仍在 $C.f_0=3$ 范围。原零角值为 $v_0(F)=-3$；
由完整 Gauss 帽 $v_0(G)\ge3v_0(F)=-9$，得到
$$
f(Y):=F(0,Y),\quad \deg f\le3,\qquad
\deg_YG(0,Y)\le9\quad(G\in\mathcal H_3).
\tag{19}
$$
$f(1)=0$、$f'(1)=\gamma\ne0$。这不要求
$F(0,Y)=Y^2(Y-1)$，也不把因子在 $(0,0)$ 的偶然零赋给整个来源格。

定义
$$
\mathscr A=\{G\in\mathcal H_3:
(\mathcal E^jG)(P)=0,\ 0\le j\le3\}.
$$
原 $K\subset\mathscr A$，而 (7) 给
$\mathcal T\mathscr A\subset\mathscr A$。
零纤维限制把 $\mathscr A$ 映入
$$
\mathscr U=(Y-1)^4 k[Y]_{\le5},\qquad \dim\mathscr U=6.
\tag{20}
$$
这里只是一个实际像的容纳空间，不称 (20) 全部有原全局提升。

其上的准确算子是
$$
T_f g=Yg'-\frac{f(Y)^3}{6\gamma^3}
\bigl[(Y\partial_Y)^4g\bigr]_{Y=1}.
\tag{21}
$$
写 $f=(Y-1)q$、$q(1)=\gamma$、$g=(Y-1)^4h$，则
$$
\boxed{
T_f:h\longmapsto
Yh'+4\,\frac{Yh-(q/\gamma)^3h(1)}{Y-1}.
}
\tag{22}
$$
分子在 $Y=1$ 为零，所得次数至多五。
因此这是明确的六维同来源纤维算子，不含未选的高轴。

置 $c_n=[Y^n]f^3$，缺项补零至 $n=9$。其首一特征多项式为
$$
\boxed{
Q_f(Z)=
\frac{\prod_{n=0}^{9}(Z-n)}{6\gamma^3}
\sum_{n=0}^{9}\frac{c_n}{Z-n},
\qquad \deg Q_f=6.
}
\tag{23}
$$
右端是多项式身份，不要求在 $Z=n$ 分别取分式值。

为证明 (23)，先在整个 $k[Y]_{\le9}$ 上使用 (21)。
四个 Euler jet 的商上，$T_f$ 依次送
$(j_0,j_1,j_2,j_3)$ 到 $(j_1,j_2,j_3,0)$；
其特征多项式为 $Z^4$。
另一方面，秩一行列式公式给全空间的特征多项式
$$
\prod_{n=0}^9(Z-n)
\left(1+\frac1{6\gamma^3}\sum_{n=0}^9
\frac{n^4c_n}{Z-n}\right).
$$
因为 $f^3$ 在 $1$ 恰三重零，
$$
\sum_n n^j c_n=0\ (j=0,1,2),\qquad
\sum_n n^3c_n=6\gamma^3.
\tag{24}
$$
用
$n^4/(Z-n)=Z^4/(Z-n)-(Z^3+Z^2n+Zn^2+n^3)$，
括号恰为 $Z^4\sum c_n/(Z-n)/(6\gamma^3)$。
约去商上的 $Z^4$ 得 (23)。
同一个 (24) 也证明最高项为 $Z^6$，不是只给次数上界。
所有所用小整数在原 $p>211$ 下为单位。

## 6. 真正可以一直续接的原核部分至多六维

定义实际稳定部分
$$
K_\infty=
\{G\in K:\mathcal T^jG\in K\text{ 对所有 }j\ge0\}.
\tag{25}
$$
没有假定 $K_\infty=K$。

**定理 3。** 在 (18) 下，零纤维限制在 $K_\infty$ 上单射，且
$$
\boxed{
\dim K_\infty\le6,\qquad Q_f(\mathcal T)K_\infty=0.
}
\tag{26}
$$

**证明。** 令 $\mathscr A_t$ 为 $\mathscr A$ 中零纤维多项式整体为零的子空间。
此处是 $G(0,Y)\equiv0$，不是只要求 $G(P)=0$。
$\mathcal T$ 在 $\mathscr A_t$ 上准确等于 $\mathcal E$，
因为 (7) 的泛函也为零。
所以 $K_\infty\cap\mathscr A_t$ 是 Euler 稳定子空间。
原 $0,\ldots,3b$ 互异，Euler 在原 charge 分解上半单；
若此交非零，其某个非零纯 charge 投影仍在该交中。
这与 (16)、(18) 及第一长行矛盾。
故零纤维限制单射，给维数界。

$Q_f(T_f)$ 杀整个 (20)，故
$Q_f(\mathcal T)G\in\mathscr A_t$。
若 $G\in K_\infty$，这个同源线性组合仍在 $K_\infty$，
由刚证的交零得 $Q_f(\mathcal T)G=0$。证毕。

(25) 本身还有有限、保原来源的准确测试。令
$$
P_{\rm ch}(Z)=\prod_{n=0}^{3b}(Z-n).
$$
由零纤维及 $\mathcal T|_{\mathscr A_t}=\mathcal E$，
$$
P_{\rm ch}(\mathcal T)Q_f(\mathcal T)\mathscr A=0.
$$
这个首一多项式次数为 $3b+7$，因此
$$
\boxed{
K_\infty=\bigcap_{j=0}^{3b+6}\mathcal T^{-j}K.
}
\tag{27}
$$
后续迭代由同一首一递推决定。
(27) 是真实原四块测试的有限交，绝不是说其中任何一个测试自动成立。

保持 R902/R903 的所有前提时，$\mathcal T$ 和
$\mathcal T-3b$ 在 $K_\infty$ 上都单射：
它们的值分别为 $U_-$ 和 $U_+$。
这仍使用同一个稳定部分，不把端点像作为两个独立维数条件。

### 6.1. 第四短窗严格越过 h 时，没有非零的全续接部分

另设 $L>h$，其余保持 (1)–(5)、(18) 的全部原假设。
则 (26) 可加强为
$
\boxed{K_\infty=0.}
\tag{28}
$
而且有更短的真实有限判据
$
\boxed{\bigcap_{j=0}^{3b}\mathcal T^{-j}K=0.}
\tag{29}
$
这里 (29) 是 $3b+1$ 个实际四块测试的共同核，不把任一单独 $K$ 认成零。

**证明。** 若 $G,\mathcal TG$ 同属 $K$，由 (11) 第一行，
$
\mathcal E^3G(t,g)-a(G)\mathcal E^2(F^3)(t,g)\in(t^T).
$
前一项消到 $L>h$，而
$\mathcal E^2(F^3)(t,g)=6e|_C^3\eta+O(t^{2h})$
的阶准确为 $h<T$，首系数为单位。
所以 $a(G)=0$，后继准确就是 $\mathcal EG$。
这使用原第三长行和第四短行，不只使用 $a(G)$ 的原点定义。

对 $G\in K_\infty$ 逐次应用，$\mathcal T=\mathcal E$ 在整个
$K_\infty$ 上成立；该空间为 Euler 稳定子空间。
原 $0,\ldots,3b$ 的 charge 互异，若空间非零，
某个非零纯 charge 投影仍在其中。
(16)、(18) 和第一长行排除它，证明 (28)。

为证明有限式，设 $\mathcal T^jG\in K$ 对 $0\le j\le3b$ 成立。
对相邻两项逐次使用上段，得
$
\mathcal T^jG=\mathcal E^jG\in K\qquad(0\le j\le3b).
$
Lagrange 投影多项式
$
\pi_n(Z)=
\prod_{\substack{0\le m\le3b\\m\ne n}}\frac{Z-m}{n-m}
\qquad(0\le n\le3b)
$
次数为 $3b$，全部分母在原 $3b<p$ 范围为单位。
因此每个实际纯 charge 分量
$\pi_n(\mathcal E)G$ 是上述同来源迭代的线性组合，仍在 $K$ 中。
原统一帽逐项迫其为零，故 $G=0$。证毕。

所以每个非零 $G\in K$ 必在至多 $3b$ 次实际后继测试之内失败。
这不指定失败的是 (11) 的哪条尾，也不把这些额外测试作为四个原中央已经给出的条件。
同 $q_{\rm src}$、十九角、原十三行带、完整 $R/S$ 和所有未读尾均保持；
特别 (28)–(29) 不能用于声称整个非稳定核已经消失。

## 7. 原 forcing 与剩余范围

对任意已存在的二步链，(11) 是第二、第三层必须共同通过的完整尾；
(12) 只在明示短窗内化简，(13) 也只在 $L>h$ 使用。
实际常数 $a(G)$ 不能与这两段尾分开选取。

本篇没有把原四条中央的零传给 $\mathcal TG$，
没有把一个核元素自由补成长链，也未证明指定 $[b_0]$
在 (26) 或原更大 $K$ 上为零或非零。
对同 $R/S$ 或同 $K_{\rm corr}/H_{\rm corr}$ 的仿射问题，
只有先证明其差确为本篇的同源二步链，才能使用这些限制。
物理 $q_{\rm src}$ 的全部 Euler 项、十九边界、原三个十三行带、
末端 $p^4$ 项及原 $\mathcal W_D$ 的其余列全部保持。

依赖：R495 的原全截面与 Gauss 帽，R815/R819 的真实角交数，
R836 的 $D_3$ 与同一来源限制序列，
R840 的第二法向前缀，以及 R902/R903。
本篇为精确代数与原格证明，没有新增数学运行或数值证书。
