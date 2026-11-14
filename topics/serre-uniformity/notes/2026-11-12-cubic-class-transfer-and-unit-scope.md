# 三次类群的范数转移、显式单位范围与模三射线反检验

日期：2026-11-12；会话：serre-uniformity-resume2；分支：cm-denominators。

**性质：独立研究笔记。** 继续检查 R56 是否能仅凭 R53 的巨大判别式或现成近纯三次单位公式完成结构性排除。下述证明界定三条路线的实际范围，不判定 R53 的三个射线类关系。

## 1. 到虚二次预解式域的自然范数把所需类全部杀掉

记 R53 的三次域为 $L$，正规闭包为 $H$，虚二次子域为
$F=\mathbb Q(\sqrt{-q})$。$2$ 在 $H/\mathbb Q$ 完全分裂。令
$(2)=\mathfrak l\overline{\mathfrak l}$ 于 $F$，并保留
$L$ 中 $\mathfrak p_0,\mathfrak p_+,\mathfrak p_-$ 的标号。

$H/L$ 的非平凡自同构交换 $F$ 的两个二进素理想。因此每个
$\mathfrak p_i\mathcal O_H$ 含两个不同的二进素理想：一个在
$\mathfrak l$ 上，另一个在 $\overline{\mathfrak l}$ 上。全部剩余次数均为一，所以
$$
N_{H/F}(\mathfrak p_i\mathcal O_H)
=\mathfrak l\overline{\mathfrak l}=(2).
$$
故复合映射
$$
\operatorname{Cl}(L)\longrightarrow\operatorname{Cl}(H)
\longrightarrow\operatorname{Cl}(F)
$$
将三个 $\mathfrak p_i$ 的类全部送到零。主理想生成元的范数相应为
$N_{L/\mathbb Q}(\alpha)\in\mathbb Q^\times$。

因此 R56 的 $42c_0=0$ 或 $43c_0=c_\pm$ 不能经这个自然转移推出
$F$ 中某一个范数二素理想的低次幂为主。虚二次域的正定范数下界虽然有效，却没有收到所需的非平凡类。要采用这条路线，必须另外构造一个不被上述范数杀掉的算术连接。

## 2. 现成纯三次和特殊单位族没有直接覆盖 R53

纯三次域的正规闭包二次子域是 $\mathbb Q(\sqrt{-3})$，而 R53 的二次预解式为
$\mathbb Q(\sqrt{-q})$、$q\ne3$。所以本域不是纯三次域；纯三次基本单位定理不能只因多项式“接近 $T^3-8n$”就套用。

