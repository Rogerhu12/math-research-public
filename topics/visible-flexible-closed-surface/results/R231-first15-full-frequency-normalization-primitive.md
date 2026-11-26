# R231 — 前 15 格正确去均值 primitive 的完整归一化证书

2026-11-26，Astra-visible-flex-6a65e705-20261126。

本条在 [R229](R229-new-gap-first15-exact-integral-normalization.md) 的同一个准确归一化场上收紧完整角逆预算。原场、准确椭圆周长初值 $f(0)=a_\ell$、全部 Fourier 系数和全部径向格均不变。实际连续证书给出

$$
\|\widehat g-g_f\|_{g_f}\le
\frac{11630602951591819629317}{39614081257132168796771975168}
<2.936\times10^{-7}<10^{-6},
$$

$$
\max|\widehat\kappa_i|\le
\frac{781816760821481612350249209927}{79228162514264337593543950336}
<9.867915<1000/97.
$$

所有前 15 格都通过。第 0 格给出最大度量上界，第 8 格给出最大曲率上界。末端第 16 格的非多项式 coast 端口 repair 仍不在本条范围；literal 有限求积 consumer、准确等距、全闭 reach 和全时族均未被声称完成。

## 1. 必须扣除的 native 角均值

沿用 R229 的 $q=|Y_\theta|$、$a=\operatorname{mean}_\theta q$、$p=f/a_\ell$、$\ell=(A^2\sin^2\theta+B^2\cos^2\theta)^{1/2}$，并写

$$
r_G=q^2-p^2\ell^2,\quad
e=q_s-(f_s/f)q,\quad m=\operatorname{mean}_\theta e.
$$

准确角逆 $\int_0^\theta q=au$ 满足

$$
W=q\theta_s
=um-\int_0^\theta e
=-\int_0^\theta H,\qquad
H=e-\frac qa m.
$$

因此被积函数必须减去 $(q/a)m$；在 native $\theta$ 中仅减常数 $m$ 会漏项。$H$ 的完整圆周积分恰为零。

定义保留取消的准确分子

$$
N=pG_s-2p_sG=p(r_G)_s-2p_s r_G,\qquad G=q^2,
$$

及

$$
e_0=\frac{N}{2p^2\ell},\quad
h=\ell/a_\ell,\quad
H_0=e_0-h\,\operatorname{mean}_\theta e_0.
$$

因为 $\operatorname{mean}h=1$，$H_0$ 也准确去均值。令 $R=N/\ell$，则

$$
H_0=\frac{R-hR_0}{2p^2}.
$$

这就是源码实际消费的式子；$R_0$ 是完整 Fourier 常数项。

## 2. 准确椭圆 Fourier 余项

设 $c=(A+B)/2$、$\zeta=(A-B)/(A+B)\in(0,1)$、$z=e^{2i\theta}$。准确因式分解为

$$
\ell=c(1-\zeta z)^{1/2}(1-\zeta z^{-1})^{1/2},
\qquad
\ell^{-1}=c^{-1}(1-\zeta z)^{-1/2}(1-\zeta z^{-1})^{-1/2}.
$$

两类单边系数从 $a_0=b_0=1$ 出发，按准确有理递推

$$
a_n=a_{n-1}\zeta\frac{2n-1}{2n},\qquad
b_n=b_{n-1}\zeta\frac{2n-3}{2n}.
$$

保留 $0\le n\le64$；每条遗漏尾的绝对和不超过首遗漏项绝对值除以 $1-\zeta$。若已保留绝对和为 $S$、尾界为 $T$，双边乘积遗漏的 Wiener 范数不超过 $2ST+T^2$，再乘各自的 $c$ 或 $c^{-1}$。

有限乘积系数是准确有理数；源码逐项舍入到 $2^{-180}$ 并把实际舍入误差加回。$h$ 还支付准确 $a_\ell$ 区间的除法误差。其常数项直接设为准确的 $1$；此操作删去该项误差，不增大先前完整误差界。

