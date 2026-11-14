# R294：Cartan 标量强迫非约化 Hasse 消失及精确判别式惯性

日期：2026-11-13。状态：**已证明；必要条件与局部精确公式，主问题未完成。**

本文从 R21 已用的 Raynaud 有限平坦延拓出发，证明完整非分裂 Cartan 正规化子情形的好约化模型，在整个 $\mathcal O_L/(p)$ 上 Hasse 不变量为零。这里没有选定全局 CM 域或 CM 参考曲线。继续使用同一个 Raynaud 方程，可以从实际最小判别式直接恢复全部 $p$ 处惯性角色，而非只恢复其十二次幂。

特别地，R290 的 $v_p(j)\ge4,5$ 及其 $p\bmod9$ 方向扩展至**任意商二次域的全部严格小惯性分支**。证明没有把模 $p$ 挠点当成模 $p^2$ 挠点，也没有使用尚未公认的高次 $p$ 进像分类。

## 1. 设置与主结论

设 $p>37$，$E/\mathbb Q$ 无 CM，且实际模 $p$ 像为 R1 的完整非分裂 Cartan 正规化子
$$
N=C\rtimes\langle s\rangle,\qquad C\simeq\mathbb F_{p^2}^{\times}.
\tag{294.1}
$$
按 R5，$\rho_{E,p}(I_p)\subset C$；按 R15，$E/\mathbb Q_p$ 潜在好超奇异。取 $p$ 处极小短模型
$$
E:\ y^2=x^3+a x+b,\qquad a,b\in\mathbb Z_p,
\qquad \delta=v_p\bigl(-16(4a^3+27b^2)\bigr).
\tag{294.2}
$$
令 $T=p^2-1$，并固定由 $\varpi^T=p$ 定义的第二层基本惯性特征
$$
\omega_2(g)=\overline{g(\varpi)/\varpi}\in\mathbb F_{p^2}^{\times}
\qquad(g\in I_p).
\tag{294.3}
$$
选取另一个剩余域嵌入至多把 $\omega_2$ 换为 $\omega_2^p$。

**定理 294.1。**

1. 在一个实际好约化扩张 $L/\mathbb Q_p$ 上，令 $\mathcal E/\mathcal O_L$ 为好模型，$R=\mathcal O_L/(p)$。其 Hasse 不变量在 $R$ 中**恒等于零**，不是仅在 $R$ 的剩余域中为零。
2. 有 $\delta\in\{0,2,3,4,6,8,9,10\}$。令
   $$
   B_\delta=1-\frac{\delta T}{12}\in\mathbb Z.
   \tag{294.4}
   $$
   则实际惯性表示的两个特征恰为
   $$
   \boxed{\omega_2^{B_\delta},\quad\omega_2^{pB_\delta}.}
   \tag{294.5}
   $$
   因而
   $$
   [C:\rho_{E,p}(I_p)]=\gcd(B_\delta,T)\in\{1,3\}.
   \tag{294.6}
   $$
3. 严格小惯性 $\rho_{E,p}(I_p)=C^3$ 的精确方向是
   $$
   \boxed{
   \begin{array}{c|c|c}
   p\bmod9&\delta&v_p(j(E))\\ \hline
   5&2\text{ 或 }8&1+3\mathbb Z_{\ge1}\\
   2&4\text{ 或 }10&2+3\mathbb Z_{\ge1}.
   \end{array}}
   \tag{294.7}
   $$
   这里第一行的最低值为 $4$，第二行为 $5$，并且没有 $K=\mathbb Q(\sqrt{-3})$ 或 R258 的 $\sigma=1$ 前提。

**定理 294.2。** 不限于小惯性，全部实际异常情形还满足：
$$
\begin{aligned}
v_p(j)>0&\Longrightarrow p\equiv2\pmod3,\quad v_p(j)\ge3,\\
v_p(j-1728)>0&\Longrightarrow p\equiv3\pmod4,\quad v_p(j-1728)\ge2.
\end{aligned}
\tag{294.8}
$$
后一行在最小好约化分歧指数 $e=4$ 时提高为
$$
v_p(j-1728)\in3+2\mathbb Z_{\ge0}.
\tag{294.9}
$$
第 5、6 节给出带最小模型系数的完整赋值表。

## 2. 取得好约化及整个 $G_L$ 上的 Cartan 标量

