# R271 附录：保全部强位的低孔幂界与原连续尾的完整局部伴随读数

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文将[真实低孔借位幂界](R271-appendix-low-physical-hole-borrow-powers-and-complete-gram-compression.md)送入原强位并头，而不删除强位。新的四次幂预算对并入的位数一致。随后在原非等权连续尾上构造同一低孔输入的真实有限 Neumann 右逆，获得完整伴随方程的低孔输出读数；没有预先压缩完整逆或核投影。

准确范围：强头为 $C=A_m+D_<$，远尾为 $D_x$，完整算子是
$\mathcal L_m=C+D_x=A_m+D_{\ge m}$。本文的伴随读数属于这个完整物理算子，不是有限强头 $C^*$ 的 Green 界，也不是原高出生裸商的读数。原全局 $T$ 与 $\mathcal L_m$ 的 carry 差没有被省去。本文不证明原 $N=M$。

已付依赖：
- 前述低孔借位稿的 $\gamma=770/256$；
- [R234 原纯尾右逆](R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) §3 的全孔层右逆；
- [完整等权池 Green 列](R271-appendix-uniform-pool-exact-green-column-and-true-head-power-budget.md)；
- [强位并头与实际源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。

R234 已经证明固定孔层属于原全局 $T$ 的值域。本文不重复登记该存在性；新增的是保原任意 $m,R$ 分拆的低孔定量预算和下述明确构造。

## 1. 同一原强头与实际孔投影

固定 $m\ge1$、$R\ge0$，令
$$
d=2^m,\qquad x=m+R,\qquad h=d+R,
$$
$$
C=A_m+D_<,\qquad
D_<=\sum_{i=m}^{x-1}(i+1)^{-2}E_i,\qquad
D_x=\sum_{i\ge x}(i+1)^{-2}E_i.
\tag{1.1}
$$
$A_m$ 是原 N 或 Y 的完整 $m$ 位头，原内积保持不变。所有 $E_i$ 是独立物理 Boolean 删除。记
$$
\nu_<:=\|D_<\|\le\sum_{i=m}^{x-1}(i+1)^{-2}\le\frac1m.
$$
由于 $A_m^d=0$、$D_<^{R+1}=0$ 且二者交换，
$$
C^h=0.
\tag{1.2}
$$
强头的物理空间是前 $x$ 位。记 $P_{\le s}^{\rm str}$ 为其中总孔数不超过 $s$ 的正交投影；它同时计算原 $m$ 位和新增 $R$ 位，不是只计算旧头。

展开同一真实幂：
$$
C^kP_{\le s}^{\rm str}
=\sum_{r=0}^{\min(k,s)}
\binom kr A_m^{k-r}D_<^rP_{\le s}^{\rm str}.
\tag{1.3}
$$
$r>s$ 的项为零。对其余项，$D_<^r$ 非零的输入强位孔数至少为 $r$，故该输入的旧头孔数不超过 $s-r$。$D_<^r$ 不作用旧头，所以在同一项中可准确使用旧头的低输入界：
$$
\begin{aligned}
\|A_m^{k-r}D_<^rP_{\le s}^{\rm str}\|
&\le
6^{k-r}
e^{-\gamma((k-r)-(s-r))_+^4}\nu_<^r\\
&=
6^{k-r}e^{-\gamma(k-s)_+^4}\nu_<^r.
\end{aligned}
\tag{1.4}
$$
这是同一输入的头/强位孔分拆，不是假设 $A_m$ 保孔。

对 (1.3) 求和得到
$$
\boxed{
\|C^kP_{\le s}^{\rm str}\|
\le(6+\nu_<)^k e^{-\gamma(k-s)_+^4}
\le7^k e^{-\gamma(k-s)_+^4},
\qquad
\gamma=\frac{770}{256}.
}
\tag{1.5}
$$
常数与 $m,R,h$ 无关。特别，早强位全部保留后，阈值仍是输入总孔数 $s$，而非 $m+R$ 或 $h$。

## 2. 完整强头 Gram 与等权池的直接推论

对任意 $\sigma>0$，使用该强头的真正 bosonic Gram
$$
H_C(\sigma)=\sum_{j<h}\frac{(C^j)^*C^j}{\sigma^j j!}.
$$
定义
$$
D_s^{(7)}(\sigma)
=\sum_{j\ge0}\frac{(49/\sigma)^j e^{-2\gamma(j-s)_+^4}}{j!}.
$$
与低孔借位稿同样的实变量优化给
$$
D_s^{(7)}(\sigma)
\le
\exp[1+s\tau+\tau^{4/3}],
\qquad
\tau=\max\{0,\log(49/\sigma)\}.
\tag{2.1}
$$
因此
$$
P_{\le s}^{\rm str}H_C(\sigma)P_{\le s}^{\rm str}
\preceq D_s^{(7)}(\sigma)P_{\le s}^{\rm str},
$$
$$
\boxed{
P_{\le s}^{\rm str}H_C(\sigma)^{-1}P_{\le s}^{\rm str}
\succeq D_s^{(7)}(\sigma)^{-1}P_{\le s}^{\rm str}.
}
\tag{2.2}
$$
第二式先取完整逆，再取压缩，使用完整 nuisance Schur。它不说明 $H_C^{-1}$ 保孔。

若另有一个真实等权池，长度 $L\ge2h$、每位权 $t$、平方强度 $\sigma=Lt^2$，则已有完整 Green 公式可应用于此处的 $C$。记该池真实分母为
$$
p_j=\prod_{\ell=1}^j t\sqrt{\ell(L-\ell+1)},
\qquad
H_{\rm pool,C}
=\sum_{j<h}\frac{(C^*)^jC^j}{p_j^2}.
$$
对任意完整强头 forcing $f$，同一最小者满足
$$
\boxed{
\begin{aligned}
&\|(P_{\le s}^{\rm str}\otimes I)
(C+D_{\rm pool})^{*\dagger}(f\otimes\Omega)\|^2\\
&\quad\le
\frac4{\sigma}
\exp[1+s\tau_4+\tau_4^{4/3}]
\langle H_{\rm pool,C}^{-1}f,f\rangle,
\qquad
\tau_4=\max\{0,\log(196/\sigma)\}.
\end{aligned}
}
\tag{2.3}
$$
其证明在真实 Green 卷积中仅使用
$\|P_{\le s}^{\rm str}(C^*)^\ell\|=\|C^\ell P_{\le s}^{\rm str}\|$。
完整 $H_{\rm pool,C}^{-1}$、真实 $h$ 和所有强位均保留；没有把它们换回旧 $A_m$ 的对象。

下面不假设存在这样的等权池，直接回到 (1.1) 的原连续远尾。

## 3. 原连续尾的逐层真右逆

记
$$
S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}.
\tag{3.1}
$$
在远尾恰好 $j$ 孔层上，原 CCR 是
$$
D_xD_x^*-D_x^*D_x
=S_xI-2\sum_{i\ge x}(i+1)^{-4}n_i.
$$
因此
$$
D_xD_x^*|_{\mathcal H_j^>}
\succeq
\left(S_x-2j(x+1)^{-4}\right)I.
$$
令
$$
J_x=\left\lfloor\frac{x+1}{12}\right\rfloor.
$$
对 $0\le j\le J_x$，由 (3.1) 得
$$
D_xD_x^*|_{\mathcal H_j^>}\succeq\frac{S_x}{2}I.
$$
所以这个完整孔层上的真正 MP 右逆存在：
$$
Q_{x,j}=D_x^*(D_xD_x^*|_{\mathcal H_j^>})^{-1},
\qquad
D_xQ_{x,j}=I,\qquad
\|Q_{x,j}\|\le\sqrt{\frac2{S_x}}.
\tag{3.2}
$$
其输出孔数恰增加一；位置可以无限。

