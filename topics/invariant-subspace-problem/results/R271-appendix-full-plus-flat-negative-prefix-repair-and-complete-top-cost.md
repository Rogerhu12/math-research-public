# R271 附录：完整右费加原平坦费的负前缀修正，以及全部顶部链差的支付

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220。AI-assisted，GPT-6 Astra Pro。

状态：**下述正算子定理、原来源应用和费用运输已证明。** 本文补上[同一 good-top 的增长负前缀构造](R271-appendix-coherent-good-top-growing-negative-prefix-and-exact-head-tests.md)所明确保留的初次完整右费缺口。修正使用同一个原源的完整右费和原平坦费，不交换度量，也不要求修正源本身属于低头旗。最终固定物理测试的局部 Gram 上界、纯高逆总费、无权 $N=M$ 与普通 ISP 仍未完成。

依赖：[真实来源与两费](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、[固定测试共同 good-top](R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)、[已有增长负前缀](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)、[更锐原列泄漏](R271-appendix-columnwise-low-height-leakage-and-sharp-cubic-log-common-cost.md)、[完整顶部费用的联合余商](R271-appendix-tail-adaptive-joint-quotient-with-complete-top-cost-transport.md)。

## 1. 同一个原源上的第三种正度量

固定一个原合法 $m,d=2^m,b$。原源空间为 $\mathscr R_b$，保留原头、尾阶和物理内积。记
$$
L=(E_bE_b^*)^{-1},\qquad
B=J_{\rm bare}^{-1},\qquad G=J_{\rm right}.
$$
对原源 $r$，
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,\quad
\lambda_{\rm flat}(r)^2=\langle LGLr,r\rangle .
$$
原两费是
$$
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2.
$$
完整右链的约束较多，故 $0\prec G\preceq B^{-1}$。这里只在固定原窗口使用已有闭值域及有界逆；不预设这些逆有一致小范数。

归一化源坐标为
$$
u=B^{1/2}r,\qquad
\mathsf H=B^{-1/2}LB^{-1/2},\qquad
C=B^{1/2}GB^{1/2},\qquad0\prec C\preceq I.
\tag{1.1}
$$
准确的费用是
$$
\alpha(r)^2=\|u\|^2,\quad
\mu(r)^2=\langle\mathsf Hu,u\rangle,\quad
\lambda(r)^2=\|C^{-1/2}u\|^2,\quad
\lambda_{\rm flat}(r)^2=\|C^{1/2}\mathsf Hu\|^2.
\tag{1.2}
$$

本篇使用
$$
\boxed{\mathsf M_3=C^{-1}+\mathsf H C\mathsf H,}
\qquad
\|u\|_{\mathsf M_3}^2
=\lambda(r)^2+\lambda_{\rm flat}(r)^2.
\tag{1.3}
$$
它在原源中恰是 $G^{-1}+LGL$。它不是原两费度量
$\mathsf M_2=I+\mathsf H C\mathsf H$。因 $C\preceq I$，
$$
\Xi(r)^2\le\|u\|_{\mathsf M_3}^2,\qquad
\mu(r)^2
\le\lambda(r)\lambda_{\rm flat}(r)
\le\frac12\|u\|_{\mathsf M_3}^2.
\tag{1.4}
$$
第一条仅用 $\alpha\le\lambda$；第二条保留原次序，来自
$\langle\mathsf Hu,u\rangle
=\langle C^{1/2}\mathsf Hu,C^{-1/2}u\rangle$。

## 2. 近共同旗的准确下界

令 $W$ 为归一化源空间中的闭子空间，并假设
$$
\| (C^{-1}-I)^{1/2}w\|\le\delta\|w\|,
\qquad w\in W,\quad\delta\ge0.
\tag{2.1}
$$
等价地，原源旗 $\mathscr F=B^{-1/2}W$ 满足
$\lambda(x)^2\le(1+\delta^2)\alpha(x)^2$。允许 $W$ 随窗口变化，也不要求它在 $\mathsf H$ 下不变。

定义
$$
R=P_W(I+\mathsf H),\qquad
\kappa(\delta)=\sqrt{1+\delta^2}+\delta.
\tag{2.2}
$$

**正算子引理。**
$$
\boxed{R\mathsf M_3^{-1}R^*
\succeq\kappa(\delta)^{-2}I_W.}
\tag{2.3}
$$
因此这个作用于 $W$ 的正算子可逆，逆范数至多 $\kappa(\delta)^2$。没有假设 $C$ 与 $\mathsf H$ 交换，也不需要 $\delta<1$。

**证明。** 置
$$
Z=C^{1/2}\mathsf H C^{1/2}\succeq0,\qquad
Q=(I+Z^2)^{-1/2}.
$$
有
$$
\mathsf M_3=C^{-1/2}(I+Z^2)C^{-1/2}.
$$
对 $w\in W$，令 $x=C^{-1/2}w$。准确分解为
$$
C^{1/2}(I+\mathsf H)w
=(C+Z)x=(I+Z)x-(I-C)x.
$$
于是
$$
\langle R\mathsf M_3^{-1}R^*w,w\rangle
=\|Q(C+Z)x\|^2.
\tag{2.4}
$$
$Q$ 与 $Z$ 交换，且在非负实轴上
$(1+z)/\sqrt{1+z^2}\ge1$，故
$$
\|Q(I+Z)x\|\ge\|x\|,\qquad \|Q\|\le1.
$$
记 $a=\langle(C^{-1}-I)w,w\rangle$。由 (2.1)，
$0\le a\le\delta^2\|w\|^2$，而
$$
\|x\|^2=\|w\|^2+a,\qquad
\|(I-C)x\|^2
=\langle(C^{-1}-2I+C)w,w\rangle\le a.
$$
因此
$$
\|Q(C+Z)x\|
\ge\sqrt{\|w\|^2+a}-\sqrt a
\ge\bigl(\sqrt{1+\delta^2}-\delta\bigr)\|w\|
=\kappa(\delta)^{-1}\|w\|.
$$
最后一步使用 $\sqrt{1+t}-\sqrt t$ 递减。代回 (2.4) 即得 (2.3)。证毕。

粗界 $(1-\delta)^2$ 在 $\delta<1$ 时也成立，但 (2.3) 保留全部参数范围。

## 3. 同时支付完整右费与原两费的真实修正

给定任意原归一化源 $u$，写 $\omega=Ru\in W$。定义
$$
\boxed{
v=\mathsf M_3^{-1}R^*
(R\mathsf M_3^{-1}R^*)^{-1}\omega,\qquad
u^0=u-v.
}
\tag{3.1}
$$
所有逆由 §1 的原固定窗口闭值域及 (2.3) 保证。直接有
$$
Ru^0=0,\qquad Rv=\omega.
\tag{3.2}
$$
$v$ 是满足 $Rv=\omega$ 的真正最小 $\mathsf M_3$ 费用修正，且
$$
\boxed{
\|v\|_{\mathsf M_3}^2
=\langle(R\mathsf M_3^{-1}R^*)^{-1}\omega,\omega\rangle
\le\kappa(\delta)^2\|\omega\|^2.
}
\tag{3.3}
$$
若 $p=B^{-1/2}v$，则
$$
\boxed{
\lambda(p)^2+\lambda_{\rm flat}(p)^2
\le\kappa(\delta)^2\|\omega\|^2,\quad
\Xi(p)^2\le\kappa(\delta)^2\|\omega\|^2,\quad
\mu(p)^2\le\frac{\kappa(\delta)^2}{2}\|\omega\|^2.
}
\tag{3.4}
$$

该修正是 $\mathsf M_3$ 正交的：
$$
\|u\|_{\mathsf M_3}^2
=\|v\|_{\mathsf M_3}^2+\|u^0\|_{\mathsf M_3}^2.
\tag{3.5}
$$
但没有把 (3.5) 改写成原 $\mathsf M_2$ 的 Pythagoras。后者只使用
$$
\Xi(r-p)\le\Xi(r)+\Xi(p).
\tag{3.6}
$$
一般 $p$ 不属于 $\mathscr F$。其完整费用已由 (3.3) 直接支付，无须给它附加错误的低头支持结论。

最后，(3.2) 在原源中准确等价于
$$
\boxed{
\langle(L+B)(r-p),x\rangle=0\quad\hbox{对每个 }x\in\mathscr F.
}
\tag{3.7}
$$
它是整个 $L+B$ 负前缀条件，不是令源或左最小者的物理坐标为零。

## 4. 原同未来带给出需要的小缺陷

对原真实来源，已有同未来带身份
$$
C^{1/2}(I+\mathsf H)u=(I-C)^{1/2}z,
\qquad
\|u\|^2+\|z\|^2\le\|Y_b\|^2.
\tag{4.1}
$$
这里 $Y_b$ 是原同一个未来向量的实际窗口部分；不是另取的自由源。由 $C$ 可逆，
$$
(I+\mathsf H)u=(C^{-1}-I)^{1/2}z.
$$
(2.1) 因而给
$$
\boxed{\|\omega\|\le\delta\|Y_b\|.}
\tag{4.2}
$$
结合 (3.4)，置
$$
\vartheta(\delta)=\delta\kappa(\delta),
$$
得到
$$
\boxed{
\lambda(p)^2+\lambda_{\rm flat}(p)^2
\le\vartheta(\delta)^2\|Y_b\|^2,\qquad
\mu(p)^2\le\frac12\vartheta(\delta)^2\|Y_b\|^2.
}
\tag{4.3}
$$
这一步同时使用近共同旗与原来源小缺陷；不是从环境坏方向推断真实来源。

可取已证明的增长整旗
$$
\mathscr F_{k_m}=\mathscr R_b\cap\ker A^{k_m},
\qquad W=B^{1/2}\mathscr F_{k_m}.
$$
例如更锐列泄漏给
$$
j_m=\max\{1,\lfloor(\log m/268)^{1/3}\rfloor\},\quad
k_m=j_m+1,\qquad
\delta_m^2\le\frac{50j_m}{3m^3}.
\tag{4.4}
$$
这里保留整个原 $d$ 尾阶，所有孔层统一。亦可使用旧
$\delta_m\le2/[m(1-m^{-1/2})]$ 的增长前缀。
两种选择均有 $k_m\to\infty,\ \vartheta_m:=\vartheta(\delta_m)\to0$。

## 5. 同一个共同 good-top 的完整费用

沿原假设中的固定 $w\ne0$、原未来向量和共同 good-top，记
$$
d=2^m,\quad Q_m=\lfloor e^{d^3/4}\rfloor,\quad
K_m=K_m^{\rm win}\asymp Q_m/d,\quad
W_0=\|w\|,\quad\rho_m=\varepsilon_m/W_0.
$$
$\varepsilon_m\to0$ 只用原实际尾收敛，不附加速率。共同选择支付
$$
\|Y_b\|^2\le\frac{2\varepsilon_m^2}{K_m},\qquad
\Xi(r)^2\le\frac{4\varepsilon_m^2}{K_m},\qquad
\|E_b^\dagger r-w\|\le\varepsilon_m.
\tag{5.1}
$$
正尾量情形取 $\rho_m>0$；零尾量已直接无非零缺陷。

对 (4.4) 的整旗作 (3.1)，得 $r^0=r-p_0$ 属于
$$
\mathscr D_{k_m}
=\{s:\langle(L+B)s,x\rangle=0\ \forall x\in\mathscr F_{k_m}\}.
$$
该旗包含原首头，所以 $\mathscr D_{k_m}$ 包含的源仍满足原首头负图要求；原源与新源的差 $p_0$ 也保这一已经存在的来源线性条件。

令 $c_m=\sqrt2+\vartheta_m$。由 (4.3)、(5.1)，
$$
\boxed{
\mu(p_0)\le\frac{\vartheta_m\varepsilon_m}{\sqrt{K_m}},\quad
\lambda(p_0)\le\frac{\sqrt2\vartheta_m\varepsilon_m}{\sqrt{K_m}},\quad
\Xi(r^0)^2\le\frac{2c_m^2\varepsilon_m^2}{K_m}.
}
\tag{5.2}
$$
$c_m\to\sqrt2$。与旧全局 resolvent 修正相比，这里已经支付普通完整顶部链差，而非仅支付左像差。

接着完整执行既有原构造：在同一 $\mathscr D_{k_m}$ 内先作
$H_m=2^{\lfloor3m/4-2\rfloor}$ 原源头旗的真实 $\mathsf M_2$ 投影，再在其闭余空间内作原 triplet／角谱的尾自适应联合谱删除。记这两步为 $p_H,p_1$，最终源
$$
\widehat r=r-p_0-p_H-p_1.
$$
由[联合完整费用定理](R271-appendix-tail-adaptive-joint-quotient-with-complete-top-cost-transport.md)的齐次性，
$$
\begin{aligned}
\mu(p_H)&\le c_m a_m\varepsilon_m,&
\lambda(p_H)&\le c_m b_m\varepsilon_m,\\
\mu(p_1)&\le c_mW_0\sqrt{\rho_m}\,K_m^{-1/4},&
\lambda(p_1)&\le\sqrt2c_mW_0\rho_m^{1/4},
\end{aligned}
\tag{5.3}
$$
其中
$$
a_m=8\sqrt d\,e^{-11d^3/128},\qquad
b_m=32\sqrt d\,e^{-3d^3/64}.
$$
全部旗都与当前真实闭约束相交，后两步仍有
$$
\Xi(r^0)^2
=\Xi(p_H)^2+\Xi(p_1)^2+\Xi(\widehat r)^2.
\tag{5.4}
$$
(5.4) 从 $r^0$ 开始；没有把初次 $\mathsf M_3$ 修正伪写为两费正交删除。

## 6. 原顶部完整最小链也准确运输

对总修正 $p=p_0+p_H+p_1$，(5.2)—(5.3) 给
$$
\boxed{
\mu(p)\le
\frac{\vartheta_m\varepsilon_m}{\sqrt{K_m}}
+c_ma_m\varepsilon_m
+c_mW_0\sqrt{\rho_m}\,K_m^{-1/4}
\longrightarrow0,
}
\tag{6.1}
$$
$$
\boxed{
\lambda(p)\le
\frac{\sqrt2\vartheta_m\varepsilon_m}{\sqrt{K_m}}
+c_mb_m\varepsilon_m
+\sqrt2c_mW_0\rho_m^{1/4}
\longrightarrow0.
}
\tag{6.2}
$$
因此同一个原完整右源算子的线性 MP 选择子满足
$$
\boxed{
\|F_b^\dagger r-F_b^\dagger\widehat r\|
=\lambda(p)\longrightarrow0.
}
\tag{6.3}
$$
这次运输包括最初的负前缀修正。没有把它换成纯
$S_H^\dagger$ 返回费用，也不改原平坦度量。

另一方面
$$
\|E_b^\dagger\widehat r-w\|
\le\varepsilon_m+\mu(p)\longrightarrow0.
$$
从同一个新顶部左最小者重建所有低于 $b$ 的真实来源，
既有稳定前缀与正耗散给全部左像、feedback 的总差由
$\mu(p)$ 支付。最终顶部仍有锐 $K_m^{-1}$ 两费预算 (5.2)、(5.4)，全部低层来源保相容。

最终同时保留：整个 $L+B$ 的 $k_m$ 负前缀、精确
$H_m$ 源旗的真实两费交测试，以及两种后续旗的相对小投影。后者仍仅对真实闭交后的旗成立。没有独立改每个低窗口，也没有把旧未来 $b+1,\ldots,b+d$ 的向量或弱误差公式赋给新顶部。所有固定物理测试的值只按
$$
|\langle E_b^\dagger r-E_b^\dagger\widehat r,f\rangle|
\le\mu(p)\|f\|
$$
连接。

## 7. 剩余任务

本文支付初次负前缀的完整右费，并将整个三步构造的原顶部完整最小链差闭合。它没有给出固定测试源 $t_f$ 的完整右费，也没有给
$-D_{UK}D_{KK}^{-1}\iota_n$ 的局部两费 Gram 以窗口阶上界。
实际测试近链中的内部 $e_p$ 和右端点仍须保留。纯高逆的高深度部分、无权 $N=M$ 与普通复 Hilbert ISP 仍为 open.md 中的真实未解项。
