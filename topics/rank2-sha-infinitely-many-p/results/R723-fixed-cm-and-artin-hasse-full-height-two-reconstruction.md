# R723 — 两固定 CM 来源恢复原整个高度二整窗

日期：2026-11-15。**状态：以下完整恢复定理及密度一范围已证明。**
本篇把 R720 的固定低度来源与 R717 的实际 Artin–Hasse 支持联立。
R720 单独使用 CM 递推的短窗限制仍正确；
加入原已付的其它 Artin–Hasse 行后，全部高度二整窗都可恢复。

保持原 $E:y^2=x^3+17$、
$$
p=6s-1>101,\quad q=p^2,\quad L=(q-1)/6=s(p-1),\quad
w=z^6,\quad U=(\sigma/z)e^{-cw^s},
$$
其中 $c=[w^s]\log(\sigma/z)$，原 $[w^s]\log U=0$ 不变。
所有有限约化均在 $k=\mathbf F_{p^2}$。

## 1. 原 Artin–Hasse 坐标的全部确定行和两个例外族

令
$$
\mathscr E_p(T)=\exp\left(\sum_{j\ge0}\frac{T^{p^j}}{p^j}\right)
 \in\mathbf Z_p[[T]]
$$
为标准整 Artin–Hasse 级数，$\overline{\mathscr E}_p$ 为其准确约化。
沿用 R717 的原唯一整分解
$$
\boxed{\quad
U(w)=\prod_{1\le n<L}\mathscr E_p(a_nw^n)\pmod{w^L}.
\quad}
\tag{1}
$$
因 $L<p^2$，若 $f=\log U$，则全部原坐标为
$$
a_n=f_n\ (p\nmid n),\qquad
a_{pk}=f_{pk}-f_k^p/p\ (1\le k<s).
\tag{2}
$$
每个 $a_n$ 整，是原完整 U 的实际坐标，不是独立可选参数。

写 $X=z^2x(z)=\sum X_nw^n$。
除 n=s 外，
$$
f_n=-\frac{X_n}{6n(6n-1)},\qquad f_s=0.
$$
因此单凭原第一位 $\bar X_n$，就已经确定
$$
\boxed{\quad
\bar a_s=0,\qquad
\bar a_n=-\frac{\bar X_n}{6n(6n-1)}
\quad\left(
n\notin\{s\}\cup\mathcal A_p\cup\mathcal B_p
\right),
\quad}
\tag{3}
$$
其中
$$
\mathcal A_p=\{pk:1\le k<s\},\qquad
\mathcal B_p=\{s+pk:1\le k<s\}.
\tag{4}
$$
(3) 的分母都是单位。
这是完整的例外分类：$n<L<p^2$ 中 p 除 n，
恰为 $\mathcal A_p$；p 除 $6n-1$，
恰为 $\{s\}\cup\mathcal B_p$。
R717 已付的原第二位除商只留在 (4) 两族中。

标准 $\overline{\mathscr E}_p$ 本身必须完整保留。
本篇不把它替换成普通有限指数，也不删它在次数 p 及以后的通用系数。
它是由明确整数 p 定义的通用整级数；
所删除的是独立的原 sigma 第二位输入，而非所有整数高精度运算。

还有一个简单而重要的三角事实：
若两个分解的首个不同坐标为 n，
它们所得 U 的首个不同系数也为 n，且该差正是两 $\bar a_n$ 的差。
因为第 n 因子从 $1+\bar a_nw^n$ 起，而更高因子尚无贡献。

## 2. 两个固定 CM 分布式

仍取
$$
\alpha_\pm=1\pm6\omega,\qquad N_+=31,\quad N_-=43,
\qquad \tau_\pm=\bar\alpha_\pm^6.
$$
原真实 division 来源为
$$
\psi_\pm=\alpha_\pm F_\pm(x^3),\quad
\deg F_+=5,\quad\deg F_-=7,
$$
并由 R720 的实际核及六倍恒等式固定。
令
$$
R_\pm(w)=w^{(N_\pm-1)/6}
        F_\pm(w^{-1}X(w)^3),\qquad
