# R56：单素数原始指标的模三射线类群筛与三阶单位递推

日期：2026-11-12；会话：serre-uniformity-resume2；分支：cm-denominators。

**状态：已证明的全局必要条件与精确算术归约。** 本篇继续 R53 的同一个三次域，证明原始高指标值必须满足三个明确的模 $(3)$ 射线类群关系之一。通过该筛之后，全部实际解由至多三个理想生成元的单位轨道给出；所需单位秩为一来自复三次域的签名，不是对辅助椭圆曲线的秩作任何假定。

本例的射线类群、基本单位及候选理想生成元尚未实算。因此本文没有判定 R53 的指标 $2q^{21}$ 是否出现，也没有给出随 $q,p$ 变化的统一排除。第 8 节精确列出已证明的有效接口与未完成的计算。

## 1. 固定域、素理想与待解方程

沿用 R53 的确定参数
$$
n=116\prod_{\substack{r\le461\\r\ {\rm prime}}}r,\qquad
q=432n^2-1.
$$
R53 已证明 $q$ 是素数，
$$
L=\mathbb Q(\theta),\qquad \theta^3-\theta-8n=0,
$$
为签名 $(1,1)$ 的三次域，最大整环为
$$
\mathcal O_L=\mathbb Z+\mathbb Z\theta+\mathbb Z\beta,\qquad
\beta=(\theta^2+\theta)/2,\qquad D_L=-q.
\tag{56.1}
$$
其乘法表为
$$
\theta^2=2\beta-\theta,\qquad
\theta\beta=\beta+4n,\qquad
\beta^2=\beta+2n\theta+4n.
\tag{56.2}
$$

对整数 $m>1$ 考察
$$
I(u,v)=u(u+v)(2u+v)-2nv^3=\pm2q^m,\qquad
(u,v)=1,\qquad 3\mid v.
\tag{56.3}
$$
当 $m=21$ 时，这正是 R53 的 $p=43$ 最后问题。更一般地，若 $p=2m+1$ 是所需素数，(56.3) 与该候选域的族 I 原始指数条件对应；本篇不把任意整数 $m$ 都宣称为一个允许的 Serre 指数。

素数 $2$ 在 $L$ 中完全分裂。用三个 $2$ 进根的标号固定
$$
\theta_0\equiv0\pmod{64},\qquad
\theta_+\equiv1\pmod{32},\qquad
\theta_-\equiv-1\pmod{32}.
$$
相应的三个范数二素理想为
$$
\begin{aligned}
\mathfrak p_0&=(2,\theta,\beta),\\
\mathfrak p_+&=(2,\theta-1,\beta-1),\\
\mathfrak p_-&=(2,\theta-1,\beta),
\end{aligned}
\qquad
(2)=\mathfrak p_0\mathfrak p_+\mathfrak p_-.
\tag{56.4}
$$
这里必须使用最大整环中的 $\beta$ 来区分后两个素理想；只把
$T^3-T-8n$ 模二分解会误读重复根。

在 $q$ 处，R53 给出
$$
(q)=\mathfrak q_1\mathfrak q_2^2,\qquad
\mathfrak q_1=(q,\theta-24n),\quad
\mathfrak q_2=(q,\theta+12n),
\tag{56.5}
$$
二者范数均为 $q$；前者是不分歧的一次因子，后者来自分歧二次因子。

令
$$
G=\operatorname{Cl}_{(3)}(L)
$$
为只有有限模 $(3)$、不加实位的射线类群：其主关系由
$x\equiv1\pmod{3\mathcal O_L}$ 给出。记
$$
c_0=[\mathfrak p_0],\qquad
c_+=[\mathfrak p_+],\qquad c_-=[\mathfrak p_-]
\quad\text{于 }G.
$$
所有出现的分数理想均与 $(3)$ 互素。
文中分数元的模三同余都按通常射线约定在
$\mathcal O_L\otimes\mathbb Z_3$ 中解释；它们允许在 $2$ 处有分母，并不要求差属于全局的 $3\mathcal O_L$。

