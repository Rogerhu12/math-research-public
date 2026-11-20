# 原局部赋值的完整权界实现补丁

日期：2026-11-20。配套 [R925§19](../results/R925-original-ys-affine-rings-and-complete-divisor-ideals.md)。本项保存已经独立审阅的完整源码差异；当前运行的稳定 helper 不变，没有新的数学运行或性能回执。

补丁：[original-local-weight-bound.patch](../scripts/original-local-weight-bound.patch)。基源 `original_ys_local_value_tools.py` 的 SHA256 为 `a954fdaf928bda3d731ecd88eecf6d418aa11bd77d7f17f03dde1683a9f3a21b`；补丁 SHA256 为 `5ed1914a58ef68490433b344e0662434bb8fd536f5ee7446a654576fd69b5644`；应用后的完整目标源为20118字节，SHA256 `566f231e614f4b961cbd695318a159ee92b08a99de2da6f4c8786474e832b5a1`。

## 完整原对象与终止门

对调用者已鉴定的同一图表和完整306基，逐个非零坐标读取真实次数与原基权，置 `W=max(deg(a_i)+d_i)`。若原点的完整剩余域次数是 `d=[κ(Q):k]`，初始界准确为 `floor(306W/d)`。有限与无穷图表使用同一权界证明；这里绝不以相对基素点的剩余次数代替完整d。

先用原κ映射区分零与非零剩余；非零剩余立即给阶0。剩余为零时，从完整最大理想的平方开始倍增，遇到首次非成员后在实际括区中二分。理论界加一仅作终止哨兵。最后仍实际核元素属于全q^v并且不属于全q^(v+1)，两份完整HNF均记哈希；原q除q²参数、真实κ嵌入以及任意阶共零的612×306完整核没有修改。

此改变省掉仅为取得初始上界而先构造的完整主理想和范数。旧主理想方法保留在类中，不以未调用的方法或理论界冒称实际局部阶已付。最大被构造的理想幂指数至多2(v+1)，但单次完整理想运算的时间及内存仍须由公开运行读取。

## 已完成的源码复核与未来接入

root与独立审阅者核过两个图表、完整d、上界为1的端点、倍增/二分括区、最后两项成员关系和完整原receipt。已经做静态AST解析及针对当前基源的完整patch apply检查；未在本地运行数学。

未来应用方式是从仓库根运行：

```sh
git apply --directory=topics/rank2-sha-infinitely-many-p/scripts topics/rank2-sha-infinitely-many-p/scripts/original-local-weight-bound.patch
```

应用后须核目标源hash并由原公开Actions执行，继续保留全部原参数、源清单、闭点/厚度、归还原格和局部值接受门。本注没有启动重复作业。
