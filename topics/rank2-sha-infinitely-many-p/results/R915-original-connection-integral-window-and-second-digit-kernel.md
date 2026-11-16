# R915 — 原完整连接的两窗整性与全阶中央核的第二位

日期：2026-11-16。**状态：下述原连接系数的有限整窗、全阶单位核的加强及其准确模 $p^3$ 修正已证明。原中央零到首边界零的主门仍未闭合。**

本篇始终使用 R663 的同一个严格 Lubin–Tate 坐标、完整 $T_{\rm g}$ 和原连接 $a(W)$。所证明的整性不是给 $a-c$ 换一个整 lift；尤其包括首个 $H$ 分母出现以后原各项之间的实际相消。R710 的通用整 forcing 反门与全部边界补项不变。

## 1. 原规范与结论

保持原好素数门，并令
$$
p=6s-1>211,\qquad q=p^2,\qquad d=p+1,\qquad e=p-1,
$$
$$
E:y^2=x^3+b,\qquad b=17,\qquad
u=x^{-1/2},\qquad
\frac{dz}{du}=(1+bu^6)^{-1/2}.
\tag{1}
$$
令 $v=h(u)$ 为 R663 的首项一整坐标，$u=u(v)$ 为其整逆。准确有
$$
[-p]v=-pv+v^q,\qquad
z(u(v))=vH(W),\qquad W=v^d,\qquad
H(W)=\mathcal H_p(W^e)=1+O(W^e).
\tag{2}
$$
仍记 $\widetilde T(v)=T_{\rm g}(u(v))$。R639/R663 已付 $\widetilde T^{\pm1}$ 整。

原连接和常数为
$$
a(W)=\frac{d}{dW}\log\frac{\sigma(z(u(v)))\widetilde T(v)}v
=c+\sum_{j\ge1}a_jW^j,\qquad
c=[z^{p+1}]\log(\sigma/z),\qquad v_p(c)=-1.
\tag{3}
$$
本篇的第一结论是
$$
\boxed{a_j\in\mathcal O\qquad(1\le j\le2p-3).}
\tag{4}
$$
窗口端点按原 $v$ 次数逐项支付，不能将其延为全部 $a_j$ 整。

