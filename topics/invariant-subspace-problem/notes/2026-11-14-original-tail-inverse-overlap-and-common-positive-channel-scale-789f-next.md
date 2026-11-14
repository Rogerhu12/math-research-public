# 原连续尾的一致倒数交差界与出生二正通道的真实尺度

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：第 1—4 节的概率界与同源二次型界已证明。** 它们不使用源的总条件数，并对任意平方可积测试函数成立。第 5 节只给出一个明确的后续充分目标，未声称该目标已证明。

依赖：[R295 分拆与初等对称和](../results/R295-birth-one-turan-remainder-law-and-all-height-strengthened-s1.md)、[首低通道共同 Schur](2026-11-14-first-low-johnson-channel-common-schur-and-original-tail-linear-budget-789f-next.md)。本文只研究原连续无限行 $z_j=j^{-4}$，不推广为任意正权行的相同估计。

## 1. 结论及其量词

固定 $x\ge2$、$k\ge1$，令
$$
\mu_k(J)=z_J/e_k(z),\qquad |J|=k,\qquad z_j=j^{-4}\ (j\ge x).
$$
对任意确定的 $k$ 元集 $I$，置
$$
R_I(J)=|J\setminus I|=\frac12|I\mathbin\triangle J|.
$$
下面的界对全部 $I$ 一致：
$$
\boxed{\mathbb E_{J\sim\mu_k}\frac1{R_I(J)+1}
\le\frac{20}{k+2},\qquad
\mathbb E_{J\sim\mu_k}\frac1{(R_I(J)+1)^2}
\le\frac{400}{(k+2)^2}.}
\tag{1.1}
$$
因此
$$
\boxed{\mathbb E\left[\frac1{R_I};R_I\ge1\right]\le\frac{40}{k+2},\qquad
\mathbb E\left[\frac1{R_I^2};R_I\ge1\right]\le\frac{1600}{(k+2)^2}.}
\tag{1.2}
$$
不对 $I$ 本身取平均，所以后面可把 $I$ 乘以同一个实际源的任意平方权。它不同于仅说明无权事件 $R_I$ 通常较大。

## 2. 两组固定大小乘积采样的基本随机序

设一行分为内、外两组，权全正；抽取总数 $t$，外组所取数为 $R_t$。若两组初等和为 $a_j,b_j$，则
$$
\mathbb P(R_t=r)\propto a_{t-r}b_r.
\tag{2.1}
$$
初等对称和的 log 凹性给 $a_{j+1}/a_j$ 随 $j$ 递减。因此
$\mathbb P(R_{t+1}=r)/\mathbb P(R_t=r)$ 在共同支撑上随 $r$ 递增；支撑端点也向同一方向移动。这给
$$
R_t\preceq_{\rm st}R_{t+1}.
\tag{2.2}
$$
例如在共同正支撑上，可把新分布写为旧分布乘一个递增函数，再用两个递增函数的非负协方差证明；零端点由极限或交叉乘法处理。交换内、外两组，同样得到内组数 $t-R_t$ 随 $t$ 随机递增。因此还准确有
$$
R_{t+1}\preceq_{\rm st}R_t+1.
\tag{2.3}
$$
这里只用了初等和 log 凹性；其正分拆证明已包含在 R295 中。

改变某一个坐标的权时，条件于该坐标未选／已选，其余坐标分别抽 $t$／$t-1$ 个，而混合概率随该权递增。若该坐标在外组，两种外部计数是 $R_t$ 与 $1+R_{t-1}$，由 (2.3) 后者随机更大；若在内组，两种外部计数是 $R_t$ 与 $R_{t-1}$，由 (2.2) 后者随机更小。故：

- 增大外组任意权使外部计数随机增大；
- 增大内组任意权使外部计数随机减小；
- 删除外组坐标可由其权降到零取得，使外部计数随机减小，只要剩余模型仍可抽取 $t$ 个。

以上事实先用于有限行。正 $\ell^1$ 平方权的固定大小采样可由初等和正级数极限得到相同结论。

## 3. 原尾与一个明确有限计数模型的比较

### 3.1 最坏的内集是最大的前 $k$ 个权

令
$$
I_0=\{x,x+1,\ldots,x+k-1\}.
$$
若某个内位比一个外位的权小，交换它们的内／外标签会使外部计数随机减小。证明可条件于其余坐标及这两个坐标被选的总数：总数为零或二时不变；总数为一时，较大权被选的概率较大，把它放到内组正好降低外部计数。有限次交换给
$$
R_{I_0}\preceq_{\rm st}R_I\quad\text{对任意 }|I|=k.
\tag{3.1}
$$

### 3.2 冻结前半段并保留一段外部权

置
$$
h=\lfloor k/2\rfloor,\qquad l=\lceil k/2\rceil,
\qquad k=h+l.
$$
条件于前 $h$ 个坐标的任意选取图样。若其中选了 $a\le h$ 个，剩余样本数是 $t=k-a\ge l$。剩余内组恰有 $l$ 个坐标
$x+h,\ldots,x+k-1$；保留紧接其后的 $l$ 个外部坐标
$x+k,\ldots,x+k+l-1$。

令 $A=(x+h)^{-4}$。剩余内组每个权至多 $A$，保留的外组每个权至少 $A/81$，因为
$$
x+k+l-1=x+h+2l-1\le3(x+h),
$$
其中 $l\le h+1$、$x\ge2$。先删除其他外部坐标，再把内权增大到 $A$、外权减小到 $A/81$，均使外部计数随机减小。剩下 $2l$ 个坐标，而 $l\le t\le k\le2l$，所以模型始终合法。最后把样本数从 $t$ 降到 $l$，按 (2.2) 再次随机减小外部计数。

