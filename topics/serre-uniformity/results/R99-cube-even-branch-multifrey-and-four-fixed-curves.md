# R99：立方分母的 III 偶分支，多 Frey 降至四条固定非 CM 曲线

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明，含精确有限计算。** 本文只处理 R19 的 $Z=Y^3$、族 III 且 $X$ 偶的实际分支。其原有同余 $E[p]\simeq A[p]$ 与一个实二次 $\mathbb Q$-曲线联合，将全部 $p>37$ 归约到四条固定非 CM 曲线。实际分支并未据此排除；不能把四个存活新形式删去，也不能将这一子分支写成 Serre 一致性已完成。

## 1. 结论及完整输入

令 $A/\mathbb Q:y^2=x^3-x$。设 $p>37$ 为素数，$(X,W,Z)$ 是 [R19](R19-converse-fermat-fixed-cm.md) 族 III 的实际非平凡解，$X$ 偶且 $Z=Y^3$。根据 R19 及[完整四次式参数化](../notes/2026-11-12-cube-denominator-primitive-quartics.md)，存在
$$
a,b>0,\quad a,b\text{ 奇},\quad (a,b)=1,\quad 3\nmid a,\quad 3\mid b,
\quad |Y|>1,\quad (Y,6p)=1,
\tag{99.1}
$$
使得
$$
h=\frac{a^2+3b^2}{2}\equiv2\pmod4,
\qquad a^4-3h^2=Y^p,
\qquad (a,h)=(a,Y)=(h,Y)=1.
\tag{99.2}
$$
更准确地，令
$$
F=a^4-18a^2b^2-27b^4,\quad T=Y^p=F/4,
$$
则
$$
X=T+9a^2b^2,\qquad
W=\pm\frac{ab(a^4+27b^4)}4,
\qquad
E:y^2=x^3-4Xx-16W,\qquad E[p]\simeq A[p].
\tag{99.3}
$$
两个 $W$ 符号均保留，$Y$ 也可为负。由 R19 已证明的排除，必有 $p\equiv3\pmod4$。以下实二次域与 R19 的虚二次 Cartan 商域不同：
$$
K=\mathbb Q(r),\quad r^2=3,\quad \mathcal O_K=\mathbb Z[r],
\quad u=1+r,\quad \pi=r-1,\quad \mathfrak p_2=(\pi).
$$
定义
$$
B(a,h):y^2=x^3+4ax^2+2(a^2+rh)x,\qquad
B_0:y^2=x^3+4x^2+(2+r)x.
\tag{99.4}
$$
对 $y^2=x^3+Ax^2+Bx$，本文的 $d$ 次二次扭曲约定为
$$y^2=x^3+dAx^2+d^2Bx.$$

**定理 99.1。** 对每一个满足 (99.1)–(99.3) 的实际分支，存在 $d\in\{1,-1,2,-2\}$ 使得
$$
\boxed{B(a,h)[p]\simeq B_0^{(d)}[p]\quad\text{作为 }G_K\text{ 的 }\mathbb F_p\text{ 表示。}}
\tag{99.5}
$$
四条右端曲线均非 CM。证明包括全部 $p>37$，不遗漏用于筛选的素数恰等于 $p$ 的情形。

## 2. 一个显式辅助角色，以及真正的下降因子

令
$$
\chi:G_K\longrightarrow\{\pm1\}
\quad\text{对应 }K(\sqrt u)/K,\qquad C=B(a,h)^{(u)}.
\tag{99.6}
$$
因此 $\rho_{C,\ell}=\rho_{B,\ell}\otimes\chi$。这一定义没有另外乘以从 $\mathbb Q$ 经范数拉回的 Dirichlet 角色。

### 2.1 $\chi$ 的准确二进导子

