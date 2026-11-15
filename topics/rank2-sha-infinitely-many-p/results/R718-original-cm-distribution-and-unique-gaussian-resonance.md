# R718 — 原高度二整窗的 CM 分布重建与唯一 Gaussian 共振

日期：2026-11-15。**状态：以下完整原 CM 分布式、整性、唯一共振和有限恢复已证明。**

R717 用两组实际第二位恢复原 sigma 整窗。
本篇将这些数据进一步约束为同一个真实 CM 同源分布式的唯一解。
只用一个明确的、次数随 p 增长的 CM division 多项式的模 p 约化，
加上该同源标号的模 p² 数据，就能恢复原整个整窗。
这些代价仍在；不把原固定来源换成任意形式 forcing。

## 1. 一个存在且大小受控的实际 CM 标号

保持
$$
K=\mathbf Q(\omega),\quad \mathcal O_K=\mathbf Z[\omega],\quad
E:y^2=x^3+17,\quad p=6s-1>101,
$$
$$
q=p^2,\qquad d=p+1,\qquad L=(q-1)/6=s(p-1).
$$
p 在 K 中惰性，故 $\mathcal O_K/p=\mathbf F_{p^2}$。

在有限域中任选一个乘法生成元 g。
中国剩余定理给一个实际 $\alpha\in\mathcal O_K$，满足
$$
\boxed{
\alpha\equiv1\pmod{6\mathcal O_K},\qquad
\bar\alpha_{\!p}=g.
}
\tag{1}
$$
本篇用 $\bar\alpha_{\!p}$ 表示模 p 约化，复共轭仍写 $\overline\alpha$。
这不是关于固定整数原根的猜想：$\alpha$ 允许随 p 选择，
有限域乘法群的循环性已保证 (1)。

写 $\alpha=a+b_0\omega$，可分别在模 $6p$ 的类中取
$|a|,|b_0|\le3p$。于是
$$
\boxed{
N=\alpha\overline\alpha=a^2-ab_0+b_0^2\le27p^2,\quad
p\nmid N,\quad N\equiv1\pmod6.
}
\tag{2}
$$
$[\alpha]$ 是同一原曲线上的 CM 同源，次数 N；
不改变曲线或原算术来源。

置
$$
\tau=g^6,\qquad N_0=N\bmod p=g^{p+1}.
$$
$\tau$ 的准确阶为 L，且
$$
N_0=\tau^s.
\tag{3}
$$
因此在 $1\le n<L$ 内，
$$
\boxed{\tau^n-N_0=0\iff n=s.}
\tag{4}
$$

## 2. 原 sigma 的 CM division 多项式及整性

原 $\sigma$ 使用 $dz=dx/(2y)$，首项 z。
六角格的准周期满足
$$
\eta(\omega\lambda)=\omega^{-1}\eta(\lambda),\qquad
\eta(\alpha\lambda)=\overline\alpha\,\eta(\lambda).
$$
第二式由第一式和 $\mathbf Z$ 线性得到。
由于 $\alpha\equiv1\bmod2$、N 为奇数，
$\sigma(\alpha z)/\sigma(z)^N$ 的两个准周期乘子及半特征符号都相消。
故
$$
\boxed{
\psi_\alpha(z)=\frac{\sigma(\alpha z)}{\sigma(z)^N}
}
\tag{5}
$$
是同一曲线上的椭圆函数。

其非零零点准确为 $\ker[\alpha]\setminus\{O\}$，在 O 极阶为 N−1；
首 Laurent 系数为 $\alpha$。所以有完整有限乘积
$$
\boxed{
\psi_\alpha(P)
=\alpha\prod_{\{T,-T\}\subset\ker[\alpha]\setminus\{O\}}
                  (x(P)-x(T)).
}
\tag{6}
$$
零因子和原首系数同时确定 (5)、(6)，没有漏一个指数或根单位。
核与 $\mu_6$ 作用相容，且 $(N-1)/2$ 被三整除。
因此 (6) 是 $x^3$ 的多项式：
$$
\boxed{
\psi_\alpha=\alpha F_\alpha(x^3),\qquad
F_\alpha(V)\in K[V]\text{ 首一},\qquad
\deg F_\alpha=M=(N-1)/6.
}
\tag{7}
$$
Galois 保持原核及归一化，给系数在 K。

