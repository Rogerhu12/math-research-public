# R4：非分裂正规化子及其子群覆盖的 Runge 计数障碍

**状态：已证明；这是路线障碍，不是 Serre 一致性的证明。**

日期：2026-11-12。会话：serre-uniformity-astra。

## 1. 结论及适用范围

固定奇素数 $p$。若无 CM 椭圆曲线 $E/\mathbb Q$ 的模 $p$ 像恰为非分裂 Cartan 正规化子 $N$，则对任意 $H\le N$、$-I\in H$，以及任何使 $\bar\rho_{E,p}(G_F)\subseteq H$ 的数域 $F$，都有
$$c_F(X_H)\le r_1(F)+r_2(F).$$
这里 $X_H$ 在自然圆分基域 $B_H=\mathbb Q(\zeta_p)^{\det H}$ 上定义，$F$ 自动包含 $B_H$；$c_F$ 是尖点的 $F$-Galois 轨道数。在最小提升域 $K=\mathbb Q(E[p])^H$ 上等号成立。

通常 Runge 定理需要 $c_F>|S|$，且 $S$ 必须包含全部无穷位。因此上述覆盖提升及其任意进一步扩域，都不能直接满足通常 Runge 条件。结论不排除 Baker 方法、非尖点除子方法、管状变式或其它额外结构。

另外，$X_{\rm ns}^+(p)$ 上的 $\mathbb Q$-有理模单位均为常数，且单纯扩充常数域也不能恢复通常 Runge 条件。

证明所用的模曲线尖点描述及自然基域属于标准背景；下面给出所有计数、域、复共轭及扩域步骤。保留 G1–G6 的标签，以便与研究笔记交叉核对；它们在本文件中均是 R4 的组成部分。

## 2. 记号与所用标准尖点事实

固定奇素数 $p$，把 $V=\mathbb F_p^2$ 识别为 $\mathbb F_{p^2}$。对 $a\in\mathbb F_{p^2}^{\times}$，令 $m_a(x)=ax$，令 $w(x)=x^p$。记
$$C=\{m_a:a\in\mathbb F_{p^2}^{\times}\},\qquad
N=C\rtimes\langle w\rangle.$$
于是 $C$ 是非分裂 Cartan，$N$ 是其正规化子，且
$$\det m_a=\operatorname N(a),\qquad \det w=-1.$$
令 $M=(V\setminus\{0\})/\{\pm1\}$。

对含 $-I$ 且行列式满的 $H\le N$，模曲线 $X_H$ 是定义在 $\mathbb Q$ 上的光滑射影几何连通曲线。上述参考文献 [1] 的 Lemma 2.1 与 Corollaries 2.2–2.3 给出：

- 几何尖点集合为 $(H\cap\mathrm{SL}_2)\backslash M$；
- 所有尖点都在 $\mathbb Q(\zeta_p)$ 上有定义；
- $\mathbb Q$ 上的 Galois 尖点轨道集合为 $H\backslash M$。

下面还要用其相对版本。设数域 $F$ 的模 $p$ 圆分特征像为
$$D_F=\chi_p(G_F)\le\mathbb F_p^\times,$$
并令 $H(D_F)=H\cap\det^{-1}(D_F)$。则
$$\boxed{c_F(X_H)=|H(D_F)\backslash M|.}\tag{2.1}$$
这不是另一个外部假设：从 Lemma 2.1 的作用公式直接得到。具体地，对 $\lambda\in D_F$ 选择 $\gamma_\lambda\in H$ 满足 $\det\gamma_\lambda=\lambda$。在上述几何尖点商集上，圆分作用由 $\lambda\gamma_\lambda^{-1}$ 作用于向量实现。不能仅凭行列式就断言这个矩阵在 $H$ 中。这里使用 $H\le N$：对乘法型元素 $m_a$，有 $\operatorname{adj}(m_a)=m_{a^p}=m_a^p\in H$；对半线性元素 $g$，有 $\operatorname{tr}(g)=0$，故 $\operatorname{adj}(g)=-g\in H$。因此对所有 $g\in H$ 都有 $\operatorname{adj}(g)\in H$，且 $\operatorname{adj}$ 是对合。于是 $\lambda\gamma_\lambda^{-1}=\operatorname{adj}(\gamma_\lambda)$ 确实在 $H$ 中，行列式是 $\lambda$；这些矩阵随 $\lambda\in D_F$ 恰好遍历 $H(D_F)/(H\cap\mathrm{SL}_2)$ 的陪集。再除以原有的 $H\cap\mathrm{SL}_2$ 作用，便是 (2.1)。这一推导只在已写明的非分裂正规化子子群范围内使用，不把它未经检查地推广到任意 $\mathrm{GL}_2$ 子群。

