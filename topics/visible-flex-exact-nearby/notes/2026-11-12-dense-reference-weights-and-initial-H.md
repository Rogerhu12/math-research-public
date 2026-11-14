# 第一块真实对象射线 reference 的正权与初始 H 误差

2026-11-12，visible-exact-astra-f6a2。

**状态：有限 reference 的两项严格预算完成。** 本文认证保存的
插值函数及其初始值，不认证它与真实 ODE 解的距离，也不将 reference
的导数界解释成真实 Jacobian 界。

环境恢复后源码与trace均重新生成；本稿使用新141段分支，旧142段报告没有被转授。

## 1. 同一冻结分支

使用新 exact-affine 第二步对象的第一块43角 forward trace：

- 141个 accepted 段；
- trace SHA256：60b0cc65c70ff5aafe872a3a405b3402d96792d61e3db34a485cd0b3b7a36492；
- 对象定义 SHA256：aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1；
- tight root 证书 SHA256：c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb；
- 准确 dyadic H SHA256：58375d24a99ba0f43b29143fe22f950a6e74e4fec2b94123d68b078fcf088260。

位置是 data/phase_ring_continuation/exact_affine_step2_dense258/
block_0000_forward.npz.gz。这里的独立报告为同目录
block_0000_forward_reference_weights.json.gz。

## 2. 正权是准确指数多项式

每段保存的 log-J 状态由七阶 DOP853 nested formula 定义一个准确
实多项式 \(L_i(\tau)\)。每个已保存 binary64 系数、时间与 h 都先
还原成 Fraction，不把浮点减法当作准确坐标变换。

选 R60 的参考权
\[
 q_i(\tau)=\exp L_i(\tau)>0,\qquad q_i'/q_i=L_i' .
\tag{W.1}
\]
这个正性来自明确定义，尚未声称 \(q_i\) 等于真实流导数。
若 \(u=(\tau-\tau_i)/(\tau_{i+1}-\tau_i)\in[0,1]\)，准确代入
\[
 z=\frac{\tau-\mathrm{told}_i}{h_i}
 =\frac{\tau_i-\mathrm{told}_i}{h_i}
  +\frac{\tau_{i+1}-\tau_i}{h_i}u .
\]
这保留了 h 与 accepted 时间差潜在的舍入差别。

设转换后的幂系数为 \(L_i(u)=\sum_{j=0}^n a_j u^j\)，\(n\le7\)。
其 Bernstein 系数为
\[
 b_k=\sum_{j=0}^k a_j\,\frac{\binom{k}{j}}{\binom nj}.
\tag{W.2}
\]
因为
\[
 u^j=\sum_{k=j}^n
 \frac{\binom{k}{j}}{\binom nj}
 \binom nk u^k(1-u)^{n-k},
\]
而 Bernstein 基非负、和为1，有
\[
 \min_k b_k\le L_i(u)\le\max_k b_k .
\]
全部系数和比较均在有理数中完成。对
\(L_i'(\tau)=\sum_{j\ge1}j a_j u^{j-1}/(\tau_{i+1}-\tau_i)\)
重复同一计算，再用 Arb 192 bits 对端点指数向外包络。

全部141段、43条 reference 的连续统一界为
\[
 -0.600306009492649
 \le L_i(\tau)\le1.3084045000896738,
\]
\[
 0.5486437202169419
 \le q_i(\tau)\le3.700265227131817 .
\]
这些端点按报告中向外 binary64 数解释；普通十进制安全界可用
\[
 \boxed{\,0.54864<q_i(\tau)<3.70027\,}.
\tag{W.3}
\]
报告保留每个 segment/ray 的 \(L_i,q_i,L_i'\) 区间，后续应优先
用局部较紧界。本文没有计算 R60 的 \(e_1=L_i'-f_\theta\)。

## 3. 准确初始网格与 dyadic H

初始归一角为准确
\[
 x_j=2\pi j/258,\qquad j=0,\ldots,42 .
\]
H 的 Fourier 系数是 JSON 中整数除以 \(2^{80}\)，负系数为共轭：
\[
 H(x)=x+h_0+
 2\sum_{k=1}^{64}
 \{\operatorname{Re}h_k\cos kx-\operatorname{Im}h_k\sin kx\}.
\]
在 Arb 192 bits 下从准确整数与有向 \(\pi,\sin,\cos\) 重算
\(H(x_j)/4\)，再减去 trace 保存的准确 dyadic initial angle。
得到
\[
 \boxed{\quad
 \max_{0\le j\le42}
 \left|\frac{H(2\pi j/258)}4-\theta_{j,\rm saved}\right|
 <3.897835\cdot10^{-17}.
 \quad}
\tag{W.4}
\]
这是对应节点的初始值误差，不是相邻节点之间的复像或整个初值 strip
包络。R60 的连续初值圆盘仍须另供 (60.16) 以及 H 的局部复像界。

## 4. 源、重放与作用范围

验证源 scripts/fourfold_dense_reference_weights.py，SHA256：

5be66a7907bf826f600440e674158e9c7ac9d007d26dd4000202916ad79924ee。

准确 Fraction 到 binary64 的向外转换复用已冻结
fourfold_interval_scalar.py，SHA256：

0400c59be86f7f143481f89d5a08ca8d0ea992be36aa1687ff9a19d10343dda8。

从仓库根执行：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python topics/visible-flex-exact-nearby/scripts/fourfold_dense_reference_weights.py \
      --trace topics/visible-flex-exact-nearby/data/phase_ring_continuation/exact_affine_step2_dense258/block_0000_forward.npz.gz \
      --dyadic-conjugacy topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
      --total-nodes 258 --first-node 0 \
      --out /tmp/visible-forward-reference-weights.json.gz

本包只供给 R60 的参考正权、其对数导数包络及一组准确初值费用。
真实 ODE 的 \(e_0,e_1\)、全管 \(B_2\)、参数二阶源、根误差、
完整无限 primitive 与算术传播仍须计入后续残差证明。
相邻多项式跳跃由另一份准确 Fraction 证书处理。