(7) 在 p 处整。
因为 $p\nmid N$ 且 E 在 p 好约化，原非零 N 挠点不能约化到 O；
约化核的素于 p 部分为零。
所以每个 $x(T)$ 在 p 上方的各处均整。
(6) 的系数因而整，而 $\alpha$ 为 p 单位。
这支付整个 $F_\alpha\bmod p$，不是只核最高系数。

(7) 可以由同一个 $[\alpha]=[a]+[b_0]\circ[\omega]$ 的曲线加法式
在有限域中构造。它是次数 $M=O(p^2)$ 的实际输入；
没有要求未知 sigma 第二位作为其定义的一部分。

## 3. 同一个原 Gaussian 下的完整分布式

保持 R614、R717 的
$$
w=z^6,\quad X(w)=z^2x(z),\quad
c=[w^s]\log(\sigma/z),\quad
U(w)=(\sigma/z)e^{-cw^s}.
$$
尤其 $[w^s]\log U=0$ 为原准确规范。
由 (7) 定义整的原有限来源
$$
R_\alpha(w)=w^M F_\alpha\bigl(w^{-1}X(w)^3\bigr).
\tag{8}
$$
它没有负次幂，常数项为一。
计算次数 $<L$ 只用 R614 已付的 $X_n\in\mathcal O$；
其约化还可由 R714 的
$\bar X_n=[Z_1^{6n}](xZ_1^2)$ 直接读取。

从 (5) 不删任何因子，准确得到
$$
\boxed{
U(\alpha^6w)
=U(w)^N R_\alpha(w)
 \exp\{t_\alpha w^s\},\qquad
t_\alpha=c(N-\alpha^{p+1}).
}
\tag{9}
$$
$\alpha^p\equiv\overline\alpha\bmod p$，故
$N-\alpha^{p+1}\in p\mathcal O$。
原 $v_p(c)=-1$ 给 $t_\alpha\in\mathcal O$。

式 (9) 的全部次数 $<L$ 均可约化。
特别指数项最多使用 $j\le p-2$，因为
$js<L=s(p-1)$，所以全部 $j!$ 都是单位。
置
$$
\mathcal E_t(w)=\sum_{j=0}^{p-2}\frac{t^j}{j!}w^{sj}
                   \quad\text{于 }k[w]/(w^L).
$$
于是原 $\bar U$ 满足完整有限式
$$
\boxed{
\bar U(\tau w)=
 \bar U(w)^N\,\bar R_\alpha(w)\,
              \mathcal E_{\bar t_\alpha}(w)
             \pmod{w^L}.
}
\tag{10}
$$

### 3.1 必须保留 N 的第二位

(10) 中是实际整数 N 的幂，不是仅把指数替换成 $N_0$。
若 $N=N_0+pN_1+p^2N_2$，则在这个窗口
$$
\boxed{
\bar U^N=\bar U^{N_0}(\bar U^p)^{N_1}\pmod{w^L}.
}
\tag{11}
$$
$p^2$ 次幂从次数 $p^2>L$ 起，因而只需 $N\bmod p^2$；
但 $pN_1$ 的全部 Frobenius 项不能删除。
下面单个递推的线性系数为 $N_0$，不代表整个右端只用 $N_0$。

## 4. 准确 scalar 是同一个椭圆 Fermat 商

定义与 R705 相同的完整商
$$
q_p(\alpha)=\frac{\alpha^p/\overline\alpha-1}{p}\pmod p.
\tag{12}
$$
保留实际 $\alpha\bmod p^2$ 即可读取它。
从
$$
N-\alpha^{p+1}
=-pN\,\frac{\alpha^p/\overline\alpha-1}{p}
$$
得到
$$
\boxed{
\bar t_\alpha
=-\overline{pc}\,N_0\,q_p(\alpha)
=c_pN_0q_p(\alpha).
}
\tag{13}
$$
后一式用 R636 的 $c_p=-\overline{dpc}$ 及 $d\equiv1\bmod p$。

$c_p=\binom{3s-1}{2s-1}17^s$ 已是显示单位。
所以 (10) 的输入只有：

- 同一实际 CM division 多项式 $F_\alpha\bmod p$；
- 原有理第一位 $X\bmod w^L$；
- 明确标号 $\alpha\bmod p^2$ 给出的 $N\bmod p^2,q_p(\alpha)$；
- 原固定 $c_p$。

本篇不将 (12) 的实部/虚部投影任意删除。
R705 的 wild 角色取它的指定迹配对；
(10) 使用整个 (12)，并同时保 (11)。
共同出现这个商不等于已经证明原中央非零。

## 5. 整个有限来源只有一个 Gaussian 共振

