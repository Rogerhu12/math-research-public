# R271 附录：指数远孔起点的相对全算子 Gram、原列投影与真实加权残量

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下原完整列空间的加权投影、相对全 carry 运输和真实 $T$ 残量界已证明。**
本稿将旧全 $T$ 比较中的 $e^{81/s}$ 绝对误差，换为已付 c26 联合 carry 的相对 Fock 乘子。
孔权起点可以取 $y\asymp e^{12d^3}$，辅助方差可以取 $s\asymp 1/y$。
使用的始终是原未加权 Gram inverse；证明不假定它的列空间被孔权保持。
完整无限级数另经一个已支付的有限高度截断返回，不把有限乘子的高度条件直接推广到无穷。

真实 $T$ 残量由同一整列的一阶分量控制，因此在相同孔权下有 $O(\sqrt s)$ 界。
本稿未给只依赖旧 $d$ 的同源清除右逆；第 8 节明确核出通用右逆仍会支付的长前缀费用。

依赖：

- [联合 carry 与有限 Fock 相对 Gram](R271-appendix-joint-carry-finite-fock-multiplier-and-exponential-strong-prefix-gram.md)，尤其 §§1--5、7；
- [全部新增强位的原完整最小源](R271-appendix-all-strong-bit-extension-weighted-complete-source.md)，尤其精确截断卷积及两向加权 $B,K$；
- [真空源矩、实际物理运输与完整加权 inverse](R271-appendix-vacuum-source-moments-all-strong-physical-transport-and-weighted-inverse.md)，尤其 §§4--6；
- [原全 $T$ 的闭域 carry 求和](R271-appendix-global-actual-operator-weighted-full-gram-inverse.md)，只使用其局部支撑、闭域及两向 carry 范数界，不使用其 $y=m+d$ 的裸 Gram 预算。

## 1. 原参数与完整列

对原 N 或 Y 取
$$
m\ge10,\qquad d=2^m,\qquad
y\ge m+d,\qquad K\ge2^{24},\qquad s\ge K/y.
$$
定义
$$
L=L_m=A_m+D_{\ge m}=C_y+D_{\ge y},\qquad
C_y=A_m+D_{[m,y)},\qquad h=d+y-m\le2y,
$$
$$
\Gamma=\Gamma_y=32^{N_{\ge y}},\qquad
\mathscr R_m=\exp\!\left(\frac{417}{8}d^3\right).
\tag{1.1}
$$
$C_y^h=0$。这里的 $h$ 是原新增长前缀的真实幂零阶，没有将它改写成旧 $d$。
对有界原算子 $X$，令
$$
\mathcal R_{X,J}(s)v
=\sum_{j=0}^J\frac{(-X)^jv}{\sqrt{j!s^j}}\otimes e_j,
\qquad H_{X,J}=\mathcal R_{X,J}^*\mathcal R_{X,J}.
\tag{1.2}
$$
所有有限 $J$ 的 Gram 至少为 $I$。完整 $J=\infty$ 级数也按算子范数收敛。
记 $i_0v=v\otimes e_0$、$P_0=i_0^*$，并在列空间上使用
$\widehat\Gamma=\Gamma\otimes I$。

## 2. 完整 $L_m$ 列空间的真实加权正交投影

记
$$
\mathscr E_{L,J}=\operatorname{Ran}\mathcal R_{L,J},\qquad
P=P_{\mathscr E_{L,J}}
=\mathcal R_{L,J}H_{L,J}^{-1}\mathcal R_{L,J}^*.
$$
列空间闭，因为零行给 $\|\mathcal R_{L,J}v\|\ge\|v\|$。
本节证明比仅对辅助真空 forcing 的整列界更强的结论：
$$
\boxed{
\|\widehat\Gamma^{\pm1}P\widehat\Gamma^{\mp1}\|
\le p:=\frac{16}{15}.
}
\tag{2.1}
$$
正指数共轭均指从自然闭域得到的有界延拓。