不能只知道 $I_L$ 的像在 $C$ 就把所有 $\mathbb F_{p^2}$ 标量当成 $G_L$ 端同态。以下选择实际处理这个区别。

因为 $j,j-1728\in\mathbb Z_p$，由短模型不变量得
$$
3v_p(a)\ge\delta,\qquad 2v_p(b)\ge\delta.
\tag{294.10}
$$
若 $\delta\ge12$，则 $p^4\mid a,p^6\mid b$，可以作 $x=p^2X,y=p^3Y$，违背极小性。因此 $0\le\delta<12$。若 $3v_p(a)\ne2v_p(b)$，则 $\delta$ 是这两个数的较小者；相等时，(294.10) 又迫该共同值就是 $\delta$，不能发生更高的抵消。所以
$$
\delta\in\{0,2,3,4,6,8,9,10\},\qquad
e_0=\frac{12}{\gcd(12,\delta)}\in\{1,2,3,4,6\},
\tag{294.11}
$$
其中 $\delta=0$ 时规定 $e_0=1$。任何好约化扩张的分歧指数 $e$ 必满足 $12\mid e\delta$，因为两个 Weierstrass 判别式相差缩放因子的十二次幂；下面的模型达到 $e_0$，所以 $e_0$ 确为最小好约化分歧指数。

在包含 $u=p^{\delta/12}$ 的温和扩张上，缩放
$$
x=u^2X,\qquad y=u^3Y
\tag{294.12}
$$
给好模型
$$
Y^2=X^3+A X+B,\qquad A=a/u^4,\quad B=b/u^6,
\tag{294.13}
$$
因为系数由 (294.10) 为整，判别式为单位。加入 $e_0$ 次单位根仅需不分歧扩张，所以可先取一个有限 Galois 好约化扩张 $L_0/\mathbb Q_p$，其分歧指数为 $e_0\le6$。

令 $F/\mathbb Q_p$ 为局部复合特征
$$
G_{\mathbb Q_p}\longrightarrow N/C\simeq\{\pm1\}
\tag{294.14}
$$
的核所切出的至多二次扩张。取 $L$ 包含 $L_0F$，必要时再加不分歧二次扩张。于是
$$
\rho_{E,p}(G_L)\subset C,\qquad e_L\le12<p-1.
\tag{294.15}
$$
实际上 R5 已给出本题的 (294.14) 在 $p$ 不分歧，所以此处可保留 $e_L=e_0\le6$；证明只用较宽的 $12$ 上界。

把 $E[p](\overline{\mathbb Q}_p)$ 识别为 $\mathbb F_{p^2}$ 的加法群。由于 (294.15)，每个标量乘法 $[z]$，$z\in\mathbb F_{p^2}$，都是一般纤维 $E[p]_L$ 的 $L$ 群概形端同态。Raynaud (1974), Corollaire 3.3.6(1) 的全忠实性，在绝对分歧指数 $e_L<p-1$ 下给唯一延拓
$$
\mathbb F_{p^2}\longrightarrow
\operatorname{End}_{\mathcal O_L}(\mathcal E[p]).
\tag{294.16}
$$
唯一性保持端同态的加法、复合及单位，因此 (294.16) 是一个真正的含单位环作用。这里使用完整 $G_L$ 的可交换性，而非仅惯性可交换性。

## 3. 非约化底环上的 Lie 标量及 Verschiebung

置 $G=\mathcal E[p]_R$，$R=\mathcal O_L/(p)$。虽然 $R$ 一般非约化，仍有
$$
\operatorname{Lie}G=\operatorname{Lie}(\mathcal E_R),
\tag{294.17}
$$
且这个模自由秩一。可直接在 $R[\epsilon]/(\epsilon^2)$ 上验证：$\mathcal E[p]$ 的切向量正是被 $d[p]=p=0$ 杀掉的椭圆曲线切向量，所以所有切向量均属于 $G$。

选择一组基后，(294.16) 的导数给含单位环同态
$$
\kappa:\mathbb F_{p^2}\longrightarrow
\operatorname{End}_R(\operatorname{Lie}G)=R.
\tag{294.18}
$$
其核不是整个域，因为 $\kappa(1)=1$，故它是环嵌入。更直接地，对任何非零 $z$，
$$
\kappa(z)\kappa(z^{-1})=1,
\tag{294.19}
$$
所以 $\kappa(z)$ 是 $R$ 的单位；这一步不要求 $R$ 为域或约化环。

