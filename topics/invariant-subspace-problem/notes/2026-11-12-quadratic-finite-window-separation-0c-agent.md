# 二阶端点对任意有限 chaos 的分离：固定头窗口与分层创建

日期：2026-11-12（UTC）。负责人：literature。预留 R99。

**状态：下述有限 Toeplitz 创建引理及二阶配对分离定理已证明。** 实际窗口恢复调用 R100 的完整证明；顶阶平方和剥离调用 R98，并保留较低次数和先前头行造成的交叉项。第 4 节的初等标量卷积递推由 l2_moments 提供，已逐项核验。

**主结论。** 若 $0\ne f\in H_{\le2}$，$0\ne g\in H_{\le q}$，其中 $q<\infty$，则存在 $n\ge0$ 使
$$
B(A^nf,g)\ne0.
\tag{0.1}
$$
由 $B$ 对称性，也可交换两端。这里排除的是有限 chaos 消失端点；没有把它扩成任意 $g\in H$，没有声称二阶向量已对整个 Hilbert 空间循环。

当某端是非零常数，已有常向量循环性即可处理；一次端点已由先前结果处理。以下证明 $f$ 的实际最高次数为 $2$，$g$ 的实际最高次数为 $q\ge1$，并反设全部实际矩为零。

依赖的完整稿：

- R96：2026-11-12-high-chaos-residual-mass-peeling-0c-agent.md；
- R97：2026-11-12-fischer-collision-influence-creation-0c-agent.md；
- R98：2026-11-12-conditioned-head-recovery-and-hs-tail-cover-0c.md；
- R100：2026-11-12-fixed-window-vector-convolution-0c-agent.md。

## 1. 纯尾符号、固定次数有界性与头记号

设剩余尾指标集为 $E$。对有限 Walsh 次数向量
$$
v=\sum_Jv_J\chi_J
$$
定义纯模型乘法
$$
\mathcal M(v)=\sum_J(-1)^{|J|}v_JS_J,
\qquad S_j=2E_j-I.
\tag{1.1}
$$
无限 $\ell^2$ 系数按 R84 的固定次数合成理解。对任意固定输入次数上限 $q$，有
$$
\|\mathcal M(v)\|_{H_{\le q}\to H_{\le q+r}}
\le C_{r,q}\|v\|_2,\qquad v\in H_{\le r}.
\tag{1.2}
$$
这不是在全 $H$ 上断言每个有限 chaos 符号都有有界乘法。

若 $a$ 纯一次，$\mathcal M(a)$ 的最高升一阶部分是平方零创建 $C_a$，其余部分至多保阶；常数 $d$ 对应 $dI$。若 $u$ 纯二次，其全部模型乘法在固定次数层间的范数不超过 $C_{2,q}\|u\|_2$。

选择固定集合
$$
|S_f|=2,\qquad |S_g|=q,\qquad
\widehat f(S_f)\ne0,\quad\widehat g(S_g)\ne0.
$$
记
$$
D_f=\sum_{j\in S_f}2^j,\qquad
D_g=\sum_{j\in S_g}2^j,\qquad
R=D_f+D_g,\qquad
L=D_g+(q+1)R.
\tag{1.3}
$$
这些是固定整数，依赖所选非零系数，但不随尾起点 $m$ 或条件化集变化。

以下总取 $m$ 充分大，使 $2^m>L$，且 $S_f,S_g\subseteq[0,m)$。任意有限异常位集 $B$ 都包含在 $[m,\infty)$，记 $s=|B|$。将 $B$ 物理条件为 $0$ 后，在低 $m$ 位整数 $i$ 处取列：
$$
F_i=f_B(i,\cdot),\qquad G_i=g_B(i,\cdot),\qquad 0\le i\le L.
\tag{1.4}
$$
这是先对有限多个位条件化，得到剩余尾上的有限次数 $L^2$ 向量；不对无限尾取点值。

## 2. 实际固定窗口、单位变换及多项式范数界

