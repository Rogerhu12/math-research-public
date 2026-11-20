# R674 新解析尾的抵消保持 relative-Gram 消费者

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**状态：源码与公式接口已完成，只有语法编译和源码阅读；尚未科学执行。** 新源为 `scripts/resume_20261120/exact_reference_tail_relative_gram_interval.py`，与首几何/六 jet 源分开保存。它不改此前已执行的优化器、旧 R657 或新首几何源码。

依据：[R657](../results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)、[R671](../results/R671-exact-reference-tail-affine-lift.md)、[R674](../results/R674-reference-tail-continuous-profile-and-same-angle-remainders.md) 第6节，以及[新首几何核接口](2026-11-20-exact-reference-tail-continuous-kernel.md)。本文件把 R674 的紧 Gram 公式接成完整消费者；不是把首几何入口的宽 `--mode metric` 改名。

## 1. 固定依赖与准确输入

新消费者绑定：

| 角色 | 源 | SHA-256 |
|---|---|---|
| R674 新解析 profile 与实际模型身份 | `exact_reference_tail_interval.py` | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |
| R657 分子、多项式乘积和闭角弧公式 | `fullclosed_relative_gram_interval.py` | `5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13` |

上述源及其全部小源码依赖均在本课题 `scripts/resume_20261120/` 和原 `notes/`、`scripts/` 中，均由实际 checkout 读取。输入必须是 R671 factory 生成的 canonical bundle、同一 node report、原 scalar 输入；可选同 field 的 reference carrier。新 profile reader 逐项确认实际 $\lambda$、准确符号 $\eta$、mesh、$M$、原 scalar 与 dense/batch/observed 源身份。

原 $g$ 仍为 $ds^2+a^2\rho^2d\phi^2$。$a$ 不替换成 Taylor 多项式；原 $q$ 和全部角模不丢弃。完整解析 $e_r(\Theta)$ 也不截成一个有限目标场。

## 2. 抵消先于范围界

令本子片同一个 Taylor profile 为 $\widehat f,\widehat Z$，并记

$$
U=q_s,\quad T_0=q_\phi,\quad c=\widehat f_s,\quad d=\widehat Z_s,
\quad F=\widehat f,\quad A\simeq a.
$$

先准确形成三个分子

$$
|U+c e_r+d e_z|^2-1,\qquad
(U+c e_r+d e_z)\cdot(T_0+F\rho e_\theta),
$$

$$
|T_0+F\rho e_\theta|^2-A^2\rho^2.
$$

它们仍为 R657 的 $P+C\cos\delta+S\sin\delta$ 形式。所有径向乘积和抵消在 Bernstein 系数处完成，准确 $e_r\cdot e_\theta=0$ 在乘积前使用；角导数0至4阶及非带限第四导余项继续按原核支付。新 profile degree10 可令分子升到20次，所有乘法及升阶都由实际次数决定，没有旧的 degree6 或 degree12 上限。

旧 `piece[4]` 只表示旧 $\chi$ 是否 active。此处不以它跳过新 lift，因为 $\eta$ 在更早的节点已经生效。

在 $\lambda=1$ 且整片 $\eta=1$ 时，$F$ 与 $A$ 是同一个形式 Taylor 多项式，故 $F^2-A^2$ 准确等于零。源码直接删除这个相同项，不对两份共同区间系数做独立减法。它没有把 $a$ 当作 $A$，也未擅自将 Taylor 的 $\sin^2+\cos^2$ 置为1；后一部分仍由相同 profile 和全部误差付清。

## 3. 新 scalar 误差与目标 scalar 只各付一次

原 R657 `relative` 先用准确 $a\in A+[-\varepsilon_a,\varepsilon_a]$ 和真实 $\rho$ 作归一化，并支付目标分子 $A^2-a^2$ 的差。因此得到的近似场矩阵 $\widehat E,\widehat M,\widehat G$ 已对应准确目标 $g$。

从这三个已经抵消的盒取

$$
B_V\ge\sqrt{\max(0,1+\overline{\widehat E})},\qquad
B_W\ge\sqrt{\max(0,1+\overline{\widehat G})}.
$$

