# R589 — 原九来源的首 p² 目标、平方零极部与完整多项式 Frobenius 整性

日期：2026-11-14。**状态：已证明。**

本篇保持 R583、R586 的九个实际来源。对同一个首 $p^2$ 有限目标，证明：

- 任意次数的原整系数多项式只需乘一个 $p$ 即整，而非按原函数因子数乘不同的 $p$ 幂；
- 所有原多项式的首分母部分都在一个显示的平方零理想中；
- 每个实际来源多项式的 $p$ 次幂在该目标内整；
- 七条原函数的首分母列准确秩七，并给原一次源格的完整整性原像；
- 同一真正饱和前缀在 $k=(p^2-1)/6$ 有一阶 $p$ 的明确改善。

这些均只在本篇显示的有限目标中使用。
首分母七列不读取最早的两个指定 $c_{4,p},c_{1,p}$；
它们的秩不能代替这两行的非消失。

## 1. 同一原来源与忠实的有限目标

取 $p=6s-1>71$、$b=17$，保持原 $w=z^6$。
用 R583 的固定 Euler 基
$$
W_{4,h}=z^h\int_0^z t^{1-h}f_4(t)\,dt\quad(h=0,1),
$$
$$
W_{1,h}=z^h\int_0^z t^{4-h}f_1(t)\,dt\quad(0\le h\le4),
\qquad f_4=x\sigma^6,\quad f_1=-xy\sigma^6.
$$
与原 $S,T$ 合为九坐标 $\boldsymbol F$。
R583 (22) 的固定 $GL_7(\mathbf Z_p)$ 变换把它们与原七个 $V_{\ell,r}$ 相连，
所以以下结论也属于原九坐标格。

令
$$
\boxed{
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p).
}
\tag{1}
$$
它是自由 $\mathcal O$ 模，基为
$$
w^r\epsilon^Q,\qquad0\le r<s,\quad0\le Q<p.
$$
张量到 $\operatorname{Frac}(\mathcal O)$ 后，$\epsilon=w^s/p$，
准确识别为 $\operatorname{Frac}(\mathcal O)[w]/(w^{ps})$。
因此原形式函数的评价是其真实的 $0\le n<ps$ 前缀：
若 $n=Qs+r$，原 $a_nw^n$ 在这个基中就是
$$
p^Qa_n\,w^r\epsilon^Q.
\tag{2}
$$
这里的行因子 $p^Q$ 不是单位，后面一直显示保留。

令
$$
\mathcal B_p=\mathcal O[
\operatorname{ev}_p(S),\operatorname{ev}_p(T),
\operatorname{ev}_p(W_{4,0}),\ldots,\operatorname{ev}_p(W_{1,4})]
\subset\mathcal A_p[1/p].
\tag{3}
$$
这是真正原多项式来源的评价代数，不是自由加入 $w,\epsilon$ 的新全局来源。

## 2. 每个因子的准确有限窗口成本

R586 已把两个 forcing 写为
$$
z^{R_\ell}f_\ell
=w\exp((a/p)w^s)G_\ell(w),
\quad
a=6p[z^{p+1}]\log(\sigma/z)\in\mathcal O^\times,
$$
$$
G_\ell=\sum_jg_{\ell,j}w^j,\qquad
v_p(g_{\ell,j})\ge-\lfloor3j/p\rfloor.
\tag{4}
$$
若 $0<k<ps$，写
$$
k=Ls+u,\qquad 1\le u\le s,\qquad L=\lfloor(k-1)/s\rfloor<p.
$$
R586 (15) 保完整实际分母，给
$$
v_p([w^k]W_{\ell,h})\ge-L-e_{\ell,h}(k),
\qquad e_{\ell,h}(k)=v_p(6k-h).
\tag{5}
$$
在本窗口，$e_{\ell,h}(k)$ 只能是零或一。
确实，$6k-h<p(p+1)$；若含 $p^2$，只可能等于 $p^2$，
但 $p^2+h\equiv1+h\not\equiv0\bmod6$，因为 $0\le h\le4$。

对原 $S,T$，同样有
$$
\boxed{v_p([w^k]S),\ v_p([w^k]T)\ge-L.}
\tag{6}
$$
为保 (6) 的原来源，使用 R418 的原径向式：
$S$ 与 $T$ 分别除去 $\exp(34cw^{s})$、$\exp(72cw^{s})$，
再除以其真实首因子 $w$，所得函数在 $R_p=p^{-1/(2p)}$ 的 Gauss 范数至多一。
这由原 $\Theta e^{-2cz^{p+1}}$、$z^2x$ 及其逆和固定角多项式直接给出。
于是 R586 (11)–(12) 的同一系数证明适用；
因 $L<p$，$L!$ 是单位，得到 (6)。
没有把 $S,T$ 的整个 theta 乘积换成抽象 forcing。

