# R912 — 原 [p] 除点输入与完整两位边界规范

日期：2026-11-16。**状态：下述完整原来源身份、规范根的两位恢复和 R699 全部有限行的输入精度均已证明。原中央零到这些边界行同时为零的蕴涵仍未证明。**

本篇使用同一条原曲线、同一个严格 Lubin–Tate 坐标及同一个完整 $T_{\rm g}$。没有用 R887 的模 $p$ 有理模型代替原 sigma 的高系数，也没有另选 Frobenius 初值。新的输入是该原曲线的整数倍 $[p]$ 除点多项式；其次数随 $p$ 增长，不是先于 $p$ 固定的覆盖。

## 1. 原规范与完整乘法平均

保持
$$
E:y^2=x^3+b,\qquad b=17,\qquad
\omega=\frac{dx}{2y}=dz,\qquad
\sigma(z)=z+\cdots,\quad y(z)=-z^{-3}+\cdots,
$$
$$
p=6s-1>211,\qquad q=p^2,\qquad d=p+1,\qquad e=p-1,
\qquad
L=2q-p-9=d(2e-1)-6.
\tag{1}
$$
同时排除原四来源的固定坏集。系数环为 R663 的未分歧整数环 $\mathcal O$。

原局部参数 $u=x^{-1/2}\sim z$、严格整坐标及其逆为
$$
v=h(u),\qquad u(v)=vV(v),\qquad V\in1+v^6\mathcal O[[v^6]],
$$
$$
[-p]v=-pv+v^q,\qquad [p]v=pv-v^q=:P(v).
\tag{2}
$$
第二个符号由原 $[-1]v=-v$ 固定。原 $\mu_6$ 作用给 $u(\zeta v)=\zeta u(v)$，所以 $V$ 的第一个可能非恒定次数确为六。

对常数一的正式级数 $U$ 定义
$$
\mathcal N_d U(v)
=\left(\prod_{\zeta^d=1}U(\zeta v)\right)^{1/d},
\tag{3}
$$
始终取常数一的唯一根。$d$ 为单位，故 $\mathcal N_d$ 保整单位，且所得级数只含 $W=v^d$。正式 log 下它就是原完整范数一投影；没有删掉某个非恒等支。

记
$$
V_c=\mathcal N_dV,\qquad
\widetilde T(v)=T_{\rm g}(u(v)),\qquad
\mathcal T(v)=\widetilde T(v)\frac{V(v)}{V_c(v)}.
\tag{4}
$$
R639 和 R663 已给 $T_{\rm g}^{\pm1}$、$V^{\pm1}$ 整。因此
$$
\mathcal T^{\pm1}\in1+v^6\mathcal O[[v^6]],\qquad
\mathcal N_d\mathcal T=1.
\tag{5}
$$
原 $V_c$ 不是可以略去的单位；它将完整出现在第6节的来源式中。

## 2. 原 [p] 除点函数、首一分子及平方根

使用同一个 sigma 定义
$$
\psi_p(P(z))=\frac{\sigma(pz)}{\sigma(z)^q}.
\tag{6}
$$
$p$ 为奇数，故它是原奇倍点除点多项式，属于 $\mathcal O[x]$，在 $O$ 的首项为 $p z^{1-q}$。定义原 $x$ 坐标的乘法分子
$$
\Phi_p(x)=x([p]P)\psi_p(P)^2.
\tag{7}
$$
整数倍加法的整除点递推给 $\Phi_p\in\mathcal O[x]$，次数为 $q$，首项为 $x^q$。等价地可用
$\Phi_p=x\psi_p^2-\psi_{p+1}\psi_{p-1}$；本篇的偶倍点符号仍由 sigma 定义，例如 $\psi_2=-2y$，两个偶因子的积保持该式。

这些整性不要求 $[p]$ 的核在特征 $p$ étale。它们是原好模型上的整倍点多项式身份。由 $\mu_6$ 同变及首项，
$$
u^{2q}\Phi_p(u^{-2})\in1+u^6\mathcal O[u^6].
$$
因此准确的常数一平方根为
$$
\mathcal S_p(u)=\sqrt{u^{2q}\Phi_p(u^{-2})}
\in1+u^6\mathcal O[[u^6]].
\tag{8}
$$
$p\ne2$ 保证该根整且唯一。原正线性项给完整身份
$$
u([p]P)=\frac{u(P)^q\psi_p(P)}{\mathcal S_p(u(P))}.
\tag{9}
$$
左右首项均为 $pu$，所以没有未付的符号。