t_\pm=-[w^s]\log R_\pm.
\tag{5}
$$
这里 s<p，所以最后一式只用原低行和单位对数分母。

R718/R720 的原分布式在完整窗口中为
$$
\boxed{\quad
\bar U(\tau_\pm w)
=\bar U(w)^{N_\pm}\bar R_\pm(w)\,
\mathcal E_{\bar t_\pm}(w)\pmod{w^L},
\quad}
\tag{6}
$$
$$
\mathcal E_t(w)=\sum_{j=0}^{p-2}\frac{t^jw^{sj}}{j!}.
$$
这里 $js<L$ 恰好只用 $j\le p-2$，没有非单位阶乘。
$N_\pm<p$，但实际整数幂 31、43 的全部交叉项仍在。
完整原 Fermat 商仍由
$\bar t_\pm=c_pN_\pm q_p(\alpha_\pm)$ 给定，未投影或设零。

定义共同六次像的准确阶
$$
e_{\rm CM}(p)=|\langle\tau_+,\tau_-\rangle|.
$$
它整除 $L$。由于 $6s=p+1$，
$$
\tau_\pm^s=N_\pm\in\mathbf F_p^\times.
\tag{7}
$$

## 3. 两组真正未知行没有共同共振

**引理。** 在 (4) 的两族上，两个 CM 行的共同共振分别为
$$
\boxed{
\begin{aligned}
\tau_+^{pk}=N_+,\ \tau_-^{pk}=N_-
&\iff e_{\rm CM}(p)\mid k-s,\\
\tau_+^{s+pk}=N_+,\ \tau_-^{s+pk}=N_-
&\iff e_{\rm CM}(p)\mid k.
\end{aligned}}
\tag{8}
$$

第一式只需对原两等式作 p 次 Frobenius：
$\tau_i^{p^2k}=\tau_i^k$，而 $N_i^p=N_i=\tau_i^s$。
所以等价于两 $\tau_i^{k-s}=1$。
第二式先按 (7) 消去 $\tau_i^s=N_i$，
得到 $\tau_i^{pk}=1$；Frobenius 再给 $\tau_i^k=1$。
两个循环子群的共同阶正是 $e_{\rm CM}(p)$，故 (8) 成立。

由于 $1\le k<s$，得到
$$
\boxed{\quad
e_{\rm CM}(p)\ge s
\quad\Longrightarrow\quad
\text{(4) 中每一个真实未知行，至少一个 CM 分母是单位。}
\quad}
\tag{9}
$$
共同共振可以出现在其它更高指标；
那些指标的原 Artin–Hasse 坐标已由 (3) 确定，
因此不是未支付的自由度。

这正是只考察 CM 群阶是否超过整个二次窗口会遗漏的原来源信息。

## 4. 完整原整窗的唯一恢复

**定理。** 假设 $e_{\rm CM}(p)\ge s$。
同一原 $\bar X\bmod w^L$、固定 $F_\pm\bmod p$、
(3) 的确定坐标及两个 (6)，唯一决定
$$
\boxed{\quad \bar U\bmod w^L.\quad}
\tag{10}
$$
不需要独立输入原 $\mathcal A_p,\mathcal B_p$ 两族的第二位。

存在性来自原 U、R717 的整分解和真实 CM 分布，
没有对任意数据预设一种额外相容性。

