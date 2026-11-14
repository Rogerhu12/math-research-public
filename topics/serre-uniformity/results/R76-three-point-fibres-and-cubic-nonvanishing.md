# R76：三点纤维界与三次环类周期的扩大非消失范围

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文独立证明同一四元数理想类中的三个同取向 CM 嵌入必须满足一个线性判别式下界，再用已发表的 Cai–Shu–Tian 公式接到实际小惯性分支。一般主界为 $M<16p/7$，在 $(\frac{-7}{p})=1$ 时加强为 $M<8p/3$；实际小惯性另有 $p\equiv2\pmod3$，用整格判别式可在两个明确子类中再扩至 $M<3p$。它扩大 R66 的 $M<p$ 非消失范围；仍未给变化的 $M$ 上界，未排除 exceptional 分母，也不处理完整惯性分支，主问题未完成。

## 1. 结论与适用对象

设 $\mathcal O$ 是虚二次域 $K$ 中的序，
$$
\operatorname{disc}(\mathcal O)=-M,\qquad M>0,
$$
$p>3$ 为在 $K$ 惰性的素数，且 $p\nmid M$。令 $B=B_{p,\infty}$ 为恰在 $p,\infty$ 分歧的四元数代数。固定嵌入 $K\hookrightarrow B$ 及极大序 $R\subset B$，满足
$$R\cap K=\mathcal O.$$
记 $\mathrm{Cls}(R)$ 为局部主右 $R$ 理想的左 $B^\times$ 等价类集合。考察
$$
\varphi:\operatorname{Pic}(\mathcal O)\longrightarrow\mathrm{Cls}(R),
\qquad [\mathfrak a]\longmapsto[\mathfrak a R].
\tag{76.1}
$$
这里 $\operatorname{Pic}(\mathcal O)$ 只包含可逆 proper 分式理想类。

**定理 76.1（三点界）。** 下列任一条件成立时，$\varphi$ 的每个纤维至多含两个理想类：
$$
\boxed{M<\frac{16}{7}p;}
\tag{76.2}
$$
或
$$
\boxed{\left(\frac{-7}{p}\right)=1,\qquad M<\frac83p.}
\tag{76.3}
$$
结论与 $R$ 的选择无关。证明不假设 $h_K=1$，也不要求 $\mathcal O$ 为极大序。

**定理 76.2（三次非消失）。** 设 $\eta$ 是导子恰为 $c$、阶恰为 $3$ 的原始环类字符，$\mathcal O=\mathbb Z+c\mathcal O_K$，因而
$$M=|D_K|c^2.$$
在定理 76.1 的任一范围内，或在 §5.3 推论 76.1a 的范围内，存在水平 $p$、权 $2$、平凡 nebentype 的归一化新形式 $g$，使
$$
\boxed{L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.}
\tag{76.4}
$$
这里使用酉自守归一化。这个结论允许 $K,c,\eta$ 同时变化。

定理 76.1 的证明在 §§2–5 完整给出。定理 76.2 仅另用已发表的素水平 Brandt 模谱分解和 Cai–Shu–Tian (2014), Theorem 1.2；适用条件在 §6 逐项说明。

## 2. 一个纤维中的同取向最优嵌入

这一节给出理想类到嵌入共轭类的注入，特别处理 $p$ 处取向。不能任意将某个嵌入与它的二次共轭互换。

### 2.1 将所有局部理想同时规范到 $p$ 处单位理想

固定 $\varphi$ 的一个非空纤维，取其中代表 $\mathfrak a_0$，并置
$$J=\mathfrak a_0R,\qquad S=\mathcal O_L(J).$$
由于 $p\nmid M$，$\mathcal O_p=\mathcal O_{K_p}$ 为不分歧二次扩张的整数环。每个可逆分式 $\mathcal O$ 理想在 $p$ 的局部化都形如 $p^n\mathcal O_p$。将其乘以有理数 $p^{-n}$ 不改变理想类。因此可以对纤维中的每个类分别选代表 $\mathfrak a$，使
$$
\mathfrak a_p=\mathcal O_p,\qquad
(\mathfrak aR)_p=R_p,\qquad J_p=R_p.
\tag{76.5}
$$

