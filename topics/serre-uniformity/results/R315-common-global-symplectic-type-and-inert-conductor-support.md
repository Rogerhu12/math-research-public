# R315：同一个全局同构的辛型与惰性坏素数支撑排除

日期：2026-11-13。状态：**已证明；实际分支的新增必要条件，主要目标仍 OPEN。**

本篇固定原来实际的全局模 $p$ 同构，比较它在表示素数 $p$、素数二、
以及其他惰性坏素数处的 Weil 配对乘子。这里不能在每个地方任意改选
一个有利同构：只有证明局部中心化子的行列式都是平方之后，
一个局部同构的辛型才约束同一个全局同构。

主要结论是：全部实际分支的全局同构均有平方辛型；在偶分支
$4\mid a$ 中，若 $p\equiv5\pmod {12}$，实际正立方自由参数 $d$
不能有任何 $q\equiv11\pmod {12}$ 的素因子。
这是一条对变化坏支撑的排除，而不是导子上界。

## 1. 实际范围与乘子的固定方式

保持 R289、R301、R306 的实际参数：
$$
\begin{gathered}
p>37,\qquad p\equiv2,5\pmod9,\qquad
a^3+db^3=1,\qquad d>0\text{ 立方自由},\\
a,b\in\mathbb Z,\qquad a\ne0,1,\qquad b\ne0,\qquad
r=1-a^3=db^3,\\
\varepsilon=-1\quad(4\mid a),\qquad
\varepsilon=1\quad(a\equiv1\pmod {16}),\\
H_a:y^2=x^3+3arx-r(2a^3-1),\qquad
B_a=A_{-\varepsilon r}:y^2=x^3-\varepsilon r,\\
\phi:H_a[p]\xrightarrow{\sim}B_a[p]
\quad\text{为同一个实际 }G_{\mathbb Q}\text{-模同构}.
\end{gathered}
\tag{315.1}
$$
其中 $A_c$ 表示 $y^2=x^3+c$。原分支还具有整 $j$、
$K=\mathbb Q(\sqrt{-3})$、$\sigma=1$ 和共同的二除域、
三除法 $S_3$ 商域；本篇从已经证明的 (315.1) 出发。
表示素数处有
$$
v_p(d)=m=
\begin{cases}
1,&p\equiv5\pmod9,\\
2,&p\equiv2\pmod9,
\end{cases}
\qquad
v_p(b)=k\ge1,\qquad v_p(r)=m+3k.
\tag{315.2}
$$
特别 $p\equiv2\pmod3$，且 $3\nmid v_p(r)>0$。