对任意特征 $p$ 底概形上的有限局部自由交换群概形，内在 Verschiebung 是
$$
V_G=(F_{G^D})^D:G^{(p)}\longrightarrow G,
\tag{294.20}
$$
并对所有群概形同态具有函子性。SGA 3, Exposé VIIA, §4.3 定义任意平坦交换群上的同态 $V$，§4.3.3 证明在有限情形中与 (294.20) 一致。因此它与闭嵌入 $\mathcal E[p]_R\hookrightarrow\mathcal E_R$ 相容，恰是椭圆曲线 Verschiebung 的限制。这里的底环始终是 $R$，没有换成剩余域。

Frobenius 基变换给
$$
\operatorname{Lie}(G^{(p)})=F_R^*(\operatorname{Lie}G).
$$
故若 $d[z]$ 在选定基中是 $\kappa(z)$，则在该基的 Frobenius 拉回中
$$
d([z]^{(p)})=\kappa(z)^p.
\tag{294.21}
$$
这是沿 $F_R:r\mapsto r^p$ 作张量积的标量关系，在非约化环上仍成立。

由函子性 $[z]\circ V_G=V_G\circ[z]^{(p)}$，取导数得
$$
\kappa(z)\,dV_G=dV_G\,\kappa(z)^p.
\tag{294.22}
$$
取 $z\in\mathbb F_{p^2}\setminus\mathbb F_p$。因为
$$
\kappa(z)-\kappa(z)^p=\kappa(z-z^p)\in R^\times,
\tag{294.23}
$$
所以
$$
\boxed{dV_G=0.}
\tag{294.24}
$$
由 (294.17) 及 Verschiebung 的限制相容性，(294.24) 就是 $dV_{\mathcal E_R}=0$。以不变微分作基，$dV$ 的标量就是 Hasse 不变量，故定理 294.1(1) 成立。

R290 §§2–3 已在任意特征 $p$ 底环上通过明确 Čech 覆盖证明：对判别式为单位的短方程，Hasse 标量为
$$
H_p(A,B)=[X^{p-1}](X^3+AX+B)^{(p-1)/2}.
\tag{294.25}
$$
该证明把相对 Frobenius 在 $H^1(\mathcal E,\mathcal O)$ 上的拉回，与 Picard 对偶 Verschiebung 的导数相认；没有对非完美环非法取 $p$ 次根。本节只需这一完整证明及 (294.20) 的已发表函子性。

若最初的好模型定义在较小的 $L_0$ 上，$\mathcal O_{L_0}/(p)\to\mathcal O_L/(p)$ 忠实平坦。因此上面得到的 Hasse 消失也沿这个基变换下降。继续扩张好约化域不会改变结论。

## 4. 从 Raynaud 存活坐标恢复精确惯性角色

本节证明 (294.5)，包括模型缩放的方向。

由 (294.16)，$\mathcal G=\mathcal E[p]/\mathcal O_L$ 是 Raynaud 的 $\mathbb F_{p^2}$ 向量群概形。各非平凡乘法特征分量的秩一性质、分类适用性及余切模比较已在 R21 §§2–3 完整证明。交换编号后可以写为
$$
\mathcal G=\operatorname{Spec}
\mathcal O_L[X_0,X_1]/(X_0^p-d_0X_1,\ X_1^p-d_1X_0),
\tag{294.26}
$$
其中
$$
d_0\in\mathcal O_L^\times,\qquad v_p(d_1)=1.
\tag{294.27}
$$
这里将赋值统一归一化为 $v_p(p)=1$。其证明中的关键是
$$
\omega_{\mathcal G}
=\mathcal O_L/(d_1)\,dX_0\oplus\mathcal O_L/(d_0)\,dX_1
\simeq\mathcal O_L/(p),
$$
所以一个 $d_i$ 必为单位，另一个的赋值恰为 $1$，不是任意混合权。

