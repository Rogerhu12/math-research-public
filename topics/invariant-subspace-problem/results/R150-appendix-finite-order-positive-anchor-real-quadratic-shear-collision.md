# R150 附录：有限阶正主行关闭实 β4 普通一次剪切碰撞

日期：2026-11-13（UTC）。kernel_resume_1cf / Astra-ISP-1cf8c51d；根全文核验完整二次域、去复倾斜、两个真实正 first 限制和循环性返回。
状态：完整证明，普通一次符号 $r=1$。全部点态高幂另作伴随图证明，不在此处由自然幂替换。

## 1. 定理与已闭范围扣除

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
v=c_*+\sum_{j\ge0}c_j\chi_j,
$$
其中 $a_*,c_*\in\mathbb R$，
$$
a_j\ge0,\quad a\in\ell^2\setminus\ell^1,\quad
a_0=\alpha>0,\qquad c_j\in\mathbb R,\quad |c_j|\le C_0a_j.
\tag{1.1}
$$
定义
$$
\Theta_a(t)=\sum_j\lfloor t a_j\rfloor.
$$
假设存在 $p>1,\gamma>0$，使充分大 $t$ 有
$$
\Theta_a(t)\ge\gamma t^p.
\tag{1.2}
$$
主行的任意物理排列均可；(1.2) 是排序计数条件。

则对任意 $\lambda\in\mathbb C$ 以及任意复 $\ell^2$ 指数权
$w=b_*+\sum b_j\chi_j$，
$$
\boxed{
\bigl[(v-u^2)^2-4\alpha^2u^2-\lambda\bigr]e^w
\text{ 对 }A\text{ 循环}.
}
\tag{1.3}
$$

若 $a_j\ge c(j+1)^{-\sigma}$，$1/2<\sigma<1$，
或下降重排满足该下界，则 (1.2) 成立。
特别
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\quad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,\quad
\frac12<\sigma<1
\tag{1.4}
$$
的普通一次实碰撞现全部 $\lambda,w$ 关闭。
$\sigma=1$ 不从本稿的有限阶条件自动得到。

先前 R150 剪切附录已关闭 $\beta\ne4\alpha^2$ 的
$(v-u^2)^2-\beta u^2-\lambda$；
非实最高中心也已由跨核实结构附录关闭。
本稿新增的正是剩余实碰撞，在 (1.1)—(1.2) 下的完整排核。
R236 的一条非可和主行与可和辅助行结论没有预先覆盖 (1.4) 的第二无界方向。

## 2. 已核接口：真实有界分支与两个定量引理

使用以下完整结果。

1. [R150：非临界支与有界尾归一化](R150-appendix-real-collision-noncritical-branch-and-bounded-tail-normalization.md)：
令 $X=X_{u,b}$、$Y=X_{v,b}$ 为真实倾斜 first，
$L=X^{-1}$，$B=B_{20}$ 为真实二阶主 Bell 系数。
普通符号
$$
F(x,y)=(y-x^2)^2-4\alpha^2x^2-\lambda
$$
的完整 Bell 最大实现 $\mathsf P$ 若有核 $M$，
则整个 $M$ 属于
$$
W=\overline{Y-X^2-B}_{\rm can}\,L
$$
的实际域，且
$$
W|_M=-E|_M,
\tag{2.1}
$$
其中 $E\in A'$ 是实际有界平方根。其构造保留全部混合 Bell 项。
该结果只用深核、真实有界根和非临界支排除，
未假定自然 $W^2$ 闭。

2. [正第一阶的实际计数半群界与有限阶整预解](R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)：
正主行 $X_a$ 的实际半群满足
$$
\|e^{-tX_a}\|\le(9/10)^{\Theta_a(t)}.
$$
在 (1.2) 下，$X_a$ 及任意有界交换扰动的整预解均满足
$$
\|(X_a+H-z)^{-1}\|
\le C\exp[C(1+|z|)^{p/(p-1)}].
\tag{2.2}
$$
任何闭 $A$ 不变限制沿用原预解限制，故同界成立。
该引理逐位付真实 carry，不使用纯模型替换。

