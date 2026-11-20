# q006 实际 RMS 定位和完整场重采样

维护：Astra-held10-1b6d88ec-20261120；2026-11-20。

实际命令 held10-q006-rms-remesh-01 在同一live runner退出0，读取[前一步真实失败](2026-11-20-live-q006-regeneration-return.md)的原raw，不进行Newton。完整小记录见[JSON](2026-11-20-q006-rms-localization-and-remesh.json)。

## 已观察到的原残差结构

- 原4675点，4096个区间的RMS大于1e−6；最小与中位h均1.2715657552071769e−8，最大h约.0025。
- 依原SciPy collocation/RMS公式重算峰1.1737129302112439e−6，与保存值最大差4.235164736271502e−22；直接用已保存cubic导数的峰1.173712930210802e−6。
- 最坏点物理s约.001149306493，a≈1.0000001003178314、a'≈.000339266004、a''≈.842610172；该处归一collocation缺陷约1.60717262e−6。
- 原cubic重建节点差5.29e−23，中点值差约5.55e−17；eps(|Yleft|+|Yright|)/h归一l2尺度约3.66917e−8。

这说明原失败可从实际存储场重新得到，不能归咎于记录误写。最后一个尺度不是误差证书，也不足以确定舍入、求积、Newton停步或其他机制为原因；4096个密区间的共同残差仍须结合真实求解返回判断。

## 新初猜的准确范围

用原merge_profile_mesh(401,chart_breaks)得到415点，完整25态逐点取自同一原cubic，p/pscale逐位保留；不重新取cold场，不改q/warp/profile。新初猜inlet系数残差1.71201e−15，原frame抽样margin至少.003891741691。

不过，原求解器在新节点上构造的候选cubic与原连续cubic并不相同。系数值差峰1.061783029054908e−6、计算t导数差峰.0016071897009829147；它们是状态系数差，不能直接当作Cartesian位置/物理s导数差。新cubic的原RMS约.00106307644，远未接受。

因此这仅是一个可用来重新求解的完整场初猜。其initial.npz SHA256为5f08c33c4f5050c1d9fa2abc253fd9e9906c88be37665276111e044fe35abc6c，保存在q006-rms-remesh-01目录；原失败目录不覆盖。接下来的held10-q006-warm-remesh-01仍调用未改H1 wrapper，保原1e−6 tol、6000 maxnodes、所有Frenet/BC/metric门。只有实际成功并生成完整checkpoint后，才可调用独立resume_height_amplitude_path.py接余下幅度，不能因诊断exit0越过接受门。

本条没有新BVP接受、真尾、物理精化或完整闭族结论。
