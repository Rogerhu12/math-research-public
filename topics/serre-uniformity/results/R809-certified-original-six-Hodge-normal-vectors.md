# R809：原六个清极 Hodge 函数的正规坐标已准确完成

## 1. 实际结论及适用范围

本结果落实[原 R809 证明](R809-original-normal-vectors-for-function-and-Hodge-inputs.md)的首个六目标 scope。原
$$
C_j=\theta U_j/\tau^4,\qquad 0\le j\le5
$$
均已在 R805 的同一正规整基上准确求出；系数域仍为原 $L=\mathbb Q(b,s)$，$s=1+2\zeta$，系数顺序仍为
$$
1,b,\ldots,b^6,s,sb,\ldots,sb^6.
$$
六目标共有 **84 个有理右端**，逐个通过全部 **1380 个原坐标**的准确代回；没有把选出的方阵解当成全关系证书。

令原正规基为 $d_a$，次数为 $0,1^{144},2^{127}$。共同 $S_5$ 的 1234 个指标 $(a,k)$ 满足 $0\le k\le5-\epsilon_a$。实际消费者准确认证每个目标的最高 $S_5$ 系数均为零，因此得到的函数确属原权四范围：
$$
C_j=\sum_{a=0}^{271}\sum_{k=0}^{4-\epsilon_a}c_{j,a,k}z^k d_a .
$$
这里并未改变 $\theta$、原 $U_j$、原 $\tau$ 或正规基。原 $A/B$ 不在本次 scope；原极理想、$D$、$\eta$、高度与任何全 $p$ 结论亦未由本次运行得到。

## 2. 真实执行与数学认证

