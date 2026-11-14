# R150 附录：实际分数逆根、有理 Newton 边与全部非零最高簇

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 boundary_resume_1cf 已全文独立核查。本文把整数斜率的结论扩到全部有理斜率 $p/q>1$。分数逆根由实际半群及正预解积分构造，全部自然域另行支付；不使用形式 Puiseux 算子或未识别的分数幂定义域。

## 1. 原函数和有理权结论

保持原函数
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d^1_j+e^1_j)\chi_j,
\tag{1.1}
$$
其中
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,
$$
$d^\nu_j=0$ 于 $a_j=0$，$\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty$，
$e^\nu\in\ell^1(\mathbb C)$，所有常数及 $\psi$ 任意。

令 $p>q\ge1$ 为互素整数。取标量 $F(x,y)$，关于 $y$ 首一、次数为 $M\ge1$，满足
$$
\boxed{
qi+pj\le pM\qquad([x^iy^j]F\ne0).
}
\tag{1.2}
$$
最高符号为
$$
H(s)=\sum_{qi+pj=pM}[x^iy^j]F\,s^j.
$$
假设
$$
\boxed{H(0)\ne0.}
\tag{1.3}
$$
条件 (1.3) 本身要求 $pM/q$ 为整数，等价于 $q\mid M$；它说最高权中的纯 $x^{pM/q}$ 系数非零。最高根的任意重数和所有低权余项均允许。

**定理 1。** 对每个 $\lambda\in\mathbb C$、整数 $r\ge1$ 和任意复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.4}
$$
不对正主行追加增长或尾率条件。

在[全柱判据](R150-appendix-polynomial-column-tests-and-invertible-normalized-parts.md)的下降重排条件
$$
\liminf_{n\to\infty}
\frac{n\sum_{j>n}(a_j^*)^2}{(\sum_{j\le n}a_j^*)^2}=0
\tag{1.5}
$$
成立时，(1.1) 中的 $e^{i\psi}b_j$ 还可换成任意复 $c_j$，只要求
$|c_j|\le C_0a_j$。这一支不需要固定复直线。

例如
$$
F(x,y)=(y^q-x^p)^m+x^{pm-1},
\qquad p>q,\quad m>1,
\tag{1.6}
$$
有 $M=qm$，满足全部条件。非整数斜率下的重复最高边及这个低于最高权的扰动均包括在内。

## 2. 用实际半群构造一个真正的 $q$ 次逆根

取已付的实际最大增生空谱锚
$$
Z=X_{a+d^0}+\omega,\qquad L=Z^{-1}\in\mathfrak C=A'.
\tag{2.1}
$$
复加权主行稿的实际计数半群给
$$
S_Z(t)=e^{-tZ}
$$
为收缩半群，并比每个固定指数更快地在算子范数中衰减。它的所有有界成员属于 $\mathfrak C$。

$q=1$ 时直接取 $B=L$；它也增生，因为 $Z$ 增生而 $L=Z^{-1}$。以下设 $q>1$，记 $\alpha=1/q\in(0,1)$，定义
$$
\boxed{
B=\frac1{\Gamma(\alpha)}
\int_0^\infty t^{\alpha-1}S_Z(t)\,dt.
}
\tag{2.2}
$$
这里先对每个向量取 Hilbert 空间强积分。近0的 $t^{\alpha-1}$ 可积，远端由已付超指数范数界可积；积分定义一个有界算子，截断尾在算子范数中趋零。不要求半群轨道在 $B(H)$ 的算子范数中连续。

由正半轴的真实 Laplace 公式和绝对积分的向量 Fubini，
$$
\boxed{
B=\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty s^{-\alpha}(Z+sI)^{-1}\,ds.
}
\tag{2.3}
$$
右侧是范数收敛的预解积分：近0预解范数有界，远端不超过 $1/s$。其常数来自
$\Gamma(\alpha)\Gamma(1-\alpha)=\pi/\sin(\pi\alpha)$。

每个 $(Z+sI)^{-1}$ 都增生。确实，若 $y=(Z+sI)^{-1}x$，则
$$
\operatorname{Re}\langle (Z+sI)^{-1}x,x\rangle
=\operatorname{Re}\langle y,(Z+sI)y\rangle\ge0.
$$
(2.3) 因而证明 $B$ 有界增生，而且 $B\in\mathfrak C$。

### 2.1 准确的根恒等式