对 $j>J_x$，采用 R234 §3 已构造的原有全孔层右逆，保持
$$
D_xQ_{x,j}=I,\qquad
\|Q_{x,j}\|
\le[10000(x+j+1)^2]^{j+1}.
\tag{3.3}
$$
(3.3) 也可作为低层选择 (3.2) 的粗上界，因为
$\sqrt{2/S_x}\le\sqrt6(x+1)^{3/2}<10000(x+1)^2$。
所以这同一个混合族同时满足全部高层粗界和低层锐界。

将 $Q_{x,j}$ 按实际远孔次数拼接成 $\mathcal Q_x$。它只作用远尾，故与 $C$ 交换。本文不声称 $\mathcal Q_x$ 在所有孔层的直和上有统一范数；在每个有限次数范围上，其所需组合均有界。

## 4. 保全部强位的有限 Neumann 列及显式一致成本

令 $P_{\le s}^{\rm tot}$ 计算前 $x$ 位加远尾的全部物理孔。对这个完整低孔输入空间定义
$$
\mathcal G_{m,R,s}
=
\left.\sum_{k=0}^{h-1}(-C)^k\mathcal Q_x^{\,k+1}
\right|_{P_{\le s}^{\rm tot}\mathcal H}.
\tag{4.1}
$$
这是有限和。每一项只读取远孔层 $0,\ldots,s+h$，因此是实际有界映射，不是形式解。