若 $\beta^2=1+r$，则
$$\beta^4-2\beta^2-2=0.$$
此多项式在 $2$ 处 Eisenstein，故 $\beta$ 是该四次局部扩张的素元，$\mathbb Z_2[\beta]$ 为其整数环；多项式判别式为
$$-4608=-2^9\cdot3^2.$$
在奇素数处，$u$ 的赋值为零，二次扩张不分歧。在 $3$ 处全域判别式已有 $D_K^2=12^2$ 的 $3^2$ 因子，故没有整基指标造成的额外削减。由判别式塔式
$$
\operatorname{Norm}_{K/\mathbb Q}\mathfrak d_{K(\sqrt u)/K}
=\frac{4608}{12^2}=32,
$$
得到
$$
\mathfrak d_{K(\sqrt u)/K}=\mathfrak p_2^5,\qquad
\boxed{\mathfrak f_\chi=\mathfrak p_2^5.}
\tag{99.7}
$$
第二个等式是二次扩张的导子–判别式公式。在两个实嵌入处，$u$ 的符号分别为正、负；所以 $\chi$ 的无穷分量分别平凡、符号角色。

### 2.2 在 $K$ 上定义的二同源

设横线表示 $K/\mathbb Q$ 的非平凡作用。具有核 $\{O,(0,0)\}$ 的正规化二同源把 $B$ 送到
$$
y^2=x^3-8ax^2+8(a^2-rh)x=\overline B^{(-2)}.
$$
正规化指不变微分的拉回因子为 $1$；例如横坐标为 $x+4a+2(a^2+rh)/x$，纵坐标取使微分因子为 $1$ 的符号。

扭曲 $u$ 后先得到 $C\to\overline B^{(-2u)}$。由于
$$\overline u=1-r=-2/u,\qquad (-2u)/\overline u=u^2,$$
再作 $(x,y)\mapsto(x/u^2,y/u^3)$，得到一个 **在 $K$ 上定义** 的同源
$$
\mu:C\longrightarrow\overline C,\qquad
\mu^*\omega_{\overline C}=u\omega_C,\qquad
\overline\mu\circ\mu=[-2].
\tag{99.8}
$$
最后一式由次数 $4$ 及微分因子 $u\overline u=-2$ 得出；特征零的椭圆曲线端同态由其微分确定。

置 $s=\sqrt{-2}$，$F_0=\mathbb Q(s)$。对任意 $g\in G_{\mathbb Q}$ 定义
$$
\widetilde\rho(g)=
\begin{cases}
\rho_C(g),&g\in G_K,\\
s\mu^{-1}\circ g,&g\notin G_K.
\end{cases}
\tag{99.9}
$$
这里第二行中 $g$ 先将 $V_\ell(C)$ 送到 $V_\ell(\overline C)$，再应用 $\mu^{-1}$；系数扩到 $F_0$。对于两个不属于 $G_K$ 的元素，乘法所产生的 $\mu^{-1}\overline\mu^{-1}=[-2]^{-1}$ 正好由 $s^2=-2$ 抵消。其余乘法关系直接由 $\mu$ 在 $K$ 上定义得到。因此 (99.9) 是 $G_{\mathbb Q}$ 的表示。这里没有假设存在一个阶二的 $G_{\mathbb Q}$ 元素在实域 $K$ 上非平凡。

由 Weil 配对，$\det(\mu)=2$；第二行的标量因子行列式为 $s^2=-2$。所以
$$
\det\widetilde\rho=\chi_{12}\chi_{\rm cyc},\qquad
\widetilde\rho^{\,s\mapsto-s}
=\widetilde\rho\otimes\chi_{12},
\tag{99.10}
$$
其中 $\chi_{12}$ 是 $K/\mathbb Q$ 的二次角色。复共轭固定 $K$，故该表示为奇表示。其 nebentypus 正是 $\chi_{12}$；不能在下降时遗漏 (99.9) 的 $\sqrt{-2}$ 因子，也不能将它误写成平凡 nebentypus。

## 3. 实际曲线 $C$ 的全部导子

$B$ 的不变量为
$$
c_4(B)=32(5a^2-3rh),\qquad
\Delta(B)=512(a^2+rh)^2(a^2-rh).
\tag{99.11}
$$

