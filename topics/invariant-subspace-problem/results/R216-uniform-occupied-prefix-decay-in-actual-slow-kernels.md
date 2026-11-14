# R216：两个实际慢边界核中全占满前缀的统一指数衰减

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本文对 R185/R188 的**整个**实际边界核建立统一估计，不要求向量来自标准递归构造，也不要求事先有任何尾速率。所控制的是整数坐标 $n\equiv-1\pmod{2^m}$，即最初 $m$ 个孔全部占满的投影；它与有限头的补投影不同。该区域恰对应标准右移的坏权。结论给任意小于临界值 1 的指数权控制，但仍远弱于真正右移所需的 $\alpha_m^{-1}$ 权，不能由此宣布内部饱和。

## 1. 对象与主结论

沿用真实负整数边界 $\mathcal H_-=\ell^2(\mathbb N_0)$，
$$
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0,
$$
$$
\mathsf N_j=B^{2^j}/d_j,
\qquad \mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},
\qquad a_j=(j+1)^{-2},
$$
以及两种实际慢算子之一
$$
T=\sum_{j\ge0}a_j\mathsf N_j
\quad\hbox{或}\quad T=\sum_{j\ge0}a_j\mathsf Y_j.
$$
置 $M=\ker T$。

记 $Q_m$ 为正交投影
$$
Q_m e_n=\mathbf 1_{\{2^m\mid n+1\}}e_n,
\qquad Q_0=I.
\tag{1.1}
$$
它投影到第 $0,\ldots,m-1$ 位全部为孔的空间，而不截断其余位。

**定理 1.1。** 对两个模型都成立
$$
\boxed{\|Q_{17r}f\|\le2e^{-4r}\|f\|
\quad(f\in M,\ r\ge1).}
\tag{1.2}
$$
更一般地，对每个 $0<\gamma<1$，存在有限常数 $C_\gamma$，使
$$
\boxed{\|Q_mf\|\le C_\gamma e^{-\gamma m}\|f\|
\quad(f\in M,\ m\ge0).}
\tag{1.3}
$$
常数不依赖 $f$。

令 $q(n)=v_2(n+1)$。由此对每个 $0<s<1$，有 $K_s<\infty$ 满足
$$
\boxed{\sum_{n\ge0}e^{2s q(n)}|f_n|^2\le K_s\|f\|^2
\quad(f\in M).}
\tag{1.4}
$$
这给整个核到一个明确加权 Hilbert 空间的连续嵌入。

## 2. 真进位使全满头分量成为纯尾的超小近核

固定 $r\ge1$。按低 $r$ 位分解整个 Hilbert 空间，令
$g_r$ 表示 $f$ 的低头全孔分量，即
$$
Q_rf=e_{2^r-1}\otimes g_r,
\qquad \|g_r\|=\|Q_rf\|.
$$
定义纯尾消灭算子
$$
D_{\ge r}=\sum_{j\ge r}a_j\mathsf E_j,
\tag{2.1}
$$
它只作用高位。级数按范数绝对收敛。

**引理 2.1。** 对任意 $f\in M$，
$$
\boxed{\|D_{\ge r}g_r\|\le26\eta_{r-1}\|f\|,}
\qquad \eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j}.
\tag{2.2}
$$

证明必须保留低位真正的 borrow。对于 $i<r$，实际链恒等式是
$$
\mathsf N_i=\mathsf N_i^{[r]}
+\frac{\alpha_r}{\alpha_i}
\mathsf E_i^*\cdots\mathsf E_{r-1}^*\mathsf N_r.
\tag{2.3}
$$
这里 $\mathsf N_i^{[r]}$ 作用低 $r$ 位，并为有限加权后移的幂；其输出不可能是该有限头的最高整数 $2^r-1$。所以
$$
Q_r\mathsf N_i^{[r]}=0,\qquad
\|Q_r\mathsf N_i\|\le\alpha_r/\alpha_i\le\eta_{r-1}.
\tag{2.4}
$$
(2.3) 是整个空间上的恒等式，无须把其余位先取真空。

