# 实际半权模函数的固定 Siegel-unit 表达

日期：2026-11-12。状态：固定函数、全部相位和有限覆盖已准确确定；
尚未把实际除 $p$ 行与一个已知非零的 Frobenius 值等同。

本篇给
[GM 素数对角公式](2026-11-12-critical-gauss-manin-legendre-lift.md)
中的实际代数模函数 $M_0=F/\vartheta_3$ 一个完整表达。
所有有限角色和常数均在素数变化前固定。

## 1. 规范及准确恒等式

令 $\lambda:(\mathbb Z/17)^\times\to\mu_4$ 满足 $\lambda(3)=-i$，
并置

$$
 F(\tau)=\sum_{17\nmid n}\lambda(n)\zeta_{289}^{19n^2}
                         e^{\pi i\tau n^2/289}.
 \tag{1}
$$

定义 theta characteristic

$$
 \vartheta[a,b](\tau)
   =\sum_{k\in\mathbb Z}
      e^{\pi i\tau(k+a)^2+2\pi i(k+a)b},
 \qquad \vartheta_3=\vartheta[0,0].
$$

本篇 Siegel 函数取以下完整乘积规范，$q=e^{2\pi i\tau}$：

$$
 \begin{aligned}
 g_{r,s}(\tau)
  ={}&-q^{B_2(r)/2}e^{\pi i s(r-1)}
      (1-q^re^{2\pi i s})\\
     &\times\prod_{n\ge1}
        (1-q^{n+r}e^{2\pi i s})
        (1-q^{n-r}e^{-2\pi i s}),\qquad
 B_2(r)=r^2-r+\tfrac16.
 \end{aligned} \tag{2}
$$