### 3.1 $2$ 处的完整最小模型

以 $v=v_{\mathfrak p_2}$ 归一化，$v(2)=2$、$v(u)=1$。由于 $a$ 奇、$h$ 偶，(99.11) 给
$$v(\Delta(B))=18,\quad v(\Delta(C))=24,\quad v(c_4(C))=12.$$
在 $C$ 上作 $x=\pi^2x',y=\pi^3y'$，所得整模型的非零系数为
$$
a'_2=(10+6r)a,\qquad
a'_4=(26+15r)(a^2+rh).
\tag{99.12}
$$
其判别式赋值为 $12$。模 $\mathfrak p_2$ 的唯一奇点在 $(x',y')=(1,0)$。平移 $x'=x''+1$ 后
$$a''_6=1+a'_2+a'_4\equiv1+r\pmod{2\mathcal O_K}.$$
因为 $v(1+r)=1$ 而 $v(2)=2$，故 $v(a''_6)=1$。Tate 算法的 II 型步骤直接说明该模型最小，Kodaira 型为 II。Ogg 公式因特殊纤维只有一个几何不可约分量而给
$$
\boxed{v_{\mathfrak p_2}(\mathfrak N_C)=12.}
\tag{99.13}
$$
这是对全部 (99.1) 参数的证明，不是从一个样本外推。

### 3.2 $3$、分母素数及 $p$ 处

在 $\mathfrak p_3=(r)$，因 $3\nmid a$，曲线 $B,C$ 都好约化；$u\equiv1\pmod{\mathfrak p_3}$。剩余曲线为
$$y^2=x^3+\overline a x^2+2x,$$
其中 $\overline a=\pm1$，故其迹分别为 $-2,+2$。

若有理素数 $q\mid Y$，则 $q\ge5$，而 $(a,h)=1$ 说明 $a,h$ 都为 $q$ 单位。由 $a^4\equiv3h^2\pmod q$，$q$ 在 $K$ 中分裂。两个共轭因子 $a^2\pm rh$ 在 $q$ 上方互素；在两个素理想处分别有乘法约化，最小判别式赋值为
$$p\,v_q(Y),\quad2p\,v_q(Y)$$
（次序依素理想而变）。相应的 $c_4$ 均为单位。角色 $\chi$ 在这里不分歧，不改变导子。

由 $(p,Y)=1$，$C$ 在 $p$ 上方好约化。因此
$$
\mathfrak N_C=\mathfrak p_2^{12}\operatorname{rad}(|Y|)\mathcal O_K.
\tag{99.14}
$$
用 Artin 导子的诱导公式与 (99.10)，
$$
\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\rho_C
\simeq\widetilde\rho\oplus(\widetilde\rho\otimes\chi_{12}),
$$
两项互为系数共轭，故导子相同。于是
$$
N(\widetilde\rho)^2=D_K^2\operatorname{Norm}\mathfrak N_C
=(768\operatorname{rad}(|Y|))^2,\qquad
N(\widetilde\rho)=768\operatorname{rad}(|Y|).
\tag{99.15}
$$

## 4. 对全部实际 $p>37$ 的绝对不可约与精确降层

### 4.1 不可约性没有留下大素数例外

$K$ 的类数为一：Minkowski 界为 $\sqrt{12}/2=\sqrt3<2$。其基本单位为 $\varepsilon=2+r$，范数为 $1$；模 $3$ 已排除范数 $-1$ 的单位。对 Freitas–Siksek (2015), Theorem 1 中的两个非恒定同源特征签名，相关单位范数给
$$
\left|N_{K/\mathbb Q}(\varepsilon^{12}-1)\right|
=7300800=2^6\cdot3^3\cdot5^2\cdot13^2.
\tag{99.16}
$$
$C$ 在 $p$ 上方好约化，$p>37$ 在 $K$ 不分歧且不整除 (99.16)。又 $\mathfrak p_3$ 主且好约化迹为 $\pm2$。该定理说明，若 $C[p]$ 可约，则
$$
p\mid\operatorname{Res}(z^2\mp2z+3,z^{12}-1)
=530784=2^5\cdot3^2\cdot19\cdot97.
\tag{99.17}
$$
两个迹符号给同一个整数。因此只可能 $p=97$，但实际 $p\equiv3\pmod4$ 排除了它。故 $C[p]$ 不可约。

