# R914 — 原非稳定四块核的八／九步截止与同源联合秩

日期：2026-11-16。**状态：以下实际有限截止、同来源链映射及整个原核的维数限制已证明。指定 forcing 和主目标仍未完成。**

本篇回到原 $T-h\le L\le h$ 也允许的窗口。
不逐项令 R907 的反馈系数 $a_i$ 为零。
先以同一个六次多项式 $Q_f(\mathcal T)$ 合成，
准确进入整个零纤维为零的原子空间，
再使用 R911 已付五／六长根界。
这样把先前随 $b$ 增长的续接测试缩到固定八或九步；
结论同时约束非稳定部分，而不将整个核认成稳定。

## 1. 共同原来源与精确假设

保持
[R907](R907-original-two-step-successor-and-six-dimensional-fiber-feedback.md)
的原十九角曲面、几何整曲线 $C=(F=0)$、$P=(0,1)$、
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad \kappa=C^2,\quad
b=\deg_YF,\quad \mathcal E=Y\partial_Y,
$$
以及已付同预算整返回
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D}.
\tag{1}
$$
仍取原 $r=2,\ C.f_0=3,\ b\ge5$ 范围，
$3b<p,\ p>211,\ F(t,0)\ne0$、$\gamma=(\mathcal EF)(P)\ne0$。
设 $g=\psi\exp\eta$、$\operatorname{ord}\eta=h$，并保
$$
\boxed{
h<T\le2h,\quad T-h>\kappa,\quad
T-h\le L<T,\quad
T=s-r-13,\quad L=\max(\ell-r,0).
}
\tag{2}
$$
**不假设 $L>h$。** 特别包含同一 unit-cofactor quartic 来源实际要求的
$L\le h$，而不重复 R911§5.1 已划出的不适用范围。

记实际四块核
$$
K=\{G\in\mathcal H_3:
(\mathcal E^jG)(t,g)\in(t^T)\ (0\le j\le2),\
(\mathcal E^3G)(t,g)\in(t^L)\},
$$
$$
V_i(G)=(\mathcal E^iG)|_C,\quad
V_T=H^0(C,N^3(-TP)),\quad n_T=\dim_kV_T.
\tag{3}
$$
$V_0,V_1:K\to V_T$ 是 R834/R902 的实际单射。
$n_T$ 保留为真实维数，不能未付非特殊性便用 Riemann–Roch 的 Euler 特征代替。

令
$$
a(G)=\frac{(\mathcal E^4G)(P)}{6\gamma^3},\qquad
\mathcal TG=\mathcal EG-a(G)F^3.
\tag{4}
$$
对 $G,H\in K$，R907 已给
$$
V_1(G)=V_0(H)\quad\Longleftrightarrow\quad
H=\mathcal TG\in K.
\tag{5}
$$
其中等号是整个 $C$ 上的限制截面相等。
在当前 $L\le h$ 范围，$a(G)$ 可以非零，本文不将其删除。

置
$$
R_C=3(e_++\mu_{0,1}),\qquad e_+=C.H_+.
$$
R907 的逐 charge 原帽给
$$
0\ne H\in\mathcal H_3
\quad\Longrightarrow\quad
v_H:=\min_n\operatorname{ord}_0[Y^n]H\le R_C<T.
\tag{6}
$$
原实际 $g$ 只在读过的 $T<s-4$ 窗口与参考 $\rho$ 相同。
后面的根能量仍只用这份身份，不延长四轴的实际窗口。

## 2. 六次合成准确消去全部反馈，而非分别选择 a_i

保持 R907 的原空间
$$
\mathscr A=\{G\in\mathcal H_3:
(\mathcal E^jG)(P)=0,\ 0\le j\le3\},
$$
$$
\mathscr A_t=\{G\in\mathscr A:G(0,Y)\equiv0\}.
\tag{7}
$$
$K\subset\mathscr A$，$\mathcal T$ 保 $\mathscr A$。
$\mathscr A_t$ 要求整个零纤维多项式为零，而非只在 $P$ 的若干 jet 为零。
因此
$$
\boxed{\mathcal T|_{\mathscr A_t}=\mathcal E,\qquad
\mathcal E\mathscr A_t\subset\mathscr A_t.}
\tag{8}
$$

