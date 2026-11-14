# 共同3Db的宽5窗口函数链恢复

日期：2026-11-13。状态：固定整数计划已经准确核验，真实369节点群运算尚在进行；不是完整高度。

R178的真实起点与初始主函数不变：Ainit=3Db+div(hD)，hD=Rg1²h³²⁴/Fbuild。完整24步证书见 `scripts/data/p41_translation_build47_complete.json.gz`，SHA `80126f2679fe969fbe1c83dd6ecbc0ff4490871310b5d4304945232308b95f33`。

同一个R121整数m用宽5有符号数字展开；最高数字3，数字长度303，但m本身仍为304位。17个预计算节点给±1、±3、…、±15及±2。整个固定DAG含303次double、57次其他AddFlip、9次flip，共369节点；原二进制算法为454次AddFlip。每个节点独立用整数递推 nR=−nP−nQ（flip为−nP）展开，最终准确为m。没有改变乘数、起点或R179最终点。

源 `scripts/p41_translation_window_slp47.py`，16113B，SHA `33f1cfe0cd3f821a29f1b72682a0a1c5cb61a1648ea0a2881207b43b2f1c45d6`。固定计划 `scripts/data/p41_translation_window47_plan.json.gz`，13953B，SHA `d48df95d4e29bd05efb14e6217f82b9b288c6fbe0a77bdcc9a3ce1808d8dae8a`；内部plan摘要 `b48fdd6b755320cf1347078aa352ad3b97acf24073b7b75b6541f4e4fcc3d38e`。

保持 div(Fnode)=nnode Ainit−Anode。AddFlip使用 Fnew=(Fleft Fright s/f0³)⁻¹，flip使用 Fnew=(Fleft s/f0²)⁻¹。每步的真实二次/三次系数都转回R102原基、检查有理Frobenius并保存SHA，不能只保留整数计划。

rolling为 `/tmp/p41_translation_window47_rolling.json.gz`，预计算完整点只单独保存一次到 `/tmp/p41_translation_window47_precomputation.json.gz`。每个完成节点原子保存当前完整点、所有函数节点、固定游标、符号、原始RNG及预计算文件摘要；第17节点之前cache仍在rolling内。后续节点只使用缓存奇倍点和当前点。

从课题目录，原样恢复命令：

```
python -B scripts/p41_translation_window_slp47.py --script-dir scripts --initial scripts/data/p41_translation_build47_complete.json.gz --checkpoint /tmp/p41_translation_window47_rolling.json.gz --precomputation /tmp/p41_translation_window47_precomputation.json.gz
```

若scratch丢失而尚无发布的窗口前缀，按同一源码和计划从完整24步起点重做新窗口；两条CM已保存的180/140位不重做。预计算完成后应保存其不可变文件与当时rolling快照，再更新本笔记及HANDOFF。原 `p41_translation_slp47.py` 二进制源作为准确基线保留，但没有运行过的完整结果。

最终函数必须为 fD=Ffinal/(gtr hD^m)，div(fD)=3mDb−Aformal。R179已经给family1的正负目标，不应重新求指数；先做真实终点主函数再取范数。完整窗口和最终高度目前都未完成。