得到有限 Laurent 多项式 $L^\flat,h^\flat$，满足

$$
\|\ell^{-1}-L^\flat\|_{\mathcal A}<4.3000\times10^{-17},
\qquad
\|h-h^\flat\|_{\mathcal A}<2.5291\times10^{-19},
$$

其中 $\|\sum c_ke^{ik\theta}\|_{\mathcal A}=\sum_k|c_k|$。实现以 $|\Re c_k|+|\Im c_k|$ 作向上界。又 $\|\ell^{-1}\|_{\mathcal A}=1/B$，因为其准确 Laurent 系数均非负。所有解析尾都保留；没有把 64 项截断当准确椭圆。

## 3. 全频整数卷积和 $1/|k|$ primitive

每格原位置实 Fourier 次数为 384，径向次数为 5。源码对全部系数作准确整数 Kronecker 卷积，得到完整 $G$ 的 Fourier 次数 768、径向次数 10。没有先把高频 $G_s$ 绝对和粗放大。

目标 $p$ 仍使用 R227 的 $2^{-200}$ 多项式系数包含及准确参数误差。构造保留取消的分子 $N$ 时，局部径向幂 $t^i$ 的 $G_i$ 和 $t^j$ 的 $p_j$ 只贡献

$$
(i-2j)p_jG_i\,t^{i+j-1}/L.
$$

所得径向次数为 19。物理格长 $L$ 的倒数保留在外置准确有理因子中。若 $N^\flat$ 为这个有限多项式，则

$$
\|N-N^\flat\|_{\mathcal A}
\le \delta p\,\|G_s\|_{\mathcal A}
+2\delta p_s\,\|G\|_{\mathcal A}=:\delta_N.
$$

每项范数均由完整径向 Bernstein 控制点和全频绝对和给出。形成

$$
R^\flat=N^\flat L^\flat,\qquad
T^\flat=R^\flat-h^\flat R^\flat_0.
$$

其 Fourier 次数不超过 $768+128=896$，而 $T^\flat_0=0$ 在整数层面逐个径向幂准确成立，源码对此断言。

若 $\beta_{i,k}$ 是 $T^\flat$ 在第 $i$ 个径向 Bernstein 控制点的 Fourier 系数，计算

$$
P=\max_i\sum_{k\ne0}\frac{|\Re\beta_{i,k}|+|\Im\beta_{i,k}|}{|k|}.
$$

所有频率的 $1/|k|$ 都在取绝对和之前保留。源码通过 $\operatorname{lcm}(1,\ldots,896)$ 使加权和仍为准确整数运算，并用准确二项式 Bernstein 转换，未以角采样近似此和。

由于 $|e^{ik\theta}-1|\le2$，以及 $H_0$ 中的分母 $2p^2$，两个因子 2 抵消，得到主部 primitive 上界 $P/p_*^2$；本 ramp 上 $p_*=1$。

令 $R^\flat_0$ 的径向准确上界为 $M_0$，$h$ 的完整 Wiener 上界为 $M_h$。完整误差按

$$
\delta_R\le\delta_N/B+\|N^\flat\|_{\mathcal A}
\|\ell^{-1}-L^\flat\|_{\mathcal A},
$$

$$
\delta_T\le(1+M_h)\delta_R
+\|h-h^\flat\|_{\mathcal A}M_0
$$

支付。真正 $R-hR_0$ 和 $T^\flat$ 都无常数项，所以该误差的 primitive 增量不超过 $\delta_T/p_*^2$。

## 4. 从 $1/\ell$ 主部回到准确 $1/q$

沿用 R229 的 $\varepsilon_0,\varepsilon_1,q_*,\rho,a_*$，取 $p^+\ge p$、$p_1^+\ge|p_s|$，则

$$
|N|\le p^+\varepsilon_1+2p_1^+\varepsilon_0=:M_N.
$$

