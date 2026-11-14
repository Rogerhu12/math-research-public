# R36：两条整 Bockstein 泛函与一个非零的 rank 2 值

**可信度：已证明。** 日期：2026-11-12。沿用 R34–R35 的 $E:y^2=x^3-17x$、$K=\mathbb Q(i)$ 和目标素数
$p\ge13,\ p\equiv1\pmod4,\ p\ne17$。

本文给出 R35 二阶行列式中两条具体的整泛函。它们来自局部 Coleman 坐标和辅助素位赋值，各作一次中心除法。对原固定 $\Phi$ 的系数
$$
z_\infty=e_{\widetilde\chi}\Phi(P_{\pi^\infty})
=F_p(T)u_\infty,\qquad
F_p(T)=(T-p)^2G_p(T),
$$
所得 rank $2$ Rubin–Stark 值准确为
$$
\boxed{\quad p^{b_p}u_nG_p(T)\pmod{\omega_n(T)}.\quad}
\tag{0.1}
$$
这里 $u_n$ 是 R35 的明确单位因子，$b_p$ 只由两个固定点的局部椭圆对数决定。附带一个完整指定的有限实例：$p=13$，辅助素理想为 $(109,i-76)$，(0.1) 的中心值为 $3\pmod{13}$。

这个实例落实了泛函和整除。对无穷多个 $p$ 证明 $G_p(p)\ne0$ 仍未完成，而且该条件比只求 $\Sha[p^\infty]$ 有限更强。

## 1. 原固定函数的局部 Coleman 坐标

取 R24 的显式严格 Lubin–Tate 坐标 $X$ 和局部单位基
$$
u_\infty=e_{\widetilde\chi}
\bigl(\beta-X(P_{\pi^n})\bigr)_n,
\qquad\beta^{p-1}=1-\pi,\quad\beta\equiv1\pmod p.
\tag{1.1}
$$
其中 $\pi=\psi_E(\mathfrak p)$，$\rho_E(\gamma)=1+p$，
$\Lambda=\mathbb Z_p[[T]]$，$T=\gamma-1$。令
$$
\theta=T-p,\quad
\omega_n(T)=(1+T)^{p^{n-1}}-1,\quad
R_n=\Lambda/(\omega_n),\quad S_n=\mathbb Z_p/p^n.
$$

R19 和 phi-coleman-tower 笔记证明原 $\Phi$ 的值 $z_\infty$ 是相容全局单位，且生成目标字符的椭圆单位模。因此唯一的系数
$$
F_p(T)\in\Lambda,\qquad z_\infty=F_p(T)u_\infty
\tag{1.2}
$$
生成 $\operatorname{char}_{\Lambda}(X_\infty^{\widetilde\chi})$。R20、R24 的秩二论证给
$$
F_p(T)=\theta^2G_p(T),\qquad G_p(T)\in\Lambda.
\tag{1.3}
$$
本结果固定采用 (1.1)–(1.2) 的 $F_p$，而非任意相差单位的特征级数；这样以下取值的常数也确定。

### 1.1 所有有限层的准确局部范数控制

令 $k_n=K_{n,\mathfrak p}=\mathbb Q_p(E[\pi^n])$，$U_n$ 为其单位群的 pro-$p$ 完备化。则
$$
\boxed{\quad
U_\infty^{\widetilde\chi}/\omega_nU_\infty^{\widetilde\chi}
\xrightarrow{\sim}U_n^{\widetilde\chi}=R_nu_n^{\rm LT}.
\quad}\tag{1.4}
$$
为免与 Rubin–Stark 单位因子混淆，有限层局部基在本文记作 $u_n^{\rm LT}$。

