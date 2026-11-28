# 完整原 collocation Jacobian 的低临时内存装配

原 SciPy 装配先构造两份全量 COO 索引、多个全尺寸块和拼接副本，再转 CSC。本次独立入口直接按原有行列位置填最终有序 CSC，所有状态、全部参数、边界行和显式零均保留；径向临时块为16。每个元素沿用原公式及运算顺序，参数 midpoint 数组的原位更新也保留。未修改已绑定的 V5、原方程或验收门。

实际检查使用已保存真 λ=.002/M24/879 节点的全部输入，64191×64191、10912470存储项。新旧装配器以及此前保存的真实完整矩阵，其 data、indices、indptr 逐位相同；NPZ SHA 均为 `28abf787e7f94ea3424ee1e0d2a9fc5839589698920c5872d3459674d382fe53`。安装后的原 prepare_sys 入口也实际调用并核同，原参数中点副作用逐位一致。完整记录见 [JSON](2026-11-28-design-complete-csc-assembly-bitwise.json)。

真对照运行66.19秒，峰810204KiB；单次新装配0.2364秒。该峰包含原／新／历史矩阵核对，不是未来 M48 BVP 的峰保证，也不把既有137/-9归因为已经确定的某个分配。

独立源为 `design/direct_csc_collocation.py`、`design/prefix_csc_assembly_driver.py` 和 `design/check_direct_csc_assembly.py`。高阶路径 n>50 仍调用原逐节点 np.dot；小阶保原整批 einsum。检查只证明这次实际完整矩阵身份及该入口的存储改变，不是新 Newton、接受解、区间逆或闭族完成。