对 (2.2) 作 $q$ 重卷积，实际半群律使被积算子成为
$S_Z(t_1+\cdots+t_q)$。全部积分由同一范数可积界支配。置
$t=t_1+\cdots+t_q$，Dirichlet 的单纯形积分给
$$
B^q
=\frac1{\Gamma(q\alpha)}
\int_0^\infty t^{q\alpha-1}S_Z(t)\,dt
=\int_0^\infty S_Z(t)\,dt
=L.
\tag{2.4}
$$
因此
$$
\boxed{B^q=L.}
$$
这是真实有界算子等式，不是形式选根。

为多条有理边固定共同分母时，同一实际半群还给兼容的整个正指数族
$$
L^{[\theta]}=\Gamma(\theta)^{-1}
\int_0^\infty t^{\theta-1}S_Z(t)\,dt,\qquad \theta>0.
$$
这些积分均由近0可积及超指数尾定义。相同的向量 Fubini 和二重 Beta 积分准确给
$$
L^{[\theta]}L^{[\eta]}=L^{[\theta+\eta]}
\qquad(\theta,\eta>0).
$$
特别，若 $Q$ 是 $q$ 的正整数倍，则以同一半群构造的逆根满足
$B_Q^{\,Q/q}=B_q$。故更换为共同分母保留同一个实际有界算子，不能任选另一形式根。

由于 $L$ 单射且像稠密，(2.4) 给 $B$ 单射且像稠密。多项式谱映射及 $\sigma(L)=\{0\}$ 给 $\sigma(B)=\{0\}$。

定义
$$
X=B^{-1},\qquad\operatorname{Dom}X=\operatorname{Ran}B.
\tag{2.5}
$$
$X$ 闭、稠密定义。$B$ 增生使 $X$ 增生；而
$(I+X)^{-1}=B(I+B)^{-1}$ 在全空间有界，所以 $X$ 最大增生。更一般，
$$
(X-z)^{-1}=B(I-zB)^{-1}\in\mathfrak C
\quad(z\in\mathbb C),
\tag{2.6}
$$
故 $X$ 空谱。

反复使用真实逆定义，得到
$$
\operatorname{Dom}X^q=\operatorname{Ran}B^q
=\operatorname{Ran}L=\operatorname{Dom}Z,
$$
并准确有
$$
\boxed{X^q=Z.}
\tag{2.7}
$$
所有有界 $\mathfrak C$ 元素保持 $X$ 的各自然幂域；这是由其与 $B$ 及 (2.6) 交换直接得到的。

## 3. 好圆预算从 $Z$ 准确传给 $X$

[幂好时间/全柱二分稿](R150-appendix-power-good-times-column-dichotomy-and-good-circle-resolvents.md)
证明：任意正不可和 $\ell^2$ 主行，至少满足下面一支。

- 全柱支：(1.5) 成立。
- 好时间支：存在某个 $\epsilon>0,c>0$ 和 $\tau_n\to\infty$，使原正计数
  $\Theta_a(\tau_n)\ge c\tau_n^{1+\epsilon}$。

在后一支，已支付的实际复主误差、相位补偿和半群分块给一列
$R_n\to\infty$、有限 $\rho,C$，使
$$
\boxed{
\sup_{|z|\le R_n}\|(Z-z)^{-1}\|
\le C\exp(CR_n^\rho).
}
\tag{3.1}
$$
只在这些好圆上需要有限阶上界，不要求整预解全局具有有限阶。

由 $B^q=L$，
$$
\begin{aligned}
(X-z)^{-1}
&=B(I-zB)^{-1}\\
&=B\left(\sum_{\ell=0}^{q-1}z^\ell B^\ell\right)
(I-z^qL)^{-1}\\
&=B\left(\sum_{\ell=0}^{q-1}z^\ell B^\ell\right)
\bigl[I+z^q(Z-z^q)^{-1}\bigr].
\end{aligned}
\tag{3.2}
$$
每个等式都由有限有界因式给出。令 $r_n=R_n^{1/q}$，得到
$$
\boxed{
\sup_{|z|\le r_n}\|(X-z)^{-1}\|
\le C'\exp(C'r_n^{q\rho}).
}
\tag{3.3}
$$
只增加了有限多项式因子，吸收进常数即可。

(3.3) 对任何有限放大及对角 $\mathfrak C$ 不变的闭部分同样成立，因为全部实际预解都保持该部分。后面按有界拟幂零 $N$ 改变等价 Hilbert 范数时，至多再乘一个固定有限常数，仍为同一个好圆指数。

