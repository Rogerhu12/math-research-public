# R150 附录：rankH2、rankV2 的本质五维层只余一个双约化 Gaussian 规范

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：必要条件已证明，剩余规范的空性未证明。** 原完整临界点若 $\operatorname{rank}H=\operatorname{rank}V=2$ 且 $\dim\operatorname{ess}(T_3)=5$，则两个物理除子都约化；全部非零 $Hp$ 分支及 H 两点正交分支均空。唯一保留分支为 $Hp=0$、$F^2+g^2=0$，且其完整五阶 Gram 被本文固定到显示的有限常数规范。本文没有把该必要规范当成实际存在的临界点，也不把它误报为已排除。

## 1. 原方程和完整结论

沿用[至少一 tangent 的完整排除稿](R150-appendix-rank-two-second-and-third-cumulants-with-a-tangent-support-have-essential-dimension-at-most-four.md) §§1–2 的原完整 $\Gamma,N$、最高式及全部尺度规范。该稿已经排除任一个非约化长度二除子，所以这里只须两个都约化。

写
$$
H=\tfrac12(z^2+w^2),\qquad V=\tfrac12(u^3+v^3),
\tag{1.1}
$$
其中四个物理点都不同。六维 $K$ 非退化，$z,w,u,v$ 都满足物理自等向关系。反设的五空间为
$$
E=\operatorname{span}(y,z,w,u,v)=\operatorname{ess}(T_3),
$$
五列独立，故 $\operatorname{rank}K|_E\ge4$。所有物理代表允许无穷远。

仍置
$$
p=Ky,\quad F=\tfrac12yKy,\quad
g=zKw,\quad a=p(z),\quad b=p(w),\quad e=uKv.
$$
原完整 mean Gaussian 三系数是
$$
F^2-a^2-b^2+g^2=0,\qquad Fa=gb,\qquad Fb=ga.
\tag{1.2}
$$
记交叉矩阵
$$
M=\begin{pmatrix}A&C\\B&D\end{pmatrix}
=\begin{pmatrix}zKu&zKv\\wKu&wKv\end{pmatrix}.
$$
V 两个 mean 系数及最高式在 V 值的评价给
$$
p(u)^2=A^2+B^2,\quad p(v)^2=C^2+D^2,\quad
p(u)^3=p(v)^3=e^3.
\tag{1.3}
$$
若 $e=0$，则 $p(u)=p(v)=0$。若 $e\ne0$，用保 (1.1) 的两个三次单位根尺度，准确规范为
$$
p(u)=p(v)=e.
\tag{1.4}
$$

**定理。** 本质五维反设下只能出现
$$
\boxed{
\begin{gathered}
a=b=0,\quad Fg e\ne0,\quad F^2+g^2=0,\\
C=-A,\quad D=-B,\quad A B\ne0,\\
A^2+B^2=e^2,\quad AB=-\frac{Fg}{2},\quad
2e^3=Fg^2=-F^3.
\end{gathered}}
\tag{1.5}
$$
此时在基 $(y,z,w,u,v)$ 中，原限制 Gram 必为
$$
\boxed{
\begin{pmatrix}
2F&0&0&e&e\\
0&0&g&A&-A\\
0&g&0&B&-B\\
e&A&B&0&e\\
e&-A&-B&e&0
\end{pmatrix}.}
\tag{1.6}
$$
其行列式是
$$
2F^2e(F-e)(2F-e)\ne0.
\tag{1.7}
$$
所以这一必要五空间实际非退化，而不是仅满足原秩下界四。

## 2. H 两点正交的全部分支为空

设 $g=0$。由 (1.2)，$F=0$、$a^2+b^2=0$；$HKH=0$。

先设 $e\ne0$ 并用 (1.4)。在两个 H 物理值评价完整 N，因 H 的 Gram 块为零，得到
$$
e(A^2+C^2)=e(B^2+D^2)=0.
$$
而 (1.3) 给两列平方和皆为 $e^2$。相加得 $2e^2=0$，矛盾。所以 $e=0$，$p(u)=p(v)=0$，并有
$$
A^2+B^2=C^2+D^2=0.
\tag{2.1}
$$

现在 $V_p=0$，完整 N 只余 $-2\operatorname{Sym}_{\Sigma}(y\otimes Hp)$。原极线恒等式 $P\,k_{Hp}=0$ 在多项式整环中迫 $Hp=0$；因为 K 可逆及 $P\ne0$，没有把仅投影为零的矩阵直接当成零矩阵。故 $a=b=0$，$y$ 与全部 E 正交。

