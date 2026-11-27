# R271 附录：同一个实际右逆在全部物理孔指数尺度上的作用

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本稿针对原负整数边界的两个实际算子 $T_N,T_Y$。物理孔层投影记为 $\mathsf P_q$，并置
$$
X_\kappa=\left\{v:\|v\|_\kappa:=\sum_{q\ge0}e^{\kappa q}\|\mathsf P_qv\|<\infty\right\},
\qquad \kappa\ge0.
$$
这里是原全部物理孔数；不是首缺位号，也不是有限头的 Jordan 分级。

[R239 指数右逆附录](R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md) A.11 已给每个 $\lambda>\kappa_0:=2+2\log(3/2)$ 的实际右逆 $X_\lambda\to H$。本稿不重复该阈值结论。新增的是：固定一次构造后，误差从整个 $H$ 映入全部 $X_\kappa$，同一个 Hilbert 空间上的 Neumann 修正保留每个 $X_\kappa$，因此同一个右逆在整条尺度上只损失固定指数 $\lambda$。

## 1. 结论与实际定义域

固定
$$
\lambda>\kappa_0,\qquad \delta=\lambda-\kappa_0>0.
$$
存在一个固定线性算子
$$
\mathcal G_\lambda:X_\lambda\longrightarrow H,\qquad
T\mathcal G_\lambda=I,
\tag{1.1}
$$
以及只依赖 $\lambda$ 的有限常数 $C_\lambda$，使其同一限制满足
$$
\boxed{
\mathcal G_\lambda:X_{\kappa+\lambda}\longrightarrow X_\kappa,
\qquad
\|\mathcal G_\lambda\|_{X_{\kappa+\lambda}\to X_\kappa}
\le \exp[C_\lambda(1+\kappa)^2]
\quad(\kappa\ge0).
}
\tag{1.2}
$$
这些不是按 $\kappa$ 重新选择的不同右逆。$\mathcal G_\lambda$ 不被定义为全 $H$ 上的有界或处处定义右逆。

令
$$
\mathscr E_\infty=\bigcap_{\kappa\ge0}X_\kappa
$$
并赋予可数共尾范数 $\|\cdot\|_n$ 的 Fréchet 拓扑。则同一个 $\mathcal G_\lambda$ 连续作用于 $\mathscr E_\infty$，且 (1.1) 在此成立。原 $T$ 在每个 $X_\kappa$ 有界，故
$$
\Pi_\lambda=I-\mathcal G_\lambda T:
\mathscr E_\infty\longrightarrow
\ker T\cap\mathscr E_\infty
\tag{1.3}
$$
是连续投影。

还可在准确自然域上迭代：
$$
\boxed{
T^n\mathcal G_\lambda^n=I\ \text{于 }X_{n\lambda},
\qquad
\|\mathcal G_\lambda^n\|_{X_{n\lambda}\to H}
\le \exp(C'_\lambda n^3).
}
\tag{1.4}
$$
没有在 (1.4) 中假设 $T$ 与 $\mathcal G_\lambda$ 交换。

## 2. 只选择一次的旧有限头右逆

选整数 $Q$ 足够大，使
$$
Q\ge64,\qquad Q\ge(4\lambda+1)/8,
$$
$$
\frac{20\log Q}{\sqrt Q}\le\frac\delta4,\qquad
\frac12\log(2Q)\le\frac\delta4Q.
\tag{2.1}
$$
两式在 $Q\ge64$ 后分别由 $(\log x)/\sqrt x$、$\log(2x)/x$ 的递减性延至所有 $x\ge Q$。$Q$ 只依赖固定的 $\lambda$。

对 $q\ge0$ 置
$$
x=q+Q,\qquad
m=m(q)=\left\lceil\tfrac12\log_2x\right\rceil,\qquad d=2^m.
$$
于是
$$
\sqrt x\le d<2\sqrt x,\qquad m\le\sqrt x.
\tag{2.2}
$$
保留原有限头，写成
$$
T^{[m]}=H_m+D_{\ge m},\qquad
H_m^d=0,\quad\|H_m\|<6.
$$
上述 R239 附录 A.1 的完整实际局部展开为
$$
T-T^{[m]}=\sum_{L\ge m}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}}.
\tag{2.3}
$$
$K_L$ 只作用于前 $L+1$ 位，故
$$
K_LH_{\le b}\subset H_{\le b+L+1}.
\tag{2.4}
$$
(2.3) 同时包括 $Y$ 型完整 Cayley 逆所产生的全部项；以下不截掉任何长进位。

