# R829：复用原 R702 系数所得 p=47 七项临界乘积

## 1. 准确结论与范围

只消费已登记的原 R702、p=47、B=10 系数，由 R770 的原阶乘/Wilson 公式得到

$$
(f_0g_6,f_1g_5,f_2g_4,f_3g_3,f_4g_2,f_5g_1,f_6g_0)
=(19,32,29,21,8,20,33)\quad\text{in }\mathbf F_{47},
$$

以及原未筛临界卷积

$$
\sum_{j=0}^{6}(-1)^j f_{6-j}g_j=16\ne0.
$$

这是一个已存在素数上、已存在原系数的有限消费者结论。它否定“所有允许的惰性素数在原 j=0 点的未筛临界卷积皆零”。它没有证明所有惰性素数的非零，也没有新求 primitive/Legendre 权，更不替代同一个可见标签的三个单位或 Serre 一致性。

## 2. 原公式和数据绑定

[R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md) 的 (770.9–10) 固定了原 f、g 及 A 的尺度。对本次 N=7，令

$$
0\le i\le6,\qquad j=6-i,\qquad h=6i+7,\qquad
Q_h=(h-2)(h-1)h(h+1)(h+2).
$$

原公式为

$$
f_i g_j=2^{(p-7)/2}Q_h A_{h-2}A_{p-h-2}\pmod p.
$$

消费者同时逐项核对原阶乘表达式；两组普通导数阶为 6i+4、6j+1，其和为 p−6。这里普通导数与 Taylor 系数的阶乘严格保留，原数据的 B=10 未作再归一。回执中的共同 Wilson 因子为 6，原 apolar 尺度 (6B)^5 为 40。

| i | j | h | f_i g_j（模 47） | 交替符号 |
|---:|---:|---:|---:|---:|
| 0 | 6 | 7 | 19 | +1 |
| 1 | 5 | 13 | 32 | −1 |
| 2 | 4 | 19 | 29 | +1 |
| 3 | 3 | 25 | 21 | −1 |
| 4 | 2 | 31 | 8 | +1 |
| 5 | 1 | 37 | 20 | −1 |
| 6 | 0 | 43 | 33 | +1 |

原输入为 [R702-prime47.json](../notes/R702-prime47.json)，Git blob
b1def2c3acd8462988dfd53d2df13750c6e30e67，文件 SHA256
22883dbbbb51e7821977218420bc7042239179665bbce808b4c9ec52aaeaba1a；
其已登记 arithmetic SHA256 为
94bc77b75d9cf7d9c98388709c7596878b72b82f30773523a0071973a6522443。
本次不重生 A、f、g 系列，不新增素数窗口。

公式文件的 Git blob 为 edb2c336e092cd7adf5370425c7447687c6326a8，
SHA256 为 736bb87b5047372334dee6049b5692b56a3ae9cf3cea9a3eec2bfb15c781f209。
请求同时绑定公式、旧输入、core 和 wrapper 的真实源身份，程序未预填七个答案。

## 3. 公开执行和完整回执

- 源提交：b2e7bde956eea3698c98d93a78b3f3a3544b983f。
- 公开 [run 43730863246](https://github.com/Rogerhu12/math-research-public/actions/runs/43730863246)，attempt 1，job 132862751167；AST、唯一七项计算、artifact 上传和冻结 verify 全部 success。
- [core](../scripts/sigma_reused_p47_critical_product.py)：4584 bytes，SHA256 d382bf4d698d6fdbaf2ab0bd47a868eeca109fb19921063e055f6362bf4bf6b0。
- [wrapper](../scripts/sigma_public_reused_p47_critical_product.py)：6048 bytes，SHA256 949096ea0b7ebe557fbb4382de25032dfc859422964b71187e88d6a7997df2b4。
- workflow SHA256：28a70645b99ffbc7d6a87fde26333737676f4538b16d49d17501ae07bcab4d71。
- 实际结果 canonical JSON：2419 bytes，SHA256 0f461cc4b01e75203e93b0001a26456973f894b200a52e9d06eadc09109d7fdd。
- 实际 manifest SHA256：d4c620ee5020ede4ebaf3461bbd98d8f1bf5b180189f449ae9ffb5c8b4afe42d。
- 一日 artifact 14168337214：3983 bytes；平台 ZIP SHA256 89ad97f0286e5148c22b69094738495a5139d5d89ed9ea5f631f1066c58ebd5c，expires 2026-11-16 15:36:57 UTC。

root 读取完整已结束 job log，解析其中实际结果，再按原 canonical 序列化作纯 IO SHA256，逐字匹配 RESULT_SHA256。冻结 wrapper 的源绑定和输出 verify 已成功。当前执行环境不可用，未另行下载 ZIP，因此上列 ZIP 摘要明确是平台报告值，不冒称本地重新核过全部 ZIP 字节。

可重算原始结果仅保一日活跃 artifact；Git 只保源码、参数、来源和本解释。没有在本地运行新的数学。

## 4. 对继续研究的约束

p=47 满足 p≡11 mod12。结合 [R826 原 companion 配对](R826-original-inert-companion-theta-CM-pairing.md) 的单位外因子，以及 [R828 原二部分奇偶性](R828-original-inert-two-primary-parity-and-old-source.md)，本例的真实六 oldform CM 值指定和非零。两条已证运输并未使该和成为与 p 无关的代数数；不能据一个非零实例推出全 p 单位。

后续必须证明一般惰性 p 的这个指定组合，或直接完成原同 primitive/Legendre 标签的配对。已经排除的普遍零猜想不再作为捷径重试，R702 的已成系数也不再重算。