记 $W_i=\|A^i\|$，$W_0=1$。在截断环 $\mathbb C[z]/(z^{L+1})$ 中定义
$$
b(z)=\sum_{i=0}^L\frac{z^i}{W_i},
\qquad
\beta(z)=b(z)^{-1}=\sum_{i=0}^L\beta_i z^i.
\tag{2.1}
$$
因为 $b(0)=1$，这是唯一的有限三角递推，不涉及无穷级数收敛。

令
$$
c_i=\sum_{h=0}^i\beta_{i-h}\frac{F_h}{W_h},
\qquad
g_i=\frac{G_i}{W_i}.
\tag{2.2}
$$
R100 的实际零矩恢复及其输出同一单位变换给出
$$
Y_r=\sum_{i=0}^r\mathcal M(c_i)g_{r-i},
\qquad
\|Y_r\|_2\le\varepsilon_{m,s},
\qquad 0\le r\le L,
\tag{2.3}
$$
其中固定 $f,g,L,q$ 的常数已吸收，且
$$
\log\varepsilon_{m,s}
\le-\frac{260}{3}16^m+s\log2
+O_{f,g,L,q}(8^m+m2^m+\log(s+1)).
\tag{2.4}
$$
特别地，这对任意位置的 $B$ 成立；不要求其最大顶点受控。

同一个窗口也可从 R98 的完整头模型取前 $L+1$ 个物理列，再乘固定的 $W_i^{-1}$ 和 $\beta$ 得到。R100 则直接给出更好的窗口恢复，不必恢复全部 $2^m$ 个头分量。

### 2.1. 列范数只按条件位数的多项式增长

若 $h$ 的总次数至多 $d$，固定任意 $t$ 个物理位，按这些位上的 Walsh 系数分组后使用 Cauchy–Schwarz，得到
$$
\|h|_{\rm fixed}\|_2
\le D_d(t)\|h\|_2,\qquad
D_d(t)=\left(\sum_{k=0}^d{t\choose k}\right)^{1/2}
\le C_d(1+t)^{d/2}.
\tag{2.5}
$$
这里已有 $m$ 个头位和 $s$ 个异常位被固定，所以
$$
\|F_i\|_2\le C(1+m+s)\|f\|_2,\qquad
\|G_i\|_2\le C_q(1+m+s)^{q/2}\|g\|_2.
\tag{2.6}
$$
固定窗口变换 (2.2) 只乘固定常数。因此可选
$$
M_{m,s}=C_{f,g,L,q}(1+m+s)^d\ge1
\tag{2.7}
$$
控制全部窗口符号系数、其固定次数算子范数和全部 $\|g_i\|_2$；$d$ 是固定整数。若 $s=O(16^m)$，则
$$
\log M_{m,s}=O(m).
\tag{2.8}
$$
这一点保证稍后有限多层阈值之间不会被条件化范数损失耗尽。

### 2.2. 顶二次核只出现在第零头系数

每个 $F_i$ 的纯尾二次部分都是同一个删点核
$$
u=u_m^{\setminus B},
$$
因为原来的总次数只有 $2$，带有任何头 Walsh 因子的项都只能有至多一次尾次数。由 $\beta b=1$，
$$
\boxed{
c_0=d_0+a_0+u,\qquad
c_i=d_i+a_i\quad(1\le i\le L),
}
\tag{2.9}
$$
其中 $d_i\in\mathbb C$，$a_i$ 为纯一次尾向量。正头系数中没有二次尾项；这不是将它们忽略，而是有限单位变换的精确消去。

### 2.3. 固定低位系数给两个不坍缩锚

