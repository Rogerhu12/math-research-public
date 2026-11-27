# 原正支 five-old 的唯一四次有理迹

2026-11-27；Astra-rank2-Sha-0b097461-20261127。

本页完成原算术线已推到的唯一有理迹。它不是新的谱枚举；
完整625项到25项以及原theta lift的来源证明接在
[原unitary字](2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)。
本页独立给出迹的准确值、可乘开的整数恒等式和唯一公开执行回执。

## 1. 完整商环与精确值

置
$$
q_b(X)=5X^4+380bX^3-240b^2X^2-1600b^3X-256b^4,
$$
$$
f_b(X)=(X+4b)(7X^2-4bX+16b^2)
       (X^3-96bX^2+48b^2X+64b^3),
$$
并在整个四维有限代数上取迹
$$
T_b=\operatorname{Tr}_{\mathbf Q[X]/q_b}
       \frac{f_b(X)}{Xq_b'(X)^2}.
$$
原输入为 $b=17$。没有挑选一个根或删去某个轨道。
$q_b$ 可分且 $Xq_b'$ 为单位；下述实际消费者给完整
Bézout 等式及全部回乘。原来源中亦可由非零5除点的
四个自由 $\mu_6$ 轨道看出可分性。

令 $q=q_1,f=f_1$。直接展开可核
$$
\boxed{
60f=Xq'(832-96X-204X^2-5X^3)
 +q(-960+80X+520X^2+20X^3).
}
$$
因此 $f/(Xq')$ 在商环中唯一的三次余式，其 $X^3$ 系数为
$-1/12$。对任一次数小于4的 $g$，Lagrange 插值的最高系数给
$$
\sum_{q(\alpha)=0}\frac{g(\alpha)}{q'(\alpha)}
 =\frac{[X^3]g}{5}.
$$
用前述余式作 $g$，立即得到
$$
\boxed{T_1=-\frac1{60}.}
$$
又 $X=bZ$ 下 $q_b=b^4q_1$、$q_b'=b^3q_1'$、
$f_b=b^6f_1$，故完整迹满足
$$
\boxed{
T_b=-\frac1{60b},\qquad T_{17}=-\frac1{1020}.
}
$$

算术线的原Miller/5-kernel规范给的待合并来源式为
$m_0/\delta=-T_{17}/42$ 和 $c_+=2T_{17}/3$；
代入的准确数值分别是
$$
\frac{m_0}{\delta}=\frac1{42840},\qquad
c_+=-\frac1{1530}.
$$
这里的数值不以新源全质量零删掉5-new或p-new补项；
完整来源分解仍必须保留。

## 2. 唯一公开回执

[完整消费者](../scripts/check-original-positive-five-old-quartic-trace.py)
只用有理数。对每个整个分母返回 Bézout 等式，保完整
四维乘法矩阵的迹，并用独立的 Lagrange 余式身份核回。
实际 $b=1,17$ 的同质缩放亦一致。没有新素数扫描或高维谱执行。

- run **46036879390**，job **140634410835**。
- source **4e827843bcee23a6a7bebf78528b59a69871e0ab**。
- 2026-11-27 **16:49:56 UTC** 返回 PASS。
- 源4964B，SHA256 **0a315b319001a1f0b5ff3dfcedbd0e619059bd494529f8478312caafd3f82f75**。
- stdout1176B，SHA256 **63ded7037646bb2ffd8e40c3ea5845159f61c85e8b36ac8b97b28bb1f8eaeea0**。
- 已读完整job log9336B，SHA256 **5ad23ec4bbeb38f5527b1c24c4059eba597633032fc00f46cae1a4d9da0b98a1**。

计算只在公开Actions；不保存可重算输出或矩阵。
本页第一节的整数恒等式另由逐项手算得到，已把实际有理值写成
不依赖再次执行的短证明。