最高式在 H 两物理值评价给
$$
A^3+C^3=0,\qquad B^3+D^3=0.
\tag{2.2}
$$
(2.1)—(2.2) 迫 $\operatorname{rank}M\le1$。直接证明如下：若某一列为零便已成立；若两列独立，它们必须属于二维平方型的两条不同等向线，故可写
$$
B=\varepsilon iA,\qquad D=-\varepsilon iC,\qquad AC\ne0,\quad\varepsilon\in\{1,-1\}.
$$
(2.2) 第一式给 $C^3=-A^3$；第二式给 $C^3=A^3$，矛盾。

H、V 的两个 Gram 块均为零，而交叉块秩至多一，所以 $K|_E$ 秩至多二，违反五空间限制秩至少四。全部 $g=0$ 情形被排除。

## 3. $g\ne0$ 且 $Hp\ne0$ 的全部分支为空

由 (1.2)，$g\ne0$ 时 $F\ne0$。若 $(a,b)\ne(0,0)$，则
$$
F^2=g^2,\qquad a^2=b^2=g^2.
$$
给 $z,w$ 分别乘适当的正负号（保 H 不变），可以同时规范为
$$
g=F,\qquad a=b=F.
\tag{3.1}
$$
令
$$
\eta=y-z-w.
$$
则
$$
\eta Kz=\eta Kw=\eta K\eta=0.
\tag{3.2}
$$
完整 N 准确化为
$$
N=F\eta^2-2F(z^2+w^2)+4V_p.
\tag{3.3}
$$

若 $e=0$，则 $V_p=0$；(3.3) 在物理值 $z$ 的评价是 $-2F^3=0$，矛盾。因此 $e\ne0$，并可使用 (1.4)，于是 $V_p=(e/2)(u^2+v^2)$。

分别在 $z,w$ 处评价 N 及最高式，得到
$$
e(A^2+C^2)=F^3,\qquad e(B^2+D^2)=F^3,
\tag{3.4}
$$
$$
A^3+C^3=F^3,\qquad B^3+D^3=F^3.
\tag{3.5}
$$
(1.3)、(3.4) 两边求总平方和，得
$$
e^3=F^3.
\tag{3.6}
$$
置 $\omega=e/F$，所以 $\omega^3=1$。将 M 除以 e，记为
$$
\begin{pmatrix}\alpha&\gamma\\\beta&\delta\end{pmatrix}.
$$
全部四个行、列平方和均为一，两个行立方和也为一：
$$
\alpha^2+\beta^2=\gamma^2+\delta^2
=\alpha^2+\gamma^2=\beta^2+\delta^2=1,
$$
$$
\alpha^3+\gamma^3=\beta^3+\delta^3=1.
\tag{3.7}
$$
特别 $\gamma^2=\beta^2$、$\delta^2=\alpha^2$。选 $\varepsilon,\nu\in\{1,-1\}$ 使 $\gamma=\varepsilon\beta,\delta=\nu\alpha$，允许零坐标。

若 $\varepsilon=\nu=1$，令 $s=\alpha+\beta$。由平方和与立方和得
$$
(s-1)^2(s+2)=0.
$$
另一方面，在 V 值 $u$ 评价 (3.3)，并用
$\eta Ku=e-A-B=e(1-s)$，给
$$
(1-s)^2=2(1-\omega).
\tag{3.8}
$$
$s=-2$ 会使 $\omega=-7/2$，与 $\omega^3=1$ 矛盾。故 $s=1$，继而 $\alpha\beta=0$、$\omega=1$，M/e 为恒等矩阵或交换矩阵。

若 $\varepsilon=1,\nu=-1$，(3.7) 两行相减给 $\alpha=0$，然后 $\beta=1$，得到交换矩阵；若 $\varepsilon=-1,\nu=1$，同理 $\beta=0,\alpha=1$，得到恒等矩阵。剩余 $\varepsilon=\nu=-1$ 使两个行立方和互为相反数，不可能均为一。零坐标也已包含。后二种许可矩阵也使 $s=\alpha+\beta=1$，所以同一个原 N 评价式 (3.8) 仍给 $\omega=1$。因此只有
$$
e=F,\qquad M/F=I_2\ \text{或}\ \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{3.9}
$$

现在 (3.2)、(3.8) 及相应的 $v$ 式说明 $\eta$ 与全部 E 正交。在物理四空间 $(z,w,u,v)$ 中，(3.9) 的原 Gram 只有两条独立行，故秩二。整个五空间限制型也只有秩二，违反原下界四。这排除了所有 $Hp\ne0$ 的双约化分支。

## 4. 准确保留并规范 $Hp=0$ 的 Gaussian 例外

这里只剩
$$
g\ne0,\qquad a=b=0,\qquad F^2+g^2=0.
\tag{4.1}
$$
特别 $F\ne0$。若 $e=0$，$V_p=0$，N 在物理值 $z$ 的评价为 $-Fg^2\ne0$，矛盾。所以 $e\ne0$，使用 (1.4)。