设 $\ell(H)=\langle H,1\rangle$ 是剩余尾上的常数系数。对 $T\subseteq S_f$，令 $n(T)=\sum_{j\in T}2^j$。由于 $|S_f|$ 已是 $f$ 的最高次数，
$$
2^{-2}\sum_{T\subseteq S_f}(-1)^{|T|}
\ell(F_{n(T)})=\widehat f(S_f).
\tag{2.10}
$$
任何额外变量都会使次数超过 $2$，所以固定其他头位和高位 $B$ 不改变右边。对 $g$ 同理：
$$
2^{-q}\sum_{T\subseteq S_g}(-1)^{|T|}
\ell(G_{n(T)})=\widehat g(S_g).
\tag{2.11}
$$
有限三角变换 (2.2) 在初段可逆，故存在固定 $\gamma_f,\gamma_g>0$，使对所有 $m,B$，
$$
\boxed{
\max_{0\le i\le D_f}|d_i|\ge\gamma_f,\qquad
\max_{0\le j\le D_g}|\ell(g_j)|\ge\gamma_g.
}
\tag{2.12}
$$
特别地，全部 $\|g_j\|$ 的前 $D_g+1$ 列不可能同时趋零。

## 3. 有限 Toeplitz 头创建引理

本节是本稿新增的核心有限窗口工具。

**引理 3.1。** 固定 $q,L\ge0$，设符号
$$
v_i=d_i+a_i,\qquad 0\le i\le L,
$$
其中 $a_i$ 纯一次，输入 $h_i$ 的尾次数至多 $q$，并令
$$
Z_n=\sum_{i=0}^n\mathcal M(v_i)h_{n-i}.
\tag{3.1}
$$
所有固定次数算子范数、$|d_i|$、$\|a_i\|$ 均由 $M\ge1$ 控制。取 $0\le j\le L$，并假设：

- $a_i=0$ 对所有 $i<j$；
- 创建 $C_{a_j}$ 在每个纯尾次数 $k\le q$ 上都有左界至少 $t$，其中 $0<t\le1$；
- $D+(q+1)j\le L$。

则存在只依赖 $q,L$ 的常数 $C$ 和整数
$$
K=(q+1)(L+3)
\tag{3.2}
$$
使
$$
\boxed{
\left(\sum_{r=0}^D\|h_r\|_2^2\right)^{1/2}
\le C M^K t^{-K}
\max_{0\le n\le L}\|Z_n\|_2.
}
\tag{3.3}
$$
可放大 $M$ 一个只依赖 $q$ 的常数以包括各升、降、保阶部分；这不改变结论的参数依赖。

### 3.1. 先按头指标建立有限三角左逆

固定一个纯尾次数 $k$。对于 $0\le r\le h$，考虑方程
$$
C_{a_j}x_r+\sum_{i=j+1}^{r+j}C_{a_i}x_{r+j-i}=y_r.
\tag{3.4}
$$
对 $C_{a_j}$ 取范数至多 $t^{-1}$ 的有界左逆。作用到每行后，得到
$$
(I+T)x=Ly,
$$
其中 $T$ 在头指标上严格下三角，所以 $T^{h+1}=0$。其范数至多 $(h+1)M/t$，故
$$
x=\sum_{\nu=0}^h(-T)^\nu Ly
$$
满足
$$
\|x\|
\le t^{-1}\sum_{\nu=0}^h
\left(\frac{(h+1)M}{t}\right)^\nu\|y\|
\le C_L\left(\frac Mt\right)^{L+1}\|y\|,
\qquad h\le L.
\tag{3.5}
$$
本步只使用真正的有限三角结构；不要求不同创建的左逆互相交换。

### 3.2. 再按尾次数下降，明确支付窗口损失

写 $h_r=\sum_{k=0}^q h_{r,k}$。最高输出尾次数 $q+1$ 中，只有创建部分参与。由于 $a_i=0$ 对 $i<j$，输出头 $n=r+j$ 的方程正是 (3.4)，其未知量为 $h_{r,q}$。因此 (3.5) 控制
$$
h_{r,q},\qquad 0\le r\le L-j.
$$

下一层输出尾次数 $q$ 中，未知的最高来源是
$C_{a_i}h_{n-i,q-1}$；其余项来自已控制的 $h_{\cdot,q}$，但常数头系数 $d_0$ 可以把它带到同一头指标 $n$。所以本层必须把可用输出窗口缩到 $n\le L-j$，从而只恢复
$$
h_{r,q-1},\qquad 0\le r\le L-2j.
$$
不能将前行较低尾次数与后行 $h$ 的贡献丢掉。

