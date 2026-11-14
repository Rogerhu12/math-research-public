# 实际五次样条 Newton：检查点复现及径向离散修复

2026-11-12，reproduce_newton。本文数值全部为双精度浮点探索，不是严格证书。

## 已复现输入

已保存的 `data/fourfold_mu4_weighted_radius_m16_checkpoint.npz` SHA256
`ec744ad6f20af237cefb9db0815933f8e4fd8252facf7bff7d95fcf8fb5b1e6f`
与元数据完全一致。不重乘物理幅度，使用 `make_candidate(series,1,1)`，
同一 evaluator 在 1201 径向点、256 角点得到

- 完整非均值度量相对算子范数采样最大值 `0.0069704960600942955`；
- 峰值位置 `x=0.0225, theta=0`；
- 直径代理 `2.3148186235253436`；
- 腰圈径向差 `0.12639431268165902`，比例 `0.054602253237952314`。

这些数字与 11-10 checkpoint 完全一致。原例没有收敛，也没有闭合固定帽。

## 同一函数的配置法

旧求解器以节点值为未知量，用八阶中心差分求节点的一阶导数；
保存后却改用另一个五次插值样条的导数诊断。两种导数在有径向高频时
不等，中心一阶差分在 Nyquist 波上为零，因此只增加角模和节点
不能排除近网格伪解。这里不是把该机制认作所有停滞的唯一原因。

新 `scripts/fourfold_newton_refined.py` 使用全区间对称五次 B-spline
控制点，偶的水平系数和奇的竖直系数由控制点反射精确实现。
设背景实际半径为 $a(x)$，三分量仍以
$U=a^4u,T=a^4t,W=a^3w$ 加权。配置方程、Jacobian、输出几何
都直接对同一组 B-spline 求导。没有把 ODE 右端冒用为样条导数。
全角非线性乘积保留至 $2M$ 以上足够的 Fourier 采样，但只将前 $M$
个正角模置零；因此必须另外报告全部实际输出频率残差。

背景及均值使用原始脚本的高分辨率五次样条表示；均值高度仍为
其实际斜率样条的反导数。所有 derivative 都来自相同值函数。
外端保留有限 Robin 代替最末 $xx$ 方程的旧边界，尚未付真实外部 DN 图。

先从原检查点运行了 201 正控制点、M16、同一 μ 与 ε=.06，结果如下。

## 节点收敛没有解决节点间误差

原 μ=4√2、ε=.06、M16、201 正控制点的 Greville 配置经过 8 步，
保留模配置系统达到 `4.4751e-11`，但从同一实际函数再检查节点之间：

- 完整度量采样残差 `0.0087439928452`；
- 保留角模自身在节点间仍有 `0.00368560014058`（m=4、xx，x=.4075）；
- 未保留角模最大系数 `0.00279953945005`（m=68、tt，x=.0225）。

因此一致 evaluator 只是必要修复。均匀 Greville 节点仍可能隐藏
接近径向 Nyquist 的导数振荡，不能说已消除径向伪解。M24/301
升频也未收敛，完整残差 `.00982716`、曲率样本约 `24.08`，保留失败记录。
正在以每个样条单元内的 Gauss 点作径向过配置，最小化全部输出角频
的实际度量残差。新脚本 `fourfold_overcollocation.py` 把腰圈第四模
的真实值作为线性等式精确消元，避免优化通过降幅到零虚假成功。
该幅度规范是 U4(0)=指定幅度，与旧的核投影幅度不同，必须重新算腰差。

## 作用量漂移与新背景对照