令
$$
\vartheta(v)=\frac{\sigma(z(u(v)))}{u(v)}\in1+v^6K[[v^6]].
$$
这里先只作特征零正式身份，不把 $\vartheta$ 的全部系数预认为整。由(6)、(9)，
$$
\boxed{\vartheta(P(v))
=\vartheta(v)^q\,\mathcal S_p(u(v)).}
\tag{10}
$$
这是同一原 sigma 的整数倍公式；没有用新的 theta 截面替换它。

## 3. 完整中央规范的精确 q 次幂式

R663 给
$$
z(u(v))=vH(W),\qquad
H(W)=\mathcal H_p(W^e).
$$
保持 R639 的 $h_\sigma=\sigma/z$ 及
$E_c=\exp(\Pi_H\log h_\sigma)$。于是
$$
\vartheta=h_\sigma\frac{H}{V},\qquad
\mathcal N_d\vartheta=E_c\frac{H}{V_c}.
$$
原 $T_{\rm g}=E_c/h_\sigma$ 遂给
$$
\frac{\mathcal N_d\vartheta}{\vartheta}
=\widetilde T\,\frac{V}{V_c}=\mathcal T.
\tag{11}
$$
这一步保留了 $H$，并由同一等式使它准确相消；没有跨越对数边界选一个新的逆。

$p v-v^q$ 与所有 $\zeta\in\mu_d$ 交换，因为 $\zeta^q=\zeta$。所以 $\mathcal N_d$ 与该代入交换。将(10)及其完整平均相除，置
$$
S(v)=\mathcal S_p(u(v)),\qquad S_c=\mathcal N_dS,\qquad
\mathcal A_p(v)=S(v)/S_c(v),
$$
得到
$$
\boxed{\mathcal T(v)^q
=\mathcal T(P(v))\,\mathcal A_p(v).}
\tag{12}
$$
全部量常数一；$\mathcal N_d\mathcal A_p=1$。没有在(12)中留下可自由选择的 $p$ 次或 $p^2$ 次根。

### 3.1 所有首层零点的共同因子确实已支付

(9)还能在同一坐标中给
$$
\boxed{
\psi_p(u(v))
=v^{1-q}(p-v^{q-1})\,\mathcal E_p(v),\qquad
\mathcal E_p(v)=
\frac{V(P(v))S(v)}{V(v)^q}
\in1+v^6\mathcal O[[v^6]].
}
\tag{13}
$$
所以原全部非零 $p$ 挠点由同一个 $p-v^{q-1}$ 因子保留。因 $d\mid q-1$，$v^{1-q}$ 和 $p-v^{q-1}$ 都被原 $\mu_d$ 作用固定。对 Laurent 平均，明确取首项为 $p v^{1-q}$ 的根；它等于
$$
v^{1-q}(p-v^{q-1})\,\mathcal N_d\mathcal E_p.
$$
因此这些因子是在完整商中逐项消掉，而不是忽略了它们的零、极或原相位。

将(13)代回也可写成
$$
\widetilde T(v)^q
=\widetilde T(P(v))\,
\frac{\psi_p(u(v))}{\mathcal N_d(\psi_p(u(v)))}.
\tag{14}
$$
(12)是这个完整式的整单位版本。所有根的首项均已固定；不对不同挠点另选相位。本文没有在 R887 的有理 $Z$ 模型中删除任何额外零点，也没有改变其 CM13 frame。

## 4. 覆盖 R699 全窗的 p⁵ 估计

令
$$
\mathcal R_L=\mathcal O[[v]]/(v^{L+1}).
$$
对任何 $U(v)\in1+v^6\mathcal O[[v^6]]$，都有
$$
\boxed{U(pv-v^q)-1\in p^5\mathcal R_L.}
\tag{15}
$$
证明逐个原单项式。若 $n\ge6$，则
$$
(pv-v^q)^n
=\sum_{j=0}^n(-1)^j\binom nj
p^{n-j}v^{n+j(q-1)}.
$$
$j\ge2$ 时次数至少 $2q+4>L$，不能进入本窗。$j=0$ 的系数属于 $p^6\mathcal O$，$j=1$ 的系数属于 $p^5\mathcal O$。这对所有高 $n$ 同时成立，且每一输出次数只含有限项。证毕。