## 3. 非分裂正规化子的单一尖点轨道

### 命题 G1（尖点域与有理模单位）

$X_N=X_{\rm ns}^+(p)$ 有 $(p-1)/2$ 个几何尖点；每个尖点的剩余域都是
$$L_0=\mathbb Q(\zeta_p)^+,$$
且尖点在 $\mathbb Q$ 上形成一个 Galois 轨道。若 $u\in\mathbb Q(X_N)^\times$ 的零点和极点都仅在尖点，则 $u\in\mathbb Q^\times$。

**证明。** $C$ 在 $V\setminus\{0\}$ 上传递，所以 $N\backslash M$ 只有一个元素。为了同时确定几何尖点数和域，考察 $N\cap\mathrm{SL}_2$ 的作用。其乘法型元素满足 $\operatorname N(a)=1$，保持向量范数；其半线性元素 $m_aw$ 满足 $\operatorname N(a)=-1$，把范数 $t$ 变为 $-t$。反过来，同范数的非零向量由范数一的乘法型元素相连，范数相反的向量也由行列式一的半线性元素相连。因此几何尖点由
$$\mathbb F_p^\times/\{\pm1\}$$
标记。圆分元素 $\lambda$ 在这个标记上乘以 $\lambda$：可在 §2 的公式中取 $\gamma_\lambda=m_a$, $\operatorname N(a)=\lambda$，于是
$$\operatorname N(\lambda a^{-1}x)=\lambda\operatorname N(x).$$
任一尖点的稳定子是圆分 Galois 群中的 $\{\pm1\}$，故尖点域正是 $L_0$。

若 $u$ 如陈述所示，$\operatorname{div}(u)$ 是 Galois 不变的尖点除子。因为所有尖点共轭，每个几何尖点在除子中的系数相同，设为 $n$。主除子次数为零，所以 $n(p-1)/2=0$，从而 $n=0$。光滑射影几何连通曲线上无零极点的函数为常数，且 $u$ 在 $\mathbb Q$ 上有定义，故常数在 $\mathbb Q^\times$。证毕。

### 推论 G2（单纯基变换不能恢复通常 Runge 条件）

对每个数域 $F$，
$$c_F(X_N)=[F\cap L_0:\mathbb Q]\le r_1(F)+r_2(F).$$
因此对任何包含所有无穷位的 $S$，均有 $c_F(X_N)\le|S|$。

**证明。** 尖点是 $\operatorname{Gal}(L_0/\mathbb Q)$ 的正则集合；$F$ 上的轨道数即 $[F\cap L_0:\mathbb Q]$。令 $B=F\cap L_0$。$B$ 完全实，它的每个实嵌入至少延拓为 $F$ 的一个无穷位，所以 $[B:\mathbb Q]\le r_1(F)+r_2(F)$。证毕。

这里允许 $F$ 依赖 $p$。尤其，直接把全部尖点分裂到 $L_0$ 上，只会同时产生 $(p-1)/2$ 个无穷位；严格不等式仍然没有出现。

## 4. 覆盖提升同样不能直接创造 Runge 条件

这一节将上一障碍推广到“先把完整正规化子像降到一个已研究的真子群，再在相应扩域上用 Runge”的路线。命题只涉及当前这一类覆盖，不宣称所有替代方法不可行。

### 引理 G3（向量稳定子与复共轭）

1. $N$ 在 $M$ 上传递，$[1]\in M$ 的稳定子是
   $$J=\{I,-I,w,-w\}=\langle-I,w\rangle.$$
2. 若 $c\in N$ 的特征多项式为 $T^2-1$，则 $c$ 在 $N$ 中共轭于 $w$。
3. 对任意包含 $-I$ 的 $H\le N$，
   $$|H\backslash M|=|\langle w\rangle\backslash N/H|.$$