按真实 mean 曲线计算
$J=2\int_0^L\sqrt{(a''z'-a'z'')/(az')}\,dx$（只在根号为正的区间），
上面 M16 样条的 J≈.4606025059，参考背景 J≈.3884536338，漂移约18.6%。
这再次说明原背景谱隙不能直接转授给有限幅 mean。解析均值梯度
与 1e-6 中心差分相差约6.6e-8；128 与256点转折点消奇积分相差1.2e-9。
这是普通浮点 quadrature，不是误差证书。

独立新参数 μ=484/89（rational 谱背景）配原三mean、radius规范，
ε=.06 时有限系统仍约1.8e-5，实际样条残差 .0061000540，
腰差比 .05367736、曲率样本7.6371；未收敛，不能作为精确解。
对其另加 J=J0 和 radius 三个 mean 约束，ε=.02 时约束 Schur矩阵
接近奇异并停滞；去掉 radius 后到 ε=.03 仍未收敛，深度mean变到 .47，
直径代理约2.477、腰差比 .0244。宽支撑 mean 方向的低模横截与作用量
梯度近共线，正在考虑 R24 的不相交内/外方向，而不继续刷同一宽mean参数。


## 已保存的过配置检查点（可直接重启）

`data/fourfold_overcollocation_m16n101_waist006_checkpoint.npz`，39069 bytes，SHA256
`598fc957bcc8cd2aa958da3bc2f69d779fd055f7ee9fce39d968d33e4ff306d6`。
同名 JSON 给所有参数、三个脚本 SHA256、振幅规范和完整误差声明。
数据是同一个实际 B-spline 曲面的控制点与 mean 参数，不是 Taylor 系数。

这里 **U4(0)=.06** 由线性消元在浮点精度内固定；不是旧的
第四模核投影等于 .06。读取时 `SplineNewton(**metadata['parameters'])`、
`candidate(vector,metadata['epsilon'])` 即得完整实际函数，不再乘 .06。

求解目标是在每个正半轴样条单元的两个 Gauss 点上，把全部非零输出
角频（4至128）同时放入实际度量的加权 L2 残差，并保留有限 Robin 外端。
Jacobian 仅去除缩放后绝对值小于 1e-15 的双精度 FFT 噪声；
**非线性残差不作这项截断**。正规方程带对角缩放与阻尼，接受每步前
实际重算原非线性目标。正规方程的数值条件性没有被当作严格逆证书。

最新保存状态的独立实际函数采样（1301 径向点，包括配置节点之间；
264角点）为：

| 数量 | 浮点采样值 |
|---|---:|
| 完整非均值度量相对算子范数 | 0.0003520724199835597 |
| 保留角模最大相对系数 | 0.00006649572828435081 |
| 未保留角模最大相对系数 | 0.00004488859875930959 |
| 两倍最大模长（直径代理） | 2.415434369798905 |
| 腰圈径向差 | 0.13337591331872056 |
| 腰差/直径代理 | 0.055218189732815906 |
| 最大绝对主曲率 | 5.8150900768639815 |
| 最小支撑函数 | 0.8773626882734986 |

完整残差峰值在 x=.1125, theta=0；保留模峰值是 m=4 的 xx 分量，x=.485；
未保留峰值是 m=72 的 tt 分量，x=0。相对旧 `.006970496` 已有实际函数
层面的改善，但仍未达到精确解，也没有连续区间上界、闭面、固定帽或 reach 证书。

从仓库根重启（输出到可丢弃工作区，按需要另选输出路径）：

```bash
mkdir -p /tmp/visible-exact-overcollocation
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_overcollocation.py \
  --modes 16 --points 101 --gauss 2 --waist .06 \
  --start-cache topics/visible-flex-exact-nearby/data/fourfold_overcollocation_m16n101_waist006_checkpoint.npz \
  --linear-method normal --regularization 1e-9 --max-evaluations 8 \
  --cache /tmp/visible-exact-overcollocation/restarted.npz \
  --out /tmp/visible-exact-overcollocation/restarted.json
```

每个改善步都会原子替换小型 checkpoint。`--max-evaluations` 对 normal 方法
表示最多正规 Newton 次数；所有实际残差试算另外写入 history。
先前 LSMR 版本在第28次残差评估时被 SIGKILL（exit137），没有得到完整
末态数组；可重做的参数为同 M16/101、Gauss2、waist .06、LSMR250次，
而它前6次已到约5.7e-5加权最大张量残差。该未保存末态不是成果输入。
这里保存的是随后重新计算并逐步 checkpoint 的正规方程版本。

下一项是同一实际函数的径向/角频细化，尤其分别压低上表的保留模节点间
残差和未保留频率。不能只用 L2 目标值或配置点读数替代实际函数检查。


## 已保存图的实际 mean 作用量与实现核查

SHA256 `598fc957...` 的过配置图不是前述 Greville 图；它的实际 mean
作用量为 `J=.4396673732396`、`J/pi=.13995047153463`，
正势半区间为 `[0,.21968543265681117]`。128/256/512点消奇积分的值
相差不超过约2.3e-12，但没有区间舍入证明。梯度数值约
`(.2553774,-10.1536,2.69396)`；不能沿用旧图的 J≈.4606。

实际过配置 Jacobian 做了一次有针对性的方向核查（M4/35控制点、
包括振幅及可选 mean 高度消元）：中心差分步长1e-5时，最大误差
1.44e-13、相对L2误差3.63e-14；步长减到1e-7后出现通常的浮点消减，
最大误差1.71e-11。这是实现检查，不是无限维右逆证明。

为避免显式巨大 Jacobian 在加密时占满内存，normal 方法现在按各
样条单元的局部支撑以 BLAS Gram 乘积组装同一个 $J^TJ$、$J^Tr$。
小型 graded 对照中，与显式稀疏乘积的最大条目差为7.11e-14
（矩阵最大条目8552.93），梯度最大差1.52e-18。再按径向块排序求解，
不改变非线性目标。显式Jacobian的151点/Gauss3试验又出现 exit137；
该轮已经逐改善步保存，后续从保存状态恢复，没有丢掉已得控制点。

## 继续细化的口径

新增 `--mesh graded` 使用对称节点
$x=L\sinh(3s)/\sinh(3)$，将径向自由度集中在实际核心；全部曲率、
度量和后验诊断仍来自同一个实际样条函数。
M16、151正控制点、每单元3个Gauss点的恢复运行，六步后实际采样完整
度量残差为 `.0002817748452`，D代理2.48907、腰差比.0533508、
最大绝对主曲率5.41289。保留模系数仍约8.58e-5，未保留约3.74e-5；
不能只因L2代价下降就说已收敛。接下来是同一图真正升到M24，
并同时监测腰圈实际 $\det II,N$，避免回到错误的核心类型。


### graded 检查点与下一次真实升频命令

已额外保存，不覆盖原101点图：
`data/fourfold_overcollocation_m16n151_graded_checkpoint.npz`，57830 bytes，
SHA256 `cfde01e091aeb06e98fe709e52dd921fc114be45aa86c964e7a3eb21dd3d497a`。
同名 JSON 含参数、实际函数复算、源哈希。用1351个径向点/264角点
重新检查得完整误差 `.0002817731463`；腰圈实际二基本形式样本
$\det II\in[-1.467285,-.963550]$、$N\in[-6.002026,-.420508]$。
这些仍只是样本。与前一表的1648点诊断差异来自径向采样集合不同。

从这个完整状态继续做当前已启动的M24升频：

```bash
mkdir -p /tmp/visible-exact-overcollocation
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_overcollocation.py \
  --modes 24 --points 151 --mesh graded --gauss 3 --waist .06 \
  --start-cache topics/visible-flex-exact-nearby/data/fourfold_overcollocation_m16n151_graded_checkpoint.npz \
  --linear-method normal --regularization 1e-7 --max-evaluations 8 \
  --cache /tmp/visible-exact-overcollocation/m24-graded.npz \
  --out /tmp/visible-exact-overcollocation/m24-graded.json
```

若只继续M16径向状态，把 `--modes` 改16、regularization改1e-8；
这两个命令都直接加载保存的实际控制点，未要求重跑已丢失的试验末态。
本会话工作区当前M24逐改善步检查点为
`/workspace/scratch/f6a2c7886477/newton-experiments/over-block-m24n151.npz`，
对应 `.log`、结束后的 `.json` 记录迭代。工作区不是永久数学输入，
若末态未另推送，可从上述已入库状态和命令重做。

## M24 的已保存实际改善与内存诊断

上述 M24 运行完成两个改善步后再次 exit137，但每步原子保存已生效。
对单步对象生命周期的独立探针显示：Gram 组装后 RSS 343 MB，
正规矩阵缩放及排序后494 MB，LU 峰值约638 MB；解完删除旧正规矩阵和
SuperLU 引用后降至131 MB，额外 `gc`/`malloc_trim` 后120 MB。
旧循环在下一次组装时仍持有前次三个正规矩阵和 LU，因而叠加内存。
现在每次解线性方程后立即释放 LU，每轮结束、最后重组梯度前释放矩阵。
这是内存生命周期修复，没有改方程。恢复 M24 后四步已完整退出0。

新永久检查点为
`data/fourfold_overcollocation_m24n151_graded_checkpoint.npz`，86453 bytes，
SHA256 `68fb488b57083caa61e94cee7682bf55e1930bb3cac88e44f0bfe903ff4bf918`。
它仍固定实际位置系数 $U_4(0)=.06$，没有改变为核投影振幅。
从已保全的两步 M24 状态以初始正规化1e-6再做四步，末步正规化
3.333333333333333e-7；全部接受步按原非线性残差验证。

| 同一实际样条量（1648径向点、392角点） | 新 M24 样本值 |
| --- | ---: |
| 完整相对非均值 metric 算子范数 | 8.894228882859246e-5 |
| 已表示模系数最大值 | 2.0864310032892925e-5 |
| 未表示模系数最大值 | 1.2329695192745538e-5 |
| 两倍最大模长（直径代理） | 2.572728038981886 |
| 腰圈径向差 | .13223860910040397 |
| 腰差/直径代理 | .051400150772537616 |
| 最大绝对主曲率 | 6.283762207785889 |
| 最小支撑函数 | .9205235963849843 |

完整误差峰值在 $x=.04623800259,\theta=0$；保留模峰值为
$m=4,xx,x=.4775$；未保留模峰值为 $m=104,tt,x=.01$。
腰圈实际二型样本仍有
$\det II\in[-1.540413,-.965999]$、$N\in[-7.273236,-.462742]$。
均值参数为 `(.785168947678,-.002127513976,-.059323364267)`。
相对前一 M24 两步状态，完整误差从2.33908e-4下降，但 mean 漂移使直径
代理继续上升，可见性比已降至.05140，后续不能只最小化L2而忽视此余量。

从永久状态续算：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_overcollocation.py \
  --modes 24 --points 151 --mesh graded --gauss 3 --waist .06 \
  --start-cache topics/visible-flex-exact-nearby/data/fourfold_overcollocation_m24n151_graded_checkpoint.npz \
  --linear-method normal --regularization 1e-6 --max-evaluations 4 \
  --cache /tmp/visible-exact-overcollocation/m24-continued.npz \
  --out /tmp/visible-exact-overcollocation/m24-continued.json
```

所有误差与几何极值仍是浮点样本。这里既未得到无穷频率解，也未构造
固定帽闭面、严格连续误差界或 reach 证书。
