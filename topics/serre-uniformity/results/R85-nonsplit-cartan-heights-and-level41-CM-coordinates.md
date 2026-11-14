# R85. 直接非分裂 Cartan 高度、层 41 的真实极化作用和全部 CM 平移坐标平方

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明并独立复核；有限层计算附完整有理数证书，GP 从头复算与所存 JSON 完全相同。** 本文把 Cai–Shu–Tian 的已发表 Gross–Zagier 公式直接用在 $X_{\rm ns}(41)$，再经次数二商映射接到真正的 $X=X_{\rm ns}^+(41)$。在 R79 的 Mordell–Weil 基 $B_{-4,f}$ 下，记
$$
U_{-7,f}=r_{7,f}B_{-4,f},\qquad
U_{-3,f}=r_{3,f}B_{-4,f}.
$$
这里 $U_\delta=[20P_\delta-D]$ 来自 $X$ 上真正的有理 CM 点，$D$ 是全部尖点之和。若 $v_\delta$ 表示 R74 同一规范的二次扭曲模符号行，$\kappa=qq^\dagger$ 是 R71 的实际项链同源的极化倍率，则
$$
\boxed{
r_{7,f}^{2}=\frac{200}{\kappa_f}\frac{v_{-7,f}}{v_{-4,f}},
\qquad
r_{3,f}^{2}=\frac{1800}{\kappa_f}\frac{v_{-3,f}}{v_{-4,f}}.
}\tag{0.1}
$$
分母中的 $\kappa_f$ 由实际项链对应的 $400$ 条路径求得；分子中的 $200,1800$ 先从曲线次数和高度公式严格推出。平方检验只检查最终结果，不替代尺度证明。

全部八个系数域中的 $r_{7,f},r_{3,f}$ 均非零，各自算到一个整体正负号。结合 R79 对 $B_{-8,f}=s_fB_{-4,f}$ 的计算，得到一个额外的无条件结论：
$$
\boxed{\eta_{D,54T_2+8\mathrm{id}}\text{ 在全部八个简单因子上的投影均非零。}}
\tag{0.2}
$$
等价地，其全部 $54$ 个共轭特征坐标都非零，且它生成 $J(\mathbb Q)\otimes\mathbb Q$ 这个秩一 Hecke 模。本文不把规范平移的非零误当成完整 QC 函数在 CM 点的导数非零。

## 1. 固定对象和高度规范

一般的几何规范先取 $p\equiv1\pmod8$，令
$$
C=X_{\rm ns}(p),\quad X=X_{\rm ns}^+(p),\quad
\pi:C\longrightarrow X,\quad d=(p-1)/2.
$$
$C$ 保留项链定向，$\pi$ 忘掉定向，故 $\deg\pi=2$。$J=\operatorname{Jac}(X)$。令 $f$ 为一个实际出现在 $J$ 中的权二、层 $p^2$ 的 new、Fricke $+$ 特征形式，$E_f$ 为其 Hecke 系数域，$e_f$ 为相应有理投影。使用 Jacobian 的规范主极化及 Rosati 伴随；这些 Hecke 投影自伴随。

为使所有同态的尺度清楚，可在极化的有理同源范畴中把 $J_f=(J,e_f)$ 视为一个直接因子，极化取 $J$ 的限制。若要使用实际阿贝尔簇模型，选一个与此因子同源的简单阿贝尔簇并传输极化即可：下文的高度分子与同态配对分母同时按同一个极化因子变化，因此比值不变。Cai–Shu–Tian 的公式本身使用 $\operatorname{Hom}\otimes\mathbb Q$，允许这里的有理投影。

对点用 $E_f$ 值 Néron–Tate 配对 $\langle\ ,\ \rangle_{K,f}$；其到 $\mathbb R$ 的迹是通常的配对。因为 $E_f$ 在 Rosati 下固定，
$$
\langle aP,bQ\rangle_{K,f}=ab\langle P,Q\rangle_{K,f}
\qquad(a,b\in E_f).
\tag{1.1}
$$
这正是 Cai–Shu–Tian §1B pp.2531–2532 的系数域值配对，而不是将不同嵌入上的标量高度混在一起。

