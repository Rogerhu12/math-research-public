# 秩三 Rubin–Stark 证书的固定椭圆单位与赋值矩阵表达式

**状态：已证明的有限层公式；跨素数非零性仍未证明。** 本文沿用 R19、R30、R32 的全部记号，特别是
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17,
$$
以及固定辅助素理想 $\mathfrak a=(67)$、修正集合 $\mathcal T=\{\mathfrak a\}$。以下给出 R32 的秩三取值如何准确变成一个固定函数 $\Phi$ 的值与两条辅助 $S$-单位的行列式。所有分母均显示出来。

## 1. 同一塔、同一固定函数与字符约定

写
$$
K_n=K(E[\pi^n]),\quad G_n=\Delta\times\Gamma_n,
\quad R=R_n=\mathbb Z_p[\Gamma_n],\quad B=\mathbb Q_p[\Gamma_n].
$$
$\widetilde\chi$ 为 R32 的直接作用字符，$\rho_E(\gamma)=1+p$。以下均在 $\widetilde\chi$ 分量上，并将单位群的 $p$-完备化写成加法模。

取 R19 的复周期和点
$$
f=34(1+i),\quad P_f=\xi(\Omega/f),\quad
P_n=\xi(\Omega/\pi^n),\quad
z_n=e_{\widetilde\chi}\Phi(P_n).
\tag{1.1}
$$
这里 $\Phi$ 就是 R19 的固定有理函数；其塔上的值是全局单位，见 R19 及 phi-coleman-tower 笔记。R32 证明去掉 $\mathcal T$-合同条件在此字符的 $p$-完备化上是同构，故可将 $z_n$ 无歧义地视作 $\mathcal T$-修正单位。

令 $\sigma_a$ 是 $(67)$ 的算术 Frobenius；$\rho_E(\sigma_a)=-67$。另令 $g_f\in\operatorname{Gal}(K_\infty/K)$ 为唯一满足
$$
\rho_E(g_f)=f
\tag{1.2}
$$
的元素。它存在，因为 $f$ 是 $\mathfrak p$-单位，且本塔的 CM 作用给 $\operatorname{Gal}(K_\infty/K)\simeq\mathbb Z_p^\times$。将这些群元素取字符分量后看作 $R$ 或 $\Lambda$ 的单位，不再另加符号。

## 2. 秩一 Rubin–Stark 元素的精确单位因子

设 $S=S_\infty(K)\cup S_{\rm ram}(K_n/K)$，令
$$
\epsilon_{1,n}
=\epsilon_{K_n/K,S,\mathcal T}^{\{\infty\},\widetilde\chi}
$$
为 BKS 的秩一 Rubin–Stark 元素，复位选择与 $\xi$ 的固定复嵌入一致。则
$$
\boxed{
\epsilon_{1,n}=u_n z_n,\qquad
u_n=\frac{4489\sigma_a^{-1}-1}{2g_f}\in R_n^\times.
}
\tag{2.1}
$$
这些 $u_n$ 来自同一个 $\Lambda$-单位 $u_\infty$，且中心评价为
$$
\boxed{u_\infty(p)=-\frac{68}{2f}
=-\frac1{1+i}.}
\tag{2.2}
$$
式 (2.1) 不依赖未出版的椭圆单位与高阶理想比较。

### 2.1 Robert 函数与 Rubin 的 $12$ 次幂规范

Bley 2006 §2 式 (2) 规定的 Robert 函数 $\psi_R$ 满足
$$
\psi_R(z;L,\mathfrak a)^{12}
=\frac{\varphi(z;L)^{12N\mathfrak a}}
 {\varphi(z;\mathfrak a^{-1}L)^{12}}.
$$
Rubin Lemma 7.10 的函数满足同一个商式。两种 $12$ 次幂的基本 theta 函数由其 sigma、Dedekind eta 和判别式表达式直接相同，故
$$
\Theta_{E,\mathfrak a}(\xi(\Omega/m))
=\psi_R(1;m\mathcal O_K,\mathfrak a)^{12}
\tag{2.3}
$$
对任一 $m\mathcal O_K$ 与 $\mathfrak a$ 互素的非平凡模成立。这里使用 $12$ 次幂，消除了 Robert 函数开根规范中的根单位歧义。

