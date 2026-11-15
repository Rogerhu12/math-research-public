# R631 — 原完整目标首 Bockstein 的准确十三阶边界核

日期：2026-11-15。**状态：已证明。**

本篇将 R618 的第二 Gaussian 系数界用于 R620 的同一个全来源矩阵。
对全 $D$ 的原首 Bockstein，低十三个普通阶不只给一个秩下界：
它的核准确是原来源中权阈值由 $p-78$ 提高到 $p$ 的子格。

全部更高 regular 尾在原整目标中至少被 $p^2$ 整除；
这个估计保留所有 $\Upsilon$ 基和全部 Gaussian 次数。
因此本篇得到真实余核中的边界映射，而非只在环境向量中看到一个单位。
一般情况下仍未计算边界核以内的 Bockstein，也不宣称整个 Smith 形式已知。
旧三块的同一个 $R$、原 $d_2$ 和完整中央条件保持不变。

## 1. 同一矩阵、来源核和原标准基

保持 R620 的
$$
p=6s-1>101,\qquad 0\le D<p,\qquad n_0=s-13,\qquad m=p-78,
$$
以及整个原
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}}.
$$
所有 $q_n$、十九角和次数帽沿 R620，不扩大来源。

完整物理矩阵仍为
$$
\boxed{
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon})\in\mathcal C_p,}
\tag{1}
$$
$a,c_*,U_0(0)$ 都是原单位；$\epsilon=w^s/p$。
目标采用 R607 的全部整关系
$$
\mathcal C_p=
\mathcal O[w,\epsilon,\Upsilon]/
(w^s-p\epsilon,\epsilon^6-w\Upsilon,
w^{s-1}\epsilon^5-p\Upsilon,\Upsilon^s).
\tag{2}
$$
它的原标准基是
$$
\Upsilon^j w^r\epsilon^t,\qquad
0\le j<s,\quad0\le t\le5,\quad0\le r<s,
$$
排除 $t=5,r=s-1$。其秩为 $ps$。
同一基也等于按 raw 次数排列的
$$
e_N=p^{-\lfloor6N/p\rfloor}w^N,\qquad0\le N<ps .
\tag{3}
$$

对任意正整数 $\lambda$，记原实际子空间
$$
\mathscr K_\lambda=
\{\bar P\in\overline{\mathcal W}_D:
\bar P(t,1+v)\in I_\lambda(t,v)\},\qquad
I_\lambda=\langle t^r v^h:6r+h\ge\lambda\rangle .
\tag{4}
$$
由 R612/R620，
$$
\ker\bar\Phi=\mathscr K_m.
\tag{5}
$$
对所用的 $\lambda=m,p$，R620 的同一个整消元也给
$$
\boxed{
k_D(\lambda):=\dim\mathscr K_\lambda
=\sum_{r=0}^{b_D}\bigl(m_r-(\lambda-6r)_+\bigr)_+,}
\tag{6}
$$
其中 $m_r=|\{n:A_n\le r\le b_n\}|$，全部是原列数。
替换阈值不改变唯一转换点和高尾整解的证明。

特别，每个 $\bar P\in\mathscr K_m$ 可在同一原来源中整选
$$
\boxed{P(t,1+v)\in I_m(t,v)\quad\text{准确成立，}}
\tag{7}
$$
而非只模 $p$ 成立。这使用 R620 的实际整核基。

定义原首 Bockstein
$$
\beta_{\mathcal C}:\mathscr K_m\longrightarrow
\operatorname{coker}\bar\Phi,\qquad
\bar P\longmapsto[\overline{\Phi(P)/p}].
\tag{8}
$$
改变 (7) 的提升只加原像，故 (8) 良定义。

## 2. 低十三阶投影确实杀掉整个原像

令 $\Pi_{13}$ 为 (2) 标准基上的投影，保留
$$
\boxed{
\Upsilon^j w^r\epsilon^t,\quad
0\le j<s,\quad0\le t\le5,\quad0\le r<13.}
\tag{9}
$$
这里包括全部允许的 $\Upsilon$，不令其为零。

