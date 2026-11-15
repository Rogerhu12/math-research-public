# R630 — 原完整除法多项式的五层修正与第一非线性单位

日期：2026-11-15。**状态：已证明。** 本篇确定同一个原 $\psi_p$ 在完整次数 $(p^2-1)/6$ 中的模 $p^4$ 修正，并给到模 $p^7$ 的五份整商。它们的首项都是显示的单位，其中真正的二次项恰从 $\tau^{2s}$ 开始。

此位置在 R624 指定 determinant 的 $\tau^{2s-1}$ 窗口之后。所证单位不等于 $\mathfrak D_p$ 的单位，也不令原两 forcing 或中央余项消失。

## 1. 同一原 sigma 与整个 division 窗口

令
$$
p=6s-1>71,\qquad
L=(p^2-1)/6=s(p-1),\qquad
u=x^{-1/2},\quad \tau=bu^6,
$$
其中 $b$ 是本题原 $p$ 单位，微分、sigma 仍为
$$
D_zx=2y,\quad y^2=x^3+b,\quad
D_z^2\log\sigma=-x,\quad \sigma=z+O(z^7).
$$
定义
$$
C(\tau)=(1+\tau)^{-1/2}=\sum C_n\tau^n,\qquad
H(\tau)=\sum_{n\ge0}\frac{C_n}{6n+1}\tau^n,\qquad
z=uH(\tau),
$$
$$
K(\tau)=(\sigma(z(u))/u)^6,\qquad
L_K=\log K,\qquad
\mathcal A=pL_K .
\tag{1}
$$
所有本篇比较都在原有限环
$$
\mathcal R_{\mathbf Q}=\mathbf Q_p[\tau]/\tau^{L+1},
\qquad
\mathcal R=\mathcal O[\tau]/\tau^{L+1}
\tag{2}
$$
中进行；不把 $(1)$ 的无限 $K$ 无条件约化模 $p$。

原整数奇除法多项式的首项为 $p x^{(p^2-1)/2}$。置
$$
Q_p(\tau)=u^{p^2-1}\psi_p(u^{-2}),\qquad u^6=\tau/b.
\tag{3}
$$
它是原 $\psi_p$ 全部系数的反转，另有显示的 $b^{-n}$ 单位尺度。特别
$$
Q_p\in\mathcal R,\qquad Q_p(0)=p.
$$
原除子与首项固定的 sigma 乘法式给
$$
\boxed{
Q_p=\frac{\sigma(pz(u))}{u}\exp(-p^2L_K/6).
}
\tag{4}
$$
没有改变原 Gaussian 为另一 ordinary sigma。

## 2. 全窗口的分母与最高端点

从 $C_n=(-1)^n4^{-n}\binom{2n}{n}$ 的进位计数，或者 R619 与 serre-uniformity R757 的同一原计算，
$$
H_n\in\mathcal O\quad(n<L),\qquad v_p(H_L)=-1.
\tag{5}
$$
这是整个 (2) 中唯一非整的 $H$ 系数。

为自含第二个需要的分母界，记
$$
Q(\tau)=1+\theta L_K=\sum q_n\tau^n,\qquad
q_0=1,\quad
q_n=-\frac{6n-4}{6n-1}q_{n-1},
\qquad \theta=\tau\partial_\tau .
\tag{6}
$$
写 $n=ap+r,\ 0\le r<p$。在 $1\le n\le L$ 中，
所有 $6j-4,6j-1$ 都严格小于 $p^2$，故每个坏因子恰含一次 $p$。
每个长度 $p$ 的完整块中，分母在 $r=s$ 出现，
分子在 $r=4s$ 出现。因此
$$
v_p(q_n)=
\begin{cases}
-1,&s\le r<4s,\\
0,&\text{其它 }r.
\end{cases}
\tag{7}
$$
若 $p\mid n$，则 $r=0$、$q_n$ 为单位，只在除以 $n$ 时再失去一次 $p$。
由 $n<p^2$ 得
$$
v_p([\tau^n]L_K)=v_p(q_n/n)\ge-1,
\qquad
\boxed{\mathcal A\in\tau\mathcal R.}
\tag{8}
$$

(5)、(8) 还给一项后文反复使用的完整整性：
$$
\boxed{H\mathcal A^j\in\mathcal R\qquad(j\ge1).}
\tag{9}
$$
因为 $\mathcal A(0)=0$，唯一坏项 $H_L\tau^L$ 乘任何
$\mathcal A^j$ 后都越过截断。
这里不能把 $H$ 本身改称整；(9) 只对所列带正阶因子成立。

## 3. 原 numerator 的 p⁷ 误差

本篇需要比原 $p^5$ 粗误差更具体的估计：
$$
\boxed{
\frac{\sigma(pz(u))}{u}
=pH(\tau)+p^7\tau E(\tau),
\qquad E\in\mathcal R.
}
\tag{10}
$$

