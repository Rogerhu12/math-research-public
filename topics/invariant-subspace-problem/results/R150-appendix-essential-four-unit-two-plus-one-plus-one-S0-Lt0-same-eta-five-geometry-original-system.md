# R150 / S0 / Lt0：同一 eta 消元后的五个几何变量原必要系统

状态：**原恒等式与输入构造已验证；一般 Lt0 尚未排除。** 本条把已完成的 $U=0$ 整支排空用于真正减少一个几何变量，恢复原三个 mean、原 $N(V)$、分别的原 $N_B/P_B$ 偶奇分量，并加入同 eta 的原四次式。它不是旧二十个 Cramer 子式的换序重跑。实际有理单位门的结果须以独立执行回执为准。

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127；2026-11-27（台北）。

## 1. 单一 eta 与原范数

沿用已登记坐标

$$e=u-1,\quad k=Q/e,\quad j=k+2-2e,\quad x=k+4,$$

$$s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,$$

$$T_n=x^2-2j^2-2\lambda jx-4xf,\quad T_d=2jk,$$

$$Z_n=sT_n-2jkA,\quad Z_d=2j^2,\quad D=s^2Z_d-4Z_n,$$

$$B=T_n-j^2s,\quad U=ek+2e-2.$$

[等孤立权重整支返回](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-equal-singleton-weights-and-same-eta-elimination.md) 已证明 $U\ne0$；原配对式 $M_a=UD-2j\eta B=0$ 与原 $D\ne0$ 随即给 $B\ne0$。设

$$n=UD,\qquad d=2jB,\qquad \eta=n/d.$$

本源在原多项式环中逐项核出

$$M_a=n-d\eta,$$

$$Z_dn^2-(1-ek)D d^2=Z_dD Q_a,\qquad Q_a=U^2D-2(1-ek)B^2.$$

因此同一个 $\eta=n/d$ 与 $Q_a=0$ 恢复原配对式和原范数，不产生另一嵌入。这里的 $d,D,Z_d$ 都已付。

对三个分别的原 eta 一次式

$$P=N(V),\quad N_{B,\mathrm{odd}},\quad P_{B,\mathrm{odd}},$$

写 $P=P_0+P_1\eta$，构造

$$\widetilde P=dP_0+nP_1.$$

源码实际核验三个独立身份

$$\boxed{dP+P_1M_a=\widetilde P}.$$

因此这三式使用相同的 $n,d$。原 $N_B/P_B$ 偶分量原样保留；源码开头还验证原最高值方程与使用二次范数简化后的公式之差，确为同一个原范数的显式倍数。所有 Gram 计算采用正确 dual product，尤其二重点 mean 的 $-2(d^2)_1=-4d_0d_1$。

## 2. 另一个原物理单位的返回

旧图的原物理单位分子为

$$L_{\mathrm{old}}=D-\eta sZ_d.$$

不能将它在消元时直接丢掉，也不能独立选择 eta。定义

$$L_*=B-Ujs.$$

源码乘回

$$dL_{\mathrm{old}}-sZ_dM_a=2jD L_*.$$

所以在已付图上原 $L\ne0$ 恰由 $L_*\ne0$ 表示。其余物理单位保持原多项式分子。

## 3. 十五个明确的原必要生成元

以下次数按 $(e,k,\lambda,f,v)$ 排列。每个归一化只除去列出的已付因子和非零有理常数，源码均乘回。前三行是原 mean；其余 $N/P$ 仍然分别存在。

| 生成元 | 次数 | 项数 |
|---|---:|---:|
| 原 $E_1$ | $(5,4,2,2,2)$ | 103 |
| 原 $E_{B,\mathrm{even}}$ | $(7,6,2,2,2)$ | 227 |
| 原 $E_{B,\mathrm{odd}}$ | $(7,5,2,2,2)$ | 174 |
| 原 $N_1$ mixed 必要式 | $(5,4,2,2,2)$ | 94 |
| 原 U 矩 | $(4,4,3,2,0)$ | 86 |
| 同 eta 原范数 $Q_a$ | $(5,5,2,2,0)$ | 103 |
| 同 eta 原 $N(V)$ | $(6,6,4,3,0)$ | 299 |
| 原 $N_B$ 偶分量 | $(10,7,3,3,3)$ | 674 |
| 同 eta 原 $N_B$ 奇分量 | $(12,8,4,4,3)$ | 1573 |
| 原 $P_B$ 偶分量 | $(13,9,3,3,3)$ | 1087 |
| 同 eta 原 $P_B$ 奇分量 | $(16,13,4,4,3)$ | 3397 |
| 原 $N_1$ 的 mean 余式 | $(8,7,1,1,2)$ | 205 |
| 原 $Q_a$ 的 mean 余式 | $(12,10,1,1,2)$ | 451 |
| 同 eta 原 $Q_4$ | $(21,16,0,0,4)$ | 764 |
| 同 eta 原 $Q_5$ | $(22,19,0,0,5)$ | 1085 |

后三类辅助行都从本源重新生成的原 mean 组合得到；188 次系数分母检查及所有组合身份均已通过。$Q_4,Q_5$ 来自 $N_1$、mean 乘法一致性行与 $Q_a$ 的三行子式，原组合逐项乘回。$32[v^4]Q_4=B_{11,8}$，且 [整个首项零曲线已经返回](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-same-eta-quartic-leading-zero-exclusion.md)，所以新增四次输入没有未处理的首项零纤维。

