# 真实混合低孔核到稳定像的正则修正

日期：2026-11-13（UTC）。作者：boundary_next。状态：已证明的实际中间结论。

本稿支付 R254 第三附录之后的一条反向桥：**已经属于混合核且尾孔数有界**的输入，可以用实际慢算子的真右逆修正到 $N=\overline{BM}$，且修正误差具有明确的真实进位预算。

一个必要的域修正先单独完成：R239 原指数右逆只声明 $G_c:\mathscr X_c\to H$，不能据此宣称输出仍在 $\mathscr X_c$。本稿从它同一组实际有限头右逆和长进位误差重新支付输入、输出两种权，得到
$$
G_{7\to3}:\mathscr X_7\longrightarrow\mathscr X_3,\qquad
TG_{7\to3}=I.
$$
后面只有使用这个加强后的映射，才把修正向量放入 $M\cap\mathscr X_3\subset N$。

混合核的低孔交空间始终作为真实交空间定义。本稿不把到纯尾高阶核的投影改称为到混合核的投影，也不证明这些交空间已经逼近全部实际核。

## 1. 对象、截断和结论

沿用原负整数边界的两个实际算子
$$
T=T_N=\sum_{j\ge0}(j+1)^{-2}N_j
\quad\hbox{或}\quad
T=T_Y=\sum_{j\ge0}(j+1)^{-2}Y_j,
\qquad Y_j=N_j(I+N_j)^{-1},
$$
$$
M=\ker T,\qquad N=\overline{BM},\qquad \mathcal D=M\ominus N.
$$
这里 $\mathcal D$ 只表示缺陷空间；以下的纯尾删除另记 $D_m$。

设 $\mathsf P_q$ 为原全部物理位的 $q$ 孔层投影，并定义
$$
\|x\|_{\mathscr X_s}=\sum_{q\ge0}e^{sq}\|\mathsf P_qx\|,
\qquad \mathscr X_s=\{x:\|x\|_{\mathscr X_s}<\infty\}.
\tag{1.1}
$$
固定
$$
Q_0=2^{22},\qquad
C_G=\frac43 e^{4Q_0}.
\tag{1.2}
$$

按 R254 第三附录的原物理位号，移除第 $0$ 位后，令
$$
\eta=\eta_0=e^{-1070},\qquad b_j=(j+2)^{-2},
\qquad C=\hbox{归一化实际尾快速移位}.
$$
对应的实际慢尾记为
$\mathcal A=\sum b_j\bar N_j$ 或 $\mathcal A=\sum b_j\bar Y_j$。
取 $m\ge2$、$d=2^m$，头由原物理位 $1,\ldots,m$ 构成；令
$$
A_m=\mathcal A_m+D_m,\qquad
D_m=\sum_{j\ge m}b_jE_j.
\tag{1.3}
$$
其中 $\mathcal A_m,C_m$ 是真实有限头截断，$D_m$ 是独立的纯高尾删除。
已付清的实际估计是
$$
\|\mathcal A\|<\frac23,\quad \|A_m\|<\frac23,\quad
\|C\|=1,\quad\|C_m\|\le1,
$$
$$
\|\mathcal A-A_m\|\le26\eta_m,\qquad
\|C-C_m\|\le\eta_m,
\tag{1.4}
$$
$$
\eta_m=\exp[-1400d^4+630d^3-300d].
\tag{1.5}
$$

混合核符号为
$$
P_m=A_m^2-\eta C_m\quad(N),\qquad
P_m=A_m^2-\eta C_m(I+A_m)^2\quad(Y).
\tag{1.6}
$$
令 $P_{\le Q}^{\rm tail,m}$ 只截断第 $m$ 位之后的尾孔数；这里采用移除首位后的尾位号，所以对应原物理位 $m+1,m+2,\ldots$。
定义闭子空间
$$
\boxed{\quad
V_{m,Q}=\ker P_m\cap\operatorname{Ran}P_{\le Q}^{\rm tail,m},
\qquad Q\in\mathbb N_0.
\quad}
\tag{1.7}
$$
其向量允许在位置指标上有无限支撑。