证明。写 $\sigma(z)/z=\sum a_nz^{6n}$。
R614 的原分解
$$
\sigma(z)/z=e^{cw^s}U(w),\qquad w=z^6
$$
在 $n<L$ 给 $U_n$ 整，在 $n=L$ 给 $v_p(U_L)\ge-1$。
此处所读 Gaussian 次数至多 $p-1$，其阶乘全为单位。因此
$$
v_p(a_n)\ge-\lfloor n/s\rfloor\qquad(1\le n\le L).
\tag{11}
$$
在 $n=L$，额外可能的 $U_L$ 极点为 $-1$，
仍大于或等于右边的 $-(p-1)$，所以没有遗漏端点。

直接代入原 $z=uH$：
$$
\frac{\sigma(pz(u))}{u}
=pH+\sum_{n=1}^{L}
 a_np^{6n+1}b^{-n}\tau^n H^{6n+1}.
\tag{12}
$$
在每个 $n\ge1$ 的实际保留项中，
外部 $\tau^n$ 使 $H^{6n+1}$ 只需要 $H_{\le L-n}$，
全部属于 (5) 的整区间。由 (11)
$$
v_p(a_np^{6n+1})\ge6n+1-\lfloor n/s\rfloor\ge7.
$$
于是 (12) 的全部非线性项都在 $p^7\tau\mathcal R$，
证明 (10)。本证明没有先将 $H_L$ 丢掉，而是逐项说明它在非线性项中超出总次数。$\square$

由 (8)，$\exp(-p\mathcal A/6)\in1+p\tau\mathcal R$。
代回 (4)，(10) 因而仍保持 $p^7$ 精度：
$$
\boxed{
Q_p=pH\exp(-p\mathcal A/6)+p^7\tau E_1,
\qquad E_1\in\mathcal R.
}
\tag{13}
$$

## 4. 原整条多项式模 p⁴ 与五份整商

**定理 1。** 在整个 (2) 中，
$$
\boxed{
Q_p\equiv
pH-\frac{p^2}{6}H\mathcal A
+\frac{p^3}{72}H\mathcal A^2
\pmod{p^4}.
}
\tag{14}
$$
更一般，对每个 $3\le r\le7$，
$$
\boxed{
Q_p\equiv
pH+\sum_{j=1}^{r-2}
 \frac{(-1)^j p^{j+1}}{6^j j!}H\mathcal A^j
\pmod{p^r}.
}
\tag{15}
$$

证明。在 (13) 中展开有限指数。常数项保留整个原 $pH$，
包括 $pH_L\tau^L$。每个正次数项的 $H\mathcal A^j$ 都由 (9) 整。
当 $j<p$ 时，其显式系数赋值为 $j+1$；
当 $j\ge p$ 时，
$$
j+1-v_p(j!)\ge j+1-\frac{j-1}{p-1}>7.
$$
所以所列截断以外的每项都在要求的 $p^r$ 中。
原 numerator 误差 (13) 也在 $p^r$ 中。$\square$

现在对 $1\le j\le5$ 定义**原实际整商**
$$
\boxed{
\mathscr E_j=
\frac{
Q_p-pH-\displaystyle\sum_{a=1}^{j-1}
 \frac{(-1)^a p^{a+1}}{6^a a!}H\mathcal A^a
}{p^{j+1}}.
}
\tag{16}
$$
式 (15) 先支付了整个分子的 $p^{j+1}$ 整除性，
故 (16) 的各项系数均整。特别
$$
\boxed{
\overline{\mathscr E}_j
=\frac{(-1)^j}{6^j j!}\bar H\,\overline{\mathcal A}^{\,j},
\qquad1\le j\le5,
}
\tag{17}
$$
其中右侧按 (9) 读取；它不要求单独约化最高的 $H_L$。

这不是五个任意目标列。每个 $\mathscr E_j$ 都来自显示的同一
$Q_p,H,\mathcal A$，扣除较低项时使用的也是同一原 $\mathcal A$。

## 5. 五个精确首项及首个真正二次单位

由 (6)，也可直接从
$$
\theta L_K=JC-1,\qquad
J_n=C_n/(1-6n)
$$
读取第一次坏项：
$$
\overline{\mathcal A}_n=0\quad(n<s),\qquad
\overline{\mathcal A}_s
=-\frac{\bar C_s}{s}=-6\bar C_s .
\tag{18}
$$
$C_s$ 为单位，因为 $2s<p$。
又有 $js\le5s<L$，此处 $H_0=1$ 且无最高坏项。
由 (17) 得到完整的首阶与绝对系数：
$$
\boxed{
\operatorname{ord}_\tau\overline{\mathscr E}_j=js,\qquad
[\tau^{js}]\overline{\mathscr E}_j
=\frac{\bar C_s^{\,j}}{j!}\in k^\times
\quad(1\le j\le5).
}
\tag{19}
$$

尤其原完整 $p^3$ 修正
$$
\mathscr E_2=
\frac{Q_p-pH+(p^2/6)H\mathcal A}{p^3}
$$
准确满足
$$
\boxed{
\overline{\mathscr E}_2=\bar H\,\overline{\mathcal A}^{\,2}/72,\qquad
\operatorname{ord}_\tau\overline{\mathscr E}_2=2s,\qquad
[\tau^{2s}]\overline{\mathscr E}_2=\bar C_s^2/2.
}
\tag{20}
$$
这付的是原多项式的实际非线性行及其首项单位，
不只是对一个形式指数猜出的候选。