## 2. 主结论

**定理 56.1。** 每个 (56.3) 的解必落入下表恰好一行：

| 坐标情形 | 下文 $\alpha$ 的完整分数理想 | 在 $G$ 中必有的关系 |
|---|---|---|
| $v$ 偶 | $\mathfrak q_1^m$ | $2m\,c_0=0$ |
| $v$ 奇、$u$ 偶 | $\mathfrak q_1^m\mathfrak p_+\mathfrak p_0^{-1}$ | $(2m+1)c_0=c_+$ |
| $v$ 奇、$u$ 奇 | $\mathfrak q_1^m\mathfrak p_-\mathfrak p_0^{-1}$ | $(2m+1)c_0=c_-$ |

其中
$$
\alpha=u+\frac v2-\frac v2\theta,\qquad
N_{L/\mathbb Q}(\alpha)=I(u,v)/2.
\tag{56.6}
$$

特别地，R53 的实际 $p=43$ 解要求
$$
\boxed{42c_0=0\quad\text{或}\quad43c_0=c_+
\quad\text{或}\quad43c_0=c_-.}
\tag{56.7}
$$
这些关系发生在模三射线类群中，故比只在普通类群中检查同一等式更强。

对通过相应关系的行，令其完整分数理想为 $\mathfrak A_\sigma$。选取
$$
(\gamma_\sigma)=\mathfrak A_\sigma,\qquad
\gamma_\sigma\equiv1\pmod{3\mathcal O_L},
$$
并置
$$
\alpha_\sigma=(-1)^m\gamma_\sigma.
\tag{56.8}
$$
则 $N(\alpha_\sigma)=q^m$。取正实基本单位 $\varepsilon>1$，使
$$
\mathcal O_L^\times=\{\pm\varepsilon^j:j\in\mathbb Z\},
\qquad N(\varepsilon)=1.
$$
令 $r$ 为 $\varepsilon$ 模 $(3)$ 的阶。因为 $3$ 在 $L$ 中完全分裂，必有
$$
r\in\{1,2\}.
\tag{56.9}
$$

将 $\alpha_\sigma\varepsilon^j$ 按基 $(1,\theta,\beta)$ 写为
$$
\alpha_\sigma\varepsilon^j=A_j+B_j\theta+C_j\beta.
$$
那么 (56.3) 的全部正号解，恰由以下条件给出：
$$
\boxed{j\in r\mathbb Z,\qquad C_j=0,}
\tag{56.10}
$$
并按
$$
u=A_j+B_j,\qquad v=-2B_j
\tag{56.11}
$$
恢复整数坐标。由理想条件，(56.11) 的整数性与原始性自动成立。负号解由同时取负 $(u,v)$ 得到。

因此射线类群关系不是全部充分条件；通过之后仍须真正求解一个三阶单位递推的零点条件。

## 3. 范数恒等式及 q 处支撑的强制选择

### 3.1 范数与分母

对 $a,b\in\mathbb Q$，
$$
N(a-b\theta)=a^3-ab^2-8nb^3.
$$
取 $a=u+v/2$、$b=v/2$，便得 (56.6)。在每个奇素数处 $\alpha$ 为整元，分母至多出现在 $2$。因为 $|N(\alpha)|=q^m$，其在所有不除 $2q$ 的素理想处估值均为零。

### 3.2 原始性排除分歧因子的高次估值

首先 $q\nmid v$。否则由 $(u,v)=1$ 有 $q\nmid u$，于是 $\alpha$ 在 $q$ 上方处处为单位，与 $q\mid N(\alpha)$ 矛盾。