定义真实和混合的多项式图算子
$$
H=\mathcal A,\quad H_m=A_m\quad(N),
$$
$$
H=(I-\eta C)\mathcal A-\eta C,\quad
H_m=(I-\eta C_m)A_m-\eta C_m\quad(Y),
\tag{1.8}
$$
以及 $J u=(u,-Hu)$、$J_mv=(v,-H_mv)$。实际 $M$ 中每个向量唯一为 $w=Ju$，$u$ 属于真实平方核 $K$。

**定理。** 存在线性映射
$$
\Lambda_{m,Q}:V_{m,Q}\longrightarrow M\cap\mathscr X_3\subset N
\tag{1.9}
$$
使
$$
\boxed{\quad
\|\Lambda_{m,Q}v-J_mv\|
\le \delta_{m,Q}\|v\|,
\quad}
\tag{1.10}
$$
其中可明确取
$$
\boxed{\quad
\delta_{m,Q}
=130 C_G
\sqrt{(2m+5)(Q+m+2)}\,
e^{7(Q+2m+3)}\eta_m .
\quad}
\tag{1.11}
$$
因而对每个真实 $w=Ju\in M$，
$$
\boxed{\quad
\operatorname{dist}(w,N)
\le\frac54\operatorname{dist}(u,V_{m,Q})
+(27\eta_m+\delta_{m,Q})\|u\|.
\quad}
\tag{1.12}
$$
特别，对
$$
Q=50d^3,\qquad m\ge4,
$$
有
$$
\boxed{\quad
\delta_{m,50d^3}\le e^{-1000d^4},\qquad
27\eta_m\le e^{-1300d^4}.
\quad}
\tag{1.13}
$$

以下逐项证明，尤其不省略 $\mathscr X_7$ 残差与 $\mathscr X_3$ 输出。

## 2. 同一实际右逆的输入、输出权损失

### 2.1 已证有限头右逆的具体输入

使用 [R239 指数右逆附录](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) A.2--A.6、A.11 中的实际构造。对每个 $q\ge0$，置
$$
x=q+Q_0,\qquad
t=t(q)=\left\lceil\frac12\log_2x\right\rceil,\qquad
a=2^t.
\tag{2.1}
$$
本节的 $a$ 是有限头长度，不是慢行系数。则
$$
\sqrt x\le a<2\sqrt x,\qquad t\le\sqrt x.
\tag{2.2}
$$
R239 的阈值为 $\kappa_{**}=2+2\log(3/2)$。参数 $Q_0$ 合法：
$$
\frac{20\log Q_0}{\sqrt{Q_0}}
<\frac{20\cdot22\cdot0.7}{2048}<0.18
<3-\kappa_{**}.
\tag{2.3}
$$
最后使用 $\log2<0.7$、$\log(3/2)<0.41$。其余 $Q_0\ge64$ 等要求显然满足。

因此同一构造给实际有限头加纯尾右逆
$$
R_q:\mathcal H_q\longrightarrow H,
$$
满足
$$
\|R_q\|\le e^{3x},\qquad
R_q\mathcal H_q\subseteq\mathcal H_{\le q+a+t}.
\tag{2.4}
$$
此外
$$
(TR_q-I)v=\sum_{\ell\ge0}K_{t+\ell}R_qv,\qquad v\in\mathcal H_q,
\tag{2.5}
$$
其中
$$
\|K_L\|\le52e^{-770\,16^{L-1}},
\qquad K_L\hbox{ 只作用原前 }L+1\hbox{ 位}.
\tag{2.6}
$$
(2.4)--(2.6) 都是原实际构造的结论，不是全形式逆的有界性假设。

### 2.2 输出在 $\mathscr X_3$ 中的绝对求和

若 $b=q+a+t$，则 $b\le q+3\sqrt x$、$b+1\le2x$。由有限孔次数支撑和 Cauchy--Schwarz，
$$
\|R_qv\|_{\mathscr X_3}
\le\sqrt{b+1}\,e^{3b}\|R_qv\|
\le \exp\!\left(3q+3x+9\sqrt x+\tfrac12\log(2x)\right)\|v\|.
$$
对 $x\ge Q_0$，
$$
\tfrac12\log(2x)\le\sqrt x,\qquad 10\sqrt x\le x.
$$
于是
$$
\boxed{\quad
\|R_qv\|_{\mathscr X_3}
\le e^{7q+4Q_0}\|v\|.
\quad}
\tag{2.7}
$$
故
$$
Rz=\sum_{q\ge0}R_q\mathsf P_qz
\tag{2.8}
$$
对每个 $z\in\mathscr X_7$ 在 $\mathscr X_3$ 中绝对收敛，并且
$$
\|R\|_{\mathscr X_7\to\mathscr X_3}\le e^{4Q_0}.
\tag{2.9}
$$
这里允许每个 $R_qv$ 涉及无限多个位置；只使用其真实孔次数界。