消去 $X_1$，每个非零几何 $p$ 挠点均满足
$$
X_0^{p^2-1}=d_0^p d_1,
\qquad v_p(X_0)=1/T.
\tag{294.28}
$$
由 (294.26) 的特殊纤维，全部 $p$ 挠点约化至原点。令
$$
t'=-X/Y
$$
为好短模型 (294.13) 在原点的形式参数。因为 $dX_0$ 生成 $\omega_{\mathcal G}\simeq\mathcal O_L/(p)$，在 $\mathcal G$ 的完成局部环中可写
$$
X_0=c_1t'+c_2(t')^2+\cdots,\qquad
c_i\in\mathcal O_L,\quad c_1\in\mathcal O_L^\times.
\tag{294.29}
$$
具体地，$\mathcal G$ 是形式群中 $[p](t')=0$ 的闭子群，故 $X_0$ 有整系数形式幂级数表示；其余切生成性质使一次项模极大理想非零。对非零挠点 $v_p(t')>0$，所以高次项赋值严格大于一次项，从 (294.28) 得
$$
\boxed{v_p(t'(P))=1/T\quad(P\in E[p]\setminus\{O\}).}
\tag{294.30}
$$

原极小短模型的参数 $t=-x/y$ 定义在 $\mathbb Q_p$ 上。缩放 (294.12) 给
$$
t=t'/u,\qquad
v_p(t(P))=\frac1T-\frac\delta{12}=\frac{B_\delta}{T}.
\tag{294.31}
$$
因 $p>3$ 时 $24\mid T$，$B_\delta$ 确是整数，且为奇数。允许 $B_\delta<0$；此时原模型中的参数有负赋值，但好模型中的 $t'$ 始终有正赋值。

使用 (294.3) 的同一个 $\varpi$，定义
$$
\ell(P)=\overline{t(P)/\varpi^{B_\delta}}
\in\overline{\mathbb F}_p\quad(P\ne O),\qquad\ell(O)=0.
\tag{294.32}
$$
所有非零点的值都非零。好模型的形式群加法为
$$
t'(P+Q)=t'(P)+t'(Q)+
\sum_{r,s\ge1}c_{r,s}t'(P)^r t'(Q)^s,
\qquad c_{r,s}\in\mathcal O_L.
$$
除以 $u\varpi^{B_\delta}$ 后，其分母的赋值为 $1/T$。每个高次项的赋值至少为 $2/T$，故取剩余值时全部消失。因此 $\ell$ 是 $\mathbb F_p$ 线性单射，其像为二维 $\mathbb F_p$ 子空间。

对 $g\in I_p$，原参数 $t$ 的 $\mathbb Q_p$ 定义性及惯性在代数闭剩余域上作用平凡给
$$
\begin{aligned}
\ell(gP)
&=\overline{g(t(P))/\varpi^{B_\delta}}\\
&=\overline{g\bigl(t(P)/\varpi^{B_\delta}\bigr)}
  \,\overline{g(\varpi)/\varpi}^{B_\delta}\\
&=\omega_2(g)^{B_\delta}\ell(P).
\end{aligned}
\tag{294.33}
$$
这固定了 (294.4) 中的**负号**。

还可以直接核实乘法角色的像不是标量群。若 $d=\gcd(B_\delta,T)$，由
$$
12B_\delta=12-\delta T
$$
得 $d\mid12$；而 $B_\delta$ 为奇数，所以 $d=1$ 或 $3$。因此该角色的像阶至少为 $T/3>p-1$。它在 $\mathbb F_{p^2}$ 中含非 $\mathbb F_p$ 的元素。任取 $\ell(P)\ne0$，二维像必等于 $\ell(P)\mathbb F_{p^2}$；在这个基下 (294.33) 就是 $\mathbb F_{p^2}$ 乘法表示。其两个嵌入给 (294.5)，并得到 (294.6)。

## 5. $j=0$ 剩余圆盘：全部系数精度与小惯性方向

假设 $v_p(j)>0$。好模型的剩余曲线具有 $j=0$，所以 $A$ 非单位、$B$ 为单位。由于第 3 节的 Hasse 消失，必须有 $p\equiv2\pmod3$：若 $p\equiv1\pmod3$，则
$$
H_p(0,B)=\binom{(p-1)/2}{(p-1)/3}B^{(p-1)/6}
$$
为单位，矛盾。

写 $p=6h+5$。对 (294.25) 逐项取系数得到
$$
H_p(A,B)=
\sum_{r=0}^{\lfloor h/2\rfloor}
\frac{(3h+2)!}{(2h+1-r)!(1+3r)!(h-2r)!}
A^{1+3r}B^{h-2r}.
\tag{294.34}
$$
所有阶乘的参数均小于 $p$。首项系数 $c_0$ 模 $p$ 非零，因而在 $R$ 上
$$
H_p(A,B)=A B^h
\left(c_0+\sum_{r\ge1}c_r(A^3/B^2)^r\right).
\tag{294.35}
$$
括号为单位，因为 $A$ 在极大理想中而 $B$ 为单位。因此
$$
H_p(A,B)=0\text{ in }R
\quad\Longrightarrow\quad A\in p\mathcal O_L.
\tag{294.36}
$$
这里得到的是精确的 $p$ 整除性，不只是均匀化参数整除性。

由 $2v_p(b)=\delta$ 及 (294.13)、(294.36)，
$$
v_p(a)\ge\left\lceil1+\frac\delta3\right\rceil,
\qquad
v_p(j)=3v_p(a)-\delta.
\tag{294.37}
$$
完整表为：

| $\delta$ | $e_0$ | $v_p(b)$ | $v_p(a)$ 的必要下界 | $v_p(j)$ 的全部必要赋值 |
|---:|---:|---:|---:|---|
| $0$ | $1$ | $0$ | $1$ | $3+3\mathbb Z_{\ge0}$ |
| $2$ | $6$ | $1$ | $2$ | $4+3\mathbb Z_{\ge0}$ |
| $4$ | $3$ | $2$ | $3$ | $5+3\mathbb Z_{\ge0}$ |
| $6$ | $2$ | $3$ | $3$ | $3+3\mathbb Z_{\ge0}$ |
| $8$ | $3$ | $4$ | $4$ | $4+3\mathbb Z_{\ge0}$ |
| $10$ | $6$ | $5$ | $5$ | $5+3\mathbb Z_{\ge0}$ |

表中的“全部必要赋值”表示精确同余类及下界，不声称每个数值都有全局异常曲线实现。

现在判定 (294.6) 何时为 $3$。$\delta=0,3,6,9$ 时 $B_\delta\equiv1\pmod3$，所以惯性完整。对于 $\delta=2,4,8,10$，好模型的 $j$ 约化为零，上面已经证明 $p\equiv2\pmod3$。按 $p\bmod9$，直接有
$$
\frac{T}{12}\equiv
\begin{cases}
1\pmod3,&p\equiv2\pmod9,\\
2\pmod3,&p\equiv5\pmod9,\\
0\pmod3,&p\equiv8\pmod9.
\end{cases}
\tag{294.38}
$$
例如这些素数分别为 $11,5,17\pmod{18}$，代入 $(p^2-1)/12$ 即得。于是 $3\mid B_\delta$ 精确等价于 (294.7) 的两行；$p\equiv8\pmod9$ 时惯性始终完整。这同时证明定理 294.1(3) 及定理 294.2 的第一行。

## 6. $j=1728$ 剩余圆盘

假设 $v_p(j-1728)>0$。此时好模型中 $A$ 为单位、$B$ 非单位。若 $p\equiv1\pmod4$，则
$$
H_p(A,0)=\binom{(p-1)/2}{(p-1)/4}A^{(p-1)/4}
$$
为单位，所以只能 $p\equiv3\pmod4$。

写 $p=4h+3$，则 $h\ge1$。在 (294.25) 中，令来自 $B$ 的项数为 $1+2r$，另外两种项数分别为 $h+1+r$ 与 $h-1-3r$，得到
$$
H_p(A,B)=
\sum_{r=0}^{\lfloor(h-1)/3\rfloor}
\frac{(2h+1)!}{(h+1+r)!(h-1-3r)!(1+2r)!}
A^{h-1-3r}B^{1+2r}.
\tag{294.39}
$$
故
$$
H_p(A,B)=B A^{h-1}
\left(d_0+\sum_{r\ge1}d_r(B^2/A^3)^r\right),
\qquad d_0\not\equiv0\pmod p.
\tag{294.40}
$$
括号为单位。因此第 3 节的消失迫 $B\in p\mathcal O_L$。

此时 $3v_p(a)=\delta$，而
$$
v_p(b)\ge\left\lceil1+\frac\delta2\right\rceil,
\qquad
v_p(j-1728)=2v_p(b)-\delta.
\tag{294.41}
$$
得到：

| $\delta$ | $e_0$ | $v_p(a)$ | $v_p(b)$ 的必要下界 | $v_p(j-1728)$ 的全部必要赋值 |
|---:|---:|---:|---:|---|
| $0$ | $1$ | $0$ | $1$ | $2+2\mathbb Z_{\ge0}$ |
| $3$ | $4$ | $1$ | $3$ | $3+2\mathbb Z_{\ge0}$ |
| $6$ | $2$ | $2$ | $4$ | $2+2\mathbb Z_{\ge0}$ |
| $9$ | $4$ | $3$ | $6$ | $3+2\mathbb Z_{\ge0}$ |

这证明 (294.8) 的第二行及 (294.9)。四种情形的惯性都为完整 $C$；它们不会误入严格小惯性分支。

## 7. 全局既约分子和实际三次参数的后果

写 $j=A_j/B_j$ 为既约分数，$B_j>0$。R2 给 $p\nmid B_j$。由 (294.8)，
$$
\begin{aligned}
p\mid A_j&\Longrightarrow p^3\mid A_j,\\
p\mid A_j-1728B_j&\Longrightarrow p^2\mid A_j-1728B_j.
\end{aligned}
\tag{294.42}
$$
在任意商域的严格小惯性分支中，进一步有
$$
\boxed{
\begin{aligned}
p\equiv5\pmod9&\Longrightarrow v_p(A_j)\in1+3\mathbb Z_{\ge1},\\
p\equiv2\pmod9&\Longrightarrow v_p(A_j)\in2+3\mathbb Z_{\ge1}.
\end{aligned}}
\tag{294.43}
$$
特别对 R96 的全部七个类数一、原始环类数三组合，而不仅是 $K=\mathbb Q(\sqrt{-3})$，若整 $j$ 的实际三次分解写为
$$
j=d_j x^3,\qquad d_j\in\mathbb Z\text{ 立方自由},\quad x\in\mathbb Z,
$$
则
$$
\boxed{p\mid x,\qquad
v_p(d_j)=\begin{cases}1,&p\equiv5\pmod9,\\2,&p\equiv2\pmod9.
\end{cases}}
\tag{294.44}
$$
这个结论作用于实际 $j$ 分解；不能只凭支撑候选就反向声称存在实际异常曲线。R290 在共同二除、三除域的特定全局模型中进一步把该整除性译成 $p\mid w$、$t\equiv2\pmod{p^{m+3}}$；那一步仍须保留其真实全局模型前提。

## 8. 文献、证明范围及未完成量

1. M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. Soc. Math. France **102** (1974), 241–280：[原文](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。使用 Théorème 1.4.1、Corollaire 1.5.1 的向量群分类，以及 Théorème 3.3.3、Corollaire 3.3.6(1), p. 268 的 $e<p-1$ 全忠实性；群环作用与端点余切模接口见 [R21](R21-twelfth-power-signature-and-cm-twists.md) §§2–4。
2. P. Gabriel, SGA 3, Exposé VIIA, §4.3、§4.3.2–4.3.3：[原刊 exposé](https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp7A.pdf)，原边页 441–445。使用一般特征 $p$ 底概形上的 Verschiebung 函子性及有限平坦时的 Cartier 对偶公式；与椭圆曲线及非约化 Hasse 标量的完整接口见 [R290](R290-nonreduced-hasse-invariant-and-fourth-order-cm-proximity.md)。
3. 文献定位：M. Bisatt, L. Furio, D. Lombardo, *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, [arXiv:2603.04021v2](https://arxiv.org/abs/2603.04021), 2026-06-08，§2.9、Proposition 8.30、Corollary 8.31，包含相关规范子群及 $j$ 赋值边界。本文不主张这些赋值边界是新的文献定理，也没有用该预印本的高次像分类作证明前提；R35 已明确保留此文献边界。本文的群概形标量论证和精确惯性首项计算已在 §§2–6 独立展开。

本结果只确定 $p$ 挠点强迫的 Hasse 精度及实际惯性。$dV=0$ 是在 $\mathcal O_L/(p)$ 上的等式，**不**表示特征零 Hasse 提升严格为零，也不自动给模 $p^2$ 的 CM 挠点同构或更高阶消失。相同 $j$ 剩余圆盘也不自动指定 $X_{\rm ns}^+(p)$ 的同一个水平结构或特殊纤维点。

O6 的忠实上层实际 Norm 原像和规范剩余量 $\mathcal L$ 仍未求得；R202 继续仅保留给实际 $\mathcal L$。这里没有得到导子或高度的统一上界，没有排除全部异常 $p$，因而课题主要目标仍未完成。