特别(15)适用于同一个实际 $\mathcal T$。令
$$
\mathscr R_p(v)=\mathcal A_p(v)^{1/q}
\tag{16}
$$
为特征零常数一的唯一正式根。它由完整 $\mathcal A_p$ 定义，不是先降模 $p$ 后选择的根。

从(12)，
$$
\mathscr R_p=\mathcal T\,\mathcal T(P(v))^{-1/q}.
$$
由(15)，$\log\mathcal T(P(v))\in p^5\mathcal R_L$。除以 $q=p^2$ 后属于 $p^3\mathcal R_L$；其指数仍属于 $1+p^3\mathcal R_L$，因为对 $p>2$，
$v_p(p^{3k}/k!)\ge3$。因此
$$
\boxed{
\mathscr R_p\in\mathcal R_L^\times,\qquad
\mathscr R_p\equiv\mathcal T\pmod{p^3\mathcal R_L}.
}
\tag{17}
$$
这里的整性与同余只声明在本篇指定有限窗。没有据(16)声称该根在整个形式级数环上整。

这也是所需精度的关键：原 $p^5$ 误差在规范根中损失准确允许的两位后，仍剩 $p^3$，所以不影响 R699 的两位行。不能把取 $q$ 次根当作不损精度。

## 5. 一个明确的有限输入精度

(16)并不要求把普通 log 的不整项逐个删去。以下给保守而足够的全输入门。