完整 N 此时为
$$
N=F y^2-F(z^2+w^2)+g(z\otimes w+w\otimes z)+2e(u^2+v^2).
\tag{4.2}
$$
在 H 值和 V 值分别评价 N，并取最高式在 H 值的评价，得到
$$
2e(A^2+C^2)=Fg^2,\qquad2e(B^2+D^2)=Fg^2,
\tag{4.3}
$$
$$
gAB=-e^3,\qquad gCD=-e^3,
\tag{4.4}
$$
$$
A^3+C^3=0,\qquad B^3+D^3=0.
\tag{4.5}
$$
(1.3) 与 (4.3) 相加给
$$
2e^3=Fg^2=-F^3.
\tag{4.6}
$$
(4.4) 故给 $AB=CD=-Fg/2\ne0$，所有四个交叉项都非零。

由 (4.5)，写
$$
C=-\zeta A,\qquad D=-\xi B,\qquad\zeta^3=\xi^3=1.
$$
(4.4) 给 $\zeta\xi=1$。两列平方和相等又给
$$
(\zeta^2-1)A^2+(\zeta-1)B^2=0.
$$
若 $\zeta\ne1$，则 $\zeta+1=-\zeta^2$，所以 $B^2=\zeta^2A^2$，可写 $B=\varepsilon\zeta A$，$\varepsilon=\pm1$。再用 $A^2+B^2=e^2$，得 $AB=-\varepsilon e^2$。与 (4.4) 比较使 $e=\varepsilon g$；(4.6) 随即给 $F=2\varepsilon g$，与 $F^2=-g^2$ 矛盾。因此
$$
\zeta=\xi=1,\qquad C=-A,\quad D=-B.
$$
这正是 (1.5)，并给 (1.6)。

## 5. 非退化性、全部尺度常数和原物理身份

对 (1.6) 的 $(z,w)$ 可逆块作 Schur 消去。它的行列式为 $-g^2=F^2$，剩余 $(y,u,v)$ 块为
$$
\begin{pmatrix}
2F&e&e\\
e&F&e-F\\
e&e-F&F
\end{pmatrix},
$$
行列式为 $2e(F-e)(2F-e)$。由 (4.6)，$e/F$ 的立方为 $-1/2$，所以它既非零、非一、也非二。这证明 (1.7)。

令 $S=u+v$、$\eta=y-S$。规范逐项给
$$
\eta\perp_K\operatorname{span}(z,w,u,v),\qquad
\eta K\eta=2(F-e)\ne0.
\tag{5.1}
$$
物理四空间本身也非退化：对 $(z,w)$ 作同一 Schur 消去，其余块在 $u+v,u-v$ 上的两个平方值为 $2e$、$2(2F-e)$，均非零。

整体加权尺度 $y\mapsto\lambda y,H\mapsto\lambda^2H,V\mapsto\lambda^3V$ 保原临界方程；在 (1.1) 中就是五列一起乘 $\lambda$。因 $F\ne0$，可选 $\lambda$ 使 $F=1$。于是剩余有限常数满足
$$
g^2=-1,\qquad e^3=-\tfrac12,\qquad
A^2+B^2=e^2,\qquad AB=-g/2.
\tag{5.2}
$$
因此必要的限制 Gram 只有这些有限平方根、三次根选择，所有选择都保留；没有假定其为实数或正数。

对任何满足这一必要规范的实际点，仍须支付完整原极线恒等式。置
$$
Y(x)=k_y(x),\ Z(x)=k_z(x),\ W(x)=k_w(x),\
U(x)=k_u(x),\ V_0(x)=k_v(x).
$$
原 N 与最高式准确是
$$
Y^2-Z^2-W^2+2gZW+2e(U^2+V_0^2)=0,
\tag{5.3}
$$
$$
Y^3-3Y(Z^2+W^2)+2(U^3+V_0^3)=0.
\tag{5.4}
$$
这里 $Y,Z,W,U,V_0$ 都仍是同一个原 K 作用后的六模式五次式；$Z,W,U,V_0$ 对应四个真实不同物理点，(5.1) 也须保持。不能把满足抽象有限 Gram 的任意五列当成原临界点。

本稿的排除与规范只使用完整原梯度的显示必要后果；没有未执行的大矩阵证书，也不重新运行旧接触门。式 (5.3)—(5.4) 在原物理数据上是否还有解，是该本质五维层准确保留的缺口。本质四维、rankH≥3、原匹配 Bell 的全局自然幂及普通 ISP 完成标准均不因本文而关闭。

**后续完整闭合（2026-11-26）：** [原两个H值方程的17矛盾](R150-appendix-rank-two-second-and-third-cumulants-have-essential-dimension-at-most-four.md)现已排尽最后双约化Gaussian规范，整个rankH=rankV=2的本质维数至多四。本文必要归约保持有效；旧规范不再需要额外物理投影消元。