写 $f(Y)=F(0,Y)$，$\deg f\le3$，
$c_n=[Y^n]f^3$，缺项补零至 $n=9$。
R907 的首一六次多项式为
$$
Q_f(Z)=
\frac{\prod_{n=0}^{9}(Z-n)}{6\gamma^3}
\sum_{n=0}^{9}\frac{c_n}{Z-n},
\qquad \deg Q_f=6.
\tag{9}
$$
其全源结论是
$$
\boxed{Q_f(\mathcal T)\mathscr A\subset\mathscr A_t.}
\tag{10}
$$
它由实际零纤维六维算子的特征多项式给出，
没有假定整个 $K$ 稳定，也没有假定任意零纤维值有全局提升。

特别，对任意 $G\in K$，置
$$
H=Q_f(\mathcal T)G.
\tag{11}
$$
则所有后续迭代准确有
$$
\mathcal T^jH=\mathcal E^jH\qquad(j\ge0).
\tag{12}
$$
这里并未认定这些截面在 $K$ 中。
(12) 是先作同源六次合成后由整个零纤维消失得到的恒等式；
不是对 $G,\mathcal TG,\ldots$ 各自添加 $a_i=0$ 条件。

## 3. R911 的能量界在这里不需要 L>h

R911 命题2的证明仅需要：
原 $H\in\mathcal H_3$、$v_H<T\le s$、
$g\equiv\rho\bmod t^T$，以及同一个 $H$ 的五或六条实际长零。
它的根引理、全部重复次数、最近根截断、十九角 forcing 和真实 $3C$ 成本
都不使用 $L>h$。
那个条件仅在 R911§4 把普通后继链直接识别为 Euler 链时使用。

因此本篇可原样使用以下两条已付准确界：
$$
\begin{aligned}
0\ne H\in\mathcal H_3,\ 
\mathcal E^jH(t,g)\in(t^T)\ (0\le j\le4)
&\ \Longrightarrow\
13(T-v_H)\le27\kappa+312b,\\
0\ne H\in\mathcal H_3,\ 
\mathcal E^jH(t,g)\in(t^T)\ (0\le j\le5)
&\ \Longrightarrow\
16(T-v_H)\le27\kappa+384b.
\end{aligned}
\tag{13}
$$
没有在本篇重新假定 squarefree、限制因子重复次数，
或把 $\mathcal H_3$ 扩大到环境多项式格。

定义两个实际有限参数门
$$
\mathsf A_5:\quad 13(T-R_C)>27\kappa+312b,
$$
$$
\mathsf A_6:\quad 16(T-R_C)>27\kappa+384b.
\tag{14}
$$

## 4. 真稳定部分准确在八或九步内被识别

仍定义
$$
K_\infty=\{G\in K:\mathcal T^jG\in K\text{ 对所有 }j\ge0\},
\qquad d_\infty=\dim_kK_\infty.
$$
R907 在原帽 $R_C<T$ 下给
$$
d_\infty\le6,\qquad Q_f(\mathcal T)K_\infty=0.
\tag{15}
$$

**定理 1。** 在 $\mathsf A_5$ 下，
$$
\boxed{K_\infty=\bigcap_{j=0}^{8}\mathcal T^{-j}K;}
\tag{16}
$$
在 $\mathsf A_6$ 下，
$$
\boxed{K_\infty=\bigcap_{j=0}^{9}\mathcal T^{-j}K.}
\tag{17}
$$
这些是同一个实际四块测试的有限交，
不将其中任何额外测试赋给任意 $G\in K$。

**证明。** 只须证明有限交包含于 $K_\infty$。
先取 $\mathsf A_5$，设 $G_j=\mathcal T^jG\in K$ 对 $0\le j\le8$ 成立。
对 (11) 的 $H$，因 $Q_f$ 的次数为六且系数属于共同常数域，
$$
H,\quad \mathcal TH,\quad\mathcal T^2H
$$
分别是同一列 $G_0,\ldots,G_8$ 的线性组合，所以都在 $K$。
由 (10)–(12)，它们准确等于 $H,\mathcal EH,\mathcal E^2H$。
每一个都有原前三条长零，合在一起便给
$\mathcal E^jH(t,g)\in(t^T)$，$0\le j\le4$。
若 $H\ne0$，(6)、(13) 与 $\mathsf A_5$ 矛盾。
故
$$
Q_f(\mathcal T)G=0.
$$
$Q_f$ 首一六次，而 $G_0,\ldots,G_5$ 已在 $K$，
同一个线性递推遂迫所有后续 $\mathcal T^jG$ 都在 $K$，
即 $G\in K_\infty$。

