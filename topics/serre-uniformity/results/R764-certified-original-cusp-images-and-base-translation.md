# R764 原全部尖点像与原基点平移的实际证书

日期：2026-11-14。状态：**精确计算完成**。公开 [Actions run 43626804312](https://github.com/Rogerhu12/math-research-public/actions/runs/43626804312) 成功，核心时间 0.440895936000004 秒。新算术只在 Rogerhu12/math-research-public 的 Actions 执行。

## 1. 原完整 Hom 格上的实际结论

保持原 $X=X_1$、$c_0$、$c_1=4424$、R735 正目标 $C/L:y^2=x^3+b$ 和 R759 的完整整数周期格。
令 $P$ 是原参考 coset 0 的 cusp，$f_{0,i}(c_0)=O$ 是十二个真实整数格基映射，且
$f_{P,i}=f_{0,i}-f_{0,i}(P)$。

此次全部 19 条既存树边的精确周期合成、全部 20 个 cusp 的树路径、十二个实际映射和原次数纤维余数均核验成功，得到
$$
\boxed{
f_{P,i}(C)=O\quad\text{对全部 20 个 cusp }C\text{ 及 }0\le i<12,
\qquad f_{P,i}(c_0)=O.
}
\tag{764.1}
$$
所以
$$
\boxed{f_{P,i}=f_{0,i},\qquad f_{0,i}(P)=O.}
\tag{764.2}
$$
完整原整数 Hom 格的 $c_0$ 平移线性泛函准确为
$$
(\nu_{0,0},\ldots,\nu_{0,11})=(0,\ldots,0)\in\mathbf F_3^{12}.
\tag{764.3}
$$
因 R759 确实给完整整数格，(764.1) 的尖点消失与 (764.3) 也对它的全部整数线性组合成立；没有仅从某一条选定微分外推全格。

实际选中的零起始第 4 个映射次数 $d=1206$。从原参考 cusp 恢复其函数后，已经满足原 $c_0$ 基点条件，无需非零三挠点平移。**此次尚未计算这个函数或原 $c_1$ 的 $\beta$ 坐标，也未计算高度。**

## 2. 完整规范与树周期

预运行算法和全部符号证明见[原方法](../notes/R764-original-cusp-periods-and-base-translation-method.md)及[R762](R762-original-mu3-quotient-and-single-function-map-recovery.md)。

原 $K=\mathbf Q(\zeta)$，$\operatorname{Im}\zeta>0$，$L=K(b)$ 是原七次模型，周期坐标序是 $1,\zeta$，实际标度为 $R_C/\Omega_0$。三个可能的固定点按原实分支记作
$$
T_0=O,\qquad T_1=(0,-b_{1/2}),\qquad T_2=(0,+b_{1/2}),
\qquad b_{1/2}=-U^{20}S(U)^3/8.
\tag{764.4}
$$
本次没有重新选择根、相位或目标模型。

读取 R738 保存的 19 条 dual-tree edge；正向始终为
$\operatorname{cusp}(gS)\to\operatorname{cusp}(g)$。
将 R759 每个实际微分 $h_i=\sum_jv_{i,j}\omega_j$ 与同次 R754 的六个相对周期精确合成：
$$
\lambda_{e,i}=\sum_{j=0}^5v_{i,j}\Pi_{e,j}.
\tag{764.5}
$$
程序在原 $L=K(b)$ 中准确乘加，然后检查全部非恒定 $b$ 系数严格为零，才能视为 $K$ 周期。沿原树路径求全部 $\lambda_{C,i}=a+c\zeta$，再核
$$
(1-\zeta)\lambda_{C,i}=(a+c)+(2c-a)\zeta\in\mathbf Z[\zeta].
\tag{764.6}
$$
两个整数坐标之和模 3 给 (764.4) 的 $\nu$。每个映射的二十个标签全部为 0；不存在浮点投影或猜测小分母。

所有 cusp 标签及下述 $c_0$ 标签，还用 R759 真正的列作用 $\zeta$ 矩阵验证了
$\nu J=\nu\pmod3$。完整矩阵、周期和树路径按阶段 SHA 保留。

## 3. 原 $c_0$ 的平移由实际次数唯一确定

R762 已证明原 deck 的固定点恰为 20 个 cusp 和 $c_0$，源和目标在这些点的切向特征均为 $\zeta$。因此固定点处的局部次数为 $1\bmod3$，非固定源轨道在固定目标纤维中贡献 $0\bmod3$。

令 $n_{i,\nu}$ 是第 $i$ 个映射的 cusp 标签计数。对实际次数 $d_i$，
$$
d_i-n_{i,\nu}\equiv [f_{P,i}(c_0)=T_\nu]\pmod3.
\tag{764.7}
$$
此次十二个映射的完整输出如下：

| 零起始映射编号 | 实际次数 | $(n_0,n_1,n_2)$ | $(d-n_0,d-n_1,d-n_2)\bmod3$ | $f_P(c_0)$ |
|---:|---:|---|---|---|
| 0 | 1485 | (20,0,0) | (1,0,0) | O |
| 1 | 1602 | (20,0,0) | (1,0,0) | O |
| 2 | 2448 | (20,0,0) | (1,0,0) | O |
| 3 | 1521 | (20,0,0) | (1,0,0) | O |
| 4 | 1206 | (20,0,0) | (1,0,0) | O |
| 5 | 1836 | (20,0,0) | (1,0,0) | O |
| 6 | 1206 | (20,0,0) | (1,0,0) | O |
| 7 | 1485 | (20,0,0) | (1,0,0) | O |
| 8 | 1521 | (20,0,0) | (1,0,0) | O |
| 9 | 1485 | (20,0,0) | (1,0,0) | O |
| 10 | 1206 | (20,0,0) | (1,0,0) | O |
| 11 | 1206 | (20,0,0) | (1,0,0) | O |

每行恰有唯一余数 1，故 (764.7) 唯一确定 (764.1)，并非从“三个点中任选一个”恢复基点。本次不需要另算 $c_0$ 端点积分。

## 4. 真实运行、来源与逐文件绑定

| 项目 | 实际记录 |
|---|---|
| run / attempt | 43626804312 / 1 |
| source commit | 6d685485fe4a6b186355d2482deb6fb5ba8144d9 |
| 完成时刻 | 2026-11-14T18:28:55.806244+00:00 |
| 核心源 SHA-256 | a2e77a39369d3021718e246087c532838da3da345f3335e12023a6960e5f3d97 |
| 方法 SHA-256 | 5d6e283bd8262af8cc6280a411850280b7ad6d4573b8c3674ab596deb36ba9aa |
| 正式 request SHA-256 | c97146b149687fdc56d5b438cc92ccd068c2bef85681b023ebf1e838f261972c |
| 最终证书 SHA-256 | f23a1e1ee3059d5608edffc3e53d739fce6bb553c9449e04330b267e4b7c588a |

实际生产者保持：

| 生产者 | run / source | 消耗文件 SHA-256 |
|---|---|---|
| R754 | 43620862489 / b36d2c58b39f42a694236d48f64444bb6fe1d0af | 证书 da4ef0eeac285da5cf32ad1372155dbb9d03917c18044b81b8236fac6e51107c |
| 同次 R754 | 同上 | 原相对周期 510a6928725df736d29d812513110c8d2542f191d8ca9bfcf0feb14ac1931ec2 |
| R759 | 43625474728 / 4728e6868e2509556e5c60e138fd97c9b4120d8e | 证书 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |
| 同次 R759 | 同上 | 原微分/次数 037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |

核心还核 R759 内部引用的 R754 证书恰等于本次实际 R754 证书。R735 模型、R738 原陪集及原闭链输入 SHA 分别为
752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574、
6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161、
d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf。
wrapper 核两个真实生产者的 manifest、run/source 和每个消耗文件 SHA。旧模型、拓扑、周期、Hom 核、整数格及次数均未重算。

## 5. 产物与下一步的准确输入

[公开小证书和全部 receipt](../computations/R764-original-cusp-periods-and-base-translation/43626804312-1/)保存执行边界。完整 manifest SHA 为
eb360b3a963a0cc32401bdc22536c050dc44bb0b27a09b11463b558f3fb7626f；
core receipt SHA 为
7752b15bb90348e1ea589e77addf388ee10d82e025080732f1c405ec037be451；
run receipt SHA 为
13e1a631aa352acd9e739d319beb868365c00c20ee925a887ae4f05d4e8467e2。

完整 artifact 名
serre-global-R764-original-cusp-periods-and-base-translation-43626804312-1，
ID 14127135207，ZIP 12850 字节，ZIP SHA-256
9785f587da96bfa88ad5cdea747fc62f14295e1db01c86a979a3a88f951e26c2。

| 完成阶段 | 字节 | SHA-256 |
|---|---:|---|
| R764-nineteen-original-tree-edge-periods.json.gz | 1823 | 53ab45f1b3d4cbd73b27466b64d06a1c0076e47663ca8129bb70ce9727f0a93a |
| R764-all-original-cusp-labels-and-c0-translations.json.gz | 3298 | 166680cdf27b89bfd9e8773eee51ac19fd59dea5f19c58a8fa7a497289b69eb0 |

两阶段保存全部精确周期、20 条原树路径、240 个 cusp 标签和完整平移泛函，只在 artifact 保留坐标。后继直接复用，完成计算不重跑。

对真实 $d=1206$，R762 商上恢复参数为 $m=2$、$D=2(t)_0$、$M=2846$；此任务按原通用界输出 RR 基至 $q_Y^{4052}$、$h/dQ$ 至 $Q^{13362}$。后续若利用更精确的真实 cusp 首阶与完整极点次数，可严格缩短前缀；这些输出不等于已算完 RR 基。

现接原低权模形式/RR 基、实际 $y_P=y_0$ 及原 $c_1$ 的 $\beta$ 求值，再到真正高度与全 $p$ 排除。主目标仍 OPEN。

依据：[R759 实际整格及次数](R759-certified-original-integral-period-lattice-and-map-degrees.md)、[R762 原商与平移判据](R762-original-mu3-quotient-and-single-function-map-recovery.md)、[R764 预运行方法](../notes/R764-original-cusp-periods-and-base-translation-method.md)及上述同源公开产物。