由 $D_x\mathcal Q_x^{k+1}=\mathcal Q_x^k$、头尾交换和 $C^h=0$，逐项消去准确给
$$
\boxed{
\mathcal L_m\mathcal G_{m,R,s}
=I|_{P_{\le s}^{\rm tot}\mathcal H},
\qquad
\mathcal L_m=C+D_x=A_m+D_{\ge m}.
}
\tag{4.2}
$$
虽然 $\mathcal L_m$ 本身不依赖 $R$，构造的分界、有限和和远尾右逆依赖 $R$。本文没有把其中一个源改变为另一个切口的源。

下面假设
$$
x=m+R\ge3072+48s.
\tag{4.3}
$$
置
$$
\tau_x=\log\!\left(7\sqrt{\frac2{S_x}}\right)>0,
$$
$$
\boxed{
\mathcal B_s(x)
=(s+3)\sqrt{\frac2{S_x}}\,
\exp[s\tau_x+\tau_x^{4/3}].
}
\tag{4.4}
$$
则
$$
\boxed{\|\mathcal G_{m,R,s}\|\le\mathcal B_s(x).}
\tag{4.5}
$$

先说明同一输入上的算子顺序。固定输入远孔层 $p\le s$ 时，旧强头孔数不超过 $s-p$，所有 $\mathcal Q_x$ 保持该头坐标。因此 (1.5) 可直接用于 $C^k$ 的这个输入。对固定 $k$，不同 $p$ 被送到不同远孔层 $p+k+1$；故按 $p$ 直和只取最大值，没有额外 $\sqrt{s+1}$。于是第 $k$ 项范数至多
$$
7^ke^{-\gamma(k-s)_+^4}
\max_{0\le p\le s}\prod_{\nu=0}^k\|Q_{x,p+\nu}\|.
\tag{4.6}
$$

### 4.1 低幂段

若 $k\le J_x-s$，所有 $p+\nu\le J_x$，(3.2) 给
$$
\max_p\prod_{\nu=0}^k\|Q_{x,p+\nu}\|
\le(2/S_x)^{(k+1)/2}.
$$
这些项的和因此不超过
$$
\sqrt{\frac2{S_x}}
\sum_{k\ge0}
\exp[\tau_x k-\gamma(k-s)_+^4].
$$
把四次项分成相等两半。实变量优化给
$$
\sup_{y\ge0}(\tau_xy-(\gamma/2)y^4)
=\frac3{4^{4/3}(\gamma/2)^{1/3}}\tau_x^{4/3}
\le\tau_x^{4/3}.
$$
又 $\gamma/2>\log2$，所以
$\sum_{\ell\ge1}e^{-(\gamma/2)\ell^4}<1$。低幂段总和至多
$$
(s+2)\sqrt{\frac2{S_x}}\,
e^{s\tau_x+\tau_x^{4/3}}.
\tag{4.7}
$$

### 4.2 高幂段

