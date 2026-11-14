# 完整首相位浮点探针与端点外推失败

2026-11-12，visible-exact-astra-f6a2。**全部相位数字仅为诊断，未得到β区间证书。**

## 固定对象与实际算子

使用type_fixed_step02完整冻结snapshot
`data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz`，
SHA256 bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532。
不作Gaussian；物理β与半径显式偶平均、γ与准确坡度积分Z显式奇平均，
与symmetric-root-interval笔记定义同一无限R33对象。计算程序采用Q256有限原函数，
所有三角/FFT/积分/浮点值均未被宣称为该无限对象的有向证书。

R37使用χ=1覆盖负核心，并固定
ℓ=∂θlog(Fz/r)−∂θlog|F|。完整零阶项用R50(50.21)的角分部公式，
未把它删掉；a,b、ω与目标K0均由同一个图计算，使用实际面积密度。
四重角n=4j的往返β由半核心积分乘1/2。root和独立audit逐式核对了
对称化、真实Z坡度、旋转基叉积、d、K0′、所有相位符号及这个频率因子。

浮点有限原函数的root为.23836991573140587，位于另已证明的真实根区间。
root之外严格区点值只需几何三jet；积分在所有原knot及其反射的共同167个
径向cell内分别作Gauss，不跨knot假设高阶光滑。原函数使用Q256quarter。

## 为什么没有得到相位证书

程序把G(ρ)=ρ^(5/2)〈J〉在[η/4,η]拟合成多项式，再外推到0求有限部分。
这一步不是R50要求的实际root Taylor包络。Chebyshev外推会放大浮点噪声，
浮点root误差也会通过δroot/ρ污染G；拟合格外的很小误差不能界定端点外推。

|角节点/Gauss阶|η|拟合次数|β浮点值|
|---|---:|---:|---:|
|64/6|1/2048|5|36.80691472|
|64/6|1/2048|7|36.80446850|
|64/6|1/4096|5|36.81535648|
|64/6|1/4096|7|36.66179353|
|128/12|1/2048|3–6|36.80230904至36.80480666|
|128/12|3/4096|3–6|36.80018075至36.80875520|

最后两行是相应四次实验的范围，不是准确β的上下界。不能据此把一个数值送进R34
并称危险格已避开。特别最小collar的高次数拟合明显不稳定，失败结果原样保留。
初轮的样本还给min ζ约.82785、min面积1.18524、max实际N约−.42564、
minFz/r约1.10889、max|ω|约.22857；这些节点门亦不代替连续区间门。

## 保存与重做

源 `scripts/fourfold_phase_beta_probe.py`；保存全部初轮和细化输出：

- data/phase_ring_continuation/type_fixed_step02_beta_extrapolation_initial.json；
- data/phase_ring_continuation/type_fixed_step02_beta_extrapolation_refined.json。

JSON记录源、几何依赖和完整输入SHA，包含每次bulk/collar值、系数、离网格差及限制。
从仓库根目录可按下列命令重做，不写入任何已有candidate：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_beta_probe.py \
 --frozen-inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
 --angles 128 --gauss 12 --collars .00048828125 .000732421875 \
 --fit-degrees 3 4 5 6 --out /tmp/sym-step02-beta-probe-refined.json
```

初轮改--angles64、--gauss6、collars为.00048828125/.000244140625、fit-degrees5/7。
接下来使用真实rootspan的Taylor/κ除法及R50有界积分，另写新入口，保留本探针
作失败诊断。也可用准确height ζ使µ变为径向√(−K0)，但必须同时转换完整d。
实际D5/D8候选不等于本snapshot，β不能未经误差预算直接迁移过去。