由于 $K$ 全实，复共轭在 $C[p]$ 上有互异的 $1,-1$ 本征值。一个在 $\mathbb F_p$ 上不可约但非绝对不可约的二维表示，其交换域为 $\mathbb F_{p^2}$，整个像落在该域的乘法群；这里不可能含有这样的复共轭。因此 $C[p]$ **绝对不可约**，(99.9) 的模 $p$ 扩张也是绝对不可约。

### 4.2 模 $p$ 的精确层为 $768$

在 $q\mid Y$ 处，Tate 曲线惯性作用的幺幂参数由 $p$ 整除，故模 $p$ 不分歧。这里 $q$ 在 $K$ 分裂，所以下降表示也不分歧。

在 $2$ 处，$C$ 潜在好约化，其有限惯性像的阶只有素因子 $2,3$。下降表示本身的惯性像也有限：限制到 $K_{\mathfrak p_2}$ 的指数至多为 $2$，故其阶仍只有素因子 $2,3$。在系数域任意一个 $p$ 上方素理想约化时，$p>37$ 保证各 ramification group 的不变维数不变，所以精确保持特征零导子指数 $8$；不需要比较不同 $p$ 素理想的约化来推断这一点。在 $3$ 处，限制到 $K_{\mathfrak p_3}$ 好约化，下降表示的惯性商为 $C_2$，而行列式 $\chi_{12}$ 在该商非平凡。两个惯性本征值恰为 $1,-1$，故模 $p$ 的准确导子指数为 $1$。因此
$$N(\overline{\widetilde\rho})=2^8\cdot3=768.$$
在 $p$ 处，$K/\mathbb Q$ 不分歧，限制为好约化椭圆曲线的表示，故下降仍为有限平坦、Serre 权二；这也可由未分歧下降的 crystalline 性与 Hodge–Tate 权 $\{0,1\}$ 说明。

由已证明的 Serre 模性及其最优层、权形式，存在
$$
f\in S_2^{\mathrm{new}}(768,\chi_{12}),\qquad
\overline{\widetilde\rho}\simeq\overline\rho_{f,\mathfrak P},
\quad\mathfrak P\mid p.
\tag{99.18}
$$
nebentypus 的 Teichmüller 提升仍为 $\chi_{12}$。这里使用一般 nebentypus 的最优模性定理；不是把只以平凡角色表述的旧降层定理直接套到 (99.18)。参考 Khare–Wintenberger (2009), §§1、9 及其说明的 Kisin 定理；实际曲线的特征零模性也可由 (99.8) 给出的 $\operatorname{Res}_{K/\mathbb Q}C$ 的 $\mathrm{GL}_2$ 型结构得到。

## 5. 与原 $E[p]\simeq A[p]$ 联合的有限域约束

取在 $K$ 分裂的下列十一个素数：
$$\mathcal Q=\{11,13,23,37,47,59,61,71,73,83,97\}.$$
[R13](R13-denominators-for-fixed-cm-congruence.md) 给出 $q\mid Y\Rightarrow q\ge4p-1$。对每一个 $p>37$ 和 $q\in\mathcal Q$，有 $q<4p-1$，因此 $q\nmid Y$，$E,A,B,C$ 都在相关素数好约化。

**若 $q\ne p$**，原同余给 $a_q(E)\equiv a_q(A)\pmod p$。由于
$$|a_q(E)-a_q(A)|\le4\sqrt{97}<40<p,$$
得到整数等式
$$a_q(E)=a_q(A).\tag{99.19}$$
若 $q=p$，不使用 (99.19)，也不假设特征 $p$ 的 Frobenius 迹同余。