3. [相反二次符号的最大增生性与有限阶空谱预解不相容](R150-appendix-opposite-quadratic-accretivity-and-finite-order-resolvent-strip.md)：
非零 Hilbert 空间上，若 $Z$ 最大增生、空谱、整预解有限阶，
且有界 $J,K$ 与其所有预解交换，使对全部充分大实数 $c$，
$$
Z^2+(cI+J)Z+K,\qquad -Z^2+(cI-J)Z-K
\tag{2.3}
$$
在准确域 $\operatorname{Dom}Z^2$ 上均最大增生，
则矛盾。
该引理以实际二次因式支付两条固定宽半条带外的预解界，
再用明确 $\exp[-\varepsilon\cosh(\beta z)]$ 障碍函数与 Liouville；
不借一般空谱群生成元的错误断言。

以下补齐把本题的未知核放入 (2.3) 所需的全部实际域和正性。

## 3. 在未知核上识别完整二次域

设 $M=\ker\mathsf P$，暂假设 $M\ne0$。
由 R88，全部 $A'$ 保持 $M$。
所有 first 的自然限制、它们的共同正则器及正主行逆均使用 R128/R186。

在 R186 足够深的核内自然域上，(2.1) 给
$$
Yf=(X^2-EX+B)f.
\tag{3.1}
$$
例如先把 $Xf$ 也放入该深域，再用
$WXf=(Y-X^2-B)f$ 与 $W(Xf)=-E(Xf)$；
$X$ 在其实际域内保持 $M$。
不能把 (3.1) 对深域的成立直接称作整个域相等。

记 $X_M=X|_{\operatorname{Dom}X\cap M}$，$Y_M$ 类似。
$X_M$ 空谱，其逆是 $L|_M$。
R134/R176 给有界交换系数的首一二次式
$$
Q_M=X_M^2-E_MX_M+B_M
$$
在准确域 $\operatorname{Dom}X_M^2$ 上闭；
其图范数与 $X_M^2$ 的图范数等价。

取 R186 共同正则器 $R(s)$，选固定足够大整数 $N$。
它的深幂保持 $M$，强趋于 $I$，并与所有相关闭 first 域交换。

若 $f\in\operatorname{Dom}Y_M$，令 $f_s=R(s)^Nf$。
则
$$
f_s\to f,\qquad Yf_s=R(s)^NYf\to Yf.
$$
每个 $f_s$ 在 (3.1) 的真实域，故 $Q_Mf_s=Yf_s$。
$Q_M$ 闭，得到 $f\in\operatorname{Dom}X_M^2$、$Q_Mf=Yf$。

反向，若 $f\in\operatorname{Dom}X_M^2$，
同一正则器给 $f_s\to f$、$Q_Mf_s\to Q_Mf$。
由 (3.1) 及 $Y_M$ 闭，得到 $f\in\operatorname{Dom}Y_M$。
所以
$$
\boxed{
\operatorname{Dom}Y_M=\operatorname{Dom}X_M^2,\qquad
Y_M=X_M^2-E_MX_M+B_M.
}
\tag{3.2}
$$
这个结论使用特定共同正则核心，不使用普通系数截断在任意核向量上的图收敛。

## 4. 减去全部复倾斜与标量常数

令
$$
X_0=X_{\sum_j a_j\chi_j},\qquad
Y_0=X_{\sum_j c_j\chi_j}.
$$
$X_0$ 最大增生、空谱；$Y_0$ 为真实实 first。
真实倾斜满足
$$
X=X_0+H,\qquad Y=Y_0+G,\qquad H,G\in A',
\tag{4.1}
$$
其中 $H$ 含 $a_*I$ 及 $H_{a,b}$，
$G$ 含 $c_*I$ 及 $H_{c,b}$。
这些是已经证明按范数收敛的实际有界交换扰动。

