# R271 附录：一位硬核的完整源 Schur、真实投影损失与同源两阶高度矩

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 在同一个 bosonic Fock 空间中，把一个 mode 改为真实硬核位，保全部横向零源后得到准确的 $2\times2$ 头 Gram 和完整 Schur。原投影与新投影之差，下面由该位的实际双占据能量控制，上面由一个明确可行核列控制；可行列不被认作新最小列。将逐位投影损失与已付对数方差导数合用，可在同一来源上同时支付
$$
\sum_j\left[j+\frac{j(j-1)}x\right]E_j
\le 30000\,\Delta_Q^2,
$$
并在原 moving-$m$ 窗口中使左边趋零。选择只作一次，先于全部合法 $Q$。

依据：

- [放大方差、共同 Fock 闭核及同源物理列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)；
- [真实强前缀与原大头的完整 Gram 比较](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)；
- [完整 Gram 的对数方差选择](R271-appendix-log-variance-selection-and-complete-source-first-height-moment.md)；
- [公共兼容塔的指数中段障碍](R271-appendix-continuous-compatible-towers-exponential-middle-height-barrier.md)。

本稿最后一个结果是实际最小源的矩预算，不声称它支付公共塔的指数中段系数，也不把小碰撞距离直接替换为到全部物理真核的距离。

## 1. 两个 mode 的真实闭核和全部源