模 $p$ 后，乘 $w^{13}$ 要么仍有普通 $w$ 阶至少十三，
要么越过原关系而变成零：
越过 $w^s$ 或 $w^{s-1}\epsilon^5$ 时都带外部 $p$。
因此
$$
\boxed{\Pi_{13}(w^{13}\overline{\mathcal C}_p)=0.}
\tag{10}
$$
由 (1)，$\Pi_{13}$ 杀掉整个 $\operatorname{im}\bar\Phi$，
所以 (8) 有真正余核上的投影
$$
\Pi_{13}\beta_{\mathcal C}:
\mathscr K_m\longrightarrow\operatorname{im}\Pi_{13}.
\tag{11}
$$
本篇不会把一个未杀原像的环境行称作 Bockstein 左证书。

## 3. 全部 regular 尾在第二权带以后至少有两次 p

取同一个 (7) 的实际整提升。
因为 $\epsilon^p=0$ 在 (2) 中准确成立，
将 (1) 写成
$$
\Phi(P)=\sum_{i=0}^{p-1}H_i(w)\epsilon^i,\qquad
H_i(w)=\sum_{r\ge0}c_{r,i}w^r,
\tag{12}
$$
并按 $r+si<ps$ 截取原 raw 目标。
$i!$ 在这一整段中都是单位。
所有 $H_i$ 都使用原 regularized 部分，保 $U_0$、$g$、$t$、
$q_n$、来源系数以及总 charge $n+40$。

设
$$
\tau_2=\frac{2p-1}{p(p^2-1)},\qquad R_2=p^{-\tau_2}.
$$
R618 的同一盘界给
$$
\boxed{v_p(c_{r,i})\ge-\lfloor6r\tau_2\rfloor.}
\tag{13}
$$
为明确全来源适用性，作如下核定。
在任意闭 $R<R_2$ 上，原 $W=z^2x$、$t/w$ 及其逆为范数一的单位；
原 sigma 去掉与 $\kappa$ 匹配的第一 Gaussian 后也为范数一的单位。
R618 允许该 Gaussian 常数与原 $c$ 相差整量。
故原 $g$ 是 $(1+8t)W^{17}$ 乘同一 regularized sigma 的三十四次幂，
范数不超过一。
原固定 $U_0$ 是相应 $g^{40}$、$t/w$ 与固定角有理单位的乘积，
仍有同一界。
每个 $q_n/t^{A_n}$ 由 $h_7,t-1,d^{-1}$ 的整数幂组成，
在 $|t|<1$ 上也有范数一；剩余 $t$ 幂非负。
来源系数在 $\mathcal O$，所以有限和不扩大范数。
最后 $a^i(n+40)^i/i!$ 仍整。
对每个严格内盘取 Cauchy 界，再令 $R\uparrow R_2$，即得 (13)。
此处的原矩阵 $U_0$ 不与 R618 中暂记的 Taylor 截断多项式混同。

给单项式 $w^r\epsilon^i$ 赋原权
$$
W=6r+i,\qquad q=\lfloor W/p\rfloor.
$$
它在 (3) 中准确满足
$$
w^r\epsilon^i
=p^q e_{r+si},
\tag{14}
$$
因为 $6s=p+1$。
所以其实际整目标系数赋值至少
$$
q-\lfloor6r\tau_2\rfloor.
$$

**引理 1（完整高尾）。** 若 $q\ge2$，则
$$
\boxed{q-\lfloor6r\tau_2\rfloor\ge2.}
\tag{15}
$$

**证明。** 由 $6r<(q+1)p$，
$$
6r\tau_2<(q+1)\frac{2p-1}{p^2-1}.
$$
$p>101$ 给 $(2p-1)/(p^2-1)<1/3$，
而对所有 $q\ge2$，$(q+1)/3\le q-1$。
故 $6r\tau_2<q-1$，取 floor 得 (15)。证毕。

