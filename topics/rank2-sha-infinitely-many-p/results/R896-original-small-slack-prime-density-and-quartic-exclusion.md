# R896 — 原低松弛 quartic 排除的无穷素数与准确正密度

日期：2026-11-16。**状态：以下素数密度及对 R895 精确候选类的排除已证明。**
这是原两长预算中一个实际无穷素数推论；它不排除一般首核，不证明通常全 Selmer 群的余秩，也不完成主目标。

## 1. 原维数与逐素数选择

保留 R680/R895 的同一 canonical 来源
$$
N_D=\dim\overline{\mathcal W}_D
=\sum_{n=0}^D(e_{n+1}+1),
$$
$$
e_{n+1}=\lfloor9n/2\rfloor+4
-3\lfloor(n+1)/4\rfloor-\lfloor(n+1)/3\rfloor+\lfloor n/2\rfloor.
\tag{1}
$$
对 $p\equiv11\pmod{12}$，置
$$
s=(p+1)/6,\quad h=(s-2)/2=(p-11)/12,\qquad
D(p)=\min\{D\ge0:N_D\ge2s\}.
\tag{2}
$$
$N_D$ 严格递增并趋于无穷，故 (2) 有定义。记实际非负差
$$
a(p)=N_{D(p)}-2s.
\tag{3}
$$