**定理。** 在 $k[w]/(w^L)$ 中，满足
$$
V(0)=1,\quad
V(\tau w)=V(w)^N\bar R_\alpha(w)\mathcal E_{\bar t_\alpha}(w),
\quad
[w^s]\log V=0
\tag{14}
$$
的 V 唯一，且恰为原 $\bar U$。
这里 $[w^s]\log V$ 只用前 s 次通常对数；
$s<p$，这些分母全是单位。

存在性已经由原整窗和 (9)–(10) 给出，未对数据作新的相容性假设。

证唯一性：若 V、V' 都满足，设它们首个差异的次数为 n。
因为两者常数为一，比较 (14) 的次数 n 得
$$
(\tau^n-N_0)([w^n]V-[w^n]V')=0.
$$
由 (4)，只能 n=s。
但该处两个对数系数的差正好等于两个 $w^s$ 系数的差，
因为全部较低系数已经相同；原 gauge 条件又迫这个差为零，矛盾。

这同时给一个完整有限算法。
若已知 $V_{<n}=\sum_{i<n}v_iw^i$，则对 $n\ne s$
$$
\boxed{
v_n=\frac{
[w^n]\{V_{<n}(w)^N\bar R_\alpha(w)\mathcal E_{\bar t_\alpha}(w)\}
}{\tau^n-N_0}.
}
\tag{15}
$$
分母均为实际单位。
在唯一 n=s 处，改用
$$
\boxed{
v_s=-[w^s]\log V_{<s}.
}
\tag{16}
$$
(15) 的右侧包含所有已有 Frobenius 交叉项；
(16) 不通过一次不合法的特征 p 高阶对数除法。

### 5.1 没有偷选更有利的 Gaussian

若不加 (14) 的最后一个条件，所有解恰相差
$$
\mathcal E_a(w)=\exp(a w^s)\pmod{w^L},\qquad a\in k.
\tag{17}
$$
因为 $\tau^s=N_0$，(17) 满足相应齐次式。
给任意两个解，先用唯一 a 消掉它们在次数 s 的差，
再用上述首差论证即可。
原 $[w^s]\log U=0$ 准确选定其中一个，未改原 $c$ 或 $j_m$。

也可选 $\alpha$ 的模 p² lift 满足
$\alpha^p\equiv\overline\alpha\bmod p^2$。
这是有限未分歧环中 Teichmüller lift 的存在性，再用 CRT 保
$\alpha\equiv1\bmod6$；此时 (13) 为零。
但其整数坐标可能升为 $O(p^2)$，N 升为 $O(p^4)$。
它不是 (2) 的同成本替换，本篇主要算法保一般 (13)。

## 6. 对 R717 的实际二位和原首行的返回

先由 (15)–(16) 求唯一 V，再用 R717 的整 Artin–Hasse 逐项因子分解，
即可读取原
$$
\bar a_{pk},\qquad \bar a_{s+pk}\qquad(1\le k\le s-1).
$$
这些正是 R717 的两组真实二位组合。
因此它们受到一个原全局同源分布式的共同约束；
不能在 (16) 的三原来源卷积中各自自由赋值。

所需额外信息现在由 $F_\alpha\bmod p$ 与同一个 $\alpha\bmod p^2$
提供，而非消失不见。
$F_\alpha$ 的次数为 M，零点是整个实际 $\alpha$ 核，
必须保其全局代价。
使用恢复的 V 构造 R717 的
$$
\Sigma_{\rm AH}=Z_1V(Z_1^6)
$$
时，原全部 $h\le p-1$ Cartier 行准确返回
$\bar g_{m,h}$，仍保 R717 的
$m(q-6)(p^3-p^2)\mathcal D_2$ 极帽。
本篇没有将该模型加入旧固定预算格。

(9) 是原来源的乘法分布式。
它不证明 (15) 的任一个真前缀由原 $j_m=0$ 强迫为零，
也不证明原 R710 的中央泛函与这个非线性递推交换。
若要以该式推出原非零，须继续保全部原 $\phi_m$、Gaussian 规范和
真实低位进位；这些正是下一步的指定问题。

本篇无新增数值执行或原根猜想，固定曲线与无穷素数的主目标仍未完成。

依赖：
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R636](R636-original-rational-cartier-return-for-two-critical-rows.md)；
[R705](R705-original-wild-character-and-absolute-weil-projection.md)；
[R714](R714-original-height-two-rational-parameter-and-full-first-cartier-window.md)；
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)。
