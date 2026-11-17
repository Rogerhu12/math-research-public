# 同一规范化 pulse 的五个完整加权支撑代表片

2026-11-17，parallel-geometry，AI 辅助。**状态：在所列四个原胞、五个精确分片上的连续区间证书已完成，全部严格正。** 只消费原有完整报告，不重采样。本条不是全 818 胞支撑结论，也没有闭曲面或 reach 声明。

## 1. 固定对象、已有输入和唯一实际执行

实际原场为 `parallel-pulse-a5-complete-base.json.gz`，SHA256 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。保存的 mesh/value/first/second jet 按 little-endian binary64 拼接 SHA 为 `840193a1cdb37f79d04f5f36f5a0c485c4eb50f3fd2a103af8c4c267d5232793`，字面定义 M320 的共同 C² 五次场。

消费的是既有 qN4096 规范化像

$$G=c+\lambda(F-c),\qquad c=(0,0,Z_0(s)),$$

其中 lambda 及 lambda_s 的严格界直接取自 R648 全 819 片索引 `parallel-pulse-gram-fixed-recovery/result.json`，SHA `df41433b71147ac11d3f0193be31323d7e23a879cb2b05231d3a3e166b0d88fb`；每片来源 d0661f3d 的完整报告和 SHA 均随本次结果保存。没有重新积分标量、重求有限均值或 lambda，没有把 raw F 的支撑误称为 G 的支撑。

固定 $A_\beta=\operatorname{diag}(1,1,1/4)$、原点中心，实际非单位法向取 $N=G_\phi\times G_s$。每个片固定 Q8192、4 个闭径向子片。唯一调用按 `0/all,390/all,498/all,817/before,817/after` 执行，session3038 自然 exit0；没有加密、重试或删去失败项，全部五片均通过。

第817原胞按准确标量开关

$$s_*=1-5/2^{60}=1152921504606846971/1152921504606846976$$

分成 before/after。先按原胞宽形成真实五次位置及 s 导数，再以准确 Fraction 参数作 de Casteljau 限片。末极短 after 片没有重新除以其极短宽，也没有重新计算两份 lambda 证书。

## 2. 完整径向、角向覆盖的含义

每个固定 s 的真实归一化一 jet 为

$$G=c+\lambda r,\qquad G_s=c_s+\lambda r_s+\lambda_s r,\qquad r=F-c.$$

把该片 lambda、lambda_s 的已证区间作为参数盒注入原径向 Bernstein 系数；在每个真实 s 处取其实际参数值，便属于这一统一包围族。未把 lambda 当 s 常数求导。$G_\phi$ 从同一 G 作真实物理角导，含旋转标架连接项。

随后采用 R643 §8 的连续分量覆盖：旋转正交架中的每个分量作为普通角函数频率至多 640，直接包围其一、二阶普通角导数，付最近角节点距离 pi/Q 的 Taylor 余项；径向控制凸包覆盖整个闭子片。A_beta 与该旋转架交换，故在分量盒内直接组成 $N=G_\phi\times G_s$，再逐角局部盒计算

$$S_\beta={(A_\beta G)\cdot N\over|N|}.$$

这里支撑乘积或除法本身没有被冒称为频率640；它们在连续分量盒内作向外区间运算。每盒先检查真实 $|N|^2$ 下界严格正，再除以其区间平方根；不采用全域最小分子除以全域最大法向长度的松化。所用 f512c96c 区间 FFT/四则算术与 R643 分量法未修改。

## 3. 实际全部结果

| 原胞/精确片 | 连续 $S_\beta$ 下界 | 连续 $|N|^2$ 下界 |
|---|---:|---:|
| 0/all | 0.4540989654778905 | 0.027558630439173323 |
| 390/all | 0.31916547418203745 | 0.03649878563728698 |
| 498/all | 0.40542443267387895 | 0.03761821379048482 |
| 817/before | 0.40541552466686065 | 0.03772933909800895 |
| 817/after | 0.40542069642938644 | 0.03772971039568278 |

每片的 `unpaid_normal_boxes`、`nonpositive_support_boxes` 均为0，`all_radius_and_angle_covered` 与 `strict_under_stated_IEEE_arithmetic` 均为真。表值是报告保存的向外 binary64 端点；对这五片的并集可以直接取更宽的有理下界 $S_\beta>319/1000$、$|N|^2>27/1000$。不能把该并集下界填给尚未读取的其余片。

各片记录的几何耗时依序为 3.70716、2.89680、2.29621、2.93057、2.28026 秒，合计约14.111秒，含首片建立区间变换的成本。耗时是此次观察，不是算法性能保证。

## 4. 固定来源与后续批次

- 新 reader `parallel-geometry-weighted-support-interval.py`，19497 B，SHA256 `f1158760756728ed1cbbdb419ed88a8d47bea2f5fba070bf4c1d7de43d3cfe6b`。
- 唯一完整聚合报告 `parallel-geometry-weighted-support-representatives.json`，27191 B，SHA256 `48d5d0523e0fb3d0d850ccc543cdc25d74feab387c002354fbf85a99f0b03e52`。
- 先行只读绑定报告 `parallel-geometry-weighted-support-bindings.json`，SHA256 `d2cde89275c7baf63b5762a65e5d3b0dce5f77f9353bd4a5f202f8048c75ef09`；该步没有运行 Transform 或几何读取。
- 区间基础源 `parallel_20261117_arclength_interval_positive.py`，SHA256 `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。
- 分量覆盖来源 `2026-11-17-parallel-root-pulse-curvature-component-box.py`，SHA256 `459dc01e8e5a7fb2b1910c2f0fb028f196eb0921855386c3858c26ba13a33afc`；只复用其已证数学方法，没有调用它重算曲率。

实际从原 scratch 工作目录运行的参数为：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 parallel-geometry-weighted-support-interval.py \
 --input parallel-pulse-a5-complete-base.json.gz \
 --interval-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
 --gram-index parallel-pulse-gram-fixed-recovery/result.json \
 --component-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-pulse-curvature-component-box.py \
 --entries 0:all 390:all 498:all 817:before 817:after \
 --out parallel-geometry-weighted-support-representatives.json --execute
```

可重算 raw 报告留仓库外。后续固定819片 wrapper97a707839c3ef45fb47ae9a9d844e0f8f293cb65b4cdd481f84bc48079740f0f/plan a2acf3719692e360f8e5a4d0dce1777882494a05286700ae82c5ff7a5561899b 原样消费这五个 record，只补其余814片；本条不提前给其终态结论。两次进程使用相同 reader、同 q4096、同 Q8192/4sub，代表及 lambda 均不重复。

R638 的正角坐标变换只正倍缩放 N，故单位支持量属于同一归一化像，不依赖是否使用该材料重参数化。此处仍是带边前缀；R650 的完整闭参数球面、整个未付尾/帽及全域实际曲率输入均不能由五个代表片替代。