在分歧二次因子中可写
$$
\theta=s+t\pi,\qquad
s\in\mathbb Z_q,\quad t\in\mathbb Z_q^\times,\quad
\pi^2=q\epsilon,\quad \epsilon\in\mathbb Z_q^\times.
\tag{56.12}
$$
这里 $t$ 为单位并非额外假设：原多项式判别式在 $q$ 处的赋值是一，简单根与另两根的差都是单位，故后两根之差的赋值恰为 $1/2$。

由 $q\nmid v$，$\alpha$ 的 $\pi$ 系数 $-vt/2$ 是单位。如果
$\mathfrak q_2\mid(\alpha)$，则其有理常数部分被 $q$ 整除，而 $\pi$ 项的 $\pi$ 进赋值恰为一。因此
$$
\boxed{v_{\mathfrak q_2}(\alpha)=1}
\tag{56.13}
$$
只要该赋值非零。

与此同时，$\alpha$ 不能在 $\mathfrak q_1,\mathfrak q_2$ 两处都可除：模 $q$ 的两个相应根为 $24n$、$-12n$，差 $36n$ 是单位；一次式 $a-bT$ 的 $b=v/2$ 也是单位，不可能同时在两根处为零。

若 $\mathfrak q_2$ 出现，(56.13) 和上述互斥性就强迫
$v_q(N(\alpha))=1$，与 $m>1$ 矛盾。故高指标原始解只能满足
$$
(\alpha)_q=\mathfrak q_1^m.
\tag{56.14}
$$
这比仅知道范数的素数支撑为 $\{q\}$ 更强；它指定了支撑在 $q$ 上方的哪一个素理想上。

## 4. 素数 2 处恰好三种分数理想模式

由 (56.6)，
$$
\alpha=u+v(1-\theta)/2.
$$

### 4.1 v 偶

此时 $\alpha$ 在三个二进因子中均为整元，而 $N(\alpha)$ 为奇数，所以三个估值都为零。原始性给 $u$ 奇；再在 $\theta_0$ 因子中取模二，得到 $v\equiv0\pmod4$。

因此二进理想因子为 $1$。

### 4.2 v 奇

在 $\theta_0$ 因子处，分子 $2u+v-v\theta_0$ 为奇数，故
$$
v_{\mathfrak p_0}(\alpha)=-1.
$$
在两个奇根处，
$$
\frac{1-\theta_+}{2}\equiv0\pmod{16},\qquad
\frac{1-\theta_-}{2}\equiv1\pmod{16}.
$$
所以 $\alpha$ 在这两处均整，并且其奇偶性分别由 $u$、$u+v$ 决定。因为 $v$ 奇，其中恰好一个为偶数。

$v_2(N(\alpha))=0$ 又给出
$$
v_{\mathfrak p_+}(\alpha)+v_{\mathfrak p_-}(\alpha)=1.
$$
因此那个正估值必须恰为一，而不是任意正数。于是
$$
(\alpha)_2=
\begin{cases}
\mathfrak p_+\mathfrak p_0^{-1},&u\text{ 偶},\\
\mathfrak p_-\mathfrak p_0^{-1},&u\text{ 奇}.
\end{cases}
\tag{56.15}
$$
还自动有：前一行 $u\equiv2\pmod4$，后一行 $u+v\equiv2\pmod4$。

结合第 3 节，这给出了定理表格中的**完整**分数理想，不存在未记下的其他素数因子。

## 5. 显式主关系与射线类群条件

令
$$
\eta=3\theta^2-4=6\beta-3\theta-4.
$$
利用 $\theta(\theta^2-1)=8n$，有精确恒等式
$$
\begin{aligned}
(3\theta^2-4)(3\theta^2-1)^2
&=27\theta^2(\theta^2-1)^2-4\\
&=1728n^2-4=4q.
\end{aligned}
\tag{56.16}
$$
又
$$
N(3\theta^2-1)=-\operatorname{disc}(g)=4q.
$$
对 (56.16) 取范数，得到
$$
\boxed{N(\eta)=4q.}
\tag{56.17}
$$

