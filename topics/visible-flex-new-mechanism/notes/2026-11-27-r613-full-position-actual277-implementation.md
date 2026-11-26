# 真实277接受点后的完整实际位置目标：全部 N256 奇频与完整行 QR/SVD

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。
**新科学范围的源码、输入和费用约定；本文件不包含该新范围的运行结论。**
本地只做源文本、AST、JSON、哈希和原日志解析。

## 1. 由原自然终态确定的实质改变

[compact 原收据](2026-11-27-r606-compact-response-natural-stall.md)记录
run45882634760/job140125470693 在1130q中自然停滞。
该轮完整 `A_t/M` 目标与实际 η **都改善**，但停滞时细网 η 仍为
`4.378056141084893e-7`，两个直接位置差分也在同一量级，未过 `2e-9`。
因此本次保留全部实际高度参数，改用
[R613](../results/R613-actual-position-defect-jacobian-and-complete-objective.md)
已推导完整离解微分的 **实际位置残差**，不是延长旧目标、只改停止阈值或删掉难行。

输入固定为原自然终态中真实接受的 iteration277：1130q JSON为23328 bytes，
SHA `d47441a4089148d05fc6dc2e4cd487d074e2e2e9e2ed0b9feea325bfb4357113`；
振幅 `1e-5`、H `0.5188922483301639`、下一阻尼 `1e-14` 均原样保留。
原失败 trial 不进入输入。入口源码同时硬绑定原run/job/source、原raw日志
2126768-byte哈希、原FINAL90599-byte哈希和上述q哈希。

## 2. 真正完整的工作网位置目标

令原连续身份中的
$$
S(r,\theta)=\frac{W_*(r,\theta)}{\sqrt{E(r)}},\qquad
W_*=\Pi\{b(\Pi R)JT\}.
$$
本次离散实现严格使用原高度模型已有的 primitive 矩阵、turning根、
`b,N,u,E,R,Y_t,Wstar`，不另建观察场。
由原高度的偶性及π周期性，`S_x` 是奇频余弦类、`S_y` 是奇频正弦类。
N256 下采用全部可分辨正奇频
$$
\mathcal K=\{1,3,\ldots,127\},\qquad
S_x=\sum_{k\in\mathcal K}c_k\cos k\theta,
\quad S_y=\sum_{k\in\mathcal K}s_k\sin k\theta.
$$
全部128个实系数行按 `c_k/sqrt(2),s_k/sqrt(2)` 取 Parseval 单位，
再乘原非均匀径向梯形质量平方根、除原振幅。
没有人为加入高模逆平方抑制；两次 primitive 的滤波来自实际重构方程本身。
目标范数和原 `A_t/M` 范数不是同一个量，两个 merit 不作跨目标比例比较。

新入口以显式 `FullPositionHeight` 子类扩展原已发布1…63纯operator，
没有改动那个冻结源文件；它直接建立1…127全部行，
没有先算旧Jac再抛掉某些方向。
全部六个高度jets、隐turning根、非零残差下权重与phase导数、
原R602从属core系数及完整参数链均保留。
新Jac方法与已发布R613方法的AST一致，仅所引用本模块奇频常量扩展。

原950个工作半径全部保留；因此实际工作Jac为
**121600 × 1130**，精确元素数为137408000，
仅双精度J占 **1099264000 bytes**。
所有原核心端式和全部内口、原67结点与28个compact基函数、
原 canonical512 tanh mean和postforce均不变。
原2…88的完整 `A_t/M` 行仍同场读出；只是不再作为接受目标。

## 3. 完整行的实际内存组织

采用[已发布完整行QR/SVD](2026-11-27-r613-complete-position-row-memory.md)。
每次只生成一份完整J，以4096行为块累积全部列范数，
然后对增广矩阵 `[J/scales,residual]` 的全部行逐块做QR。
每个旧R与下一块全部原行一同进入下一QR；没有丢弃原数据行。
最终只对1130×1130的R做SVD，保留所有奇异方向，不形成正规方程。