证明与 R20 首层证明相同，但在此说明其任意层版本。对 $m\ge n$，局部互反律的范数余核是 $\operatorname{Gal}(k_m/k_n)$，$\Delta$ 的共轭作用平凡；赋值群的 $\Delta$ 作用也平凡。非平凡 $\widetilde\chi$ 因而消去这两项，使 $U_m^{\widetilde\chi}\to U_n^{\widetilde\chi}$ 的范数满射。Hilbert 90 又给范数核为
$(\gamma^{p^{n-1}}-1)U_m^{\widetilde\chi}$；原像的赋值修正经 $e_{\widetilde\chi}$ 消失。用 R20 的紧性和有限交性质取相容原像，便得到无限层核恰为 $\omega_nU_\infty^{\widetilde\chi}$。

非异常性排除了 $\mu_p\subset k_1$。若某个 $k_n$ 含 $\mu_p$，则 $[k_1(\mu_p):k_1]$ 同时整除 $p-1$ 与 $[k_n:k_1]$ 的 $p$ 幂，矛盾。因此各层单位群没有 $p$ 挠；结合 R24 的局部自由基，得到 (1.4) 的整自由模同构，未加入有限核或有限余核。

## 2. 中心除法在有限环中的准确含义

评价
$$
e_n:R_n\longrightarrow S_n,\qquad T\longmapsto p\pmod{p^n}
$$
满足
$$
\boxed{\quad\ker e_n=\theta R_n,\qquad
\theta\text{ 是 }R_n\text{ 的非零因子}.\quad}
\tag{2.1}
$$
第一项来自
$$
R_n/\theta R_n\simeq\mathbb Z_p/\omega_n(p)\mathbb Z_p,
\qquad v_p(\omega_n(p))=n.
$$
第二项可在 $B_n=\mathbb Q_p\otimes R_n$ 中检查：它分解为各有限阶 $\Gamma_n$ 字符的域，每个分量上的 $\theta$ 值是
$\zeta-(1+p)\ne0$，因为 $\zeta$ 是有限阶单位根而 $1+p$ 非有限阶。所以 $\theta$ 在 $B_n$ 中可逆；$R_n$ 为无 $\mathbb Z_p$ 挠模，故在 $R_n$ 中为非零因子。

因此当 $R_n$-线性泛函 $f:V\to R_n$ 满足 $e_n f=0$ 时，可唯一地定义整泛函
$$
f/\theta:V\longrightarrow R_n.
\tag{2.2}
$$
这是本文所谓一次 Bockstein 除法：它使用短正合列
$0\to R_n\xrightarrow{\theta}R_n\to S_n\to0$。不对有限群环作不良定义的形式求导，也不在 $S_n$ 中除以零。

## 3. 两个原始泛函与全局 Kummer 互反式

取 R35 的辅助素数 $\mathfrak q$、其上方素位 $w$，并假设
$$
\lambda_{p,n}(c_w)\in S_n^\times.
\tag{3.1}
$$
令 $U_{\mathfrak q}$ 为 R35 的 $\widetilde\chi$ 分量的 $S\cup\{\mathfrak q\}$-单位格，带固定 $(67)$ 的合同条件。局部化后，由 (1.4) 定义
$$
\mathcal L_n:U_{\mathfrak q}\longrightarrow R_n,
\qquad\operatorname{loc}_{\mathfrak p}(u)=\mathcal L_n(u)u_n^{\rm LT}.
\tag{3.2}
$$
在 $\mathfrak p$ 处的赋值不造成问题：它的 $\Delta$ 作用平凡，所以目标字符的 $S$-单位局部化仍在单位模中。特别地，
$$
\mathcal L_n(z_n)=F_{p,n},
\tag{3.3}
$$
下标 $n$ 表示模 $\omega_n$。

第二个原始泛函是 R35 的等变赋值
$$
v_w:U_{\mathfrak q}\longrightarrow R_n.
$$

### 3.1 局部 Kummer 常数