若 V、V' 都满足全部条件，取首个不同的 Artin–Hasse 坐标 n。
由 (3)，n 必在 (4) 内。
由第1节的三角事实，它们的首个不同普通系数也在 n。
在该处比较 (6)，对每个 i 都有
$$
(\tau_i^n-N_i)([w^n]V-[w^n]V')=0.
$$
(9) 给至少一个非零分母，矛盾。
故 (10) 唯一。

这个证明没有取特征 p 的高阶普通对数。
原 gauge 已作为确定坐标 $\bar a_s=0$ 保留。

### 4.1 全部步骤均有明确有限递推

按 n=1,\ldots,L-1 依次求值，维护已知普通系数及实际 AH 因子。
记
$$
P_{<n}(w)=\prod_{j<n}\overline{\mathscr E}_p(\bar a_jw^j)
                   \pmod{w^{n+1}},\qquad
V_{<n}(w)=\sum_{j<n}v_jw^j.
$$

若 n 不在 (4)，直接用 (3) 的实际 $\bar a_n$，置
$$
v_n=[w^n]P_{<n}+\bar a_n .
\tag{11}
$$
其中 n=s 使用 $\bar a_s=0$。

若 n 在 (4)，选一个 $\tau_i^n-N_i\ne0$ 的实际符号，
先按完整分布求
$$
v_n=
\frac{[w^n]\{V_{<n}^{N_i}\bar R_i\mathcal E_{\bar t_i}\}}
     {\tau_i^n-N_i},
\qquad
\bar a_n=v_n-[w^n]P_{<n}.
\tag{12}
$$
(12) 中已有 AH 因子的所有 Frobenius 项仍在。
选择哪个单位行不影响答案，因为每一步都与实际存在的原解相同。
因此所得解还满足未用于该步的另一条完整 CM 式，
而不是把剩余方程删掉。

## 5. 固定低度恢复适用于密度一的惯性素数

R720 已完整证明：在 $p\in[X_0,2X_0]$ 中，
除去至多 $O(X_0^{9/10}/\log X_0)$ 个素数，
固定范数群 $\langle31,43\rangle$ 和两个反共轭比值群的阶
都超过 $X_0^{3/5}$，从而
$$
e_{\rm CM}(p)>X_0^{6/5}/12.
$$
对充分大 X_0，这个下界超过 $s=(p+1)/6$。
所以 (10) 对惯性素数的相对密度一子族成立；
和原既定正密度惯性条件相交，仍保其密度。

这里没有固定原根猜想，没有随 p 增大的 CM division 次数，
也没有把实际 Fermat 商换成一个可自由取值的参数。

第一位输入本身也已由原有理函数提供。
R721 的低极帽参数满足
$$
D\widehat Z=1,\qquad \widehat Z=z+O(z^{p^2}),\qquad
(\widehat Z)_\infty=p(2s-1)\mathcal D_2 .
$$
因此对全部 $n<L$，
$$
\bar X_n=[\widehat Z^{\,6n}](x\widehat Z^2).
\tag{13}
$$
最后读取的次数至多 $p^2-7$，低于坐标误差首次可能进入的 $p^2-1$。
所有读入量都来自这个原曲线的有理函数及两个固定核。

## 6. 全部原首 Cartier 行与剩余主门

由 (10) 取得完整 U 后，R721 的
$$
\widehat\Sigma=\widehat Z\,\bar U(\widehat Z^6),\qquad
\widehat A_m=\widehat\Sigma^m\phi_m
$$
恢复 $m=34,72,136$ 的全部原首行 $1\le h\le p-1$。
真实总极帽仍为
$$
m(p^2-6)p(2s-1)\mathcal D_2,
$$
而负幂观察还须按 R721 保其它全部零点及实际 Cartier 留数。
第三 m 继续需要它独立的原中央条件。

本篇完成的是：原整个高度二系数窗及其两族二位组合，
在密度一惯性素数上受到两个固定五次、七次来源的唯一约束。
它不把这种唯一性认成指定非零。

要由此完成主目标，仍须把这个**同一个原解**与
R710 的全部中央进位、原固定 $\phi_m$ 及 R708 的实际前缀联系起来。
原 $j_m=0$ 尚未被证明迫此前缀零；
同源 pullback 也没有免费进入旧预算格。
这些条件继续保留。

依赖：
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)；
[R718](R718-original-cm-distribution-and-unique-gaussian-resonance.md)；
[R720](R720-two-fixed-cm-sources-and-density-one-resonance-window.md)；
[R721](R721-minimal-two-torsion-poles-for-original-height-two-parameter.md)；
[R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)；
[R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)。