## 4. 两个不同整数幂的窄扇形引理

将[有限阶窄扇形引理](R150-appendix-finite-order-resolvent-narrow-sectors-and-all-nonzero-leading-clusters.md)
中的低阶 $cX$ 换成 $cX^q$，最高阶为 $p>q$。准确结论如下。

设 $X$ 最大增生、空谱，满足某个 (3.3) 型好圆界；设 $J$ 有界、与全部预解交换，且
$$
\sigma(J)=\{\kappa\},\qquad\kappa\ne0.
$$
若
$$
Q_\pm=cX^q\pm\beta JX^p,\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}X^p,
\quad c\ge0,\quad|\beta|=1,
\tag{4.1}
$$
都最大增生，则矛盾。

完整变化只有以下几处。按
$$
\|h\|_\eta^2=\sum_{n\ge0}\eta^{-2n}\|(J-\kappa I)^nh\|^2
$$
取等价 Hilbert 范数，使 $\|J-\kappa I\|\le\eta$。因 $J$ 与三组真实半群交换，$X,Q_\pm$ 仍最大增生；好圆界仅改固定常数。

收缩半群矩插值以最高阶 $p$ 使用，吸收低阶 $cX^q$ 后有
$$
\|X^pu\|\le C(\|Q_\pm u\|+\|u\|).
$$
记 $N=J-\kappa I$，置
$$
a_\pm(z)=cz^q\pm\beta\kappa z^p,
$$
$$
F_\pm(z)=Q_\pm-a_\pm(z)I\mp\beta Nz^p.
$$
准确自然因式为
$$
\boxed{
F_\pm(z)=(X-z)
\left[
c\sum_{\ell=0}^{q-1}z^\ell X^{q-1-\ell}
\pm\beta J\sum_{\ell=0}^{p-1}z^\ell X^{p-1-\ell}
\right].
}
\tag{4.2}
$$

远离 $\operatorname{Re}(\beta\kappa z^p)=0$ 的任意小固定角邻域，先取 $\eta$ 足够小，再取 $|z|$ 足够大。由于 $p>q$，
$c|z|^q$ 被 $\eta|z|^p$ 吸收。最大增生预解和有界扰动于是给
$$
\|F_\pm(z)^{-1}\|=O(|z|^{-p}),\qquad
\|X^pF_\pm(z)^{-1}\|=O(1).
$$
矩插值再给
$$
\|X^jF_\pm(z)^{-1}\|=O(|z|^{j-p})
\quad(0\le j\le p).
$$
(4.2) 方括号乘真实 $F_\pm^{-1}$ 映入 $\operatorname{Dom}X$，所以它就是 $(X-z)^{-1}$。最高组各项为 $O(1/|z|)$；低阶组为
$O(|z|^{q-1-p})$，更小。

剩余只有 $2p$ 个可任意窄的扇形。取扇形幂障碍
$\exp[-\delta(e^{-i\theta_0}z)^\nu]$，其中 $\nu$ 大于 (3.3) 的有限指数，扇形半宽小于 $\pi/(2\nu)$。外圆只沿 $r_n$ 取，(3.3) 足以使障碍压过增长；不需要两个好圆之间的上界。最大模原理后令 $\delta\downarrow0$，得到全平面有界预解。负实轴衰减与 Liouville 矛盾。引理得证。

## 5. 原有理权 Bell 的自然核与有限非零谱

固定 $\lambda,r,w$，令 $D=rM$。先保持原完整
$[F(x,y)-\lambda]^r$ 的全部混合 Bell 系数，再通过原真实有界代换
$$
x_{\rm old}=Z+H_0,\qquad
y_{\rm old}=Y+R_0Z+K_0,
\qquad Y=e^{i\psi}X_b,
$$
写成共同深域上的有限核心 $P(Z,Y)$。

在权 $\operatorname{wt}x=q,\operatorname{wt}y=p$ 下，正阶微分严格降权；有界 $x$ 平移降权，而 $y$ 中新增 $R_0x+K_0$ 也因 $p>q$ 降权。因此
$$
\boxed{
\widehat P(t,s)
=t^{pD}P(t^{-q},t^{-p}s)
=H(s)^rI+tE(t,s)\in\mathfrak C[t,s],
}
\tag{5.1}
$$
关于 $s$ 首一，次数 $D$，且 $\deg_sE<D$。