### 2.2 最低导子层的复 regulator 公式

置 $m_n=f\pi^n$，$F_n=K(m_n)$。有限字符 $\eta$ 遍历 $G_n$ 中限制在 $\Delta$ 为 $\widetilde\chi$ 的字符，并膨胀到 $\operatorname{Gal}(F_n/K)$。

在 $2,17$ 上方惯性群上，CM 作用值在 $\mu_4$ 中；$\widetilde\chi$ 对它们的约化忠实，$p$-幂阶的 $\Gamma_n$ 字符不改变这些惯性作用。因此各 $\eta$ 在坏素数处具有同一个导子 $\mathfrak f$。在 $\mathfrak p$ 处，其 tame 字符非平凡，故
$$
\operatorname{cond}(\eta)=\mathfrak f\pi^s
\quad\text{某个 }1\le s\le n.
\tag{2.4}
$$
特别地，没有遗漏或新增的坏素数 Euler 因子。

Bley 2006，p.90 式 (10)，给最低导子层 Robert 单位的复 regulator；在本文情形 $w(\operatorname{cond}\eta)=1$。若将该单位视为 $F_n$ 的单位，公式右端含有层数因子 $[F_n:K(\operatorname{cond}\eta)]$。

另一方面，Rubin Corollary 7.7 给
$$
N_{K(f\pi^j)/K(f\pi^{j-1})}
\Theta_{E,\mathfrak a}(\xi(\Omega/(f\pi^j)))
=\Theta_{E,\mathfrak a}(\xi(\Omega/(f\pi^{j-1})))
\quad(j>1).
\tag{2.5}
$$
因为两层导子均含 $\pi$，这里没有 $1-\operatorname{Frob}^{-1}$ 因子。作用 $e_\eta$ 后，范数左侧等于相应层数乘上原元素；故 (2.5) 正好消去 Bley 公式的层数因子。

令
$$
b_n=N_{F_n/K_n}
\Theta_{E,\mathfrak a}(\xi(\Omega/(f\pi^n))).
$$
复 regulator 与范数相容：单位的范数对应在复位置换模上把上方素位送到其下方素位。因此由 (2.3)、Bley 式 (10) 和 (2.5)，得到
$$
\lambda(e_\eta b_n)
=12(4489-\eta(\sigma_a))
 L_S^*(\eta^{-1},0)\,e_\eta w_\infty.
\tag{2.6}
$$
此处 $L_S^*$ 是恰好一阶的 leading coefficient。它的导子支持与 $S$ 的有限部分相同，故是 Bley 公式的同一个值。

BKS 的 $\mathcal T$-修正给乘子 $1-4489\eta(\sigma_a)^{-1}$。与 (2.6) 相比，复 regulator 的单射性于是给
$$
\epsilon_{1,n}
=-\frac1{12}\sigma_a^{-1}e_{\widetilde\chi}b_n.
\tag{2.7}
$$
这只是复 regulator 定义的精确比较，没有调用任何 $p$-adic regulator 非零结论。

### 2.3 平移参数产生的固定 Galois 元素

Rubin 的单位为
$$
\eta_n^{(a)}=\Lambda_{E,\mathfrak a,P_f}(P_n).
$$
$K_n/K$ 在 $\mathfrak p$ 处全分歧，而 $K(\mathfrak f)/K$ 在此未分歧，所以二者交为 $K$；射线类域次数公式给
$$
F_n=K(\mathfrak f)K_n.
$$
于是
$$
\eta_n^{(a)}
=N_{F_n/K_n}\Theta_{E,\mathfrak a}(P_f+P_n).
\tag{2.8}
$$
令 $\beta_n=f+\pi^n$。它与 $f\pi$ 互素，且
$$
P_f+P_n=[\beta_n]\xi(\Omega/(f\pi^n)).
$$
由 CM reciprocity，(2.8) 与 $b_n$ 相差 $\sigma_{(\beta_n)}$ 的作用。若写 $\psi_E((b))=\varepsilon(b)b$，则 $\varepsilon$ 只依赖 $b\bmod\mathfrak f$。因为 $\pi=\psi_E(\mathfrak p)$，有 $\varepsilon(\pi)=1$，故
$$
\varepsilon(\beta_n)=\varepsilon(\pi^n)=1,
\qquad
\psi_E((\beta_n))=\beta_n\equiv f\pmod{\pi^n}.
$$
因此 $\sigma_{(\beta_n)}$ 在 $K_n$ 上的限制就是 $g_f$，并且
$$
\eta_n^{(a)}=g_f b_n.
\tag{2.9}
$$
代入 (2.7)，得
$$
\epsilon_{1,n}
=-\frac1{12\sigma_a g_f}\,e_{\widetilde\chi}\eta_n^{(a)}.
\tag{2.10}
$$