共同缩放权后，得到同一个比较随机变量 $R_*$：从 $l$ 个内权 $1$ 和 $l$ 个外权 $1/81$ 中抽取 $l$ 个时的外部计数。它不依赖先前条件图样。因此
$$
\boxed{R_*\preceq_{\rm st}R_{I_0}\preceq_{\rm st}R_I.}
\tag{3.2}
$$

### 3.3 两个倒数矩由同一个平方直接控制

$R_*$ 的未归一质量为
$$
t_r=\binom lr^2\,81^{-r},\qquad0\le r\le l,
\qquad
\frac{t_{r+1}}{t_r}=\frac{(l-r)^2}{81(r+1)^2}.
$$
逐项求和即得
$$
\mathbb E\left[\left(\frac{l+1}{R_*+1}-1\right)^2\right]
=81\bigl(1-\mathbb P(R_*=0)\bigr)\le81.
\tag{3.3}
$$
由 $L^2$ 三角不等式，
$$
\left\|\frac{l+1}{R_*+1}\right\|_{L^2}\le1+9=10.
$$
再用 $L^1\le L^2$、$l+1\ge(k+2)/2$ 和 (3.2) 对递减函数的比较，就得到 (1.1)。最后在 $r\ge1$ 时 $r^{-1}\le2(r+1)^{-1}$，给出 (1.2)。

## 4. 不需要源条件数的共同二次型比较

对任意 $p\in L^2(\mu_k)$，减去其均值不会改变 $p(I)-p(J)$。令 $I,J$ 独立服从 $\mu_k$，并置
$$
\mathscr E_k(p)=\mathbb E\left[
\frac{|p(I)-p(J)|^2}{|I\setminus J|};\ I\ne J\right].
$$
由于 $|I\setminus J|\le k$，
$$
\mathscr E_k(p)\ge\frac2k\operatorname{Var}_{\mu_k}(p).
$$
另一方面用 $|u-v|^2\le2(|u|^2+|v|^2)$、两端对称及对每个固定 $I$ 都成立的 (1.2)，得到
$$
\boxed{\frac2k\operatorname{Var}_{\mu_k}(p)
\le\mathscr E_k(p)
\le\frac{160}{k+2}\operatorname{Var}_{\mu_k}(p).}
\tag{4.1}
$$
特别地，若 $\sum_{|I|=k}z_Ip(I)=0$，未归一形式为
$$
\boxed{\frac{2e_k}{k}\|p\|_k^2
\le\sum_{|I|=|J|=k,\ I\ne J}
z_Iz_J\frac{|p(I)-p(J)|^2}{|I\setminus J|}
\le\frac{160e_k}{k+2}\|p\|_k^2.}
\tag{4.2}
$$
它对全部 $p$ 一致，不能只理解为无源采样的高概率结论。两边可用于同一个算子源的 Gram；没有先对每个源选不同概率空间。

## 5. 出生二真实正通道的尺度及还欠的预算

在首低通道共同 Schur 稿的 $s=2$ 模型中，$p=p^\sharp|_{|I|=k}=\mathcal R_{k,2}f$，$k=n+2$，$\|p\|_k^2=\langle C_nf,f\rangle$。记该稿整个正通道为
$$
\mathcal P(f)=e_{k-1}e_{k+1}\,
\mathbb E_Q\frac{2(r+1)}{r(2r-1)}\|P_Dh_D(y)\|^2.
$$
中央反对称统计 $p(I)-p(J)=\delta^*h_D(y)$ 的条件平方和为
$\binom{2r}{r}\frac{2r}{2r-1}\|P_Dh_D\|^2$。除以 $r$ 并对原权求和，因此准确有
$$
\mathcal P(f)=\sum_{|I|=|J|=k,I\ne J}
z_Iz_J\frac{|p(I)-p(J)|^2}{|I\setminus J|}.
$$
式 (4.2) 遂支付这个实际正通道的完整尺度：
$$
\boxed{\frac{2e_k}{k}\langle C_nf,f\rangle
\le\mathcal P(f)
\le\frac{160e_k}{k+2}\langle C_nf,f\rangle.}
\tag{5.1}
$$

剩余负量仍是同稿中的
$$
\mathcal N(f)=e_{k-1}e_{k+1}\operatorname{Var}_Q u(y),
\qquad \langle\mathcal A_{2,n}f,f\rangle=\mathcal P(f)-\mathcal N(f).
$$
**尚未证明**存在独立于 $n,x,f$ 的有限 $L$ 使
$$
\mathcal N(f)\le Lk\,\mathcal P(f).
\tag{5.2}
$$
若能证明 (5.2)，则 (5.1) 会给真正允许损失的算术比较
$$
e_{k+1}C_{n-1}+e_{k-1}
(C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*)
\preceq(2+160L)e_kC_n.
\tag{5.3}
$$
这一步保留同一个 $f$ 和完整桥。再按已经明确的同源平方完成，足以给加强常数
$\kappa=(2+160L)^2e_k^2/(4e_{k-1}e_{k+1})$；原尾的 scalar Turán 比可用 R295 的 $674/81$ 界。

(5.2) 的因子 $k$ 由已证明的正通道 $1/k$ 尺度吸收，而不是乘到仅知趋零的 graph 锚上。本文没有取得 (5.2)，也不把上述出生二的条件充分关系提升到其他出生或完整 graph。