令 $\mathcal H$ 为 Hilbert 头空间，$C$ 为有界算子，$C^h=0$，其中 $h\ge1$。取
$$
b>0,\qquad s'>0,\qquad S=b^2+s',\qquad p=\frac{b^2}{S}\in(0,1).
\tag{1.1}
$$
在 $\mathcal H\otimes\mathcal F(\mathbb C^2)$ 中，$a_i,a_r$ 是两个标准 bosonic annihilator，归一基满足 $a|j\rangle=\sqrt j\,|j-1\rangle$。定义闭算子
$$
\mathcal B=C+b\,a_i+\sqrt{s'}\,a_r
\tag{1.2}
$$
于 annihilator 的自然定义域。$C$ 有界，故这是闭 annihilator 的有界扰动。置
$$
\mathscr M_0=\ker\mathcal B,\qquad
\mathscr M_1=\mathscr M_0\cap\{N_i\le1\}.
\tag{1.3}
$$
两者都是闭子空间，且 $\mathscr M_1\subset\mathscr M_0$。这里先在同一 Fock 空间中取交，没有把物理硬核投影假定为核保持算子。

以单位正交变换改用 collective mode
$$
a_c=\frac{b a_i+\sqrt{s'}a_r}{\sqrt S}
$$
及其正交 transverse mode。于是 $\mathcal B=C+\sqrt S\,a_c$，不作用在 transverse mode 上。强迫
$$
f=g\otimes|0,0\rangle
$$
处于 transverse 真空。按 transverse 占据分解的各空间约化 $\mathscr M_0$，所以 $P_{\mathscr M_0}f$ 的 transverse 分量仍严格为零。这一步保留并正交消去了全部非零 transverse 源。

定义完整头 Gram
$$
H_C(S)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{S^j j!},\qquad
a=H_C(S)^{-1}g,\qquad
E_j=\frac{\|C^j a\|^2}{S^j j!}.
\tag{1.4}
$$
$H_C(S)\succeq I$。直接逐层求解闭核方程，得到
$$
v=P_{\mathscr M_0}f
=\sum_{j=0}^{h-1}\frac{(-C)^ja\otimes|j_c,0_\perp\rangle}{S^{j/2}\sqrt{j!}},
\qquad
q_0=\|v\|^2=\langle g,H_C(S)^{-1}g\rangle.
\tag{1.5}
$$
所有列都是有限多项式，属于 (1.2) 的自然域。一般 transverse 源虽可有无限 Fock 次数，已由上面的真实约化正交性处理；没有只在真空列上偷换完整投影。

在 $\{N_i\le1\}$ 中，$a_i$ 的限制正是 Boolean 删除 $E$。把这一位并入头，得到
$$
C'=\begin{pmatrix}C&bI\\0&C\end{pmatrix}=C+bE,
\qquad (C')^{h+1}=0.
\tag{1.6}
$$
新核为 $C'+\sqrt{s'}a_r$ 的完整核，所有头源 $(a_0,a_1)\in\mathcal H\oplus\mathcal H$ 都保留。记
$$
H=H_C(s'),\qquad
B=\left(1+\frac{b^2}{s'}\right)H+
          \frac{b^2}{s'^2}C^*HC .
$$
从
$$
(C')^j=\begin{pmatrix}C^j&jbC^{j-1}\\0&C^j\end{pmatrix}
$$
逐项计算，得完整新 Gram
$$
\boxed{
H_{C'}(s')=
\begin{pmatrix}
H&(b/s')C^*H\\
(b/s')HC&B
\end{pmatrix}.
}
\tag{1.7}
$$
$B\succeq I$，而且整块 $\succeq I$。因此真正消去新位源 $a_1$ 后的 Schur 为
$$
\boxed{
H_{\rm eff}
=H-\frac{b^2}{s'^2}C^*H B^{-1}HC,\qquad
q_1=\|P_{\mathscr M_1}f\|^2
=\langle g,H_{\rm eff}^{-1}g\rangle .
}
\tag{1.8}
$$
这是先保全部新源再作最小化。特别 $C^*HB^{-1}HC$ 的次序不能改变。

## 2. 一个可行核列及完整 Schur 的形式比较

取新头源
$$
a'=\left(a,-\frac bS Ca\right).
\tag{2.1}
$$
其真实核列记作 $z$. 在 Bargmann 记号下可写为有限多项式
$$
z=\exp\!\left(-\frac{Cz_r}{\sqrt{s'}}\right)
\left[a-\frac bS Ca\left(z_i-\frac b{\sqrt{s'}}z_r\right)\right].
\tag{2.2}
$$
直接微分验证 $\mathcal Bz=0$；它对 $z_i$ 至多一次，所以 $z\in\mathscr M_1$。亦可完全用归一 Fock 基验证，因为
$$
(C')^k a'
=\left((1-kp)C^ka,-\frac bS C^{k+1}a\right).
\tag{2.3}
$$
故候选的总尾次数仍小于 $h$；新增一位没有把这个特定源的终端高度增加一层。

固定总尾次数 $j$。相对于 (1.5) 第 $j$ 列的头范数，$z$ 的 bit-$0$ 和 bit-$1$ 系数分别为
$$
(1-jp)(1-p)^{-j/2},\qquad
\sqrt{jp}\,(1-p)^{-(j-1)/2}.
$$
因此
$$
\langle v_j,z_j\rangle=E_j,\qquad
\|z_j\|^2=A_j(p)E_j,
$$
其中
$$
\boxed{
A_j(p)=(1-p)^{-j}[1-jp+j(j-1)p^2].
}
\tag{2.4}
$$
这也给 $\langle f,z\rangle=\langle g,a\rangle=q_0$。不同总尾次数正交，故
$$
\boxed{\|z-v\|^2=\sum_j[A_j(p)-1]E_j.}
\tag{2.5}
$$
$j=0,1$ 的差严格为零；对 $j\ge2$，
$$
0\le A_j(p)-1
\le j(j-1)p^2(1-p)^{-j}.
\tag{2.6}
$$
上界来自 $(1-p)^j\ge1-jp$；非负性也由 (2.5) 在各固定 $j$ 上的平方得到。

定义
$$
W_p=\sum_{j=0}^{h-1}
[A_j(p)-1]\frac{(C^*)^jC^j}{S^j j!}.
$$
不将候选当作最小列，有完整形式比较
$$
\boxed{H_C(S)\preceq H_{\rm eff}\preceq H_C(S)+W_p.}
\tag{2.7}
$$
右边是在固定 $a_0=a$ 时使用 (2.1) 的可行上界。左边可由嵌套投影给
$H_{\rm eff}^{-1}\preceq H_C(S)^{-1}$ 后合法反转；两者都为有界严格正算子。等价地，固定全部两-mode 真空系数后，旧 collective 真空列是旧核中的最小能量，任何新硬核合法列不可能比它更小。

## 3. 真实投影损失的两侧界

令
$$
c_j(p)=1-(1-p)^j-jp(1-p)^{j-1}.
\tag{3.1}
$$
这是旧第 $j$ 个 collective 粒子列在新位上出现至少两个粒子的准确概率。于是
$$
\|P_{\{N_i\ge2\}}v\|^2=\sum_j c_j(p)E_j.
$$
$P_{\mathscr M_1}f=P_{\mathscr M_1}v$，嵌套正交投影给
$$
q_0-q_1=\|v-P_{\mathscr M_1}v\|^2.
$$
新投影位于 $\{N_i\le1\}$，而 $z$ 是该闭核中的合法候选。因此
$$
\boxed{
\sum_j c_j(p)E_j
\le q_0-q_1
\le\sum_j[A_j(p)-1]E_j.
}
\tag{3.2}
$$
这是真最小源的标量二次型差，不是只计算某个候选的能量。

对 $j\ge2$，保留恰好双占据的概率给
$$
c_j(p)\ge\frac{j(j-1)}2p^2(1-p)^{j-2}.
\tag{3.3}
$$
因此当所有非零列满足 $jp\le K$、$p\le p_0<1$ 时，两端都与
$p^2\sum_jj(j-1)E_j$ 在只依赖 $K,p_0$ 的常数内可比。这里没有将这些常数乘到一个未经证明的公共塔 inverse 上。

## 4. 原连续尾逐位损失的准确累计

固定原 N 或 Y 头 $A_m$，$d=2^m$。对整数 $y\ge m$ 定义
$$
b_i=(i+1)^{-2},\quad
S_y=\sum_{i\ge y}b_i^2,\quad
C_y=A_m+D_{[m,y)},\quad h_y=d+y-m.
\tag{4.1}
$$
全强头保留，$C_y^{h_y}=0$。forcing $g_y$ 是同一个原有限头向量 $g$，在 $[m,y)$ 位补真空。

先取原方差 $S_y$。在同一全尾 Fock 空间上固定闭算子
$A_m+\sum_{i\ge m}b_i a_i$，只逐次加入 $m,\ldots,y-1$ 位硬核约束。相应闭核 $\mathscr K_y$ 递减，且
$$
q_y(0)=\|P_{\mathscr K_y}f\|^2
=\langle g_y,H_{C_y}(S_y)^{-1}g_y\rangle.
$$
每一差 $q_y(0)-q_{y+1}(0)$ 都由 (3.2) 给出。若 $y\ge\max(10,m+d)$，则
$$
\frac3{y+4}\le p_y=\frac{b_y^2}{S_y}\le\frac3{y+1},
\quad j<h_y\le2y,\quad (1-p_y)^j\ge e^{-8}.
$$
最后一个不等式用 $-\log(1-p)\le p/(1-p)$。因此，写
$\mathfrak F_2(y)=\sum_jj(j-1)E_j(y)$，得到
$$
\boxed{
\frac{9e^{-8}}{2(y+4)^2}\mathfrak F_2(y)
\le q_y(0)-q_{y+1}(0)
\le\frac{9e^8}{(y+1)^2}\mathfrak F_2(y).
}
\tag{4.2}
$$

有限区间的损失准确望远镜。无限区间也可取递减闭子空间投影的强极限。其交是全尾硬核空间内的 $\ker L_m$：在该物理空间上原删除 $D_{\ge m}$ 有界，Fock 自然域与其作用相容，闭核方程就是 $L_m=A_m+D_{\ge m}$。所以
$$
\sum_{y\ge x}\frac{\mathfrak F_2(y)}{(y+4)^2}
\le\frac{2e^8}{9}
\left[q_x(0)-\|P_{\ker L_m}f\|^2\right].
\tag{4.3}
$$
这没有给括号随 $m$ 的未知衰减率，也没有把 $\ker L_m$ 改成原全局 $M$。

## 5. 同一来源的一阶与二阶矩可同时选择

现在取整数
$$
x\ge\max(10,m+d),\qquad y\in\{x,\ldots,2x-1\}.
$$
额外加入一个独立 bosonic mode，其方差为
$$
t\in[S_x,2S_x].
$$
这个 mode 只用于完整 Gram 和选择参数，不被称为原物理新位。对固定 $t$，仍在同一 Fock 空间中逐位施加硬核条件；未处理尾和额外 mode 合成的方差为
$$
s_y(t)=S_y+t.
$$
记
$$
a_y(t)=H_{C_y}(s_y(t))^{-1}g_y,\quad
E_j(y,t)=\frac{\|C_y^ja_y(t)\|^2}{s_y(t)^j j!},
$$
$$
q_y(t)=\langle g_y,a_y(t)\rangle,\quad
\mathfrak F_1(y,t)=\sum_jjE_j(y,t),\quad
\mathfrak F_2(y,t)=\sum_jj(j-1)E_j(y,t).
\tag{5.1}
$$
固定 $t$ 时 $q_y(t)$ 随 $y$ 不增；固定 $y$ 时它随 $t$ 不减。置
$$
\mathcal V_x=q_x(2S_x)-q_{2x}(S_x)\ge0.
\tag{5.2}
$$

原尾积分比较为
$$
\frac1{3(y+1)^3}\le S_y
\le\frac{y+4}{3(y+1)^4}.
\tag{5.3}
$$
对当前矩形区间，一位参数 $p_y=b_y^2/(t+S_y)$ 满足
$$
p_y\ge\frac1{16x},\qquad
p_y\le\frac3{2(x+1)},\qquad jp_y\le3.
\tag{5.4}
$$
第一式用 $b_y^2\ge(2x)^{-4}$、$t+S_y\le3S_x$，
以及 $(x+1)^4\ge x^3(x+4)$。后两式用
$$
t+S_y\ge
\frac1{3(x+1)^3}+\frac1{3(y+1)^3},
$$
从而
$$
p_y\le\frac3{y+1+(y+1)^4/(x+1)^3},
\qquad j<h_y\le y+x.
$$
由于 $x\ge10$，(5.4) 给 $(1-p_y)^j\ge e^{-4}$。把 (3.3) 放入真实损失，得
$$
\frac{\mathfrak F_2(y,t)}{512e^4x^2}
\le q_y(t)-q_{y+1}(t).
\tag{5.5}
$$
所以对每个 $t$，
$$
\frac1x\sum_{y=x}^{2x-1}\frac{\mathfrak F_2(y,t)}x
\le512e^4\,\mathcal V_x.
\tag{5.6}
$$

另一方面，已付完整 inverse 的对数导数在这里准确变为
$$
\frac{dq_y}{d\log t}
=\frac{t}{t+S_y}\mathfrak F_1(y,t).
$$
$t\ge S_x\ge S_y$，故这个前因子至少 $1/2$。积分给
$$
\int_{\log S_x}^{\log(2S_x)}
\mathfrak F_1(y,e^\tau)\,d\tau
\le2[q_y(2S_x)-q_y(S_x)]
\le2\mathcal V_x.
\tag{5.7}
$$
将 (5.6)、(5.7) 在有限 $y$ 集合和 $\log t$ 区间上平均。全部被积函数非负连续，故存在同一个 $(y_*,t_*)$，使
$$
\boxed{
\mathfrak F_1(y_*,t_*)+\frac{\mathfrak F_2(y_*,t_*)}x
\le
\left(512e^4+\frac2{\log2}\right)\mathcal V_x
<30000\,\mathcal V_x.
}
\tag{5.8}
$$
若 $\mathcal V_x=0$，同一结论由非负积分为零成立。没有为两阶矩分别重选两个来源。

## 6. 原同一 $V_Q/K_Q/u_f$ 与 moving-$m$ 范围

以上实际源全部来自同一个有限物理 forcing $f$，在充分大的原头中取 $g=f$。选择 $(y_*,t_*)$ 不含 $Q$。令
$$
R_y=y-m,\qquad s=s_y(t),\qquad
F_{y,t}
=\sum_{j=0}^{h_y-1}
\frac{(-C_y)^ja_y(t)\otimes\omega_{j,y}}{s^jj!},
\quad
\omega_{j,y}=(D_y^*)^j\Omega.
\tag{6.1}
$$
这是原硬核物理列，不是上面的辅助 bosonic 向量。因
$\|\omega_{j,y}\|^2\le j!S_y^j\le j!s^j$，
$$
\|F_{y,t}\|^2\le q_y(t).
$$
已付逐列同源身份在
$$
Q\ge R_y+h_y-1
$$
给出
$$
P_{V_{m,Q}}F_{y,t}=P_{V_{m,Q}}f,\qquad
P_{K_{m,Q}}F_{y,t}=P_{K_{m,Q}}f.
\tag{6.2}
$$
全部强头、完整零源和原两个投影均保留。因此对同一个
$$
u_{m,Q,f}=(P_{V_{m,Q}}-P_{K_{m,Q}})f,\qquad
\Delta_{m,Q,f}^2=\|f-u_{m,Q,f}\|^2,
$$
有 $q_y(t)\ge\|u_{m,Q,f}\|^2$。

若一次取
$$
Q\ge d+4x-2m,
\tag{6.3}
$$
则 (6.2) 对选择矩形及端点 $y=2x$ 全部成立。结合
$q_x(2S_x)\le\|f\|^2$，得到
$$
\mathcal V_x\le\Delta_{m,Q,f}^2
$$
以及同一个来源上的
$$
\boxed{
\sum_j\left[j+\frac{j(j-1)}x\right]E_j(y_*,t_*)
\le30000\,\Delta_{m,Q,f}^2
}
\tag{6.4}
$$
对所有满足 (6.3) 的合法原 cut 同时成立。

最后取 $d=2^m$、$x=m+d$。当 $m$ 充分大时，整个 $y\in[x,2x]$ 满足
$y+1\le d^{4/3}/8$，而 $s_y(t)\ge S_y$ 且 $s_y(t)\to0$。
真实强前缀完整 Gram 定理因此给 (5.2) 的两端同趋
$\|P_Mf\|^2$，故
$$
\mathcal V_x\longrightarrow0,\qquad
\mathfrak F_1(y_*,t_*)+\mathfrak F_2(y_*,t_*)/x\longrightarrow0.
\tag{6.5}
$$
例如 $m\ge16$ 已使上面的几何区间条件成立；(6.3) 可由 $Q\ge6d$ 保证，仍落在原 $4d\le Q\le e^{26d^3}$ 母窗口内。这里是更换辅助强前缀和方差而保持同一原 $u_{m,Q,f}$，不是更换原算子或原测试向量。

## 7. 未付的完整返回

(3.2) 是单步实际投影损失的双侧界，(4.3) 是逐位真损失的准确累计，(6.4) 是同一原缺陷控制的两阶矩。三者都保了完整横向自由和 Schur 最小化。

但从 $y$ 到无限多硬核位的实际源会重新最小化，不能将后续源的能量免费换成 $a_y(t)$ 的能量；额外方差 $t>0$ 也不是原物理尾的一部分。公共兼容塔在 $j\le x$ 的指数障碍仍在。本稿没有由 (6.4) 推出全部顺次 MP 修复，也没有删除真实返回投影或原 $T$ 的 carry／同一 $w$ 条件。$N=M$ 仍未由此证明。