### 5.1 全部局部参数的枚举

在 $\mathbb F_q$ 上，参数变换 $(a,b)\mapsto(\lambda a,\lambda b)$ 将 $X,W$ 分别乘以 $\lambda^4,\lambda^6$，所以原 $E$ 同构不变；将辅助 $B$ 变为其 $\lambda$ 次二次扭曲，因此辅助迹的平方不变。只须遍历
$$[a:b]\in\mathbb P^1(\mathbb F_q),\qquad F(a,b)\ne0,$$
使用代表 $(a,1)$、$a\in\mathbb F_q$，以及 $(1,0)$。对每个代表按 (99.3) 计算原曲线，并仅保留 (99.19)。然后按 (99.2)、(99.4) 计算辅助迹平方，形成集合 $S_q$。

换取 $r$ 的另一个剩余平方根时，辅助曲线与原来的 $-2$ 次扭曲二同源，因此迹平方不变。换取 $W$ 的符号时原曲线作 $-1$ 次扭曲；若 $q\equiv1\pmod4$，此扭曲在剩余域平凡，若 $q\equiv3\pmod4$ 则 $a_q(A)=0$，所以条件 (99.19) 仍等价。全部符号已包括。

逐项标准库点数得到：

| $q$ | $a_q(A)$ | $S_q$ | 保留的射影参数数 |
|---|---:|---|---:|
| 11 | 0 | $0,4,16$ | 4 |
| 13 | 6 | $4,16$ | 3 |
| 23 | 0 | $0,36,64$ | 6 |
| 37 | $-2$ | $4,16,36,100,144$ | 18 |
| 47 | 0 | $0,36,64$ | 10 |
| 59 | 0 | $0,16,36,144$ | 12 |
| 61 | $-10$ | $4,16,36,100,144$ | 18 |
| 71 | 0 | $0,36,64,100,144$ | 14 |
| 73 | $-6$ | $16,64,100,196$ | 15 |
| 83 | 0 | $0,16,36,64,144,256$ | 12 |
| 97 | 18 | $36,100,324$ | 7 |

因为 $C=B^{(u)}$，其局部迹与 $B$ 的迹只差一个符号。对 $q\ne p$，(99.18) 便给出
$$a_q(f)^2\equiv s_q\pmod{\mathfrak P}\quad\text{对某个 }s_q\in S_q.$$
定义真正的整数
$$
D_q(f)=q\prod_{s_q\in S_q}
N_{\mathbb Q(f)/\mathbb Q}\bigl(a_q(f)^2-s_q\bigr),
\qquad G_f=\gcd_{q\in\mathcal Q}D_q(f).
\tag{99.20}
$$
当 $q\ne p$ 时，$p$ 整除其中一个范数；当 $q=p$ 时，前面的因子 $q$ 已保证 $p\mid D_q(f)$。所以对全部实际 $p>37$，无例外地有
$$p\mid G_f.\tag{99.21}$$
若某些 $D_q$ 为零，用通常的 $\gcd(n,0)=|n|$ 约定，所有都零时 $G_f=0$。

## 6. 精确新形式计算：六个轨道被排，四个非 CM 轨道保留

PARI/GP 的精确命令
$$\texttt{mfinit([768,2,12],0)},\qquad\texttt{mfeigenbasis}$$
给出新空间维数 $28$，共十个 Galois 轨道。这里 $12$ 表示 Kronecker 角色 $\chi_{12}$，末尾参数 $0$ 指新子空间。以下 $z$ 是系数域的生成元，编号采用证书中 PARI 2.19.0 的顺序；为避免仅依赖软件排序，同时列出定义多项式及两个系数。

