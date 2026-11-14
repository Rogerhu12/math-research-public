# 完整moving连接几何：可恢复消费者与未执行范围

2026-11-13 23:29 UTC。源码
scripts/fourfold_codazzi_moving_connection_frame_probe.py
已保存；**平台执行环境不可用，本次尚未运行它，也没有新的几何数值结论。**

## 1. 消费的准确对象

只读同一完整[0,25/8] moving候选。默认要求原ac1d5b98…索引SHA，
逐片加载器核对全部五片SHA、大小、节点连接和完整系数形状，
再核对真实目标、COORDINATES、α/ν准确有理元数据。
若实际重放得到新科学数组，须明确给新expected SHA并重做其后验；
输出不能冒称原ac1d证书。

程序直接按
[R133准确moving连接](../results/R133-supplement-moving-frame-with-complete-residual-and-mean.md)
积分F,X,Y,N。对完整u=αU、v=s+αV、m=〈v〉、d=−βI(u²+Kv²)，
使用τ=dv/m−γu和
(p,q,t)=(βτ/γ,a(γKv+du/m),ad/m)。
因此每个角样点不再反解physical角，也不把φ当作θ。
全部2M primitive、3M连接和真实mean保留；N>6M只解决这些有限连接的卷积支持，
不支付积分后标架的无限角尾。

外端圆与旋转标架按真正θ_R(φ)=φ+I(v−m)/m锚定。
这只是明确的参考世界锚；真实帽与它的位置/法向差仍欠。
完整B、C及Cmean与参考差写入报告，不以近零抹去。
径向积分后的腰只作一个共同常量高度平移，
不强制投到平面、不重置frame、不做静默正交化。

## 2. 每一真实分片与续算

径向网格包含全部原PPoly节点；每一步的两端和中点
明确使用同一个实际原片的多项式，保留真实单侧值。
每个原接口还同时观察左右两侧的φ连接和model径向方向。
不能用默认右连续PPoly在一次跨片RK4步中混淆端点。

每64个完整径向行保存一个不可覆写的压缩块，含：

- 该块全部r索引、F、frame N、左右两侧重构样本法向；
- 最后一行的完整12维F/X/Y/N；
- 累积角约束、Gram、metric、formal曲率及chart观测；
- 前块SHA、完整候选/源/目标/模块/网格/运行库身份。

块本身即检查点，原子改名后才算保存；无需只存在内存的监督器。
恢复时逐块核对完整hash链、连续且不重叠的索引、所有形状/有限值、
末状态与几何末行，并从其后第一条未成行继续。
源码或目标身份变化不能悄悄接用旧块。已保存块与失败报告均保留。

完整块只存实际scratch工作目录；它们是可重建中间，不复制入Git。
最终只选择64个径向截面，源码预先限制未压缩几何数据小于4.8MB，
并核对最终单文件不超过5MB。

## 3. 观察量及不能提前授予的结论

全部角导数使用四重协变Cartesian Fourier微分。
检查Fφ=avY/m、Xφ=AY+BN、Yφ=−AX+CN、Nφ=−BX−CY，
以及完整moving第一基本型和frame Gram误差。
每一真实接缝的左右两个样本法向都进入最终支撑扫描。

curvature字段明确是候选formal第二基本型的主曲率；
并非未解重构浸入的严格真实曲率。N512的角微分混叠、RK4连续误差、
原PDE残差和θr−τ差都未因采样消失。
这些费用只能由
[全状态校正到完整几何定理](../results/R133-supplement-moving-state-correction-to-complete-geometry.md)
及实际连续预算接入。

完成到腰后才得到共同高度平移；随后扫所有完整保存行，
统一计算位置模、两侧法向支撑和π/4旋转腰见证。
最近样点搜索包括四个绕轴转像和上下反射，避免只比较一侧。
但采样最近距离仍不是连续最近距离下界。
若腰jet尚未精确匹配，反射对象只是诊断点云，不能称闭C²面；
R以外真实tail/帽、固定四marker尚未包含。

## 4. 实际恢复后直接运行

从topic目录运行，以下路径只是独立新尝试的位置：

~~~sh
PYTHONPATH=scripts OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_moving_connection_frame_probe.py \
  --candidate /dev/shm/visible-exact-ac0d699811ad/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --checkpoint-dir /workspace/scratch/ac0d699811ad/moving-connection-fullR-blocks \
  --max-new-rows 512 --angles 512 --step .001 \
  --out notes/2026-11-13-R133-moving-connection-fullR-attempt001-floating.json \
  --geometry /workspace/scratch/ac0d699811ad/moving-connection-fullR-sampled-geometry.npz.gz
~~~

若complete=false且无failure，下一次同参数加--resume，
只把--out改成从未存在的attempt002路径；继续到全部行完成。
若failure非空，保留真实失败、检查它指向的具体门再修复；
不能把普通退出0与wholecomplete混同。
现阶段源码尚未执行，不宣称Python导入、数值门或上述sampled报告已成功。