定义自然闭算子
$$
S=YB^p.
\tag{5.2}
$$
原规范 Bell 核若含非零 $f$，用全部原倾斜 first、$Z,Y$ 的同一个 R186 单射共同正则器深幂得到 $h\ne0$，并支付所有原有限词。所有 $B$ 幂有界且属于 $\mathfrak C$，故保这些域。于是
$$
h\in\operatorname{Dom}S^D,\qquad
\widehat P[B](S)h=B^{pD}P(Z,Y)h=0.
\tag{5.3}
$$
原项 $Z^iY^j$ 的系数是 $B^{pD-qi-pj}$，指数由 (1.2) 非负。原词深度可取 $N\ge pD+2$，并包含原有限族所需的更大固定深度。

同一自然相伴核图构造给非零闭 $\Gamma\subseteq H^D$ 和
$$
J=S^{(D)}|_\Gamma\in B(\Gamma).
$$
它保持全部对角 $\mathfrak C$，且
$$
H(J)^r=-B_\Gamma E[B_\Gamma](J)
$$
拟幂零。因此
$$
\sigma(J)\subseteq H^{-1}(0).
\tag{5.4}
$$
(1.3) 使 $J$ 为有界单位；在好时间支还可取一个非零 Riesz 子图 $\mathcal M$，使 $\sigma(J|_\mathcal M)=\{\kappa\}$。

这些闭图、自然幂域、Riesz 不变性与整数稿完全相同，只把有界拟幂零归一系数 $L$ 换为已经真实构造的 $B$。没有把原规范 Bell 域认作自然 $S^D$ 域。

## 6. 好时间支：准确支付 $cX^q\pm\beta JX^p$ 的域

在 §5 的 Riesz 子图 $\mathcal M$ 上，$X=B^{-1}$ 的部分仍最大增生、空谱，$X^q=Z_\mathcal M$，并有 (3.3)。

整个 $\mathcal M$ 都在自然 $S$ 域中。对每个
$x\in\operatorname{Dom}X^p$，
$$
X^px\in\mathcal M,\qquad
Yx=S X^px=JX^px.
\tag{6.1}
$$
所以 (6.1) 在全部自然域上准确成立。

原共享位移使两个实际 first
$$
cZ\pm e^{-i\psi}Y
$$
对充分大的固定 $c$ 最大增生。其部分在 $\mathcal M$ 上也最大增生。

令 $\beta=e^{-i\psi}$。对 $x\in\operatorname{Dom}X^p$，同一原 first 共同正则器在 $X^p$ 图中逼近 $x$：每个正则器在 $\mathfrak C$ 中，故与 $B$ 及 $X^p$ 的完整域交换；其足够深幂的像在
$\operatorname{Dom}Z^m=\operatorname{Dom}X^{qm}$，取 $qm\ge p$ 即够。它也在 $Y$ 图中逼近，因为 (6.1) 和闭域交换已付。

原两个完整 first 的闭性因此给
$$
Q_\pm=cX^q\pm\beta JX^p
\subseteq(cZ\pm\beta Y)_\mathcal M
$$
于准确自然域 $\operatorname{Dom}X^p$。

另一方面
$$
(Q_\pm-\lambda)B_\mathcal M^p
=\pm\beta J+cB_\mathcal M^{p-q}
-\lambda B_\mathcal M^p
\tag{6.2}
$$
是有界单位：$p-q\ge1$，右侧是单位 $\pm\beta J$ 乘
$I+$“拟幂零 $B_\mathcal M$ 乘有界交换子”。所以自然 $Q_\pm$ 闭、空谱。取负实参数，左侧满射、包含它的最大增生部分单射，迫完整域和作用相等。

§4 的引理遂排除 $\mathcal M$。这关闭好时间支，不需要原 $\Gamma$ 被 $C$ 保持。

## 7. 全柱支：两个整数幂的真实回传

现假设 (1.5) 成立，允许 $Y=X_c$ 的辅助行一般复受控。正主加权误差的实际有限位集、复中心 $\sigma_n$、头绝对值比与
$\sqrt{d_n}g_n/|\sigma_n|\to0$ 已由全柱稿 §6 支付。

仍反设 §5 给有界单位 $J=S|_\Gamma$。在
$\operatorname{Dom}X^{pq}=\operatorname{Dom}Z^p$ 上，逐次使用 (6.1) 和 $J$ 与 $X$ 的域交换，得到
$$
\boxed{Y^q=J^qZ^p.}
\tag{7.1}
$$
每个中间输入都在下一次 $X^p$ 域中；这是真实自然幂等式。