先将新增尾截成 $D_{[y,x)}$。旧列空间
$\mathscr E_0=\operatorname{Ran}\mathcal R_{C_y,J}\otimes\mathcal H_{\ge y}$
的原正交投影与 $\Gamma$ 交换，其辅助支撑至多 $h-1$。
已付精确卷积给
$$
B=P_{\{N_a\le J\}}
\exp(-D_{[y,x)}a_{\rm aux}^*/\sqrt s)|_{\mathscr E_0},
\qquad K_B=B^*B,
\qquad P_x=BK_B^{-1}B^*.
\tag{2.2}
$$
这是真正完整截断列空间的正交投影。任意 $J$ 均使用 (2.2)，
不将一个未含全部塔的截断列空间称为整个闭核。

令 $\alpha=\|D_{[y,x)}\|/\sqrt s$，
$\theta_h(u)=u\sqrt h+u^2/2$，
$$
\theta_+=\theta_h(\alpha/32),\qquad
\theta_-=\theta_h(32\alpha),\qquad
\Theta=\theta_++\theta_-<1/32.
$$
最后一式只用 $\|D_{[y,x)}\|\le1/y$、$h\le2y$、$s\ge2^{24}/y$，
故不需要 $y=m+d$。
两向列共轭及原 $K_B^{-1}$ 的界为
$$
\|B_+\|\le e^{\theta_+},\qquad
\|B_-\|\le e^{\theta_-},\qquad
\|\Gamma_0K_B^{-1}\Gamma_0^{-1}\|
\le(2-e^\Theta)^{-1}.
$$
由 $\Gamma_0 B^*\widehat\Gamma^{-1}=B_-^*$ 的相应定义域恒等式，
$$
\|\widehat\Gamma P_x\widehat\Gamma^{-1}\|
\le\frac{e^{\theta_++\theta_-}}{2-e^\Theta}
\le\frac{32/31}{30/31}=\frac{16}{15}.
\tag{2.3}
$$
反向共轭交换 $\theta_+,\theta_-$，给同一常数。

把 $C_x=A_m+D_{[m,x)}$ 视为全物理空间上的算子，有 $C_x\to L$ 于算子范数。
固定有限 $J$ 时，$\mathcal R_{C_x,J}$、$H_{C_x,J}^{-1}$ 以及 $P_x$ 均按算子范数收敛到对应的 $L$ 对象。
先在有限位置、有限孔核心上取极限，再用 $\Gamma$ 闭性和该核心的图范数稠密性，得到 (2.1)。
同理，已付完整列及 inverse 界为
$$
\|\widehat\Gamma\mathcal R_{L,J}H_{L,J}^{-1}\Gamma^{-1}\|
\le\frac{16}{15},\qquad
\|\Gamma H_{L,J}^{-1}\Gamma^{-1}\|\le\frac{31}{30}.
\tag{2.4}
$$
本节也可通过 $J\to\infty$ 得到全列版本，但下面的相对 carry 步骤先保持有限 $J$。

## 3. 原全 carry 的两向相对乘子

固定有限 $J\ge1$，要求
$$
b=\sqrt{J/s}\le\mathscr R_m.
\tag{3.1}
$$
联合 c26 预算在原无限物理空间已包含
$\mathcal E=L_m-T$；有限前缀并非其成立条件。
以 $U(z)=e^{-zT}e^{zL}$ 作准确有限 Fock 乘子 $U_J$，符号与 (1.2) 一致，得到
$$
\mathcal R_{T,J}=U_J\mathcal R_{L,J},\qquad
P_0U_J=P_0,\qquad U_J^*i_0=i_0.
\tag{3.2}
$$
第零行恒等与最后的 forcing 身份都是精确恒等式。