**证明。** 传递性来自乘法群。一个 $m_a$ 或 $m_aw$ 固定 $[1]$，当且仅当 $a=\pm1$，得到 1。$C$ 的非标量元素没有 $\mathbb F_p$ 特征直线，而 $c$ 有两个不同的 $\mathbb F_p$ 特征值，故 $c=m_aw\notin C$。条件 $c^2=I$ 等价于 $\operatorname N(a)=1$。有限域乘法群是循环群，映射 $b\mapsto b/b^p$ 的核为 $\mathbb F_p^\times$，其像恰是范数一群，所以存在 $b$ 使 $a=b/b^p$。于是 $c=m_bw m_b^{-1}$。最后 $M=N/J$，逆元映射把 $H\backslash N/J$ 变成 $J\backslash N/H$；中央的 $-I\in H$ 在 $N/H$ 上作用平凡，故可将 $J$ 换成 $\langle w\rangle$。证毕。

### 命题 G4（最小提升域上尖点轨道数等于无穷位数）

设无 CM 椭圆曲线 $E/\mathbb Q$ 的模 $p$ 像恰为 $N$，把挠点分裂域记为 $L=\mathbb Q(E[p])$，以所选基识别 $\operatorname{Gal}(L/\mathbb Q)=N$。设
$$H\le N,\qquad -I\in H,\qquad \det H=\mathbb F_p^\times,$$
并令 $K=L^H$。则 $E$ 的 $H$ 级结构给出 $X_H(K)$ 的点，并且
$$\boxed{c_K(X_H)=c_{\mathbb Q}(X_H)=r_1(K)+r_2(K).}\tag{4.1}$$

**证明。** 由定义，$G_K$ 在 $E[p]$ 上的像为 $H$，所以对应 $H$ 结构在 $K$ 上有定义。

Weil 配对给出 $\mathbb Q(\zeta_p)=L^{N\cap\mathrm{SL}_2}$。因为 $\det H$ 满，限制到 $H$ 的行列式仍满，所以 $G_K$ 的圆分像是全部 $\mathbb F_p^\times$。因此 §2 的公式给出
$$c_K(X_H)=|H\backslash M|=c_{\mathbb Q}(X_H).$$
同样可表述为 $K\cap\mathbb Q(\zeta_p)=\mathbb Q$，且所有尖点的 Galois 作用在基变换后不变。

固定一个嵌入 $L\hookrightarrow\mathbb C$。$K$ 的所有嵌入形成 $N/H$。复共轭的单点轨道对应实嵌入，双点轨道对应成对的复嵌入，所以其轨道数是 $r_1(K)+r_2(K)$。椭圆曲线的奇性及 Weil 配对给出复共轭矩阵的特征值 $1,-1$；由 G3，它在 $N$ 内共轭于 $w$。故
$$r_1(K)+r_2(K)=|\langle w\rangle\backslash N/H|=|H\backslash M|,$$
完成证明。

### 命题 G5（进一步扩域也不能恢复这类提升的 Runge 条件）

保留 G4 的 $E,N,H,L$。允许任意数域 $F$，只要求在当前选定的基下
$$\bar\rho_{E,p}(G_F)\subseteq H.$$
那么
$$\boxed{c_F(X_H)\le r_1(F)+r_2(F).}\tag{4.2}$$
因此对任何 $S\supseteq M_F^\infty$，通常 Runge 条件 $c_F(X_H)>|S|$ 都不成立。

**证明。** 令 $D=D_F$，$H_D=H\cap\det^{-1}(D)$，并令 $K_D=L^{H_D}$。因为 $\bar\rho_{E,p}(G_F)\subseteq H_D$，有 $K_D\subseteq F$。公式 (2.1) 和 G3 给出
$$c_F(X_H)=|H_D\backslash M|
=|\langle w\rangle\backslash N/H_D|.
$$
这里 $-I\in H_D$，因为 $\det(-I)=1$。与 G4 同样的复共轭—嵌入对应说明右侧恰为 $r_1(K_D)+r_2(K_D)$；这一句不需要 $\det H_D$ 满。数域每个无穷位在有限扩域中至少有一个延拓，所以
$$r_1(K_D)+r_2(K_D)\le r_1(F)+r_2(F).$$
证毕。