对每个这样的 $\mathfrak a$，同纤维条件给 $b_{\mathfrak a}\in B^\times$，满足
$$b_{\mathfrak a}\mathfrak aR=J.$$
由 (76.5)，在 $p$ 处有 $b_{\mathfrak a}R_p=R_p$，故
$$b_{\mathfrak a}\in R_p^\times.$$
输运原来的嵌入，定义
$$
\iota_{\mathfrak a}:K\hookrightarrow B,\qquad
\iota_{\mathfrak a}(x)=b_{\mathfrak a}x b_{\mathfrak a}^{-1}.
\tag{76.6}
$$
其 $\mathcal O$ 像在 $S$ 中，且为最优嵌入。确实，任意有限素数 $q$ 处可写
$$\mathfrak a_q=t_q\mathcal O_q,\qquad t_q\in K_q^\times,$$
于是
$$
\mathcal O_L(\mathfrak aR)_q=t_qR_qt_q^{-1},
\qquad
K_q\cap t_qR_qt_q^{-1}=\mathcal O_q.
$$
再由 $b_{\mathfrak a}$ 共轭即可。

### 2.2 取向相同

令 $\mathfrak P$ 为 $S$ 上方唯一的两边素理想：其在 $p$ 的局部化是极大序 $S_p=R_p$ 的 Jacobson 根，而在 $q\ne p$ 的局部化为 $S_q$。局部除法代数结构给
$$
S/\mathfrak P\simeq\mathbb F_{p^2},\qquad
\mathfrak P^2=pS.
\tag{76.7}
$$
后一个等式在 $p$ 处是四元数除法极大序的标准局部等式；在 $q\ne p$ 处两边均为 $S_q$。

每个 $b_{\mathfrak a}$ 在 $p$ 处是单位，而 $S/\mathfrak P$ 交换。因此 (76.6) 在剩余域上诱导同一个映射
$$\mathcal O_p/p\mathcal O_p\longrightarrow S/\mathfrak P.$$
这就是下文所用的共同 $p$ 取向。因 $p\nmid2M$，$\sqrt{-M}$ 的两个取值在剩余域不同；故不能为简化几何而独立翻转某一个嵌入的符号。

### 2.3 纤维类到 $S^\times$ 共轭类的注入

先记录
$$
\mathfrak aR\cap K=\mathfrak a.
\tag{76.8}
$$
这可逐素数检验：
$$
t_qR_q\cap K_q=t_q(R_q\cap K_q)=t_q\mathcal O_q=\mathfrak a_q.
$$

设 $\iota_{\mathfrak b}=u\iota_{\mathfrak a}u^{-1}$，其中 $u\in S^\times$。则
$$
y=b_{\mathfrak b}^{-1}u b_{\mathfrak a}
$$
中心化 $K$。二次极大交换子域在 $B$ 中的中心化子就是自身，故 $y\in K^\times$。同时
$$
y(\mathfrak aR)
=b_{\mathfrak b}^{-1}u(b_{\mathfrak a}\mathfrak aR)
=b_{\mathfrak b}^{-1}uJ
=b_{\mathfrak b}^{-1}J
=\mathfrak bR.
\tag{76.9}
$$
按 (76.8) 与 $K$ 相交，得到 $y\mathfrak a=\mathfrak b$。所以 $[\mathfrak a]=[\mathfrak b]$。

因此：

> 一个纤维中的不同理想类，在同一极大序 $S$ 中给出两两不被 $S^\times$ 共轭的最优嵌入；这些嵌入在 $p$ 处有同一取向。

## 3. 将三点碰撞化为有限种欧氏三角形