为保留无界孔权的域，逐 carry 使用原局部支撑：
$A_m^j(\operatorname{ad}_{D_m}^aK_q)A_m^k$ 仅作用前 $q+1$ 位。
两向 $\Gamma_y$ 共轭所付费用至多
$32^{\max(0,q-y+1)}\le32^{q+1}$。
因此原 c26 逐 $q$ 预算及同一个 factorial 积分给
$$
\lambda:=2\frac b{\mathscr R_m}\,32^{m+1}e^{-15d^4/8}
\le e^{-7d^4/4},
\tag{3.3}
$$
$$
\boxed{
\|\widehat\Gamma^{\pm1}U_J^{\pm1}\widehat\Gamma^{\mp1}\|
\le e^\lambda,\qquad
\|\widehat\Gamma^{\pm1}(U_J^{\pm1}-I)\widehat\Gamma^{\mp1}\|
\le e^\lambda-1.
}
\tag{3.4}
$$
(3.3) 的最后一步用
$\log2+(m+1)\log32\le d^4/8$；$m\ge10$ 足够。
全部 carry 级数在两向加权算子范数中收敛。
先在有限物理核心核相同乘子恒等式，再用闭性，给 (3.4) 的真实域结论。
这一步没有 $e^{81/s}$。

## 4. 不假设列空间保权的原最小者运输

记 $P=P_{\mathscr E_{L,J}}$，在完整辅助环境空间定义
$$
A=I+P(U_J^*U_J-I)P.
\tag{4.1}
$$
它在 $\mathscr E_{L,J}$ 上是 $(U_J|_{\mathscr E_{L,J}})^*(U_J|_{\mathscr E_{L,J}})$，
在正交补上是 $I$；所以 $A$ 原本就是可逆正算子，而且与 $P$ 交换。
由 (2.1)、(3.4)，
$$
\|\widehat\Gamma(A-I)\widehat\Gamma^{-1}\|
\le\delta:=p^2(e^{2\lambda}-1)\le4\lambda<1/2.
\tag{4.2}
$$
于是，在 $\operatorname{Dom}\widehat\Gamma$ 的完备范数
$\|\widehat\Gamma v\|$ 中作 Neumann 级数，得到
$$
\|\widehat\Gamma A^{-1}\widehat\Gamma^{-1}\|
\le(1-\delta)^{-1},\qquad
\|\widehat\Gamma(A^{-1}-I)\widehat\Gamma^{-1}\|
\le\frac\delta{1-\delta}.
\tag{4.3}
$$
原 Hilbert 空间逆的唯一性将它识别为 (4.1) 的同一个 $A^{-1}$。
没有把 $\Gamma$ 限制成未知列空间上的自同构。

对原同一个 $f\in\operatorname{Dom}\Gamma$，置
$$
a_X=H_{X,J}^{-1}f,\qquad k_X=\mathcal R_{X,J}a_X,
\qquad X=L,T.
$$
因为 $k_L=Pi_0f$、$U_J^*i_0f=i_0f$，原投影变换公式准确给
$$
k_T=U_JA^{-1}k_L,\qquad a_T=P_0A^{-1}k_L.
\tag{4.4}
$$
故
$$
\boxed{
\|\widehat\Gamma\mathcal R_{T,J}H_{T,J}^{-1}\Gamma^{-1}\|
\le\frac{p e^\lambda}{1-\delta}<\frac98,
\qquad
\|\Gamma H_{T,J}^{-1}\Gamma^{-1}\|<\frac98.
}
\tag{4.5}
$$
此外，
$$
\boxed{
\begin{aligned}
&\|\widehat\Gamma(\mathcal R_{T,J}H_{T,J}^{-1}
       -\mathcal R_{L,J}H_{L,J}^{-1})\Gamma^{-1}\|\le10\lambda,\\
&\|\Gamma(H_{T,J}^{-1}-H_{L,J}^{-1})\Gamma^{-1}\|\le10\lambda.
\end{aligned}}
\tag{4.6}
$$
例如第一行的直接上界为
$p(e^\lambda-1+\delta)/(1-\delta)$，第二行是 $p\delta/(1-\delta)$；
在 (3.3) 的范围均小于 $10\lambda$。
真正 $T$ 列投影也满足
$$
P_{\mathscr E_{T,J}}=U_JA^{-1}PU_J^*,\qquad
\|\widehat\Gamma P_{\mathscr E_{T,J}}\widehat\Gamma^{-1}\|
\le\frac{p e^{2\lambda}}{1-\delta}<\frac98.
\tag{4.7}
$$
以上所有 inverse 与投影都保原未加权定义。