指数 $r,s$ 不先约化模 $\mathbb Z$；这是保留根单位相位所必需的。
所有 $q^a$ 均指 $e^{2\pi i a\tau}$。该规范及整数平移公式可核于
Koo–Shin（2010），*Function fields of certain arithmetic curves and application*，
Acta Arith. 141.4，式 (2.1)、Proposition 2.1，印刷页 323；
[出版方全文](https://www.impan.pl/shop/en/publication/transaction/download/product/83037)，
DOI [10.4064/aa141-4-2](https://doi.org/10.4064/aa141-4-2)。

准确结论为

$$
 \boxed{\quad
 M_0(\tau)=\frac{F(\tau)}{\vartheta_3(\tau)}
   =\sum_{r=1}^{16}\lambda(r)\zeta_{68}^{4r^2+3r}
      \frac{g_{(17+2r)/34,(17+8r)/34}(\tau)}
           {g_{1/2,1/2}(\tau)}.
 \quad} \tag{3}
$$

这不是只在 CM 点成立的数值式，而是在整个上半平面成立的函数恒等式。

## 2. 相位的逐步证明

把 (1) 按 $n=r+17k$ 分组。
$19(r+17k)^2/289$ 的交叉项模整数为 $4rk/17$。
而 characteristic theta 还含常数相位 $4r^2/289$，所以

$$
 F(\tau)=\sum_{r=1}^{16}
        \lambda(r)\zeta_{289}^{15r^2}
        \vartheta[r/17,4r/17](\tau).
 \tag{4}
$$

Jacobi 三重乘积给

$$
 \vartheta[a,b]
 =q^{a^2/2}e^{2\pi iab}
   \prod_{n\ge1}(1-q^n)
    (1+q^{n-1/2+a}e^{2\pi ib})
    (1+q^{n-1/2-a}e^{-2\pi ib}).
$$

代入 (2) 的 $r=a+1/2,s=b+1/2$。
由于 $B_2(a+1/2)=a^2-1/12$，所有 $q$ 的额外幂与 $\eta$ 的
$q^{1/24}$ 恰好抵消，得到

$$
 \vartheta[a,b]
 =-e^{\pi i(ab+(b-a)/2+1/4)}\eta\,
          g_{a+1/2,b+1/2}.
$$

除以 $a=b=0$ 的同一公式，准确有

$$
 \frac{\vartheta[a,b]}{\vartheta_3}
 =e^{\pi i(ab+(b-a)/2)}
        \frac{g_{a+1/2,b+1/2}}{g_{1/2,1/2}}.
 \tag{5}
$$

在 (4) 中取 $a=r/17,b=4r/17$。总相位的 $2\pi i$ 指数是

$$
 \frac{15r^2}{289}+\frac{2r^2}{289}+\frac{3r}{68}
       =\frac{4r^2+3r}{68},
$$

即得 (3)。另用 90 位精度在 $\tau=i$ 与 $\tau=0.12+1.13i$
进行了非严格数值排错：截断 Gaussian 和、characteristic theta 和、
Siegel 乘积的数值差小于 $10^{-80}$。这里未将浮点差或截断误差认定为
认证输入；证明完全来自上述准确乘积恒等式。
可复算的短脚本为
[check-siegel-theta-resolvent.py](../scripts/check-siegel-theta-resolvent.py)。

## 3. 一个明确固定的代数覆盖

令 $N_0=34$，并记 (3) 中的十六个单位比为 $s_r$。
同一出版原文的 Proposition 2.1 给

$$
 g_a\circ\gamma=\epsilon(\gamma)g_{a\gamma},\qquad
 g_{a+h}=(-1)^{h_1h_2+h_1+h_2}
 e^{-\pi i(h_1a_2-h_2a_1)}g_a.
 \tag{6}
$$

其中 $\epsilon(\gamma)$ 与指标 $a$ 无关，因此在单位比中消去。
若 $\gamma\equiv I\pmod{2N_0^2}$，则对 $a=j/N_0$ 有
$a\gamma=a+2N_0jB$，后面的整数平移在 (6) 中的相位准确为 $1$。
故每个 $s_r$ 是 $\Gamma(2N_0^2)=\Gamma(2312)$ 上的模函数。
其 cusp 展开也在固定分圆数域中：由 (2)，指数分母除 $2N_0^2$，
常数相位和系数均在 $\mathbb Q(\zeta_{2N_0^2})$。
因此 (3) 已在一个明确、固定的模曲线上实现，而不是随 $p$ 重选覆盖。

也可使用较小的基础曲线和根扩张：Proposition 2.3（同文印刷页 324）
给 $g_a^{12N_0}\in\mathcal F_{N_0}$，所以

$$
 U_r=s_r^{408}\in\mathcal F_{34}.
 \tag{7}
$$

在 $Y(34)$ 上加入指定的 $408$ 次根 $s_r$，便得到另一个固定有限覆盖。
所有 $U_r$ 都是 modular units；在特征零去 cusp 的曲线上，该根覆盖
是 étale 的。这里不额外声称某个未经计算的整模型已经只在
$2,3,17$ 处有坏约化。

在 CM germ $t=\lambda_{\rm Leg}-1/2$ 上，(3) 有二阶零点。
除以固定的非零 $t^2$ 系数 $m_2$ 后，得到原 GM 公式的
$M=M_0/m_2=t^2+O(t^4)$。因此新表达保留的是原来的实际 $M$。
特别在 $\tau=i$，characteristic 的非平凡 $17$ 部分所指的点为

$$
 \frac{\tau+4}{17}\bigg|_{\tau=i}
       =\frac1{4-i},
$$

与实际 $17$-同源 theta 构造的 CM 核一致。

## 4. 固定单位 Frobenius 商与实际目标的接口

取一个使上述固定覆盖、CM 分支都整且 $m_2$ 为单位的好位 $p\ge7$，
并在包含所需常数的非分歧局部扩张中工作。
在形式盘上取系数 Frobenius $\sigma$，并明确规定
$\phi(s)(t)=\sigma(s)(t^p)$，即逐系数作用 $\sigma$ 后代入 $t^p$。
每个 $s_r$ 是单位 germ，故

$$
 E_{r,p}(t)=\frac{\phi(s_r)/s_r^p-1}{p}
      \in\mathcal O_p[[t]].
 \tag{8}
$$

令 $c_r=\lambda(r)\zeta_{68}^{4r^2+3r}$。
因 $p\nmid68$，有 $\sigma(c_r)=c_r^p$，所以由 (3) 得准确等式

$$
 \frac{\phi(M_0)-M_0^p}{p}
 =\sum_r c_r^p s_r^p E_{r,p}
  -\frac{(\sum_r c_rs_r)^p-\sum_r c_r^p s_r^p}{p}.
 \tag{9}
$$

右侧第二项是完整的整系数交叉多项式，不能丢弃。
这是一个真实、有限的单位 Frobenius 商表达，且十六个函数都已明确指定。

但它还不是实际的 GM 除 $p$ 行。一个准确的检验是：由于
$M_0\in t^2\mathcal O_p[[t]]$，

$$
 \frac{\phi(M_0)-M_0^p}{p}\in t^{2p}\mathcal O_p[[t]].
 \tag{10}
$$

所以其 $t^{(p+1)/2}$ 系数恒为零。对归一化的 $M$ 也一样。
实际目标还包含

$$
 [t^{(p+1)/2}]
 \left(Z+\frac12W\log(K/J)\right),\qquad
 W=\frac{M}{(1-4t^2)J^{3/2}},\quad (2t\partial_t-1)Z=W.
$$

因而要从 (8)–(9) 得到实际有限秩 Frobenius/Bockstein 比较，
必须同时保留参考周期、连接及除 $p$ 的指定 jet。
仅对 $M$ 或单个单位使用 Frobenius 商，不能把 (10) 的零式改读成
原目标的非零证书。
