# R438：原 Bezout 小核的惰性三权与对角全部 carry 交叉行

日期：2026-11-14。**状态：已证明。** 本篇直接使用 R424/R430 的全局 theta 恒等式，把同一原 $S_{34}$ 的完整惰性三权聚合送入任意第二轴 Taylor 测试；不用普通测度的反卷积。对角上的三个权逐一保留全部交叉项，并把原 $T_{72}$ 接回同一固定多项式。两原中央同时失败由此给出一个带实际除 $p$ 行的准确可逆消元式，未把交叉项分别置零，也未把有限核的非退化当作新增中央条件。

## 1. 固定 E1 规范与四条实际来源

使用 R403 已付的共同 $E_1:y^2=x^3+1$ 规范，保留
$$
p=6s-1>83,\quad a=p\kappa\in\mathcal O^\times,
\quad\alpha=36/17,\quad\beta=9/17,\quad w=z^6,
$$
$$
t=-1/x^3,\quad X=z^2x,\quad\Theta=x\sigma^2,
\quad g=(1+8t)\Theta^{17}e^{-\kappa w^s}.
$$
固定曲线及周期到这个模型的单位运输仍按 R403 保留。定义首项一的 regularized theta
$$
\vartheta=\Theta e^{-\kappa w^s/17}
=\left(g/(1+8t)\right)^{1/17}.
\tag{1}
$$
本文只读至 $w^{3s}$；$3s<p$，所以 (1) 的首项一根在原三权整性窗口内整，不引入新的 Gaussian 选择。

写
$$
h_7=7+4t+16t^2,\quad d=1+8t,
\quad P=1+30t-144t^2+32t^3.
$$
R424 的四个真正原因子在当前规范中是
$$
\begin{aligned}
G_{16}&=\sigma^{16}x(x^3+1)(x^3-8),\\
F_{18}&=\sigma^{18}x(x^6-4x^3/7+16/7),\\
G_{18}&=\sigma^{18}(x^9-30x^6-144x^3-32),\\
C_{34}&=G_{16}G_{18},\qquad S=G_{16}F_{18}.
\end{aligned}
\tag{2}
$$
以下普通 $w$ 级数均为准确 regularized 部分：
$$
\begin{aligned}
A(w)&=\vartheta^8X^{-1}(1-t)d,\\
F(w)&=\vartheta^9X^{-2}h_7/7,\qquad
G(w)=\vartheta^9P,\\
C(w)&=A(w)G(w),\qquad
S_0(w)=wA(w)F(w)=\vartheta^{17}\frac{t(t-1)dh_7}{7}.
\end{aligned}
\tag{3}
$$
也就是说
$$
\begin{aligned}
S(z)&=e^{\kappa w^s}S_0(w),&
C_{34}(z)&=e^{\kappa w^s}z^2C(w),\\
G_{18}(z)&=e^{\beta\kappa w^s}G(w),&
F_{18}(z)&=e^{\beta\kappa w^s}z^4F(w).
\end{aligned}
\tag{4}
$$
因此第一轴两来源的 Gaussian 都是 $a$，第二轴两来源的 Gaussian 都是 $\beta a$。$C(0)=F(0)=G(0)=1$，$S_0=w+\cdots$。例如
$$
[w]G=-156/5,\quad [w]F=-52/35,\quad
[w]C=-4108/105,\quad [w^2]S_0=-988/105.
\tag{5}
$$
这些归一固定了原幂、常数和 CM 权，不能把 $C_{34}$ 或 $F_{18}$ 改当 principal 来源。

## 2. 完整第一轴三权向整个第二轴返回

R430 的全局来源身份为
$$
\mathcal K(y,x)=-\frac23\{S(y)G_{18}(x)-C_{34}(y)F_{18}(x)\}.
$$
分别去掉 (4) 的两个 Gaussian 后，准确得到
$$
\boxed{\widehat{\mathcal K}(y,x)
=-\frac23\{S_0(y^6)G(x^6)-y^2x^4C(y^6)F(x^6)\}.}
\tag{6}
$$
第一项的两个 CM 权是 $(0,0)$，第二项是 $(2,4)$。令
$$
S_0=\sum s_nw^n,\quad G=\sum g_nw^n,\quad
C=\sum c_nw^n,\quad F=\sum f_nw^n.
$$
整个双变量系数只有
$$
\boxed{\begin{aligned}
[y^{6i}x^{6j}]\widehat{\mathcal K}&=-2s_ig_j/3,\\
[y^{6i+2}x^{6j+4}]\widehat{\mathcal K}&=2c_if_j/3
\end{aligned}}
\tag{7}
$$
两种形状，其余余类为零。