一般地，在恢复尾次数 $k$ 时，只使用输出
$$
n\le L-(q-k)j.
$$
所有更高尾次数的输入在这个头窗口内已被前面步骤控制；头递推 (3.5) 恢复
$$
h_{r,k},\qquad
0\le r\le L-(q-k+1)j.
\tag{3.6}
$$
每层的已知余项范数至多是
$(L+1)M$ 乘前面高尾层的有限范数和。设
$Q=C_L(M/t)^{L+1}$。有限的 $q+1$ 次下降递推给总上界
$$
C_{q,L}Q(1+C_LMQ)^q
\max_n\|Z_n\|
\le C_{q,L}M^Kt^{-K}\max_n\|Z_n\|,
$$
其中 (3.2) 是安全的整数指数。最后 (3.6) 在 $k=0$ 时仍覆盖 $r\le D$，证明 (3.3)。

### 3.3. 小先前行及小高阶项的扰动版本

若 $i<j$ 只满足 $\|a_i\|\le\sigma$，则先将它们从符号中删掉。若 $\max_i\|h_i\|\le M_g$，每个输出改变至多
$C_{q,L}\sigma M_g$。

同样，若真实符号另外含有固定次数部分 $e_i$，且
$$
\|\mathcal M(e_i)\|_{H_{\le q}\to H}\le\zeta,
$$
其每个输出贡献至多 $C_L\zeta M_g$。因此
$$
\boxed{
\left(\sum_{r=0}^D\|h_r\|_2^2\right)^{1/2}
\le C M^Kt^{-K}
\left[
\max_n\|Z_n^{\rm true}\|
+C_{q,L}M_g(\sigma+\zeta)
\right].
}
\tag{3.7}
$$
若第 $j$ 行本身与一个满足创建下界的符号相差 $\zeta$，同样把差额加进方括号即可。这一版本将明确处理条件化新增的二次项所造成的线性污染。

## 4. 固定有限标量卷积的初等下界

最后收尾需要有限代数的定量事实。以下递推由 l2_moments 提供，免去 Nullstellensatz 证书，也保留对后续系数抵消的完整控制。

**引理 4.1。** 固定非负整数 $d,e$。设复系数 $a_i,b_i$ 对 $0\le i\le d+e$ 满足模不超过 $1$，且
$$
\max_{i\le d}|a_i|\ge\delta,\qquad
\max_{j\le e}|b_j|\ge\delta,\qquad0<\delta\le1.
$$
令
$$
\epsilon=\max_{0\le n\le d+e}
\left|\sum_{i=0}^n a_i b_{n-i}\right|.
$$
则存在只依赖 $d,e$ 的显式正数 $c_{d,e}\le1$ 和整数 $K_{d,e}\ge1$，使
$$
\boxed{\epsilon\ge c_{d,e}\delta^{K_{d,e}}.}
\tag{4.1}
$$
可递推取
$$
c_{0,e}=2^{-e},\quad K_{0,e}=e+2,
$$
$$
K_{d,e}=1+(e+1)K_{d-1,e},\qquad
c_{d,e}=2^{-e}(c_{d-1,e}/4)^{e+1}\quad(d\ge1).
\tag{4.2}
$$

**证明。** 先记一个直接的三角估计。若 $|a_0|\ge\tau>0$，由低卷积系数逐项解 $b_j$，得
$$
|b_j|\le \epsilon |a_0|^{-1}(1+|a_0|^{-1})^j
\le\epsilon\,2^j\tau^{-j-1}
\quad(0\le j\le e),
\tag{4.3}
$$
其中 $\tau\le1$。因此某个 $|b_j|\ge\delta$ 蕴含
$$
\epsilon\ge2^{-e}\delta\,\tau^{e+1}.
\tag{4.4}
$$
当 $d=0$，可取 $\tau=\delta$，得到 (4.2) 的基步。

现对 $d$ 归纳。令
$$
\tau=(c_{d-1,e}/4)\delta^{K_{d-1,e}}\le\delta/4.
$$
若 $|a_0|\ge\tau$，式 (4.4) 直接给 (4.1)–(4.2)。

