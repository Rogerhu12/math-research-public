# R271 附录：一位正 commutator 因子与完整最小源的整段占据行

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 一位硬核完整 Schur 可改写为正的 $I+u\mathcal K$ inverse，不引入未付的小奇值 inverse。其实际新位源有准确两项正能量分解。对同一个辅助方差作一次选择后，区间 $[x,2x)$ 内全部实际新源的占据范数平方和、以及同一正 Schur 余项的和，均由原同源缺陷控制。所有原 $u_{m,Q,f}$ 保持，但本稿的占据行作用于合法代表 $F_{y+1,t}$，不把它误认作固定 $u_{m,Q,f}$ 的向量行。

依据：

- [一位硬核完整 Schur、真实投影损失及两阶矩](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)；
- [原强前缀完整 Gram 与远尾方差极限](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)；
- [原物理同源列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)。

## 1. Fock 自然域上的正 commutator

令 $C^h=0$ 为有界头算子，$s'>0$，定义
$$
H=H_C(s')=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{s'^j j!},
\qquad
T=\frac1{\sqrt{s'}}H^{1/2}CH^{-1/2}.
\tag{1.1}
$$
一-mode Fock 中，$R_C(s')$ 的第 $j$ 行为
$(-C)^j/(s'^{j/2}\sqrt{j!})$。于是
$$
\mathcal I=R_C(s')H^{-1/2}
$$
是真等距，像恰为 $\mathscr M=\ker(C+\sqrt{s'}\,a)$，其中 $a$ 是标准 annihilator。该像只含 Fock 次数 $0,\ldots,h-1$。所以 $a\mathcal I$、$a^*\mathcal I$ 都有界，分别只达到次数 $h-2$、$h$；以下所有压缩及乘积在自然闭域上有完整意义。

记 $P=P_{\mathscr M}$。因为 $a\mathscr M\subset\mathscr M$，
$$
\mathcal I^*a\mathcal I=-T.
$$
在这些有限次数列上用 $aa^*-a^*a=I$，得
$$
\boxed{
\mathcal K:=I+T^*T-TT^*
=\mathcal I^*a(I-P)a^*\mathcal I
=\big((I-P)a^*\mathcal I\big)^*
  \big((I-P)a^*\mathcal I\big)\succeq0 .
}
\tag{1.2}
$$
这是真核外创建列的平方，不是只因 $H\succeq I$ 猜测一个 commutator 符号。

逐行能量移位还给
$$
\|T H^{1/2}z\|^2
=\sum_{j=1}^{h-1}\frac{j\|C^jz\|^2}{s'^j j!}
\le(h-1)\langle Hz,z\rangle,
$$
故
$$
0\preceq\mathcal K\preceq I+T^*T\preceq hI.
\tag{1.3}
$$

## 2. 完整新源的正因子化

加入权 $b>0$ 的一个真实硬核位，令
$$
u=\frac{b^2}{s'},\qquad C'=C+bE,\qquad S=s'+b^2.
$$
以前稿的完整 Gram 对两个源头同时作 $H^{-1/2}$ 同余，得到
$$
\mathcal H=
\begin{pmatrix}
I&\sqrt u\,T^*\\
\sqrt u\,T&(1+u)I+uT^*T
\end{pmatrix}.
$$
由 (1.2)，右下块准确为 $I+u\mathcal K+uTT^*$，从而
$$
\mathcal H=
\begin{pmatrix}I&0\\\sqrt u\,T&I\end{pmatrix}
\begin{pmatrix}I&0\\0&I+u\mathcal K\end{pmatrix}
\begin{pmatrix}I&\sqrt u\,T^*\\0&I\end{pmatrix}.
\tag{2.1}
$$
特别 $I+u\mathcal K\succeq I$，其 inverse 范数至多 $1$。这里没有先压掉任何新位源。

置 $\mathcal R=(I+u\mathcal K)^{-1}$。完整逆的各块为
$$
\boxed{
\mathcal H^{-1}=
\begin{pmatrix}
I+uT^*\mathcal RT&-\sqrt u\,T^*\mathcal R\\
-\sqrt u\,\mathcal RT&\mathcal R
\end{pmatrix}.
}
\tag{2.2}
$$
因此前稿的真空源 Schur 满足
$$
\boxed{
H_{\rm eff}^{-1}
=H^{-1/2}[I+uT^*(I+u\mathcal K)^{-1}T]H^{-1/2}.
}
\tag{2.3}
$$

对 forcing $(g,0)$，令 $\xi=H^{-1/2}g$。真正最小的新源 $(a_0,a_1)$ 白化后准确为
$$
\widehat a_0=H^{1/2}a_0
=\xi+uT^*\mathcal RT\xi,\qquad
\widehat a_1=H^{1/2}a_1=-\sqrt u\,\mathcal RT\xi.
\tag{2.4}
$$
它一般不等于前稿用于上界的候选
$(a,-bCa/S)$。

记新投影平方为 $q_{\rm new}$，而 $q(s')=\langle g,H_C(s')^{-1}g\rangle$。其增益有完整正分解
$$
\boxed{
\begin{aligned}
G&:=q_{\rm new}-q(s')
=u\langle T\xi,\mathcal RT\xi\rangle\\
&=\|\widehat a_1\|^2+
u\|\mathcal K^{1/2}\widehat a_1\|^2.
\end{aligned}}
\tag{2.5}
$$
新核列在 bit-$1$ 行恰为 $R_C(s')a_1$，所以第一项等于新实际投影在这一位上的占据范数平方。第二项保留真实核外创建列，不能当作零。

若 $\mathfrak F_1(s')=\sum_jj\|C^jH_C(s')^{-1}g\|^2/(s'^jj!)$，则移位给
$\mathfrak F_1(s')=\|T\xi\|^2$，故
$$
\frac{u}{1+uh}\mathfrak F_1(s')
\le G\le u\mathfrak F_1(s').
\tag{2.6}
$$
这始终是当前完整 $H_C(s')$ 的同源能量，未将它换成另一高度的 source。

## 3. 原连续尾的同一参数整段增益

保前稿记号
$$
x\ge\max(10,m+2^m),\quad
C_y=A_m+D_{[m,y)},\quad h_y=2^m+y-m,
\quad y=x,\ldots,2x,
$$
$$
S_y=\sum_{i\ge y}(i+1)^{-4},\qquad z_y=(y+1)^{-4}.
$$
固定同一个有限物理 forcing $f$，把中间位置补真空得到 $g_y$。固定辅助方差 $t\ge0$，令
$$
q_y(t)=\langle g_y,H_{C_y}(S_y+t)^{-1}g_y\rangle.
\tag{3.1}
$$
如前稿，在同一 Fock 空间中保所有真实尾 mode 和一个系数 $\sqrt t$ 的额外 mode。只逐次增加真实位的硬核约束，闭核 $\mathscr K_y(t)$ 递减。其实际投影
$v_y(t)=P_{\mathscr K_y(t)}f$ 满足 $\|v_y(t)\|^2=q_y(t)$。

在第 $y$ 步，新剩余方差为
$$
s'_y=t+S_{y+1},\qquad u_y=z_y/s'_y.
$$
用 §1–2 中 $C=C_y$、$s'=s'_y$ 定义
$H_y,T_y,\mathcal K_y,\widehat a_{1,y}(t)$。准确增益为
$$
G_y(t)
=q_{y+1}(t)-q_y(t-z_y)
=\|\widehat a_{1,y}(t)\|^2+
u_y\|\mathcal K_y^{1/2}\widehat a_{1,y}(t)\|^2 .
\tag{3.2}
$$
这里 $q_y(t-z_y)$ 的总方差就是 $S_y+t-z_y=s'_y$。

取 $t\in[S_x,2S_x]$。由于 $z_x<S_x$，以上全部参数严格为正。嵌套投影给 $q_{y+1}(t)\le q_y(t)$，所以
$$
0\le G_y(t)\le q_y(t)-q_y(t-z_y).
\tag{3.3}
$$
置一个稍宽的同源端点差
$$
\boxed{
\mathcal V_x^\sharp
=q_x(2S_x)-q_{2x}(S_x-z_x)\ge0.
}
\tag{3.4}
$$

每个 $q_y$ 连续可导且不减。用非负导数和 Fubini，
$$
\begin{aligned}
\int_{S_x}^{2S_x}[q_y(t)-q_y(t-z_y)]\,dt
&\le z_y[q_y(2S_x)-q_y(S_x-z_y)]\\
&\le z_y\,\mathcal V_x^\sharp.
\end{aligned}
$$
最后一步同时使用 $y\le2x$ 的核嵌套和 $z_y\le z_x$ 的参数次序。因
$\sum_{y=x}^{2x-1}z_y=S_x-S_{2x}$，得到整段估计
$$
\boxed{
\frac1{S_x}\int_{S_x}^{2S_x}
\sum_{y=x}^{2x-1}G_y(t)\,dt
\le\left(1-\frac{S_{2x}}{S_x}\right)\mathcal V_x^\sharp.
}
\tag{3.5}
$$
所有 integrand 都是非负连续函数；存在一个共同 $t_*\in[S_x,2S_x]$ 使
$$
\boxed{
\sum_{y=x}^{2x-1}
\left[
\|\widehat a_{1,y}(t_*)\|^2+
u_y\|\mathcal K_y^{1/2}\widehat a_{1,y}(t_*)\|^2
\right]
\le\mathcal V_x^\sharp.
}
\tag{3.6}
$$
它控制全部 $x$ 个新位的完整最小源，不为每个位另选参数。

另一方面，对任何该区间内的 $t$，真实投影步差正交并准确望远镜：
$$
\sum_{y=x}^{2x-1}\|v_y(t)-v_{y+1}(t)\|^2
=q_x(t)-q_{2x}(t)\le\mathcal V_x^\sharp.
\tag{3.7}
$$

## 4. 固定物理压缩与全部同一原 $u_f$

在上面的共同 Fock 空间中，令 $\mathcal P_{\rm phys}$ 为：所有真实尾位只保 $0/1$ 占据，并将额外 mode 投到真空。它是固定正交投影，不依赖 $y$。当 $t$ 固定时，
$$
F_{y,t}:=\mathcal P_{\rm phys}v_y(t)
=\sum_{j=0}^{h_y-1}
\frac{(-C_y)^ja_y(t)\otimes(D_y^*)^j\Omega}
     {(S_y+t)^j j!},
\tag{4.1}
$$
正是原已付的物理同源列。等式逐总 Fock 次数成立；额外 mode 的非真空项全部被准确压掉，没有把其方差加到原物理算子中。

$v_{y+1}(t)$ 在第 $y$ 位已经硬核。因此该位的 bosonic annihilation 与物理 Boolean 删除相同，且与其它位及额外 mode 的物理压缩相容。由 (2.5)，
$$
\|E_yF_{y+1,t}\|^2
\le\|a_yv_{y+1}(t)\|^2
=\|\widehat a_{1,y}(t)\|^2,
\tag{4.2}
$$
这里 $a_y$ 是第 $y$ 个 bosonic annihilator，和源向量 $a_y(t)$ 用上下文严格区分。固定压缩又给
$$
\|F_{y,t}-F_{y+1,t}\|
\le\|v_y(t)-v_{y+1}(t)\|.
$$
因此同一个 $t_*$ 满足
$$
\boxed{
\sum_{y=x}^{2x-1}
\left[
\|E_yF_{y+1,t_*}\|^2+
u_y\|\mathcal K_y^{1/2}\widehat a_{1,y}(t_*)\|^2
\right]\le\mathcal V_x^\sharp,
}
\tag{4.3}
$$
$$
\boxed{
\sum_{y=x}^{2x-1}
\|F_{y,t_*}-F_{y+1,t_*}\|^2\le\mathcal V_x^\sharp.
}
\tag{4.4}
$$
源的重新最小化没有被删掉；它正是 (3.7)、(4.4) 中的步差。

若
$$
Q\ge2^m+4x-2m,
\tag{4.5}
$$
则所有 $y\in[x,2x]$、包括 (3.4) 两端的完整物理列，均满足原
$Q\ge(y-m)+(h_y-1)$ 的支持门。已付逐列身份遂给
$$
(P_{V_{m,Q}}-P_{K_{m,Q}})F_{y,t}
=u_{m,Q,f}:=(P_{V_{m,Q}}-P_{K_{m,Q}})f.
\tag{4.6}
$$
同样，$q_{2x}(S_x-z_x)\ge\|u_{m,Q,f}\|^2$，而
$q_x(2S_x)\le\|f\|^2$。所以
$$
\boxed{\mathcal V_x^\sharp\le
\Delta_{m,Q,f}^2:=\|f-u_{m,Q,f}\|^2.}
\tag{4.7}
$$
选择 $t_*$ 先于全部合法 $Q$，故 (4.3)–(4.4) 对同一个参数及所有这些 $Q$ 同时受 $\Delta_Q^2$ 控制。

这些标量二次型结论对任意原头 forcing $g$ 成立。因此在保原真空嵌入后，(3.5)、(4.3) 的积分版本也是完整 forcing 空间上的正算子不等式，可以作同一个 forcing 合同；不需先取某个环境 inverse 范数。

## 5. 与两阶高度矩同时保持

若还需要前稿的一阶、二阶高度矩，可在同一次选择中保留它们，而不是事后重选。令
$$
\mathfrak F_1(y,t)=\sum_j jE_j(y,t),\qquad
\mathfrak F_2(y,t)=\sum_jj(j-1)E_j(y,t).
$$
前稿的逐位碰撞界对每个 $t$ 给
$$
\frac1x\sum_{y=x}^{2x-1}\frac{\mathfrak F_2(y,t)}x
\le512e^4\mathcal V_x^\sharp.
$$
对一阶矩，先按 $\log t$ 积分，再用 $t\le2S_x$，得
$$
\frac1{S_x}\int_{S_x}^{2S_x}
\frac1x\sum_{y=x}^{2x-1}\mathfrak F_1(y,t)\,dt
\le4\mathcal V_x^\sharp.
$$
与 (3.5) 相加后一次取最小点，得到共同 $t_\#$ 使
$$
\boxed{
\sum_yG_y(t_\#)+
\frac1x\sum_y
\left[\mathfrak F_1(y,t_\#)+\frac{\mathfrak F_2(y,t_\#)}x\right]
\le30000\,\mathcal V_x^\sharp.
}
\tag{5.1}
$$
随后可在有限 $y$ 集合中选一个 $y_\#$，保该来源的两阶矩
$\mathfrak F_1+\mathfrak F_2/x\le30000\mathcal V_x^\sharp$，同时仍保整个新位行的同一 $t_\#$ 预算。此加强用常数 $30000$；若只需整段行，(3.6) 的常数为 $1$。

对 $x=m+2^m$、$m\to\infty$，原强前缀定理给
$\mathcal V_x^\sharp\to0$，因为两端总方差均不小于相应的真实 $S_y$，且均趋零。充分大的 $m$ 下，$Q\ge6\cdot2^m$ 可满足 (4.5)，且仍在原 $e^{26d^3}$ 母窗口内。

## 6. 仍须保留的返回

新整段 norm-row 是 $\{E_yF_{y+1,t_*}\}_y$，并非
$\{E_yu_{m,Q,f}\}_y$。一般 $E_y$ 不与原 $V_Q/K_Q$ 的正交投影交换，(4.6) 不能把它移过投影。步差平方和 (4.4) 也不能免费变成共同终点全部占据行的平方和。

此外，额外 mode 在物理压缩中已删掉，但压缩本身不保持核。故 (4.3) 不等于完整 MP 修复，也不证明将所有后续硬核条件施加完之后的总源费用小。真正中层返回与原 same-$w$ 条件仍需共同支付；$N=M$ 保持未证。