### 2.3 误差在 $\mathscr X_7$ 中的行、列加权和

用等价范数
$$
\|z\|_{7,Q_0}=e^{7Q_0}\|z\|_{\mathscr X_7}.
$$
(2.5) 中第 $\ell$ 项的输出孔次数不超过
$$
b_\ell=q+a+2t+\ell+1.
$$
由 $a+2t+1\le4\sqrt x+1\le x$，有
$$
b_\ell+Q_0\le2x+\ell,\qquad b_\ell+1\le2x+\ell.
$$
对每个输入列 $v\in\mathcal H_q$，逐输出行求和给
$$
\begin{aligned}
\|K_{t+\ell}R_qv\|_{7,Q_0}
&=\sum_{p=0}^{b_\ell}e^{7(p+Q_0)}
 \|\mathsf P_pK_{t+\ell}R_qv\|\\
&\le52\sqrt{b_\ell+1}\,
 \exp[3x+7(b_\ell+Q_0)-770\,16^{t+\ell-1}]\|v\|.
\end{aligned}
\tag{2.10}
$$
这一步将全部输出行都包含在内，没有只估计某一指定行。

因为 $770\,16^{t+\ell-1}=48.125\,a^4 16^\ell$，且对 $x\ge64$、$\ell\ge0$
$$
\log52+\tfrac12\log(2x+\ell)\le x16^\ell,
\qquad \ell\le16^\ell,
$$
(2.10) 的指数至多
$$
-48.125\,a^4 16^\ell+29x16^\ell
\le-40\,a^4 16^\ell.
\tag{2.11}
$$
最后使用 $a^4\ge x^2$、$x\ge Q_0>29/8$。
于是长进位级数在 $\mathscr X_7$ 中绝对收敛，且
$$
\|(TR_q-I)v\|_{7,Q_0}
\le 2e^{-40a(q)^4}\|v\|.
\tag{2.12}
$$

定义 $Ez=\sum_q(TR_q-I)\mathsf P_qz$。对于有限列和，先对每一输出行使用三角不等式，再对全部行求加权和，(2.10)--(2.12) 给
$$
\begin{aligned}
\|Ez\|_{7,Q_0}
&\le\sum_{q\ge0}2e^{-40a(q)^4}\|\mathsf P_qz\|\\
&\le
\left[\sup_{q\ge0}2e^{-40a(q)^4-7(q+Q_0)}\right]\|z\|_{7,Q_0}\\
&<\frac14\|z\|_{7,Q_0}.
\end{aligned}
\tag{2.13}
$$
绝对收敛使同一不等式延至整个 $\mathscr X_7$。因此
$$
E:\mathscr X_7\to\mathscr X_7,\qquad\|E\|<\frac14.
\tag{2.14}
$$

由实际 $T$ 在 $H$ 上有界，有限列的 $TR=I+E$ 传到极限；这与 R239 已证 $T:\mathscr X_3\to\mathscr X_3$ 的作用相同。置
$$
\boxed{\quad
G_{7\to3}=R(I+E)^{-1}.
\quad}
\tag{2.15}
$$
Neumann 级数在 $\mathscr X_7$ 中收敛，(2.9)、(2.14) 遂给
$$
\boxed{\quad
TG_{7\to3}=I,\qquad
\|G_{7\to3}\|_{\mathscr X_7\to\mathscr X_3}
\le\frac43e^{4Q_0}=C_G.
\quad}
\tag{2.16}
$$
这一步正是原 $\mathscr X_c\to H$ 定理之外所补的输出域结论。

