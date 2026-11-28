# W native 十三个实际支付原子的来源与正确 mean 静态核对

日期：2026-11-28 UTC。会话：Astra-ISP-8542378f-20261127。
本页只追踪既有定理和冻结源的定义，不重算、不重跑、不新增结果门。
这里列的是 native 构造实际使用的十三个原子，不缩减当前物理 W
原域的其它既有条件；尤其 J19 的完整适用域仍以其正式定理为准。

## 1. 十三个原子的逐项来源

令 $u=e+1,Q=ek,V=(e+1)k+2$。所有结果路径均相对本课题 `results/`。

| 原子 | 原因及正式来源 |
|---|---|
| $e$ | $e=u-1$；[整个 u=1 排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-complete-exclusion.md)，2026-11-26 原完整 Gram 归约。 |
| $k$ | $k=Q/e$；$e$ 已付，$Q=pq$ 为原非零配对。原范围见[原 U 值 atlas](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)及[一般 Delta0 单首项值图](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-global-monic-value-quadratic.md)第 1 节。 |
| $u$ | 原非零孤立均值图的单位；同上两个原范围，非新排除或新 compact 条件。 |
| $ek-1$ | $Q-1=-\rho^2$；原配对互异，沿原 atlas 与共同尺度图。 |
| $V$ | $u(Q+2)-2=eV$；[整个 W 首项零面排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-W-leading-zero-exclusion.md)使前者为单位。 |
| $k+4$ | 原权恒等式 $\Phi=-2e^2(k+4)/V$；Delta0 图中 $\Phi$ 已由[原 P1 双系数零整支](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-P1-double-zero-and-weighted-moment-coordinates.md)支付，准确逻辑又列于 W 首项零面第 1 节。 |
| $\operatorname{num}P_{02}$ | 原最高值 $P_{02}=2P_0\ne0$，原 atlas 已付；当前有理式的分母只含先前权单位。 |
| $\operatorname{num}M$ | $M=4bc(1-Q)$，$bc(1-Q)$ 属原 unit211 物理单位；不是把一个二次范数直接支付。 |
| $k+1$ | [整个 k=-1 权线排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-W-kminus1-exclusion.md)。 |
| $H_{\rm old}=4ek-k^2-4k-8$ | [整个 H=0 的完整原返回](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-H-zero-complete-original-exclusion.md)，其原六列 F29 覆盖及整 C3/F26 返回；并非 H198。 |
| $k+2$ | [整个一般等权 b=c 排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md)支付 $\ell-u$；准确身份 $(\ell-u)kV=u(k+2)(2-Q)$ 于是支付 $k+2$。 |
| $J_{19}$ | [整个余 W 的 J19 排除](../results/R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md)，完整 F568 有限自由模型及 F20 五 QQ 低域返回。其正式范围及其它既有权条件全部保留。 |
| $C_9$ | [整个 C9 原排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)，包含二次扩张、所有范数零支及有限返回。 |

这些来源没有使用本次发现有缺口的 compact R2 / compact mean(1) 文件。
下面给出本次有针对性检查的原定义证据；不以“日期较早”替代定义核对。

## 2. 原 mean 的准确检查

原四维乘法的 jet 分量为
$(vw)_1=v_0w_1+v_1w_0$。所以正确原均值项是
$-2(d^2)_1=-4d_0d_1$，而非 $-2d_1^2$。

### 2.1 原 W 首项、k=-1 与 P1 双零

以下实际自含 Python 源均已静态读到完整正确乘法：

- W 首项零：
  `2026-11-27-unit211-generic-LS-Delta-zero-W-leading-zero-original-return-8542.py`，
  SHA `3769e6d602dd3c153e33991f15cd04d97f0b9cbbc6010666611f777ccee2c397`。
- k=-1：
  `2026-11-27-unit211-generic-LS-Delta-zero-W-kminus1-original-return-8542.py`，
  SHA `43393adf1bd9190a6c361ec6750f4e96716086727d9f02035b0d301410450cb7`。

两者原 mean 逐字都是
`return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]`。

P1 双零源
`2026-11-27-unit211-generic-LS-P1-double-zero-original-return-8542.py`，
SHA `7001773497aeb492055b8e2ac6d63d8c044c0f5af937b2997aebadad627dc5f7`，
直接形成完整向量
`EE=va(va(ev,vs(-2,DK(d))),va(vs(-2,vm(d,d)),vs(2*F2,d)))`。
没有使用错误 scalar square 替换。

