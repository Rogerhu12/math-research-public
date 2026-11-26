# R150 / S0 / Lt0：排除两个孤立权重相等，并合法消去同一 eta

状态：**已证明**。整个 $U=ek+2e-2=0$ 原曲线为空；因此原配对式中的 $B$ 也是单位，可在一般剩余 Lt0 上唯一重构同一个 $\eta$，并由原二次式 $Q_a$ 精确恢复原范数。此结论服务于一般图的完整原 $N/P$ 返回；没有排除一般 Lt0。

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）。

## 1. 待支付的唯一除法边界

原坐标满足

$$e=u-1,\quad k=Q/e,\quad j=k+2-2e,\quad \ell=j/k,$$

$$u-\ell=\frac{ek+2e-2}{k}=\frac Uk.$$

在原 $p+q=2,p\ne q$ 规范中，$u=bp+cq$、$\ell=b+c$，所以

$$u-\ell=(b-c)(p-q)/2.$$

因此 $U=0$ 恰是两个孤立权重 $b=c$ 的整支。其解出式

$$k=\frac{2-2e}{e}$$

只使用已付单位 $e$。

依[原同eta系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-same-eta-four-monomial-original-system.md)，取原 Cramer 必要式 $P_{045},P_{035},P_{034}$ 及新同 eta 必要四次式 $Q_4$。自含源从原 Frobenius Gram、原三个 mean 及分别的原 $N/P$ 重建这些式；$Q_4$ 的原来源仍是不除以 $B$ 的身份

$$D Q_a=M_a(UD+2j\eta B)+2B^2M_n,$$

其中

$$M_a=UD-2j\eta B,\qquad M_n=Z_d\eta^2-(1-ek)D,$$

$$Z_d=2j^2,\qquad Q_a=U^2D-2(1-ek)B^2.$$

故本条在 $U=B=0$ 上也合法，不预用待证单位。

## 2. 整条曲线的原有理返回

每个原三参数多项式 $p$ 先按 $m=\deg_kp$ 清除已付分母，并逐项核验

$$e^m p(e,k,v)-\widehat p(e,v)=U\,h(e,k,v).$$

随后只剥除已付的 $e,e+1,e-1,2e-1,v$ 因子并乘回。得到四个原必要多项式，其 $(e,v)$ 次数分别为

$$ (23,6),\quad(28,6),\quad(30,6),\quad(21,4), $$

项数分别为 $103,133,143,69$。将第一个与后三个分别取完整 $v$ 结式，得到三个非零 $\mathbf Q[e]$ 多项式 $R_1,R_2,R_3$，次数为

$$234,\qquad245,\qquad168.$$

没有除以任何 $v$ 首项，所有降次纤维都保留。实际有理 Euclid/Bézout 组合成单一原三输入身份：

$$S_1R_1+S_2R_2+S_3R_3=e^{28}(e-1)^{26}(e+1)^{38}(e+\tfrac12)^3,$$

$$\deg S_1=118,\qquad\deg S_2=107,\qquad\deg S_3=102.$$

源逐项乘回；三个系数的合并 SHA-256 为

`4f61e65e0c67322c1ca6136b7eaab6d56cb0466a44223b24e1e59321f8b703cb`。

$e=0,1,-1$ 已由原单位和零基点权重整支排除。唯一其余根 $2e+1=0$ 也不可能，因为源在原参数环核出

$$e(4e-k-4)+U=2(e-1)(2e+1).$$

在 $U=0$、$e=-1/2$ 上，这迫使 $4e-k-4=0$，即已排除的半权整支。于是整个 $U=0$ 曲线为空。

## 3. 同一点、同一 eta 的原范数重构

剩余一般图上 $U$ 与 $D=2j^2\Delta_U$ 都非零，其中 $\Delta_U=(h-k)^2$ 来自已排除的原U值碰撞；它不是配对判别量 $1-Q$。原 $M_a=0$ 给

$$2j\eta B=UD\ne0.$$

因此 $B\ne0$，并且原 eta 唯一为

$$\eta=\frac{UD}{2jB}.$$

这一个重构必须同时用于所有原矩、配对、normal 和最高值方程。它没有独立选择范数的另一个根。

令 $n=UD,d=2jB$。源在原多项式环中还核验

$$M_a=n-d\eta,$$

$$Z_dn^2-(1-ek)D d^2=Z_d D Q_a.$$

所以在已付的 $d\ne0$ 图上，原配对式加原范数式与

$$\eta=n/d,\qquad Q_a=0$$

严格等价：原式推出 $Q_a$ 使用已付 $D$；反向代入的范数分子恰为 $Z_dDQ_a$。任何另外对 eta 一次的原式 $P_0+P_1\eta=0$ 都可精确转为

$$dP_0+nP_1=0,$$

分母只为同一个已付 $d$。因此原 $N(V)$ 以及分别的 $N_B/P_B$ 奇分量可以在不丢失嵌入的前提下返回五个变量 $(e,k,\lambda,f,v)$。原三个二次 mean、U 矩、偶分量和全部其他必要约束仍须保留。

## 4. 实际执行

自含源：`notes/2026-11-27-unit211-S0-Lt0-equal-singleton-weights-original-return-8542.py`。

- 30,610 字节，SHA-256 `c85369cf7679912846a143c019dae763dbf8a288a23d3ad25d46e0eebb523f09`。
- 无参数；Python 3.12.14、python-flint 0.9.0；60 秒 alarm、4 GiB 地址空间上限。
- 实际退出码 0；外部墙钟 4.246669 秒、源内 4.144809 秒，最大 RSS 53,892 KiB。
- stdout 22,265 字节，SHA-256 `aa17261355dcccddb61c74b8a81442188e4186a55c3b801953005115a416d634`。
- 回执：`notes/2026-11-27-unit211-S0-Lt0-equal-singleton-weights-execution-8542.json`。

本条补齐同 eta 消元真正需要的除法边界。一般 S0/Lt0、原全临界理想幂来源与普通 Hilbert ISP 仍未完成。