Cayley 情形令
$$
\mathsf Y_i^{[r]}=\mathsf N_i^{[r]}(I+\mathsf N_i^{[r]})^{-1}.
$$
它仍为低头严格下三角矩阵，故 $Q_r\mathsf Y_i^{[r]}=0$。由实际逆差
$$
\mathsf Y_i-\mathsf Y_i^{[r]}
=(I+\mathsf N_i)^{-1}
(\mathsf N_i-\mathsf N_i^{[r]})
(I+\mathsf N_i^{[r]})^{-1}
$$
以及两个逆的范数均不超过 3，得到
$$
\|Q_r\mathsf Y_i\|\le9\alpha_r/\alpha_i\le9\eta_{r-1}.
\tag{2.5}
$$
于是两种模型中低位总贡献统一不超过
$9(\sum_i a_i)\eta_{r-1}\|f\|\le18\eta_{r-1}\|f\|$。

对于 $i\ge r$，实际算子只作用高位，因而与 $Q_r$ 交换；同时
$$
\|\mathsf N_i-\mathsf E_i\|\le\eta_i,\qquad
\|\mathsf Y_i-\mathsf E_i\|\le4\eta_i.
$$
故高尾实际和与 (2.1) 的差不超过
$4(\sum_i a_i)\eta_r\le8\eta_r$。
在 $Q_rTf=0$ 中合并低位和高位误差，就得到
$$
\|D_{\ge r}g_r\|
\le(18\eta_{r-1}+8\eta_r)\|f\|
\le26\eta_{r-1}\|f\|.
$$
证毕。这里未把 $g_r$ 宣布成纯尾的精确核。

## 3. 任意近核的窗口全孔估计

将纯尾分为一个长度 $m$ 的窗口和后续尾：
$$
H_{r,m}=\sum_{j=r}^{r+m-1}a_j\mathsf E_j,
\qquad R_{r,m}=\sum_{j\ge r+m}a_j\mathsf E_j.
$$
两算子交换，$D_{\ge r}=H_{r,m}+R_{r,m}$。记
$$
\tau_r=\sum_{j\ge r}(j+1)^{-2}\le\frac1r\quad(r\ge1).
\tag{3.1}
$$

因为不同孔位的消灭矩阵交换且各自平方为零，精确成立
$$
H_{r,m}^{m}
=m!\left(\prod_{j=r}^{r+m-1}a_j\right)
\mathsf E_r\cdots\mathsf E_{r+m-1}.
\tag{3.2}
$$
右边把窗口全孔分量等距搬到窗口真空。因此对任意高尾向量 $g$，
$$
\|H_{r,m}^{m}g\|
=m!\left(\prod_{j=r}^{r+m-1}a_j\right)
\|P_{\mathrm{all},[r,r+m)}g\|.
\tag{3.3}
$$

多项式因式分解给
$$
H_{r,m}^m-(-R_{r,m})^m
=\sum_{k=0}^{m-1}H_{r,m}^{m-1-k}(-R_{r,m})^kD_{\ge r}.
$$
故若 $\|D_{\ge r}g\|\le\varepsilon$，则
$$
\|H_{r,m}^{m}g\|
\le\tau_{r+m}^m\|g\|+m\tau_r^{m-1}\varepsilon.
\tag{3.4}
$$
结合 (3.1)—(3.4) 以及
$\prod_{j=r}^{r+m-1}a_j=(r!/(r+m)!)^2$，得到
$$
\boxed{
\|P_{\mathrm{all},[r,r+m)}g\|
\le A_{r,m}\|g\|+B_{r,m}\varepsilon,
}
\tag{3.5}
$$
其中
$$
A_{r,m}=\frac{((r+m)!/r!)^2}{m!(r+m)^m},
\qquad
B_{r,m}=\frac{m r^{-(m-1)}((r+m)!/r!)^2}{m!}.
\tag{3.6}
$$
这个有限窗口推导无渐近近似；后续所有误差仅来自引理 2.1 的已付款真实进位。