若 $k>J_x-s$，则 (4.3) 给
$$
k\ge\frac{x+1}{12}-s\ge\frac x{24},
\qquad k\ge128,\qquad k\ge2s.
\tag{4.8}
$$
对全部层使用同一个粗界 (3.3)，
$$
\max_p\prod_{\nu=0}^k\|Q_{x,p+\nu}\|
\le[10000(x+s+k+1)^2]^{(k+1)(s+k+1)}.
$$
由 (4.8)，
$$
x+s+k+1\le28k,\qquad
(k+1)(s+k+1)\le2k^2,
$$
所以第 $k$ 项的对数范数至多
$$
-\frac{\gamma}{16}k^4
+k\log7+2k^2(16+2\log k).
$$
对 $k\ge128$，$\log k\le k/8$，从而
$$
k\log7+2k^2(16+2\log k)\le k^3
\le\frac{\gamma}{32}k^4.
$$
高幂项遂被 $e^{-\gamma k^4/32}$ 支配，其总和小于 $1$。结合 (4.7)，并用
$\sqrt{2/S_x}e^{s\tau_x+\tau_x^{4/3}}\ge1$，得到 (4.4)--(4.5)。

此估计在求和前没有把 $k<h$ 粗替成 $h$。因此 $h$ 即使远大于固定输入孔数，常数仍只依赖 $s$ 和真实远尾起点 $x$。对固定 $s$，
$$
\log\mathcal B_s(x)
=O_s((\log(x+1))^{4/3}).
\tag{4.9}
$$

## 5. 原完整伴随方程及 MP 输出的低孔读数

由 (4.2)，对每个实际 Hilbert 向量 $y$ 和每个
$f\in P_{\le s}^{\rm tot}\mathcal H$，
$$
\langle y,f\rangle
=\langle y,\mathcal L_m\mathcal G_{m,R,s}f\rangle
=\langle\mathcal L_m^*y,\mathcal G_{m,R,s}f\rangle.
$$
因此
$$
\boxed{
\|P_{\le s}^{\rm tot}y\|
\le\mathcal B_s(x)\|\mathcal L_m^*y\|
\qquad(y\in\mathcal H).
}
\tag{5.1}
$$
这是原连续非等权尾上的完整方程，不需要预设 $y$ 的孔支持。

特别，对完整伴随 Moore--Penrose 逆的自然域
$$
f\in\operatorname{Ran}\mathcal L_m^*
\oplus\ker\mathcal L_m
=\operatorname{Dom}(\mathcal L_m^*)^\dagger,
$$
取 $y=(\mathcal L_m^*)^\dagger f$，有
$\|\mathcal L_m^*y\|\le\|f\|$，故
$$
\boxed{
\|P_{\le s}^{\rm tot}(\mathcal L_m^*)^\dagger f\|
\le\mathcal B_s(x)\|f\|.
}
\tag{5.2}
$$
(5.2) 给这个低输出压缩的有界延拓；没有说完整
$(\mathcal L_m^*)^\dagger$ 有界。等价地，低输入
$\mathcal L_m^\dagger P_{\le s}^{\rm tot}$ 可由
$(I-P_{\ker\mathcal L_m})\mathcal G_{m,R,s}$ 实现，且范数满足同一界。这里保留整个物理核投影，未以某个低源 Gram 的逆替代它。

## 6. 与原测试及未付运输的区别

(2.3) 是等权池模型的低强头输出，(5.1)--(5.2) 是原连续尾完整
$\mathcal L_m$ 的低总孔输出。二者的对象和度量不同，本文没有将它们混同。

若要用于原固定物理测试配对，仍须证明实际被读取的向量确为这些低孔输出，或者支付将测试送到这里的逆伴随和完整投影。相对孔 Riordan 算子在环境中只作用远孔，因而与强头孔投影交换；但原返回测试还含真实
$P_{\widehat{\mathscr E}}$，其头核旗和零源 Schur 一般不保物理孔。仅由环境交换不能把该投影删除。

同样，原强孔 Artin 相似的完整物理 Gram、原全局 $T-\mathcal L_m$ 的 carry 差、以及同一个 $W$ 来源均须保持。尤其 (5.2) 不给有限强头 $C^{*\dagger}$ 的真空 forcing 列，也不等价于所需的 $O_a(R^3)$ 整列费用。

本稿实际新增的可用预算是：全部原强位保留时的 (1.5)，以及原连续尾上不付环境幂零维数的 (4.5)、(5.1)--(5.2)。原完整返回主配对、普通右封口和 $N=M$ 仍需后续同源控制。