## 5. 支付完整无限级数，不将有限高度条件丢掉

对任意 $y\ge m+d$，原闭域 carry 界及 $\|C_y\|\le7$ 给
$$
\|\Gamma^{\pm1}L\Gamma^{\mp1}\|\le8,
\qquad
\|\Gamma^{\pm1}T\Gamma^{\mp1}\|\le9.
\tag{5.1}
$$
取一个有限整数
$$
J_*\ge\max\{h-1,\ 81e^2/s,\ 4d^4+2\},
\qquad J_*/s\le\mathscr R_m^2.
\tag{5.2}
$$
设 $X=L,T$。两向共轭及伴随的正确次序给
$$
\left\|\Gamma\sum_{j>J_*}\frac{(X^*)^jX^j}{j!s^j}\Gamma^{-1}\right\|
\le\sum_{j>J_*}\frac{(81/s)^j}{j!}
\le e^{-J_*}=:\tau\le e^{-4d^4-2}.
\tag{5.3}
$$
最后一步由 $j!\ge(j/e)^j$、$j\ge81e^2/s$ 得每项至多 $e^{-j}$；
$\sum_{j>J_*}e^{-j}=e^{-J_*}/(e-1)<e^{-J_*}$。
同样，完整尾列本身满足
$$
\|\widehat\Gamma\mathcal R_{X,>J_*}\Gamma^{-1}\|\le\sqrt\tau.
\tag{5.4}
$$

现在以已付的有限 $H_{X,J_*}^{-1}$ 作加权 Neumann，
得到原完整 $\mathcal H_X(s)=H_{X,\infty}(s)$ 的逆。
其与有限逆之差通过
$$
\mathcal H_X^{-1}-H_{X,J_*}^{-1}
=-H_{X,J_*}^{-1}(\mathcal H_X-H_{X,J_*})\mathcal H_X^{-1}
$$
控制。对前 $J_*$ 行先把有界整列映射
$\mathcal R_{X,J_*}H_{X,J_*}^{-1}$ 保在一起，再使用 (5.3)；
不单独乘上 $\|\mathcal R_{X,J_*}\|$。
尾行则用 (5.4)。因此从有限列到完整列所增加的差至多 $3\sqrt\tau$。
结合 (3.3)、(4.5)--(4.6)，得到
$$
\boxed{
\|\widehat\Gamma\mathcal R_{T,\infty}(s)\mathcal H_T(s)^{-1}\Gamma^{-1}\|
\le\frac87,
\qquad
\|\Gamma\mathcal H_T(s)^{-1}\Gamma^{-1}\|\le\frac87,
}
\tag{5.5}
$$
$$
\boxed{
\begin{aligned}
&\|\widehat\Gamma(\mathcal R_{T,\infty}\mathcal H_T^{-1}
       -\mathcal R_{L,\infty}\mathcal H_L^{-1})\Gamma^{-1}\|
\le e^{-3d^4/2},\\
&\|\Gamma(\mathcal H_T^{-1}-\mathcal H_L^{-1})\Gamma^{-1}\|
\le e^{-3d^4/2}.
\end{aligned}}
\tag{5.6}
$$
可直接使用的总上界是 $10e^{-7d^4/4}+6e^{-2d^4-1}<e^{-3d^4/2}$。
所有级数极限都在原 Hilbert 空间先识别，再由闭孔权和图范数极限识别加权延拓。

例如，以下明确参数统一满足 (5.2)：
$$
m+d\le y\le e^{12d^3},\qquad
K/y\le s\le2K/y,\qquad K\ge2^{24}.
\tag{5.7}
$$
取 $J_*$ 为 (5.2) 三个下界的最大值向上取整。
因为 $1/s\le y/K\le e^{12d^3}$、$h\le2y$，
$$
J_*/s
\le2y/s+81e^2/s^2+(4d^4+3)/s
\le e^{25d^3}<\mathscr R_m^2
$$
对 $m\ge10$ 成立。这里旧 c26 参数仍为 $d=2^m$；
没有把它改成 $2^y$。