它们分别包围 $|\widehat V|$ 和 $|\widehat T/(a\rho)|$。实现用原向外 `sqrt`，包括对区间下端的零截断。

新 profile 给出 $e_{f,r}$ 与 $e_{Z,r}$。置

$$
\epsilon_V=\sqrt{e_{f,1}^2+e_{Z,1}^2},\qquad
\epsilon_W=e_{f,0}/a_-.
$$

第二式在取界前准确约去 $\rho$，避免小 $\rho$ 处不必要的放大。将三个近似条目分别扩张

$$
\Delta_E=2B_V\epsilon_V+\epsilon_V^2,
$$

$$
\Delta_M=B_W\epsilon_V+B_V\epsilon_W+\epsilon_V\epsilon_W,
$$

$$
\Delta_G=2B_W\epsilon_W+\epsilon_W^2.
$$

这里不再重复加目标 $a-A$ 的费用；它已由 `relative` 支付。随后用原准确对称 $2\times2$ 谱范数公式，得到真实新场相对准确 $g$ 的连续上界。

同一已付误差也用于子片端点与准确角网格点，故可输出当前场连续误差 supremum 的严格下界。该下界仅说明本候选不能靠继续细化证书来降低真实误差，不是对整个自由空间的无解论证。

## 4. 源码入口与完整 CLI

```python
reader = module.make_reader(
    repo=repo, bundle=candidate, node_report=node_report,
    scalar_input=scalar_input, reference_carrier=profile_or_None,
    angles=8192, radial_subdivisions=16, scalar_degree=5, panels=128)
record = reader.certify(cell)
```

前半部分在 $\eta=0$ 的整胞直接用原 R657 公式在当前候选上重新计算；不会复用旧候选界。活动尾每次径向加密在新符号中心重建同一真实 $a/I$ Taylor jet。报告给出实际最大分子次数、每项 scalar 费用、角四阶费用、同候选上下界、最坏位置及耗时。

以下为一个明确选择 `cell=900` 的首次局部命令模板；它只是完整参数示例，尚无运行结果或该胞优劣结论。`candidate` 与 `reference_profile` 必须来自公开 Actions 中本次真实 R671 输出。后续选择其它胞或 `all` 必须在实际命令中明示。

```bash
python "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_relative_gram_interval.py" \
  --repo "$repo" --bundle "$candidate" \
  --node-report "$runwork/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$runwork/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --reference-carrier "$reference_profile" \
  --cells 900 --angles 8192 --radial-subdivisions 16 \
  --scalar-degree 5 --panels 128 \
  --out "$runwork/postprocess/reference-tail-tight-gram-cell900.json"
```

`--cells` 是必需参数，可为逗号分隔原胞号或 `all`。默认角数8192、每个准确联合片16个径向子片；不隐式启动全922胞高成本运行。新的 FullHold profile helper 内部使用256角/24模来建立其完整 Laurent 辅助信息；本 Gram 的实际角覆盖始终为明确请求的8192，并保留全部原 $M$ 模。profile 的这一辅助角设置不被用作 Gram 证书。

同一原重建的 scalar 输入与 node report 路径如上。若载体经过已证明的径向精化，应显式改用该精化的实际 node report 和 canonical bundle；保持原 scalar 输入。可省略 `--reference-carrier`，改由原整数 oracle 查询需要的符号中心。

## 5. 报告与范围

每个原胞结束立即写同一完整 raw 报告，并输出紧凑一行实际上下界和耗时。报告绑定实际 bundle/node/source/model SHA，记录 Actions run 身份、真实峰值内存及全部已覆盖胞。raw 留 Actions 工作目录，不提交仓库或 Release。

只有明确覆盖全部原胞且全域上界不超过 $10^{-6}$ 才置 `metric_certified=true`；两平帽度量不变，镜像保持 Gram。选定胞上界不能被解读为全曲面界。此源不支付嵌入、reach、marker，也不证明求解器在固定 $g$、参数与 $t$ 下随网格/频率精化收敛。

没有本地科学运行，没有实际新场数值结论或旧证书重跑。完整候选结论须以公开 Actions 的真实返回为准。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