### 指数三例子

若 $p\equiv2\pmod3$，令 $H=C^3\rtimes\langle w\rangle$。此时 $-I\in C^3$，且 $\det H=\mathbb F_p^\times$：$p\equiv2\pmod3$ 使立方映射在 $\mathbb F_p^\times$ 上可逆。$[N:H]=3$，$N/C^3\cong S_3$，$H/C^3$ 是一个反射子群。复共轭在三个陪集上的循环型为 $(1)(2)$，故 $K=L^H$ 有签名 $(r_1,r_2)=(1,1)$。相应地，尖点有两个 $K$-Galois 轨道。

这解释了为何 Le Fourn–Lemos 对 **有理** 指数三像的 Runge 分析，不能经“把完整正规化子像提升到三次数域”直接解决当前剩余情形：有理指数三像有两个尖点轨道与一个无穷位，提升后的完整正规化子像有两个尖点轨道与两个无穷位。

### 命题 G6（去掉满行列式要求）

G4–G5 可扩展到任意包含 $-I$ 的 $H\le N$；此时将 $X_H$ 定义在其自然圆分基域
$$B_H=\mathbb Q(\zeta_p)^{\det H}$$
上，并选取与所固定的 Weil 配对相符的几何连通分支。若 $K=L^H$，则 $B_H\subseteq K$，且
$$c_K(X_H)=r_1(K)+r_2(K).$$
若任意数域 $F$ 满足 $\bar\rho_{E,p}(G_F)\subseteq H$，则自动有 $B_H\subseteq F$，从而 $X_H$ 可在 $F$ 上考虑，并仍然有
$$c_F(X_H)\le r_1(F)+r_2(F).$$

**证明。** 模曲线的自然基域描述见参考文献 [2] 开头，或 [3] §1。Weil 配对及有限 Galois 对应给出
$$K\cap\mathbb Q(\zeta_p)=L^{\langle H,N\cap\mathrm{SL}_2\rangle}=L^{\det^{-1}(\det H)}=B_H,$$
所以 $K$ 包含所需基域。对任意上述 $F$，圆分像 $D_F\subseteq\det H$，故 $G_F$ 固定 $B_H$。

在这个选定分支上，几何尖点仍是 $(H\cap\mathrm{SL}_2)\backslash M$。对 $\lambda\in D_F$ 仍然可以选取 $\gamma_\lambda\in H$，而 §2 已验证伴随矩阵保持本题的 $H$。所以相对公式
$$c_F(X_H)=|(H\cap\det^{-1}(D_F))\backslash M|$$
依旧成立。其余证明就是 G4–G5 的双陪集计数及复共轭—嵌入对应；它们不使用行列式满。对 $F=K$，有 $D_K=\det H$，给出等式；对一般 $F$，取 $K_D=L^{H\cap\det^{-1}(D_F)}\subseteq F$，得到不等式。证毕。

这也覆盖了最极端的全级提升：若 $H=\{\pm I\}$，则 $K$ 含 $\mathbb Q(\zeta_p)$，所有 $(p^2-1)/2$ 个几何尖点在 $K$ 上有定义，但 $K$ 也恰有 $(p^2-1)/2$ 个无穷位；仍没有严格的 Runge 不等式。


## 5. 参考文献

[1] S. Le Fourn and P. Lemos, *Residual Galois representations of elliptic curves with image contained in the normaliser of a non-split Cartan*, Algebra Number Theory 15 (2021), 747–771, Lemma 2.1 and Corollaries 2.2–2.3. <https://arxiv.org/pdf/2002.02714>。本文只在 $H\le N$、$-I\in H$ 的范围内使用，并在 §2 显式验证所需的伴随矩阵闭合性。

[2] Y. Bilu and P. Parent, *Runge's method and modular curves*, IMRN 2011, 1997–2027, Theorem 1.2. <https://arxiv.org/pdf/0907.3306>。

[3] D. Zywina, *Improved bounds for integral points on modular curves using Runge's method*, arXiv:2403.14904 (2024), §1 and Theorem 1.1. <https://arxiv.org/html/2403.14904v1>。其改进仍明确要求相同的 Runge 严格不等式。
