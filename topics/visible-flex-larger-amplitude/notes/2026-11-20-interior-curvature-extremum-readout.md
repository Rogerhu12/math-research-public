# Gauss 点之间的实际曲率峰：两个新候选的局部位置优化

2026-11-20 UTC，Astra-larger-resume-24b2ab87-20261120。**有限数值读出，不是连续上界，也不是 reach 证书。** 这是从新观察集的最坏点出发，在同一真实 quintic 胞内部寻找另一个实际点；没有重算旧全域审计，没有改变候选、度量或标量。

## 1. 为何需要这一次读出

R655 已指出有限径向采样不自动控制完整非线性 Gram 或曲率。新增每胞六 Gauss 行消除了原节点/中点的特定精确盲空间，却不意味着曲率最大值必在这些点上。新约束求解的最大曲率位于胞821，且其必要乘积接近数值筛选线 `.98`，因此直接检查这个新峰的胞内位置有具体必要。

这里的 `.98` 是求解器留给连续覆盖和后续构造的数值余量，不是 README 的新完成标准。真实必要条件仍是 `.03 D K≤1`；超过 `.98` 而未超过1，不能宣称 reach 不可能。

## 2. 实际场及计算

新源 [read_closed_local_extremum_20261120.py](../scripts/read_closed_local_extremum_20261120.py)，SHA256
`f376c058fd9d931ee4df6dabf68cbabc93e8e6c0b61cb15a1b2c20fd9f135456`。

它直接消费原完整闭场仿射 `pack/unpack`，用现有六端口 Hermite 权在任意局部坐标 $u∈[0,1]$ 读出真实 $(q,q_s,q_{ss})$，再使用原 dense 算子的角向合成及包含旋转标架连接的两阶角导。完整解析 lift 为

$$F=q+\chi(s)\{(R+S-s)e_r(\Theta(\phi))+He_z\}.$$

计算 $F_s,F_\phi,F_{ss},F_{s\phi},F_{\phi\phi}$ 后，由实际第一、第二基本形式求两个欧氏主曲率。没有把参考标量 $a$ 的采样值当成实际第一基本形式；几何读出无需另问 $a$。

半径、节点和端口在这一数值读出中仍按求解所用的 binary64 载体计算，不将它冒为严格符号 $\alpha S+\beta$ 模型的向外界。严格连续核另行处理这些输入误差。

以原最坏点的 $(u,\phi)$ 为起点，用有界 Nelder–Mead 最小化 $-\max(|\kappa_1|,|\kappa_2|)$，边界为 $[0,1]×[0,\pi/2]$。`xatol=fatol=2e-10`、`maxiter=300`。`success=true` 仅表示该优化器的停止条件满足，既不证明这个点是局部最大值，也不证明它是整个胞或整个曲面的最大值。它只给一个新找到的、可重复求值的实际曲率点。

## 3. 两个真实结果

| 项目 | 首六步2038 | 续十二步3a3 |
|---|---:|---:|
| 起始 stage / angle | 6772 / 208 | 1643 / 5 |
| 同一 parent cell | 821 | 821 |
| 起始局部 $u$ | .16939530676686776 | .5 |
| 起始曲率绝对值 | 7.935384160596277 | 7.978713227413113 |
| 新点 $u$ | .10619286662269253 | .42224930597422994 |
| 新点 $s$ | 1.0132013196831464 | 1.0145445595503904 |
| 新点 $\phi$ | .6370952763981583 | .016682618788290776 |
| 新点最大曲率绝对值 | 7.991357693366212 | 8.09521095710513 |
| 传入完整体 $D$ 点下界 | 4.087221451205496 | 4.09152646644 |
| 新点 $.03D_{\rm lb}|\kappa|$ | .9798734576574735 | .9936530964723217 |
| 优化迭代 / 函数求值 | 91 / 191 | 69 / 149 |

两次初始曲率与原全 Gauss 读出差小于 $4.1×10^{-13}$，这是实际新任意点计算接口的必要一致性观察。两次进程都自然 exit0，分别耗时约 .52/.57 秒，包括输入读取；并非旧完整场再采样。

首父仍通过这个额外已知点的 `.98` 筛选，但它的余量明显小于 Gauss 最大值所显示的余量。第二父的 Gauss 乘积为 `.979353490142`，新点已达到 `.993653096472`：它仍小于真实必要界1，但不能继续声称它通过包含这些已知新点的 `.98` 筛选。

因此后继求解把任意胞内位置接入几何约束及真实线搜。它们不必加入度量目标，因而无需改变已声明的正权目标或重算同 $g$ 的标量载体。若从第二父向 `.98` 恢复，线性约束右端可以为负；旧的“向零收缩修复”此时不合法，因为零方向不是可行点。后继必须实际恢复，或回到已知通过这组点的2038父；不能隐去这些点。

## 4. 来源与复现

共同观察载体 SHA256：`71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`。原 dense 源 SHA256：`e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`；Hermite/观察源 SHA256：`26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d`。

两个输入分别为：

- `work/geometry_path/curvature-qp-gauss-six-step.npz`，SHA `2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`，按[首六步配方](2026-11-20-curvature-qp-gauss-six-step-result.md)重建。
- `work/geometry_path/curvature-qp-gauss-twelve-step-02.npz`，SHA `3a3f77c9363ec866c4f8e12d294d226ef2f9d7bbabfbe258819a009177c8477c`，由同源从首六步父续12步、携带其同载体有界点记忆所得。

设置 `repo` 为仓库、`topic` 为本题、`work` 为仓库外工作目录；首父准确调用为：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/read_closed_local_extremum_20261120.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-gauss-six-step.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --stage 6772 --angle 208 --diameter-point-lower 4.087221451205496 \
 --out "$work/root/gauss-six-step-local-curvature.json"
```

第二次将 bundle 改为第二父，`--stage 1643 --angle 5 --diameter-point-lower 4.09152646644`，使用新输出路径。两份实际报告 SHA256 分别为 `e36b039f6cdca4954b105d64fe50ea1624019a94c8912d1298b287f997bf45fb`、`d89a71494f93d81e9a958e81a9687bc20a82740a2c171cf798b54661bc70a571`。完整实际报告仅保 scratch；上述源、输入身份、参数和结论足以重现。本条没有新增严格存在、全域上界、闭面 reach 或相位振幅结论。