具体地，(7.1) 的归纳给 $Y^j x=J^jX^{pj}x$，$0\le j\le q$；$J$ 与 $X$ 的各自然域交换，故每个输出保有所需剩余域。

取同一原 first 深正则向量 $h_t\to h\in\Gamma$，使 $h_t$ 与 $J^qh_t$ 都在所需原 $Z,Y$ 词域。对原伴随共同深域中的 $f$，准确有
$$
\langle h_t,(Y^*)^qf\rangle
=\langle Y^qh_t,f\rangle
=\langle J^qZ^ph_t,f\rangle
=\langle J^qh_t,(Z^*)^pf\rangle.
$$
$J^q$ 有界，取极限得到
$$
\boxed{
\Pi(Y^*)^q=(J^*)^q\Pi(Z^*)^p
}
\tag{7.2}
$$
于原共同伴随深域，其中 $\Pi$ 是到 $\Gamma$ 的正交投影。

现在使用测试多项式
$$
\mathscr P_n(z)
=I-\left(\frac{Z^*}{\overline{\sigma_n}}\right)^p
+z\,\frac{(Y^*)^q}{\overline{\sigma_n}^{\,p}}.
\tag{7.3}
$$
以全柱稿的两个头和两个尾 $A,B_0,T,U$ 记号展开，
$$
\mathscr P_n(z)
=I-(I+A+T)^p
+z\,\overline{\sigma_n}^{\,q-p}
\left(\frac{\overline{t_n}}{\overline{\sigma_n}}I+B_0+U\right)^q.
\tag{7.4}
$$
常数项为
$z\overline{t_n}^{\,q}/\overline{\sigma_n}^{\,p}
=O_R(|\sigma_n|^{q-p})\to0$；其余单项式次数介于1与 $p$，系数一致有界。

因此全柱稿 §3 的三组证明逐项适用：取迭代次数
$\ell_n/d_n\to\infty$、
$g_n\sqrt{\ell_n}/|\sigma_n|\to0$，按常数因子数、头总次数、尾总次数至少有一个达到 $\ell_n/3$ 分组，得到
$$
\boxed{
\sup_{|z|\le R}
\|\mathscr P_n(z)^{\ell_n}Q_{F_n}\|^{1/\ell_n}\to0
}
\tag{7.5}
$$
对每个固定 $R<\infty$ 成立。所有总词次数至多 $p\ell_n$，由 R251 同一补集尺度完整支付。

(7.2) 使投影回传中的有界逆换为 $(J^*)^{-q}$。有限 Cauchy 系数公式只需选
$R>\|J^{-q}\|$，便得到
$$
\|\Pi Q_{F_n}\|
\le\frac{1}{1-\|J^{-q}\|/R}
\sup_{|z|=R}\|\mathscr P_n(z)^{\ell_n}Q_{F_n}\|
\to0.
$$
$Q_{F_n}\to I$ 强，故 $\Pi=0$，矛盾。全柱支也已关闭。

## 8. 两支合并与原点态结论

幂好时间/全柱二分适用于每个原正 $a\in\ell^2\setminus\ell^1$。固定复直线辅助在好时间支使用 §6，在全柱支使用 §7；一般复受控辅助只在已付的全柱条件下使用 §7。

两支都排除原规范 Bell 的非零核。原完整 $C$ 自伴性给像稠密，而 R186 的循环指数图核心给
$$
[\mathcal Pe^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
其作用正是 (1.4) 的原普通点态向量，定理1得证。

例如对全部 $1/2<\sigma\le1$，
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=i\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
$$
有
$$
\boxed{
[(v^2-u^3)^m+u^{3m-1}-\lambda]^r e^w
\text{ 对全部 }m>1,\lambda,r,w\text{ 循环。}
}
$$
一般 (1.6) 的归一式是 $(s^q-1)^m+t^q$；当 $m>q$ 时，在每个 $\kappa^q=1$ 处并无所需 $t^m$ 消失阶。上例 $q=2$ 因而在 $m>2$ 时还提供明确的超消失阶新范围。

先前简单 Newton 根的交集范围按旧来源扣除；本文新增包括非整数斜率的任意重簇及这些不满足平衡消失阶的余项。

本稿只处理一个最高有理斜率上全部根非零的情形。含多个不同 Newton 边且留下真正零最高簇、斜率降到1或以下，以及一般非仿射线复骨架的非全柱支仍保留。原正常见证专属源预算和普通复 Hilbert ISP 没有因此完成。
