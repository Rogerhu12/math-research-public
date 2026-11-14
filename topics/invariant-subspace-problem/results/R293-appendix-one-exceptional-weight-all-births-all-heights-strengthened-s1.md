# R293 附录：单异常正权加等权池的全部出生、全部高度加强 S1

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下加强桥不等式已证明。** 新增的是实际三次桥费用，不重计这个权族已有的普通相邻序。它也说明强位传输稿中的第二高度必要式，在单异常位的整个权族中不会产生反例。一般独立正权的加强式仍未解决。

## 1. 所证的加强式

对任意有限正权行 $d=\sum b_iE_i$，在合法出生 $s$ 记
$$
G_j=\mathcal J_{j,s}^*\mathcal J_{j,s},\qquad
L_j=\mathcal J_{j,s-1}^*\mathcal J_{j,s-1},\qquad
\mathcal J_{j,r}=(d^j/j!)^\dagger|_{K_r},
$$
$$
C_j=G_j^{-1},\qquad B=\left.\sum b_i^3E_i\right|_{K_s}:K_s\to K_{s-1}.
$$
若 $s=0$，省略下出生和 $B$。令完整高度 $h=N-2s$。对 $1\le n\le h$，最高处约定 $C_{h+1}=0$，其余精度均取真实完整逆后压缩的逆。定义
$$
\delta_{n+1}=\frac1{n+1}(C_nB^*L_{n+2}-C_{n-1}B^*L_{n+1}),
$$
$$
\boxed{
E_n=C_nG_{n-1}C_n-C_{n+1}
-\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*.
}
\tag{1.1}
$$
这里 $L_{n+2}$ 在全部所列高度均合法，因为下出生的高度为 $h+2$。$n=1$ 是 R275 的 S1，$n=2$ 是[强位传输稿](R293-heavy-bit-transfer-of-strengthened-first-edge-sos.md)中的真实必要式。

**定理。** 若原权行只有一个异常权，其余位等权，则每个合法出生及全部 $1\le n\le h$ 都有
$$
E_n\succ0.
\tag{1.2}
$$
最高硬端亦包括在内。共同缩放权行只将 (1.1) 乘一个正数，故证明可把普通池权归一为 $1$。

## 2. 出生一固定线的实际完整最小逆

先取权行
$$
(\sqrt t,\underbrace{1,\ldots,1}_{m\text{ 位}}),\qquad t>0,\quad m\ge2.
$$
出生一的池置换固定 primitive 线由实际向量
$$
v=e_{\rm head}-\frac{\sqrt t}{m}\sum_{i\in\mathrm{pool}}e_i,
\qquad \|v\|^2=1+\frac tm
\tag{2.1}
$$
生成。真空为下出生。

在高度 $j$ 的完整固定输入层，以“头空、池 $j+1$ 孔”与“头占、池 $j$ 孔”的未归一子集和为基。$A_j=d^j/j!$ 的完整 $2\times2$ 矩阵是
$$
\begin{pmatrix}
\binom{m-1}{j}&\sqrt t\binom{m-1}{j-1}\\
0&\binom mj
\end{pmatrix}.
\tag{2.2}
$$
对 $0\le j\le m-1$ 可逆。源 (2.1) 的两个坐标为 $(-\sqrt t/m,1)$，因此唯一固定输入原像为
$$
x_{
m head}=\binom mj^{-1},\qquad
x_{
m pool}=-\frac{\sqrt t(j+1)}{m\binom{m-1}{j}}.
$$
分别乘池子集和的范数平方 $\binom m{j+1}$、$\binom mj$，得到同源能量
$$
\gamma_j=
\frac{t(j+1)}{m\binom{m-1}{j}}+\binom mj^{-1}.
\tag{2.3}
$$
任何完整物理原像经池置换平均后仍解同一方程且范数不增；所以 (2.3) 是整个物理输入层的真正最小值，不只是一个试探原像费用。

将源归一后，固定线上的真实 Gram 与精度是
$$
G_j=\frac{m[m-j+t(j+1)]}{(m+t)(m-j)\binom mj},\qquad
C_j=\frac{(m+t)(m-j)\binom mj}{m[m-j+t(j+1)]}.
\tag{2.4}
$$
真空的真实 Gram 以及归一源上的桥值为
$$
L_j=\frac1{\binom mj+t\binom m{j-1}},\qquad
\beta=B(v/\|v\|)
=\sqrt{\frac{mt}{m+t}}(t-1).
\tag{2.5}
$$
最后一个等式直接来自 $Cv=t^{3/2}-\sqrt t$；它不是由目标不等式反向定义的桥。

## 3. 任意高度的完整正分子