反设某一纤维含三个不同类，并由 §2 取得相应嵌入 $\iota_0,\iota_1,\iota_2$。写
$$
\mathcal O=\mathbb Z[\omega],\qquad
\omega=\frac{t+\sqrt{-M}}2,\qquad t\in\{0,1\},
$$
其中 $t\equiv M\pmod2$。置
$$
\omega_i=\iota_i(\omega),\qquad
v_i=\omega_i-\frac t2.
$$
$B^0\otimes_{\mathbb Q}\mathbb R$ 是三维欧氏空间，内积取
$$
\langle x,y\rangle=-\frac12\operatorname{Tr}(xy)
\quad (x,y\in B^0\otimes\mathbb R).
$$
其平方范数即 reduced norm。于是
$$
\operatorname{Tr}(v_i)=0,\qquad
\operatorname N(v_i)=\frac M4.
\tag{76.10}
$$
三个点两两不同；它们不共线，因为直线与球面至多交于两点。

共同取向给
$$
\omega_i-\omega_j\in\mathfrak P.
$$
所以各边长平方满足
$$
0<\operatorname N(\omega_i-\omega_j)\in p\mathbb Z,
\qquad
\operatorname N(\omega_i-\omega_j)\le M.
\tag{76.11}
$$
第一条由 $\mathfrak P$ 的局部 norm 赋值给出，第二条为半径 $\sqrt M/2$ 的球面两点之间的距离界。

在本节以后所需的 $M<8p/3$ 范围中，特别有 $M<3p$，每条边长平方只能为 $p$ 或 $2p$。忽略重标号，只有四种可能：
$$
(p,p,p),\quad(p,p,2p),\quad(p,2p,2p),\quad(2p,2p,2p).
\tag{76.12}
$$
接下来的两个单位论证排除前两种；它们利用 (76.7)，不只是实旋转的存在性。

## 4. 两种小三角形产生整单位共轭

### 4.1 等边型 $(p,p,p)$

令
$$a=\omega_1-\omega_0,\qquad b=\omega_2-\omega_0.$$
此时
$$
\operatorname N(a)=\operatorname N(b)=\operatorname N(a-b)=p.
$$
由于 $a,b\in\mathfrak P$ 且为纯四元数，
$$
\beta=a^{-1}b=-\frac{ab}{p}\in S,
\qquad
\operatorname N(\beta)=1.
\tag{76.13}
$$
极大序在标准共轭下稳定，故 $\beta^{-1}=\overline\beta\in S$，即 $\beta\in S^\times$。

恒等式
$$
\operatorname N(a-b)=\operatorname N(a)+\operatorname N(b)+\operatorname{Tr}(ab)
$$
给 $\operatorname{Tr}(ab)=-p$，因此
$$\operatorname{Tr}(\beta)=1,\qquad \beta^2-\beta+1=0.$$
直接用 $a^2=b^2=-p$ 和 $ab+ba=-p$ 计算可得
$$
\beta a\beta^{-1}=-b,\qquad
\beta b\beta^{-1}=a-b.
\tag{76.14}
$$

令
$$c=\omega_0+\frac{a+b}{3}.$$
因 $\operatorname N(v_0+a)=\operatorname N(v_0+b)=\operatorname N(v_0)$，
$$
\langle v_0,a\rangle=\langle v_0,b\rangle=-p/2.
$$
又 $\langle a,b\rangle=p/2$，故 $c$ 的纯部与 $a,b$ 都正交。纯四元数中，这使它与 $ab$ 的纯部平行，从而 $c$ 与 $\beta$ 交换。由 (76.14)，
$$
\beta\omega_0\beta^{-1}
=c-\frac{-b+(a-b)}3
=\omega_0+b
=\omega_2.
\tag{76.15}
$$
$\omega$ 生成 $\mathcal O$，故 $\iota_0,\iota_2$ 被整单位共轭，与 §2.3 矛盾。

### 4.2 直角型 $(p,p,2p)$