### 2.2 H_old 整支的嵌入 JS 原 Gram

`2026-11-27-unit211-generic-LS-W-H-zero-complete-original-return-8542.js`
SHA `b1f2e6d113f6934f3003d51d08bcb36e7a9818fa898386da7f13d867540156ef`。

本次只解读其中嵌入的原 Gram 源字符串，未执行它。
`W0_H_full_affine_build_JS` 的 SHA 是
`d5442db8ef5488c2c164165fd5a02921ab27abcacd7ef0fd06a6efc4d39f76d4`，
完整原行使用

~~~javascript
function mean(j){
 const first=j===1?tau(vm(gr[0],gr[1])).scale(2):tau(vm(gr[j],gr[j]));
 return first.sub(kd[j].scale(2))
  .sub(vm(dv,dv)[j].scale(2)).add(F2.mul(dv[j]).scale(2));
}
~~~

随后直接以 `mean(1),EBe,EBo,N1,NS,PS` 作原六式。
因此虽然这是旧 JS 源，它也不包含后来 compact 中的错误。

### 2.3 等权的原 Gram

`2026-11-27-unit211-equal-weight-original-affine-quadratics-8542.js`
SHA `88914af76ec66403312723ef45d12c2a503553007353e33d9e4774e90b7ccff1`，
原 mean 亦明确使用 `vm(dv,dv)[j]`；
同一个原 N4/P2 使用完整 `vm`，无 compact 依赖。

整负半权的自含 Python
`2026-11-27-unit211-equal-weight-negative-half-complete-original-return-8542.py`
SHA `5063af65da86c69b5d89dfd595e5a885f5b16443edd4683097e0d84f61c52e33`，
也直接使用 `vm(d,d)[j]`。
整个等权的其它已刊边界及合成仍按其正式完整证明引用，不在此重算。

### 2.4 整 C9 的原 Gram 和低域

整合源
`2026-11-27-unit211-generic-LS-W-C9-complete-original-certificate-8542.py`
SHA `9c3ff9f47c67e04bd5dad62c2de810828bf9d625729c08c4e7f0c25e04e1e45b`。

只静态解读其组件字符串即可看到：

- `original_Gram_head_atlas` SHA
  `cc3d0ac5db03437d7b86e5c3a8424f9c1128feebd3c0d3dbba2305f15db43a25`；
- `low_norm_original_Gram_return` SHA
  `c96f236a9d0091434dc082383abf88bda6ca1b3456b17b5e224e0647676a4e4f`。

两个独立原 Gram 入口都用
`return first-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]`。
所有组件均没有 compact-all-means 或 two-means 依赖。

### 2.5 整 J19 的高低入口

原四次全域源
`2026-11-27-unit211-generic-LS-W-J19-quartic-six-generator-original-finite-cover-8542.py`
SHA `f43664bf12637f8add0a01589a854d2cafe22a2711b7dfd826752f90831aa784`
直接使用 `vm(dv,dv)[j]`。

高域源
`2026-11-27-unit211-generic-LS-W-J19-entire-F588-original-finite-Gauss-flint-api-corrected-8542.py`
SHA `6815bbd8769bcea3ba4a2ca6f5a5d03d731300d07d3c960b1139aad30d14bbd2`
只从该正确原四次源再生必要定义。

低 F20 自含源
`2026-11-27-unit211-generic-LS-W-J19-F20-entire-low-fibers-original-QQ-return-8542.py`
SHA `ff21db393371343c1b0f0c23345b629cc6d647ba76b05d35c94c6be417670784`
独立从原 Gram 计算，亦明确使用 `vm(dv,dv)[j]`。

## 3. 对本轮整 Lhalf 结论的影响

正确 mean 的直接 native→G D→F101 全返回链已另记
`W-native-Lhalf-correct-jet-mean-source-chain-8542.md`。
上述既有原子来源与该链均不承继此次错 compact mean(1)。
因此本次已实际得到的整 Lhalf 原理想排除不因这一具体定义错误撤回。

该结论不替其它尚未追踪的分支背书，也不扩大任何已付单位定理的原域。
没有重跑已成来源、没有修改冻结源或旧执行状态。