有界交换扰动保持所有单 first 的自然幂域；
所以
$$
\operatorname{Dom}X_M^2=\operatorname{Dom}(X_0)_M^2,\qquad
\operatorname{Dom}Y_M=\operatorname{Dom}(Y_0)_M.
$$
展开 (3.2)，得
$$
\boxed{
(Y_0)_M=(X_0)_M^2+J_M(X_0)_M+K_M
}
\tag{4.2}
$$
在完整域 $\operatorname{Dom}(X_0)_M^2$ 上，其中全空间有界系数为
$$
J=2H-E,\qquad K=H^2-EH+B-G.
\tag{4.3}
$$
它们属于 $A'$、保持 $M$，与 $(X_0)_M$ 的全部预解交换。
这一步没有把任意复倾斜的 $X,Y$ 直接称为增生。

## 5. 两个正 first 的自然限制确实就是二次式

对任意实数 $c>C_0$，原系数行
$$
d_j^\pm=ca_j\pm c_j
$$
非负，且
$$
d_j^\pm\ge(c-C_0)a_j,\qquad \sum_jd_j^\pm=\infty.
$$
故真实闭 first
$$
Z_\pm(c)=X_{\sum_j d_j^\pm\chi_j}
$$
均最大增生、空谱，其自然限制 $(Z_\pm(c))_M$ 也最大增生，
预解就是全空间预解在 $M$ 上的限制（R128/R134）。

在共同深域上有真正第一阶线性恒等式
$$
Z_\pm(c)=cX_0\pm Y_0.
\tag{5.1}
$$
结合 (4.2)，它在那里等于
$$
Q_\pm(c)=\pm(X_0)_M^2+(cI_M\pm J_M)(X_0)_M\pm K_M.
\tag{5.2}
$$
(5.2) 最高系数为 $\pm I$，所以在准确域
$\operatorname{Dom}(X_0)_M^2$ 上闭。

现在识别完整域，不能从 (5.1) 默认无界自然和闭。
把两个 $Z_\pm(c)$ 及 $X_0,Y_0$ 都纳入有限 R186 共同正则器。
若 $f\in\operatorname{Dom}(Z_\pm(c))_M$，
正则化后 (5.2) 成立，且 $Z_\pm(c)f_s\to Z_\pm(c)f$；
$Q_\pm(c)$ 闭，迫 $f\in\operatorname{Dom}(X_0)_M^2$。
反向若 $f$ 属于该平方域，同一图逼近及 $Z_\pm(c)$ 的闭性给相反包含。
因此
$$
\boxed{
\operatorname{Dom}(Z_\pm(c))_M=\operatorname{Dom}(X_0)_M^2,\qquad
(Z_\pm(c))_M=Q_\pm(c).
}
\tag{5.3}
$$
对每个 $c>C_0$ 都成立。
故 (5.2) 的两个相反二次式确实最大增生。

## 6. 有限阶条带引理排核并返回指定向量

记 $Z=(X_0)_M$。
R128/R134 给 $Z$ 最大增生且空谱。
(1.2) 与 §2 的真实计数半群界给其整预解有限阶增长；
其预解范数不超过原 $H$ 上范数。
(4.3)、(5.3) 逐项满足 (2.3) 的全部准确假设。

“两个相反二次符号”引理因此排除非零 $M$。
故
$$
\ker\mathsf P=0.
$$
$\mathsf P$ 在原 $H$ 上完整 $C$ 自伴，
所以其像稠密。
R186 中 $\xi_w=e^w$ 的真实全部混合域和循环图核心给
$$
[F(u,v)e^w]_A=\overline{\operatorname{Ran}\mathsf P}=H,
$$
即 (1.3)。

没有把任何全空间稠密像免费传给未知限制；
实际限制上使用的都是正 first 的真实满射预解。
没有把通常伴随同域或 $C$ 下传到 $M$。
完整 Hilbert 普通 ISP 仍需其他开放接口；本稿确实关闭所列实碰撞类。