定义素数集
$$
\mathcal P_{\rm low}
=\{p\equiv11\pmod{12}:a(p)\le D(p)+15\}.
\tag{4}
$$
下文证明
$$
\boxed{
\lim_{X\to\infty}
\frac{\#\{p\le X:p\in\mathcal P_{\rm low}\}}
     {\#\{p\le X:p\equiv11\pmod{12}\}}
=\frac{12}{47}.
}
\tag{5}
$$
因此它在全体素数中的相对自然密度为 $3/47$，特别包含无穷不同素数。

对这些素数，只要候选满足 R895 的其余原范围，在同一个
$D(p)$ 的原矩阵内，不存在 R895 所述
$r=3,\tau=1,\bar P=t^3F^4q$ 的完整同 $P,R,S$ 的 $p^3$ 提升。
这里不主张任何原首核必定是该类型。

## 2. 全部取整项：线性系数不能略去

置 $m=D+1$，并记
$$
\epsilon=m\bmod2,\qquad r_4=m\bmod4,\qquad r_3=m\bmod3.
$$
由 (1)，准确有
$$
e_{n+1}+1
=5n+5-(n\bmod2)-3\lfloor(n+1)/4\rfloor-\lfloor(n+1)/3\rfloor.
$$
分块求和给
$$
\sum_{k=1}^m\lfloor k/4\rfloor
=\frac{m^2}{8}-\frac m4+\frac{r_4(2-r_4)}8,
$$
$$
\sum_{k=1}^m\lfloor k/3\rfloor
=\frac{m^2}{6}-\frac m6+\frac{r_3(1-r_3)}6,
\qquad
\sum_{n=0}^{m-1}(n\bmod2)=\frac{m-\epsilon}{2}.
$$
例如第一式把 $m=4q+r_4$ 代入后，两边都等于
$2q^2-q+qr_4$；第二式同样把 $m=3q+r_3$ 分成完整三项块即可。
于是
$$
N_D=\frac{47}{24}m^2+\frac{35}{12}m
+\frac{\epsilon}{2}
-\frac{3r_4(2-r_4)}8-\frac{r_3(1-r_3)}6.
$$
换回 $D$ 得完整拟多项式
$$
\boxed{
N_D=\frac{47}{24}D^2+\frac{41}{6}D+\gamma_D,\quad
\gamma_D=\frac{39}{8}+\frac{\epsilon}{2}
-\frac{3r_4(2-r_4)}8-\frac{r_3(1-r_3)}6.
}
\tag{6}
$$
$\gamma_D$ 只依赖 $D\bmod12$，所以有界。
此外 (1) 给 $e_{n+1}+1\ge(47n+35)/12>0$，证明第1节使用的严格递增。

令
$$
U_D=3N_D-1,\qquad A=\frac{47}{8},\qquad \beta=\frac{82}{47}.
$$
(6) 准确写成
$$
\boxed{U_D=A(D+\beta)^2+c_D,\qquad
c_D=3\gamma_D-1-A\beta^2=O(1).}
\tag{7}
$$
因此实际线性项产生平移 $\beta$；不能只以
$\sqrt{8p/47}$ 而不记录这个平移来判每个素数的有限条件。

由 (2)，对充分大 $p$，$D=D(p)$ 的准确区间是
$$
U_{D-1}<p\le U_D.
\tag{8}
$$
同一个 $D$ 内 (4) 等价为
$$
\boxed{
3N_D-3(D+15)-1\le p\le3N_D-1.
}
\tag{9}
$$
对充分大 $D$，(9) 的下端大于 $U_{D-1}$，因为
$N_D-N_{D-1}=(47/12)D+O(1)>D+15$。
因此 (9) 确实位于该最小 $D$ 的区间，未把相邻来源混合。

## 3. 固定同余类上的平方根相位等分布

记
$$
x(p)=\sqrt{8p/47}-82/47.
\tag{10}
$$
对任意固定 $q\ge1$、$(b,q)=1$，序列
$$
(x(p)\bmod1)_{p\equiv b\ ({\rm mod}\ q)}
\tag{11}
$$
等分布于 $[0,1)$。

这里直接从已发表的 Bergelson–Kolesnik–Madritsch–Son–Tichy
Theorem 2.1 推出，不需要短区间逐段有素数。该定理适用于有非零非整数幂项的有限实幂和，容许同时有实系数整数幂项。

具体地，固定非零整数 $k$，令 $e(u)=\exp(2\pi i u)$。
用同余类的有限 Fourier 恒等式，
$$
\sum_{\substack{p\le X\\p\equiv b\ ({\rm mod}\ q)}}e(kx(p))
=
\frac{e(-k\beta)}q
\sum_{j=0}^{q-1}e(-jb/q)
\sum_{p\le X}e\left(k\sqrt{8/47}\,p^{1/2}+\frac jq p\right).
\tag{12}
$$
每个内和除以 $\pi(X)$ 趋于零：当 $j=0$ 只有非零平方根项，
当 $j\ne0$ 加上线性项仍满足上述 Theorem 2.1。
固定等差数列的素数定理给
$$
\pi(X;q,b)/\pi(X)\longrightarrow1/\varphi(q).
$$
故 (12) 除以 $\pi(X;q,b)$ 也趋于零。
Weyl 判据证明 (11)。常数平移和有限个排除素数均不改变结论。

注意这里的指数是 $1/2$。我们直接使用 Theorem 2.1 和 (12)，
不借用另带指数附加条件的 corollary。该段唯一深的分析输入是
已发表的实幂素数等分布定理及固定模数的素数定理；没有假设
GRH、素数间隙猜想或每个长度 $\asymp\sqrt X$ 区间都有素数。

## 4. 最小维数误差与密度的完整夹逼

由 (7)–(8)，
$$
D(p)-x(p)\in[-O(D^{-1}),1+O(D^{-1})].
\tag{13}
$$
只要 $\{x(p)\}$ 与 $0,1$ 的距离大于固定 $\varepsilon>0$，
充分大时 (13) 便给
$$
D(p)=\lceil x(p)\rceil,\qquad D(p)-x(p)=1-\{x(p)\}.
\tag{14}
$$
使用 (7) 和 $p=A(x(p)+\beta)^2$，得到
$$
\begin{aligned}
a(p)
&=(U_D-p)/3\\
&=\frac A3(D-x(p))(D+x(p)+2\beta)+\frac{c_D}{3}\\
&=\frac{47}{12}D(D-x(p))+O(1).
\end{aligned}
\tag{15}
$$
误差对所有余类一致有界，因为 $\gamma_D$ 周期有界、(13) 保证
$D-x(p)$ 有界。准确地，令
$\varepsilon_p=a(p)/D-(47/12)(D-x(p))=O(D^{-1})$，
则
$
a(p)\le D+15
\quad\Longleftrightarrow\quad
D-x(p)\le\frac{12}{47}
+\frac{12}{47}\left(\frac{15}{D}-\varepsilon_p\right).
\tag{16}
$
这个实际误差将在下述夹逼中完整保留。

取 $0<\varepsilon<6/47$。对充分大素数，
$$
\{x(p)\}\in(35/47+\varepsilon,1-\varepsilon)
\ \Longrightarrow\ p\in\mathcal P_{\rm low}
$$
（这里同时要求 $p\equiv11\pmod{12}$），反之
$$
p\in\mathcal P_{\rm low}
\ \Longrightarrow\
\{x(p)\}\in(35/47-\varepsilon,1)\cup[0,\varepsilon).
\tag{17}
$$
第一项由 (14)–(15) 给严格余量；第二项把整数附近 (14) 可能失效的
全部端点窗也计入。没有未经证明地声称 $O(1)$ 长度的变动区间含素数很少。

第3节在 $q=12,b=11$ 上应用，(17) 分别给相对下、上密度
$$
12/47-2\varepsilon,\qquad 12/47+2\varepsilon.
$$
令 $\varepsilon\to0$，即得 (5)。再乘该固定素数同余类的密度
$1/\varphi(12)=1/4$，得到全体素数中的 $3/47$。

同一证明还给：若固定 $12\mid q$、$(b,q)=1$、
$b\equiv11\pmod{12}$，则 (4) 在 $p\equiv b\pmod q$ 中的相对密度
仍为 $12/47$，在全体素数中的密度为 $12/(47\varphi(q))$。
这只加入固定同余条件，不声称保持任意非阿贝尔 Chebotarev 条件。

## 5. 回到同一个原四块和 R895

由 (6)，
$$
D(p)\sim\sqrt{8p/47},\qquad p/D(p)^2\longrightarrow47/8.
\tag{18}
$$
所以原 $p>D+40$、$f_D<p$ 及固定有限坏素数排除在充分大时成立。
$p\equiv11\pmod{12}$ 使 $s=2h+2$，并使 R895 的
$h<s-4$、$h\ge17$ 自动在充分大时成立。

对 R895 允许的任意 $1<\ell\le h-1$，仍准确定义
$$
\delta_D=N_D-(2s+\ell).
$$
此时
$$
\ell+\delta_D=N_D-2s=a(p).
\tag{19}
$$
因此对 $\mathcal P_{\rm low}$ 内充分大素数，
$$
\ell+\delta_D\le D+15\le D+15+2j
\quad(0\le j\le2).
$$
R895 的严格反门直接排除该候选的完整同源 $p^3$ 提升。
不需假设 $\delta_D\ge0$ 或 $\delta_D=0$，也不需假设
$\mathfrak o_D(R)=0$。

所用的 $D$ 是 (2) 里新定义的逐素数来源。这个选择允许定义并研究
相应原 $\mathcal W_D/M$；它**不授权**把别的已经固定了
$D,k$ 的全局旗标或预算换成 (2)。
若某个应用要求另一套固定来源，必须先实际证明两者的关系。

## 6. 尚未排除的原对象

本条证明了一个具有明确正密度的、同一候选类上的无穷排除。
稠密混合 charge 的一般首核、其它 $r/\tau$、非单位余因子、
奇异支，以及原完整 $K_1$ 的同修正全高前缀仍保留在 open。
本条不证明这些来源自动转为 R895 的 quartic，也不声称原
Bost/Smith 的饱和成本已改善。

尤其“无穷多个素数排除某个 quartic 类型”不是
“无穷多个素数的通常全 Sha 初级部分有限”。原任务后者仍未完成。

## 7. 精确来源

- V. Bergelson, G. Kolesnik, M. Madritsch, Y. Son and R. Tichy,
  *Uniform distribution of prime powers and sets of recurrence and van der Corput sets in $\mathbf Z^k$*,
  Israel J. Math. **201** (2014), 729–760,
  DOI 10.1007/s11856-014-1049-4，
  Theorem 2.1（p.735；证明至p.741）；
  固定同余类的 Fourier 恒等式与素数相对密度亦见 pp.742–743。
  [作者主页完整 PDF](https://people.math.osu.edu/bergelson.1/BKMS_PrimePowers.pdf)。
- [R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)：
  同一十九角来源及(1)。
- [R895](R895-original-quartic-same-corrector-intersection-and-small-slack-exclusion.md)：
  同 $P,R,S$ 完整 $p^3$ 的准确低松弛反门。

本篇是手工证明，无数学程序、素数扫描或可重算数据输出。