由 $e=N/(2pq)$、$e_0=N/(2p^2\ell)$，以及 $q^2-p^2\ell^2=r_G$，有保守上界

$$
|e-e_0|
\le
\frac{M_N\varepsilon_0}
{2p_*q_*B(q_*+B)}
=:\epsilon_d.
$$

这里使用 $p_*=1$；若分母保留额外的 $p$ 因子只会使上界更小。同时

$$
\left|\frac qa-\frac{\ell}{a_\ell}\right|
\le \frac{\rho}{a_*}\left(1+\frac A{a_{\ell,-}}\right)=:\epsilon_h.
$$

完整均值先单独认证：

$$
|m|\le\frac{M_0+\delta_R}{2p_*^2}+\epsilon_d=:M_m.
$$

因此

$$
|H-H_0|
\le\left(1+\frac A{a_{\ell,-}}\right)\epsilon_d+\epsilon_h M_m.
$$

两者都准确去均值，沿较短的互补圆弧积分，完整剩余 primitive 不超过 $\pi$ 乘此上界。最终

$$
|W|\le
\frac{P+\delta_T}{p_*^2}
+\pi\left[
\left(1+\frac A{a_{\ell,-}}\right)\epsilon_d+\epsilon_h M_m
\right].
$$

全部 15 格的 $W$ 上界最大值小于 $5.107\times10^{-10}$。这一小量不意味着 $m$ 同样小；最大 $m$ 上界约 $3.10177\times10^{-8}$，源码明确保留它。

## 5. 完整归一化预算的消费

R229 的全部中心导数、位置速度扰动、完整 $E/F/G$ 和实际二阶曲率公式继续适用。本次只把角逆速度换成以上 $W$，并在

$$
\lambda_s=-\lambda m/a,\qquad
\lambda_{ss}=\lambda(2m^2/a^2+(f_s/f)m/a-m_s/a)
$$

中使用新的 $M_m$。$|m_s|$ 仍由 R229 完整 $\eta_1$ 控制，$C_s,C_{ss}$ 仍保留完整 $\eta,\eta_1$。没有为了使角逆界好看而删去真实均值导致的缩放导数，也没有以原场曲率冒归一化场自身曲率。

所有最终四则运算、平方根和门槛比较继续用 96-bit 定向整数区间。本文开头给出的两个严格有理数是完整计算的最终结果。

## 6. 本次真实执行

源码 [6a65-geometry-ramp-normalization-primitive.py](../scripts/6a65-geometry-ramp-normalization-primitive.py)，18381 bytes，SHA256 为 a0feeb59db257e1217b38dc433da9a8c45712dd537f0402c559e7ceb55714def。

实际完整进程自然 exit **0**，239.681831227 s，峰值 RSS **74400 KiB**；15 格全部通过。单格 pilot 只用于核新接线，完整结论来自后续全部 15 格的独立实际执行。

| 身份 | SHA256 |
|---|---|
| 同一 ramp master | 0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7 |
| R227 本次输入恢复报告 | be0c2ad9610bc6a63edf1e6eced42f82a22fb8ed2c73f65412f017c14fb71d3e |
| R228 本次输入恢复报告 | c8f43da932ec21d9925e358b1a025c1e38df067a4ed96e3384d9eeb6c53af48e |
| 完整新 report | fa374672e0c876b618b24980472d438ab59832476a0eba49f802388216c69881 |
| stdout | 789264ef14d424eeab55c2ee9b09dcb4b382b53cc10465adf3f880fdff8584b1 |
| 外部 process receipt | 5e1db5d0a76b8b699052825d0a90e23577e59d06778f997d7796535419dc6e8e |

同一 source/master/输入证书在进程中绑定 SHA，准确卷积沿用 R227 的独立 signed-complex fixture。原件恢复不是新结论；本条新增的是正确加权去均值及全频 primitive 对同一完整归一化场的连续收紧。第 16 格、实际尾连接和全时闭族仍继续。