固定 $1\le n\le m-1$，置
$$
k=m-n\ge1,\quad a=m+t,\quad c=\binom mn,
$$
$$
u=k+1+nt,\qquad v_0=k+(n+1)t,\qquad w=k-1+(n+2)t.
$$
全部分母严格为正。由 (2.4)–(2.5)，
$$
C_n=\frac am\frac{kc}{v_0},\quad
C_{n-1}=\frac am\frac{nc}{u},\quad
C_{n+1}=\frac am\frac{k(k-1)c}{(n+1)w},
$$
$$
L_{n+1}=\frac{n+1}{cv_0},\qquad
L_{n+2}=\frac{(n+1)(n+2)}{ckw}.
\tag{3.1}
$$
当 $k=1$，$C_{n+1}=0$ 正是实际硬顶，不使用一个不存在的 Gram。剪切创新准确为
$$
\delta_{n+1}
=\frac{2\beta a(m+1)}{m v_0uw}.
\tag{3.2}
$$
其中用到
$(n+2)u-nw=2(m+1)$；没有漏掉因子 $1/(n+1)$。

将 (3.1)、(3.2) 与 $\beta^2=mt(t-1)^2/(m+t)$ 代入 (1.1)，直接约去共同正因子，得到
$$
\boxed{
E_n=
\frac{m+t}{m}\,
\frac{\binom mn\,k(m+1)}{n(n+1)(n+2)v_0^2u^2}\,
\mathcal R_{n,k}(t),
}
\tag{3.3}
$$
其中只有一个三次多项式：
$$
\boxed{\begin{aligned}
\mathcal R_{n,k}(t)={}&k(k+1)^2(n+2)\\
&+n\{k(3k+5)(n+2)+4(n+1)\}t\\
&+n\{k(3n-1)(n+2)+(3n-2)(n+1)\}t^2\\
&+n^3(n+1)t^3.
\end{aligned}}
\tag{3.4}
$$
因为 $n,k\ge1$，(3.4) 的每个系数严格正，故固定线上的 (1.2) 已证明。

为使约分可逐式复核，约分前的多项式身份是
$$
\begin{aligned}
&k u^3w(n+1)(n+2)
-n(k-1)v_0^2u^2(n+2)
-4nt(t-1)^2(m+1)^2\\
&\hspace{25mm}=(m+1)w\,\mathcal R_{n,k}(t).
\end{aligned}
\tag{3.5}
$$
这是一条普通整数多项式恒等式；全正性不依赖浮点采样、优化或未列出的符号证书。

## 4. 出生一的非固定分支

出生一还有正交空间
$$
V_{\rm std}=\{f:f_{\rm head}=0,\ \sum_{i\in\mathrm{pool}}f_i=0\}.
$$
所有实际 Gram 与池置换交换，在此空间上为标量；这一点也可由任何与全部池置换交换的矩阵具有恒定对角和非对角条目直接看出。三次桥在该空间上为零。

取一个池暗对 $(e_i-e_j)/\sqrt2$，该对被池删除及伴随共同杀掉。其余 $m-2$ 个池位与异常头取真空；这个共同约化源的各阶 Gram 准确为
$$
G_j^{\rm std}=\frac1{\binom{m-2}{j}+t\binom{m-2}{j-1}}.
\tag{4.1}
$$
所有方向具有同一个值。因此 (1.1) 在该分支退化成正初等对称和的严格 Newton 差
$$
\frac{e_n^2}{e_{n-1}}-e_{n+1}>0,
$$
最高层按 $e_{h+1}=0$。这支付完整出生一，不仅是固定线。

## 5. 共同正交池串支付全部物理出生

对一个有 $M$ 个单位权位的原池，在内部 primitive 出生 $j$ 取单位向量 $f$。它的标准正交上升串长为
$$
\ell=M-2j,
$$
删除的相邻系数为 $\sqrt{q(\ell-q+1)}$。这些串及其重数正交穷尽整个池 Hilbert 空间，且同时约化池删除和伴随。池的三次权删除就是同一个池删除，因此也保留每条串。

张量异常单个位后，每个共同约化块恰是长度 $\ell$ 的等权固定串加一异常位。其相对 primitive 出生仅有零和一：相对零用真空初等对称和及零桥，相对一用 §§2–4 的准确加强式。短串 $\ell=0,1$ 中不存在的分支直接删除；高度零没有待证 $n$。

在给定物理出生 $s$，相对零分支来自池内部出生 $j=s$，相对一分支来自 $j=s-1$。两者的实际总高度均为 $M+1-2s$，所有完整逆与三次桥都在同一共同约化分解中处理。因而 (1.1) 是已证严格正块的有限正交直和，得到 (1.2) 的全部物理出生结论。

本稿没有把单异常池的正交分解用于一般独立权，也没有把任意高阶加强式自动等同于全部 one-bit 归纳条件。一般多权、一般 S1/S2 与普通 Hilbert ISP 仍各自保留其缺口。