## 6. 真正的原 $T$ 残量及同一个 $w$ 的配对

有限 $J\ge1$ 时令 $a_T=H_{T,J}^{-1}f$，完整时令
$a_T=\mathcal H_T(s)^{-1}f$。
从 (4.5) 或 (5.5) 取实际第 $j$ 行，得到
$$
\boxed{
\|\Gamma T^j a_T\|
\le c\sqrt{j!}\,s^{j/2}\|\Gamma f\|,
\qquad
c=\frac98\ \text{（有限列）},\quad c=\frac87\ \text{（完整列）}.
}
\tag{6.1}
$$
有限情形取 $j\le J$，完整情形所有 $j\ge0$ 都成立。
特别，若 $f$ 支撑在前 $y$ 位，
$$
\boxed{\|\Gamma_y T a_T\|\le\frac87\sqrt s\,\|f\|.}
\tag{6.2}
$$
这是原完整算子的真实源残量，含全部实际 carry。

对每个 $w\in M=\ker T$，因 $H_{T,J}w=w$、$\mathcal H_T(s)w=w$，
$$
\boxed{\langle w,a_T\rangle=\langle w,f\rangle.}
\tag{6.3}
$$
这保原同一个 $w$；没有从 (6.2) 把 $a_T$ 宣称为物理核向量。

还可保持实际旧源能量。若 $f=i_0g$ 是前 $y$ 位 forcing，
令旧完整 $C_y$ 列的能量为 $E_l$、$\mu_1=\sum_{l=1}^{h-1}lE_l$。
真空源矩定理在 $J\ge h-1$ 后稳定，结合 (5.6) 给
$$
\|\widehat\Gamma_y(k_T-k_y)\|
\le e^{-3d^4/2}\|g\|
  +\frac{64}{\sqrt{3K}\,y}\sqrt{\mu_1}.
\tag{6.4}
$$
因此第 1 行有更精确的同源界
$$
\|\Gamma_yTa_T\|
\le\sqrt s\left[
\left(1+\frac{64}{\sqrt{3K}\,y}\right)\sqrt{\mu_1}
+e^{-3d^4/2}\|g\|\right].
\tag{6.5}
$$
一次旧 log 方差选择仍可把 $\sqrt{\mu_1}$ 换成
$\Delta_{g,Q}/\sqrt{\log2}$，在旧定理给出的共同 $x,Q$ 范围内使用；
不对每个后续 cut 另换方差。

## 7. 原物理同源列与指数母窗口

记旧真实物理列为
$$
f_y^{\rm phys}=\sum_{j=0}^{h-1}
\frac{(-C_y)^ja_y\otimes(D_y^*)^j\Omega}{j!s^j},
\qquad a_y=H_{C_y,h-1}(s)^{-1}g.
$$
原物理运输定理和 (5.6) 直接给
$$
\boxed{
\|\Gamma_y(a_T-f_y^{\rm phys})\|
\le e^{-3d^4/2}\|g\|
+\frac{96}{\sqrt{3K}\,y}\sqrt{\mu_1}.
}
\tag{7.1}
$$
这里的 $\Gamma_y$ 作用于真实全部 $i\ge y$ 物理孔，
不把辅助层作为物理层。
旧列在 $Q\ge(y-m)+(h-1)$ 时保持原 $P_{V_Q}f$、$P_{K_Q}f$ 及同一个 $u$；
其所有两端 partial 继续由这个同一 $u$ 生成。
(7.1) 是原全 $T$ 正则化列与此已知同源物理列的比较，
并不把有限 $Q$ 的同源身份直接赋给 $a_T$。