取 $\omega_0$ 为两条平方长度 $p$ 的边的共同端点，仍写 $a=\omega_1-\omega_0,b=\omega_2-\omega_0$。现在
$$
\operatorname N(a)=\operatorname N(b)=p,\qquad
\operatorname N(a-b)=2p,
$$
故 $ab+ba=0$。同一公式
$$\beta=-ab/p\in S^\times$$
给
$$
\operatorname{Tr}(\beta)=0,\quad\beta^2=-1,\quad
\beta a\beta^{-1}=-a,\quad
\beta b\beta^{-1}=-b.
\tag{76.16}
$$
令 $c=\omega_0+(a+b)/2$。与上一节相同的等范数计算给 $c$ 的纯部垂直 $a,b$，故 $c$ 与 $\beta$ 交换。于是
$$
\beta(\omega_0+a)\beta^{-1}
=c-\frac{a-b}{2}
=\omega_0+b.
\tag{76.17}
$$
这次 $\iota_1,\iota_2$ 被整单位共轭，同样矛盾。

这两个论证并未要求 $c\in S$：$c$ 只用于实几何恒等式；实际用于共轭的 $\beta$ 已由 $\mathfrak P^2=pS$ 严格证明属于 $S^\times$。

## 5. 剩余两种三角形及 $-7$ 加强

### 5.1 无附加条件的 $16/7$ 界

三点 $v_i$ 的仿射平面与 (76.10) 的球面相交成圆。该圆是三角形的外接圆，其半径平方不超过 $M/4$。

若边长平方为 $(p,2p,2p)$，以平方长度 $p$ 的边为底，三角形高的平方为 $7p/4$，面积平方为 $7p^2/16$。外接圆半径平方为
$$
\frac{p(2p)(2p)}{16(7p^2/16)}
=\frac{4p}{7}.
$$
因此
$$M\ge\frac{16p}{7}.\tag{76.18}$$
若边长平方全为 $2p$，外接圆半径平方为 $2p/3$，因而
$$M\ge\frac{8p}{3}.\tag{76.19}$$

当 $M<16p/7$ 时，(76.12) 中前两种已由 §4 排除，后两种被 (76.18)–(76.19) 排除。这证明定理 76.1 的第一部分。

### 5.2 当 $p$ 在 $\mathbb Q(\sqrt{-7})$ 分裂

现在假设 $M<8p/3$，并考察唯一还可能存在的 $(p,2p,2p)$ 型。选两个从同一顶点发出的边 $a,b$，使
$$
\operatorname N(a)=p,\quad
\operatorname N(b)=2p,\quad
\operatorname N(a-b)=2p.
$$
再次由 (76.7)，
$$
\beta=-ab/p\in S,\qquad
\operatorname N(\beta)=2,\qquad
\operatorname{Tr}(\beta)=1.
\tag{76.20}
$$
故 $\beta$ 满足不可约多项式
$$X^2-X+2,$$
其判别式为 $-7$。这给出 $\mathbb Q(\sqrt{-7})\hookrightarrow B$。

若 $(\frac{-7}{p})=1$，在 $p$ 局部化后将得到
$$\mathbb Q_p\times\mathbb Q_p\hookrightarrow B_p.$$
但 $B_p$ 是除法代数，不能含非平凡幂等元；矛盾。因此 (76.20) 的三角形也被排除，证明 (76.3)。

在 $(\frac{-7}{p})=-1$ 的情形，本文没有排除这种三角形；不能无条件把 $16/7$ 改为 $8/3$。

### 5.3 整格判别式与实际小惯性中的 $3p$ 界

保留三个同纤维的点，令
$$L=\mathbb Z\langle1,\omega_0,a,b\rangle\subset S.$$
极大序 $S$ 的 reduced discriminant 为 $p$，故其 reduced-trace 配对的行列式为 $-p^2$。若四个向量线性独立，$L$ 是满秩整数格，从而
$$
\det\bigl(\operatorname{Tr}(x_ix_j)\bigr)_{x_i\in(1,\omega_0,a,b)}
=-p^2[S:L]^2.
\tag{76.27}
$$
若不独立，这个行列式为零；该退化情形应单独处理，不能称 $[S:L]=0$。