还将使用 R239 A.7--A.8 的真实稳定像后果
$$
\boxed{M\cap\mathscr X_3\subset N.}
\tag{2.17}
$$
其理由是：对任意 $f\in N^\perp$，唯一规范形式原像满足逐层
$\|h_q\|\le C e^{3q}\|f\|$，并在 $\mathscr X_3$ 上合法配对为
$\langle h,Tg\rangle=\langle f,g\rangle$。
若 $g\in M\cap\mathscr X_3$，则右端为零，故 $g\in(N^\perp)^\perp=N$。
不需要假设 $P_{\mathcal D}g$ 保持指数矩。

## 3. 真实截断差在 $\mathscr X_7$ 中的明确预算

令
$$
T^{[h]}=(T|_{\mathcal F_h})\otimes I+
 \sum_{i\ge h}(i+1)^{-2}E_i
\tag{3.1}
$$
为原物理前 $h$ 位的真实有限头加纯尾。
[R216](../results/R216-uniform-occupied-prefix-decay-in-actual-slow-kernels.md) §8.1 的真实链和 Cayley 逆差给
$$
\|T-T^{[h]}\|\le26\eta_{h-1}.
\tag{3.2}
$$
这里 $Y$ 型用的是真实 $(I+N_i)^{-1}$ 与真实有限头逆，范数均不超过 $3$；(3.2) 没有删除 Cayley 分母。

取
$$
K_L=T^{[L+1]}-T^{[L]}.
$$
它只作用原前 $L+1$ 位，且由 (3.2)
$$
\|K_L\|\le26(\eta_{L-1}+\eta_L)\le52\eta_{L-1}.
\tag{3.3}
$$
范数望远镜极限准确给
$$
T-T^{[m+1]}=\sum_{L\ge m+1}K_L.
\tag{3.4}
$$

任一这样的局部算子最多改变 $L+1$ 个孔。逐输入孔层并对最多 $2L+3$ 个输出孔层作 Cauchy--Schwarz，有
$$
\|K_L\|_{\mathscr X_7\to\mathscr X_7}
\le52\sqrt{2L+3}\,e^{7(L+1)}\eta_{L-1}.
\tag{3.5}
$$
置 $\Phi(k)=-\log\eta_k=1400\,16^k-630\,8^k+300\,2^k$。则
$$
\Phi(k+1)-\Phi(k)
=21000\,16^k-4410\,8^k+300\,2^k\ge16590
\quad(k\ge0).
\tag{3.6}
$$
所以 (3.5) 相邻主项之比小于
$\sqrt2 e^{7-16590}<1/2$。求和 (3.4) 得到
$$
\boxed{\quad
\|T-T^{[m+1]}\|_{\mathscr X_7\to\mathscr X_7}
\le104\sqrt{2m+5}\,e^{7(m+2)}\eta_m.
\quad}
\tag{3.7}
$$
该级数在 $\mathscr X_7$ 中收敛，且其 $H$ 中极限就是实际截断差。
(3.7) 保留原物理跨界的准确 $\eta_m$，不改成粗 $e^{-770d^4}$。

## 4. 真实混合核的首位图与全部 Cayley 因子

记 $R_m=\eta C_m$。按原最低位分成两行，实际混合截断有
$$
T_N^{[m+1]}=
\begin{pmatrix}A_m&I\\R_m&A_m\end{pmatrix}.
\tag{4.1}
$$
因此 $P_mv=0$ 直接给 $J_mv=(v,-A_mv)\in\ker T_N^{[m+1]}$。

在 $Y$ 型，准确首位 Cayley 计算给
$$
\begin{pmatrix}I-R_m&0\\0&I-R_m\end{pmatrix}
T_Y^{[m+1]}
=
\begin{pmatrix}H_m&I\\R_m&H_m\end{pmatrix},
\tag{4.2}
$$
其中 $H_m=(I-R_m)A_m-R_m$。左乘子可逆，因为 $\|R_m\|\le\eta<1$。