在 $\mathfrak p_0$ 处，$\theta_0$ 被 $64$ 整除，所以
$v_{\mathfrak p_0}(\eta)=2$；在 $\mathfrak p_\pm$ 处，$\eta$ 为奇单位。在 $q$ 处，
$$
\eta(24n)\equiv0\pmod q,\qquad
\eta(-12n)\equiv-3\pmod q.
$$
结合范数，得到精确理想式
$$
\boxed{(\eta)=\mathfrak q_1\mathfrak p_0^2.}
\tag{56.18}
$$

特别注意 $\eta\equiv-1\pmod{3\mathcal O_L}$，所以 $-\eta\equiv1$。因此 (56.18) 在模三射线类群中已经给出
$$
[\mathfrak q_1]=-2c_0.
\tag{56.19}
$$
同样，$-2\equiv1\pmod3$，故
$$
c_0+c_++c_-=0
\quad\text{于 }G.
\tag{56.20}
$$

还可用原多项式导数直接交叉核对。三个二进根上 $3\theta^2-1$ 的估值分别为 $0,1,1$，而在 $q$ 处恰支撑于 $\mathfrak q_2$。于是
$$
(3\theta^2-1)=\mathfrak q_2\mathfrak p_+\mathfrak p_-,
\qquad
\left(\frac{3\theta^2-1}{2}\right)
=\mathfrak q_2\mathfrak p_0^{-1}.
$$
这个分数元模三同余于一，所以 $[\mathfrak q_2]=c_0$ 也在 $G$ 中成立。它与 (56.5) 再次给出 (56.19)。同时
$$
\frac{\eta}{q}
=\left(\frac2{3\theta^2-1}\right)^2
$$
已经在 $L$ 中是平方，不能把它误用来构造一个新的非平凡二次扩张。

若 (56.3) 中 $3\mid v$，则
$$
\alpha\equiv u\pmod{3\mathcal O_L}.
$$
范数是三进单位，所以 $3\nmid u$；因此 $\alpha\equiv1$ 或 $-1$。在需要时乘以 $-1$，可使生成元同余于一，所以 $(\alpha)$ 在 $G$ 中的类为零。

把定理表格的三个完整理想代入 (56.19)，即得到
$$
2m\,c_0=0,\qquad
(2m+1)c_0=c_+,\qquad
(2m+1)c_0=c_-.
$$
反过来，每个相应等式恰说明该行的分数理想在 $G$ 中为零，所以确实可选取 (56.8) 的射线主生成元。它还不保证该生成元或其单位倍的 $\beta$ 坐标为零。

对于固定 $L$，若 $h_0$ 是 $c_0$ 在 $G$ 中的阶，则第一行要求
$2m\equiv0\pmod{h_0}$；若 $c_\pm$ 不在 $\langle c_0\rangle$ 中，相应行彻底排除。若在其中，则另外两行各给一个关于 $2m+1$ 的剩余类。这个筛控制的是指数的算术位置；本篇没有把它冒充最大指数的绝对上界。

## 6. 从射线主生成元恢复全部原始整数点

### 6.1 单位秩和模三阶数

因为 $D_L<0$，$L$ 的签名为 $(1,1)$，Dirichlet 单位定理给单位秩一。三次域的有限单位只有 $\pm1$。选择实嵌入下大于一的基本单位 $\varepsilon$，则其范数为一，所有正范数单位均为 $\varepsilon^j$。

$3\mid n$，所以
$$
g(T)\equiv T(T-1)(T+1)\pmod3
$$
有三个不同根；从而
$$
\mathcal O_L/3\mathcal O_L\simeq\mathbb F_3^3.
$$
每个单位的模三像平方为一，故 (56.9) 成立。