定义这个单因子的整数权
$$
\omega(k)=L+6u.
$$
其范围为 $6\le\omega(k)\le2p-1$。
若 (5) 中 $e_{\ell,h}(k)=1$，准确有
$$
\boxed{\omega(k)=p+h.}
\tag{7}
$$
因为 $6k=pL+\omega(k)$，
而在上述范围中 $\omega(k)-h$ 唯一可能的正 $p$ 倍数是 $p$。
(7) 是来自原短分母的真实条件。

## 3. 所有次数、所有混合单项式的统一一 p 界

取任意一个非恒定原单项式及其 $w^n$ 系数中的一项，
由正整数 $k_1+\cdots+k_q=n<ps$ 给出。
每个因子写为 $k_i=L_is+u_i$，$1\le u_i\le s$。
设其中实际具有一次 $p$ 分母的 Euler 因子共 $B$ 个。

若
$$
n=Qs+r,\qquad0\le r<s,\qquad
C=\left\lfloor\frac{\sum_i u_i}{s}\right\rfloor,
$$
则
$$
Q=\sum_iL_i+C,\qquad
\nu(n):=Q+6r=\sum_i\omega(k_i)-pC.
\tag{8}
$$
所有因子的系数成本按 (5)–(6) 至多
$$
\sum_iL_i+B=Q+(B-C).
\tag{9}
$$
由 (7)，有分母的每个因子贡献至少 $p$ 的权，其余因子权非负。
所以
$$
\nu(n)\ge p(B-C).
$$
而目标的基权至多
$$
Q+6r\le(p-1)+6(s-1)=2p-6.
$$
因此 $B-C\le1$；若 $\nu(n)<p$，则更有 $B-C\le0$。

这证明如下全部来源定理。

**定理 1。** 对任意次数的整系数原多项式 $P$，以及所有 $0\le n<ps$，
$$
\boxed{
v_p([w^n]P(\boldsymbol F))
\ge -Q-\mathbf1_{\nu(n)\ge p},
\quad n=Qs+r,\quad\nu(n)=Q+6r.
}
\tag{10}
$$
常数列在 $n=0$ 处整；(10) 的非恒定部分已逐项证明。
所有混合乘积、重复因子与整系数和均由同一非阿基米德三角不等式覆盖。

特别，
$$
\boxed{p\,\mathcal B_p\subset\mathcal A_p.}
\tag{11}
$$
这是同一个原代数的任意多项式，不是只对七条线性列的结论。
它也没有按各列的原函数次数分别乘 $p^q$ 后冒认成原格。

## 4. 全来源的共同平方零极部

在
$$
\overline{\mathcal A}_p=k[w,\epsilon]/(w^s,\epsilon^p)
$$
上，给 $w,\epsilon$ 分别赋整数权 $6,1$。
定义实际单项式理想
$$
\boxed{
J_p=\langle w^r\epsilon^Q:Q+6r\ge p\rangle
\subset\overline{\mathcal A}_p.
}
\tag{12}
$$
其维数为
$$
\dim_kJ_p=\sum_{r=1}^{s-1}6r=3s(s-1).
$$
(10) 精确给
$$
\boxed{
\overline{pF}\in J_p\quad\text{对每个 }F\in\mathcal B_p.
}
\tag{13}
$$
目标的最大权是 $2p-6$，因此
$$
\boxed{J_p^2=0.}
\tag{14}
$$
此外，$J_p$ 的每个单项式都含 $\epsilon^5$：
因为 $6r\le p-5$，条件 $Q+6r\ge p$ 迫 $Q\ge5$。

这不仅描述七条线性列；(13) 对整个原多项式代数同时成立。
这里的“平方零”只在本篇准确的有限模 $p$ 目标中成立，
不声称原整函数相乘为零。

### 4.1 完整非线性 Frobenius 整性

取任意 $F\in\mathcal B_p$。
由 (11)、(13)，可写
$$
F=A+R/p,\qquad A\in\mathcal A_p,
$$
其中 $R$ 是 $\overline{pF}$ 按 (1) 的基作的任一标准系数提升，
每个单项式权至少为 $p$。