对第一轴使用原 $S$ 的同一个完整三权算子
$$
\mathfrak C_a^Y
=a^2[y^{p+1}]-pa[y^{2(p+1)}]+2p^2[y^{3(p+1)}],
\qquad
\mathfrak c_S=a^2s_s-pa s_{2s}+2p^2s_{3s}.
\tag{8}
$$
因为 $p+1=6s$，第二项在三个权上逐项为零。因此
$$
\boxed{\mathfrak C_a^Y\widehat{\mathcal K}
=-\frac23\mathfrak c_S\,G(x^6).}
\tag{9}
$$
特别，对任意实际有限 Taylor 线性测试 $\lambda_X$，有
$$
(\mathfrak C_a^Y\otimes\lambda_X)(\widehat{\mathcal K})
=-2\mathfrak c_S\lambda_X(G(x^6))/3.
\tag{10}
$$
在原整性窗口内这是一条整映射身份，模 $p^3$ 后同样成立。它只用 (6) 的全局来源及 CM 权，未把普通有界测度、第二轴反卷积或深度域运输移到惰性位。

原完整惰性中央失败给出 R403 的 $\mathfrak c_S\equiv0\pmod{p^3}$，故确实控制 (10) 中全部第二轴测试。反过来取第二轴常数项，因 $G(0)=1$，这些三权行同时为零准确等价于 $\mathfrak c_S\equiv0$。所以这里没有新增独立的第一轴中央条件；类型 $(2,4)$ 也没有被迫消失。

## 3. 对角的三个权保留全部交叉项

沿同一真实对角 $y=x=z$，总 Gaussian 是
$$
a_{52}=(1+\beta)a=(26/17)a.
\tag{11}
$$
不能用 $a$ 代替它。(6) 的完整对角零等价于
$$
\boxed{S_0(w)G(w)=wC(w)F(w).}
\tag{12}
$$
对 $k=1,2,3$，定义全部非端点交叉和
$$
B_k(S_0,G)=
\sum_{h=0}^{k-1}\sum_{i=1}^{s-1}
s_{hs+i}\,g_{(k-h)s-i},
\tag{13}
$$
以及完整的类型 $(2,4)$ 配对
$$
R_k(C,F)=
\sum_{h=0}^{k-1}\sum_{i=0}^{s-1}
c_{hs+i}\,f_{(k-h-1)s+s-1-i}.
\tag{14}
$$
令 $Z_k=R_k-B_k$。$s_0=0$、$g_0=1$ 给出准确三角式
$$
\boxed{\begin{aligned}
s_s&=Z_1,\\
s_{2s}+g_ss_s&=Z_2,\\
s_{3s}+g_ss_{2s}+g_{2s}s_s&=Z_3.
\end{aligned}}
\tag{15}
$$
因此原 $S$ 的完整三权恰为
$$
\boxed{\mathfrak c_S=
\bigl(a^2+pa g_s+2p^2(g_s^2-g_{2s})\bigr)Z_1
 +(-pa-2p^2g_s)Z_2+2p^2Z_3.}
\tag{16}
$$

**证明。** 在 $[w^{ks}](S_0G)$ 中，来源下标被 $s$ 整除的端点分别给
$s_{ks}+\sum_{h=1}^{k-1}s_{hs}g_{(k-h)s}$，其余全部唯一落入 (13)。在 $[w^{ks-1}](CF)$ 中，每个下标唯一写为 $hs+i$、$0\le i<s$，得到 (14)。逐个 $k$ 比较即为 (15)；三角消元后代入 (8) 得 (16)。$\square$

(13) 包含每一条跨 $s$ 边界的卷积尾，(14) 包含余类二与四相加时的整个偏移一。若用总 degree52 的三权算子作用于 (12)，只能得到同一恒等式的相应加权和；它不把 (13)、(14) 的各项分别置零。特别 (9) 不能直接给对角上任意依赖 $y$、$x$ 的新测试赋零。

## 4. 原 T72 与小核之间的准确固定多项式

置
$$
V_1=1-4t,\quad V_2=1-20t-8t^2,\quad
V_3=1+96t+48t^2-64t^3.
$$
原 $L_{38}=T/S$、$E_{20}=J_{12}\Theta(2\cdot)$ 的 regularized 部分分别为
$$
L(w)=\vartheta^{19}V_1V_2V_3,\qquad
E(w)=\vartheta^{10}dV_2.
\tag{17}
$$
第二轴的 $B_{38},D_{38}$ 因而为 $B=EG$、$z^4D=z^4EF$。一个完整四次多项式恒等式是
$$
\boxed{V_1V_3-dP=54t(1-4t)^2.}
\tag{18}
$$
令 $N(w)=\vartheta^{19}tV_2(1-4t)^2$，则
$$
\boxed{L=B+54N,\qquad
T_0=S_0L=wC D+54S_0N.}
\tag{19}
$$
$N=-w+\cdots$，$[w]B=-308/15$，$[w]L=-1118/15$。所有项的总 Gaussian 都是 $\alpha a$，即同一个原 degree72；没有以 degree52 的中央归一替代原 $T$。