射线主生成元 $\gamma_\sigma\equiv1\bmod3$ 满足
$|N(\gamma_\sigma)|=q^m$。又其范数模三为一，而
$q^m\equiv(-1)^m\bmod3$，所以范数的符号必为 $(-1)^m$。于是 (56.8) 确实满足
$$
N(\alpha_\sigma)=q^m,\qquad
\alpha_\sigma\equiv(-1)^m\pmod3.
\tag{56.21}
$$
该理想的全部正范数生成元恰为 $\alpha_\sigma\varepsilon^j$。其模三仍是所需标量，当且仅当 $\varepsilon^j\equiv1$，也就是 $j\in r\mathbb Z$。

### 6.2 零坐标条件自动给正确整数格

对 $\sigma=0$，理想 $\mathfrak A_0=\mathfrak q_1^m$ 整，所以其每个生成元都属于 $\mathcal O_L$。若 $\beta$ 坐标为零，便是 $A+B\theta$，其中 $A,B\in\mathbb Z$，(56.11) 自然给整数。

对 $\sigma=+$ 或 $-$，$2\alpha$ 为整元。其模二在三个因子中的值为 $(1,0,0)$；在基 $(1,\theta,\beta)$ 中，这就是 $1+\theta$。因此若
$$
\alpha=A+B\theta+C\beta,
$$
则 $2A,2B$ 均为奇整数，而 $C\in\mathbb Z$。当 $C=0$ 时，
$A+B\in\mathbb Z$、$-2B\in\mathbb Z$，仍给 (56.11) 的整数坐标。

由范数恒等式，这些坐标满足 $I(u,v)=2q^m$。其原始性也自动成立：若奇素数 $\ell$ 同时整除 $u,v$，则 $\alpha\in\ell(\mathcal O_L\otimes\mathbb Z_\ell)$。当 $\ell\ne q$ 时这与范数支撑矛盾；当 $\ell=q$ 时，这会使 $\mathfrak q_2$ 也出现在 $(\alpha)$ 中，与已指定的 $\mathfrak q_1^m$ 矛盾。如果 $2\mid u,v$，三次齐次性给 $8\mid I(u,v)$，与 $v_2(I)=1$ 矛盾。

最后，$\alpha\equiv(-1)^m\bmod3$ 且 $C=0$ 强迫 $B\equiv0\bmod3$，故 $3\mid v$。这证明 (56.10) 的充分方向。

反方向已经由第 3–5 节的完整理想分类及单位群描述给出。因此这里得到的是真正双向的参数化，没有遗留“再检查整数性和原始性”的隐含步骤。

## 7. 缺失坐标的三阶递推与有效零点接口

### 7.1 明确的整数矩阵

写基本单位
$$
\varepsilon=a+b\theta+c\beta,\qquad a,b,c\in\mathbb Z.
$$
由 (56.2)，乘以 $\varepsilon$ 的矩阵为
$$
M_\varepsilon=
\begin{pmatrix}
a&4nc&4n(b+c)\\
b&a-b&2nc\\
c&2b+c&a+b+c
\end{pmatrix}
\in\operatorname{SL}_3(\mathbb Z).
\tag{56.22}
$$
若 $w_j=2(A_j,B_j,C_j)^{\mathsf T}$，则
$$
w_j=M_\varepsilon^j w_0\in\mathbb Z^3
\qquad(j\in\mathbb Z).
$$
因此要解的就是第三坐标为零，另限制 $j\in r\mathbb Z$。

令
$$
T_\varepsilon=\operatorname{Tr}(\varepsilon),\qquad
S_\varepsilon=\operatorname{Tr}(\varepsilon^{-1}).
$$
基本单位不在 $\mathbb Q$，所以其最小多项式为
$$
T^3-T_\varepsilon T^2+S_\varepsilon T-1.
$$
缺失坐标 $z_j=2C_j$ 满足具体三阶递推
$$
\boxed{
z_{j+3}=T_\varepsilon z_{j+2}
-S_\varepsilon z_{j+1}+z_j.
}
\tag{56.23}
$$
这不是已经识别出的 Lucas 或 Lehmer 序列。本文不使用 BHV 原始除子定理。