在精确算术下该压缩保存全部最小二乘模型、梯度、阻尼步和预测下降；
末端原残差范数与压缩范数同时记录，浮点一致性不升格为严格逆证书。
必要的QR块、读取原行数、处理旧R行数、小SVD、方向求解和解析列全都计数。
这解决完整位置行数增长后的内存组织，未通过减少输出维数节省工作。

## 4. 实际接受、同一场细读数与所有未付缺口

每次新步骤须在同一1130q全场重新评估完整S，保留原实际/预测下降比、
8个阻尼尝试、9级回溯及完整六jet物理函数限制。
接受点、下一阻尼、最后拒绝试探和可能尚未完成的pending试探分开保存。
本次最多60个新迭代、5400秒科学clock，预留240秒给完整细读数；
clock或预算停止都不等于通过。

原细网 **1728 × 512**、全部半径和两组直接位置差分继续保留。
同场读取完整D谱0…128、原At/M2…88、核心全角方程、失号最高系数、
正域和真实几何。
R606与R615共享一次必要的系数/ρ遍历：R606原系数与界只形成一次，
已形成的 `G,G_e` 及其同场常数直接交给R615。
R615采用细网全部可分辨奇频1…255，正式尾从257起；没有调用旧R606门再重复计算一遍。

R615读数保留两次primitive滤波，但它仍是条件浮点观察：
径向系数、完整ODE/DtN、隐根、舍入以及半径连续区间误差须进一步认证。
固定点上的有限η、离散S小或某个有限参数空间满秩均不支付完整README标准。

[R617](../results/R617-finite-pre-tanh-poles-and-open-cap-rigidity.md)
已排除固定有限pre-tanh加有限post角带的非平凡准确开帽解，
但未给任何正误差下界。因此本次是实际响应求解，仍须继续角带增长、
独立无限post响应、真实强迫内尾与固定完整g的后继极限。
不能把本次有限1130q更贴合的目标称为已经存在准确根的完整函数空间。

## 5. 完整输入、成本和发布身份

完整stdin为 **67172 bytes**，SHA-256
`b21486214dbec1ddd6033a2a90218a91150d6e0b271a12b104aa6ed3203694c4`。
其中原31425-byte重建源逐字保留，完整原run3336.041297306秒与此前各层成本
分层继承；没有把原曾完成的工作从前史删去或列成本次新工作。

这次无新inner Riccati、无新内口、无旧方向/restriction检查，
但新进程必需的dense outer/inward、connector/core/H和postforce重建
仍按实际RHS/点数完整收费。所有新几何、position cache/导数、
Jac/QR/SVD、试探、compact基、canonical mean、同场系数与两个直接模板
均分别记账；重叠counter不相加成虚构总数。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `scripts/r613_full_position_height_20261127.py` | 24413 | `6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0` |
| `.github/workflows/visible-r613-full-position-20261127.yml` | 4183 | `207a369c6eb16cd41a1977f8432fa432bcad74a1210ea26910df8d7dab2b5706` |
| `computations/request-r613-full-position-20261127.json` | 79500 | `fb4a1835f1ebb31051ccc3e7b66257bf6db94b79a12ec53d12f6f270e4f2a19b` |

request绑定22个源码/workflow；Python3.12.14、NumPy2.3.5、SciPy1.17.0和Actions均固定。
沿用原height串行concurrency、一个公开ubuntu job、100分钟外部timeout。
运行入口先真实pull双仓规则、检查本会话QUEUE，规则差异不通过就停止新科学，
随后移除凭据、回到发布source并逐源验hash。只stdout，无raw/artifact/Release或Git数值表写入。

本地静态检查只验证解析、来源、维数计数、原接受q逐字身份与全部绑定一致；
没有本地计算S、ODE、几何、Jac、QR或优化。
