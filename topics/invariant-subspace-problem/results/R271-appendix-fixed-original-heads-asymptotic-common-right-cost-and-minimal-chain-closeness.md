# R271 附录：固定原头旗的渐近共同右费与真正最小链逼近

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；最短核泄漏观察：Astra-ISP-1cf8c51d / root。AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 对每个固定物理头数 $h$，整个原源旗
$\mathscr R_q\cap\ker A_m^h$ 的完整右费、裸右费和真幂底项在 $m\to\infty$ 时一致等价，比例趋于 $1$，且对全部合法 $q$ 与全部源尾核阶统一。真正完整最小链与真正裸最小链也在原范数中相对趋近。

关键改进是同源真幂链的内部残量只读取一个低高度删除块，
其平方范数至多 $hS_m$ 倍真幂底项，而非一般的头算子范数倍。
此外，原 R249 条件数给一整组增长的 dyadic 头
$H\asymp(\log m)^{1/4}$，其完整／裸费仍一致趋于 $1$。
不据此交换平坦源 Gram，也不把允许低域改动后的链逼近当作纯 $S_H^\dagger$ 上界。普通 ISP、原 $N=M$ 及一般实际余流比较仍 OPEN。

依赖：[原真幂底项与两道桥](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[固定原头反向补全](R271-appendix-every-fixed-original-head-flag-and-paid-backward-head-completion.md)、[出生一小头修复](R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md)、[R249 真实平衡相似](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)。

## 1. 原空间、费用及精确结论

固定原 $m\ge5,d=2^m$、$A=A_m$、$D=D_m$，以及合法 $q$。
令 $F_h=\operatorname{span}(e_0,\ldots,e_{h-1})=\ker A^h$，
$$
\mathscr E_{h,q}
=\mathscr R_q\cap(F_h\otimes\mathcal H_q)
=\bigoplus_{i=0}^{h-1}e_iE_{d-i-1,q},
\qquad 2\le h\le d-1.
\tag{1.1}
$$
尾旗始终保原 $d$，没有用小头数 $h$ 替换。

记 $a(r)$、$c(r)$ 分别为同一个源的原真正裸、完整最小链，
$$
\alpha(r)=\|a(r)\|,\qquad\lambda(r)=\|c(r)\|.
$$
同源真幂链为
$$
b_t(r)=(-1)^{t-1}
(D^t:\mathcal H_{q+t}\to\mathcal H_q)^\dagger A^{t-1}r
\quad(1\le t\le h),\qquad b_t=0\quad(t>h).
\tag{1.2}
$$
原精确分解给
$$
\|b(r)\|^2\le\alpha(r)^2\le\lambda(r)^2,\qquad
\alpha(r)^2-\|b(r)\|^2
=\|\mathcal G^\dagger\zeta(r)\|^2.
\tag{1.3}
$$

使用原固定首 $h$ 头逆
$$
B_h=(A|_{\operatorname{span}(e_1,\ldots,e_{h-1})})^{-1}
:F_{h-1}\to F_h\cap e_0^\perp,\qquad \kappa_h=\|B_h\|.
$$
它保全部短头旗，且在 $d\ge h+1$ 后不随 $m$ 改变。
置
$$
\nu_m=\|D_m\|\le m^{-1},\qquad
S_m=\sum_{\ell\ge m}(\ell+1)^{-4}\le(3m^3)^{-1},
$$
$$
\Gamma_h(m)=\kappa_h
\sum_{k=0}^{h-2}(\kappa_h\nu_m)^k,\qquad
\varepsilon_h(m)^2=
\min\{\nu_m^2,hS_m\}\,\Gamma_h(m)^2.
\tag{1.4}
$$

**主结论。** 对整个 $\mathscr E_{h,q}$，
$$
\boxed{
\lambda(r)^2\le
[1+\varepsilon_h(m)^2]\|b(r)\|^2
\le[1+\varepsilon_h(m)^2]\alpha(r)^2.
}
\tag{1.5}
$$
而且有准确的最小链平方关系
$$
\boxed{
\begin{aligned}
\|a(r)-b(r)\|^2&=\alpha(r)^2-\|b(r)\|^2,\\
\|c(r)-a(r)\|^2&=\lambda(r)^2-\alpha(r)^2,
\end{aligned}}
\tag{1.6}
$$
从而
$$
\boxed{
\|a(r)-b(r)\|^2+\|c(r)-a(r)\|^2
\le\varepsilon_h(m)^2\|b(r)\|^2.
}
\tag{1.7}
$$
特别，这同时支付原出生一最小不相容量和新 $H_2^\circ$ 高能量。

## 2. 两带性质和所需短核界

写
$$
E_{\ell,p}=\ker D^\ell\cap\mathcal H_p,\qquad
U_{\ell,p}=E_{\ell,p}\ominus E_{\ell-1,p},\qquad E_{0,p}=0.
$$
原交换子为
$$
[D,D^*]=S_mI-2W_m,\qquad
[D,[D,D^*]]=-2D_{3,m},\qquad [D,D_{3,m}]=0.
\tag{2.1}
$$
所以 $\operatorname{ad}_D^3(D^*)=0$。
有限交换展开给
$$
D^{\ell+2}D^*
=D^*D^{\ell+2}
+(\ell+2)[D,D^*]D^{\ell+1}
+\binom{\ell+2}{2}[D,[D,D^*]]D^\ell.
$$
因此
$$
\boxed{D^*E_{\ell,p}\subseteq E_{\ell+2,p+1}.}
\tag{2.2}
$$
结合 $DE_{\ell,p}\subseteq E_{\ell-1,p-1}$ 并取正交补，即得真实两带性质
$$
\boxed{
DU_{\ell,p}\subseteq
U_{\ell-1,p-1}\oplus U_{\ell-2,p-1}.
}
\tag{2.3}
$$
这里低于高度 $1$ 的空间按零处理。

还需原短核范数界
$$
\boxed{\|D|_{E_{\ell,p}}\|^2\le(\ell-1)S_m.}
\tag{2.4}
$$
为说明它不要求 $D^*$ 保核旗，作如下归纳。
$D=0$ 在 $E_1$ 上。
若 (2.4) 在 $E_{\ell-1}$ 上成立，则对 $z\in E_{\ell-1}$，
$$
\|D^*z\|^2
=\|Dz\|^2+\langle[D,D^*]z,z\rangle
\le(\ell-1)S_m\|z\|^2.
$$
而 $Dx\in E_{\ell-1}$ 对 $x\in E_\ell$，在该输出空间对偶便得 (2.4)。

## 3. 同源真幂残量只读取一个低高度块

令
$$
y_t=Ab_t+Db_{t+1}.
$$
真幂原像身份给 $D^ty_t=0$，且只有 $1\le t\le h-1$ 可能非零。
另一方面，
$$
b_t\perp E_{t,q+t},\qquad
b_{t+1}\perp E_{t+1,q+t+1}.
$$
$A$ 只作用头，所以也保这些尾空间的正交补。
因此有准确投影式
$$
\boxed{
y_t=P_{E_{t,q+t}}Db_{t+1}.
}
\tag{3.1}
$$
由 (2.2)，右端只读取 $P_{E_{t+2,q+t+1}}b_{t+1}$；
再用 $b_{t+1}\perp E_{t+1}$ 及 (2.3)，得到更窄的精确式
$$
\boxed{
y_t=P_{U_{t,q+t}}D
P_{U_{t+2,q+t+1}}b_{t+1}.
}
\tag{3.2}
$$
所有投影均为原 Hilbert 正交投影，未把幂逆先压成 primitive Gram。

(2.4) 给
$$
\|y_t\|^2
\le(t+1)S_m
\|P_{U_{t+2,q+t+1}}b_{t+1}\|^2.
$$
不同 $t$ 对应不同输入、输出段，所以平方相加后
$$
\boxed{
\|y\|^2\le
S_m\sum_{t=1}^{h-1}(t+1)
\|P_{U_{t+2,q+t+1}}b_{t+1}\|^2
\le hS_m\|b\|^2.
}
\tag{3.3}
$$
不使用高度估计，(3.1) 还直接给
$$
\|y\|^2\le\nu_m^2\|b\|^2.
\tag{3.4}
$$
这证明 (1.4) 中较小的两个真实泄漏常数均可用。

## 4. 完整零首源补量及 (1.5)

$y_t\in F_{h-t}\otimes E_{t,q+t}$。
取 $v_j=0$ 对 $j\ge h$，再倒递
$$
\boxed{
v_t=B_h(y_t-Dv_{t+1}),\qquad
t=h-1,\ldots,1.
}
\tag{4.1}
$$
原短头旗和尾核旗逐步给
$$
v_t\in F_{h-t+1}\otimes E_{t,q+t}.
\tag{4.2}
$$
因此 $v$ 在原宽度 $d$ 中合法，$Av_t+Dv_{t+1}=y_t$。
最左端 $Dv_1=0$，因为 $v_1\in E_1$；末端也为零。
于是 $Sv=y$、$Fv=0$。
有限三角反代的全部费用为
$$
\boxed{\|v\|\le\Gamma_h(m)\|y\|.}
\tag{4.3}
$$
$h-1$ 次幂为零的移位项只产生 (1.4) 的有限和，不需无限级数收敛。

同源完整候选 $\widetilde c=b-v$ 满足原全部方程。
逐段 $b_t\perp E_t$、$v_t\in E_t$，故
$$
\lambda(r)^2\le\|\widetilde c\|^2
=\|b\|^2+\|v\|^2
\le[1+\varepsilon_h(m)^2]\|b\|^2.
$$
这证明 (1.5)。真正最小者 $c(r)$ 不被认作此特定候选。

## 5. 真正最小链之间的原范数关系

原裸分解准确给 $a-b=-\mathcal I\mathcal G^\dagger\zeta$，
且 $\mathcal I$ 等距，证明 (1.6) 第一式。

对真正完整最小链 $c$，其低投影 $P_Lc$ 是同源可行裸链。
因此
$$
P_Lc-a\in\ker\mathsf F\cap Z,
$$
而真正裸最小 $a$ 与这个零首源低空间正交；
$a$ 还与全部高输入正交。
于是
$$
\langle a,c\rangle=\|a\|^2,
$$
从而
$$
\|c-a\|^2=\|c\|^2-\|a\|^2=\lambda^2-\alpha^2.
$$
这证明 (1.6) 第二式。
加上 (1.5) 即得 (1.7)；没有把任何非正交差的平方直接相加。

## 6. 每个固定原头旗的一致渐近

固定 $h$ 后，原 $\kappa_h$ 为常数，且 $\nu_m\to0$。
若 $m\ge2\kappa_h$，则有限和由一个收敛几何级数上界，得到
$$
\Gamma_h(m)\le2\kappa_h,\qquad
\boxed{
\varepsilon_h(m)^2\le
\frac{4h\kappa_h^2}{3m^3}.
}
\tag{6.1}
$$
因此
$$
\boxed{
\sup_{\substack{q\ {\rm 合法}\\0\ne r\in\mathscr E_{h,q}}}
\left(\frac{\lambda(r)}{\alpha(r)}-1\right)
\le\frac{2h\kappa_h^2}{3m^3}\longrightarrow0.
}
\tag{6.2}
$$
同样，$\alpha(r)/\|b(r)\|$ 与 $\lambda(r)/\|b(r)\|$ 均一致趋于 $1$。
由 (1.7)，两个真正最小链的相对差满足
$$
\boxed{
\frac{\|c(r)-a(r)\|}{\alpha(r)}
\le2\kappa_h\sqrt{\frac h3}\,m^{-3/2}.
}
\tag{6.3}
$$
原出生一最小不相容也满足
$$
\|\mathcal G^\dagger\zeta(r)\|
\le2\kappa_h\sqrt{h/3}\,m^{-3/2}\|b(r)\|.
\tag{6.4}
$$
所有量始终来自同一个原源。

特别 $h=2$ 时 $\kappa_2=1$、$\Gamma_2=1$，故不需 $m$ 的额外门槛即有
$$
\boxed{\lambda(r)^2\le(1+2S_m)\alpha(r)^2
\quad(r\in\mathscr E_{2,q}).}
\tag{6.5}
$$
$h=1$ 仍精确为 $\lambda=\alpha=\|b\|$。

## 7. 一整个增长原头旗仍趋于共同费用

前节也可把 $B_h$ 倒递换成 R249 的真实 dyadic 头相似。
设 $H=2^n$、$5\le n<m$，
$$
A_n=\Sigma_n(\gamma_nJ_H)\Sigma_n^{-1},\quad
\gamma_n=e^{20-\mathcal L_n},\quad
\mathcal L_n=\frac{25H^4}{2(H-2)},\quad
\mathfrak k_n=\|\Sigma_n\|\,\|\Sigma_n^{-1}\|.
$$
完整出生一修正的范数可取
$$
\Gamma_{n,m}^{(1)}
=\mathfrak k_n\sum_{k=0}^{H-2}\gamma_n^{-k-1}\nu_m^k.
\tag{7.1}
$$
§§3–5 因此给
$$
\boxed{
\lambda(r)^2\le
[1+HS_m(\Gamma_{n,m}^{(1)})^2]\|b(r)\|^2
\quad(r\in\mathscr E_{H,q}).
}
\tag{7.2}
$$

R249 的准确式直接给
$$
\begin{aligned}
\log(\mathfrak k_n\gamma_n^{-1})
\le{}&
\left(\frac{35}{6}+\frac{25}{H-2}\right)H^4+15H^3\\
&-(150n-275-\log12)H-\frac{910}{3}+2\log H.
\end{aligned}
$$
$H\ge32$ 时第二行负，第一行除以 $H^4$ 后至多
$35/6+25/30+15/32<8$，故
$$
\boxed{
\mathfrak k_n\gamma_n^{-1}\le e^{8H^4},\qquad
\gamma_n^{-1}\le e^{H^4}.
}
\tag{7.3}
$$
第二式由 $\mathcal L_n-20\le H^4$ 直接得到。

对充分大的 $m$，选最大的 dyadic $H=H(m)\ge32$，使
$$
\boxed{H^4\le\frac{\log m}{8}.}
\tag{7.4}
$$
于是 $H(m)\asymp(\log m)^{1/4}$、$H(m)\to\infty$，且最终 $H(m)<d/2$。
由 (7.3)，
$$
\nu_m\gamma_n^{-1}\le m^{-7/8}\le\frac12,\qquad
\Gamma_{n,m}^{(1)}
\le2\mathfrak k_n\gamma_n^{-1}\le2m.
$$
代入 (7.2)，得到整个增长原旗的统一界
$$
\boxed{
\lambda(r)^2\le
\left(1+\frac{4H(m)}{3m}\right)\|b(r)\|^2
\le
\left(1+\frac{4H(m)}{3m}\right)\alpha(r)^2,
\quad r\in\mathscr E_{H(m),q}.
}
\tag{7.5}
$$
误差 $4H(m)/(3m)\to0$，(1.6)–(1.7) 的真正链差也同样趋零。
这里的 $H(m)$ 与此前可用大常数删除的 $d^{3/4}$ 头宽不同；
(7.5) 新增的是增长旗上常数趋于 $1$。

### 与已发表的逐列前缀界的关系

已有 [R239 逐列真实头预算](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md) 已在更大的 $(\log m)^{1/3}$ 原源前缀上证明 $\lambda^2\le(1+O(m^{-2}))\alpha^2$。因此本节的 $(\log m)^{1/4}$ 尺度是本证明对真幂底项的一个明确推论，不作为首次增长前缀共同右费登记。本文额外支付的是 §§3–6 中同一个真幂底项的 $hS_m$ 泄漏、固定 $h$ 的 $O_h(m^{-3})$ 平方比例，以及真正 $a,b,c$ 三条最小链的原范数关系。

## 8. 原两费用的接口与边界

令 $\delta_m^2$ 表示 (6.1) 或 (7.5) 中相应误差，
$C_m=\sqrt{1+\delta_m^2}\to1$。
在显示的原源旗上，同源 Cauchy--Schwarz 仍只用真实 Gram：
$$
\boxed{
\mu(r)^2\le\lambda(r)\lambda_{\rm flat}(r)
\le\frac{C_m}{2}\bigl[\alpha(r)^2+\lambda_{\rm flat}(r)^2\bigr].
}
\tag{8.1}
$$
因此该旗可按原 $M_2=B+LGL$ 度量与真实负图取闭交并投影，
保所有已证好顶部来源与完整费用；其常数趋于共同费用值。

本文未把压缩后的 $B$ 与 $G^{-1}$ 比较用于交换
$\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle$ 中的算子；
$Lr$ 可能离开显示的源旗。
同样，(1.6) 中 $c-a$ 一般同时含低域零首源改动与高域补量，
所以它不提供固定裸候选的纯 $S_H^\dagger$ 逆界。
原源头支撑也没有被传递给整个真正 $\mathcal G^\dagger\zeta$ 的头支撑。