## 6. 与 R624 临界 determinant 的精确分界

R624 的原 $\mathfrak D_p$ 只使用 canonical $\Lambda^\dagger$
至 $\tau^{2s-1}$。由 (20)，真正的二次修正在这个窗口恰为零。
所以 (14) 在同一个低窗口压成
$$
\boxed{
Q_p\equiv pH-\frac{p^3}{6}H L_K
\pmod{p^4,\tau^{2s}}.
}
\tag{21}
$$
因此也可以不用有限 log，而先定义
$$
D_{\rm lin}=\frac6{p^3}H^{-1}(pH-Q_p)
\quad\bmod\tau^{2s}.
$$
这里 $D_{\rm lin}$ 本身保留原 $L_K$ 的一个 $p$ 极点；
不是一个可以立即约化的整多项式。
准确的是
$$
D_{\rm lin}-L_K\in p\mathcal O[\tau]/\tau^{2s}.
$$
减去 R606 已定的
$6c_b^\dagger b^{-s}\tau^sH^{p+1}$ 后，整个差才整，
并且其 mod $p$ 值与 R624 的 $\mathscr L_p^\dagger$ 相同。

这解释了两个不同精度现象：

- 完整原 $p^2$ 修正 (17) 的第一份，只读取
  $\overline{pL_K}$；原 $n<s$ 的正常 $L_K$ 系数在其中全为零。
- 原正常低系数第一次以 $p^3$ 数据出现，决定 $\Lambda^\dagger$
  和两个临界 forcing；(20) 的已证二次单位却从 $\tau^{2s}$
  才开始，尚未落进这个 determinant 所需的窗口。

因此不能由 (19) 的五个单位宣称
$c_4,c_1$ 或 $\mathfrak D_p$ 非零。
这里没有把离开原 sigma 的任意参数修改当作反例，
只是在同一原公式中说明每个实际观察读取哪些位数和哪些次数。

## 7. 原三挠点常数给出的完整端点约束

原标准三挠点递推给
$$
\psi_p(0)=-(4b)^L,\qquad Q_{p,L}=-4^L.
\tag{22}
$$
这个规范与 serre-uniformity R757 的 $b=-1$ 版本一致；
按原 division 的权 $p^2-1$ 缩放即得任意本题 $b$。
又 $L$ 是四的倍数，故
$$
pH_L=\frac1{p\,4^L}\binom{2L}{L}.
$$
读取 (14) 的最高次数并乘 $p4^L$，得到
$$
\boxed{
\binom{2L}{L}
\equiv
-p\,16^L
+\frac{p^3\,4^L}{6}[\,\tau^L\,]H\mathcal A
-\frac{p^4\,4^L}{72}[\,\tau^L\,]H\mathcal A^2
\pmod{p^5}.
}
\tag{23}
$$
两个显示系数均已由 (9) 证明整。
(23) 保留整个 $L$ 截断的真实卷积，没有将它们替换成
$[\tau^{s-1}]KC$ 或 $[\tau^{s-1}]KH^3$。

更高的 (15) 同样可在这个原端点读取，但不得遗漏
$\sigma(pz)$ 在精度 $p^7$ 开始的 numerator 项。
本篇没有由某个浅端点单位或中央二项式单位删去这些卷积。

## 8. 后续需要解决的实际问题

本篇完成的是原整条 division 多项式的真实非线性修正、
五个完整整商及其准确单位首项。
要用它推进原两曲线的无穷素数目标，仍须证明一种原来源上的关系，
把 (20) 的 $\tau^{2s}$ 单位或 (23) 的完整端点送到
R624 的指定 determinant / R595–R606 的完整中央余项，
并保所有正常低系数、Gaussian 补项与原一次除 $p$ 商。

当前未证明这种返回，也未声称原 $\mathfrak D_p$、两个 forcing
或两个完整 $j_m$ 已有新的非消失结论。
主目标仍未完成。

## 依赖

- [R591](R591-original-inert-forcing-in-one-parameter-and-exact-resonance.md)：同一个原 $C,H,J,K$ 和 (6) 的准确递推。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)、[R619](R619-original-cartier-sparse-rows-and-second-newton-block.md)：原 sigma 的全 $n<L$ 整窗和唯一 $H_L$ 极点。
- [R624](R624-original-paired-forcing-determinant-and-four-digit-division-return.md)：指定两块 determinant 的完整物理行与四位返回。
- [Serre R757](../../serre-uniformity/results/R757-full-original-division-polynomial-mod-p2-and-Frobenius-constant-units.md)：原全多项式、原三挠常数及浅精度；本篇扩展时逐项重付 numerator、指数阶乘和最高极点。
- [Serre R760](../../serre-uniformity/results/R760-original-critical-sigma-jets-from-four-digit-division-data.md)：原第一临界低窗口；本篇未更换其 sigma 或 inverse-sigma 规范。

以上全部证明均为原恒等式和有限精度估计，没有新增素数扫描。