Rubin Lemma 6.8 规定
$$
\langle R,x\rangle_{\pi^n}
=\bigl(\pi^{-1}\log_E(R)\bigr)\delta_n(x).
$$
R27 的显式互反律和 (1.1) 给
$$
\delta_\infty(u_\infty)
=\kappa_0\,\mathbf t,\qquad
\kappa_0=(\pi-1)(-\beta^{-1})
=\frac{1-\pi}{\beta}\in\mathbb Z_p^\times,
\tag{3.4}
$$
其中 $\mathbf t$ 是固定 Tate 基。有限层范数相容性于是给
$$
\delta_n(x)=\kappa_0 e_n(\mathcal L_n(x))\,\mathbf t_n.
$$
所以对全局点 $R\in E(K)$，局部 Kummer 常数准确为
$$
c_R=\kappa_0\,\frac{\log_E(R)}{\pi}\in\mathbb Z_p.
\tag{3.5}
$$
其赋值为 $v_p(\log_E R)-1$；没有额外的 $p$ 因子。归一化理想 $(\pi^n)$ 与 $(p^n)$ 在 $\mathbb Z_p$ 中相同，所以以下统一写成模 $p^n$。

### 3.2 全局 Artin 互反给出的行关系

令 $t_{R,w}\in\mathbb Z_p/p^n$ 为全局 $\pi^n$-Kummer 类在 $w$ 的算术 Frobenius 上的值，按 $\mathbf t_n$ 取坐标。则对所有 $u\in U_{\mathfrak q}$，
$$
\boxed{\quad
c_R e_n(\mathcal L_n(u))
+t_{R,w} e_n(v_w(u))=0\quad\text{于 }S_n.
\quad}\tag{3.6}
$$
证明如下。把 $R$ 的 Kummer 类限制到 $K_n$，得到到 $E[\pi^n]$ 的交换 Galois 同态，它远离 $\mathfrak p$ 无分歧。将主 idèle $u$ 代入全局 Artin 互反，所有局部项之和为零。在 $\mathfrak p$ 处使用 (3.4)–(3.5)；在 $g w$ 处，Frobenius 值是 $\rho_E(g)t_{R,w}$，所以这些项合成直接作用约定的 $e_n(v_w(u))t_{R,w}$。原有 $S$ 中有限素位的位置模的 $\chi$ 分量为零，见 R32，故不留下额外赋值项；无穷位也不贡献 pro-$p$ 项。这得到 (3.6)。

## 4. 两行都可以整地除一次中心

射线类群正合列说明 $v_w(u)c_w=0$。对它应用 (3.1) 的满射，得到
$$
e_n(v_w(u))=0\quad(u\in U_{\mathfrak q}).
$$
由 (2.1)，
$$
V_{n,w}:=v_w/\theta\in\operatorname{Hom}_{R_n}(U_{\mathfrak q},R_n).
\tag{4.1}
$$

令
$$
b_p=\min\{v_p(\log_E P),v_p(\log_E Q)\}-1\ge0,
\qquad P=(-1,4),\ Q=(9,24).
\tag{4.2}
$$
在 (3.6) 中取达到这个最小值的点。其 $c_R$ 为 $p^{b_p}$ 乘一个单位，而第二项已为零。因此
$$
p^{b_p}e_n(\mathcal L_n(u))=0
\quad(u\in U_{\mathfrak q}),
$$
再由 (2.1)，
$$
L_{n,w}^{(1)}:=p^{b_p}\mathcal L_n/\theta
\in\operatorname{Hom}_{R_n}(U_{\mathfrak q},R_n).
\tag{4.3}
$$
这两条泛函定义在完整的 $U_{\mathfrak q}$ 上；整性不是只对 $z_n,z_w$ 两个测试元素检查得来的。(3.6) 正是已知全局点在这里提供的额外算术输入。

## 5. 实际行列式及最低中心阶数