| 轨道 | 系数域多项式 | $a_{11}$ | $a_{13}$ | $G_f$ | CM 域基本判别式 |
|---|---|---|---|---:|---:|
| 1 | $z^2+2$ | $-6$ | $0$ | $2^{12}$ | $-8$ |
| 2 | $z^2+2$ | $2$ | $-4$ | $0$ | 非 CM |
| 3 | $z^2+2$ | $2$ | $4$ | $0$ | 非 CM |
| 4 | $z^2+2$ | $6$ | $0$ | $2^{12}$ | $-8$ |
| 5 | $z^2+2$ | $-2$ | $4$ | $0$ | 非 CM |
| 6 | $z^2+2$ | $-2$ | $-4$ | $0$ | 非 CM |
| 7 | $z^4+1$ | $-2z^3+2z$ | $0$ | $2^{24}$ | $-8$ |
| 8 | $z^4+4z^2+1$ | $2z^2+4$ | $0$ | $2^{24}$ | $-24$ |
| 9 | $z^4-z^2+1$ | $2z^3-4z$ | $0$ | $2^{24}$ | $-24$ |
| 10 | $z^4-z^2+1$ | $0$ | $4z^3-8z$ | $2^{28}$ | $-3$ |

全部范数在实际系数域计算；即使某个 $a_q$ 恰为有理整数，也按该域的完整次数取范数。证书保留十一个 $D_q$ 的整数值，而非只保留最终 gcd。其算法是整数、有理数及数域的精确线性代数，不使用 GRH、浮点识别或预存新形式数据库。各轨道维数之和为 $6\cdot2+4\cdot4=28$，覆盖整个新空间。

由 (99.21)，轨道 $1,4,7,8,9,10$ 不可能出现。下面精确识别其余四个，而不是仅称其为“不能筛掉的形式”。

## 7. 四个存活轨道就是 $B_0$ 的四个固定扭曲

令 $C_0=B_0^{(u)}$。有
$$
\Delta(B_0)=64(2+r),\qquad j(B_0)=420032-241408r,
$$
$$
\minpoly(j(B_0))=t^2-840064t+1593413632.
\tag{99.22}
$$
所以 $B_0,C_0$ 在奇素数处处好约化。$C_0$ 也有 (99.8) 的同源与 (99.9) 的下降。

在 $\mathfrak p_2$，对 $d=1,-1,2,-2$ 逐项使用 Tate 算法，得到

| $d$ | $v_{\mathfrak p_2}\mathfrak N_{C_0^{(d)}}$ | Kodaira 型 | $v_{\mathfrak p_2}\Delta_{\min}$ | Tamagawa 数 |
|---|---:|---|---:|---:|
| 1 | 12 | $\mathrm I_2^*$ | 18 | 2 |
| $-1$ | 12 | $\mathrm I_2^*$ | 18 | 2 |
| 2 | 12 | $\mathrm I_2^*$ | 18 | 4 |
| $-2$ | 12 | $\mathrm I_2^*$ | 18 | 4 |

这是证书中 $\texttt{elllocalred}$ 的完整精确输入、输出计算；GP 的 Kodaira 码 $-6$ 表示 $\mathrm I_2^*$。例如 $d=1$ 的换元为
$$[u_0,r_0,s_0,t_0]=[1,r-1,0,4-2r],$$
换元后的系数是
$$[a_1,a_2,a_3,a_4,a_6]=[0,1+7r,8-4r,42+2r,36r-36].$$
由同一个诱导导子公式，四个下降系统的精确层都是 $768$，权二、nebentypus $\chi_{12}$。

$B_0$ 非 CM 可独立于软件证明：在 $K$ 的度一素数 $11,13$ 处分别有普通约化迹绝对值 $2,4$。若 $B_0$ 有 CM，其 CM 域在普通约化下分别必须是
$$
\mathbb Q(\sqrt{2^2-4\cdot11})=\mathbb Q(\sqrt{-10}),\qquad
\mathbb Q(\sqrt{4^2-4\cdot13})=\mathbb Q(i),
$$
矛盾。因此四个扭曲也全非 CM。$\operatorname{Res}_{K/\mathbb Q}C_0$ 的 $\mathbb Q$-端同态由 (99.8) 包含 $\mathbb Q(\sqrt{-2})$，因非 CM 恰为这个二次域，所以是简单的 $\mathrm{GL}_2$ 型阿贝尔曲面。已证明的 $\mathrm{GL}_2$ 型模性给出上述层的新形式；参见 Khare–Wintenberger, Corollary 10.2，或 Ribet (1992), Theorem 4.4 与现已成立的 Serre 定理。