## 4. 一个完全明确的统一指数常数

在 (3.5) 中取 $m=16r$、$g=g_r$。
于是窗口全孔分量正是原向量的 $Q_{17r}$ 分量。

先证明
$$
A_{r,16r}\le e^{-4r}\quad(r\ge1).
\tag{4.1}
$$
只需以下由积分比较直接得到的阶乘界：
$$
e(n/e)^n\le n!\le en(n/e)^n\quad(n\ge1).
\tag{4.2}
$$
例如对单调函数 $\log x$，
$\int_1^n\log x\,dx\le\log(n!)\le\int_1^n\log x\,dx+\log n$。

用 (4.2) 估计 (3.6)，得到
$$
A_{r,16r}
\le \frac{(17r)^2}{e}
\exp\!\left[r\{18\log17-16\log16-16\}\right].
$$
由 $\log(17/16)\le1/16$ 和 $\log17<3$，花括号小于 $-9$。
又 $(17r)^2/e\le e^{5r}$：$2\log17-1<5$ 且
$2\log r\le2(r-1)\le5(r-1)$。于是 (4.1) 成立。

由 (3.6)，准确有
$$
B_{r,16r}=A_{r,16r}\,16r^2\,17^{16r}.
$$
引理 2.1 给 $\varepsilon\le26\eta_{r-1}\|f\|$，从而
$$
B_{r,16r}\varepsilon
\le e^{-4r}\bigl(416r^2 17^{16r}\eta_{r-1}\bigr)\|f\|
\le e^{-4r}\|f\|.
\tag{4.3}
$$
最后一个因子至多 1：其对数不超过
$$
\log416+2\log r+16r\log17-770\,16^{r-1}
\le7+50r-770\,16^{r-1}<0.
$$
这里用 $16^{r-1}\ge r$，对所有 $r\ge1$ 成立。

(3.5)、(4.1)、(4.3) 和 $\|g_r\|\le\|f\|$ 证明
$$
\|Q_{17r}f\|\le2e^{-4r}\|f\|.
$$
特别，令 $r=\lfloor m/17\rfloor$ 并利用 $Q_m\le Q_{17r}$，即可得到一个显式的全尺度版本
$$
\|Q_mf\|\le2e^4 e^{-4m/17}\|f\|\quad(m\ge0).
\tag{4.4}
$$

## 5. 任意小于 1 的指数率

固定正整数 $c$，在 (3.5) 取 $m=cr$。同一个阶乘界给
$$
A_{r,cr}\le\frac{((c+1)r)^2}{e}\exp[rF(c)],
$$
$$
F(c)=(c+2)\log(c+1)-c\log c-c.
\tag{5.1}
$$
有
$$
\frac{F(c)}{c+1}\longrightarrow-1\qquad(c\to\infty).
\tag{5.2}
$$
这直接由
$F(c)=2\log(c+1)+c\log(1+1/c)-c$ 得到。

给定 $0<\gamma<1$，先选 $\gamma'$ 满足 $\gamma<\gamma'<1$，再固定足够大的 $c$，使
$F(c)<-\gamma'(c+1)$。多项式前因子可在大 $r$ 时由严格的指数余量吸收。
同时
$$
B_{r,cr}=A_{r,cr}\,cr^2(c+1)^{cr},
$$
所以 $26\eta_{r-1}B_{r,cr}$ 也在大 $r$ 时小于任意指定的 $e^{-K r}$；其正项只有 $O_c(r+\log r)$，负项为 $-770\,16^{r-1}$。