取实际 $m=34,72,136,66$，或任意另行有同一来源定义且 $p\nmid m$ 的 $m$。令
$$
L_m=\partial_W+ma(W),\qquad
k(W)=1+dW\frac{H'}H,
\qquad
J_{m,i}=\left[L_m^{-1}\{k(W)W^i\}\right]_{W=0}.
\tag{5}
$$
逆仍是 R663 的同一个严格内盘 Banach 逆；没有改变原中央函数。

R710 已证明存在准确单位 $\varepsilon_{m,i}$，满足
$$
J_{m,i}=(-1)^ii!(mc)^{-i-1}\varepsilon_{m,i}.
$$
本篇将其加强为对**全部** $i\ge0$ 成立的
$$
\boxed{
\varepsilon_{m,i}\in1+p^2\mathcal O,\qquad
\varepsilon_{m,i}\equiv
1+\binom{i+2}{2}\frac{a_1}{mc^2}\pmod{p^3\mathcal O}.
}
\tag{6}
$$
$i$ 不限于 $i<p$。整个 $i!$ 及其实际赋值均保留。

## 2. 原 zeta 在严格 $2p^2$ 窗中的全部非整项

置
$$
\beta_n=\binom{-1/2}{n}
=(-1)^n4^{-n}\binom{2n}{n}\in\mathbf Z_p.
$$
原 Weierstrass zeta 的同一 $u$ 展开是
$$
\Xi(u)=\zeta_{\rm W}(z(u))
=u^{-1}\sum_{n\ge0}\frac{\beta_n b^n u^{6n}}{1-6n}.
\tag{7}
$$
这是由 $d\zeta_{\rm W}/dz=-x$、原 $dz/du$ 和首项 $u^{-1}$ 积分所得，常数由奇性固定。

本节只读取 Laurent 次数严格小于 $2q$。其中分母 $6n-1$ 至多含一个 $p$。确实 $q\equiv1\bmod6$，而 $6n-1\equiv5\bmod6$；第一个正的、被 $q$ 整除且具有该剩余类的数是 $5q>2q$。

出现一个 $p$ 的全部指标恰为
$$
n=s+pk,\qquad
0\le k\le2s-1,\qquad
6n-1=p(6k+1).
\tag{8}
$$
最后的范围等价于 $p(6k+1)<2q$。每个 $6k+1$ 都是单位；这里没有省略任一共振指标。

在(8)中 $2s<p$、$2k<p$，故中心二项式的 Lucas 公式无进位地给
$$
\beta_{s+pk}\equiv\beta_s\beta_k\pmod p.
\tag{9}
$$
具体地，$\binom{2s+2pk}{s+pk}\equiv\binom{2s}s\binom{2k}k$；因 $p$ 奇且 $4^p\equiv4\bmod p$，符号和 $4$ 的分母也正好给(9)。

令
$$
Z_{<2p}(u)=
\sum_{0\le k\le2s-1}
\frac{\beta_k b^k}{6k+1}u^{6k+1}.
\tag{10}
$$
它是原 $z(u)$ 在次数严格小于 $2p$ 的截断，且属于 $\mathcal O[u]$。一般 $z(u)$ 的第一个可能含 $p$ 的此类分母在 $6k+1=5p$；因此这里的所有系数均整。

将(8)、(9)代入(7)，再使用剩余域中的 Frobenius，得到完整有限恒等
$$
\boxed{
p\Xi(u)\equiv
-\beta_s b^s Z_{<2p}(u)^p
\pmod{p,\ u^{2q}}.
}
\tag{11}
$$
(11)在 Laurent 截断意义下理解：保所有次数 $<2q$，其中唯一负次数 $u^{-1}$ 的系数已被 $p$ 杀掉。左边的这些系数全整，故约化合法。右边在约化后取 $p$ 次幂，未将一个不整无限 $z(u)$ 直接作模 $p$ 运算。

## 3. 同一严格坐标中的实际相消

整代入 $u(v)=v+O(v^2)$ 保留截断次数及整性。由(2)且 $q>2p$，
$$
Z_{<2p}(u(v))=v+O(v^{2p})
$$
在整级数中成立：高于截断的 $z(u)$ 项不可能改变次数 $<2p$，而原 $z(u(v))$ 在此窗准确等于 $v$。故(11)给
$$
p\Xi(u(v))\equiv-\beta_s b^s v^p
\pmod{p,\ v^{2q}}.
\tag{12}
$$

还须保留原微分因子。记
$$
\ell(v)=\frac{d}{dv}z(u(v)).
$$
因 $u(v)$ 整且 $(1+bu^6)^{-1/2}$ 整，$\ell\in1+v\mathcal O[[v]]$。对原等式
$z(-pv+v^q)=-pz(v)$ 求导并准确约去 $-p$，得到
$$
\ell(v)=\ell(-pv+v^q)(1-pv^{q-1}).
$$
约化后 $\bar\ell(v)=\bar\ell(v^q)$。比较首个可能的正次数便证明
$$
\boxed{\ell(v)\equiv1\pmod p.}
\tag{13}
$$
这一步在全部级数上成立，不依赖给 $H$ 另选整模型。

R663 的准确连接式为
$$
d v^p a(W)
=\Xi(u(v))\,\ell(v)
+\frac{\widetilde T'(v)}{\widetilde T(v)}-\frac1v.
\tag{14}
$$
$\widetilde T'/\widetilde T$ 整；原 $v^{-1}$ 极在(14)中准确相消。将(12)、(13)代入 $p$ 倍的(14)，得
$$
p\,d\,v^p a(W)\equiv-\beta_s b^s v^p
\pmod{p,\ v^{2q}}.
\tag{15}
$$
特别
$$
pdc\equiv-\beta_s b^s\pmod p.
\tag{16}
$$
实际常数仍为(3)的特征零 $c$；后文不以(16)的某个任意 lift 替换它。

$a_j$ 在(15)中的原次数为
$$
p+dj.
$$
其严格小于 $2q$ 恰允许
$$
0\le j\le2p-3:
\qquad p+d(2p-3)=2q-3<2q,
$$
而下一指标的次数已为 $2q+p-2$。对每个 $1\le j\le2p-3$，(15)先支付 $pa_j$ 整，再给其模 $p$ 为零。因为 $d$ 是单位，得到(4)。

这里包括 $j=e-1$ 和 $j\ge e$ 的实际连接系数；这时单独的 $H'/H$ 已可能含分母。证明使用(14)的全部原项，不会把这些分母单项删掉。

## 4. 全阶核：哪些原非交换词能进入第二位

沿用 R710 的准确逆展开
$$
L_m^{-1}=(mc)^{-1}
\sum_{n\ge0}(-\mathcal D_m)^n,\qquad
\mathcal D_m=(mc)^{-1}\partial_W+(a-c)/c.
\tag{17}
$$
一个可能给 $W^i$ 常数项的词，先取 $k_tW^{i+t}$，含正次数乘法指标 $j_1,\ldots,j_s$，其导数数目必为
$$
r=i+t+\sum_\nu j_\nu.
\tag{18}
$$
R710 的整数正规排序证明每个非零词的整数系数都被 $i!$ 整除。将其除以原主项
$(-1)^ii!(mc)^{-i-1}$ 后，额外估值至少为
$$
\Delta=
t+v_p(k_t)+\sum_\nu\left(j_\nu+v_p(a_{j_\nu}/c)\right).
\tag{19}
$$
以下保原各项，不假 $a-c$ 全局整。

首先 $H(W)=\mathcal H_p(W^e)$，所以 $k_t=0$，除非 $e\mid t$。R710 的完整界
$v_p(k_t)\ge-\lfloor t/e\rfloor$ 给所有非恒定 $k$ 项
$$
t+v_p(k_t)\ge e-1=p-2.
\tag{20}
$$

对 $1\le j\le2p-3$，(4)及 $v_p(c)=-1$ 给
$$
j+v_p(a_j/c)\ge j+1.
\tag{21}
$$
对 $j\ge2p-2=2e$，仍使用 R710 已付的真实全尾界，得到
$$
j+v_p(a_j/c)
\ge j+1-\lceil j/e\rceil
\ge2e-1.
\tag{22}
$$
因此每个非主词都至少多两个 $p$。模 $p^3$ 时，唯一可能留下的非主词为：

- $t=0$；
- 恰有一次 $a_1W/c$ 乘法；
- 其余恰为 $i+1$ 次 $(mc)^{-1}\partial_W$。

任意 $j\ge2$ 的项至少多三个 $p$，两次乘法至少多四个 $p$；(20)在原 $p>211$ 门下更高。R710 的原收敛证明仍适用，故可按这些实际估值截断，无遗漏无限高词。

## 5. 一次 $a_1$ 词的准确系数

为核清尺度，令 $r_1$ 为一次 $W$ 乘法右侧的导数数目。必须 $0\le r_1\le i$；左侧导数数目为 $i-r_1+1$。该词作用于 $W^i$ 的整数因子是
$$
\frac{i!}{(i-r_1)!}(i-r_1+1)!
=i!(i-r_1+1).
$$
展开(17)的符号、外部逆和这次原 $ma_1W$ 乘法合计后，全部这类词为
$$
(-1)^i i!\,ma_1(mc)^{-i-3}
\sum_{r_1=0}^{i}(i-r_1+1).
\tag{23}
$$
有限和是 $(i+1)(i+2)/2$。除以主项，(23)恰为
$$
\binom{i+2}{2}\frac{ma_1}{(mc)^2}
=\binom{i+2}{2}\frac{a_1}{mc^2}.
\tag{24}
$$
这证明(6)，包括正号、$m^{-1}$ 和整个二项系数。

还可以直接认出此处的原低连接系数。由
$X=WH^d=W+O(W^{e+1})$ 及
$\sigma\widetilde T/v=E_{\rm c}(X)H(W)$，且 $e>2$，
$$
\boxed{a_1=2[z^{2d}]\log(\sigma/z).}
\tag{25}
$$
所以(24)没有新自由参数，亦不等于给原 $c$ 任选一位 Hasse lift。

## 6. 对四个原中央的实际意义

对原 $\mathcal B_m(W)=\sum b_{m,i}W^i$，R710 的完整公式仍是
$$
j_m=\sum_{i\ge0}(-1)^ii!\frac{p^{i+1}}{\gamma_m^{i+1}}
\,\varepsilon_{m,i}b_{m,i},
\qquad \gamma_m=mpc\in\mathcal O^\times.
\tag{26}
$$
本篇给出了这些同一权重更精确的第二位与第三位；没有改变任一 $b_{m,i}$。对四个实际 $m$，(24)使用共同的原 $a_1,c$，只保显示的 $m^{-1}$ 差异。

R912 所恢复的也是同一个 $u(v),T_{\rm g}$ 与四原 $\mathcal B_m$。因此(4)可用于其完整有限窗口中的连接计算，而不必把 R710 的粗分母界误作实际出现的分母。R912 的所有 $V_c$ 项、两位余数和原首层相位继续保留。

最后，(6)不把 $j_m=0$ 化成 $b_{m,i}=0$。R710 的实际低部分和除商、正则补项和 R708 的长前缀门均仍在。尤其 R708 的 $h$ 阶块读取 $z^{(p+1)h}=w^{sh}$；约 $3p/4$ 个块仍需 $O(p^2)$ 次输入，不能用只保持前五块的 R887 二因子近似替代。

### 依赖

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)，(2)–(4)、(18)–(23)：同一个严格坐标、原 zeta 展开、完整 $a,k$ 与实际常数。
- [R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)，§§2–4：全尾估值、逐词 $i!$ 整除、无限词收敛及准确单位核。
- [R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)，(8)、(18)、(20)：原迹的短模 $p$ 前缀及其真实输入次数；本篇没有重证或加强其非消失结论。
- [R912](R912-original-p-division-and-complete-two-digit-boundary-input.md)：同一个 $[p]$ 除点输入、全部两位行与原四来源规范。

本篇全部为原形式级数和有限系数恒等的手证；没有数学执行、目标素数扫描或新增可重算数据文件。


## 附录 A. 原 \([p]\) 输入给出的有限连接递推

本附录继续使用正文(1)–(3)的同一个原 $a(W)$，以及 R912 的 $\psi_p,\Phi_p,V,V_c,S,S_c$。它没有另选连接的高系数，也没有把 R912 的旧截断自动延长。为读取正文(4)的整个窗口，以下明确改取
$$
L_{\rm conn}=2q-2=d(2e).
\tag{A1}
$$
这里 $L_{\rm conn}$ 是原 $v$ 次数，不是 $W$ 次数。

### A.1 完整原倍点恒等式及其微分

置
$$
X=WH(W)^d,\qquad
\mathscr E(W)=E_c(X)H(W)
=\frac{\sigma(z(u(v)))\widetilde T(v)}v,
$$
$$
F(W)=W(p-W^e)^d=W(W^e-p)^d.
\tag{A2}
$$
最后两个表达式相同，因为 $d=p+1$ 为偶数；它们都是原 $[p]v=pv-v^q$ 在 $W=v^d$ 上的实际作用。仍有
$$
a(W)=(\log\mathscr E(W))'.
$$

R912 的原除点等式是
$$
\vartheta(P(v))=\vartheta(v)^qS(v),\qquad
\vartheta(v)=\frac{\sigma(z(u(v)))}{u(v)},\qquad
P(v)=pv-v^q.
$$
完整 $\mu_d$ 平均与 $P$ 代入交换，且
$$
\mathcal N_d\vartheta=\frac{\mathscr E}{V_c}.
$$
因此准确得到
$$
\boxed{
\mathscr E(F(W))
=\mathscr E(W)^q\,\mathscr C_{\rm div}(W),\qquad
\mathscr C_{\rm div}
=S_c(W)\frac{V_c(F(W))}{V_c(W)^q}.
}
\tag{A3}
$$
所有 $V_c$ 因子均在式中；常数一根及全部除点首项沿用 R912。即使 $\mathscr E$ 本身不整，(A3)仍是原特征零正式恒等式，而 $\mathscr C_{\rm div}$ 是确定的整单位。

记
$$
\kappa_j=[W^j](\log\mathscr C_{\rm div})'.
$$
对(A3)作原 $W$ 微分，得
$$
\boxed{q\,a(W)=F'(W)a(F(W))-(\log\mathscr C_{\rm div}(W))'.}
\tag{A4}
$$
此处没有把导数移入一个模 $p$ 根，也没有以任意 Hasse lift 替换正文的实际 $c=a_0$。

### A.2 严格两窗内的准确三角式

对任意 $r\ge0$，
$$
F'(W)F(W)^r
=\frac1{r+1}\frac d{dW}
\left\{W^{r+1}(p-W^e)^{d(r+1)}\right\}.
\tag{A5}
$$
读取 $W^j$ 时只有 $j=r+ke$ 的项可能出现。在 $0\le j<2e$ 中，$k$ 只能为零或一。$k=0$ 的系数是 $p^{d(j+1)}$；$k=1$ 时 $r=j-e$，系数准确为
$$
-d(j+1)p^{d(j-e+1)-1}.
$$
这也直接由多项式微分证明，不要求 $r+1$ 在 $\mathcal O$ 中可逆。

故整个窗口具有准确的特征零递推
$$
\boxed{
\bigl(q-p^{d(j+1)}\bigr)a_j
=-\kappa_j
-\mathbf1_{j\ge e}\,
d(j+1)p^{d(j-e+1)-1}a_{j-e},
\quad 0\le j<2e.
}
\tag{A6}
$$
当 $j=0$ 时，$a_0=c$ 是原赋值 $-1$ 的系数。每个对角因子都满足
$$
q-p^{d(j+1)}=p^2\left(1-p^{d(j+1)-2}\right)
\in p^2\mathcal O^\times.
\tag{A7}
$$
因此(A6)由同一个原整单位 $\mathscr C_{\rm div}$ 逐项决定全部 $a_j$，包括 $c$。它不是四个来源各自的一组自由高参数。

还可把原中央坐标因子单独保留而不丢弃。令
$$
g=(\log V_c)',\qquad \widetilde a=a-g,\qquad
s_c=(\log S_c)'.
$$
(A4)等价于
$$
q\,\widetilde a=F'\widetilde a(F)-s_c.
\tag{A8}
$$
正文已证 $\widetilde a_0\in p^{-1}\mathcal O^\times$，以及
$\widetilde a_j\in\mathcal O$ 对 $1\le j<2e$ 成立。

对(A8)的复合项除以 $q$ 后逐项估值。$k=0,j=0$ 给至少
$d-3=p-2$；所有 $j\ge1$ 的 $k=0$ 项更高。$k=1$ 中最低者是 $j=e,r=0$，其系数包含
$j+1=e+1=p$，所以估值至少为
$$
1+(d-1)-2-1=d-3=p-2.
$$
$r\ge1$ 时同样更高。由此得到共同的准确有限同余
$$
\boxed{
a(W)\equiv(\log V_c(W))'
-\frac1{p^2}(\log S_c(W))'
\pmod{p^{p-2},\,W^{2e}}.
}
\tag{A9}
$$
(A9)的常数系数在 $p^{-1}\mathcal O$ 中比较，其余系数在 $\mathcal O$ 中比较。作为原整输入的实际推论，
$$
[W^j](\log S_c)'\in p^2\mathcal O
\quad(1\le j<2e),
\qquad
[W^0](\log S_c)'\in p\mathcal O^\times.
\tag{A10}
$$
这些整除是(A8)及原连接整性共同给出的结论；没有预设一个任意整单位都满足它们。

### A.3 新截断下的同原五位输入

要读取(A6)或(A9)到 $j=2e-1=2p-3$，须知道原 $S_c,V_c$ 至 $W^{2e}$，亦即至 $v^{L_{\rm conn}}$。这确实比 R912 使用的
$L=2q-p-9$ 长，故必须重付端点。

R912 的两个精度论证在这个新端点仍成立：

1. 若 $U\in1+v^6\mathcal O[[v^6]]$，则
$$
U(pv-v^q)-1\in p^5
\left(\mathcal O[[v]]/(v^{L_{\rm conn}+1})\right).
\tag{A11}
$$
逐原单项式展开时，取至少两个 $-v^q$ 因子的项次数至少为 $2q+4>L_{\rm conn}$；取零个或一个的系数分别含 $p^6$ 或 $p^5$。因此没有新增低精度项。

2. 为求 $V(v)$ 至 $v^{L_{\rm conn}}$，只需严格坐标及其逆至次数
$L_{\rm conn}+1=2q-1<2q$。原共轭递推每次只除
$p\mathcal O^\times$。若此前系数的不确定项为 $p^4E(u)$，其中 $E$ 无常数、一次项，则
$$
E([-p]u)\equiv E(u^q)\equiv0\pmod{p,u^{2q}}.
$$
另一侧线性项含 $p^5$，$q$ 次幂差含 $p^6$，所以原
$\psi_p,\Phi_p\bmod p^5$ 仍逐阶唯一确定 $V\bmod p^4$ 到这个新端点。

平方根、形式反演、完整 $\mu_d$ 乘法平均及其常数一 $d$ 次根都只除单位。因此同一组原整数倍除点多项式数据给
$$
\psi_p,\Phi_p\bmod p^5
\ \Longrightarrow\
S_c,V_c\bmod(p^4,W^{2e+1}).
$$
对整单位取其对数导数，可用 $U'/U$ 直接计算，无额外分母损失；已知单位至 $W^{2e}$，正好确定其导数至 $W^{2e-1}$。在(A9)中除以 $p^2$ 后，得到
$$
\boxed{
\psi_p,\Phi_p\bmod p^5
\ \Longrightarrow\
a_j\bmod p^2,\quad 0\le j\le2p-3,
\qquad L_{\rm conn}=2q-2.
}
\tag{A12}
$$
也可直接用(A6)归纳：$\kappa_j$ 已知模 $p^4$，每个准确对角因子只损两位，低指标的移位项具有上述更高估值。常数 $c$ 的模 $p^2$ 在其真实 $p^{-1}\mathcal O$ 中理解，不另改 lift。

### A.4 与四个实际中央的接口

(A12)和 R912(22)使用同一个 $V,V_c,S_c$ 及同一个原 sigma 初值。故正文(6)、(26)中所有落在上述窗的连接修正，已经有与原四个 $\mathcal B_m$ 兼容的有限除点输入。没有把 $a$ 的数据独立于四来源另作选择。

本附录没有从(A6)推出四个 $j_m$ 的新零，也没有使 R708 的完整低前缀自动消失。其确切新增范围是：原连接的实际两窗系数由同一个 $[p]$ 数据精确递推，且五位除点输入足够支付它们的第二位。更高中央商、原边界的完整卷积及全部 $V_c$ 项继续保留。