若下一步还使用大辅助真 $F_0$ 构造，可给一个同时合法的增长窗。
取 $m\in4\mathbb N$、$m\ge20$，取任意整数
$$
m+d\le y\le e^{12d^3},\qquad L=y.
$$
令 $J$ 为不小于 $h+L-1$ 的最小偶数，$r=J+1$ 为奇数；于是
$$
h+L\le r\le h+L+1,\qquad J\le3y.
$$
取
$$
R=576(m+1)^2y^2,\qquad x=m+R,\qquad Q=R+r.
\tag{7.2}
$$
则 $R$ 为偶数且 $R\ge d$，
$$
J\le3y\le\frac{\sqrt{x+1}}{8(m+1)},
\qquad Q\le600(m+1)^2y^2<e^{26d^3}.
\tag{7.3}
$$
最后一个常数界用 $r\le3y+1$、$m\ge20$，
而 $\log(600(m+1)^2)<2d^3$。
同样由 $\log(2400(m+1)^2)<2d^3$ 得 $x+1<e^{26d^3}/4$；
旧 $y$ 完整物理列所需的 $R_y+h-1$ 远小于此 $Q$。

若还需最高 carry 零头改基后的 c26 母预算，必须另令 $n=2^{m-1}=d/2$，
并把本节上限收紧为
$$
y\le e^{12n^3}.
\tag{7.4}
$$
此时相同 $R,r,Q$ 满足 $Q<e^{26n^3}$、$x+1<e^{26n^3}/4$。
改基头为 $m-1$ 时的强长度是 $R+1$，所以准确支持条件仍由 $Q=R+r$ 支付。
不能将 $y\asymp e^{12d^3}$ 时的旧 $m$ 预算直接挪给 $m-1$。

此窗的低新增孔 $\le L$ 包含在全部 $\ker C_t^r$ 和真正 $F_0$ 中，
故既有大辅助真 $F_0$ 定理可按原范围应用。
但是该定理的原完整残余是否在 $\Gamma_y$ 下有可支付费用，仍未由 (7.2) 解决。

## 8. 清除端的费用核对：已知通用右逆仍依赖长前缀

上述 carry 和列比较只使用旧 $d$ 的预算及 $J/s\le\mathscr R_m^2$。
这并不自动把真残量的物理右逆费用改成仅依赖 $d$。

既有实际右逆定理针对
$$
\mathscr X_\kappa=
\left\{v:\sum_{q\ge0}e^{\kappa q}\|P_qv\|<\infty\right\},
\qquad \kappa>\kappa_*:=2+2\log2.
$$
因 $\kappa_*<\rho:=\log32$，可选 $\kappa\in(\kappa_*,\rho)$。
分解前 $y$ 位孔数 $a\le y$ 与远孔数 $b$，三角及 Cauchy--Schwarz 给
$$
\begin{aligned}
\|v\|_{\mathscr X_\kappa}
&\le\sum_{a=0}^y\sum_{b\ge0}
e^{\kappa(a+b)}\|P_a^{<y}P_b^{\ge y}v\|\\
&\le
\frac{e^{\kappa y}}
{\sqrt{(1-e^{-2\kappa})(1-e^{-2(\rho-\kappa)})}}
\|\Gamma_yv\|.
\end{aligned}
\tag{8.1}
$$
所以把 (6.2) 直接送入该通用右逆，所得已知上界仍含
$$
C_\kappa\,e^{\kappa y}\sqrt s,
\tag{8.2}
$$
而不是仅依赖旧 $d$ 的常数乘 $\sqrt s$。
当 $y\asymp e^{12d^3}$、$s\asymp1/y$ 时，(8.2) 不能给趋零清除。
这只说明现有通用估计不能完成此步骤，不是实际最小清除费用的下界。
此外该右逆的既有输出界是原 Hilbert 范数，
不能在没有另付输出正则性时宣称修正后的核向量属于所需指数孔空间。

因此准确的新增接口是：在指数远孔起点与真实闭域中，
原全 $T$ 正则化源有 (6.2)、(6.5) 的小残量及 (7.1) 的同源物理比较；
剩余必须利用这一个实际残量的来源，证明更强的清除费用或完整 MP 返回。
普通 ISP、真 $F_0$ 在 $S_x$ 的绝对 $\mathcal Z_\gamma$ 均未由本稿完成。