**证明。** (17) 直接由 R403/R424 的原多项式取出 $\Theta$ 幂得到。展开左端 (18) 为 $54t-432t^2+864t^3$。乘 $\vartheta^{19}V_2$，再用 (12)，即得 (19)。$\square$

## 5. 两原完整中央同时失败时的实际可逆交叉消元

写 $L=\sum l_nw^n$，$l_0=1$，并令
$$
U_k=B_k(S_0,L)=
\sum_{h=0}^{k-1}\sum_{i=1}^{s-1}s_{hs+i}l_{(k-h)s-i},
\qquad k=1,2,3.
\tag{20}
$$
原 $T_0=S_0L$ 的三个端点准确为
$$
d_1=s_s+U_1,\quad
d_2=s_{2s}+s_sl_s+U_2,\quad
d_3=s_{3s}+s_{2s}l_s+s_sl_{2s}+U_3.
\tag{21}
$$
保持两个原基准
$$
\mathfrak c_S=a^2s_s-pa s_{2s}+2p^2s_{3s},\qquad
\mathfrak c_T=\alpha^2a^2d_1-p\alpha a d_2+2p^2d_3.
\tag{22}
$$
若它们同时为零模 $p^3$，先有 $U_1\in p\mathcal O$，并有完整必要且充分的三权精度消元式
$$
\boxed{\begin{aligned}
0\equiv{}&\alpha^2a^2\frac{U_1}{p}-\alpha aU_2+2pU_3\\
&+\bigl(a\alpha(\alpha-1)+p(2-\alpha)l_s\bigr)s_{2s}
 +2p(1-\alpha^2)s_{3s}\pmod{p^2},\\
s_s\equiv{}&\frac pa s_{2s}-\frac{2p^2}{a^2}s_{3s}\pmod{p^3}.
\end{aligned}}
\tag{23}
$$
其中第一式乘 $p$，连同 $U_1\in p\mathcal O$ 和第二式，反向准确恢复 (22) 的两个模 $p^3$ 零。

**证明。** 将 (21) 代入 $\mathfrak c_T-\alpha^2\mathfrak c_S$。所得完整式是
$$
\begin{aligned}
&\alpha^2a^2U_1-p\alpha aU_2+2p^2U_3
 +pa\alpha(\alpha-1)s_{2s}+2p^2(1-\alpha^2)s_{3s}\\
&\hspace{15mm}-p\alpha a s_sl_s
 +2p^2(s_{2s}l_s+s_sl_{2s}).
\end{aligned}
$$
以 $\mathfrak c_S\equiv0$ 代入 $s_s$，模 $p^3$ 后末行变成
$p^2(2-\alpha)l_s s_{2s}$；$s_sl_{2s}$ 因 $s_s\in p\mathcal O$ 自动属于三阶尾，而非事先丢弃。模 $p$ 先得 $U_1\equiv0$，再合法除以 $p$ 得 (23)。逆向把这些步骤还原即可。$\square$

系数
$$
\boxed{a\alpha(\alpha-1)+p(2-\alpha)l_s
=\frac{684}{289}a-\frac{2p}{17}l_s}
\tag{24}
$$
是实际整单位。因此一旦保留同一真实 $U_1/p,U_2,U_3,l_s,s_{3s}$，(23) 唯一决定 $s_{2s}\bmod p^2$，再决定 $s_s\bmod p^3$。$U_1/p$ 是固定交叉和的真实下一位，不是可选提升；$s_{3s}$ 及第三完整中央基准也未消失。

(19) 允许在 (20) 中把每个实际 $U_k$ 准确拆为 $B_k(S_0,B)+54B_k(S_0,N)$。两个部分仍是同一来源给出的耦合交叉和；(9)、(12) 都没有分别杀掉它们。

## 6. 对同一个有限矩阵的适用边界

本文只运输原函数和其有限三权行，没有替换 R403/R425/R434 的原 $M^3$。若把 (16) 或 (23) 放入该矩阵，仍须保留整个 $P_{134}$、$U_0$、总 charge 四十、两条十三行 carry 带，以及真正 $K_1(M)$、$C_2(M)$、原提升后的左核。第二轴测试是实际 Taylor 线性行；它不把新的乘积中央、独立隐藏深度条件或自由接触尾加入原来源。

脚本 `scripts/check-r438-inert-kernel-diagonal.py` 在原 $p=101$ 上核对整个来源多项式、三个完整对角行和两个原中央的精确差式，并在 R425 的指定完整 Hensel 条件模型中核对 (23) 的合法除法及单位消元。条件模型不被认作新算术来源，有限核验不被用作跨素数结论。
