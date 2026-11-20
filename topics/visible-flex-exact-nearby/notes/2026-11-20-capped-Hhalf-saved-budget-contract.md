# R138：截顶曲率 H^(1/2) 已成 X/Y 小标量消费者

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

## 唯一新目标及现有输入

公开入口为 `scripts/fourfold_codazzi_capped_Hhalf_saved_budget.py`，由
`scripts/fourfold_codazzi_capped_Hhalf_saved_budget_public_worker.py` 执行。
它只读取完整 X `44737045152/1` 与完整 Y `44740320925/1` 的 actual 和
execution，共四份已成 UTF-8 小文件。读取的是四份完整文件，不是提取的
旧数字片段；原全部身份、scope、4651 完整闭格、旧失败门及输出哈希保留。
无旧 native、binary part、数组恢复，无旧脚本 import，无旧 ODE、frame、
primitive、积分或已成科学 target 调用。

数学依据为
[Z](../results/R138-supplement-sharper-outer-lift-and-capped-curvature-energy.md)
和 [GB](../results/R138-supplement-capped-curvature-Hhalf-Grushin-and-root-budget.md)。
两者已解析证明

\[
K\ge\min(46x,1/40),\quad
\|z\|_{L^2H^{1/2}}\le\tfrac52\sqrt{\mathfrak G_{cap}}
                       +\tfrac3{\sqrt2}\|z(L)\|_2,
\quad \|\omega_R\|_2\le\tfrac85\sqrt B .
\]

根端保持自由、环境零模完整保留。同一个 Qrepair、实际物理角、实际
`DF(Qrepair)`、固定 `p=e_z/2`、原全频外图、mean 及原区间不变。

## 五个新上界

从 X 读取 `C_E,C_H,A_Theta,Gamma,h_B`，从 Y 读取 `h_E,E_0,E_1`；
每个输入采用原完整整数十进制球的有向上端点。严格按以下顺序生成五球：

\[
\begin{split}
w_E^{(1/2)}&=\tfrac52\Gamma\sqrt{A_\Theta}
                         (\sqrt{C_E}+\sqrt{C_H}h_E),\\
w_B^{(1/2)}&=\tfrac52\Gamma\sqrt{A_\Theta C_H}h_B
                         +\tfrac{24}{5\sqrt2}A_\Theta\sqrt\Gamma,\\
a_{EE}&=E_0(w_E^{(1/2)})^2+E_1w_E^{(1/2)}h_E,\\
a_{EB}&=2E_0w_E^{(1/2)}w_B^{(1/2)}
                    +E_1(w_E^{(1/2)}h_B+w_B^{(1/2)}h_E),\\
a_{BB}&=E_0(w_B^{(1/2)})^2+E_1w_B^{(1/2)}h_B.
\end{split}
\]

记录名依次为 `wE_half_upper,wB_half_upper,aEE_upper,aEB_upper,aBB_upper`。
每个输出先取有向上端点，再以 `mid_rad_10exp(75)` 保存完整整数
midpoint/radius/exponent，原子写盘，读回整个输出文件，核包含后才把保存球
的上端点交给后续式。三个 body-only 门由**保存后上端点**判定：

\[
a_{EE}<2,\qquad a_{BB}<1,\qquad
a_{EB}^2<4(2-a_{EE})(1-a_{BB}).
\]

成功指五个完整新预算均计算完成；不以 body 门为真作为科学执行成功条件。
false 不等于算子奇异。旧 X/Y 两组原 false 门在新输出中原样保留，未修改旧文件。

## 条件性的第六个目标

仅当上述三个 body 门全部通过，才读取旧 Y 的同一 `r_E,r_B` 完整球上端点。
它们来自原 `H^(2/3)` 到根 `H^(-1/3)` 的路径；新的体 `H^(1/2)` 绝不替代该路径。
令

\[
M=\begin{pmatrix}2-a_{EE}&-a_{EB}/2\\-a_{EB}/2&1-a_{BB}\end{pmatrix},
\quad r=(r_E,r_B)^T,
\quad C_{allow}=\frac{\det M}{2r^T\operatorname{adj}(M)r}.
\]

本输入的 `r` 非零，分母必须经有向比较严格正。商先取有向**下**端点，
按同一完整整数球写盘及读回核包含；记录 `C_allow_lower` 的资格来自读回球
的下端点。后继实际根型若支付 `C_*≤saved_lower`，则
`M−C_* rr^T≥M/2>0`。此处不计算、猜测或免费授予 `C_*`。
若任一 body 门 false，第六目标明确标记未计算，不留下伪零下界。

## 公共执行及保存

精度 320 bits，沿同一已成运行的 Python `3.12.14`、python-flint `0.9.0`。
新增依赖为零。全部 admission 与完整四文件身份检查先于数值 import。
新的消费 marker 必须实际 push 成功，才允许启动唯一科学 child。工作流只
接受 run attempt 1；发现 marker 后不重试科学。无本地科学运行。

worker 直接沿已成 GH4 的运维逻辑：部分 clone、实际 `pull --rebase`，
每次 pull 核根和本题 README 的实际差异及已读提交号，科学期间每 1800 秒
一次实际 pull；新未读规则则停止后续科学并完整保留已成 prefix/回执。
每次发布以实际公开 topic tree 加完整本地 delta 核算 200000000 字节上限，
保 120000 字节余量。推送拒绝立即再 pull/rebase/push，循环至成功；
即使 index 无新差异也仍 push 可能尚未发布的提交。

唯一科学输出为 `capped-Hhalf-body-budget.json`，schema 显式固定；完成时
恰为五个 mandatory 记录，或 body 门全真时六个记录。中途失败保留所有已经
完整写盘的标量前缀与实际失败原因，不能把前缀当完整。科学输出、执行回执、
简短 report 原样公开且记录完整哈希，不用 artifact 或 Release，不公开新数组。
没有 full inverse、非齐次两 RHS、实际根型或总题完成资格的转授。

生成 metadata 的命令（不导入科学入口）为：

```bash
python scripts/make_capped_Hhalf_saved_budget_manifest.py \
  --repo /path/to/math-research-public --source-dir /path/to/new-small-sources \
  --out /path/to/new-metadata
```

公共 child 接口与 GH4 相同：`--manifest --manifest-sha --input-map --output --checkout`。
仅 metadata 生成器可在本机执行；科学入口要求仓库公共 Actions 环境。