原 $N_1/Q_a$ 主子式也是 [已完整排空的边界](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-N1-Qa-pivot-zero-exclusion.md)。本源重建原行、主子式、全部已付剥除，最后核验完整常数乘单因子分解，并精确匹配规范 $J_1$ 的 SHA-256：

`47f6f57c37a083489d6f49aae97dcceebb61db67e6e59a80001a7d15acc906b4`。

规范因子的有理常数归一化与旧源的未归一化子式不同；常数也乘回，不把两种序列化误当作同一个 SHA。

## 4. 饱和、覆盖与真正单位门

在 $\mathbf Q[e,k,\lambda,f,v]$ 加两个辅助变量，分别要求

$$\xi S_{\mathrm{physical}}=1,\qquad \zeta S_{\mathrm{chart}}=1.$$

第一组为以下十八个已付分子之积：

$$e,\ k,\ e+1,\ j,\ x,\ ek-1,\ D_3,\ \lambda,\ Z_n,\ D,\ L_*,\ A_f,$$

$$e-1,\ 4e-k-4,\ 4\lambda-1,\ A,\ W_n,\ B.$$

这里

$$D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4,$$

$$W_n=(\lambda-1)T_d-T_n,\qquad A_f=(3-4\lambda)kZ_d-Z_n(k-4e).$$

除原图定义的物理单位外，$e-1$、$4e-k-4$、$4\lambda-1$、$A$、$W_n$ 分别来自已登记的零基点权、半权、参数首项及原 U jet 整支；$B$ 来自本条前置的 $U=0$ 整支排空。

第二组为以下九个已登记整支排空后的单位：

$$v,\quad4e-k,\quad\Omega=2e^2-ek+2,\quad B_{4,4},\quad B_{11,8},\quad J_1,$$

$$2e-1,\quad U,\quad77e-16.$$

$B_{4,4}$ 在源中使用此前原 $P_{045}$ 首项曲线的完整公式；$B_{11,8}$ 使用刚从原 $Q_4$ 重建并核 SHA 的同一式。没有把这两个首项或 $J_1$ 当作未付的泛型条件。两组只使饱和输入分组，不改变每个因子非零的要求。

完整 Singular 理想 $I$ 含上述十五个生成元及两个饱和式，变量顺序固定为

`(invPhysical,invChart,lam,f,v,k,e), dp`。

实际执行流程先在**独立进程**运行 45 秒以内的 `liftstd(...,"std")` 小单位 smoke，要求退出码 0、精确通过 marker 且无 Singular `?` 诊断。通过前不写入也不启动完整输入。随后完整门使用 `liftstd(I,cert,"slimgb")`，1200 秒、8 GiB 地址空间上限；必须实际计算并验证

$$\operatorname{matrix}(I)\,\mathrm{cert}=[1].$$

超时、进程错误、语法诊断或只返回非单位基，都不能成为排空结论。源码保留完整输出摘要、长度、SHA 与真实退出码；不使用 `modstd` 或并行 tasks 接口。

本条只说明所有原临界点映入该精确必要理想，以及所选原式在已付图上的同 eta 返回。未证明它与完整原临界理想的全部生成元等价，也未预宣称幂来源。

## 5. 已实际执行的构造检查

自含源：[2026-11-27-unit211-S0-Lt0-same-eta-five-geometry-safe-slimgb-QQ-8542.py](../notes/2026-11-27-unit211-S0-Lt0-same-eta-five-geometry-safe-slimgb-QQ-8542.py)。

- 38,286 字节，SHA-256 `7161bc65dca9656ac76c35c3154f2085efe090b96cf9e699dd5af7f45c922c69`。
- 本地参数仅为 `--build-only`；Python 3.12.14、python-flint 0.9.0；构造阶段 60 秒 alarm、8 GiB 地址空间上限。
- 实际退出码 0；外部墙钟 11.280860 秒、源内 11.023649 秒；最大 RSS 51,000 KiB。
- stdout 26,797 字节，SHA-256 `a11d493a693e91fa7a6bd159c2aca0aa84964ce5635b1eb6567935f9a641d301`。
- 生成的完整 Singular 输入 223,588 字节，SHA-256 `41c822173a00b11665571a5ca325d6530303ef4d28ccaf28471bbf12d82aabab`；它可由自含源确定性再生，没有保存大系数文件。
- 构造回执：`notes/2026-11-27-unit211-S0-Lt0-same-eta-five-geometry-build-execution-8542.json`。
- 前置一次构造检查曾把未归一化 $J_1$ 与规范因子的 SHA 比较，因常数归一化差异而断言退出；没有运行 QQ 门。完整负回执保存在 `notes/2026-11-27-unit211-S0-Lt0-same-eta-five-geometry-build-normalization-failure-8542.json`。现版用实际完整因子分解和常数乘回修复这一输入校验。

本地没有 Singular，故本条没有单位证书或一般 Lt0 排空宣称。独立 QQ 门的实际回执另行登记。

专用公开 Actions：`.github/workflows/invariant-subspace-Lt0-same-eta-five-geometry-8542.yml`。本次 source/workflow push 触发一次；运行身份与真实结果随实际返回登记，不将排队或 BEGIN 当单位证书。