$\mathsf A_6$ 的证明完全相同：
$G_0,\ldots,G_9$ 使
$H,\mathcal EH,\mathcal E^2H,\mathcal E^3H$ 都在 $K$，
准确得到 $H$ 的六条长零，
再用 (13) 的第二界。证毕。

所以在 $\mathsf A_5$ 下，每个非稳定的非零 $G\in K$
必须在前八次真实后继中失败；
$\mathsf A_6$ 时至多九次。
失败仍是 R907(11) 的完整同源尾条件之一，
不把它换成一个可自由选择的原点标量。

## 5. 整个原核的联合秩界

对 $j=8$ 或 $9$ 定义同源链映射
$$
\mathcal C_j:K^{j+1}\to V_T^j,\qquad
(G_0,\ldots,G_j)\longmapsto
(V_1G_0-V_0G_1,\ldots,V_1G_{j-1}-V_0G_j).
\tag{18}
$$
由 (5)，投到第一坐标把其核准确识别为
$\bigcap_{i=0}^{j}\mathcal T^{-i}K$。
不存在独立选择后继的自由度；若第一坐标为零，
$V_0$ 的单射也逐项迫其余坐标为零。

故在相应的 (14) 下，
$$
\ker\mathcal C_8\simeq K_\infty
\quad\text{或}\quad
\ker\mathcal C_9\simeq K_\infty.
$$
仅用目标的真实维数，不假定链映射满射，得到
$$
\boxed{
9\dim K\le8n_T+d_\infty\le8n_T+6
\quad(\mathsf A_5),
}
\tag{19}
$$
$$
\boxed{
10\dim K\le9n_T+d_\infty\le9n_T+6
\quad(\mathsf A_6).
}
\tag{20}
$$
同时保已有 $\dim K\le n_T$，所以精确可取两者的较小上界。
例如 $\mathsf A_5$ 时
$$
n_T-\dim K\ge
\left\lceil\frac{n_T-d_\infty}{9}\right\rceil.
$$
这限制整个非稳定核；并非只重复 $d_\infty\le6$。
原 $\mathcal H_3$ 四块像秩至少为
$\dim\mathcal H_3-\min(n_T,\lfloor(8n_T+6)/9\rfloor)$，
另一个门同理。
与其它显示单位块相加仍须先支付实际交，不作形式秩相加。

在 R911 已明示的实际二次区域，$\mathsf A_5$ 或 $\mathsf A_6$
可按其完整有限条件读取。
本篇没有改变 $D/s/\ell$ 的原预算，也不把 (14) 当作对全部参数自动成立。

## 6. 指定留数与非稳定 forcing 仍是同一个类

R907§8 的原指定行
$$
\Lambda(G)=\mathfrak G_F(q_{\rm src}t^rG)
$$
及其两个实际分歧迹 $m_4,m_5$ 在本篇不变。
特别仍有
$$
\begin{aligned}
\Lambda(Q_f(\mathcal T)G)
={}&\Lambda(Q_f(\mathcal E)G)
-\frac{(\mathcal E^4G)(P)}{6\gamma^3}(m_5-45m_4)\\
&-\frac{(\mathcal E^5G)(P)}{6\gamma^3}m_4.
\end{aligned}
\tag{21}
$$
只有在 (16) 或 (17) 的全部实际测试已经成立，
或已经另证 $G\in K_\infty$ 时，
本篇才将 (21) 左边置零。
不能因 $Q_f(\mathcal T)G$ 的零纤维为零便删它，
也不能把 $m_4,m_5$ 或两个原点 jet 当作自由参数或单位。

对同一非空仿射 forcing 纤维，(19)–(20) 限制它的差空间；
并未判该纤维为空，也未判 $\Lambda$ 或原 $[b_0]$ 在其上为零或非零。
固定边界补偿、原点短尾、十九角和 conductor、
全部 $q_{\rm src}$ 导数、唯一 $V_2$、
同 $K_{\rm corr}/H_{\rm corr}$、完整 $R/S$、
三个十三行带、末端四次 carry 及下一精度都保留。
原全 $\mathcal W_D$ 的其余列也未缩成这个已付 $\mathcal H_3$ 子格。

依赖：R907 全来源反馈及六维零纤维、R911 固定五／六长根界，
以及它们所引用的 R680/R837 全十九角和全重复因子成本。
本篇是精确线性与原来源证明，没有新运行或数据。
