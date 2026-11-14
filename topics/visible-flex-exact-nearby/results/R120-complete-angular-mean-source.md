# R120 补充：完整角均值与非均值源的实际下界

2026-11-13，newton_source。**已证明，限于明示径向截面。**

输入候选、固定目标和整个 $\eta=10^{-9}$ 参数盒均与 R120 相同。
入口 `scripts/fourfold_phase_newton_source_angular_mean.py` 用16384个
完整连续角格覆盖实物理圆；每格都保留完整 primitive 尾、相关曲率及 source。
完整输出是 `notes/2026-11-13-newton-source-angular-mean-native.json`。

若格 $I_j$ 上有 $q(\theta)\in[l_j,u_j]$，所有格等长，则

$$
\frac1N\sum_j l_j\le\langle q\rangle_\theta\le
\frac1N\sum_j u_j.
$$

程序以原向外舍入 `reduce_box` 求和再除以整数 $N$。
随后从每个 $[l_j,u_j]$ 中以区间减法减去这个完整均值区间。
任一符号固定的新区间给该格上的 $|q-\langle q\rangle|$ 下界，
取最大值即为非均值 $C^0$ norm 的下界。这是整圈积分包络，未把梯形抽样均值
当作真均值，也没有删除完整方程的 mean。

实际结果（十进制均向外放宽）：

| $r$ | $\langle q\rangle_\theta$ | $\|q-\langle q\rangle\|_\infty$ 下界 | $\langle q_{\rm mat}\rangle_\theta$ | $\|q_{\rm mat}-\langle q_{\rm mat}\rangle\|_\infty$ 下界 |
|---:|---|---:|---|---:|
| $0$ | $[-0.004517,0.003446]$ | $0.604740$ | $[-0.004339,0.004006]$ | $0.555675$ |
| $1/8$ | $[-0.000819,0.000801]$ | $0.110584$ | $[-0.000825,0.000822]$ | $0.103040$ |
| $1/4$ | $[-0.000573,0.000577]$ | $0.064131$ | $[-0.000528,0.000542]$ | $0.059571$ |

因此腰部约0.61的 source 主要属于非mean 部分。简单地删掉常数模无法把它
变成很小的源。更换一个从一开始固定的目标度量仍是另外的数学操作，
其 source 变化有非均值部分，本表没有排除这种优化。

本次同步输出的 $K_0,E,E',a,a',a''$ 按
$K_0=-a''/(aE)+a'E'/(2aE^2)$ 来自同一目标，供核对。
三行 native 运行60.84秒，完整程序 SHA、输入 SHA 和参数分数在报告中。
重放：

```sh
python scripts/fourfold_phase_newton_source_angular_mean.py --angles 16384 \
  --out notes/2026-11-13-newton-source-angular-mean-native.json
```

这些截面下界用于选择接下来要改进的候选或结构化逆。
它们不构成闭面不可弯的证明，不代替整个径向源、高角档或非线性收敛。