选剩余根 $r=5\pmod{11}$、$r=4\pmod{13}$，直接点数及 $u$ 的二次符号给
$$a_{11}(C_0)=-2,\qquad a_{13}(C_0)=4.$$
有理扭曲 $d$ 对这两个系数乘以 $\bigl(\frac d{11}\bigr)$、$\bigl(\frac d{13}\bigr)$，故在第 6 节完整表中唯一识别为
$$
\begin{array}{c|rrrr}
d&1&-1&2&-2\\\hline
\text{轨道}&5&3&2&6.
\end{array}
\tag{99.23}
$$
若选共轭的系数嵌入，只是在 $G_{\mathbb Q}$ 上乘 $\chi_{12}$；限制到 $G_K$ 后不变。因此 (99.18) 与 (99.23) 给
$$C[p]\otimes\overline{\mathbb F}_p\simeq C_0^{(d)}[p]\otimes\overline{\mathbb F}_p.$$
两边原先都在 $\mathbb F_p$ 上定义，并且绝对不可约；互同态空间由 $\mathbb F_p$ 线性方程给出，所以在扩域上非零便在 $\mathbb F_p$ 上非零，因而同构已在 $\mathbb F_p$ 上成立。最后两边同时去掉 $\chi$，得到 (99.5)。定理得证。

## 8. 为什么不能把四个剩余轨道继续按同一固定素数窗口排除

对每个奇素数 $q$，形式参数 $(a,b)=(1,0)$ 给
$$T=X=1/4,\quad W=0,\quad E=A,\quad h=1/2,\quad B=B_0.$$
故在每个好分裂素数处，$B_0$ 的迹平方必属于由 (99.19) 定义的允许集合。更一般 $(a,b)=(d,0)$ 给 $E\simeq A$ 与 $B=B_0^{(d)}$。所以四个固定参考形式使 (99.20) 的某个因子恒为零，继续盲目扩大同一种固定窗口不会使其 gcd 变为非零。

这不是一个实际整数解：$b=0$ 违反 (99.1)，也没有 $|Y|>1$。但实际正奇数 $b$ 可以被任意指定的有限批奇素数整除，故这些局部剩余类不能因为全局 $b\ne0$ 就删去。对固定 $q<p$，$x\mapsto x^p$ 在 $\mathbb F_q^\times$ 上还是双射，单独加入 $T$ 为 $p$ 次幂条件也不改变这一点。

实际 $C$ 的二进型为 II、$v(\Delta_{\min})=12$，四条参考的型为 $\mathrm I_2^*$、$v(\Delta_{\min})=18$。**这些符号与赋值不同，本身尚不能证明模 $p$ 表示不相同。** 需要比较完整二进惯性作用、辛类型或其他全局条件。当前结论不把 Kodaira 型差异当作已经闭合的排除。

## 9. 实二次 Hecke 角色文献的准确版本接口

Pacetti–Villagra Torcomian 的作者版 PDF（题为 *Q-curves, Hecke characters and some Diophantine equations II*，文件日期 2022-03-22）印刷第 5 页 Theorem 2.1 对 $D_K/4\equiv3\pmod8$ 的显示表写了 $\mathfrak p_2^3$。同一作者版印刷第 7 页，定义在
$$\mathcal O_{K,\mathfrak p_2}^{\times}/(1+8\mathcal O_{K,\mathfrak p_2})$$
上的局部 Hecke 分量却指定
$$
\chi_{\mathfrak p_2}(r)=-1,\quad
\chi_{\mathfrak p_2}(1+2r)=1,\quad
\chi_{\mathfrak p_2}(-1)=-1.
$$
因为 $r^2=3$，在模 $8\mathcal O_K$ 的单位群中 $5=-r^2$，所以逐项得到
$$
\chi_{\mathfrak p_2}(5)
=\chi_{\mathfrak p_2}(-1)\chi_{\mathfrak p_2}(r)^2=-1.
$$
但 $5\in1+4\mathcal O_K=1+\mathfrak p_2^4$，故该分量导子至少 $\mathfrak p_2^5$，不能为 $\mathfrak p_2^3$。这里 $D_K=12$，不是把无平方因子的 $3$ 与域判别式混用。