若 $|a_0|<\tau$，则 $a_1,\ldots,a_d$ 中仍有模至少为 $\delta$ 的系数。令 $a_i'=a_{i+1}$。移位卷积满足
$$
\sum_{i=0}^n a_i'b_{n-i}
=\sum_{i=0}^{n+1}a_i b_{n+1-i}-a_0b_{n+1},
\quad0\le n\le d+e-1,
$$
故其最大模至多 $\epsilon+\tau$。归纳假设给
$$
\epsilon+\tau
\ge c_{d-1,e}\delta^{K_{d-1,e}}=4\tau,
$$
所以 $\epsilon\ge3\tau$。由于
$2^{-e}\delta\tau^{e+1}\le\tau$，这也蕴含与前一分支相同的下界 (4.4)。归纳完成。

注意系数 $a_i$ 在 $d$ 之后、$b_j$ 在 $e$ 之后仍允许存在，并进入所需低卷积；移位递推没有删除它们。

**一般尺度推论。** 若系数模不超过 $M\ge1$，而两个初段最大值分别至少为固定 $\gamma_f,\gamma_g>0$，归一化两端除以 $M$，取
$$
\delta=\min(1,\gamma_f,\gamma_g)/M
$$
，就有
$$
\boxed{
\max_{n\le d+e}|H_n|
\ge c\,M^{2-K_{d,e}}.
}
\tag{4.5}
$$
这至少是 $M$ 的固定负幂。尤其当 $\log M=O(m)$ 时，下界为 $\exp[-O(m)]$，足以与后面的超快误差矛盾。

## 5. 二次核先削小，及后续条件化的精确变化

由 R98 的证明，对任意固定
$$
0<\alpha\le a_{2,q},
$$
全部充分大的 $m$ 都存在 $B_*\subseteq[m,\infty)$，使
$$
|B_*|
\le\frac{2\alpha}{\rho_2}16^m+O_{f,q}(1),\qquad
\|u_m^{\setminus B_*}\|_2\le\delta_*:=e^{-\alpha16^m},
\tag{5.1}
$$
其中
$$
\rho_2=\rho_{2,q}=\frac1{4q^2}.
\tag{5.2}
$$
R98 主定理使用一个具体 $a_{2,q}$；其 §6 的预算对任意更小正数仍成立，而且保留上述按 $\alpha$ 缩小的删点预算。

以后所有条件化都在剩余高尾继续添加顶点。二次核只会继续删去系数，所以始终有 $\|u\|\le\delta_*$。

若在当前符号 (2.9) 上新增有限集 $D$，则：

- $u$ 变为 $u^{\setminus D}$；
- 对每个正头行 $i>0$，线性系数 $a_i$ 恰变为 $a_i^{\setminus D}$；
- 第零头行线性系数变为
  $$
  a_0^{\rm new}
  =a_0^{\setminus D}
   +\sum_{k\notin D}
      \left(\sum_{j\in D}u_{\{j,k\}}\right)\chi_k.
  \tag{5.3}
  $$

对新增项使用 Cauchy–Schwarz，
$$
\left\|
a_0^{\rm new}-a_0^{\setminus D}
\right\|_2
\le\sqrt{|D|}\,\|u\|_2
\le\sqrt{|D|}\,\delta_*.
\tag{5.4}
$$
对于从 $B_*$ 以后所有新增位的并，同样一次使用 (5.3) 即得 $\sqrt{s}\delta_*$，无需把每一步的平方根损失累加。含两个新增位的二次项只改变常数，不再产生线性项。

这也是先消公共顶二次核再处理线性头行的目的：所有正头行只有坐标删除；唯一可能重新污染早期线性行的项有明确超小范数。

## 6. 有限阈值层级与总异常位预算

