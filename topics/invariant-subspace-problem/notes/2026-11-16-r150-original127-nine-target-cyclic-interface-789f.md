# F127 九个原目标的完整循环子模与 h* 作用接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted, GPT-6 Astra Pro。  
日期：2026-11-16。

本入口只消费已经完成的原 F127 扭子状态，计算九个原目标生成的完整参数子模及其共同最小湮灭子，并计算原整数 $h^*$ 的作用。本文是执行接口；尚未运行这一新消费者，不预填子模维数、湮灭多项式或零作用结论。没有声称本地 AST 或编译已经执行。

## 1. 已付输入和原来源

原执行为 run **43772109844**，step **original127-complete-whole-torsion60**，execution source **ff73f96185986879e4fe9a8e72fa42453843738c**。小实际回执：

~~~text
notes/r150-source-kernel-session-789f/43772109844-original127-complete-whole-torsion60.json
blob 1c421e54e33f0a0e7477ae23034ba510fc59f193
21892 B
SHA256 5b9e34b3d091194a4dd2072ab9c9f2320e6c804879a4716ae9c2ebfbb1932a7e
~~~

该实际结果包括全部 6188 原来源：常预基 3333 列，加其余 **2855** 列。恢复的 660 列实际有 658 零正常形及两个非零正常形，后者原 ID 6046、6063 均进入完整 GB；没有沿用旧 2195 列的遗漏子集。完整 GB 的秩为 1021、自由方向 13；全标准窗为 805，完整观测核为 **299** 维。该 299 是整个仿射扭子维数，不是当前九目标子模维数。

原状态保留整个 805 维空间、13 个自由尾泄漏方向、完整观测稳定性、299 列扭子嵌入 $K$、其作用 $J$，以及原标签 2 至 10 的九目标坐标。当前新入口再核全部 $805\cdot9=7245$ 个 $KT$ 坐标，锁定二进制布局与目标的方向。它不重新计算正常形、GB、观测空间或整个扭子。

全部三个临时输入逐完整 SHA 核验：

| 文件（位于 original127-whole-torsion） | 字节 | SHA256 |
|---|---:|---|
| original127-whole-torsion-pipeline-receipt.json | 9819 | 2c1054b2c3224c7c27c4ff09e1852bbab3a219429f8d08528832d81041de8c07 |
| torsion-whole-state.bin | 1414575 | 948d6e78dc96e8d9e367797d33919ce4c1e1deb406dee346505200da00ea4d60 |
| whole-torsion-characteristic.json | 2560 | ee048002bcda7090ed599709d88ad2d74ecd46448e647bfb3513fa3ad9b64bd6 |

whole binding 为 **05c13d9a57fee12f0751d40feccbfb601686b3d02f497d0e8a99092c44db4211**，原 GB binding 为 **9e8510d9519e43fe4f8765a6672194c9dba6d1776a9adf652ac343c5261ebc3e**。

## 2. 固定原整数多项式

参数文件：

~~~text
notes/2026-11-16-r150-original-hstar-integer-parameters-789f.json
blob bb66e2938a2625aa67059cea7f35a4816b64f4bc
1286 B
SHA256 e04560989cfe0d888995290fa917b457f09f6caa975f59889ee0864e5b82ae31
~~~

它以升幂系数给出

$$
F_+=-8+32s-25s^2+5s^3,\qquad
F_-=864+864s+135s^2+5s^3,
$$

$$
E_8=9600-25472s-3392s^2+15936s^3-2888s^4-936s^5
+153s^6+50s^7+5s^8,
$$

$$
h^*=s^3F_+^2F_-^2E_8,\qquad h_0=(s-2)h^*.
$$

消费者先在整数中重乘并核全部 24 个 $h^*$ 系数、次数 23、首项 3125，再约化到 F127。该首项为 127 单位。依据是原正式稿 [full-affine-divisor-monic-at31-and-residual-envelope157](../results/R150-appendix-full-affine-divisor-monic-at31-and-residual-envelope157.md)，blob **4aadf7e744f7da751cdbf847dbd66709905905e8**。参数没有采用任何旧有限域缩放。

## 3. 原目标子模的完整性

令 $V=\mathbb F_{127}^{299}$，$J$ 为已付参数作用，$T$ 的九列为原目标。构造

$$
\mathcal K=(T,JT,\ldots,J^{299}T).
$$

从其实际 RREF 选择**原 Krylov 列**，得到 $B$；每列保留原 target label 和参数幂次，不用无来源的 RREF 行代替它。再选择 $B$ 的真实原坐标单位子式，求限制作用 $J_T$ 和种子坐标 $T_T$，核全部原 299 行：

$$
JB=BJ_T,\qquad T=BT_T.
$$

一方面 $B$ 的每列都是原目标的参数倍，故 $\operatorname{im}B$ 包含于 $M=\mathbb F_{127}[s]\langle t_1,\ldots,t_9\rangle$。另一方面上述两个完整恒等式说明 $\operatorname{im}B$ 不变且包含九个种子，故包含 $M$。两者相等，支付完整子模，不只是有限前缀。代码另核所选基列无需参数幂 299；这个冗余末块用于每个单目标的首次依赖检查。