本文的 (99.6) 在同一三个单位上的局部 Hilbert 符号恰为 $[-1,1,-1]$，在奇处不分歧、在两个实处一正一负；其二进导子由 (99.7) 独立计算。该文的全局 $\varepsilon$ 在本例是 $\chi_{12}$，限制到 $G_K$ 平凡，因此 $\chi^2=1$ 与我们的显式二次扩张一致。此处谈的是同一个局部 Hecke 分量，不是事后乘上范数 Dirichlet 角色的另一版本。

上述只指出**已读取作者版内部的显示表与其局部定义不相容**，不据此声称未读取的期刊最终版有误。本文全部导子和下降由 §§2–3 自证，因而不依赖这张表。该文 Theorem 3.2 后的 Remark 2 确实处理 $K=\mathbb Q(\sqrt3)$ 的特殊情况；其 §5 也明确保留 $d=3$ 的非 CM 新形式，不能引用它排除第 7 节四条曲线。

## 10. 可复验入口与原始来源

- [完整标准库 Python + 内嵌 GP 程序](../notes/verify_r99_d3_multifrey.py)。
- [精确 JSON 证书](../notes/r99_d3_multifrey_certificate.json)：全部射影参数、迹集合、十个轨道的十一个系数及 $D_q$、二进导子、角色判别式和四扭曲识别。

~~~sh
python3 -B topics/serre-uniformity/notes/verify_r99_d3_multifrey.py \
  --gp /tmp/pari-2.19.0/gp --check
~~~

通用已安装环境可将 --gp 改为实际 GP 路径。--write 从零重新生成证书；--finite-only 只用 Python 标准库重做全部有限域点数。范数与 gcd 使用每个 $D_q$ 的前置因子 $q$，所以证书直接涵盖 $q=p$。

1. N. Freitas, S. Siksek, *Criteria for irreducibility of mod p representations of Frey curves*, J. Théor. Nombres Bordeaux **27** (2015), 67–76, Theorem 1；[作者预印本](https://arxiv.org/pdf/1309.4748)，[DOI](https://doi.org/10.5802/jtnb.894)。
2. C. Khare, J.-P. Wintenberger, *Serre's modularity conjecture (I)*, Invent. Math. **178** (2009), 485–504；§§1、9、10，特别是 Theorem 9.1 及其已由 Kisin 证明的假设、Corollary 10.2；[作者全文](https://www.math.ucla.edu/~shekhar/papers/results.pdf)。
3. K. A. Ribet, *Abelian varieties over Q and modular forms*, Algebra and Topology 1992 (Taejŏn), 53–79, Theorem 4.4；[作者全文](https://math.berkeley.edu/~ribet/Articles/korea.pdf)。其当时的 Serre 假设现由第 2 项及所引 Kisin 定理解除。
4. A. Pacetti, L. Villagra Torcomian, *Q-curves, Hecke characters and some Diophantine equations II*, Publicacions Matemàtiques **67** (2023), 569–599；[作者版](https://sweet.ua.pt/apacetti/papers/Q-curves2.pdf)，[DOI](https://doi.org/10.5565/publmat6722304)。角色版本边界见 §9。
5. PARI/GP，精确模形式及椭圆曲线局部算法；[官方模形式文档](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_forms.html)，[官方椭圆曲线文档](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html)。本文证书生成于 PARI/GP 2.19.0，不调用条件性类群算法。