用 $\omega_0=t/2+v_0$ 消去第一行列的标量部分，迹行列式等于 $-16$ 乘以 $(v_0,a,b)$ 的欧氏 Gram 行列式。对于 $(p,2p,2p)$ 型，这个 Gram 矩阵为
$$
\begin{pmatrix}
M/4&-p/2&-p\\
-p/2&p&p/2\\
-p&p/2&2p
\end{pmatrix}.
$$
直接展开其行列式，得到迹行列式
$$-p^2(7M-16p).$$
因此不论是否退化，该边型都必须满足
$$
\boxed{7M-16p\in\{n^2:n\in\mathbb Z_{\ge0}\}.}
\tag{76.28}
$$
在满秩情形 $n=[S:L]$；退化情形右边为零。

对于 $(2p,2p,2p)$ 型，Gram 矩阵为
$$
\begin{pmatrix}
M/4&-p&-p\\
-p&2p&p\\
-p&p&2p
\end{pmatrix},
$$
迹行列式等于 $-4p^2(3M-8p)$。满秩时 (76.27) 使 $[S:L]$ 为偶数；退化时仍为零。因此该边型必须满足
$$
\boxed{3M-8p\in\{n^2:n\in\mathbb Z_{\ge0}\}.}
\tag{76.29}
$$

现在额外假设 $p\equiv2\pmod3$。式 (76.29) 的左边模 $3$ 等于 $p\equiv2$，不可能为平方。于是当 $M<3p$ 时，§3 的全部边型中只可能剩下 $(p,2p,2p)$，而它必须同时满足 (76.28) 以及 $\mathbb Q(\sqrt{-7})\hookrightarrow B$。

**推论 76.1a。** 设 $p\equiv2\pmod3$、$M<3p$。若
$$
7M-16p\notin\{n^2:n\in\mathbb Z_{\ge0}\},
\tag{76.30}
$$
或 $(\frac{-7}{p})=1$，则 $\varphi$ 每个纤维至多两个类。特别，下列两个明确子类均可把定理 76.1 的界扩大到 $M<3p$：
$$
\boxed{\left(\frac{-7}{p}\right)=1}
\quad\text{或}\quad
\boxed{M\equiv1\pmod3.}
\tag{76.31}
$$
第二个子类来自 $7M-16p\equiv M-p\equiv2\pmod3$。这个加强使用 $p\equiv2\pmod3$，不属于对任意惰性 $p$ 无附加同余条件的定理 76.1。

## 6. 三次颜色不可能在小纤维中平衡

令 $\eta:\operatorname{Pic}(\mathcal O)\twoheadrightarrow\mu_3$。在 Brandt 模中定义
$$
P_\eta
=\sum_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O)}
  \eta(\mathfrak a)^{-1}[\varphi(\mathfrak a)]
\in\mathbb C[\mathrm{Cls}(R)].
\tag{76.21}
$$
因 $\eta$ 非平凡，
$$\deg P_\eta=\sum_{[\mathfrak a]}\eta(\mathfrak a)^{-1}=0.$$
某个纤维中三个颜色的数量为 $n_0,n_1,n_2$ 时，其系数为
$$n_0+n_1\zeta_3+n_2\zeta_3^2.$$
利用 $\zeta_3^2=-1-\zeta_3$ 及 $\{1,\zeta_3\}$ 在 $\mathbb Q$ 上线性独立，该系数为零当且仅当
$$n_0=n_1=n_2.\tag{76.22}$$
一个非空且大小至多为 $2$ 的纤维不可能满足 (76.22)。定理 76.1 或推论 76.1a 因而给
$$P_\eta\ne0.\tag{76.23}$$

注意，这里证明的是**三种颜色不能同时平衡**；没有把某个单独颜色和的非零，当成足够的整体模素数论证。此处在特征零中讨论有限纤维，与 R72 的 exceptional 圆分素理想问题不同。