为明确同一个 $R_q$ 的选择，令
$$
s=q+d,\quad
N_F=\left\lceil\tfrac32(s+2)\right\rceil,\quad
F=\{m,\ldots,m+N_F-1\},\quad t=(m+N_F)^{-2}.
$$
取旧有限正对角压平算子
$$
\Delta e_S=\prod_{j\in S\cap F}\frac{a_j}{t}\,e_S,
\qquad a_j=(j+1)^{-2}.
$$
它保次数，$\|\Delta^{-1}\|\le1$。压平创建算子在所需全部尾次数 $p\le q+d$ 上有增益至少 $t$：除 $N_F$ 个平权位外，保留的未压平尾方差给
$$
t^{-2}\sum_{j\ge m+N_F}a_j^2
\ge\frac{m+N_F-3}{3},
$$
所以交换子下界至少为
$$
\left[N_F-2p+\frac{m+N_F-3}{3}\right]t^2I\ge t^2I.
$$
选其规范逐层右逆 $Q'_p$，则 $Q'_p$ 增加一个尾孔且 $\|Q'_p\|\le t^{-1}$。把它们合为所需有限层上的 $Q'$，定义
$$
R_q=\left.
\Delta^{-1}\sum_{k=0}^{d-1}(-H_m)^k(Q')^{k+1}\Delta
\right|_{H_q}.
\tag{2.5}
$$
各次组合均在已付的尾次数 $0,\ldots,q+d$ 中。头尾交换与 $H_m^d=0$ 给准确恒等式
$$
T^{[m]}R_q=I,\qquad
R_qH_q\subset H_{\le q+d+m}.
\tag{2.6}
$$
输出允许无限位支撑；(2.6) 只断言有限全部孔次数。

旧 A.25、A.61 的同一次输入压平成本给
$$
\log\|R_q\|
\le\kappa_0q+3d+\log d+d\log6+2d\log(m+N_F)
\le\kappa_0q+20\sqrt x\log x.
$$
由 (2.1)，
$$
\boxed{\log\|R_q\|\le\kappa_0q+\delta x/4.}
\tag{2.7}
$$
$q=0$ 的输入压平空积等于 $1$；(2.5)–(2.7) 均包括该层。

## 3. 同一个 R 的所有加权输出

由 (2.2)、(2.6)，输出次数至多 $q+3\sqrt x$，所含层数不超过 $2x$。Cauchy–Schwarz 给
$$
\|R_qv\|_\kappa
\le\sqrt{2x}\,e^{\kappa(q+3\sqrt x)}\|R_qv\|,
\qquad v\in H_q.
$$
使用
$$
3\kappa\sqrt x\le\frac{\delta x}{4}+\frac{9\kappa^2}{\delta},
\qquad \frac12\log(2x)\le\frac{\delta x}{4},
$$
以及 (2.7)，得到
$$
\begin{aligned}
\log\|R_q\|_{H_q\to X_\kappa}
&\le(\kappa+\kappa_0)q+\frac{3\delta x}{4}
+\frac{9\kappa^2}{\delta}\\
&\le(\kappa+\lambda)q+\frac{3\delta Q}{4}
+\frac{9\kappa^2}{\delta}.
\end{aligned}
\tag{3.1}
$$
故同一逐层和
$$
Rv=\sum_{q\ge0}R_q\mathsf P_qv
\tag{3.2}
$$
在 $X_{\kappa+\lambda}\to X_\kappa$ 绝对收敛，且
$$
\boxed{
\|R\|_{X_{\kappa+\lambda}\to X_\kappa}
\le\exp\left(\tfrac34\delta Q+\frac{9\kappa^2}{\delta}\right).
}
\tag{3.3}
$$
不同 $\kappa$ 的和在共同定义域上相同，因为它们在原 $H$ 中都是同一列部分和的极限。

## 4. 固定误差从 H 映入所有指数空间

先在 $H_q$ 上定义实际误差
$$
E_q=TR_q-I=\sum_{\ell\ge0}K_{m+\ell}R_q.
\tag{4.1}
$$
第 $\ell$ 项输出次数至多
$$
b=q+d+2m+\ell+1\le2x+\ell.
$$
(2.3)、(2.7) 因而给
$$
\|K_{m+\ell}R_qv\|_\kappa
\le52\sqrt{b+1}
\exp\left(\kappa b+\kappa_0q+\frac{\delta x}{4}
-770\,16^{m+\ell-1}\right)\|v\|.
\tag{4.2}
$$
注意 $770\,16^{m+\ell-1}=48.125\,d^4\,16^\ell\ge48.125\,x^2\,16^\ell$。对 $x\ge64$，
$$
\log52+\tfrac12\log(2x+\ell+1)\le x+\ell.
$$
令 $A_\kappa=2\kappa+\kappa_0+\delta/4+1$。丢掉额外的负余量后，(4.2) 的对数系数不超过
$$
-48x^2\,16^\ell+A_\kappa x+(\kappa+1)\ell.
\tag{4.3}
$$
两项正量分别支付：
$$
A_\kappa x-8x^2\,16^\ell
\le A_\kappa x-8x^2\le A_\kappa^2/32,
$$
$$
(\kappa+1)\ell\le(\kappa+1)4^\ell
\le12x^2\,16^\ell+\frac{(\kappa+1)^2}{48x^2}.
$$
所以 (4.3) 不超过
$$
-28x^2\,16^\ell+c_\lambda(1+\kappa)^2,
\tag{4.4}
$$
例如可取
$$
c_\lambda=\frac{(3+\kappa_0+\delta/4)^2}{32}+\frac1{48}.
$$
这一步没有把线性的 $\kappa\ell$ 误并成随 $\kappa$ 增大的负指数系数。

先对全部 $\ell$ 求和，再对正交输入层 $q$ 使用 Cauchy–Schwarz，得到同一个连续延拓
$$
E=\sum_{q\ge0}E_q\mathsf P_q:H\longrightarrow X_\kappa
\quad(\kappa\ge0),
$$
$$
\boxed{
\|E\|_{H\to X_\kappa}
\le2e^{c_\lambda(1+\kappa)^2}
\left(\sum_{q\ge0}e^{-56(q+Q)^2}\right)^{1/2}.
}
\tag{4.5}
$$
各延拓在稠密的有限次数直和上相同，因此作为 $H$ 值算子也相同。特别，$E(H)\subset\mathscr E_\infty$。

全 Hilbert 范数的小量直接由新估计 (4.5) 支付，不另借旧尺度上的小量。由 Q≥(4lambda+1)/8 得 lambda<2Q；又 kappa0<3、delta<2Q、Q≥64，故
$$
3+\kappa_0+\delta/4<6+Q/2\le Q,\qquad
c_\lambda\le Q^2/32+1/48\le Q^2/16.
$$
在 (4.5) 取 kappa=0，使用 H 范数不超过 X0 范数，以及
$$
\sum_{q\ge0}e^{-56(q+Q)^2}
\le\frac{e^{-56Q^2}}{1-e^{-112Q}}\le2e^{-56Q^2},
$$
即得
$$
\boxed{
\|E\|_{H\to H}
\le2\sqrt2\,\exp[-(28-1/16)Q^2]<\frac14.
}
\tag{4.6}
$$
这里是先对正交输入层使用平方和而得到的全 H 小量；没有把 Xlambda 上的算子范数直接改名为 Hilbert 范数。

## 5. 一个 Hilbert 逆同时保全部尺度

由 (4.6)，同一个
$$
U=(I+E)^{-1}\in B(H),\qquad\|U\|_{H\to H}\le4/3
\tag{5.1}
$$
确实存在。若 $v\in X_\nu$，则
$$
Uv=v-EUv\in X_\nu
$$
由 (4.5) 成立，而且
$$
\|Uv\|_\nu
\le\left(1+\tfrac43\|E\|_{H\to X_\nu}\right)\|v\|_\nu.
\tag{5.2}
$$
所以同一 $U$ 保留每个 $X_\nu$，无需在不同 Banach 空间上另外选择逆。

在 $X_\lambda$ 上定义
$$
\mathcal G_\lambda=RU.
\tag{5.3}
$$
由 (3.3)、(4.5)、(5.2)，对 $\nu=\kappa+\lambda$ 可把所有有限常数吸收到 $C_\lambda$，得到 (1.2)。

实际恒等式也保留完整定义域。对 $v\in X_\lambda$，$R$ 的部分和在 $H$ 收敛，$T$ 在 $H$ 有界，故由 (4.1) 得
$$
TRv=v+Ev.
$$
再用已证的 $Uv\in X_\lambda$，
$$
T\mathcal G_\lambda v=(I+E)Uv=v.
$$
这证明 (1.1)，没有要求 $R$ 在全 $H$ 有界或先假定某个未证明的闭域。

R239 A.8 已付 $T:X_\kappa\to X_\kappa$ 的实际有界性，包含完整 $Y$ 型局部壳和。因此 $\mathcal G_\lambda$ 和 $T$ 连续作用于 $\mathscr E_\infty$；(1.3) 的幂等性由 $T\mathcal G_\lambda=I$ 直接得到。

若 $v\in X_{n\lambda}$，连续应用 $\mathcal G_\lambda$ 经过
$$
X_{n\lambda}\to X_{(n-1)\lambda}\to\cdots\to X_0.
$$
每一步均有实际右逆等式，所以 $T^n\mathcal G_\lambda^nv=v$。范数乘积满足
$$
\|\mathcal G_\lambda^n\|_{X_{n\lambda}\to H}
\le\exp\left(C_\lambda\sum_{j=0}^{n-1}(1+j\lambda)^2\right)
\le\exp\bigl(C_\lambda(1+\lambda)^2n^3\bigr).
$$
这证明 (1.4)。

## 6. 与同一个规范来源及稳定核的准确关系

仍记 $M=\ker T$、$N=\overline{BM}$。旧 R239 A.42 已给
$$
M\cap\mathscr E_\infty\subset N.
\tag{6.1}
$$
简证是：对任意 $w\in N^\perp$，其规范形式解 $T^*h(w)=w$ 在充分大的 $X_\kappa$ 上连续配对；对 $v\in M\cap\mathscr E_\infty$ 有
$\langle w,v\rangle=\langle h(w),Tv\rangle=0$。

对有限整数支撑 $f$，令 $Jf$ 为原有限三角方程 $T(Jf)=f$ 的规范有限支撑解。其存在性来自 $T$ 的首下降系数非零；选择 $(Jf)_0=0$ 后唯一。由 (1.2)，
$$
\mathcal G_\lambda f-Jf\in M\cap\mathscr E_\infty\subset N.
$$
因此对同一个 $w\in N^\perp$，
$$
\boxed{
\langle w,\mathcal G_\lambda f\rangle
=\langle w,Jf\rangle
=\langle h(w),f\rangle.
}
\tag{6.2}
$$
有限整数支撑在每个 $X_\kappa$ 稠密，故 (6.2) 把该同一规范来源表示为 $\mathcal G_\lambda$ 的连续对偶作用。它只是 $X_\lambda$ 上的连续泛函；没有推出 $h(w)\in H$。

原 $B$ 也保每个 $X_\kappa$：它在首个可下降位为 $j$ 的部分，系数为 $\alpha_j$，孔次数改变 $j-1$，所以
$$
\|B\|_{X_\kappa\to X_\kappa}
\le\sum_{j\ge0}\alpha_j e^{\kappa(j-1)}<\infty.
$$
由 $BT=TB$ 及实际右逆等式，
$$
(B\mathcal G_\lambda-\mathcal G_\lambda B)\mathscr E_\infty
\subset M\cap\mathscr E_\infty\subset N.
\tag{6.3}
$$
(6.3) 不授权在含更多 $\mathcal G_\lambda$ 的词中自由交换 $B$，因为未证明 $\mathcal G_\lambda$ 保持 $N$。

本稿没有证明 $M\cap\mathscr E_\infty$ 在整个 $M$ 稠密，也没有证明 $\Pi_\lambda$ 延拓为 $H$ 上有界投影。同一个真实 $W=M\ominus N$ 的 $\Gamma$ 上界、Green 图核心及 $N=M$ 仍未付清。新获得的是固定构造的全指数尺度右逆、全 $H$ 来源的光滑误差和准确的同一规范来源表示。