所有点等式在 $J(\mathbb Q)\otimes\mathbb Q$ 中解释，除非另行声明为实际整点等式。R57 所核查的层 $41$ 输入给 $A=J$、秩 $54$；R79 已证明每个 $B_{-4,f}$ 非零，故 $J_f(\mathbb Q)\otimes\mathbb Q$ 是由它生成的一维 $E_f$ 空间。

## 2. 真正的非分裂 Cartan 层是 CST 的 admissible order

取 $\delta=-3$ 或 $-7$，并假定 $p$ 在 $K=\mathbb Q(\sqrt\delta)$ 中惰性。令 $\chi=1$，环类导子 $c=1$，自守导子 $N=p^2$。这两个整数不是同一个概念；$p^2$ 的层不使 CM 整环的导子变成 $p$。

### 引理 2.1：有限局部四元数和实际整环

在所有有限处，Cai–Shu–Tian Theorem 1.5 所需的四元数代数分裂。在 $p$ 处，一个实际 admissible order 是
$$
R_p=\mathcal O_{K,p}+pM_2(\mathbb Z_p)
\subset M_2(\mathbb Q_p),
\tag{2.1}
$$
其中选定非分裂 Cartan 所给的 $\mathcal O_{K,p}\subset M_2(\mathbb Z_p)$。它的约化判别式为 $p^2$，且
$$R_p\cap K_p=\mathcal O_{K,p}.$$
在其余有限处取与 $\mathcal O_K$ 相容的极大整环。相应的 $R^\times$ 层 Shimura 曲线就是 $C=X_{\rm ns}(p)$。

**证明。** 在 $p$ 处，CST Lemma 3.1(4)，期刊 p.2555，断言对惰性二次扩张和不分歧 $\chi$，相应四元数代数分裂恰当且仅当自守导子指数为偶数。这里指数是 $2$。在 $v\ne p$，自守表示不分歧，属于 principal series；Lemma 3.1(1) 同样给有限四元数分裂。无穷处的权二离散系列及平凡环类字符给定四元数，故去掉唯一无穷处后得到的 nearby coherent algebra 是 $M_2(\mathbb Q)$。

CST Lemma 3.4，p.2558，说明当局部 $K$ 非分裂、$n>0,c=0$ 时，admissible order 唯一，并具体为
$$\mathcal O_K+I\mathcal O_B,\qquad
n=\delta(B)+\operatorname{length}_{\mathcal O}(\mathcal O_K/I).$$
此处 $B$ 分裂、$n=2$、$K_p/\mathbb Q_p$ 不分歧，所以取 $I=p\mathcal O_{K,p}$ 即得 (2.1)。也可直接检查：$R_p$ 在 $M_2(\mathbb Z_p)$ 中的加法指数为 $p^2$，故约化判别式为 $p^2$；与 $K_p$ 的交显然是极大整环。

$R_p^\times$ 是 $\mathrm{GL}_2(\mathbb Z_p)$ 中模 $p$ 落在 $\mathbb F_{p^2}^\times$ 的元素，正是非分裂 Cartan 的逆像。其行列式像为全部 $\mathbb Z_p^\times$；因此得到通常定义于 $\mathbb Q$、几何连通的 $X_{\rm ns}(p)$。这里尚未取正规化子商。证毕。