### 6.1 已发表谱分解的精确用途

素水平的 Eichler–Jacquet–Langlands 对应把
$$\mathbb C[\mathrm{Cls}(R)]^0$$
分解为水平 $p$、权 $2$ 新形式的特征线。可参见 Gross (1987), §5，特别 pp.143–144 的 Hecke 模同构及 Eisenstein/尖点谱分解；具体 Brandt 模归一化亦见 Cai–Shu–Tian (2014), pp.2526–2527。

这里不遗漏 Eisenstein 方向：若 $S_x$ 为类 $x$ 的左序、$w_x=|S_x^\times/\{\pm1\}|$，Hermitian 配对为
$$
\left\langle\sum a_x[x],\sum b_x[x]\right\rangle
=\sum_x a_x\overline{b_x}w_x.
$$
Eisenstein 向量与 $\sum_x w_x^{-1}[x]$ 成比例，其正交补恰为普通次数零空间。$P_\eta$ 已在此空间中。又 $S_2(\mathrm{SL}_2(\mathbb Z))=0$，素水平没有需要另行剔除的权二旧形式。

因此 (76.23) 给某个 $g$，使其特征线上的正交投影 $P_\eta^g$ 非零。

### 6.2 Cai–Shu–Tian, Theorem 1.2

采用其 $N=p$、虚二次判别式 $D_K$、原始环类导子 $c$。条件逐项为：

- $(c,p)=1$，由 $p\nmid M$ 给出；
- $p\nmid D_K$ 且在 $K$ 惰性；
- 其条件 (ii) 的分歧集合为 $\{p,\infty\}$，基数为偶数；
- 四元数序的判别式为 $p$，即这里的极大序，且 $R\cap K=\mathcal O_c$；
- $\eta$ 的导子恰为 $c$，故是该公式要求的原始环类字符。

其 Theorem 1.2 的因子在这里化为
$$
L(1,g,\eta)
=\frac{8\pi^2(g,g)_{\Gamma_0(p)}}{u^2\sqrt M}
  \langle P_\eta^g,P_\eta^g\rangle,
\qquad u=|\mathcal O_c^\times/\{\pm1\}|.
\tag{76.24}
$$
系数严格正，右边由 $P_\eta^g\ne0$ 非零。这证明定理 76.2。式 (76.24) 是该论文的算术中心 $1$；它对应 (76.4) 的酉中心 $1/2$，与 R66 (7.1) 的归一化相同。

本证明只从已发表公式调用“非零投影给非零中心值”，并独立给出投影不全为零的三点几何理由。未使用 Studnia submitted 论文中的命题作为证明输入。

## 7. 接回实际异常椭圆曲线

采用 R66 的实际完整非分裂正规化子像，且
$$
\rho_{E,p}(I_p)\subsetneq C.
$$
R66 已独立给出
$$
p\equiv2,5\pmod9,\qquad
\rho_{E,p}(I_p)=C^3,
$$
三次商字符 $\eta$ 为原始反圆分环类字符，其导子 $c=c_\eta$ 满足
$$
M=|D_K|c^2,\qquad p\nmid M.
$$
商域 $K$ 中的 $p$ 惰性。因此定理 76.2 可直接用于这条真实 $E$ 所给的字符，无须固定某条 CM 参考曲线。

**推论 76.3。** 在实际小惯性分支中，若
$$
\boxed{p>\frac7{16}|D_K|c_\eta^2,}
\tag{76.25}
$$
或
$$
\boxed{
\left(\frac{-7}{p}\right)=1,\qquad
p>\frac38|D_K|c_\eta^2,
}
\tag{76.26}
$$
或
$$
\boxed{
p>\frac13|D_K|c_\eta^2,\qquad
\left[
\left(\frac{-7}{p}\right)=1\quad\text{或}\quad
7|D_K|c_\eta^2-16p\notin\{n^2:n\in\mathbb Z_{\ge0}\}
\right],
}
\tag{76.32}
$$
则存在 R69 所需的水平 $p$ 新形式 $g$。因而：