### 2.4 与原固定 $\Phi$ 的比较

R19 的除子证明对辅助 $(67)$ 原样成立：$[-67]$ 固定 $E[\mathfrak f]$，所以
$$
\frac{\Lambda_{E,\mathfrak a}(P)}
 {\Lambda_{E,\mathfrak a}(-P)}
=\left(\frac{\Phi([-67]P)}{\Phi(P)^{4489}}\right)^{12}.
$$
在 $P=P_n$ 取值并投影到奇字符，给
$$
e_{\widetilde\chi}\eta_n^{(a)}
=6(\sigma_a-4489)z_n.
\tag{2.11}
$$
把 (2.11) 代入 (2.10)，即得 (2.1)。R32 已证明 $1-4489\sigma_a^{-1}$ 是各层以及 $\Lambda$ 中的单位；$2$ 与 $g_f$ 也是单位。其中心评价由 $\rho_E(\sigma_a)=-67$、$\rho_E(g_f)=f$ 得到 (2.2)。

## 3. 加入两个分裂素位的赋值正合列

固定 $W=\{\mathfrak q_1,\mathfrak q_2\}\in\mathcal V_{2,n}$，为每个 $\mathfrak q_j$ 选择一个上方素位 $w_j$。记
$$
U_0=(\mathcal O_{K_n,S,\mathcal T}^{\times}\otimes\mathbb Z_p)^{\widetilde\chi},
\qquad
U_W=(\mathcal O_{K_n,S\cup W,\mathcal T}^{\times}\otimes\mathbb Z_p)^{\widetilde\chi}.
$$
定义直接作用的等变赋值
$$
v_j(u)=\sum_{g\in G_n}\operatorname{ord}_{g w_j}(u)g
=\sum_{g\in G_n}\operatorname{ord}_{w_j}(g^{-1}u)g,
$$
再取 $\widetilde\chi$ 分量，并用 $e_{\widetilde\chi}\mathbb Z_p[G_n]\simeq R$。这个方向使 $v_j(hu)=h v_j(u)$，没有取逆字符。

射线理想类正合列给
$$
0\longrightarrow U_0\longrightarrow U_W
\xrightarrow{(v_1,v_2)}R^2
\xrightarrow{(a,b)\mapsto ac_1+bc_2}A_n
\longrightarrow A_{n,W}\longrightarrow0,
\tag{3.1}
$$
其中 $c_j$ 是 $w_j$ 的类的字符分量，
$$
A_{n,W}=A_n/(Rc_1+Rc_2).
\tag{3.2}
$$
(3.1) 中原本去掉的 $S$-类在该字符上为零，原本的射线修正又由 R32 消失，所以确是这里的 $A_n$。

张量 $\mathbb Q_p$ 后，类群项消失，得到
$$
0\longrightarrow B U_0\longrightarrow B U_W
\xrightarrow{(v_1,v_2)}B^2\longrightarrow0.
\tag{3.3}
$$
$B U_0$ 是秩一自由 $B$-模，$B U_W$ 是秩三自由 $B$-模。此结论只来自 Dirichlet regulator 的各有限字符维数，不断言相应整 $R$-格自由。

## 4. 秩三元素的赋值收缩及行列式公式

采用 BKS 的顺序 $V\cup W=[\infty,\mathfrak q_1,\mathfrak q_2]$，并令
$$
\epsilon_{3,n,W}
=\epsilon_{K_n/K,S\cup W,\mathcal T}^{V\cup W,\widetilde\chi}.
$$
则
$$
\boxed{(v_1\wedge v_2)(\epsilon_{3,n,W})=\epsilon_{1,n}.}
\tag{4.1}
$$