**根的两位唯一性。** 若 $R,R'\in1+v\mathcal R_L$ 为整单位，且
$$
R^q\equiv(R')^q\pmod{p^4\mathcal R_L},
$$
则
$$
R\equiv R'\pmod{p^2\mathcal R_L}.
\tag{18}
$$
取 $(R/R')-1$ 首个不属于 $p^2$ 的系数，次数记为 $n$。此前各系数均在 $p^2\mathcal O$。第 $n$ 次的 $q$ 次幂系数是 $q$ 乘该系数，加上仅由此前系数组成的高次乘积。那些乘积全在 $p^4\mathcal O$（实际至少 $p^6$）；线性项的赋值至多三，矛盾。因此(18)成立。

于是 $\mathcal A_p\bmod(p^4,v^{L+1})$ 唯一决定实际 $\mathscr R_p\bmod(p^2,v^{L+1})$。逐次数恢复时，$q r_n$ 等于已知第 $n$ 个系数减去此前系数的完整 $q$ 次幂交叉项；只在保留这些交叉项后作原准确整除。不能只将 $\mathcal A_p-1$ 除以 $p^2$。

坐标也可以用同一组除点多项式支付。由(9)，$\psi_p,\Phi_p$ 的模 $p^5$ 数据决定原
$$
f(u)=[-p]u=-u^q\psi_p(u)/\mathcal S_p(u)
$$
到所需次数的模 $p^5$ 数据。这里 $u^q\psi_p$ 整且从 $pu$ 起，平方根和逆都只除单位。

R663 的逐次数共轭递推为
$$
h\circ f=(-p\,h+h^q),\qquad h(u)=u+\cdots,
$$
第 $n>1$ 个修正分母是 $(-p)^n+p=p\cdot\mathcal O^\times$。
在全部 $n\le L+1<2q$ 中，已知低系数仅保到模 $p^4$ 已足够形成误差的模 $p^5$：
其不确定项为 $p^4E(u)$，且 $E$ 无常数、一次项；
由 $f(u)\equiv u^q\bmod p$，
$$
E(f(u))\equiv E(u^q)\equiv0\pmod{p,u^{2q}}.
$$
另一侧 $-p\,\delta h$ 属于 $p^5$，而
$(h+\delta h)^q-h^q$ 属于 $p^6$。
所以每一步除以该一个 $p$ 后，得到原 $h_n\bmod p^4$；归纳支付整个窗口。首项一的形式反演不再损失精度，故获得 $V\bmod(p^4,v^{L+1})$。

由此可取完整的充分输入：
$$
\boxed{\psi_p,\Phi_p\text{ 的原模 }p^5\text{ 多项式数据}
\quad\Longrightarrow\quad
V,\mathcal A_p\bmod(p^4,v^{L+1})
\quad\Longrightarrow\quad
\mathscr R_p\bmod(p^2,v^{L+1}).}
\tag{19}
$$
不声称这个五位上界最优。原固定 $b$ 和来源分母按实际精度保留。

平均(3)也无须新增根的自由数据：可用
$\operatorname{Res}_v(v^d-W,S(v))$ 计算完整乘积，再取常数一的 $d$ 次根。只读次数 $\le L$ 时，输入高于 $L$ 的项不可能回到低次。所有 $1/2,1/d$ 次根均为单位 Hensel 操作。

## 6. 回到原四来源与全部两位行

将原四个来源写成
$$
A_\nu(z)=\sigma(z)^{m_\nu}\phi_\nu(P(z)),\qquad
m_\nu=34,72,136,66,
$$
$$
\phi_\nu(P(u))=u^{-(m_\nu-6)}P_\nu(bu^6).
\tag{20}
$$
$P_\nu$ 是 R821 已固定的完整原多项式；对 $34,72$，它们就是 R699(10)。没有改首 $z^6$ 规范，也没有给伙伴另加中央条件。

R699 的实际整单位来源为
$$
A_\nu^{\rm LT}(v)
=V(v)^{-(m_\nu-6)}
\,\widetilde T(v)^{-m_\nu}
\,P_\nu(bv^6V(v)^6).
\tag{21}
$$
由(4)和(17)，得到完整且共同的恢复式
$$
\boxed{
A_\nu^{\rm LT}(v)\equiv
V(v)^6\,V_c(v)^{-m_\nu}\,
\mathscr R_p(v)^{-m_\nu}\,
P_\nu(bv^6V(v)^6)
\pmod{p^3,\ v^{L+1}}.
}
\tag{22}
$$
四个来源使用同一个 $V,V_c,\mathscr R_p$。尤其 $V_c^{-m_\nu}$ 保留全部中央系数；它虽只含 $v^d$，仍会进入原边界卷积，不能设为一。

若记(22)右边为 $A_\nu^\sharp$，则所有所需原系数都可用
$$
b_{\nu,j}\equiv
[v^{d-6+dj}]A_\nu^\sharp\pmod{p^2},
\qquad 0\le j\le2e-2.
\tag{23}
$$
最大读取次数恰为 $L$。对 R699 已付高度与全迹规范的两个原来源 $m=34,72$，原两位判据逐字成为
$$
\begin{aligned}
[v^{d-6+di}]A_m^\sharp
+p[v^{d-6+d(i+e)}]A_m^\sharp&\equiv0\pmod{p^2},
&&0\le i\le e-2,\\
[v^{d-6+d(e-1)}]A_m^\sharp&\equiv0\pmod p.
\end{aligned}
\tag{24}
$$
最后一行少一位和全部 $2p-3$ 个剩余域位均未改变。式(22)对另外两条实际来源也成立；本篇不据此省略它们各自的算术与全局高度前提。

## 7. 已付范围和仍待证明的中央关系

(12)、(17)、(22)支付的是原完整输入，不仅是前五个模 $p$ Gaussian 块。它保留真实 sigma 初值、全部首层除点因子、严格 LT 坐标及原中央单位。R887 的 $P_2$ 或 $P_6P_{m-6}$ 模型在第六块后的实际差没有被宣布为零；这里使用的是由原 $[p]$ 恒等式恢复的完整规范。

其成本仍依赖 $p$：$\deg\psi_p=(q-1)/2$、$\deg\Phi_p=q$、窗口 $L=O(p^2)$，并使用(19)的准确高位。没有把它们加入先于 $p$ 固定的低度 theta 格，也没有用模 $p$ 极帽改写 R700 已有的对数高度界。

原完整 $j_m=0$ 仍须通过 R663(28) 的同一个全连接，才能对(24)给出约束。本篇没有证明一个中央标量迫全部(24)，没有给四个新的算术零，也没有从输入的唯一性推出某个指定系数非零。

### 依赖

- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：同一个完整 $T_{\rm g}$、原 CM 平均及整性。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：原严格整坐标、$[p]v=pv-v^q$、完整边界与原中央连接。
- [R699](R699-original-uniform-two-digit-boundary-criterion.md)、[R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：原完整两位判据、全部输入次数、同一个全迹的高度范围。
- [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)：四个固定全多项式及其独立中央条件。
- [R887](R887-original-z-all-cm-transport-and-exact-hasse-normalization.md)：原有理模型、首差与共同低读者；本篇未改其任何初值或 frame。

本篇是一般符号证明；没有数学数值运行、目标素数扫描或可重算输出文件。
