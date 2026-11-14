# R254 第八附录：特殊高尾修复的真实头四次预算与 p>4/9 正则饱和

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的实际中间结论。

本稿使用 [R254 第七附录](../results/R254-appendix-restricted-pure-kernel-right-inverse-and-subexponential-stable-range.md) 中同一个真实受限右逆，再对整个含混合项的有限和保留真实头的四次进位衰减。没有把受限右逆用于尚未属于有限阶核的残量。

## 1. 不变的输入、输出和目标

固定 $m\ge2$、$d=2^m$，仍用去掉原第 $0$ 位后的平方符号
$$
P_m=D^2+Q_m.
$$
$A_m$ 为前 $m$ 个尾位的真实慢头，$C_m$ 为该头的归一化快速移位；高尾为
$$
D=\sum_{j\ge m}(j+2)^{-2}E_j,\qquad \|D\|\le1.
$$
两型分别为
$$
Q_m=A_m^2-\eta C_m+2A_mD\quad(N),
\tag{1.1}
$$
$$
Q_m=A_m^2+2A_mD-\eta C_m(I+A_m+D)^2\quad(Y),
\tag{1.2}
$$
其中 $\eta=\eta_0=e^{-1070}$。
$\|A_m\|<2/3$、$\|C_m\|\le1$，且 $Q_m$ 具有严格正头次数。

把 (1.2) 全部展开：
$$
\begin{aligned}
Q_m={}&A_m^2+2A_mD-\eta C_m-2\eta C_mA_m
-\eta C_mA_m^2\\
&-2\eta C_mD-2\eta C_mA_mD-\eta C_mD^2.
\end{aligned}
\tag{1.3}
$$
因此每一项都是
$$
\zeta\, A_m^pC_m^rD^t,\qquad
0\le t\le2,\quad 1\le p+r\le3,
$$
而全部标量系数的绝对和不超过
$$
3+9\eta<4.
\tag{1.4}
$$
$N$ 型也满足同一界。

R254 第七附录给完整纯尾层上的同一个实际 $G_q$，
$DG_q=I$，输出孔数增加一，并在 $\ker D^s\cap\mathcal H_q$ 上满足
$$
\|G_qf\|\le s L_{m,q}^s\|f\|,
\qquad
L_{m,q}=512\sqrt{q+1}(m+q+2)^{3/2}.
\tag{1.5}
$$
令 $H=G^2$，并仍定义
$$
\mathcal G_m
=H\sum_{k=0}^{d-1}(-Q_mH)^k.
\tag{1.6}
$$
它是真实右逆 $P_m\mathcal G_m=I$，并在有限孔输入上最低增加两次、最高增加 $2d$ 次孔。

本稿只估计
$$
r\in\ker D^{2d}\cap\mathcal H_{\le q}.
\tag{1.7}
$$
这些正是第六、七附录中的特殊顶部残量；中间核阶仍按第七附录逐步上升。

## 2. 真实有限头单项式的四次进位衰减

令 $\bar N_j$ 为 $C_m$ 的实际归一化 $2^j$ 次幂，$0\le j<m$。
$\bar N_0=C_m$，$\|\bar N_j\|\le1$，并准确满足
$$
\bar N_j^2=\eta_{j+1}\bar N_{j+1},\qquad
\bar N_m=0,\qquad
\eta_{j+1}\le e^{-770\,16^j}.
\tag{2.1}
$$
最后一个指数有意使用比原物理位更弱的统一界，不改变原算子。

考虑包含 $n=\sum_j k_j$ 个真实 $\bar N$ 因子的单项式。
按二进位归约，令 $c_j$ 为从第 $j$ 位向第 $j+1$ 位的进位次数。
若进位越过第 $m-1$ 位，单项式含 $\bar N_m$，准确为零。
否则输出的二进位数至多有 $m$ 个非零位，逐位守恒给
$$
\sum_jc_j=n-\operatorname{popcount}\!\left(\sum_jk_j2^j\right)
\ge n-m.
\tag{2.2}
$$
令
$$
E=\sum_j16^jc_j.
$$
每条真实进位链满足
$c_{j+\ell}\ge\lfloor c_j/2^\ell\rfloor$。
当 $c_j\ge1$，取 $\ell=\lfloor\log_2c_j\rfloor$。
非零单项式不允许这条链越出有限头，所以
$$
E\ge16^{j+\ell}\ge16^j(c_j/2)^4,
\qquad
c_j\le2E^{1/4}2^{-j}.
$$
对 $j$ 求和，得到
$$
\sum_jc_j\le4E^{1/4}.
$$
当 $n\ge2m$ 时，(2.2) 因而给
$$
E\ge(n/8)^4.
$$
每次进位都保留 (2.1) 的真实标量因子，末端互异 $\bar N$ 的乘积范数不超过 $1$，所以
$$
\boxed{
\left\|\prod_j\bar N_j^{k_j}\right\|
\le e^{-\gamma n^4},
\qquad n\ge2m,\qquad
\gamma=\frac{770}{4096}.
}
\tag{2.3}
$$
这不是只在某个基向量上的估计；先作的是实际算子代数等式。