### 7.2 实嵌入一侧有直接大小上界

令 $\varepsilon_{\mathbb R}=\varepsilon>1$，另两共轭为
$\varepsilon_{\mathbb C},\overline{\varepsilon_{\mathbb C}}$，则
$$
|\varepsilon_{\mathbb C}|=\varepsilon^{-1/2}.
$$
取 $\beta$ 坐标的线性泛函可写为
$$
\operatorname{coeff}_{\beta}(x)
=\operatorname{Tr}_{L/\mathbb Q}
\left(\frac{2x}{3\theta^2-1}\right).
\tag{56.24}
$$
可由 (56.2) 的迹矩阵直接核对；三个嵌入下的系数均非零。因此
$$
C_j=A\varepsilon^j+
B\varepsilon_{\mathbb C}^j+
\overline B\,\overline{\varepsilon_{\mathbb C}}^j,
\qquad A\in\mathbb R^\times,\quad B\in\mathbb C^\times,
\tag{56.25}
$$
其中 $A,B$ 都由已选生成元和基本单位有效确定。

若 $C_j=0$，则
$$
|A|\varepsilon^j
\le2|B|\varepsilon^{-j/2}.
$$
故对 $j\ge0$ 已有直接上界
$$
j\le\frac{2}{3\log\varepsilon}
\log\left(\frac{2|B|}{|A|}\right).
\tag{56.26}
$$
如果右端为负，这一侧没有零点。

### 7.3 负指数一侧须使用复对数下界

当 $j=-h<0$ 时，两项复共轭可以相消，不能继续沿用 (56.26)。
令
$$
\zeta=\varepsilon_{\mathbb C}/\overline{\varepsilon_{\mathbb C}},
\qquad \lambda=-B/\overline B.
$$
由 (56.25) 的零点等式，
$$
\left|1-\lambda\zeta^{-h}\right|
=\left|\frac A{\overline B}\right|\varepsilon^{-3h/2}>0.
\tag{56.27}
$$
$\zeta$ 不是单位根：否则某个正幂 $\varepsilon^s$ 的两个共轭相等。由于 $L$ 为三次域，没有非平凡中间域，这将强迫 $\varepsilon^s\in\mathbb Q$；它是有理单位，遂与 $\varepsilon>1$ 矛盾。

已发表的 Baker–Wüstholz 复对数线性形式下界应用于
$\lambda,\zeta,-1$，给出可计算的正常数 $C_0,C_1$，使 (56.27) 的非零左边满足
$$
\left|1-\lambda\zeta^{-h}\right|
\ge C_0(h+3)^{-C_1}.
\tag{56.28}
$$
这里选择靠近零的对数时，所引入的 $2\pi i$ 整数倍系数为 $O(h)$；所有代数数均位于固定三次域的次数六正规闭包内。若某个对数项为零，可直接删除，仍为同一已发表定理的适用情形。

把 (56.27)、(56.28) 合并，指数衰减与多项式下界给出一个可计算的 $h$ 上界。随后只须在这个有限区间内用整数矩阵 (56.22) 精确检查，而非依赖浮点近似。