这控制 (12) 的**全部**所读高尾，包括可能含普通分母的项，
不是只对有限低系数作模 $p$ 形式运算。
不同项落到同一个 raw 行时相加仍至少在 $p^2$ 中，故没有遗漏抵消问题。

由 (7)，带权代入
$$
t=\tau_0w+\cdots,\qquad
v=g(w)e^{a\epsilon}-1=a\epsilon+
\text{更高权项}
$$
及原 $w^{13}$ 前缀使 (12) 中所有 $W<p$ 的系数准确为零。
对 $p\le W<2p$，(13) 还给这些系数整：
此时 $6r<2p$，所以 $6r\tau_2<2(2p-1)/(p^2-1)<1$。
于是 (15) 证明
$$
\boxed{
\overline{\Phi(P)/p}
\text{ 只由准确第一权带 }p\le6r+i<2p\text{ 给出。}}
\tag{16}
$$

## 4. 第一权带的 carry 是真正标准基上的单射

在 $0\le i<p$、$p\le W=6r+i<2p$ 中，
由 (14) 有
$$
\frac{w^r\epsilon^i}{p}=e_{r+si}.
\tag{17}
$$
这些 raw 行全部在目标内，因为
$$
6(r+si)=W+pi<p(p+1)=6ps.
$$

