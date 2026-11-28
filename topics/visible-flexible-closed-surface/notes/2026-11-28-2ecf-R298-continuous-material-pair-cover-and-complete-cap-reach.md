# 完整材料点对覆盖与实际新帽的全局厚度

**已证明。** [R298](../results/R298-actual-entire-432-core-and-fixed-caps-complete-reach.md) 对同一 R296/R297 432 场支付全部闭核、准确平盘、完整新帽的嵌入与 reach≥.095。配合 D≤3.1644、两项强距离和固定握持集，全部强几何条件同时成立。该场独立 G11 的原度量误差约 .1529865061，故课题强精度仍未完成。

路径是从真实场新产生的完整非局部问题继续。先在同一实际图上取 82,082 点，33,534,220 个有序近对的最小法球比约 .1000677094，原帽的已证碰撞输入则由 R292 排除，不能混用。对 26,134,654 个更短弦配对，保守的材料坐标折线路径留下 28,288 对；材料坐标直线路径配合逐径段实际 Gram 上界，有限观察中全部通过。这些仅用于选择连续证明，均不构成 reach 下界。

首个连续覆盖将位置及 Gram 都取每象限 128 个角格，Python 树保存大量未决叶，在 3,200,000 次判定后进程 exit 137，未产生全域结论。随后真正更换证明网：位置每象限256角格、Gram每象限1024角格；先保存有 SHA 的完整闭盒，整数覆盖使用独立小型 C++ 程序、只保留前32个未决例及总数。该次完整自然结束，1,263,616 个闭盒、2,502,300 次节点对访问，未决为零。全部数学推导和路径条件见 R298，未把前一次中断算作通过。

## 字面重生

`S` 为本课题公开 scripts 目录，`W` 为已按 R296/R297 的源生产记录重生真实输入的目录。NumPy 及原 x87 区间核用于连续包围；C++20 编译器用于准确整数分类。闭盒、编译件和大数值数组只保存于运行环境，不提交仓库。

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python "$S/2ecf-released-complete-material-pair-cover.py" \
  --source "$S" --scripts "$S" \
  --state "$W/polar-released-cut-flat40-enriched.json" \
  --field "$W/polar-released-cut-flat40-enriched.npz" \
  --spatial "$W/polar-released40-genuine-floor-R293.json" \
  --edge "$W/polar-R293-432-true-Gamma95-F140-edge-ordered.json" \
  --ramp "$W/polar-new-gap-092-master-ramp.npz" \
  --quarter-angles 256 --gram-quarter-angles 1024 --radial-depth 2 \
  --output "$W/R298-complete-closed-boxes.bin"
g++ -std=c++20 -O3 -Wall -Wextra \
  "$S/2ecf-released-material-pair-cover-integer.cpp" \
  -o "$W/R298-integer-cover"
"$W/R298-integer-cover" "$W/R298-complete-closed-boxes.bin" \
  "$W/R298-complete-pair-cover.json"
```

[小型证据文件](2026-11-28-2ecf-R298-continuous-core-and-full-cap-evidence.json)包含源码与输入 SHA256、完整数组摘要、分类计数及准确比例。大闭盒 SHA256 是 `9193a4c2726195b8d32635806352395cb42cad2a814b30e91817277ee2636d5c`。核心曲率与形状依赖的 R296/R297 均为已登记的同场证明，本次不重算其结论。

本轮共享工作盘满时，首条待发记录的 git add 因 index 写入空间不足失败。将本会话公开 checkout 的 9,072 个文件共 226,861,181 字节逐文件 SHA 校验迁至独立临时位置，原工作路径保留符号链接，再完成原未提交记录；没有删除研究输入或把失败发布算成功。旧 Python 覆盖的资源退出与数值求解误差分别保留，均不影响上述自然结束的整型证书。