对于 $Y$ 型，
$$
\bar Y_j=\bar N_j(I+\bar N_j)^{-1},\qquad
\|(I+\bar N_j)^{-1}\|\le3.
$$
该界可直接由
$(I+\bar N_j)^{-1}=(I-\bar N_j)(I-\bar N_j^2)^{-1}$
以及 (2.1) 得到，最后一位平方为零也包括在内。
所有因子均为 $C_m$ 的函数，故逆可全部移到一侧，至多付 $3^P$，其中 $P$ 是慢因子数。

实际慢头为
$$
A_m=\sum_{j<m}(j+2)^{-2}\bar X_j,
\quad \bar X_j=\bar N_j\ \text{或}\ \bar Y_j.
$$
因 $\sum_{j<m}(j+2)^{-2}<2/3$，
对 $n=P+R\ge2m$，展开有限和并使用 (2.3)，有
$$
\boxed{
\|A_m^P C_m^R\|
\le2^n e^{-\gamma n^4}.
}
\tag{2.4}
$$
$N$ 型有更小系数，但本稿统一使用 (2.4)。
对其余 $n$，环境界 $\|A_m^P C_m^R\|\le1$ 即可。

## 3. 每个混合词保留头衰减

展开 (1.6) 中有 $k$ 个 $Q_m$ 的一项。
由于 $H,D$ 只作用纯尾，全部有限头因子都与它们交换。
因此每个词可以准确写成一个头单项式
$A_m^P C_m^R$
乘一个尾词
$$
H D^{t_k}H\cdots D^{t_1}H,\qquad 0\le t_i\le2.
\tag{3.1}
$$
总头因子数满足
$$
k\le P+R\le3k.
\tag{3.2}
$$
这里没有交换 $H$ 与 $D$；只把独立有限头拉到一侧。

尾词的第 $j$ 次 $H$ 仍可用核阶上界
$s_j=2d+2j$。$D^{t_i}$ 不增加核阶，范数又不超过 $1$。
输入次数始终不超过 $q+2j$。置
$$
L_*=512\sqrt{q+2d+1}(m+q+2d+2)^{3/2},
$$
$$
U=2\log(4d)+6d\log L_*.
\tag{3.3}
$$
第七附录的逐步界给，对每个 $k\le d-1$，
$$
\begin{aligned}
\|\text{尾词}|_{\ker D^{2d}\cap\mathcal H_{\le q}}\|
&\le(4d)^{2(k+1)}
 L_*^{(k+1)(4d+2k+1)}\\
&\le e^{(k+1)U}.
\end{aligned}
\tag{3.4}
$$
中间核阶没有被固定为初值 $2d$。

若 $k\ge2m$，(3.2)、(2.4) 使每个头词满足
$$
\|A_m^P C_m^R\|
\le 8^k e^{-\gamma k^4}.
$$
(1.4) 给全部词的标量系数绝对和至多 $4^k$。
因此完整的第 $k$ 项满足
$$
\boxed{
\|H(Q_mH)^k r\|
\le32^k e^{(k+1)U-\gamma k^4}\|r\|,
\qquad k\ge2m.
}
\tag{3.5}
$$
对于 $k<2m$，准确的粗界是
$$
\|H(Q_mH)^k r\|\le4^k e^{(k+1)U}\|r\|.
\tag{3.6}
$$
所有真实 Cayley 逆、混合词数量与尾域成本已经分别列出。

## 4. 完整有限和的优化

令
$$
L=U+\log32.
$$
因 $\gamma>1/100$，对所有 $t\ge0$，
$$
-\gamma t^4+Lt\le3L^{4/3}.
\tag{4.1}
$$
例如把 $t=L^{1/3}x$，$x-x^4/100$ 的最大值为
$(3/4)25^{1/3}<3$。

低 $k<2m$ 的 (3.6) 指数至多 $2mL$；
高 $k$ 的 (3.5) 指数至多 $U+3L^{4/3}$。
有限和至多有 $d$ 项，故
$$
\boxed{
\|\mathcal G_mr\|\le\mathfrak B_{m,q}\|r\|,
\qquad
\log\mathfrak B_{m,q}
=\log d+\max\{2mL,\ U+3L^{4/3}\}.
}
\tag{4.2}
$$
也可以同时保留第七附录旧的 $\mathcal B_{m,q}$，取两个已证上界的较小值。