由 (3.5) 得，存在 $r_0$ 和常数，使
$$
\|Q_{(c+1)r}f\|\le C e^{-\gamma'(c+1)r}\|f\|
\quad(r\ge r_0).
$$
一般 $m$ 取 $r=\lfloor m/(c+1)\rfloor$，利用投影单调性，将有限个小尺度吸收到常数中，即得 (1.3)。严格指数余量也可把 $\gamma'$ 改成 $\gamma$；此处没有让块长度依赖向量。

## 6. 加权域与目前能推出的范围

对 $q(n)=v_2(n+1)$，由非负项求和，精确有
$$
\sum_ne^{2s q(n)}|f_n|^2
=\|f\|^2+\sum_{m\ge1}
\bigl(e^{2sm}-e^{2s(m-1)}\bigr)\|Q_mf\|^2.
\tag{6.1}
$$
给定 $0<s<1$，取 $s<\gamma<1$，用 (1.3) 后右侧为一个收敛的几何级数乘 $\|f\|^2$，证明 (1.4)。

作为另一个直接推论，$B^*|_M:M\to\mathcal H_-$ 有正的统一下界。
确实，取固定 $m$ 使 $2e^4e^{-4m/17}<1/2$，则
$$
\|B^*f\|^2
=\sum_n\alpha_{q(n)}^2|f_n|^2
\ge\alpha_{m-1}^2\|(I-Q_m)f\|^2
\ge\tfrac34\alpha_{m-1}^2\|f\|^2.
\tag{6.2}
$$
因此 $B^*M$ 是环境空间中的闭子空间。
**这不是** $B|_M$ 的伴随 $P_MB^*|_M$ 的下界：压缩到 $M$ 仍可能消去整个向量，正是未知的 $M\ominus\overline{BM}$ 所对应的情形。

真正标准右移 $J_1$ 的定义域条件为
$$
\sum_n\alpha_{q(n)}^{-2}|f_n|^2<\infty.
$$
实际 $-\log\alpha_q\asymp16^q$，所以 (1.4) 的 $e^{s q}$ 控制远不足于此条件；它也没有给出 $M\cap\operatorname{Dom}J_1$ 的稠密性。另一方面，(1.3) 是对整个 $M$ 一致的真实结论，不能与此前只对递归构造向量的尾预算混为一谈。

## 7. 与移动块下界的关系

[R214](R214-movable-correction-blocks-and-polynomial-tail-obstruction.md) 控制有限头补投影 $(I-P_m)$：非零 $f\in M\ominus N$ 必须具有一定多项式慢的**最高位**尾。
本文控制 $Q_m$：同一个向量在**最低连续孔前缀**上具有统一指数衰减。
两者是不同方向的投影，完全可以同时成立。不得把本文的 $Q_m$ 换成 $I-P_m$，也不得把两条估计直接相撞当作矛盾。

## 8. 固定有限个最高剩余类与全部伴随后移幂

前述全孔条件可扩到每个固定数量的最高剩余类。
固定整数 $k\ge1$，当 $2^m\ge k$ 时，令
$$
Q_m^{[k]}e_n
=\mathbf 1_{\{n\bmod 2^m\in\{2^m-k,\ldots,2^m-1\}\}}e_n.
$$
对于有限个 $2^m<k$ 的尺度可定义 $Q_m^{[k]}=I$。

**定理 8.1。** 对每个固定 $k\ge1$、$0<\gamma<1$，有
$$
\boxed{\|Q_m^{[k]}f\|\le C_{\gamma,k}e^{-\gamma m}\|f\|
\quad(f\in M,\ m\ge0).}
\tag{8.1}
$$

### 8.1. 最高 $k$ 行的真实近方程

固定 $r$ 且 $2^r\ge k$，令 $g$ 为 $f$ 的低 $r$ 位最高 $k$ 行组成的向量，视为 $\mathbb C^k$ 值高尾。
有限头 $T_r$ 严格下三角，所以投影到最高 $k$ 行时，来自其余更低头行的矩阵块严格为零。设相应 $k\times k$ 角为 $C_{r,k}$，则
$$
C_{r,k}^k=0,\qquad \|C_{r,k}\|\le6.
$$
第 2 节同一真实链和逆差估计给全空间比较
$$
\|T-(T_r\otimes I+I\otimes D_{\ge r})\|\le26\eta_{r-1}.
$$
因此在 $Tf=0$ 上，有
$$
(C_{r,k}+D_{\ge r})g=e,
\qquad \|e\|\le26\eta_{r-1}\|f\|.
\tag{8.2}
$$
$C_{r,k}$ 和 $D_{\ge r}$ 作用不同因子而交换。由 $C_{r,k}^k=0$ 及多项式差幂公式，
$$
D_{\ge r}^{k}g
=\sum_{j=0}^{k-1}D_{\ge r}^{k-1-j}(-C_{r,k})^j e.
$$
故
$$
\boxed{\|D_{\ge r}^{k}g\|
\le26k6^{k-1}\eta_{r-1}\|f\|.}
\tag{8.3}
$$
本式为固定阶的近广义核结论，没有取消真实误差。

### 8.2. 长窗口消去

仍写 $D_{\ge r}=H_{r,m}+R_{r,m}$，并取 $m\ge k$。
二项式展开中将 $D_{\ge r}$ 的次数小于 $k$ 的项单列，得
$$
H_{r,m}^{m}g
=\sum_{j=0}^{k-1}\binom mj(-R_{r,m})^{m-j}D_{\ge r}^j g
+\mathcal E g,
$$
其中
$$
\|\mathcal E g\|
\le2^m\tau_r^{m-k}\|D_{\ge r}^kg\|.
$$
令 $n=r+m$，使用 $\tau_r\le1/r$、$\tau_n\le1/n$ 和精确的 (3.3)，得到
$$
\begin{aligned}
\|Q_{r+m}^{[k]}f\|
\le{}&A_{r,m}\left[\sum_{j=0}^{k-1}\binom mj(n/r)^j\right]\|f\|\\
&+A_{r,m}\,2^m r^k(n/r)^m\,
26k6^{k-1}\eta_{r-1}\|f\|.
\end{aligned}
\tag{8.4}
$$
窗口全孔、原低 $r$ 位属于最高 $k$ 行，恰好拼成低 $r+m$ 位最高 $k$ 行，所以左边的投影确实是所写的 $Q_{r+m}^{[k]}$。

固定 $m=cr$ 后，方括号只是关于 $r$ 的 $k-1$ 次多项式，第二行的正增长是 $\exp(O_{c,k}(r+\log r))$；它被 $\eta_{r-1}$ 的 $\exp(-770\,16^{r-1})$ 压倒。
照第 5 节选取固定大 $c$，严格指数余量吸收这些固定次数多项式。再以 $r=\lfloor m/(c+1)\rfloor$ 插值尺度，证明 (8.1)。

### 8.3. 所有固定幂的环境下界

取一个固定整数 $k\ge1$。在 $Q_m^{[k]}$ 的补集上，$n+1,\ldots,n+k$ 没有一个被 $2^m$ 整除。因此
$$
\prod_{t=1}^k\alpha_{v_2(n+t)}\ge\alpha_{m-1}^k.
$$
由 (8.1)，可选一个固定 $m$，使
$\|Q_m^{[k]}f\|\le\frac12\|f\|$ 对所有 $f\in M$ 成立。于是
$$
\boxed{
\|(B^*)^kf\|\ge\frac{\sqrt3}{2}\alpha_{m-1}^k\|f\|
\quad(f\in M).
}
\tag{8.5}
$$
故每个 $(B^*)^kM$ 都是环境空间中的闭子空间。

等价地，$P_MB^k:\mathcal H_-\to M$ 是满射；这一等价只用 Hilbert 空间闭值域定理，伴随正是 $(B^*)^k|_M$。
该满射的预像不保证落在 $M$。未知的 $\overline{B^kM}=N$ 与这里的 $P_MB^k\mathcal H_-=M$ 不同，所以 (8.5) 仍未证明 $N=M$。