固定第 3 节的安全指数
$$
K=(q+1)(L+3),
\qquad
\rho_1=\rho_{1,q}=\frac1{4q}.
\tag{6.1}
$$
取 $\alpha>0$ 足够小，使
$$
\alpha\le a_{2,q},\qquad
\alpha\left[
\left(\frac2{\rho_2}+\frac1{2K\rho_1}\right)\log2+K
\right]<1.
\tag{6.2}
$$
这样的正数显然存在。令
$$
\alpha_j=\frac{\alpha}{4(K+1)^{j+1}},
\qquad
\delta_j=e^{-\alpha_j16^m},
\qquad0\le j\le R.
\tag{6.3}
$$
于是
$$
\alpha_{j-1}=(K+1)\alpha_j\quad(j\ge1),\qquad
K\alpha_j<\alpha/4.
\tag{6.4}
$$

从 $B_*$ 开始，依次处理 $j=0,1,\ldots,R$。在第 $j$ 步，对当前一次系数 $a_j$ 使用 R96 的剥离引理，影响阈值为 $\rho_1$，目标范数为 $\delta_j$。得到新增位集 $D_j$，使候选删点向量
$$
\widetilde a_j=a_j^{\setminus D_j}
$$
满足以下二择一：

- $\|\widetilde a_j\|\le\delta_j$；
- $\|\widetilde a_j\|>\delta_j$ 且
  $$
  \sup_k I_k(\widetilde a_j)
  \le\rho_1\|\widetilde a_j\|^2.
  \tag{6.5}
  $$

候选向量是剥离前系数的直接删点向量。对 $j=0$，真实条件化可能另添 (5.4) 的小项；不将候选向量与真实向量未经证明地等同。

R96 的预算与 (2.7) 给
$$
|D_j|
\le\frac2{\rho_1}
\left(\log\max(1,\|a_j\|)+\alpha_j16^m\right)+1.
\tag{6.6}
$$
有限归纳表明所有中间总位数都是 $O(16^m)$，于是 $\log\max(1,\|a_j\|)=O(m)$。因此最终及所有中间的总位数满足
$$
\begin{aligned}
s
&\le
\left(\frac{2\alpha}{\rho_2}
+\frac2{\rho_1}\sum_{j=0}^R\alpha_j\right)16^m+O(m)\\
&\le
\alpha\left(\frac2{\rho_2}+\frac1{2K\rho_1}\right)16^m+O(m).
\end{aligned}
\tag{6.7}
$$
这里用了
$\sum_{j\ge0}\alpha/[4(K+1)^{j+1}]=\alpha/(4K)$。
这是一切 $2^s$ 实际条件化损失的完整预算。

## 7. 每个线性行的大低影响分支都不可能

假设第 $j$ 步出现 (6.5)。R97 给候选创建在每个输入次数 $k\le q$ 上的下界
$$
\|C_{\widetilde a_j}v\|
\ge\frac{\delta_j}{\sqrt2}\|v\|.
\tag{7.1}
$$
将真实符号的第 $j$ 行替成候选行。若 $j=0$，差额范数至多 $\sqrt{s}\delta_*$；若 $j>0$，两者相同。

以前已经落入小分支的正头行，在继续条件化后只会缩小。第零行的额外变化由 (5.4) 一次控制。因此对 $j\ge1$，全部以前头行的线性范数至多
$$
\delta_{j-1}+\sqrt{s}\delta_*.
\tag{7.2}
$$
对 $j=0$ 没有以前头行。真实二次符号仍只有第零行且范数至多 $\delta_*$。

应用引理 3.1 的扰动版本，取 $D=D_g$。因为
$$
L=D_g+(q+1)R\ge D_g+(q+1)j,
$$
窗口足够。式 (2.12) 的非零 $g$ 锚和 (3.7) 给
$$
\gamma_g
\le
P_m\,\delta_j^{-K}
\left[
\varepsilon_{m,s}
+\mathbf1_{\{j\ge1\}}\delta_{j-1}
+\sqrt{s+1}\,\delta_*
\right],
\tag{7.3}
$$
其中 $\log P_m=O(m)$；它包括有限窗口系数、输入列和有限三角递推的全部多项式范数损失。

逐项检查右侧：