CST 的 $\Sigma_1$ 在此为 $\{p\}$，而 $c_1=1$。由于 $\gcd(N,\delta c)=1$，Theorem 1.5 中的 $\Sigma$ 与 $\Sigma_D$ 均为空。因此公式不删除任何有限 Euler 因子，也不产生 $2^{-\#\Sigma_D}$ 的额外倍数。局部 admissible 条件中处理 $c_1$ 与 $N$ 同时有素因子的分支，在此不出现。

### 引理 2.2：实际映射处于 toric test line

由 $J_f$ 因子给出的非零映射 $C\to J_f$，只要经 $X$ 分解且以 Hodge 类为基点，就是 CST Theorem 1.5 的非零 test vector。

**证明。** 远离 $p$，该映射的自守分量为极大紧子群不变的新向量。在 $p$，它已经对 $R_p^\times$ 不变，特别对 $\mathcal O_{K,p}^\times$ 不变。由于 $K_p/\mathbb Q_p$ 不分歧，
$$K_p^\times=p^{\mathbb Z}\mathcal O_{K,p}^\times.$$
中心作用平凡，所以它对全部 $K_p^\times$ 不变。CST Definition 3.6 和 Proposition 3.7，p.2560，在非分裂且 $c<n$ 的情形，恰把 test line 定义为这个 $\chi^{-1}$ 特征空间，并证明其一维和每个非零向量的 toric period 非零。Proposition 3.8 同时给该线与 $R_p^\times$ 不变量的关系。

我们使用的是已存在的非零 $J_f$ 映射，故不需要以抽象维数相等代替向量非零，也没有把 $X_0(p^2)$ 的普通 new vector 在惰性处直接冒充这个 Cartan test vector。证毕。

## 3. Hodge 基点、商次数二和精确高度公式

记 $D_C$ 为 $C$ 的全部尖点之和。两条曲线的所有尖点宽度均为 $p$，$\deg D_C=2d$，且
$$\pi_*D_C=2D.$$
权十二判别式的除子等式，或 $j$ 的 Riemann–Hurwitz 公式，给
$$
\xi_C=\frac{D_C}{2d},\qquad \xi_X=\frac Dd
\quad\text{in }\operatorname{Pic}\otimes\mathbb Q,
\qquad \pi_*\xi_C=\xi_X.
\tag{3.1}
$$
这里 $\xi$ 是 CST 定义的规范化 Hodge 类。具体地，R79 (4.1) 给
$$K_X+D+\tfrac12E_2+\tfrac23E_3\sim \tfrac p6D,$$
其归一化就是 $D/d$；同样的 orbifold 典范类关系适用于 $C$。因此椭圆点的稳定子没有留下一个额外的基点平移。

定义
$$u_D(x)=[dx-D],\qquad
f_C=e_f u_D\circ\pi:C\longrightarrow J_f.
\tag{3.2}
$$
由 (3.1)，$f_C(\xi_C)=0$。它对应的 Jacobian 同态为
$$d\,e_f\pi_*:J_C\longrightarrow J_f.$$
在双方的规范极化下，$\pi_*^\dagger=\pi^*$ 且 $\pi_*\pi^*=[2]$，所以
$$
\boxed{f_Cf_C^\dagger=2d^2\operatorname{id}_{J_f}.}
\tag{3.3}
$$

CST 在 pp.2529–2530 先定义配对为曲线体积的倒数乘同态复合，再把 $U$-level pairing 定义为乘回同一体积。因此其 Theorem 1.5 的分母对 (3.2) **正是 $2d^2$**。不用另乘 $X_{\rm ns}$ 与 $X_0(p^2)$ 的群指数或体积比。

两个域 $K_{-3},K_{-7}$ 均类数一。完整 CM 整环在 $E[p]$ 上给非分裂 Cartan，因而给
$$Q_\delta\in C(K_\delta),\qquad
\pi(Q_\delta)=P_\delta\in X(\mathbb Q).$$
这是极大整环导子一的 Heegner 点。CST 的类群和只有一个项，故
$$P_1'(f_C)=f_C(Q_\delta)=U_{\delta,f}.$$
单位数 $u_{-3}=3,u_{-7}=1$ 出现在公式的 $u^2$ 中；不再除一次点本身。

### 命题 3.1：直接 Cartan 高度公式

对每个 $\sigma:E_f\hookrightarrow\mathbb R$，有
$$
L'(f^\sigma/K_\delta,1)
=\frac{8\pi^2(f^\sigma,f^\sigma)}{u_\delta^2\sqrt{|\delta|}}
\frac{\langle U_{\delta,f},U_{\delta,f}\rangle_{K_\delta,f}^{\sigma}}{2d^2}.
\tag{3.4}
$$

**证明。** 应用 CST Theorem 1.5，pp.2532–2533。引理 2.1 验证其局部根号、admissible order、导子及 Euler 因子条件；引理 2.2 验证所用的非零 test vector；(3.1)–(3.3) 验证实际基点和同态配对。取第二个向量为由极化对偶得到的向量，则 Heegner 点配对成为 (3.4) 的自配对。以上同时适用于非有理 Hecke 系数域。证毕。

## 4. 与真实 $q$ 的分裂 CM 点比较

R79 的 $B_{-4}=q[\widetilde P_{-4}-\infty]$ 是从 $X_0(p^2)$ 上的水平 CM 点得到。R71 的实际同源满足
$$qq^\dagger=\kappa,\qquad q^\dagger q=\kappa e_0.$$
在同一目标因子 $J_f$ 中使用同一极化，$X_0(p^2)\to J_f$ 映射的 $U_0(p^2)$-pairing 因而为 $\kappa_f$。CST Theorem 1.1 及 Theorem 1.5 在 p.2534 的普通模曲线例子给
$$
L'(f^\sigma/K_{-4},1)
=\frac{8\pi^2(f^\sigma,f^\sigma)}{u_{-4}^{2}\sqrt4}
\frac{\langle B_{-4,f},B_{-4,f}\rangle_{K_{-4},f}^{\sigma}}
{\sigma(\kappa_f)},\qquad u_{-4}=2.
\tag{4.1}
$$
这里源的归一化 Hodge 类与 $\infty$ 相同于 $\operatorname{Pic}\otimes\mathbb Q$；可由 Manin–Drinfeld 的尖点挠性，或 R75 的 $T_2-3$ 同源论证得到。

现在专取 $p=41$。R57 的 DLF 输入使各 $L'(f^\sigma,1)$ 非零，而 $L(f^\sigma,1)=0$。故
$$
L'(f^\sigma/K_\delta,1)
=L'(f^\sigma,1)L(f^\sigma\otimes\chi_\delta,1).
\tag{4.2}
$$
第 5 节将证明 $\delta=-3,-7$ 的全部扭曲值非零；(3.4) 遂证明全部 $U_{\delta,f}$ 非零。由秩一，存在唯一 $r_{\delta,f}\in E_f^\times$ 使
$$U_{\delta,f}=r_{\delta,f}B_{-4,f}.$$

对 (3.4)、(4.1) 作比值。所有点已在 $J(\mathbb Q)\otimes\mathbb Q$ 中，所以两个二次域的高度同为从 $\mathbb Q$ 基变换而来的高度；若采用不除扩张度的规范，双方都恰乘二，仍然取消。得
$$
r_{\delta,f}^{2}
=\frac{d^2u_\delta^2\sqrt{|\delta|}}{4\kappa_f}
\frac{L(f\otimes\chi_\delta,1)}{L(f\otimes\chi_{-4},1)}.
\tag{4.3}
$$

R74 的固定定向是
$$v_\delta(\Phi_f^-)=-\tau_\delta L(f\otimes\chi_\delta,1),
\qquad\tau_\delta=i\sqrt{|\delta|}.$$
于是
$$
\frac{v_{\delta,f}}{v_{-4,f}}
=\frac{\sqrt{|\delta|}}2
\frac{L(f\otimes\chi_\delta,1)}{L(f\otimes\chi_{-4},1)}.
$$
代入 (4.3)，严格得到
$$
\boxed{r_{\delta,f}^{2}
=\frac{d^2u_\delta^2}{2\kappa_f}\frac{v_{\delta,f}}{v_{-4,f}}.}
\tag{4.4}
$$
因为 $d=20$，(4.4) 就是 (0.1)。这里所有对数微分的切映射因子都取消：比较的是同一个目标因子内的点比例。不能因此在 R68 的独立微分基高度系数中删掉其切映射因子。

## 5. 两条真正惰性 CM 模符号行的非消失

使用 R74、R79 的同一个空间：
$$
M=S_2^{\rm symbols}(\Gamma_0(1681))^{\mathrm{star}=-1},\qquad
V=M^{\rm new,\,Fricke=+},\qquad\dim V=54.
$$
由 `msinit(1681,2,-1)`、`msnew`、`msatkinlehner` 直接构造其有理基 $P$。置
$$H=T_2+2T_3,\qquad
v_\delta=\sum_{a=1}^{|\delta|-1}\chi_\delta(a)
\operatorname{mseval}(M,P,[a/|\delta|,\infty]).
\tag{5.1}
$$
$H$ 的特征多项式平方自由，其八个不可约因子次数为
$$2,3,3,4,4,8,12,18.$$
这里的八个因子及全部 $6H$ 整数矩阵已由 R79 证书保存。

对行 $v$ 记 $K(v,H)$ 的第 $j+1$ 行为 $vH^j$，$0\le j<54$。精确计算得到
$$
\det K(v_{-3},H)\equiv92\pmod{1009},\qquad
\det K(v_{-7},H)\equiv483\pmod{1009}.
\tag{5.2}
$$
分母只含 $2,3$，故可在模 $1009$ 下计算。两个非零行列式证明两行在全部 $54$ 条复特征线上都非零：若某条特征线被 $v$ 消去，则所有 $vH^j$ 同样消去它，与满秩矛盾。结合 (5.1) 的精确 Gauss 和公式，得到第 4 节所需的全部扭曲中心值非零。

因此 $U_{-3}$、$U_{-7}$ 各自也是 $J(\mathbb Q)\otimes\mathbb Q$ 的循环 Hecke 生成元。R47 的对数同构及 R77 的非退化 $47$ 进高度也分别适用于这两个真实点。

## 6. 不靠类型猜测：在实际模符号上求 $\kappa$

### 6.1 项链对应给出的准确路径算子

令 $Y=X_{\rm sp}^+(41)$，固定无序对子 $s_0=\{\infty,0\}$。RW Lemma 8 给：一个对子属于 $20$ 个项链；一个不同对子 $\{a,b\}$ 与 $s_0$ 同时互为对跖点，当且仅当交比 $b/a$ 为非平方，此时恰有一个项链。若两对子有共同点，则不可能同为对跖对子。因此实际对应 $\lambda\varphi$ 在此纤维上的作用是
$$
20\,s_0+
\sum_{\substack{a\in\mathbb F_{41}^\times\text{ 平方}\\
                   b\in\mathbb F_{41}^\times\text{ 非平方}}}\{a,b\}.
\tag{6.1}
$$
和式有 $20^2=400$ 项；每个无序对子恰出现一次。因为 $-1$ 是平方，“一平方、一非平方”恰与交比非平方等价。

R71 的 $q^\dagger q=r^\dagger\lambda\varphi r$ 在 Fricke $+$ 源上对应 $2\lambda\varphi$。因此 (6.1) 的系数分别成为 $40$ 和 $2$。

为每个 $(a,b)$ 选 $g_{a,b}\in\mathrm{SL}_2(\mathbb Z)$，其模 $41$ 将 $\infty,0$ 送到 $a,b$。对子标号是右陪集，故在模符号的反变拉回中使用 $g_{a,b}^{-1}$。设 $D_p=\operatorname{diag}(p,1)$；$\tau_{\rm sp}=p\tau_0$ 给 $X_0(p^2)\simeq X_{\rm sp}(p)$，所以源上的路径矩阵为
$$D_p^{-1}g_{a,b}^{-1}D_p.$$
若 $g_{a,b}=\left(\begin{smallmatrix}A&B\\C&D_0\end{smallmatrix}\right)$，同一个分式线性变换可写成整矩阵
$$
G_{a,b}=
\begin{pmatrix}pD_0&-B\\-p^2C&pA\end{pmatrix}.
\tag{6.2}
$$
换取同一右陪集的代表不改变下降到 $Y$ 的算子。实际对应关于互换两端对称，所以对偶作用也给同一个算子。

由 (5.1)，$v_{-4}=\operatorname{mseval}(M,P,[1/4,3/4])$。故只需 $400$ 次路径评价即可严格算出
$$
\boxed{
v_\kappa:=v_{-4}\kappa
=40v_{-4}+2\sum_{a,b}
\operatorname{mseval}(M,P,
[G_{a,b}(1/4),G_{a,b}(3/4)]).
}\tag{6.3}
$$
矩阵 (6.2) 的射影行列式为正，路径的方向与 R74 完全相同。

脚本为各 $(a,b)$ 构造整行列式一的提升并逐项检查。具体取 $C=(a-b)^{-1}\bmod p$、$A\equiv aC\bmod p$，给 $A$ 加 $p$ 的倍数直到 $\gcd(A,C)=1$；Bezout 求出 $AD_0-BC=1$ 后，以 $D_0\mapsto D_0+Ck$、$B\mapsto B+Ak$ 使 $D_0\equiv1\bmod p$。于是 $A/C\equiv a$、$B/D_0\equiv b$。没有从浮点特征值反推这些矩阵。

### 6.2 实际各 Hecke 因子的识别

$\kappa$ 与所有远离 $41$ 的 Hecke 算子交换，而 $v_{-4}$ 是循环行。因此 (6.3) 唯一确定 $\kappa$ 在 $V$ 上的全部作用。对 $H$ 的每个不可约因子 $f_H$，在实际核空间 $\ker f_H(H)$ 上求出唯一的
$$k_f(X)\in\mathbb Q[X],\qquad\deg k_f<\deg f_H,$$
满足
$$v_{-4}k_f(H)=v_\kappa.$$
等式在该核空间上解释。按 R79 的因子顺序，得到：

| 因子次数 | $\kappa_f$ 或 $\kappa_f/2$ 的最小多项式 | R71 的局部类型 |
|---:|---|---|
| $2$ | $\kappa_f=64$ | PS，字符阶 $4$ |
| $3$（$X^3+X^2-33X-85$） | $\kappa_f=32$ | $\mathrm{St}\otimes\chi_{41}$ |
| $3$（$X^3+X^2-30X+41$） | $\kappa_f=50$ | SC，字符阶 $6$ |
| $4$（$X^4-3X^3+4X-1$） | $\kappa_f=72$ | PS，字符阶 $10$ |
| $4$（$X^4+9X^3-108X-81$） | $F_2(\kappa_f/2)=0$ | PS，字符阶 $5$ |
| $8$ | $F_4(\kappa_f/2)=0$ | PS，字符阶 $20$ |
| $12$ | $F_3(\kappa_f/2)=0$ | SC，字符阶 $14$ |
| $18$ | $F_6(\kappa_f/2)=0$ | SC，字符阶 $42$ |

$F_2,F_3,F_4,F_6$ 是 R71 §5 的明确多项式。表内的关系均由实际 $k_f(h_f)$ 精确代入验证；它们用于与 R71 的有限群计算对照，不用于选择 $k_f$。例如第五个因子上直接算得
$$
\kappa_f=\frac{32}{27}h_f^3+\frac{64}{9}h_f^2-\frac{32}{3}h_f-8.
\tag{6.4}
$$
因此这里已经连接了真实全局 Hecke 因子和有限群类型，不能把它替换成按两个表的维数凑出的匹配。全部八个 $k_f$ 的有理系数保存在附带证书中。

## 7. 全部坐标平方和非零规范平移

利用 (0.1) 与第 6 节的实际 $\kappa_f$，脚本在每个域
$$E_f=\mathbb Q[h_f]=\mathbb Q[X]/(f_H)$$
中求出 $a_{3,f},a_{7,f}$，并严格验证
$$
\kappa_f a_{3,f}^{2}=1800\frac{v_{-3,f}}{v_{-4,f}},\qquad
\kappa_f a_{7,f}^{2}=200\frac{v_{-7,f}}{v_{-4,f}}.
\tag{7.1}
$$
两个根均非零。数学上的真实点比例满足
$$r_{3,f}\in\{a_{3,f},-a_{3,f}\},\qquad
r_{7,f}\in\{a_{7,f},-a_{7,f}\}.$$
这是每个数域一个符号；一个域的共轭嵌入不能独立选号。

例如次数二因子 $h^2-2h-31=0$ 上，
$$
\kappa_f=64,\qquad
r_{3,f}=\pm\frac{15}{4},\qquad
r_{7,f}=\pm\frac{5(h+1)}8,\qquad
s_f=\pm\frac{h+5}{4}.
\tag{7.2}
$$
取 $h=1+4\sqrt2$ 可把这些数全部写在 $\mathbb Q(\sqrt2)$ 中，但证书无需选择实嵌入。

### 定理 7.1：实际规范平移是循环 Hecke 生成元

令 $G=54T_2+8\mathrm{id}=2(27T_2+4\mathrm{id})$。则 $\eta_{D,G}$ 在每个 $J_f$ 中非零，因而生成 $J(\mathbb Q)\otimes\mathbb Q$ 作为有理 Hecke 模。

**证明。** R79 已在真实 Jacobian 中证明
$$
\eta_{D,G}=108U_{-7}+1080B_{-8}+80B_{-4}+\frac{16}{3}U_{-3}.
$$
故在基 $B_{-4,f}$ 下其坐标为
$$
\xi_{G,f}=108r_{7,f}+1080s_f+80+\frac{16}{3}r_{3,f}.
\tag{7.3}
$$
R79 的 $a_{8,f}$ 满足 $s_f\in\{a_{8,f},-a_{8,f}\}$。对三符号的全部八种选择，独立有理数检查器将
$$
80+108\epsilon_7a_{7,f}+1080\epsilon_8a_{8,f}
+\frac{16}{3}\epsilon_3a_{3,f},\qquad\epsilon_i\in\{\pm1\},
\tag{7.4}
$$
模 $f_H$ 约化，并逐项断言所得多项式非零。八个域的计数全部是 $8/8$。这些有限恒等式只用整数和分数，不用数值近似；完整输入和检查代码见第 8 节。

例如 (7.2) 的八个数写成
$$80\ \pm(135+270\sqrt2)\ \pm(1620+1080\sqrt2)\ \pm20,$$
其 $\sqrt2$ 系数不可能为零。其余七域以完全相同的多项式约化给严格非零证书。真实的三个符号虽未选择，必属于 (7.4)，故真实 $\xi_{G,f}$ 非零。每个 $J_f(\mathbb Q)\otimes\mathbb Q$ 为一维 $E_f$ 空间，最后一句随即成立。证毕。

还可直接给真实 $\xi_{G,f}$ 的一个八次代数约束。令
$$
A=(108a_{7,f})^2,\quad B=(1080a_{8,f})^2,\quad
C=(16a_{3,f}/3)^2,
$$
并写 $S=A+B+C$、$P=AB+AC+BC$、$R=ABC$。则 $t=\xi_{G,f}-80$ 满足
$$
t^8-4St^6+(6S^2-8P)t^4
-(4S^3-16SP+64R)t^2+(S^2-4P)^2=0.
\tag{7.5}
$$
证明是对 $t-(\pm108a_7\pm1080a_8\pm16a_3/3)$ 的八个因子作乘积；每个奇次根号项都取消。式 (7.5) 的系数都已精确求得，不需要确定实际点符号。

## 8. 有限证书及复算

文件如下，均为文本；不需要 Sage、Magma 或附加 Python 包。

- `scripts/p41_inert_cm_coordinates.gp`：PARI/GP 2.19.0，从层 $1681$ 的真实模符号空间重新构造基、$H$、扭曲行和 $400$ 条对应路径；求全部八域的 $\kappa_f,a_{3,f},a_{7,f}$。本次从零运行约八秒。
- `scripts/data/p41_inert_cm_certificate.json`：实际整数行 $v_{-3},v_{-7},v_\kappa$，所有 $k_f,a_{3,f},a_{7,f}$ 的有理系数，以及最小多项式关系。通过 SHA256 固定 R79 的实际 $6H$ 矩阵和 $a_{8,f}$，避免重复保存。
- `scripts/verify_p41_inert_cm_coordinates.py`：仅用 Python 标准库，在 $\mathbb Q$ 上独立核对全部对应及平方恒等式，并核对 (7.4) 的所有 $64$ 个非零结果。

证书的 SHA256 为

    9086c4436c06f033a9cb5825a5b69bec411bcce329b3233574b49875f16f5866

具体地，令 $Q_f(X)=\prod_{g\ne f}g(X)$ 为其余七个 Hecke 因子的乘积。Python 检查器在完整 $54$ 维有理矩阵上验证
$$
v_{-4}k_f(H)Q_f(H)=v_\kappa Q_f(H),
$$
$$
v_{-4}\frac{k_f(H)a_{3,f}(H)^2}{1800}Q_f(H)=v_{-3}Q_f(H),
$$
$$
v_{-4}\frac{k_f(H)a_{7,f}(H)^2}{200}Q_f(H)=v_{-7}Q_f(H).
\tag{8.1}
$$
这里先在 $\mathbb Q[X]/(f_H)$ 中约化再评价，等价性由 $f_H(H)Q_f(H)=0$ 保证。全部分母用整数倍清除，所以 (8.1) 不是只在模 $1009$ 下的检验。模 $1009$ 仅用于证明两条扭曲行的满秩。

## 9. 对 O5 的准确接口和继续方向

R79 的真实 $\xi_G$ 现在在每个系数域中被限制到显式的八个数，并证明它的实际投影非零；两个之前未知的真实有理 CM 点坐标也已求到符号。结合 R77，可在每个因子中使用非零的 $47$ 进高度系数和非零的平移坐标。

仍须为 R47 的完整函数保留同一规范的辅助局部高度，以及 R54 的有限坏高度靶值。全局二次项的线性系数非零，不保证减去辅助局部高度后的 CM 根导数非零；(7.5) 也没有选择实际 Mordell–Weil 符号。下一项实际算术计算是这些符号或混合高度、以及局部高度的可认证 jets。本文的有限层结论不改变本课题的全层完成标准。

## 原始来源与精确定位

1. Li Cai, Jie Shu and Ye Tian, **Explicit Gross–Zagier and Waldspurger formulae**, *Algebra & Number Theory* **8** (2014), 2523–2572，DOI [10.2140/ant.2014.8.2523](https://doi.org/10.2140/ant.2014.8.2523)，[期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)。§1B pp.2528–2532 给 Hodge 基点、同态配对、$U$-pairing 和系数域值高度；Theorem 1.5 pp.2532–2533 为实际使用的公式；p.2534 的例子连接普通 $X_0(N)$。Lemma 3.1(4) p.2555 给惰性处偶导子判据；Lemma 3.4 p.2558 给 $\mathcal O_K+I\mathcal O_B$；Definition 3.6、Propositions 3.7–3.8 p.2560 给实际 test line。该期刊 PDF 前有两页封面，PDF 页号比期刊起始页的相对序号多二。
2. Marusia Rebolledo and Christian Wuthrich, **A moduli interpretation for the non-split Cartan modular curve**, *Glasgow Mathematical Journal* **60** (2018), 411–434，DOI [10.1017/S0017089517000180](https://doi.org/10.1017/S0017089517000180)，[作者 2017-06-19 版本](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。§3.2 p.7 给尖点和宽度；Lemma 8 p.8 给交比及对跖项链计数；§4.1 pp.12–13 给 $\varphi,\lambda$；Lemma 22 p.18 给与真正曲线对应的规范化。实际 Rosati 倍率的完整连接已在 R71 证明。
3. [PARI/GP 官方模符号文档](https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html)：用于 `msinit`、`msnew`、`msatkinlehner`、`mshecke`、`mseval` 的数学定义。R74 固定 star 符号、twist Gauss 和定向和循环行判据；本次计算始终复用该空间。
4. 仓库 R47：真实全局高度的对数坐标；R54：有限坏高度靶集；R57：层 $41$ 的实际 $A=J$ 与解析秩一输入；R68、R71：极化传输和实际项链同源；R74、R77：$47$ 普通性、圆分导数及各因子高度非退化；R79：完整 $T_2$ 规范平移、$B_{-4},B_{-8}$ 及其精确比例平方。
