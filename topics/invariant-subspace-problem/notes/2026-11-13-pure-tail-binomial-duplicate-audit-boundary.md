# 二项纯尾坏族的去重核查：未发布 b612 不登记新增结果

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d。

本次重做稿 blob `b612394ea5110cf6cb8bbb4d8d453f722b5c1ba2` 未发布、未登记为新结果。继续核查旧文后，确认其二项抵消族、纯尾全源指数障碍与指数常数均由既有 R239 覆盖。它不进入新结论编号。

## 准确重编号关系

沿用 [R239 Chernoff 附录](../results/R239-appendix-actual-boundary-range-threshold-chernoff-refinement.md) 的纯尾
$$
 C_m=D_m^*=\sum_{j\ge m}(j+1)^{-2}E_j^*,\quad
 I=\{m,\ldots,m+q-1\},\quad A_I=\prod_{j\in I}(j+1)^{-2}.
$$
令 $U=C_I$、$V=C_{\rm tail}$，并置
$$
 X_\ell=U^\ell\Omega/\ell!,\qquad Y_k=V^k\Omega/k!.
$$
重做稿使用
$$
 f_{m,q}=\sum_{\ell=0}^q
 \frac{(-1)^\ell}{\binom q\ell}X_\ell Y_{q-\ell}.
$$
旧 R239 §1 的向量则是
$$
 u_{m,q}=A_I^{-1}\sum_{k=0}^q
 (-1)^k\frac{(q-k)!}{q!}X_{q-k}V^k\Omega.
$$
由于 $V^k\Omega=k!Y_k$，取 $\ell=q-k$ 后准确得到
$$
 \boxed{u_{m,q}=(-1)^qA_I^{-1}f_{m,q}.}
$$
因此两稿归一化向量仅差相位 $(-1)^q$。相应的
$D^*f=(q+1)Y_{q+1}$ 也就是旧 R239 (1.1) 的同一恒等式。

重做稿的粗率
$$
 \kappa=(3+\log3)/2
$$
恰等于旧稿已经列明的 $\gamma_0$。旧 Chernoff 估计进一步给
$\Gamma\approx2.360343347>2.36>\kappa$，已严格更强。图模型纯尾权
$(j+2)^{-2}$ 仅需在这个纯尾等式中作位置单位重标号 $r=j+1$；这不允许重编号真实 carry 的 $\eta_j$。

旧 Chernoff 式保留 $R=m+q$ 的准确有限参数，因而其纯尾估计也适用于
$m=o(q)$，包括当前 $m(q)=O(\log\log q)$：整理同一阶乘式即可得
$\|D^*\widehat f_{m,q}\|\le\exp[-\Gamma q+o(q)]$。这只是既有公式的参数范围说明，不另登记新指数障碍。

## 高阶核投影消灭只是旧受限右逆的直接推论

令 $Z_{q,h}=\ker D^h\cap\mathcal H_q$。[R254 第十附录](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md) 的相容 $R_1$ 已给
$$
 DR_1u=u,\qquad
 \|R_1u\|\le h(2R)^h\|u\|\quad(u\in Z_{q,h}),
$$
其中 $R$ 是该稿已支付的有限源层常数。对任意 $\xi\in\mathcal H_q$，配对即得
$$
 \|P_{Z_{q,h}}\xi\|
 \le h(2R)^h\|D^*\xi\|.
$$
所以归一化旧坏族在
$m=O(\log\log q)$、$h=O((\log q)^{1/3})$ 下满足
$$
 \|P_{Z_{q,h}}\widehat f_{m,q}\|
 \le\exp[-\Gamma q+o(q)].
$$
这只把旧受限原像应用到旧坏族；不构成新的无权核心、特殊残量能量界或 $N=M$ 结论。

当前工作继续针对真实特殊源及完整伴随链。不能把全源层的旧坏方向再登记为新障碍，也不能把上述投影消灭冒充对完整压缩 Gram 逆的控制。
