# R105/R107 原生完整输入恢复

2026-11-13，visible-exact-astra-ac0d。状态：五个原入口实际完成；没有用旧执行收据重建缺失矩阵。

运行环境 Python 3.12、python-flint 0.9.0、NumPy 2.3.5。执行命令从本课题目录运行：

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_replay_native_core_2256.py \
  --out-dir data/native_core_20261113_ac0d
```

脚本按原顺序完成低块对称分解、175 叶真实有限核心传播、whole-eta 切口 Fourier、40 行强 Gram 和六维组合。完整 JSON 与 NPZ 均保存在上述目录。每份报告保留实际输入哈希、精确参数域及原程序的完整状态标识；这次不是从四舍五入摘要恢复证书。

## 实际结果

- 真有限偶核心 DN 误差小于 `0.025382309`。
- 六维组合原有全部已付误差小于 `0.002442476`。
- 完整已付 Banach 乘积小于 `0.154315098`。
- 中心端帽下，已付有限六维逆范数小于 `74.708434`。
- 真参数帽额外相对 form 费用的充分允许值大于 `0.01141230544`。

这些外取数值均直接弱化完整报告中的 Arb 有向端点。有限角子空间与完整高模反馈的区别保持不变：这里没有证明被遗漏高度通道或无限高低 Schur 补可逆。

恢复的 `family_quarter_cut_strong_Grams.npz` 为 40148 字节，SHA256 为
`a35c292d980fdf9dc072dc5e66b02aeed6a82d14f808d75cfc920536df8bee09`，
与旧 01:02 收据及 22:56 记录精确相同。新 core/切口 JSON 含真实运行时间及本次路径，因而不要求它们的序列化哈希与旧文件一致。原数组及当前完整证明入口各自保留在报告内。

## 后续消费

R111 真实 body `[1/4,3]` 的原生恢复正在独立运行；main 中已存在的 322 段 graft 将由原 collector 检查后接入。只有该完整报告与本次六维原报告真正合成后，才能把旧 `entire_actual_parameter_family_certified=false` 更新为同一有限子块的全参数结论。即便此项成立，完整 PDE 强逆和非线性精确化仍须继续。