按 R35，选 $h,z_w$ 使 $v_w(z_w)=h$，则
$$
\epsilon_{2,n,w}=\frac{u_n}{h}z_n\wedge z_w,
\qquad
u_n=\frac{4489\sigma_{67}^{-1}-1}{2g_f}\in R_n^\times.
$$
因为 $v_w(z_n)=0$，由 (4.1)–(4.3) 直接计算
$$
\begin{aligned}
\bigl(L_{n,w}^{(1)}\wedge V_{n,w}\bigr)(\epsilon_{2,n,w})
&=\frac{u_n}{h}
\det\begin{pmatrix}
p^{b_p}F_{p,n}/\theta & p^{b_p}\mathcal L_n(z_w)/\theta\\
0 & h/\theta
\end{pmatrix}\\
&=p^{b_p}u_n F_{p,n}/\theta^2\\
&=p^{b_p}u_nG_{p,n}.
\end{aligned}
\tag{5.1}
$$
第一行可在 $B_n$ 中演算；两条泛函的整性以及 (1.3) 又保证每个最终值属于 $R_n$。没有在模 $p^n$ 的环里先评价再作除法，也不需要未知的主化阶 $h$ 作数值近似。

中心评价为
$$
\boxed{\quad
e_n\bigl((L_{n,w}^{(1)}\wedge V_{n,w})(\epsilon_{2,n,w})\bigr)
=-\frac{p^{b_p}}{1+i}\,G_p(p)\pmod{p^n}.
\quad}\tag{5.2}
$$
因此若 $G_p(p)\ne0$，取 $n>b_p+v_p(G_p(p))$，再取 R35 保证存在的任一辅助素数，就得到一个非零值，证明该 $p$ 的初级有限性。

对这对原始泛函而言，总共两次中心除法是首次可能产生非零中心值的阶数。原始配对 $(\mathcal L_n,v_w)$ 只给 $u_nF_{p,n}$；只除一行给 $u_nF_{p,n}/\theta$（可能另乘 $p^{b_p}$），中心均为零。两行各除一次得到
$$
G_p(p)=\frac{F_p''(p)}{2}.
\tag{5.3}
$$
这个最低阶结论只针对上述局部坐标/赋值行及其中心除法，不断言任意整 Rubin–Stark 泛函都必须来自此构造。

### 5.1 充分值仍强于初级有限目标

若 $G_p(p)\ne0$，特征级数在中心恰有二重零。反向推理不成立：R34 的 $q_p=1$ 只控制中心模的几何生成元数，允许非平凡 Jordan 块。

例如仅在模论上取
$$
M=\Lambda/(\theta)\oplus\Lambda/(\theta^2),\quad
B=\Lambda/(\theta)\text{ 为第一直和项},\quad
\mathcal A=M/B=\Lambda/(\theta^2).
$$
则中心 Selmer 维数是二，$q=1$，且局部秩一中心像单射，但特征级数是 $\theta^3$，相应 $G(p)=0$。这是说明逻辑强弱的模论例子，不声称本曲线某个素数实现它。不能从本题要求的初级有限性倒推出 (5.3) 非零或 $p$-adic 高度非退化。

## 6. 指定非零实例：$p=13$ 与 $\mathfrak q=(109,i-76)$

本节只落实一次公式，不以有限实例代替跨素数论证。采用 $13$-进嵌入 $i\equiv8\pmod{13}$，故
$$
\pi=-3+2i,\quad \bar\pi\equiv7,\quad
f=34(1+i)\equiv7\pmod{13}.
$$

### 6.1 局部点和辅助素数均为有限精确算术

直接计数给 $\#E(\mathbb F_{13})=20$。有理数群法精确给
$$
\frac{t([20]P)}{13}\equiv
\frac{t([20]Q)}{13}\equiv7\pmod{13},
\qquad t=-x/y.
$$
因为形式群对数在 $13\mathbb Z_{13}$ 上与 $t$ 模 $13^2$ 相同，且 $20\equiv7\pmod{13}$，所以
$$
\frac{\log_E(P)}{13}\equiv
\frac{\log_E(Q)}{13}\equiv1\pmod{13}.
\tag{6.1}
$$
故 $b_{13}=0$，R35 的未饱和严格类模 $13$ 是 $\kappa(P-Q)$。