1. 由 (2.4)、(6.7)、(6.2)，实际误差乘 $\delta_j^{-K}$ 后的 $16^m$ 指数上界小于
   $$
   -\frac{260}{3}
   +\alpha\left[
      \left(\frac2{\rho_2}+\frac1{2K\rho_1}\right)\log2+K
     \right]
   <-\frac{257}{3}.
   \tag{7.4}
   $$
2. 当 $j\ge1$，先前行误差满足
   $$
   \delta_j^{-K}\delta_{j-1}
   =e^{-(\alpha_{j-1}-K\alpha_j)16^m}
   =e^{-\alpha_j16^m}\longrightarrow0.
   \tag{7.5}
   $$
3. 二次污染满足
   $$
   \delta_j^{-K}\delta_*
   =e^{-(\alpha-K\alpha_j)16^m}
   \le e^{-3\alpha16^m/4}\longrightarrow0.
   \tag{7.6}
   $$

$\sqrt{s+1}$ 和 $P_m$ 的对数都只有 $O(m)$，不能改变这些严格负号。因此 (7.3) 的右侧趋零，与固定 $\gamma_g>0$ 矛盾。

对有限多个 $j$ 依次应用此论证，得到：对全部充分大的 $m$，每一行都只能落在小分支。最终异常位集 $B$ 满足 (6.7)，且
$$
\|u\|\le\delta_*,
\qquad
\|a_i\|\le2\delta_R
\quad(0\le i\le R),
\tag{7.7}
$$
其中第零行的 $\sqrt{s}\delta_*$ 已被 $\delta_R$ 吸收。

本论证明确保留了 $i>R$ 的头系数：在应用固定窗口引理时，它们进入窗口内的后行交叉项，并由 $M_{m,s}$ 控制。只在最后使用输出 $r\le R$ 时，它们因三角指标而确实不再出现。

## 8. 只剩标量卷积，得到最终矛盾

对最终条件化集 $B$，令
$$
b_j=\ell(g_j).
$$
对 (2.3) 的前 $R+1$ 个输出取常数尾系数。利用 (2.9)、(1.2)、(7.7)，得到
$$
H_r:=\sum_{i=0}^r d_i b_{r-i},
\qquad
|H_r|
\le\varepsilon_{m,s}
+C_{q,L}M_{m,s}(\delta_R+\delta_*),
\quad0\le r\le R.
\tag{8.1}
$$
由于 $\alpha_R>0$ 固定，右侧对全部充分大的 $m$ 至多
$$
\exp[-\tfrac12\alpha_R16^m].
\tag{8.2}
$$
另一方面，(2.12) 给标量两端初段的固定非零锚；全部 $d_i,b_j$ 由 $M_{m,s}$ 控制。引理 4.1 取 $d=D_f,e=D_g$，因此给
$$
\max_{r\le R}|H_r|
\ge cM_{m,s}^{\,2-K_{D_f,D_g}}
=\exp[-O(m)].
\tag{8.3}
$$
这与 (8.2) 矛盾。全部实际矩为零的假设被排除，主定理得证。

## 9. 结论范围与方法中的必要区分

本稿完成的是最高次数为二的任意无限秩第一端，与任意有限 Walsh 次数第二端之间的实际矩分离。它不要求系数 $\ell^1$、有界函数、连续代表或有限支撑；所有剩余尾系数都只要求 $\ell^2$。

证明中真正新增的衔接为：

- 固定头窗口的创建左逆必须同时按头位置和尾次数递推，每降一尾阶都会再损失 $j$ 个头位置；
- 前头行的下阶项始终保留，并由有限阈值层级支付；
- 共同二次核通过有限单位变换只留在第零行，后续条件化造成的线性污染由 $\sqrt{s}\delta_*$ 精确控制；
- 最后使用有限标量递推处理卷积的全部高系数抵消，没有假设这些抵消不存在。

任意有限次数第一端的推广需要同时安排多层高阶核、多个头窗口与条件化污染；本稿没有仅凭二阶证明将该推广登记为已证。任意 $L^2$ 消失端点和完整 Hilbert 不变子空间问题仍未由此解决。