所用外部定理为 A. Baker, G. Wüstholz, “Logarithmic forms and group varieties”, J. reine angew. Math. **442** (1993), 19–62，[DOI](https://doi.org/10.1515/crll.1993.442.19)；作者的 *Logarithmic Forms and Diophantine Geometry* (Cambridge, 2008), Chapter 7, pp. 149–166 亦给出完全显式的定量版本，[出版社章节](https://doi.org/10.1017/CBO9780511542862.008)。本节将该成熟定理所需的非零性、域次数和两侧增长分别验证；没有从 Skolem–Mahler–Lech 的有限性直接宣称有效求解。

## 8. 巨大判别式没有自动排除射线类群关系

### 8.1 一个不能省略的单位问题

若 $42c_0=0$，就有某个生成元使 $\mathfrak p_0^{42}$ 为主。它的范数绝对值为 $2^{42}$，但这不迫使它的实、复嵌入同时很小；乘以无限单位可以使一边任意大、另一边任意小。因此不能将虚二次域的正定范数下界直接套在这里。

事实上，“最大判别式任意大、$2$ 完全分裂”本身甚至不排除这种普通类群关系。下面给一个独立的明确说明；它不是 R53 的同一个域，也不声称满足这里的模三射线条件。

令 $C=2^{42}$，取整数 $N>C$、$N\equiv7\pmod8$，并定义
$$
f_N(T)=T^3+NT-C.
$$
其唯一实根位于 $(0,1)$，因为导数处处为正；三次首一式若可约须有整数根，因此它不可约。设根为 $\vartheta$，域为 $L_N$。

在 $2$ 处，零附近的根赋值恰为 $42$。又 $-N\equiv1\bmod8$，可取奇数平方根 $s^2=-N$；在 $\pm s$ 处 $f_N=-C$ 的赋值为 $42$，导数 $-2N$ 的赋值为一。强 Hensel 引理给另外两个不同的奇根。因此 $2$ 在 $L_N$ 完全分裂，且若 $\mathfrak l_0$ 是偶根对应的范数二素理想，就有
$$
(\vartheta)=\mathfrak l_0^{42}.
\tag{56.29}
$$

这些域的最大判别式可以无界。取任意大的素数 $R\equiv2\pmod3$，$R>3$。立方映射在 $\mathbb F_R$ 上双射，因此可选非零 $N_0$ 使
$$
-4N_0^3-27C^2\equiv0\pmod R.
$$
相应导数 $-12N_0^2$ 非零，故在 $N_0$ 的 $R$ 个模 $R^2$ 提升中，恰一个会使判别式再被 $R^2$ 整除。选择其他提升，并同时令 $N\equiv7\bmod8$、$N>C$，便得到
$$
v_R(\operatorname{disc}(f_N))=1.
$$
指标平方不能除去这个奇赋值，故 $R\mid D_{L_N}$。这证明存在最大判别式任意大而 (56.29) 成立的复三次域。

这个例子没有证明 R53 的三个关系中的任何一个成立；它只严格排除了“判别式很大，所以范数二素理想的阶一定大于四十二”这条无效推理。若要在 R53 中排除关系，必须真正使用其射线类群、基本单位，或额外的特殊算术。

### 8.2 当前实际计算状态

已完成且可直接复验的部分是：

- 最大整环基、$2,q$ 上方全部素理想及其范数；
- 原始高指标元在 $q$ 处只能支撑于 $\mathfrak q_1$；
- 三种完整二进分数理想模式；
- $\eta$ 的精确范数与主理想；
- 模三射线类群中的三个必要关系；
- 通过筛之后的双向单位轨道参数化、三阶整数递推以及两侧有效零点论证。

**尚未计算**本例 $G$ 中 $c_0,c_\pm$ 的实际关系，也尚未得到基本单位 $\varepsilon$、调节子，或通过筛的 $\alpha_\sigma$。当前环境未安装 PARI/GP 或 Sage；本文没有以某个未经执行的软件命令当作已算出的证明，也没有把设备情况当作数学不可解性。

即使未来算出这些固定域数据并完整解决 $m=21$，也只是一个固定 $q,p$ 的判定。为了处理变化的 $p,Z,L$，还需要一个真正统一的输入；(56.26)、(56.28) 的常数依赖基本单位和理想生成元，不能未经证明便视为绝对常数。

R56 因而给出了新的全局类群筛与可执行的精确递推目标，同时保留了尚未完成的实际计算和统一性缺口。