完整核对如下。因为 $W$ 完全分裂，新增的两个 Euler 因子为 $1-(N\mathfrak q_j)^{-s}$，它们在 $s=0$ 的首项为 $s\log N\mathfrak q_j$。故秩三 leading term 是原秩一 leading term 乘上这两个实对数。复 regulator 在 $w_j$ 坐标的映射恰为 $v_j\log N\mathfrak q_j$，这两个对数因子因而约去。$S$ 中可取 $w_0$ 位于 $\mathfrak p$ 上方，其字符分量为零，所以 BKS 规范中的 $w_j-w_0$ 不产生额外项。由 (3.3) 的顶外积收缩同构及复 regulator 的单射性得到 (4.1)。两个有限位移过第一列的符号为正，与所选顺序一致。

任选 $z_1,z_2\in U_W$，使
$$
V_W=\begin{pmatrix}v_1(z_1)&v_1(z_2)\\v_2(z_1)&v_2(z_2)\end{pmatrix}
$$
的行列式在 $B$ 中可逆。由 (3.3) 和 (4.1)，
$$
\boxed{
\epsilon_{3,n,W}
=\frac{\epsilon_{1,n}\wedge z_1\wedge z_2}{\det V_W}
=\frac{u_n}{\det V_W}\,z_n\wedge z_1\wedge z_2
\quad\text{于 }\bigwedge_B^3(BU_W).
}
\tag{4.2}
$$
因此对任意 $\phi_0,\phi_1,\phi_2\in\operatorname{Hom}_R(U_W,R)$，有准确公式
$$
\boxed{
(\phi_0\wedge\phi_1\wedge\phi_2)(\epsilon_{3,n,W})
=\frac{u_n}{\det V_W}
\det\begin{pmatrix}
\phi_0(z_n)&\phi_0(z_1)&\phi_0(z_2)\\
\phi_1(z_n)&\phi_1(z_1)&\phi_1(z_2)\\
\phi_2(z_n)&\phi_2(z_1)&\phi_2(z_2)
\end{pmatrix}.
}
\tag{4.3}
$$
右侧先在 $B$ 中计算；Bley–BKS 的整性保证它实际属于 $R$。这并不表示可以在不知道整格的情况下任意指定三个行向量：每一个 $\phi_i$ 都必须在整个 $U_W$ 上取 $R$ 中的值。

## 5. 可选成标量的分母及正确的模精度

可使 (4.3) 的分母完全明确。令 $h_j$ 为 $w_j$ 在完整射线类群 $\operatorname{Cl}^{\mathcal T}(K_n)$ 中的阶，选择
$$
(w_j)^{h_j}=(\widetilde z_j),\qquad
\widetilde z_j\equiv1\pmod w\quad(w\mid\mathfrak a),
$$
并取 $z_j=e_{\widetilde\chi}\widetilde z_j$。则
$$
v_i(z_j)=h_j\delta_{ij},\qquad
\det V_W=h_1h_2.
\tag{5.1}
$$
置 $s=v_p(h_1h_2)$，将 (4.3) 的三阶行列式记为 $D_{n,W}(\phi)$。因为 $u_n$ 是 $R$-单位，整性恰说明
$$
D_{n,W}(\phi)/(h_1h_2)\in R.
\tag{5.2}
$$
于是 R32 的有限证书可准确改写成
$$
\boxed{
 e_n\!\left(D_{n,W}(\phi)/(h_1h_2)\right)\ne0
 \quad\text{于 }\mathbb Z_p/p^n.
}
\tag{5.3}
$$
固定因子 $u_n$ 不改变这个非零条件；按中心评价它的单位值已经明确为 $-1/(1+i)$。

必须**先在 $R_n$ 中除以 $h_1h_2$，再作用 $e_n$**。不能先对原始行列式做 $T=p$ 评价后在模 $p^n$ 中除以 $p^s$。原因是 $e_n$ 只有模 $p^n$ 精度，且不存在同样定义的 $R_n\to\mathbb Z_p/p^{n+s}$ 环同态：$\omega_n(p)$ 的估值恰为 $n$。

一个有效计算方式是用 $R_n$ 的自由 $\mathbb Z_p$ 基
$$
1,\gamma_n,\ldots,\gamma_n^{p^{n-1}-1}
$$
先得到 $D_{n,W}(\phi)$ 的各系数模 $p^{n+s}$，利用 (5.2) 逐系数除以 $p^s$ 及剩余单位，再用 $\gamma_n\mapsto1+p\bmod p^n$。这个过程给 (5.3) 的准确值，不依赖任意幂级数提升。

