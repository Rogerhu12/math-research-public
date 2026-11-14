# R133 补篇：最终 ac1 中心的完整均值 Green 已实际计算

2026-11-14。原六步重放已经恢复最终完整 ac1 候选的全部科学数组及五个分片；随后原标量消费者一次正常执行完 **7721 个连续闭盒、6143 个真实 PPoly 均值接口**。本篇给出此前未算的传播因子和全区间均值算子常数。

结论是给定完整非平均场之后的标量均值逆。完整非平均补逆、参数 Schur 非零和真实外尾匹配仍是另外的方程。

## 1. 对象、实际输入和执行

中心仍为

\[
R=25/8,\qquad
\alpha=6890507429876859/9007199254740992,\qquad
\nu=-2572625729470897/72057594037927936.
\]

完整索引 SHA256 是

`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。

[第六步恢复记录](../notes/2026-11-14-R133-final-replay-stage06-restored.md) 和其中的实际科学数组对照确认：16 个科学字段、65 个初值的位模式、全部 `[4,6144,65]` 系数和五个原 gzip 分片都与原候选一致。这里没有从初值清单猜测缺失的径向系数。

原程序 [fourfold_codazzi_final_scalar_mean_cached.py](../scripts/fourfold_codazzi_final_scalar_mean_cached.py) 的 SHA256 是 `6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93`。本次没有修改它。程序准确连接先前完成的 493、96、1334 行真实目标缓存，与所有候选节点和控制端点作共同细分；三个输入的完整身份及原 scalar germ 均写入结果。整个原参数区间 \(|\eta|\le10^{-9}\) 和全部 primitive 尾保留。

实际运行：320-bit Arb，进程正常返回 0，用时 22.259743 秒。完整报告以 [7721 盒 native 无损分片清单](../notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json) 保存，恢复后的原容器 SHA256 为 `e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`；[实际进程记录](../notes/2026-11-14-R133-final-complete-scalar-mean-process.json) 保存命令、来源及返回状态。

这里的圆周范数使用归一化平均 \(\langle1\rangle=1\)，径向积分使用原 \(dr\)。未知变化量是完整物理 moving 变量 \(h=(\xi,\zeta)=(\delta u,\delta v)\)，没有除以 \(\alpha\)。当前有限中心有 32 模，未知变化量仍允许全部 Fourier 模。

## 2. 被实际消费的标量恒等式

完整推导见 [scalar mean 与残差敏感参数源](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md) 和 [三角 Green 与缓存消费者](R133-supplement-complete-mean-triangular-Green-and-cached-consumer.md)。为明确本次常数的意义，记

\[
m=\langle v\rangle<0,\quad z=\langle\zeta\rangle,\quad
\widetilde h=(\xi,\zeta-z),\quad
n=\frac{a^2}{m^2},\quad\tau=-\frac{2a^2}{m^3}>0,
\]
\[
\mathcal V=\langle u^2\rangle+K\langle(v-m)^2\rangle,
\quad R_0=m'-\beta m(1-\mathcal V-Km^2),
\quad\widetilde c=2\beta\mathcal V-3R_0/m.
\]

所有导数都取真实 PPoly 导数；计算没有把近似中心的残差设为零。置
\(\rho=a'^2/E_\nu\)、\(Y=\tau z-\rho w\,\delta\nu\)，则

\[
Y'=\widetilde cY+
4\beta n\langle u\xi+K(v-m)(\zeta-z)\rangle
+\tau\langle f_2\rangle+F_\nu\delta\nu,
\tag{A.1}
\]
\[
F_\nu=\widetilde c\rho w+
2\beta n\langle(v-m)^2\rangle\partial_\nu K,
\qquad
\partial_\nu K=-Kw+\frac{\beta w'}{2E_\nu}.
\tag{A.2}
\]

候选均值跳和独立响应跳分别保留。在任意共同接口，若 \([z]_i=j_i\)，则

\[
Y_i^+=T_iY_i^-+(T_i-1)\rho_iw_i\delta\nu+\tau_i^+j_i,
\qquad T_i=(m_i^-/m_i^+)^3.
\tag{A.3}
\]

真实候选跳由准确 dyadic 两侧系数计算。即使某一候选接口连续，也允许在那里输入独立的 \(j_i\)。

## 3. 完整传播因子

定义

\[
I_-=\int_0^R(-\widetilde c)_+\,dr,\qquad
J_m=3\sum_i\frac{|[m]_i|}{\min(|m_i^-|,|m_i^+|)},\qquad
\Gamma=e^{I_-+J_m}.
\]

实际有向结果给

\[
I_-<0.013149547925409,\quad
J_m<1.169345\,10^{-18},\quad
\boxed{\log\Gamma<0.013149548,\qquad\Gamma<1.013237.}
\tag{A.4}
\]

带符号的整个积分还满足

\[
-0.004600583<\int_0^R\widetilde c\,dr<-0.00046415.
\]

传播因子使用任意后向子区间的负部积分，不能用这个带符号全积分替代它。全部 \(6143\) 个实际乘法接口已经包括在 \(J_m\) 中。

## 4. 整个体区的完整 \(L^2\) 界

下表的常数**已经乘上 \(\Gamma\)**。每行是列出的单独输入到 \(\|z\|_{L^2(0,R)}\) 的严格上界；各输入线性叠加。

| 输入 | 严格系数上界 |
|---|---:|
| 原 mean 端值 \(|z(R)|\) | 0.288584 |
| 同一端值改用物理 \(|\delta C_0(R)|\) 表示 | 9.707939 |
| 完整非平均场 \(\|\widetilde h\|_{L^2_{r,\phi}}\) | 0.103384 |
| 普通 mean 源 \(\|\langle f_2\rangle\|_{L^2_r}\) | 0.538112 |
| 独立响应 mean 跳 \(\sum_i|j_i|\) | 0.698331 |
| reference-subtracted 参数积分及真实接口列 \(|\delta\nu|\) | 0.001498957 |

前两行是同一外端信息的两种坐标，使用时选择相应表示。参数还有准确恢复式 \(z=(Y+\rho w\delta\nu)/\tau\) 的直接项；本次另付

\[
\|\rho w/\tau\|_{L^2_r}<0.001436627.
\]

因此包含直接项的**完整参数列**满足

\[
\boxed{\|z_\nu\|_{L^2_r}<0.002935584\,|\delta\nu|}
\tag{A.5}
\]

（这里仅列参数输入，其他输入列按上表另加）。直接项没有重复乘 \(\Gamma\)，也没有被当成已经消失的参考源。

在既有真实长段/正帽合同的适用域中，若进一步用其真实非线性 mean 的导数列表达外端数据，则整条体区 mean 的两列为

\[
D_Z:\quad 7.157487\,10^{-6},\qquad
D_{f_B}:\quad7.952763\,10^{-7}.
\tag{A.6}
\]

这些乘的是原合同的 \(L^2\) 入口及独立 \(\dot H^2\) 端口范数。原 \(f_B\) 及远端 label 方程仍保留；(A.6) 不设置 \(f_B=0\)，也不证明外尾已经匹配。

全体区估计沿用了真实三角核的行、列积分顺序。对闭盒界 \(b_i\ge\sup\tau^{-1}\)、源率 \(e_i\) 和长度 \(\ell_i\)，有

\[
\|G_e\|_{L^2\to L^2}
\le\Gamma\sqrt{
\left(\max_i b_i\sum_{j\ge i}\ell_je_j\right)
\left(\max_j e_j\sum_{i\le j}\ell_ib_i\right)}.
\tag{A.7}
\]

本次逐盒连续界、全部径向积分与完整 Fourier 正交恒等式实际代入了 (A.7)；没有把 \(\sup_r\sum_m\) 误当 \(\sum_m\sup_r\)，也没有使用角采样替代均值积分。

## 5. 腰 mean 端口

控制函数在腰为零，故没有参数直接接触项。到 \(|z(0)|\) 的全部已乘 \(\Gamma\) 系数如下。

| 输入 | 严格系数上界 |
|---|---:|
| 原 \(|z(R)|\) | \(2.729204\,10^{-13}\) |
| 物理 \(|\delta C_0(R)|\) | \(9.181042\,10^{-12}\) |
| 真实帽 \(D_Z\) 列（原合同域） | \(6.769015\,10^{-18}\) |
| 独立 \(D_{f_B}\) 列（原合同域） | \(7.521128\,10^{-19}\) |
| 非mean \(L^\infty_rL^2_\phi\) | 0.085776712 |
| 普通 mean 源 \(L^\infty_r\) | 0.597291063 |
| 非mean \(L^2_{r,\phi}\) | 0.112001425 |
| 普通 mean 源 \(L^2_r\) | 0.732535123 |
| 独立 mean 跳 \(\ell^1\) | 1.017011959 |
| 完整 reference-subtracted 参数体源及接口 | 0.004626403 |

这里没有把腰 mean 设为零。它将随完整物理幅度行、外端 mean 和保留的 \(b_4\) 行一起进入 Schur 消去。

## 6. 可消费记录与限制

[有向舍入程序](../scripts/fourfold_codazzi_final_mean_native_rounding.py) 消费原完整 native，核完整区间、7721 行、6143 个候选接口及原源码/候选身份，再逐一验证以上严格有理上界；其 [实际可读界报告](../notes/2026-11-14-R133-final-complete-scalar-mean-readable-bounds.json) 保存完整有向输入值。

原 8.06 MB 完成报告只保存这一份完整计算，不附任何重复前缀。遵根 README 单件不超过 5 MB、较大文件须压缩的规则，使用共享 [无损分片工具](../scripts/fourfold_native_lossless_parts.py) 将原 gzip 字节分成 5 个独立 `.bin.gz` 二进制压缩块（直接 gzip 原字节，没有 base64 或 JSON 编码）。已实际在另一个工作路径恢复全部字节并核得同一 SHA；没有重算、缩减或修改任何数值行。每块小于 5 MB，恢复后仍是后续 mean-completed response/adjoint 消费器所需的原完整逐盒输入。

恢复命令为：

```sh
python scripts/fourfold_native_lossless_parts.py restore \
  --manifest notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json \
  --out /path/to/full-mean-native.json.gz
```

之后将恢复路径传给原消费者的 `--mean`，或舍入程序的 `--native`。大候选数组及重放中间数据仍遵恢复记录保存在可重建工作目录。

本结果真正关闭此前待付的 \(\Gamma\) 和完整标量 mean 各列。它没有把正在计算的 193 态有限 trial 当成全频体区逆，没有判定真实 \(\nu\) Schur 符号，也没有由小 mean 界推出非线性闭面存在。后续消费者须继续保留全部非平均反馈、真实外边界、各响应接口和未知高 Fourier 尾。