对各目标，实际 RREF 其 $299\times300$ 单列 Krylov 矩阵。若秩为 $d$，检查主元恰在 $0,\ldots,d-1$ 幂，再从第 $d$ 列得到首个关系，并逐原 299 坐标乘回。此前独立性与该关系共同证明得到的是该目标的**最小**湮灭多项式 $m_j$。共同最小湮灭子为

$$
m=\operatorname{lcm}(m_1,\ldots,m_9).
$$

代码独立核 $m=\operatorname{minpoly}(J_T)$，核 $\chi_{J_T}$ 整除已付完整 $\chi_J$，以及所有因子乘积。子模维数、特征多项式次数和最小多项式次数分别记录，不混为同一数量。

## 4. h* 的实际作用和完整像子模

先在原 299 坐标以 Horner 法算

$$
H=h^*(J)T,\qquad H_0=(J-2I)H.
$$

同时在真实子模坐标算 $h^*(J_T)T_T$ 并核 $B$ 运输后的所有原坐标。小回执给九列逐列零标志、这九列的秩，以及 $h_0$ 的同类数据。

随后对 $H$ 重作独立完整 Krylov 子模、九个首次依赖、全原行作用与坐标核验。这一阶段的原来源记录是 $s^a h^*(s)t_j$；临时 phase 明存完整整数乘子 $h^*$，不会把它误记为单独 $s^at_j$。

由 PID 循环分解，各循环因子 $f_i\mid m$ 在乘 $h^*$ 后变为 $f_i/\gcd(f_i,h^*)$；最大循环因子给

$$
\operatorname{ann}(h^*M)=
\left(\frac{m}{\gcd(m,\overline{h^*})}\right).
$$

新入口先实际重建 $h^*M$，再核这个商式。它不假设半单性，不通过理论商式跳过原目标作用。$h_0M$ 的最小湮灭子按同一已证完整 $M$ 的商式记录，九个 $h_0$ 目标作用仍逐列实际计算。

## 5. CLI、预算与恢复

唯一程序：

~~~text
notes/2026-11-16-r150-original127-nine-target-cyclic-module-789f.py
blob b4e735dc12e8dee8b483728b895677dcfff23a09
20947 B
SHA256 d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3
~~~

输入清单：

~~~text
notes/2026-11-16-r150-original127-nine-target-cyclic-inputs-789f.json
blob 7f7d20cea28e98415639f8c3a65c4321cdc5297c
3037 B
SHA256 adb5c0917fe675fba6b08ea0e1c4691018312f35641b0c1504e9aa1c95f32314
~~~

~~~text
python {scripts}/2026-11-16-r150-original127-nine-target-cyclic-module-789f.py
  --whole-out {work}/original127-whole-torsion
  --hstar {scripts}/2026-11-16-r150-original-hstar-integer-parameters-789f.json
  --out {work}/original127-nine-target-cyclic-module
  --seconds 60
  --memory-mib 1024
~~~

外墙预算 120 秒；依赖已成功的 whole-torsion60 步。只需要现有 python-flint 0.9.0，无新编译或安装。使用的 nmod_mat.rref、inv、minpoly、charpoly、transpose 与精确有限域矩阵乘法已按 [0.9.0 官方文档](https://python-flint.readthedocs.io/en/latest/nmod_mat.html) 核查。

输入、源码 SHA 和算法标识组成语义 binding，预算与临时绝对路径不进入 binding。每个已完成 phase 原子保存为临时 gzip，压缩头 mtime 固定为 0，完整字节 SHA 与解压 payload SHA 均进入小 manifest。Krylov、各目标首次依赖、完整子模、$h^*$ 作用分别成 phase；续接只读相同 binding 的完成 phase。未完成的单次 RREF 没有可恢复内部状态，不声称已保存。软预算检查在精确操作之间进行；FLINT 单次调用返回前不保证 Python 软停止，故外层另有 120 秒上限。

小回执为：

~~~text
{work}/original127-nine-target-cyclic-module/original127-nine-target-cyclic-receipt.json
~~~

临时 manifest 是 target-cyclic-manifest.json。完整基、作用、原目标幂次来源、逐列 RREF 主元和矩阵均只在 job 临时 phase 保存。小回执保所有九个最小多项式的完整系数、共同因子分解、实际维数、完整原乘回门、各文件 SHA，不重复放大矩阵或长主元列表。

## 6. 结论边界

这是原矩阵在**单一有限域 F127** 的完整目标子模计算。实际非零作用只能给该域的非成员证据；实际零作用也不自动给特征零原来源。完整仿射扭子 299、自然无穷远资格门、J127 的算术缺陷、Ω127 的系数约化、以及可能的 Q 剩余因子分别由其自己的已验证证书决定。本入口不把旧 31 系数扭子的维数下界搬到 127，不把未知 $s+64$ 因子解释成特征零例外点，也不预称 $h^*$ 或 $h_0$ 杀掉九个目标。