- 原公开源提交：[91fbd81eb539c07f11e21116e71def91fdab5254](https://github.com/Rogerhu12/math-research-public/commit/91fbd81eb539c07f11e21116e71def91fdab5254)。
- 原公开运行：[43712427063](https://github.com/Rogerhu12/math-research-public/actions/runs/43712427063)，job 132806699613；compute 与冻结 wrapper 的完整 verify 均成功。
- 原 core SHA256：dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d。
- 原 wrapper SHA256：3616aac1b7d5dc373f0599c7ca023ef300f647fa204cd874a9655ca55b9607ea。
- 数学 core 实际耗时：13341.116785255 秒。

原 $S_5$ 的真实短矩阵为 1380 行、1234 列，来自 69 阶、每阶 20 个原坐标。所选 1234 阶 minor 在 $\ell=1000000007$ 上的实际行列式为 **29693114**。原 R809 的注入证明把完整 1380 坐标代回提升为原函数恒等式。全部六目标共用该原短矩阵、同一组选行和同一模逆；没有另外产生一个正规基。

重构仍按每一组保存的整数分子除以该组的 column denominator，再乘原目标 rational scale，最后按原 $S_5$ 指标映入 $(a,k)$。原 $82^{10}$ 缩放、$b/s$ 两块及 $B_{\mathrm{fld}}=\lambda b$ 的换基各保留原约定的一次应用；不额外清除或重复插入尺度。

## 3. 可续接的准确来源

以下为原成功运行的身份记录，均是复算入口的 SHA；大数组与机器证书不进入 Git 或 Release。

| 原文件 | 字节 | SHA256 |
|---|---:|---|
| full-outputs-manifest.json | 4044440 | 84908131c5a232d7accf5919a999c0bfbae4b2b632dcfc03c1e634494ef27b4e |
| p41-original-S5-normal-coordinate-certificate.json | 49515 | 8c117fa17d7ecf423307c850681fa6062f10534fbb2a444502c514bf9f0d9948 |
| R809-S5-basis-index.json.gz | 103410 | f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119 |
| R809-accepted-S5-short-minor.json.gz | 4678 | d631c02412ed53edae3a37c54eee3e8ebbe5d196ead69a9532767bc9f2cdea9b |
| R809-prime-1000000007-short-rank.json.gz | 4203 | 763b8c2dfc15bd3950dfbd2fca7f0c79c33a0f51cfffab1a9468fd8ff29a5e3f |
| R809-stage-manifest-be80c72a2878d432657a3f61.json.gz | 548056 | 23757c1106143c109b20cc78b6e21cb77d35279cc716882b7650232392e8ff64 |

六个原 normal-vector 索引各自记录其准确坐标分组、分母及目标尺度。其 SHA256 依次为：

| 目标 | 索引 SHA256 |
|---|---|
| C0 | 59ffa0cbaee44aa5c4f6cc027d13ecbd564a04b23bebd747ccba39b030220b37 |
| C1 | ba31b586ccfe77a7b1e7835a164d85fb9848284ce33d53e93fb04b3556a9022b |
| C2 | cefb9bbdb811fb203cb1266c4bee93bdce49eff9cab792f96f1928f0b057e1dc |
| C3 | d26f0f49974cb892039d4a490ab4febd52a07f8777698f96460d0df860452f4b |
| C4 | ae07b7732ee7e3db49c5e6cf55fdf80e8a0a4751aa1c3c8cb94629146a68414a |
| C5 | 1f268c7c0022578b3c723b97e178b11b92f388e990766626095496270e4666af |

原输入 bundle 为 R809-retained-producer-inputs.tar.gz，279221663 B，SHA256 13a9486fff42b5150a5177c49aaee8a1c6790776df886a0f9ed9f865ea46827f。原固定模逆为 7693407 B，SHA256 d61b9eb35866dfca066aa5bb22042465d68b5aacf4372f75be0908e5fa9115ca。它属于 $\ell=1000000007$，不能冒充 R827 所用 $\ell=1000000753$ 的模逆。

原一日 artifact 14168728276，545778174 B，GitHub 平台 ZIP digest 为 1ec83d6c910e119bfc9f82b35520b493a235b8dea1ddba247b60e46f00c8a550，到期时间 2026-11-16 15:52:48 UTC。平台 digest 与文件级准确认证各自说明，不混称新的全 ZIP 下载重哈希。

## 4. 本次小来源读取的明确范围

原成功 job 已执行冻结 wrapper 的完整输出、原输入 bundle 与全关系检查。为把真实来源交给 R827，随后公开运行 [43733430148](https://github.com/Rogerhu12/math-research-public/actions/runs/43733430148)，源提交 [1674f17b3efcb6010cd69608cfcb70941c24f116](https://github.com/Rogerhu12/math-research-public/commit/1674f17b3efcb6010cd69608cfcb70941c24f116)，job 132870711858，只执行来源 IO。

该任务以原 run/source/artifact 身份固定完整 manifest 与证书，再以 HTTP Range 精读 **16 个原成员，共 4798730 B**；实际传输 2301527 B、54 次 Range。它逐成员复核原 manifest SHA，并打印 R809_SOURCE_IO_REVIEW_SUMMARY，其中已给全真的 R827 producer 配置。1234 条原 $S_5$ 大行、12 个大坐标组、旧输入 bundle 和模逆没有被重复下载或重算。

小 IO 一日 artifact 为 14168779933，4820909 B，平台 ZIP digest ea95ac158336bf9ac640e82cbdc406b26fd160b4a51680b6038f649dc495fe6c，到期 2026-11-16 16:05:02 UTC。小任务不声称重新核过未下载的大组或整个原 ZIP；其关系正确性引用前述原成功运行的完整 verify。

## 5. 紧接的消费者

R827 可立即消费上述原 $S_5$ 行来源、实际 basis/minor 身份和已有 R787/R824 真模方向，求同一原 canonical $B$ 在其固定剩余域上的正规坐标。新的辅助素数不复用不相同的旧模逆；原 $Q$ 行与已成坐标不重算。

[两图终止判据](R827-original-global-modular-surjectivity-and-derivative-termination.md)仍必须实际完成整个有限图的多项式生成检验及无穷远 rank272。首请求 $q=4$ 只是请求参数；本结果没有提前断言该检验成功或原 $D$ 约化。R787 的原准确 A/B 和 R824 的其它准确五次关系继续各自恢复已成前缀，后继只能绑定实际完成的关系来源。