现在取 $q=25d^3$。已有
$\log L_*<13+6\log d$，从而
$$
L\le128d(1+\log d).
$$
$2mL$ 为 $O(d\log^2d)$，另一项为
$O(d^{4/3}(1+\log d)^{4/3})$。
一个对全部 $m\ge2$ 足够的明确界是
$$
\boxed{
\log\mathfrak B_{m,25d^3}
\le4096\,d^{4/3}(1+\log d)^{4/3}.
}
\tag{4.3}
$$
可这样核验低支路也被吸收：写 $x=\log d$，则
$x^3/[(1+x)e^x]\le x^2e^{-x}<1$；
所以 $d\log d(1+\log d)$ 被
$d^{4/3}(1+\log d)^{4/3}$ 的固定倍数控制。
高支路用 $\sqrt[3]{128}<6$ 即有足够数值余量。

## 5. 真正的正则核饱和：所有 p>4/9

对每个实际 $u\in K$，仍取第七附录中同一
$$
v_m=P_{\le q}\mathsf V_{m,q}u,\qquad
r_m=P_mv_m,\qquad
c_m=\mathcal G_mr_m,\qquad k_m=v_m-c_m,
\quad q=25d^3.
$$
特别
$$
r_m\in\ker D^{2d}\cap(\mathcal H_{q-1}\oplus\mathcal H_q).
$$
因此 (4.2)--(4.3) 的受限界确实适用于它。
全部准确支撑与核归属不变：
$$
c_m\in\ker D^{2d}\cap\mathcal H_{[q+1,q+2d]},
\qquad
k_m\in\ker P_m\cap\mathcal H_{\le q+2d}.
$$
残量仍满足
$$
\|r_m\|
\le\tau_{q-2}(u)+e^{-500d^4}\|u\|.
\tag{5.1}
$$

**定理。** 对任意 $p>4/9$、$c>0$，原两个实际慢核都满足
$$
\boxed{
M\cap\operatorname{Dom}e^{\,c(1+\mathcal N)^p}
\subseteq N.
}
\tag{5.2}
$$

确实，若 $w=Ju$ 属于左侧，首位分量提取给
$\tau_Q(u)\le C_we^{-c(1+Q)^p}$。
而 $q=25d^3$ 时
$$
d^{4/3}(1+\log d)^{4/3}=o(d^{3p}).
$$
结合 (4.3)、(5.1)，得到 $\|c_m\|\to0$。
真实 $X_7\to X_3$ 桥给
$$
n_m=\Lambda_{m,q+2d}k_m\in N.
$$
其全部 carry 与输出域已经在第七附录付清。
本稿还可同时使用旧
$\log\mathcal B_{m,q}\le100d^2(1+\log d)\le2d^4$
来保持 $m\ge4$ 的明确修正误差 $e^{-997d^4}\|u\|$。
于是 $n_m\to Ju=w$ 强于 Hilbert 空间，证明 (5.2)。

该证明直接处理原实际核，不要求缺陷投影保权。
它没有证明这个正则子集在 $M$ 内稠密。

## 6. 真缺陷的全序列尾率

仍以 $\tau_Q(w)=\|\mathbf1_{\{\mathcal N>Q\}}w\|$ 表示全部物理孔次数尾。

设 $0\ne w=Ju\in M\ominus N$。
第六、七附录的真实配对仍给，对充分大 $m$，
$$
\|c_m\|\tau_{q-1}(w)\ge\frac25\|w\|^2.
$$
将 (4.2) 用于 $r_m$，并用 (5.1)，小的
$e^{-500d^4}$ 项可以由旧上界吸收。
因此
$$
\mathfrak B_{m,q}\tau_{q-2}(w)^2
\ge\frac15\|w\|^2
$$
对充分大 $m$ 成立，必要时先把上界改为旧、新上界的较小值。
由 (4.3)，
$$
\log\frac{\|w\|}{\tau_{25d^3-2}(w)}
\le2048\,d^{4/3}(1+\log d)^{4/3}
+\tfrac12\log5.
$$
相邻 $q$ 网格比为 $8$，按尾范数单调性推至全部次数，得到
$$
\boxed{
-\log\frac{\tau_Q(w)}{\|w\|}
=
O\!\left(
Q^{4/9}(\log(Q+2))^{4/3}
\right).
}
\tag{6.1}
$$
特别对所有 $p>4/9$，左侧为 $o(Q^p)$。
这仍是非零缺陷的必要慢尾条件，不是尾部上界，也不排除任意慢的 Hilbert 尾。

## 7. 未越过的范围

本稿改善的是已经属于 $\ker D^{2d}$ 的特殊顶部残量。
用于把实际核向量送到这个有限阶核的前半桥仍是 R254 第三、五附录；
不能对未证明属于某个 $\ker D^s$ 的高阶残量直接使用 (1.5)。

正则指数已经跨过 $1/2$，但本结论只在原负整数边界的实际核中成立。
不因此把 Haar 表示中正则器的值域、Haar 不变限制的域密度或正常态结论搬到这里。

一般实际核向量仍可能没有任何 (5.2) 中的次数正则性。
任意慢尾还不能支付 (4.3) 的成本。因此 $N=M$、无权缺陷能量及普通 ISP 仍未完成。