核查的已发表原始来源包括 C. Levesque, “A class of fundamental units and some classes of Jacobi-Perron algorithms in pure cubic fields”, Pacific J. Math. **81** (1979), 447–466，[期刊全文](https://msp.org/pjm/1979/81-2/pjm-v81-n2-p13-s.pdf)。其对象为明确的纯三次族及附加整除条件，不是一般 $T^3-T-8n$。最简循环三次族则与本域的 $S_3$ 正规闭包、签名也不同。

另检索到 I. Kimura, H. Umemoto, “On explicit units in a family of cubic fields and the arithmetic of curves arising from powers of these units”, [arXiv:2611.07333](https://arxiv.org/abs/2611.07333)（2026-11-05）。这是新预印本，本笔记没有直接采用其中尚未独立证明的结果。其明确多项式族为
$$
T^3-3bT-b^3.
$$
若想只用一个有理缩放 $\theta=rT$ 将该式变成 R53 的
$T^3-T-8n$，比较系数必须满足
$$
3br^2=1,\qquad b^3r^3=8n,
$$
进而
$$
b^3=1728n^2.
$$
但 R53 的 $v_3(n)=1$，右侧三进赋值为五，不可能是有理数的立方。因此没有这种直接缩放。这里没有排除通过另一个二次生成元变换而得到偶然的域同构，但目前也未构造这种变换或由此得到单位。

简单的范数一候选还须真正检查整性。例如
$\theta/(\theta+1)$ 的范数虽为一，但在每个奇素数 $r\mid n$ 上，
$\theta$、$\theta+1$ 分别支撑于模 $r$ 的不同根所对应的素理想，所以它不是整单位。把范数一的分数元当作基本单位会漏掉这些分母。

## 3. 即使 2、3 都完全分裂，巨大判别式仍不迫使模三射线类阶很大

R56 §8 给出了普通类群版本的反检验。以下将其加强到**模三射线类群**，并保留 $2,3$ 全分裂。这个辅助族不具备 R53 的单素数判别式及其特殊多项式，因此不声称已经判断 R53 的关系。

令
$$
C=2^{42},\qquad B_0=(C+8)/9,
$$
并取任意正整数 $c\equiv36\pmod{96}$。考虑
$$
f_c(T)=T^3+3T^2+(B_0+3c)T+c,
$$
令 $\beta$ 为其根，置
$$
\alpha=1+3\beta,\qquad S=C-7+27c.
$$
直接代换给
$$
\alpha^3+6\alpha^2+S\alpha-C=0,\qquad
N(\alpha)=C.
\tag{N.1}
$$

### 3.1 不可约性与签名

式 (N.1) 左端的导数为
$$
3T^2+12T+S=3(T+2)^2+S-12>0.
$$
它在 $T=0$ 为负，在 $T=1$ 的值为 $27c>0$，所以唯一实根在 $(0,1)$。首一三次式若可约须有整数根，而这里只有一个实根且它不是整数，故不可约。所定义的域 $L_c$ 的签名为 $(1,1)$。

### 3.2 素数 3 完全分裂，且生成元满足射线条件

因为 $C=2^{42}\equiv10\bmod27$，
$$
B_0\equiv2\pmod3,\qquad c\equiv0\pmod3.
$$
所以
$$
f_c(T)\equiv T^3-T=T(T-1)(T+1)\pmod3
$$
有三个不同根。因此 $3$ 在最大整环中完全分裂，且按构造
$$
\alpha=1+3\beta\equiv1\pmod{3\mathcal O_{L_c}}.
$$

### 3.3 素数 2 完全分裂，并有实际的 42 次射线主关系

$c\equiv36\bmod96$ 给 $c\equiv4\bmod32$，从而
$$
S\equiv5\pmod{32}.
$$
式 (N.1) 在零附近有一个二进根，其赋值恰为 $42$。另一方面
$9-S\equiv4\bmod32$，可取 $s^2=9-S$、$v_2(s)=1$。二次式
$T^2+6T+S$ 的两个奇根是 $-3\pm s$。

在这两个近似根上，式 (N.1) 的值为 $-C$，赋值 $42$；其导数为
$2T(T+3)$，赋值恰为二。强 Hensel 引理给两个不同的奇根。故 $2$ 在 $L_c$ 完全分裂。

若 $\mathfrak p_0$ 对应那个偶根，则由 (N.1) 的范数和上述估值，
$$
(\alpha)=\mathfrak p_0^{42}.
$$
又 $\alpha\equiv1\bmod3$，所以确有
$$
\boxed{42[\mathfrak p_0]=0
\quad\text{于 }\operatorname{Cl}_{(3)}(L_c).}
\tag{N.2}
$$

### 3.4 最大判别式可无界

令
$$
H(t)=2t^2(t+3)+C.
$$
这个非恒定整数多项式的值有无穷多个素因子。可直接用 Schur 的初等论证：若素因子只在有限集合中，令 $P$ 为它们的乘积，取 $t=CPk$，则
$H(t)/C$ 是一个大于一且模 $P$ 同余于一的整数，矛盾。

故可取任意大的素数 $R\mid H(t)$，并排除有限集合
$R\mid6C(C+8)$。此时 $t\not\equiv0,-2\bmod R$。取
$$
S_0=-3t^2-12t\pmod R.
$$
则 $T^3+6T^2+S_0T-C$ 在 $T=t$ 处有二重根且非三重根。其判别式作为 $S$ 的多项式为
$$
D(S)=36S^2-4S^3+864C-27C^2-108CS.
$$
代入 $S_0$ 并使用 $H(t)=0\bmod R$，得到
$$
D'(S_0)=-108t(t+2)^3\not\equiv0\pmod R.
$$
因为 $S=C-7+27c$，其关于 $c$ 的导数也非零。可用 CRT 同时选择
$c\equiv36\bmod96$、$S\equiv S_0\bmod R$，并避开使判别式被 $R^2$ 除的唯一提升。于是
$$
v_R(\operatorname{disc}(\alpha))=1.
$$
最大整环指标平方不能消去这个奇赋值，所以 $R\mid D_{L_c}$。因此这些域的最大判别式无界，同时始终满足 (N.2) 和 $2,3$ 完全分裂。

这严格说明：单凭巨大最大判别式、单位秩一、$2,3$ 的完全分裂以及模三射线条件，不能推出 R56 第一个关系失败。R53 的**单素数判别式和其特殊三次形状**仍可能提供额外信息，但本轮尚未从中得到这种判定。

## 4. 接续方向

未得到 R53 的基本单位或三个射线类关系的数值判定。根会话将继续研究资源转向 R50 的实际交替矩阵条目：以单素数松弛 Selmer 类为基，将非对角条目写成固定 CM 除法域中的 Kummer 剩余符号，再检查椭圆单位的显式互反是否能提供这些类的具体生成元。该接口另写 R60，不把这里的辅助族扩展成主问题的反例。

