# R150：原十七式固定标准源的第一轮 31-adic 残差（已执行，尚未 correction）

本条独立冻结第一轮残差生成；后续 correction 在新文件继续，不回写本条。
原问题及完整 Macaulay 来源见 `2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md`。
以下只在明确的整数模型、模数及固定预算内陈述。

## 1. 原始整数方程与目标

仍使用原 11 条物理极化 N 方程和 6 条完整 Gamma 方程；不是把 N 换成整个矩阵零式。
`2026-11-14-r150-first-padic-integer-model-789f.js` 调用既有原参数生成器，
从共同常数分母 D 及每行常数 content 得到 17 条 primitive 整数方程。
D 与所有 content 在 31 下均为单位，故这一步保留原有理方程的理想。
本条的 source coefficients 是 primitive 整数方程的系数；并非已经乘回 D/content 的有理原式系数。

生成器保存全部原整数系数，完成原固定 D 的 3927 次检查，并核对 4433 个实际系数项的
mod31 剩余类全部等于此前冻结的原模型。输出完整整数方程 JSON、mod961 模型及各自 SHA。
这不是对参数值的抽样。

令

\[
\begin{aligned}
F_+(s)&=5s^3-25s^2+32s-8,\\
F_-(s)&=5s^3+135s^2+864s+864,\\
E_8(s)&=5s^8+50s^7+153s^6-936s^5-2888s^4
 +15936s^3-3392s^2-25472s+9600,\\
h_0(s)&=s^3(s-2)F_+(s)^2F_-(s)^2E_8(s).
\end{aligned}
\]

这是次数 24 的**特征零候选**，尚未证明它乘九个目标属于特征零原理想。
整数展开直接核得 \(h_0\bmod31=25h_{31}\)，其中 \(h_{31}\) 为此前已证的九目标共同首一最小 annihilator。
目标仍是原九个 \(t_j=(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a)^2\)，\(2\le j\le10\)。

## 2. 固定原来源列与首位代表

使用已证的 3333 原 N 预基来源和 2195 原余来源，总计 5528 个真实原行，
仍以原 6188 行号存储、未选行系数为零。来源权重
\(\delta_r=10(|u_r|+1)+5\mathbf1_{\Gamma}\)，输出单项式权重
\(w_\mu=10(|\mu|-1)\)。本条固定 \(B=85\)。

完整 T96 真 kernel 的标准单项式，加全部原常预基列，给出
217374 个固定整数来源列 \(A_{\rm std}\)，嵌入 219032 个加权输出坐标。
这些来源列 mod31 独立，因此在 Q 上独立。
此前 kernel 正规形给 \(h_{31}t\) 的最小余来源 cost 85。
本程序把该真实代表经完整 H/J、backward、forward 常预基记录恢复到原 primitive 行，
再乘 25，并将所有系数取标准数字 \(0,\ldots,30\)，得到 \(x_0\)。

已实际逐系数验证

\[
 A_{\rm std}x_0\equiv h_0t\pmod {31}.
\]

该验证涵盖全部原 6188 行与全部 219032×9 个加权输出系数；没有仅核投影或 scalar pairing。
同时检查每个非零 source 属于上述固定 5528 原行，且次数加来源权重不超过 85。
实际最大 source coefficient 次数是 **74**，最大 source cost 是 **85**。

## 3. 首轮实际残差

直接用原整数方程的 mod961 系数作完整卷积，逐项验证
\(A_{\rm std}x_0-h_0t\) 可被 31 整除，保存

\[
 r_1=\frac{h_0t-A_{\rm std}x_0}{31}\pmod {31}.
\]

此处除法是对已经验证为 31 的倍数的 mod961 代表逐项进行，因此得到正确的 mod31 残差。
实际结果为：

- 原始 native 时间：**6.28131 秒**；wrapper 总执行时间 **6.291365054 秒**。
- 总计 **1,874,424** 个非零残差系数，最大输出 cost **85**。
- 源最大次数 **74**，source cost **85**；全部来源与加权范围检查成立。
- `initialOriginalPrimitiveIdentityMod31=true`。
- `allWeightedBoundsVerified=true`。
- **`correctionComputed=false`**。

逐目标残差非零数（目标 j=2,…,10）为：

`[208804, 208557, 208715, 204470, 208754, 208773, 208751, 208795, 208805]`

本条只构造并核验 \(r_1\)。它既不声称 \(r_1\) 属于固定来源像，也不声称
\(h_0t\) 已有 mod961 证书，更不声称特征零包含。

## 4. 下一步判据的准确含义

若在同一固定标准列中求得 \(A_{\rm std}z_1=r_1\pmod{31}\)，则
\(x_0+31z_1\) 才是 mod961 的原式证书；必须对原十七式再作完整验证。
若余正规形不为零，或其真 kernel 标准源 cost 超过 85，则本预算的固定来源空间不能完成本轮提升。
因为固定列有一个 mod31 单位子式，这样的失败排除该固定整数列空间中的特征零解，
不能排除更高预算或额外来源中的表示。
有限多位成功也仍需有理重构和完整原式精确恒等式才可成为特征零结论。

## 5. 文件与重现

代码（本条起冻结）：

- `2026-11-14-r150-first-padic-integer-model-789f.js`
- `2026-11-14-r150-first-padic-residual-789f.cpp`
- `2026-11-14-r150-first-padic-residual-runner-789f.py`

实际小文件和完整压缩数据均保存在 `r150-first-padic-residual-789f/`，
`manifest.json` 列出逐文件大小和 SHA256；完整初始源与残差均已压缩持久保存，未仅留临时路径。
原十七式模型、四个常预基来源文件、canonical C 输入的固定 SHA 在实际运行 receipt 中。

初始源未压缩 SHA256：
`265b0b420afd925d72eb1ab2e2e329fe6232644d740a78aede67866da3545c96`。

首轮残差未压缩 SHA256：
`0ed97a63ca646584e9494b757505037a696f7fef460de3da62bbdaccae851c18`。

native 程序以 `timeout --kill-after=10s 60s prlimit --as=536870912 --core=0` 运行。
整数模型生成先有一次 Node 在 512MiB address-space 限制下的 V8 初始化失败（退出 133，数学未开始）；
随后 `--max-old-space-size=256` 下成功，耗时 0.401695 秒。
该 JS 回执的 RSS 观察值为零，表示采样未获得有效观察，**不宣称实际 RSS 为零或已验证 512MiB resident 峰值**。
上述 native 残差计算的硬 address-space 限制则确实生效。

实际 native CLI：

```text
PROGRAM canonical-C.bin original31-model.txt nf-reduction.bin \
        nf-forward.bin nf-backward.bin original-integer-mod961.txt OUTPUT_PREFIX
```

`R150P031` 存全部 6188 原行、原方程编号/乘子/权重及九目标初始系数；
`R150RH31` 存全部 4367 原 m 单项式的 219032 个加权参数坐标及九目标残差。
两种格式中所有域元素均为规范的 0,…,30。