所有这些尾函数交换，故有准确代数恒等式
$$
H_m^2-R_m
=(I-R_m)\bigl[A_m^2-R_m(I+A_m)^2\bigr]
=(I-R_m)P_m.
\tag{4.3}
$$
因此对 $P_mv=0$，两行均给
$$
\boxed{T^{[m+1]}J_mv=0}
\tag{4.4}
$$
而没有使用近似分式。
若与 R254 的 $Z_m=A_m(I+A_m)^{-1}$ 图字典核对，则
$$
H_m-Z_m=P_m(I+A_m)^{-1},
\tag{4.5}
$$
所以 $H_mv=Z_mv$ 在 $\ker P_m$ 上准确成立。
$(I+A_m)^{-1}$ 是真实有界逆，因 $\|A_m\|<2/3$ 而范数小于 $3$。

两个模型统一有
$$
\|H_m\|,\|H\|
\le\frac23+\frac53\eta<\frac34.
$$
于是
$$
\boxed{\quad \|J_m\|,\|J\|\le\frac54.\quad}
\tag{4.6}
$$
这里将 $J,J_m$ 视为在整个尾空间上的图映射，因而也能用于不必属于相同核的差向量。

由 (1.4)，$N$ 型图差至多 $26\eta_m$。在 $Y$ 型，准确分解给
$$
H-H_m=(I-\eta C)(\mathcal A-A_m)
-\eta(C-C_m)(I+A_m),
$$
所以
$$
\|H-H_m\|
\le\left[26(1+\eta)+\frac53\eta\right]\eta_m
<27\eta_m.
\tag{4.7}
$$
两型因此统一满足
$$
\boxed{\quad
\|(J-J_m)u\|\le27\eta_m\|u\|.
\quad}
\tag{4.8}
$$

最后，若 $v\in V_{m,Q}$，则 $A_m,C_m,H_m$ 都不增加纯高尾孔数：其中只有 $D_m$ 改变该次数，且降低一。有限头自身只占 $m$ 位，首位图再增加至多一个原首位孔。因此
$$
\boxed{\quad J_mv\in\mathcal H_{\le Q+m+1}.\quad}
\tag{4.9}
$$
这说明其属于所有有限指数孔空间，不要求位置有限。

## 5. 修正到实际核与稳定像

取 $v\in V_{m,Q}$，置 $w_m=J_mv$。
由 (4.4)，
$$
Tw_m=(T-T^{[m+1]})w_m.
\tag{5.1}
$$
由 (4.6)、(4.9)，
$$
\|w_m\|_{\mathscr X_7}
\le\sqrt{Q+m+2}\,e^{7(Q+m+1)}\|w_m\|
\le\frac54\sqrt{Q+m+2}\,e^{7(Q+m+1)}\|v\|.
\tag{5.2}
$$
把 (3.7) 直接用于此向量，得到实际残差的全指数范数
$$
\boxed{\quad
\|Tw_m\|_{\mathscr X_7}
\le130\sqrt{(2m+5)(Q+m+2)}
\,e^{7(Q+2m+3)}\eta_m\|v\|.
\quad}
\tag{5.3}
$$
这不是从环境范数误差自动推断加权误差。

定义
$$
\boxed{\quad
\Lambda_{m,Q}v
=J_mv-G_{7\to3}TJ_mv.
\quad}
\tag{5.4}
$$
(5.3) 支付 $G_{7\to3}$ 的真实输入域，而 (2.16) 给输出在 $\mathscr X_3$。
于是
$$
T\Lambda_{m,Q}v=0,\qquad
\Lambda_{m,Q}v\in\mathscr X_3,
$$
从 (2.17) 得
$$
\Lambda_{m,Q}v\in M\cap\mathscr X_3\subset N.
\tag{5.5}
$$
再用 (2.16)、(5.3)，就得到 (1.10)--(1.11)；事实上修正误差在 $\mathscr X_3$ 范数中也满足同一个上界。

这个构造未断言 $\Lambda_{m,Q}v$ 必为一个实际 $BM$ 向量；它已严格落入目标闭稳定像 $N=\overline{BM}$，这正足以用于下面的距离估计。

## 6. 窗口 $Q=50d^3$ 的数值预算

