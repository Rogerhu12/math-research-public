# R120 补充：腰部 source 的实际下界

2026-11-13，newton_source。**已证明的指定点界；不作全域结论。**

R120 的全圈上界约0.63，首先须区分这是区间包络还是候选本身的残差。
新入口 `scripts/fourfold_phase_newton_source_point_diagnostic.py` 保持整个
$\eta=10^{-9}$ 参数盒、同一个固定目标与所有 infinite primitive 误差，
只把角区间半宽改为零，计算精确节点 $\theta_j=j\pi/(2N)$ 的真值包络。
有限多项式值仍由向外舍入 FFT 计算，完整 $A_0$ 误差仍逐点加回；
输出明确标 `whole_real_angle_circle=false`。

实际输出 `notes/2026-11-13-newton-source-point-diagnostic-native.json` 给：

| $(r,\theta)$ | 完整真实 $q=-\mathcal C_s(\rho^2f)/2$ 的包络 |
|---|---|
| $(0,0)$ | $0.612611743059477<q<0.612613889441334$ |
| $(1/8,69\pi/2048)$ | $-0.112253165503291<q<-0.112251016333059$ |
| $(1/4,459\pi/8192)$ | $0.065232751906718<q<0.065234842124772$ |

所有区间对整个参数盒同时成立。下界不是浮点点值：程序直接使用完整区间
的符号固定端点。例如第一行的完整下端点大于所列十进制下界。
因此本候选在该固定目标下的全局 source $C^0$ norm 至少0.6126117；
只加密角区间或改进 Fourier 舍入包络不可能使这个同一范数降至 $10^{-3}$。

这不表示该候选不能精确化。完整右逆的频率作用、源的 mean/非mean 分量、
更好的近似候选，以及从一开始选择其他固定目标，仍可改变真正迭代门。
此处不以 source 大小单独推出不存在性，也不将它作为任务完成。

目标曲率在入口中明确按

$$
E=\langle |F_r|^2\rangle_\theta,\qquad
E'=2\langle F_r\cdot F_{rr}\rangle_\theta,
\qquad K_0=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}
=-\frac1{a\sqrt E}\left(\frac{a'}{\sqrt E}\right)'
$$

逐盒计算。它没有复用旧背景的 $-a''/a$。
这与 $g_0=E\,dr^2+a^2d\theta^2$ 是同一目标，且 source 用的 $\Delta$
亦为该 $K_0$ 的相关曲率分子。

重放命令：

```sh
python scripts/fourfold_phase_newton_source_point_diagnostic.py \
  --out notes/2026-11-13-newton-source-point-diagnostic-native.json
```

native 已实际完成三行；源、原始对象、origin、direction 和两份依赖入口
SHA 均记录在报告中。