两个不同单项式不可能在这条权带中落到同一行。
若 $r+si=r'+si'$，则
$$
(6r+i)-(6r'+i')=p(i'-i).
$$
两边权差的绝对值小于 $p$，故 $i=i'$、$r=r'$。
因此 (17) 是单项式基之间的准确单射。

更明确地写
$$
i+1=6j+t,\quad0\le t\le5,\qquad
b=r+j-s .
$$
由 $p\le W<2p$ 得
$$
0\le b<s,\qquad (b,t)\ne(s-1,5),
$$
且 (17) 的原标准基表示为
$$
\boxed{
\frac{w^r\epsilon^i}{p}
=\Upsilon^j w^b\epsilon^t,\qquad
W-p=6b+t.}
\tag{18}
$$
这里 $0\le j<s$。
因此 (9) 准确保留第一权带中的
$$
\boxed{p\le W<p+78,}
\tag{19}
$$
其余第一权带项均被丢掉。
这使用全部 $\epsilon^6=w\Upsilon$ 和边界关系；
没有把标准基换成不合法的自由 $w,\epsilon$ 单项式。

## 5. 准确边界核

在 $k[w,\epsilon]/I_p(w,\epsilon)$ 上，
R612 的原带权坐标代入
$$
t\mapsto\bar t(w),\qquad
v\mapsto\bar g(w)e^{\bar a\epsilon}-1
$$
是过滤自同构：
首项分别为 $\bar\tau_0w$ 和 $\bar a\epsilon$，
其他项严格增加权。
乘回 $\bar c_*\bar U_0e^{40\bar a\epsilon}$ 是过滤线性单位。
这两者都保持每个 $I_\lambda$，尤其保持 $I_m$ 和 $I_p$。

将 (19) 的整个权带除去原 $w^{13}$，准确对应
$$
m\le6r+i<p.
$$
所以 (16)–(19) 表明：
$\Pi_{13}\beta_{\mathcal C}(\bar P)$ 是
$\bar P$ 在 $I_m/I_p$ 中的类，经同一个过滤单位及单射 (17) 的像。
因此得到本篇的完整结论。

**定理 1。**
$$
\boxed{
\ker(\Pi_{13}\beta_{\mathcal C})=\mathscr K_p
\subset\mathscr K_{p-78}.}
\tag{20}
$$
特别
$$
\boxed{
\operatorname{rank}(\Pi_{13}\beta_{\mathcal C})
=k_D(p-78)-k_D(p),}
\tag{21}
$$
两项都由同一原来源的准确求和 (6) 给出。

(20) 与所取 (7) 的提升无关：
若改为 $P+pR$，(8) 增加 $\bar\Phi(R)$，
恰被 (10) 杀掉。
所以这不是挑选有利提升后的环境像计算。

(20) 也给真正原左证书：
取 (9) 中任意坐标行或其线性组合，
它们均杀整个原首像；
在 $\mathscr K_{p-78}/\mathscr K_p$ 上，
经 (18) 的独立基可选出恰有 (21) 条独立配对。
没有新增来源，也没有把 $\mathscr K_p$ 说成可自由补的 normal 数据。

## 6. 真实 Smith 结论及不能越过的边界

设 $N_D=\operatorname{rank}\mathcal W_D$。
R620 已给恰有 $N_D-k_D(p-78)$ 个单位 Smith 因子。
原首 Bockstein 的秩等于剩余 Smith 因子中赋值恰为一的数目。
于是 (21) 严格推出
$$
\boxed{
\#\{\text{恰为 }p\text{ 的 Smith 因子}\}
\ge k_D(p-78)-k_D(p),}
\tag{22}
$$
$$
\boxed{
\#\{\text{赋值至少二的因子或特征零核方向}\}
\le k_D(p).}
\tag{23}
$$
这是实际物理矩阵的结论；
其依据是已杀整个原像的 (11)，而非来源饱和。

一般只知
$$
\ker\beta_{\mathcal C}\subset\mathscr K_p.
$$
$\mathscr K_p$ 内的某些向量仍可能由 (9) 之外的行检测到；
也可能在更高精度才产生障碍。
故不能把 (22) 改成等号，不能由 (23) 写出全部高 Smith 指数。

唯一立即完整的情形是 $k_D(p)=0$。
由 R620 同一个准确单射判据，
$$
k_D(p)=0\quad\Longleftrightarrow\quad p>6b_D.
$$
此时全部非单位因子恰为 $p$，没有特征零核。
当 $k_D(p-78)>0$ 时，
这个范围等价于 R620 的
$0\le b_D-(s-13)\le12$；
因此定理1统一恢复其十三阶边界窗，
并给窗内、窗外同一实际首 Bockstein 的准确边界秩。

## 7. 原旧目标与全局量词仍保留

本篇的 $\Pi_{13}$ 在 (9) 中读取所有 $\Upsilon$ 层；
其中大量行不在旧三块目标内。
所以 (20) 不自动限制 R597 的旧第二类，
不能把 $\mathcal C_p$ 的边界核当成旧 $M$ 的 $K_2$。

原同一个 $R$ 的两条十三行、$\mathcal D_\psi^+$、
完整第二 forcing 和实际剩余像仍按原定义读取。
R629 已支付的是旧 $b_D\ge s-13$ 短目标；
较小预算中的真实余类没有由本篇被判定。

同样，(6)、(21) 属于指定有限大目标的实际全部列。
本篇没有将这些不连续行换成任意连续真前缀，
没有给核基或其乘积赋中央零，
也没有从 (13) 自动推出全 $D/k$ 的全局严格成本门。

## 依赖

- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  同一原 regularized 来源的第二盘和全部系数界；
  本篇 (15) 使用它支付完整高尾，不能只用旧低精度约化代替。
- [R620](R620-full-original-weighted-hilbert-function-and-thirteen-row-smith-window.md)：
  全来源准确 Hilbert 函数、同帽角核整提升、十三阶 Smith 特例。
- [R612](R612-original-full-source-weighted-kernel-and-fixed-nodal-exit.md)：
  原完整带权坐标和 $w^{13}/U_0$ 的真实运输。
- [R607](R607-original-integral-target-and-mixed-schur-decomposition.md)：
  全 $\mathcal C_p$ 标准基及所有混合 carry。

本篇为全参数证明，不增加素数扫描或未执行证书。