在 $\mathbb F_{109}$ 中取 $i=76$。直接群法给 $\#E(\mathbb F_{109})=130$，且 $[\pi]=[-3]+[2i]$ 的核为以下十三点：
$$
O,\quad(1,\pm23),\quad(29,\pm5),\quad(46,\pm31),\quad
(63,\pm42),\quad(80,\pm53),\quad(108,\pm4).
$$
因此 $\mathfrak q=(109,i-76)$ 的 Frobenius 在 $E[\pi]$ 上为恒等，$\mathfrak q$ 完全分裂于 $K_1/K$。同一计算给
$$
[\pi]E(\mathbb F_{109})
=\{O,(0,0),(36,\pm41),(51,\pm49),(58,\pm18),(73,\pm45)\},
$$
而
$$
P-Q=(26,28)\notin[\pi]E(\mathbb F_{109}).
$$
由于整个 $E[\pi]$ 已有理，一个 $\pi$-除法点被 Frobenius 固定，当且仅当该纤维在 $\mathbb F_{109}$ 中有点。因此 $\kappa(P-Q)$ 在 $w$ 的 Frobenius 上非零。这证明 R35 的 $d_{13}=0$，并且任取 $w\mid\mathfrak q$ 都满足 (3.1)。

这些局部点算和辅助素数数据由
[短整数脚本](../scripts/check-r36-p13.py)
独立重现；脚本不调用曲线数据库、数值 $L$ 函数或浮点运算。

### 6.2 已发表临界值输入及最终取值

CLS II 的正确 Table I 中，$D=17,p=13$ 一项为
$$
c_{13}^+(E)/13^2\equiv6\pmod{13}.
\tag{6.2}
$$
这里引用的是该论文已经修正旧表因子 $4$ 后的精确计算。R19 的准确公式
$$
\lambda_{13}:=\delta^{13}\log\Phi(O)
=-2 f^{13}12!\,c_{13}^+(E)
$$
给 $\lambda_{13}/13^2\equiv6$。另一方面 R24 的本地基值为
$$
\operatorname{CW}_{13}(u_\infty)\equiv1-\bar\pi\equiv7\pmod{13},
$$
且
$\lambda_{13}=F_{13}((1+13)^{13}-1)\operatorname{CW}_{13}(u_\infty)$。
该参数属于 $13^2\mathbb Z_{13}$，除去 $\theta^2$ 后模 $13$ 得
$$
G_{13}(13)\equiv6/7\equiv12\pmod{13}.
$$
最后 R35 的 Rubin–Stark 单位因子满足 $e_1(u_1)=-1/(1+i)\equiv10\pmod{13}$。所以对以上指定辅助素数与任一上方素位 $w$，
$$
\boxed{\quad
e_1\bigl((L_{1,w}^{(1)}\wedge V_{1,w})(\epsilon_{2,1,w})\bigr)
=10\cdot12=3\pmod{13}.
\quad}\tag{6.3}
$$
这是 (5.2) 的一个具体非零值。表值 (6.2) 是已发表输入；附带脚本仅复核其余整数算术和归一化，不声称重新算出了该 Hecke 值。

## 来源与当前边界

- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，Lemma 6.8、Theorem 6.9、§11.2、Proposition 12.2、Theorem 12.3：[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- J. Coates、Z. Liang、R. Sujatha，*The Tate-Shafarevich group for elliptic curves with complex multiplication II*，Milan J. Math. 78 (2010)，395–416；预印本 Table I 的 $D=17,p=13$ 行及其前的旧表勘误：[原文](https://arxiv.org/pdf/1005.4206)。
- 本仓库 R19、R20、R24、R27、R34、R35。

两条导出泛函及 (5.1) 无条件成立。尚需证明的跨素数输入是某种足够弱的非零性；本次具体构造给出的 $G_p(p)\ne0$ 仍未对无穷多个 $p$ 证明。有限阶字符处椭圆单位对数非零，本身不证明这一中心二阶值非零。