对任意两条椭圆曲线的模 $p$ 同构 $f:E[p]\to E'[p]$，
定义唯一乘子 $\mu(f)\in\mathbb F_p^\times$：
$$
e_{p,E'}(fP,fQ)=e_{p,E}(P,Q)^{\mu(f)}.
\tag{315.3}
$$
称其**平方辛型**，若 $\mu(f)\in\mathbb F_p^{\times2}$。
这意味着可对 $f$ 再乘一个 $\mathbb F_p^\times$ 标量，使其严格保持配对；
不意味着原来给定的 $\mu(f)$ 必等于一。
乘子在复合下相乘。保原点的椭圆曲线同构乘子为一，
次数三同源在 $p>3$ 挠点上的乘子为三，标量 $[c]$ 的乘子为 $c^2$。

固定
$$
\mu=\mu(\phi)\in\mathbb F_p^\times.
\tag{315.4}
$$
将 $\phi$ 限制到任何分解群仍是这个 $\mu$。
若一个局部表示的全部等变自同构都是标量，
其任意两个局部同构相差标量，因而辛型相同。
下文在每个需要这一结论的地方分别核准中心化子。

## 2. 表示素数处的有限平坦辛型引理

**引理 315.1。** 设 $p>7$、$p\equiv2\pmod3$，
$a\in\mathbb Z_p$，$r=1-a^3\ne0$，
$v_p(r)>0$ 且 $3\nmid v_p(r)$。令
$$
H:y^2=x^3+3arx-r(2a^3-1),\qquad
D=A_{-r}:y^2=x^3-r.
\tag{315.5}
$$
若存在 $G_{\mathbb Q_p}$ 等变同构 $H[p]\simeq D[p]$，
则**每个**这样的同构都具有平方辛型。

**证明。** 取 $u^6=r$，令
$L=\mathbb Q_p(\mu_6,u)$。这是 Galois 扩张，
由于 $\mu_6$ 的扩张不分歧且六与 $p$ 互素，其绝对分歧指数是
$$
e=\frac6{\gcd(6,v_p(r))}\in\{3,6\}<p-1.
\tag{315.6}
$$
对两条曲线都作 $x=u^2X,\ y=u^3Y$，得到好模型
$$
\begin{aligned}
H'&:Y^2=X^3+3au^2X-(1-2r),\\
D'&:Y^2=X^3-1.
\end{aligned}
\tag{315.7}
$$
两个特殊纤维字面上都是
$$
E_0/\mathbb F_p:\quad Y^2=X^3-1.
\tag{315.8}
$$
其判别式 $-432$ 是单位。它因 $p\equiv2\pmod3$ 而超奇异。

对每个 $g\in G_{\mathbb Q_p}$，两个模型的下降都由同一个 $u$ 给出：
底域的 $g$ 作用复合某个相同的 $\mu_6$ 坐标缩放。
惯性缩放像的阶为 $e$，因而包含非平凡 $\mu_3$。

Raynaud 的 Corollaire 3.3.6(1) 在 $e<p-1$ 下的完全忠实性，
把给定同构和其逆唯一延拓到 $\mathcal O_L$ 上的有限平坦 $p$ 群。
唯一性保留全部下降关系。约化并转到
$\overline{\mathbb F}_p$ 后，得到群概形自同构
$$
f:E_0[p]\longrightarrow E_0[p]
\tag{315.9}
$$
与上述惯性及整个半线性下降作用交换。

现在在群概形层面求这一中心化子。写 $G=E_0[p]_{\overline{\mathbb F}_p}$。
超奇异椭圆曲线的协变 Dieudonné 模给
$$
\operatorname{End}(G)\simeq
\left\{
\begin{pmatrix}t^p&s\\0&t\end{pmatrix}:
t\in\mathbb F_{p^2},\ s\in\overline{\mathbb F}_p
\right\}.
\tag{315.10}
$$
这一明确式见 Byszewski–Cornelissen (2018), Example 6.6，
印刷第 2213 页。也可在基 $e_1,e_2$ 中取
$Fe_2=e_1,\ Fe_1=0,\ Ve_2=-e_1,\ Ve_1=0$，
由 $F$ 的 $p$ 半线性和 $V$ 的 $p^{-1}$ 半线性直接求得：
可交换矩阵必须上三角，其对角元为 $t^p,t$，
同时 $t^{p^2}=t$，而上方非对角元任意。

令 $z$ 为实际 $\mu_3$ 自同构的一个生成元。
它满足 $z^2+z+1=0$。这个多项式在 $\mathbb F_p$ 不可约，
因此 $\mathbb F_p[z]\simeq\mathbb F_{p^2}$。
在 (315.10) 中，$z$ 的两个对角特征分别为
$\zeta_3,\zeta_3^p$，它们不同。用 (315.10) 中的上三角幺幂
自同构可消去 $z$ 的非对角元；此后与 $z$ 交换迫非对角元 $s=0$。
所以得到内在等式
$$
\operatorname{End}(G)^{\mu_3}
=\mathbb F_p[z]\simeq\mathbb F_{p^2}.
\tag{315.11}
$$

取算术 Frobenius 的完整下降同构 $\Phi$。
这里 $\Phi$ 是可逆的、底域系数经 $x\mapsto x^p$ 的半线性同构；
它既不是 Dieudonné 模上的幂零算子 $F$，
也不是椭圆曲线的纯不可分 Frobenius 态射。
实际 $\mu_3$ 坐标自同构经底域 Frobenius 变为其 $p$ 次幂。
来自 $u$ 的额外 $\mu_6$ 缩放属于 (315.11) 的交换子环，
不会改变其共轭作用。因此
$$
\Phi z\Phi^{-1}=z^p,\qquad
\Phi t\Phi^{-1}=t^p\quad(t\in\mathbb F_p[z]).
\tag{315.12}
$$
与全部下降交换的 $f$ 必在 (315.11) 的 Frobenius 固定环中，即
$$
f=[c],\qquad c\in\mathbb F_p^\times.
\tag{315.13}
$$
这一论证不要求同时选择一个在 $\mathbb F_p$ 定义、
又把 $\mu_3$ 对角化的基。

原同构的 Weil 乘子记为 $\nu$。
两侧的好模型有取值于 $\mu_p$ 的完美有限平坦 Weil 配对。
泛纤维上的配对恒等式由平坦性和分离性延拓，并可约化。
由 (315.13)，约化后乘子为 $c^2$。
完美性说明 $[\nu-c^2]$ 在 $G$ 上为零，故 $\nu=c^2$ 于 $\mathbb F_p$。
这里不能改用几何 $p$ 挠点的集合：超奇异情形该集合没有足够点，
但群概形配对仍完美，能准确区分所有模 $p$ 标量。
引理得证。$\square$

## 3. 两个 CM 参考之间的辛型，以及全局乘子

标准三同源
$$
\iota_c:A_c\longrightarrow A_{-27c},\qquad
(x,y)\longmapsto
\left(
\frac{x^3+4c}{x^2},
\frac{y(x^3-8c)}{x^3}
\right)
\tag{315.14}
$$
的核为 $\{O,(0,\sqrt c),(0,-\sqrt c)\}$。
它对 $p>3$ 的挠点是同构，Weil 乘子为三。
原点处按延拓解释这个有理公式。

若 $p\equiv5\pmod {12}$，则 $-1$ 在 $\mathbb Q_p$ 中为平方，
所以 $A_r$ 与 $A_{-r}$ 直接同构，乘子为一。
若 $p\equiv11\pmod {12}$，则三在 $\mathbb Q_p$ 中为平方；
取 $c_0^2=3$，$c_0^6=27$，复合
$$
A_r\xrightarrow{\ \iota_r\ }A_{-27r}
\xrightarrow{\ (x,y)\mapsto(x/c_0^2,y/c_0^3)\ }A_{-r}
\tag{315.15}
$$
得到乘子三。同时 $(3/p)=+1$，故这个乘子也是平方。
这里使用的是 $\sqrt3$；不能改成在这些 $p$ 中不存在的 $\sqrt{-3}$。

**定理 315.2。** 在全部实际范围 (315.1)–(315.2) 中，
$$
\boxed{\mu(\phi)\in\mathbb F_p^{\times2}.}
\tag{315.16}
$$

**证明。** 若 $\varepsilon=1$，$B_a=A_{-r}$，
把给定 $\phi$ 限制到 $G_{\mathbb Q_p}$，直接应用引理 315.1。
若 $\varepsilon=-1$，$B_a=A_r$，
将 $\phi$ 复合上述平方辛型的 $A_r[p]\to A_{-r}[p]$ 再应用引理；
复合乘子与第二个乘子都为平方，故原来同一个 $\mu(\phi)$ 为平方。
$\square$

## 4. 偶分支的独立二进辛型锚

下面不借助第 2 节的特征 $p$ 群概形计算，
在 $4\mid a$ 分支独立证明 (315.16)。
它同时核实：二处的有限分歧不允许任意改变全局辛型。

设 $s=v_2(a)\ge2$。此时
$$
r=1-a^3,\qquad
3ar\in 2^s\mathbb Z_2^\times,\qquad
-r(2a^3-1)=1-3a^3+2a^6.
\tag{315.17}
$$
取 $t^3=2$，$L_2=\mathbb Q_2(\zeta_3,t)$，
其分歧指数为三。对 $H_a$ 与 $A_r$ 都使用
$x=t^2X,\ y=2Y+1$，得到
$$
\begin{aligned}
H_a':\quad
Y^2+Y&=X^3+\frac{3ar\,t^2}{4}X
                 +\frac{-3a^3+2a^6}{4},\\
A_r':\quad
Y^2+Y&=X^3-\frac{a^3}{4}.
\end{aligned}
\tag{315.18}
$$
以 $v_{L_2}(2)=3$ 归一化，第一式的 $X$ 系数赋值
$3s+2-6\ge2$，两个常数的赋值均至少十二。
所以两侧都有好约化，且特殊纤维字面相同：
$$
E_2/\mathbb F_2:\quad Y^2+Y=X^3.
\tag{315.19}
$$
全部 Galois 下降也相同：三阶惯性只在 $X$ 上作相同
$\mu_3$ 缩放，$Y$ 不变；底域 Frobenius 和其缩放因子亦相同。

由于 $p$ 为奇数，好模型的 $p$ 挠点是有限 étale 群概形。
Hensel 底环上的有限 étale 特殊化等价，
把特殊纤维的恒等映射唯一提升为两侧 $p$ 挠点的同构；
唯一性保留全部 $G_{\mathbb Q_2}$ 下降。
Weil 配对也在此有限 étale 比较下保留，
所以存在一个乘子为一的
$H_a[p]\to A_r[p]$ 的 $G_{\mathbb Q_2}$ 同构。

现求全部局部自同构。三阶惯性满足
$X^2+X+1$，因 $p\equiv2\pmod3$ 在 $\mathbb F_p$ 不可约，
其线性中心化子是 $\mathbb F_{p^2}$。
算术 Frobenius 二在实际 $\mu_3$ 上作用为平方、即取逆，
故在这个二次域上作用为非平凡自同构。
与惯性及 Frobenius 同时交换的可逆元因此只有
$\mathbb F_p^\times$。
每个局部同构与已经构造的乘子一同构相差标量，
所以每一个的乘子都是平方。特别原来全局 $\phi$ 的限制如此。

## 5. 其他惰性坏素数处的全部局部辛型

**引理 315.3。** 设 $q\ne p$，$q\ge5$，
$q\equiv2\pmod3$，$q\mid d$，其余参数如 (315.1)。
则存在 $G_{\mathbb Q_q}$ 同构
$H_a[p]\to A_{-r}[p]$，且每个这样的同构都有平方辛型。
对 $A_r$ 参考，全部局部同构的乘子平方类则为
$$
\begin{array}{c|c}
q\bmod12&\mu\bigl(H_a[p]\to A_r[p]\bigr)
\ \text{所在的平方类}\\ \hline
5&\mathbb F_p^{\times2}\\
11&3\mathbb F_p^{\times2}.
\end{array}
\tag{315.20}
$$

**证明。** 由于 $d$ 立方自由且 $q\mid d$，
$$
n_q=v_q(r)=v_q(d)+3v_q(b)>0,\qquad 3\nmid n_q.
\tag{315.21}
$$
取 $u_q^6=r$、$L_q=\mathbb Q_q(\mu_6,u_q)$，
其分歧指数为三或六。与 (315.7) 同一个坐标变换，
把 $H_a$ 与 $A_{-r}$ 变成有字面相同特殊纤维
$Y^2=X^3-1$ 的好模型；它们有相同的全部下降。
现在 $q\ne p$，有限 étale 特殊化直接给一个保持 Weil 配对的
$G_{\mathbb Q_q}$ 模 $p$ 同构。

惯性中非平凡 $\mu_3$ 在 $p$ 挠点上不可约，
其中心化子为 $\mathbb F_{p^2}$；
因 $q\equiv2\pmod3$，Frobenius $q$ 使 $\mu_3$ 取逆，
迫整个分解群的中心化子为 $\mathbb F_p$。
所以所有局部同构的辛型都与上述配对保持同构相同。

若 $q\equiv5\pmod {12}$，$-1$ 在 $\mathbb Q_q$ 是平方，
故 $A_{-r}\simeq A_r$，乘子一。
若 $q\equiv11\pmod {12}$，三在 $\mathbb Q_q$ 是平方，
复合
$$
A_{-r}\xrightarrow{\ \iota_{-r}\ }A_{27r}
\xrightarrow{\text{以 }\sqrt3\text{ 缩放}}A_r
\tag{315.22}
$$
得到乘子三。
$A_r[p]$ 的分解群中心化子同样是标量，
所以这分别给全部同构的平方类，而不只是某个可选同构的平方类。
$\square$

## 6. 实际坏支撑的排除

**定理 315.4。** 若实际分支满足 $4\mid a$，
则每个 $q\ne p$、$q\equiv11\pmod {12}$、$q\mid d$ 都迫
$$
\left(\frac3p\right)=1.
\tag{315.23}
$$
因而
$$
\boxed{
4\mid a,\quad p\equiv5\pmod {12}
\quad\Longrightarrow\quad
q\nmid d\ \text{对所有素数 }q\equiv11\pmod {12}.
}
\tag{315.24}
$$
等价地，对这些 $q$，
$$
v_q(1-a^3)\equiv0\pmod3.
\tag{315.25}
$$
若偶分支的 $d$ 确实有一个 $q\equiv11\pmod {12}$ 素因子，
则必须
$$
p\equiv11\pmod {12},\qquad
p\equiv11\text{ 或 }23\pmod {36}.
\tag{315.26}
$$

**证明。** 偶分支 $B_a=A_r$。
由定理 315.2，或者第 4 节的独立二处证明，
同一个实际全局同构 $\phi$ 的乘子 $\mu$ 为平方。
另一方面，把这个 $\phi$ 限制到 $G_{\mathbb Q_q}$，
引理 315.3 说明它属于 $3\mathbb F_p^{\times2}$。
所以三必须为模 $p$ 平方。
对 $p\equiv2\pmod3$ 的奇素数，二次互反律给
$$
\left(\frac3p\right)=
\begin{cases}
-1,&p\equiv5\pmod {12},\\
+1,&p\equiv11\pmod {12}.
\end{cases}
\tag{315.27}
$$
这证明 (315.23)–(315.24)。
在 (315.24) 的情形 $q\ne p$ 自动成立，故量词可以覆盖所有
$q\equiv11\pmod {12}$。
由 $r=db^3$ 和 $d$ 立方自由，(315.24) 与 (315.25) 等价。
最后把 $p\equiv11\pmod {12}$ 与 $p\equiv2,5\pmod9$ 合并，
得到 (315.26)。$\square$

## 7. 准确范围与剩余缺口

以上限制确实使用同一个实际全局 $\phi$。
第 5 节的等变同构虽是局部构造的，但中心化子计算保证所有局部
同构辛型相同，所以可以用它限制给定的全局乘子。
没有把“某处存在一个辛同构”当成“全局给定同构必须辛”。

本结论有下列明确边界。

- 奇分支 $a\equiv1\pmod {16}$ 的指定参考为 $A_{-r}$。
  第 5 节在全部这些惰性坏素数处都给平方辛型，与 $p$ 处一致；
  因而没有同样的支撑排除。
- 条件 $q\mid d$ 保证非平凡三阶惯性。如果只有 $q\mid b$、
  $q\nmid d$，不能沿用上述中心化子证明。
- 对 $q\equiv1\pmod3$，Frobenius 不反转 $\mu_3$；
  中心化子可包含整个 Cartan，其范数给任意
  $\mathbb F_p^\times$ 行列式，所以局部辛型可能可变。
  本篇没有对这些分裂素数作相同结论。
- (315.24) 排除一种实际支撑，但没有给剩余素数的大小、数量或导子上界。
  它也没有证明偶分支剩余参数不存在，更未消除所有其他原始分支。
  R312 的局部匹配和非零严格 CM Selmer 构造与本篇不矛盾：
  那些构造的 $H_a[p]$ 有完整 $\mathrm{GL}_2$ 像，并无这里给定的
  全局 CM 同构。

## 8. 依赖和已核主来源

1. **R289、R301、R306**：实际整三次正规形、指定的
   $H_a[p]\simeq B_a[p]$、两个二进分支和 (315.2)。
   本篇不改变 CM 扭曲符号。
2. M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*,
   Bulletin de la Société Mathématique de France **102** (1974), 241–280，
   Corollaire 3.3.6(1)，印刷第 268 页：
   $e<p-1$ 下的有限平坦 $p$ 群完全忠实性。
   [原刊 PDF](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。
3. J. Byszewski and G. Cornelissen,
   *Dynamics on abelian varieties in positive characteristic*,
   Algebra & Number Theory **12**(9) (2018), 2185–2235，
   Example 6.6，印刷第 2213 页：
   超奇异椭圆曲线 $p$ 挠群概形端环的明确矩阵式。
   [原刊 PDF](https://msp.org/ant/2018/12-9/ant-v12-n9-p06-s.pdf)，
   DOI 10.2140/ant.2018.12.2185。
   本篇从该端环自行求实际 $\mu_3$ 中心化子、完整 Frobenius 下降
   和 Weil 乘子，没有把 Dieudonné $F$ 当成下降 Frobenius。

这是纯证明条目，没有依赖数值扫描、脚本输出或未认证的类群计算。