对所有 $j\ge1$，
$$
\boxed{R^j\in p^{j-1}\mathcal A_p,\qquad R^p=0.}
\tag{15}
$$
第一式的证明保真正乘法进位：
一个乘积单项式初始权至少为 $jp$；
每次把 $w^s$ 换成 $p\epsilon$，恰取出一个 $p$，并使剩余基权减少 $p$。
非零剩余项的权至多 $2p-6$，所以至少要取出 $j-1$ 个 $p$。
第二式来自每个原单项式均含 $\epsilon^5$，故 $p$ 次乘积被 $\epsilon^p$ 杀掉。

现在在特征零的同一目标中展开
$$
F^p=A^p+\sum_{j=1}^{p-1}\binom pj A^{p-j}R^j/p^j+R^p/p^p.
$$
中间二项式系数均含 $p$，配合 (15) 后每项都整，末项为零。
所以得到真实的全非线性结论
$$
\boxed{F^p\in\mathcal A_p\quad(F\in\mathcal B_p).}
\tag{16}
$$
(16) 不是把原普通 core 或某一条中央条件改称 Frobenius 整性。
它仅使用了实际有限目标、完整乘法和所有原来源的 (10)。
也不能从 $F^p$ 在这个有限目标整，推出 $F^p$ 在更大圆盘整或过收敛。

## 5. 七条原函数的全部首极部与准确秩

R586 的全部系数同余在本目标给出显示多项式
$$
\boxed{
\mathcal R_{\ell,h}:=\overline{pW_{\ell,h}}
=
\sum_{r=0}^{s-2}
\frac{\bar a^{\,p+h-6-6r}\,\bar g_{\ell,r}}
{(p+h-5-6r)!}\,
w^{r+1}\epsilon^{\,p+h-6-6r}.
}
\tag{17}
$$
所有显示阶乘严格小于 $p$；各指数非负且在 (1) 的基范围内。
证明是按 R586 的真实条件 $6k-h=mp$ 取出唯一一次分母项，
再准确应用 $w^s=p\epsilon$。
非共振项，以及 $k$ 为 $s$ 的整倍数的项，在 $\overline{pW}$ 中均为零。

每个 (17) 的单项式恰有权 $p+h$。
不同 $h$ 的块因而分离。
在 $h=0,1$ 两个双来源块，选择 $r=0,1$ 两条真实坐标，
去掉显示的单位幂和单位阶乘后，矩阵恰为
$$
\begin{pmatrix}
1&1\\
-4b/35&6b/35
\end{pmatrix},
\qquad\det=2b/7\in k^\times.
$$
另外 $h=2,3,4$ 的单来源块，各由 $g_{1,0}=1$ 给非零列。
故
$$
\boxed{
\dim_k\langle\mathcal R_{4,0},\mathcal R_{4,1},
\mathcal R_{1,0},\ldots,\mathcal R_{1,4}\rangle=7.
}
\tag{18}
$$
这是完整有限目标中的秩，不是只检查七个数值样本。

例如七个单位主元可取：
对 $h=0,1$ 取 $r=0,1$，对 $h=2,3,4$ 取 $r=0$；
每一主元的原 $w$ 指标准确为
$$
n=(p+h-6-6r)s+r+1.
\tag{19}
$$

因此在原一次源格
$$
\mathcal O\langle1,S,T,W_{4,0},W_{4,1},W_{1,0},\ldots,W_{1,4}\rangle
$$
中，评价落入 $\mathcal A_p$ 的完整原像是
$$
\boxed{
\mathcal O\langle1,S,T\rangle
\ \oplus\
p\mathcal O\langle W_{4,0},W_{4,1},W_{1,0},\ldots,W_{1,4}\rangle .
}
\tag{20}
$$
证明：乘 $p$ 后模 $p$ 的原 $1,S,T$ 列均为零，
而七列由 (18) 线性独立。故七个系数必须且只需同时含 $p$。
经 R583 的固定整基变换，原七 $V$ 坐标也具有同一 (20)。

### 5.1 两个最早指定系数在此首极部中不可见

准确保留 R586 的
$$
c_{4,p}=g_{4,s-1}=[z^{p-1}]f_4,\qquad
c_{1,p}=g_{1,s-1}=[z^{p-4}]f_1.
$$
它们没有出现在 (17) 中；上限是 $s-2$。

这不是删去一个高阶误差。
对 $h=1$ 的最早共振 $k=s$，
$$
p[w^s]W_{\ell,1}\equiv c_{\ell,p}\pmod p,
$$
但在原目标中 $w^s=p\epsilon$，
所以它贡献的是整项 $c_{\ell,p}\epsilon$。
再乘外面的 $p$ 后，其首极部为零。
同理，R586 中 $h=2,3,4$ 的 $k=hs$ 三行，
各被 $w^{hs}=p^h\epsilon^h$ 准确吸收为整项。

