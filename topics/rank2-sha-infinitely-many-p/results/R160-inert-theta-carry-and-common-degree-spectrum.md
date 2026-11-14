# R160 — 实际惰性 theta 首进位与全列次数谱行

- **日期：** 2026-11-12。
- **状态：** 已证明；未得到严格惰性 arithmeticity 预算。
- **对象：** R117/R162 的原平面 $(A_2,B)$ 与原普通系数源
  $\mathbb Z_p[X,Y]_{\le D}$，所有混合列均保留。
- **完整证明：**
  [实际首进位与共同次数谱行](../notes/2026-11-12-inert-theta-carry-and-common-degree-spectrum.md)。

## 准确结果

取 $p=4r-1\ge7$，$W=\log\vartheta^{68}$、
$a_n=[s^n]W'$、$C_p=pa_{r-1}\bmod p\ne0$。有
$$
pW'(s)\equiv C_ps^{r-1}(1-s)^{2r-1}\pmod{p,s^p}.
$$
$pW'$ 的系数到 $p^2-1$ 均整；$W$ 在 $m<p^2$ 最低赋值为 $-1$，
但 $[s^{p^2}]W$ 的赋值是 $-2$。更早的指数进位准确为
$$
p[s^{pr}]\vartheta^{68p}\equiv-C_p/r\pmod p;
$$
该指数在所有更低次数处整。

原整数流满足
$$
\delta^p=\mathfrak c_p\partial_L+\mathfrak bE_\theta,\qquad
\mathfrak c_p=-C_p/(68r)\ne0,
$$
以及全部原源列共同的关系
$$
h_{n+j(p+1)}
 \equiv\mathfrak c_p^j(n+1)^{\overline j}h_nE_\theta^j\pmod p.
$$
$E_\theta$ 在源上的谱为 $68q,\ 0\le q\le D$。
其特征多项式给一条真正相同的前缀行；在相应上升阶乘为单位时，
最高 Hurwitz 行在准确饱和核上被 $p$ 除。
普通 Taylor 行仍须除以最高 $N!$，本文没有省去这个成本。

## 可复跑有限证书

[脚本](../scripts/check-theta-plane-saturated-jets.py) 和
[完整冻结数据](../scripts/check-theta-plane-saturated-jets.json)
用精确有理数、整可逆 kernel 列变换，记录 $D=4,8$ 的七个实际
$(D,p)$ 例子，未施加任何中央消失假设。
它们只是有限诊断；不能据其外推 R159 的严格门槛
$a_I+2b_I<2$。

原中央全失败怎样通过实际 amplitude 改善这些完整饱和格，仍未付清。
