# 真实首cell的混合方程与显式插值诊断

会话：`true_a_analysis`。本批固定的是既有 `−.0781 H` 接受尾的第0个完整物理cell，不是新的闭曲面，也不是更大幅度的联立结果。原非线性尾为M8、角求积128；本cell包含18个shooting子段。两端约束固定为真实外端高度v、真实内端动量t；改用物理坐标时同一约束逐点可逆变换。

最外checkpoint节点的momentum在原程序中已经重标度。恢复时严格按 `createCompactTailDN.cutJets` 将该节点momentum乘 `rho=2^a`；其它stage输入使用原存储值。这项尺度在导出器中有明确代码。完整mean根和所有表示的模式均保留。

## 完整单元和固定g比较

原factory直接给每个节点的r,w,w_r，统一参数为 `x=r_outer-r`。每个原stage内部按其原参数取网格端点，再以实际r的中点放置Hermite–Simpson中点。这样不会把不同stage参数的r_x跳跃混入物理场。独立参考使用不可变原momentum引擎，从每个真实stage内端状态积分；参考RK允许原cusp分割，并记录每段高精度流与原shooting端点的小差。

|坐标/网格|完整根相对残差|ODE残差|相对独立参考状态差|最小A|
|---|---:|---:|---:|---:|
|v,t；每stage 8区间|1.65e−15|1.43e−16|.03114|.15439|
|v,t；每stage 16区间|2.37e−14|1.28e−15|.006717|.06536|
|v,t；每stage 32区间|7.95e−14|2.49e−15|.001561|.01561|
|v,t；16点余弦端点加cusp|1.59e−5|7.38e−7|.002632|−.01823|
|h,p；每stage 16区间|1.58e−15|1.07e−18|5.00e−5|.0027367|
|h,p；16点余弦端点加cusp|9.18e−15|1.48e−18|2.75e−5|.0029068|

第四行Newton line search失败，未通过接受门。其负A不是精确等距曲面穿零的证据。其余行仅通过有限混合方程的残差门。h,p的连续等价变换见 `physical_coordinates_derivation.md`；它改变了径向collocation坐标，没有改变g、角求积、原momentum密度或零模。

## 必须保留的坏插值结果

先把v直接作三次Hermite、L作二次，再还原物理高度，会在原脉冲端点极薄的w_r变化层制造严重的导数误差。16/32区间的实际Cartesian最大曲率约为4.24e4/8.01e4，虽然节点代数残差已很小。最坏例在raw segment6→5接口，背景w=.02，端点w_r=0，但隔很小的r就达到约−6。已知背景尺度1/w的强变化不适合被这种低次v多项式吸收。

仅对这些v解的节点数据事后改成物理H插值也不能修正问题，因为该节点数据并未满足H自身的离散积分关系。此后处理的实际metric甚至超过1，所有数值均保留，未筛去。

真正改用h,p边值离散以后，再用物理H显式插值，情况明显不同：uniform16的实际曲率约8.0400，接近原参考8.03997；但metric约3.68e−4、完整Cartesian张量缺陷约.922，rr接点跳约18.8。graded16的曲率约35，仍不合格。**这些低次插值没有支付C²。** 不能用从ODE假设重算的height rr替代实际插值的rr。

`cartesian_interpolant.py` 用二阶前向微分代数直接微分其实际角展开图，不借Gauss方程替换rr。独立中心差分核对了位置的一、二阶导数；`audit_actual_cell_cartesian.py` 对每个径向区间的左右极限及中点同时检查全部Cartesian二jet、Gauss/完整张量、接点跳跃。基准Cartesian图调用原 `f6tail_relative_spatial_jets.mjs`；其平面rr仍是原四阶差分，因此明确记录差分尺度。背景w_rr也保留两个差分步的差异，未将其当作区间误差界。

下一项针对性改进是R11已有的共享Cartesian位置/一阶/二阶jet五次插值。它直接给显式C²图，避免把高度节点残差误读成全Cartesian正则性。该项尚不属于本批结果。

## 复现与出处

`actual_cell_manifest.json` 固定所有新源码及40个原依赖的历史commit/SHA。`actual_cell_completed_scalar.json` 收录全部完成行、失败行、各原segment的最坏指标、命令参数和原始输出SHA；状态、Gram矩阵、角点数组及大轨迹不在交付中。

先用恢复器将原源放入仓库外scratch。原 `−.0781 H` checkpoint按已发布 `nonlinear-tail-stage1` 的原向量延拓方案再生；本次确切输入SHA在紧凑记录中。不可把不同高度向量或物理参数的tail state贴成同一输入。每次复现也可以显式传入自己已持有的同参数接受checkpoint。

```bash
python recover_actual_dependencies.py --repo REPO --scratch SCRATCH
node export_actual_cell.mjs SCRATCH/bundle/topics/visible-flexible-closed-surface INPUT_CHECKPOINT CELL.json.gz 16 256 0 1 uniform
OPENBLAS_NUM_THREADS=1 python probe_actual_cell.py --input CELL.json.gz --coordinates physical --out CELL-mixed.json
OPENBLAS_NUM_THREADS=1 python audit_actual_cell_cartesian.py --input CELL.json.gz --solution CELL-mixed.json --representation physical-height --out CELL-cartesian.json
```

`8/16/32`、`uniform/cusp-cosine`、`normalized/physical`分别是明确的离散参数。原始 `.gz/.npz` 在scratch生成；含路径、时间的输出SHA不要求跨平台逐字相同，应比对所述方程、参数、源码和误差指标。

## 依赖闭包实际启动核对

本v2仅补不可变原依赖 `general_root_smooth_tail_cells.cjs`，原数学代码、已完成运行记录和历史源码不变。已从空目录恢复全部40个文件，并调用冻结导出器实际组装factory、导出18个stage共37节点。该动态require只做 `git show` SHA核对无法检出；实际完成记录见 `dependency_smoke_scalar.json`。
