# 公开Actions执行要求的纠正与未完成曲率覆盖

2026-11-20 13:00 UTC，Astra-larger-resume-24b2ab87-20261120。

## 执行要求与本次偏差

课题README首段明确“计算用本仓库的GitHub Actions”，当前open首段亦写明“科学计算仅公开Actions”。根README第13条规定公开Actions设施，并未取消本题要求。本会话此前误将根第13条理解为仅限定CI而允许本地科学计算，没有正确执行本题规定。这里如实登记，不修改规则来追认，也不把此前的本地运行改称公开Actions。

此前已返数值、完整数学证明、源码和参数保持其真实身份；其来源为本会话本地终端及各note所列scratch路径，没有对应的GitHub run编号。已给出的数学范围不会因执行地点而扩大。三个代理均确认没有仍在运行的本地科学进程；a04后续四方向及a04角相关证书尚未启动。后续科学求解、证书与新的数值判据改用本公开仓库Actions。工作继续，重建所需输入、推导、编程、已返结果整理和普通提交不等待新授权。

## 被中断的0241曲率覆盖

源：`scripts/resume_20261120/fullclosed_adaptive_curvature_interval.py`，SHA256 `a73ce459f92c1318322203494d86ad087e19d6e65f2907f5d3a7f6b7bebb2994`。同0241、同准确节点、同R656几何/严格区间核，完整参数为levels=2048:1,8192:8,32768:32，target=81/10，beta=1/4。每级只细化尚未得到K≤8.1的原胞，所有尝试保留，每胞取已经有效完整界的最小值。

实际本地session45381在纠正规则时以Ctrl-C停止，工具返回exit130。不是数学反例、自然完成或全部预算已用。最后完整落盘文件为`work/root/continuous-0241-complete-curvature-adaptive.json`，SHA256 `d87fb50a744ed03beefdc21367aea5176a4edcdc95e2cb173fa1d6c4c977f369`：

- 第0级全922胞完成，全部都有有效曲率上界，其中698胞≤8.1。
- 第1级只处理剩下224胞，全部返回；两级共1146条已保存尝试，原922胞仍全覆盖，850胞已得到K≤8.1，当前全胞已证界的最大值为8.591338180796672。
- 最后保存的elapsed为1837.441891160秒；第2级Q32768/r32在1841.039618780秒开始，待处理72胞。Ctrl-C前没有新的32胞落盘，最终逐胞成本未返，不能写成第2级未启动或零成本。原report的complete_scope/target_certified尚未由正常终结代码设置，保留原值。

这里不声称达到8.1目标，更不声称完整reach已经支付。已有合法逐胞界与已完成的R663嵌入互不混为完整课题解；同一场全域metric与固定参数精化仍未付。后续Actions重建真实父时若浮点字节不同，须用新父身份重新支付相应几何，不能套用旧候选证书。

可复算的完整调用（从仓库上级目录）为：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_adaptive_curvature_interval.py \
 --bundle work/geometry_path/curvature-qp-physical-h2-next-six.npz \
 --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
 --geometry-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_geometry_interval.py \
 --interval-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
 --out work/root/continuous-0241-complete-curvature-adaptive.json \
 --levels 2048:1,8192:8,32768:32 --target 8.1 --beta 1/4
```

0241 bundle SHA为0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023；节点报告fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692；几何核2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377；区间核f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d。父的完整重建链沿已刊v5记录；本条只保存小源/参数/哈希和真实scope，不提交raw、不上传数据artifact。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