1. R69 对任意配对乘子 $\alpha$ 构造的实际扭曲完整水平曲线 $X_E^\alpha(p)$ 有非零秩零商；其有理点群有限性的输入是已发表 Bertolini–Darmon 定理。
2. R72 的最优商、整微分及尖点形式浸入证明适用。对任意 $F/\mathbb Q$ 满足 $F[p]\simeq E[p]$，每个 $j(F)$ 分母素数 $\ell$ 都必须满足
   $$\ell\text{ exceptional for }p,\qquad
   \ell\equiv\chi_K(\ell)\pmod p.$$
   这包括 $F=E$。

上述两项分别是 R69、R72 已证结果的直接代入；本文新增的是提供非零 $L$ 值的更大参数范围。实际分支满足 $p\equiv2\pmod3$，所以 (76.32) 可用；特别当 $(\frac{-7}{p})=1$ 或 $|D_K|c_\eta^2\equiv1\pmod3$ 时，只需 $p>M/3$。后一个子类也可写为 $|D_K|\equiv1\pmod3$ 且 $3\nmid c_\eta$。

也可取逆否命题：若实际小惯性分支存在一个非 exceptional 的 $j(E)$ 分母素数，则必有
$$
M\ge\frac{16p}{7},
$$
并在 $(\frac{-7}{p})=1$ 或 $M\equiv1\pmod3$ 时必有 $M\ge3p$。一般地，若同时有 $M<3p$，则必须满足
$$
\left(\frac{-7}{p}\right)=-1,\qquad 7M-16p=n^2
$$
对某个 $n\in\mathbb Z_{\ge0}$ 成立（本题 $p>37$，没有 $p=7$ 的分歧例外）。这些都是真实导子的必要条件，但没有给 $M$ 上界。

## 8. 精确边界与来源

本结果在原有的两点注入界之外，利用了“同一纤维三个点”的约束。它没有声称大判别式序的 CM 约化总有小纤维；若 $M$ 继续增大，(76.11) 允许更多边范数，本文的四种三角形分类便不再穷尽。

同样，原始三次环类字符的导子仍可变化。R66 §4 已说明仅靠类数一、三次反圆分、$p$ 不分歧，不能给这个导子上界。因此即使 (76.25) 比 $p>M$ 覆盖更大范围，也不能据此完成统一排除。

文中不采用未经证明的 $p\gg\sqrt M$ 非消失范围。这里得到的是严格证明的线性界。三点纤维界还与环类多项式模 $p$ 的重根现象相关，但证明 (76.4) 直接使用理想类映射 (76.1)，不需要把 CM 约化对应或“多项式非立方”额外当作黑箱。

### 已发表输入

- B. H. Gross, *Heights and the special values of L-series*, in **Number theory (Montreal, Que., 1985)**, CMS Conference Proceedings **7** (1987), 115–187，§5，pp.140–144。用途：素水平 Brandt 模的完整谱分解。[原文扫描](https://wstein.org/papers/bib/Gross-Heights_and_the_Special_Values_of_L-series.pdf)。本次通过原文网页检索核对 p.144 的谱分解，不下载 PDF。
- Li Cai, Jie Shu, Ye Tian, *Explicit Gross–Zagier and Waldspurger formulae*, **Algebra & Number Theory 8** (2014), no.10, 2523–2572，Theorem 1.2，pp.2525–2527。[DOI](https://doi.org/10.2140/ant.2014.8.2523)，[出版社原文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)。用途：原始环类字符的精确非零周期—中心值公式及相容序的存在性。

### 仓库中已证明的接口

- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际小惯性字符、精确 $M$、原 $p>M$ 范围。
- [R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)：实际秩零商及已发表的有理点有限性输入。
- [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：最优商整微分、尖点形式浸入与 exceptional 分母必要条件。

§§2–5 的理想注入、取向、单位共轭和三角形计算，以及 §6 的颜色计数，为本文完整展开的独立证明。
