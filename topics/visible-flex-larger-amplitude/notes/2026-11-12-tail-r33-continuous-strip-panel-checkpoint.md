# R33 连续条带面板的持久检查点

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。

## 实际状态与提交范围

2026-11-12 会话50588已正式退出0：全部 cell12 至23，共30792个真实源面板；44.884934807秒，峰 RSS176984KiB。没有新 ODE 或径向数值求积。最初一次因分组列文件不含独立 input_hashes 字段而退出1，没有任何结果；现改为验证已支付 density manifest 绑定的列文件及 ready 两个准确 SHA。数学源未改。

本次只提交源脚本、完整 summary、本说明及 cell012/cell013 两包。**cell014 至 cell023 的十个完整面板包未提交，只保留于当前执行器；不能说它们已经持久保全。** 下表和 summary 保存十包的原始 SHA。如执行器丢失，必须用下面命令真实重做，先核对输入/源 SHA，再核对下方数学负载 SHA，不能把当前本地文件当成还存在。原始文件 SHA 校验本次保存件；重跑耗时和峰内存会变化，不能要求整个输出文件 SHA 相同。

主研究解和原始场不受此派生数据选择影响。exact_closure 已获得全部十二个本地面板，正在按有序位置结合真实带符号列；这不是全频低反馈已经通过的声明。

## 完整重建命令

在仓库课题目录运行。所需 python-flint 与固定源都和当前 R33/R26 账本一致。工具的默认范围是12..23、log-span=1/16、192-bit Arb。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/tail_r33_continuous_strip_panels.py --density notes/2026-11-12-tail-r33-plateau2-density-window.json.gz --columns notes/2026-11-12-closure-real-linear-q003-low46-recovered-columns-01-08.json.gz --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json --out-prefix notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels
```

端口半径、物理 V 和连续条带必须使用下面这些准确输入，禁止以新的参考或其它条带替换后冒称同一包。

| 输入 | SHA-256 |
|---|---|
| notes/2026-11-12-tail-r33-plateau2-density-window.json.gz | 0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9 |
| notes/2026-11-12-closure-real-linear-q003-low46-recovered-columns-01-08.json.gz | 673ba350f50d2c7d15b633487261dcc7cc636287f6da74a5ecd161794e9bf4b1 |
| notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |

源工具及被读取的辅助源 SHA：

| 源 | SHA-256 |
|---|---|
| tail_r33_continuous_strip_panels.py | 169a678f692b7a783ae8cb53b36ad2183e01929749cfe1692b5023ebb00be395 |
| tail_r33_middle_ordered_physical.py | ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e |
| closure_real_head_source_enclosure.py | 97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47 |
| closure_real_linear_head_enclosure.py | 1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e |

## 全部原始输出 SHA

| cell | 本次提交 | 文件 | 字节 | SHA-256 |
|---:|---|---|---:|---|
| 12 | 是 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell012.json.gz | 1434563 | d0dc6791001a1668afa2f9442bbefbe7e6644e73b0b753943df5a9bc12258181 |
| 13 | 是 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell013.json.gz | 1502615 | 7397ebc436ae5c4cd396ae2e6d5d27c4f2b45e17fae5e75f94eb0acb9e95dc22 |
| 14 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell014.json.gz | 1564942 | 8c60a814743342019cb9ed57c44b5c6af6322582b6858e10809c23d3a43474f7 |
| 15 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell015.json.gz | 1700818 | ff3edff52b900aeca5533ebd81910c958522577514c82bfca67e7d9df849ebce |
| 16 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell016.json.gz | 1776623 | 4d7ee6c8264f5561f593f2a64663825332972eba05354cbc9bc668189b5d37e1 |
| 17 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell017.json.gz | 1837077 | 99a4469f1ef5404616995132507b19c8ac92ccd079496e8000c123bcb3196e43 |
| 18 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell018.json.gz | 1985325 | 25ed4622a6df7c74d696b3aa74ca178d91e154696b4cad9ddb043d1a1c7725bc |
| 19 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell019.json.gz | 2079646 | d2666f7276224dab13277a7892dc40ef9175507b689857101641ad814d028c48 |
| 20 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell020.json.gz | 2151524 | 7c19c94f80e9dedd04c8c6acfb5ef0159318d10082e4429bed518b66c6f47904 |
| 21 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell021.json.gz | 2266141 | 1861bd9b58f540be5152fcb8f11d67dc1ce5383aee59b6e41f0487a6f8ad7283 |
| 22 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell022.json.gz | 2337200 | ebc8ef89f637a5c01345e229bf1f9b5e07189ec224087fdf94c079012ab749b4 |
| 23 | 否，丢失后重算 | notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell023.json.gz | 2404524 | 2e9c84d22cd7b1db46b57b7217d0201b345fd7f6e24fe93b98a7a8a824f0dd85 |

cell12 的真实条带端点最大区间宽小于0.00005833；cell13小于0.000000001069。每一面板都保存源坐标有理端点、r/w/V/V_over_w、cV/w 材料、canonical 源积分、b_tau 前缀/总量和真实 tau 两端。完整数学证明为 R33 第15节。

## 可重算的数学负载 SHA

将每个面板 JSON 顶层的 elapsed_seconds 和 peak_RSS_KiB 两字段删去，其余内容以 sort_keys=True、separators=(comma,colon) 的 JSON UTF-8 编码取 SHA-256。运行时元数据不参与此可重复性比较，数学字段一项不删。

| cell | 数学负载 SHA-256 |
|---:|---|
| 12 | 95e372eb96795faee241d9f3e5eabeed412696e04de7c32562c7a497f127229a |
| 13 | f176684306ba1bc58d8910cdeb11c878bbc3eea0ef57dc7c2c0673cb2847939c |
| 14 | 8918c5515c040479f26948b141baab5bd777f03fe8683303609aad5b52df4da7 |
| 15 | df83867ab9965a823ce966e51742b5d8392c29c5c8bd743c49de412b88e9a0c2 |
| 16 | 3b5f7b75623be8d5eb87f379917a6b9426e2eebd849588d6ed0d9461375c5e8a |
| 17 | ff1090ea4c444785e272f88f119f000114a0072259ae67bc1215a09eece75ec7 |
| 18 | a5974fccf21e66cde355a2279c1db547203dbca93df956fe54921f9ea19eed4c |
| 19 | a0a23ae0c9617dc9736540155f8022d366e6828bb119b1772bda9281a26409fc |
| 20 | 1662e0dbabc25842236e198a784a0d0d9467edcc04058aae5477a534db212b9f |
| 21 | 8107c84d7236f5a6211c93c61da8a87b5f3d3db3433794271d522bf0f15f16da |
| 22 | c9cf625f84e8d51b349919fd6203f6001e5d028639aa3039ef98190c45889804 |
| 23 | f56fff706337209e94c022482b4b9a8a873f82f42c41c1c2a3825fe2cdb5cf29 |