由 (1.2)、(1.5)、(1.11)，在 $Q=50d^3$ 时
$$
\begin{aligned}
\log\delta_{m,Q}
={}&-1400d^4+980d^3-300d+2^{24}\\
&+\log(520/3)
+\tfrac12\log[(2m+5)(50d^3+m+2)]
+14m+21.
\end{aligned}
\tag{6.1}
$$
对 $m\ge4$、$d\ge16$，有
$$
m\le d/2,\quad 2m+5\le2d,\quad
50d^3+m+2\le51d^3,
$$
$$
\log(520/3)<6,\qquad
\tfrac12\log(102d^4)<3+2\log d.
$$
故第二行的正项至多
$$
30+7d+2\log d\le d^2.
\tag{6.2}
$$
例如 $2\log d\le d/2$，而 $30+(15/2)d\le d^2$ 对 $d\ge16$ 成立。

丢掉 $-300d$，再用
$$
2^{24}\le256d^4,\qquad 980d^3\le64d^4,\qquad d^2\le d^4,
$$
便有
$$
\log\delta_{m,50d^3}\le(-1400+256+64+1)d^4
=-1079d^4\le-1000d^4.
\tag{6.3}
$$
此外
$$
\log(27\eta_m)
\le4-1400d^4+630d^3-300d
\le-1300d^4
\quad(d\ge16).
\tag{6.4}
$$
因此 (1.13) 对全部 $m\ge4$ 成立，不只是渐近断言。

更一般地，对每个固定 $\lambda>0$，取 $Q=\lfloor\lambda d^3\rfloor$ 时，
$$
\log\delta_{m,Q}=-(1400+o(1))d^4.
\tag{6.5}
$$
(6.5) 只描述本反向修正的成本，不扩大 R254 第三附录已经证明的纯尾窗口范围。

## 7. 明确的距离估计与真正缺陷的投影间隙

取真实 $w=Ju\in M$。因为 $V_{m,Q}$ 是两个闭子空间的交，它有唯一最小距离点 $v_0$，且
$$
\|u-v_0\|=\operatorname{dist}(u,V_{m,Q}),\qquad \|v_0\|\le\|u\|.
$$
这里取的是对交空间本身的正交投影；没有声称它等于
$P_{\ker P_m}P_{\le Q}^{\rm tail,m}$，也不交换这两个投影。

由 $\Lambda_{m,Q}v_0\in N$、(4.6)、(4.8)、(1.10)，
$$
\begin{aligned}
\operatorname{dist}(w,N)
&\le\|Ju-\Lambda_{m,Q}v_0\|\\
&\le\|(J-J_m)u\|+\|J_m(u-v_0)\|
  +\|J_mv_0-\Lambda_{m,Q}v_0\|\\
&\le\frac54\operatorname{dist}(u,V_{m,Q})
  +(27\eta_m+\delta_{m,Q})\|u\|.
\end{aligned}
\tag{7.1}
$$
这证明 (1.12)，常数未乘在未知普通 Hilbert 尾上。

若 $0\ne w=Ju\in\mathcal D$，则
$\operatorname{dist}(w,N)=\|w\|$，且 $\|u\|\le\|w\|$。从而
$$
\boxed{\quad
\operatorname{dist}(u,V_{m,Q})
\ge\frac45(1-27\eta_m-\delta_{m,Q})\|w\|.
\quad}
\tag{7.2}
$$
若括号为负，该不等式只给平凡界；对匹配窗口 $Q=50d^3,m\ge4$，其明确为
$$
\boxed{\quad
\operatorname{dist}(u,V_{m,50d^3})
\ge\frac45(1-2e^{-1000d^4})\|w\|.
\quad}
\tag{7.3}
$$
这是确实使用 $w\perp N$ 的缺陷专属间隙。它不假设缺陷非零。

相应地，若某个实际 $u\in K$ 沿 $m\to\infty$ 的一条子列满足
$$
\operatorname{dist}(u,V_{m,50d^3})\longrightarrow0,
\tag{7.4}
$$
则 (7.1) 迫 $Ju\in N$。若 (7.4) 对全部 $u\in K$ 成立，才可推出 $N=M$。

R254 第三附录目前给的是
$$
\operatorname{dist}(u,\ker D_m^{\,2d})
\le\tau_{50d^3}(u)+e^{-500d^4}\|u\|.
$$
纯尾高阶核通常大于 $\ker P_m$；该结论尚不提供 (7.4)。本稿把从真实混合低孔核到实际稳定像的后半桥完整支付，仍须解决前半桥的混合有限模块或其他缺陷专属能量。

