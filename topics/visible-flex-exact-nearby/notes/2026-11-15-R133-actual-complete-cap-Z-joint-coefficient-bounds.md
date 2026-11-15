# 实际完成：完整帽区连续方向 Z 的逐系数联合界

本记录消费公开 Actions run 43674204314 / attempt 1 的真实输出。数学子进程返回 0，10 个门全部通过，完整帽区 $[9/10,25/8]$ 的 660 个原三次片已经逐片消费。此结论是同一完整连续方向 $Z$ 的新联合上界；它不是新的 PDE 解、全频逆或参数 Schur 结论。

## 1. 原对象和此次新增范围

原完整 193 状态物理 trial index 为 data/current_root_phase_response_20261114/response-full.json，SHA256：

ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6

本次只读取该索引的两个完整原 shard：

| 原文件 | 原字节数 | SHA256 |
| --- | ---: | --- |
| response-full-part012.npz.gz | 2698989 | 777337c853329f26719b148e34db079c5ca0ed34991aa40220f25624e4af0b3c |
| response-full-part013.npz.gz | 1517845 | 4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037 |

它们从已成功的原 prepare run 43583838026 / 1 的 artifact visible-exact-body-prepared-43583838026-1 恢复，原 artifact ID 14109363064。恢复仅复制并校验原字节，没有重建 trial。

连续修补只消费既成 notes/2026-11-14-R133-explicit-continuous-response-direction-native.json.gz，原 SHA256：

87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88

同一完整方向定义 SHA256：

6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04

本次读取其全部 193 个 exact_complete_repair_coefficient_suprema，包括槽 96 的独立 even mean。没有把全区修补上界冒作逐片有符号 offset，也没有重算原连续修补。原 physical trial 不另乘 alpha，不投掉 mean，不增加非零 Fourier 槽的第二次倍数或平方根归一。

## 2. 联合范数及真实数值

令 $z_k(r)$ 为完整反射 sine/cosine 振幅。先对每个固定状态槽，在完整帽区取径向上界，再对所有状态求和：

$$
\mathcal J_{\sigma,q}(Z)
=\sum_k e^{4|j_k|\sigma}(4|j_k|)^q
\sup_{r\in[9/10,25/8]}|z_k(r)|.
$$

$q=0$ 时 mean 权为 1；$q=1,2$ 时 mean 导数准确为零，其本身仍保存在完整状态中。非零实振幅的一份绝对值就是相应两复 Fourier 系数绝对值之和。每片原 binary64 三次系数按精确有理数读取，在准确交段上计算四个精确 Bernstein 控制值；逐状态取全部原片最大值后，只加一次既成逐系数修补上界。

公开 native 实际授予下列完整 pair 的严格上界。表中十进制数向外截取，完整有向球保存在原输出。

| strip 宽度 $\sigma$ | $\mathcal J_{\sigma,0}$ | $\mathcal J_{\sigma,1}$ | $\mathcal J_{\sigma,2}$ |
| --- | ---: | ---: | ---: |
| $0$ | $<0.842592508277$ | $<3.447636241897$ | $<14.529967330435$ |
| $1/256$ | $<0.856171333333$ | $<3.504887089257$ | $<14.783259087745$ |
| $1/128$ | $<0.869975739133$ | $<3.563136711801$ | $<15.041357290884$ |
| $1/64$ | $<0.898277121481$ | $<3.682708600150$ | $<15.572390512334$ |

这些量的次序是逐系数径向 supremum 后再求和，能直接用于需要联合径向/Fourier 代数范数的合同；不是先求逐点 Wiener 和再对径向取最大值。原 $\xi$、$\zeta$ 两分量的各表以及 exact_complete_Z_mean_absolute_upper 也完整保留。它们均为经证明的上界，不是方向实际范数的下界。

原准确帽左端为 $9/10$，首消费原片编号 5484；末片编号 6143，末端 $25/8$。10 门核验实际覆盖无隙、无重复，全部 660 片恰好一次。没有以 binary64(0.9) 替换真实左端。

## 3. 实际过程、来源及可读收据

公开运行：

https://github.com/Rogerhu12/math-research-public/actions/runs/43674204314

工作流提交 eca7a66290928a339efeefc4e36f9ec843198efa。数学 source SHA256：

d909f2fc5eff54e42c3dcfe9355016f42c08cef1a6b04298cc62022fe6bf7d1e

worker SHA256：

4dd0af86d323ebfecb22060b80e2c5cee8da54d5696255fd560a0e52b87a09d2

13 项 input manifest SHA256：

6be86873a8ccce61cdea1860605650d3075430e2a593bf540a0d1e37438bd7a5

数学实际用时 4.9908802550000075 秒；该子进程包装层观测 10.000651038 秒。实际新增 660 片、复用此次数学前缀 0 片；旧 target、FFT、ODE、连续修补及帽残差重新计算总数为 0。此次实际工作是新 Bernstein/联合范数消费。

目录为 notes/cap_Z_joint_coefficient_ci/run-43674204314-1-complete-cap-Z-joint-coefficients/。下表路径相对于该目录：

| 输出 | 字节数 | SHA256 |
| --- | ---: | --- |
| native/complete-cap-Z-joint-coefficients.json.gz | 71737 | dd236bb30e17ed457a45bd38a24ff3188d896562e5e2e4189d5f3a5579cdc39c |
| process.json | 6397 | 61896c151fcd7593076195e0d320713f829a087cb9e3b597bbbd61b0c650ae61 |
| evidence/complete-cap-Z-joint-summary.json | 17371 | 67fa3c6664ab90a1dbbc91960b10f4f75c8f6372fee272ddca8f780f834efb86 |

本记录读的是上述公开小文本和 artifact 元数据，没有经连接器读取 gzip 或原 NPZ。新 artifact visible-exact-complete-cap-Z-joint-coefficients-43674204314-1 的 ID 为 14145860552、大小 4808747 字节、SHA256 digest 为：

770a94a207c735a493176c07092405f6a8aed916215a0543264c445c2613ab1f

它同时保留本次 native、实际过程和两个原 shard 的完整字节。

四次真实 pull 的 README 检查均有空差异。末次为 2026-11-15 03:52:19.088472 UTC，从 8adc3251a8fe2ee7bcbc5d6d8381631b1558141e 拉到 890caa1668f2442073f97b4fc319ea9aeae403a5。根 README 与本题 README SHA256 分别仍为 8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2、81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220；另外读过规则变更的提交仍记录为 ee26c0a65a2e63c15f2ccfba6714181584416542。

## 4. 此结果准确保留的范围

本次仅消费同固定物理 $\eta_0$、同原 $\nu_0$ 下的完整连续方向 $Z$，并保留全部 96 odd、96 nonmean even 和 1 个 even mean 状态。它可作为该显式参数方向在帽区的联合系数预算；对别的方向或改变本征参数没有自动转授。

intrinsic_beta_gamma_K_bounds_consumed 明确为 false。需要 $\beta,\gamma,K$ 的后续合同应另消费同帽区已成 intrinsic 闭行，不能由本记录凭空取得。

这次没有重新计算已成 5970 矩阵格、7908 adjoint 格、真实帽边界或 Green；完整无限 BVP 逆、未知 high 反馈、真正参数响应与非线性同域/Schur 仍不由本条结论授予。