相反，$h=0$ 的最早分母在 $k=p=6s-1$，确实留下
$$
\frac{\bar a^5}{720}\,\bar g_{\ell,s-2}\,
w^{s-1}\epsilon^5
$$
这个可见首极部。
它读取的是相邻的 $g_{\ell,s-2}$，不能改标为 $c_{\ell,p}$。
所以 (18)、(20) 都没有排除两个指定 $c_{\ell,p}$ 同时为零。

## 6. 原多项式前缀与显示的行成本

对任意 $D$，仍使用原
$$
E_{D,9}=\bigoplus_{|\alpha|\le D}\mathbf Z\,\boldsymbol X^\alpha,
\qquad r_n(P)=[w^n]P(\boldsymbol F).
$$
(11) 给同一个整评价矩阵
$$
\boxed{
M_{p,D}(n,\alpha)
=p^{1+\lfloor n/s\rfloor}\,r_n(\boldsymbol X^\alpha),
\qquad0\le n<ps.
}
\tag{21}
$$
这是统一的行缩放，没有对不同单项式按其原函数次数改用不同列格。

全部原前缀的精确零关系因此保持：
在分式域上以及与原整源格相交后，
$$
\ker(r_0,\ldots,r_{k-1})
=\ker(M_{p,D}(0,-),\ldots,M_{p,D}(k-1,-)).
\tag{22}
$$
但 $\bar M$ 的模 $p$ 核不自动等于真正核的约化；
后续若需要提升，仍须在 (21) 中付真实 Bockstein 与原前行。

在真正的 $K_{D,k}$ 上，最后一行准确还原为
$$
\varphi_{D,9}^k
=p^{-1-\lfloor k/s\rfloor}M_{p,D}(k,-)|_{K_{D,k}}.
$$
因此 (10) 直接给全部 $D$ 的实际饱和界
$$
\boxed{
\log\|\varphi_{D,9}^k\|_p
\le\left(Q+\mathbf1_{Q+6r\ge p}\right)\log p,
\quad k=Qs+r<ps.
}
\tag{23}
$$

特别取
$$
k_*=(p^2-1)/6=(p-1)s.
$$
此时 $Q=p-1,r=0$，所以
$$
\boxed{\log\|\varphi_{D,9}^{k_*}\|_p\le(p-1)\log p
\quad\text{对全部 }D.}
\tag{24}
$$
R583 的粗 Gaussian 项在这一行是 $p\log p$，且其高次误差为零；
所以 (24) 是同一真实源格的一阶 $p$ 改善。
它只是一条明确高度二行，不是所有 $k$ 的 cutoff，也没有改变现有全球主系数。

(18) 中的高阶主元仍不能自行给某个真饱和行非零。
例如固定 $D=1$ 时，原十列的完整前缀在固定有限阶已满秩，
其后真正的 $K_{1,k}$ 为零。
本篇保留 (21)–(23)，不把首极部秩七当作原主目标所需的非零中央。

## 7. 复核与后续实际接口

[check-r589-finite-euler-pole-algebra.mjs](../scripts/check-r589-finite-euler-pole-algebra.mjs)
在已经使用的共同 $b=1$ 惰性纤维 $p=17$ 上，
直接由原有理级数重建 $S,T$ 和全部七 $W$ 的完整 $ps=51$ 维目标，
核对 (17) 的全部列、准确秩七、全部次数至三的 219 个混合单项式、
以及七条线性来源和一条非线性来源的完整 $p$ 次幂整性。
还检验一个单位尺度 $b=2$。
这不是在坏位 $p=17$ 上约化原 $b=17$ 曲线；
原 $b=17$ 的全参数运输由 R586 (22) 和本篇证明保留。

证书共完成 219,394 项精确检查；参数部分另核真实权、乘法进位和全次数的组合上界。
所有计算只核对上述全参数证明，不扩大椭圆曲线非消失扫描。

(17)、(21) 给了可以继续计算的实际首极部和前缀矩阵。
下一步若比较指定 $c_{4,p},c_{1,p}$，必须从第 5.1 节保留的整项
或它们的下一层提升读取；不能从当前不可见的七列秩作结论。
普通负矩 $I_4,I_1$、原 $S/T$ 全中央及 mixed 补域也没有在这里换成新的零条件。