## 6. 单个辅助对究竟移除了哪两个类群方向

令 $J_{n,W}$ 是固定 $W$ 下所有 (4.3) 的取值生成的理想。则有比 R32 求和形式更具体的等式
$$
\boxed{
J_{n,W}=\operatorname{Fitt}_{R,0}(A_{n,W})
=\operatorname{Fitt}_{R,0}(A_n/(Rc_1+Rc_2)).
}
\tag{6.1}
$$
证明只用已出版 BKS Theorem 1.5(ii) 的 $i=0$ 形式，应用于 $S\cup W$、秩 $r=3$。其转置 Selmer 正合列在此字符上为
$$
0\longrightarrow A_{n,W}\longrightarrow
\mathcal S^{\rm tr}_{S\cup W,\mathcal T,\chi}
\longrightarrow R^3\longrightarrow0.
$$
右端自由，所以作为 $R$-模可裂。故转置模的第三 Fitting 理想恰是 $A_{n,W}$ 的第零 Fitting 理想；BKS 的秩三外积值公式给 (6.1)。这里的分裂无需选为规范分裂。

这个等式说明辅助素数不仅需要在 $K_n/K$ 完全分裂，还必须在正确的理想类方向上发挥作用。若 $c_1=c_2=0$，则
$$
J_{n,W}=\operatorname{Fitt}_{R,0}(A_n).
$$
R30 给 $q_p\ge1$，故无限层第零 Fitting 理想包含于 $(T-p)$。准确基变换与 R32 的评价公式随即给
$$
e_n(J_{n,W})=0
\quad\text{对所有这样的 }W,n.
\tag{6.2}
$$
所以把两条辅助素数都选成字符类群中平凡的类，绝不产生所需的新证书。它只把原秩一取值扩写成一个没有新类群信息的三阶行列式。

## 7. 现在剩下的具体算术缺口

本笔记已经把秩三 Rubin–Stark 元素消去为：

1. 原固定有理函数 $\Phi$ 的单个塔值 $z_n$；
2. 两条可通过射线理想类主化取得的 $S$-单位；
3. 三个在完整 $S$-单位整格上取整数值的等变同态；
4. 一个明确的标量分母 $h_1h_2$。

因此无需再把一个抽象秩三复 $L$ 值作为不可计算黑箱。但主问题仍要求：对无穷多个 $p$，选到某层 $n$、某对非平凡类方向的辅助素数及某三条整数值同态，使归一化行列式满足 (5.3)。

复 regulator 非零只能保证有理化后存在非零值；Baker–Brumer 型的 $p$-adic 对数非零也没有给行列式在所需精度下的非零性。若把三条同态换成局部对数，还必须证明它们的整性、$R_n$-线性及对所需对偶格的控制；不能默认这三个问题已经由对数非零解决。尤其，辅助主化分母与整格中三列的共同 $p$-因子都可能增长。

以上公式保留了这两个实际缺口：辅助类方向的选择，以及归一化行列式的模精度。它们不被 (2.2) 的固定单位因子或普通的复非零性自动消除。

## 来源

- W. Bley，*On the Equivariant Tamagawa Number Conjecture for Abelian Extensions of a Quadratic Imaginary Field*，Doc. Math. **11** (2006), 73–118，§2 式 (2)、p.90 式 (7)、(10)；[出版原文](https://ftp.gwdg.de/pub/EMIS/journals/DMJDMV/vol-11/04.pdf)。
- D. Burns、M. Kurihara、T. Sano，*On zeta elements for $\mathbb G_m$*，Doc. Math. **21** (2016), 555–626，Theorem 1.5(ii)、§§4.1、5.1–5.2 及 Theorem 8.1；[出版原文](https://ems.press/content/serial-article-files/26320?nt=1)。
- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，Theorem 7.4(ii)、Corollary 7.7、Lemma 7.10、Definition 8.1、Proposition 11.6 的辅助理想关系；[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- 本仓库 R19、R30、R32，以及 `notes/2026-11-12-phi-coleman-tower.md`。
